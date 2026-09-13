"""Stage 7 geometry evidence and calculation checks."""
import csv, hashlib, json, re, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
RUN=ROOT/'simulation/geometry/stage07_plate_gap'
def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    checks=[]
    def check(name,ok): assert ok,name; checks.append({'check':name,'status':'pass'})
    d=json.loads((ROOT/'geometry/geometry_definition.json').read_text()); m=json.loads((RUN/'manifest.json').read_text())
    s=d['specimen']; f=d['fixture']; out=(RUN/'mapdl_geometry.out').read_text(errors='replace'); deck=(RUN/'geometry.dat').read_text()
    decision=(ROOT/'docs/geometry_decision.md').read_text(encoding='utf-8')
    check('Trofimov geometry source and DOI recorded',all(x in decision for x in ['60 mm','10 mm','4 mm']) and '10.1016/j.addma.2022.102693' in d['specimen']['source'])
    check('Specimen dimensions are 60 by 10 by 4 mm',(s['length_mm'],s['width_mm'],s['thickness_mm'])==(60.0,10.0,4.0))
    check('Fixture margin arithmetic',f['plate_length_mm']==s['length_mm']+2*f['planar_margin_each_side_mm'] and f['plate_width_mm']==s['width_mm']+2*f['planar_margin_each_side_mm'])
    check('Derived geometry calculations exact',m['derived_calculations']=={'specimen_volume_mm3':2400.0,'nominal_contact_area_each_face_mm2':600.0,'length_to_thickness':15.0,'width_to_thickness':2.5,'length_to_width':6.0,'fixture_plate_volume_each_mm3':7000.0})
    with (RUN/'gap_design.csv').open(newline='',encoding='utf-8') as fp: rows=list(csv.DictReader(fp))
    check('Five normalized gap levels',len(rows)==5 and [float(r['total_gap_mm']) for r in rows]==[0,0.01,0.02,0.04,0.08])
    check('Gap equations reproduced',all(abs(float(r['gamma'])-float(r['total_gap_mm'])/4.0)<1e-12 and abs(float(r['plate_separation_mm'])-(4.0+float(r['total_gap_mm'])))<1e-12 for r in rows))
    with (ROOT/'geometry/candidate_clearance_audit.csv').open(newline='',encoding='utf-8') as fp: candidates=list(csv.DictReader(fp))
    check('All five prompt candidate gaps explicitly evaluated',[float(r['candidate_total_gap_mm']) for r in candidates]==[0,0.025,0.05,0.1,0.2])
    check('Candidate gap normalization is exact',all(abs(float(r['gamma_for_h0_4mm'])-float(r['candidate_total_gap_mm'])/4.0)<1e-12 for r in candidates))
    check('Candidate dispositions retain coverage without unsupported exclusion',[r['disposition'] for r in candidates]==['retained','represented within normalized screen','represented within normalized screen','deferred','deferred'])
    check('Geometry MAPDL execution succeeded',m['execution']['executed'] and m['execution']['returncode']==0)
    check('MAPDL build and volume count verified',all(x in out for x in ['RELEASE= 2026 R1','BUILD= 26.1','STAGE7_TOTAL_GAP_MM=0.040000000','STAGE7_GAMMA=0.010000000','TOTAL NUMBER OF VOLUMES SELECTED =     3']))
    check('MAPDL output has no warning or error','*** ERROR' not in out and '*** WARNING' not in out)
    check('APDL deck contains no field analysis or mesh command',not re.search(r'(?im)^\s*(solve|antype|et|mat|mshape|mshkey|vmesh|amesh|nsel|d|f|sf|sfe|bfe)\s*[,\n]',deck))
    check('Saved database exists and is hashed',(RUN/'stage07_plate_gap.db').exists() and m['output_sha256']['stage07_plate_gap.db']==h(RUN/'stage07_plate_gap.db'))
    check('All raw output hashes match',all(h(RUN/name)==value for name,value in m['output_sha256'].items()))
    check('Source/input/table hashes match',m['source_sha256']==h(ROOT/'geometry/geometry_definition.json') and m['input_sha256']==h(RUN/'geometry.dat') and m['gap_table_sha256']==h(RUN/'gap_design.csv'))
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_geometry.py'); result=unittest.TextTestRunner(stream=sys.stderr,verbosity=1).run(suite)
    check('Seven geometry unit tests pass',result.wasSuccessful() and result.testsRun==7)
    report={'stage':7,'date':'2026-09-13','passed':True,'checks':checks,'count':len(checks),'scope':'Geometry calculations and geometry-only MAPDL preprocessing; no mesh or field solution.','sha256':{'definition':h(ROOT/'geometry/geometry_definition.json'),'builder':h(ROOT/'scripts/build_geometry.py'),'mapdl_input':h(RUN/'geometry.dat'),'mapdl_output':h(RUN/'mapdl_geometry.out'),'database':h(RUN/'stage07_plate_gap.db')}}
    (ROOT/'docs/stage_07_geometry_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f'{len(checks)} geometry checks passed')
if __name__=='__main__': main()
