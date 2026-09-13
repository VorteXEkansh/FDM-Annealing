"""Stage 9 document, provenance, thermal verification and production-gate checks."""
from pathlib import Path
import csv, hashlib, json, re, subprocess, sys
from pypdf import PdfReader
import pdfplumber

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'output/pdf/Constrained-Annealing-2026-DRAFT.pdf'

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    checks=[]
    def check(name, condition):
        assert condition,name
        checks.append({'check':name,'status':'pass'})
    manifest=json.loads((ROOT/'data/source/manifest.json').read_text())
    check('Base PDF hash preserved',digest(ROOT/'data/source'/manifest['source_name'])==manifest['sha256'])
    check('Complete 24-page base source',len(PdfReader(ROOT/'data/source'/manifest['source_name']).pages)==24)
    audit=(ROOT/'docs/base_paper_audit.md').read_text(encoding='utf-8')
    for label in ['KEEP','KEEP BUT REWRITE','REPLACE','DELETE','MOVE TO SUPPLEMENT','REUSE AS LITERATURE CONTEXT']:
        check('Disposition '+label,label in audit)
    check('All methods subsections audited',all('§5.'+str(i) in audit for i in range(1,20)))
    check('All discussion subsections audited',all('§6.'+str(i) in audit for i in range(1,9)))
    check('Figures inventoried',all(re.search(r'\| '+str(i)+r' / ',audit) for i in range(1,10)))
    check('Tables inventoried',all(re.search(r'\| '+str(i)+r' / ',audit) for i in range(1,12)))
    check('Appendix tables inventoried','| A1 / 24' in audit and '| A2 / 24' in audit)
    catalog=json.loads((ROOT/'data/literature/base_reference_catalog.json').read_text(encoding='utf-8'))
    check('All 50 base references cataloged',[r['base_id'] for r in catalog]==list(range(1,51)))
    source=(ROOT/'manuscript/current.md').read_text(encoding='utf-8')
    refs=json.loads((ROOT/'data/literature/verified_sources.json').read_text(encoding='utf-8'))
    citations=set(map(int,re.findall(r'\[(\d+)\]',source)))
    check('Retained references and citations correspond',citations==set(range(1,41)))
    check('Retained DOIs present',all(r['doi'] in source for r in refs))
    check('Objectives numbered 1 through 5',re.findall(r'^(\d)\. ',source,re.M)==['1','2','3','4','5'])
    check('Equations numbered consecutively',re.findall(r'\((\d+)\)\s*$', '\n'.join(l for l in source.splitlines() if l.startswith('EQ:')),re.M)==list(map(str,range(1,21))))
    check('No duplicated or result figures',source.count('FIGURE:')==1 and source.count('CAPTION: Figure 1.')==1)
    for path in ['results/run_registry.csv','data/literature/property_registry.csv','data/literature/validation_registry.csv']:
        with (ROOT/path).open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
        check('No invented data in '+path,len(rows)==0)
    check('No dummy ANSYS binaries',not any((ROOT/'models/ansys').glob('*.rst')) and not any((ROOT/'models/ansys').glob('*.wbpj')))
    check('One primary research question',source.count('<b>Primary research question.</b>')==1)
    check('Five secondary research questions',re.findall(r'^SQ([1-5])\.',source,re.M)==list('12345'))
    check('Four testable propositions',re.findall(r'^H([1-4]) —',source,re.M)==list('1234'))
    check('Scope and non-claims explicit',all(t in source for t in ['FREE','GAP','traction-free','Gravity is omitted','discrete-element','Intended contribution','Results status.']))
    material_files=['material/pla_properties.csv','material/property_sources.csv','material/uncertainty_ranges.csv','material/fixture_properties.csv']
    before_material={p:digest(ROOT/p) for p in material_files}
    subprocess.run([sys.executable,str(ROOT/'scripts/build_material_database.py')],check=True,cwd=ROOT,capture_output=True)
    check('Material database reproducible byte-for-byte',before_material=={p:digest(ROOT/p) for p in material_files})
    with (ROOT/'material/pla_properties.csv').open(encoding='utf-8-sig') as f: pla=list(csv.DictReader(f))
    with (ROOT/'material/property_sources.csv').open(encoding='utf-8-sig') as f: prop_sources=list(csv.DictReader(f))
    with (ROOT/'material/uncertainty_ranges.csv').open(encoding='utf-8-sig') as f: uncertainty=list(csv.DictReader(f))
    with (ROOT/'material/fixture_properties.csv').open(encoding='utf-8-sig') as f: fixture=list(csv.DictReader(f))
    check('Expected property record counts',len(pla)==96 and len(prop_sources)==11 and len(uncertainty)==16 and len(fixture)==18)
    required=['value','unit','temperature_C','source_key','doi_or_reference','PLA_formulation','confidence_relevance','how_used_in_ANSYS','source_locator']
    check('Every PLA number has units, temperature, source, formulation, confidence and ANSYS treatment',all(all(r[k] for k in required) for r in pla))
    check('All property sources have immutable evidence hashes',all(re.fullmatch(r'[0-9a-f]{64}',r['sha256']) for r in prop_sources))
    prony_k=[r for r in pla if r['property_symbol']=='kᵢ']
    prony_t=[r for r in pla if r['property_symbol']=='τᵢ']
    check('Complete 23-pair Prusament Maxwell spectrum',len(prony_k)==len(prony_t)==23 and {r['component'] for r in prony_k}=={r['component'] for r in prony_t})
    k0=float(next(r['value'] for r in pla if r['property_symbol']=='E_∞'))
    e0=float(next(r['value'] for r in pla if r['property_symbol']=='E_0'))
    check('Prusament reference modulus arithmetic',abs(k0+sum(float(r['value']) for r in prony_k)-e0)<1e-9 and e0==1691.594)
    check('No cross-formulation comparator admitted',all(r['compatibility_status']!='admissible_within_source_domain' for r in pla if r['dataset_role']=='comparator'))
    check('Missing bounds are explicit rather than zero-filled',all((r['lower']==r['upper']=='') and r['status']=='no bound invented' for r in uncertainty if r['range_type']=='unresolved evidence gap'))
    check('No probability distributions assigned',all(r['probability_model']=='none' for r in uncertainty))
    check('Fixture table brackets planned range',set(r['temperature_C'] for r in fixture)=={'20','100','200'} and set(r['property_symbol'] for r in fixture)=={'ρ','c_p','k','α','E','ν'})
    manifest4=json.loads((ROOT/'material/build_manifest.json').read_text(encoding='utf-8'))
    check('Material output hashes recorded',all(digest(ROOT/x['path'])==x['sha256'] for x in manifest4['outputs']))
    check('Material evidence hashes recorded',all(digest(ROOT/x['path'])==x['sha256'] for x in manifest4['evidence']))
    equation_map=list(csv.DictReader((ROOT/'docs/equation_implementation_map.csv').open(encoding='utf-8')))
    check('Every governing equation has an implementation target', [r['equation'] for r in equation_map]==list(map(str,range(1,21))))
    test_report=json.loads((ROOT/'docs/stage_05_constitutive_tests.json').read_text(encoding='utf-8'))
    check('All 38 constitutive tests passed',test_report['passed'] and test_report['tests_run']==38 and all(r['status']=='pass' for r in test_report['tests']))
    check('Constitutive test input and code hashes match',all(digest(ROOT/p)==h for p,h in test_report['sha256'].items()))
    check('Irreversibility and crystallization gaps explicitly retained',all(t in source for t in ['No bulk annealing-induced irreversible-strain relation is parameterized','No crystallization kinetic equation','tangent-versus-mean']))
    reference_path=ROOT/'material/constitutive_reference.json'
    reference_before=digest(reference_path)
    subprocess.run([sys.executable,str(ROOT/'scripts/build_constitutive_reference.py')],check=True,cwd=ROOT,capture_output=True)
    check('Constitutive reference conversion reproducible byte-for-byte',digest(reference_path)==reference_before)
    before=digest(PDF)
    subprocess.run([sys.executable,str(ROOT/'scripts/build_manuscript.py')],check=True,cwd=ROOT,capture_output=True)
    check('PDF reproducible byte-for-byte',digest(PDF)==before)
    reader=PdfReader(PDF)
    check('Complete manuscript page count matches reviewed stage record',len(reader.pages)==json.loads((ROOT/'docs/stage_09_pdf_review.json').read_text())['page_count'])
    review=json.loads((ROOT/'docs/stage_09_pdf_review.json').read_text())
    check('All pages visually reviewed for the current PDF hash',review['visual_status']=='pass' and review['reviewed_pdf_sha256']==digest(PDF) and review['reviewed_pages']==list(range(1,len(reader.pages)+1)))
    text='\n'.join(p.extract_text() for p in reader.pages)
    for pattern in [r'F3498',r'sqrt\s*\(',r'epsilon_ann',r'Delta L',r'95 C',r'3 x 3',r'130 physical specimens',r'\bTODO\b',r'\bTBD\b',r'\ufffd']:
        check('Forbidden manuscript pattern absent: '+pattern,not re.search(pattern,text))
    check('Thermal evidence boundary explicitly reported','six structural/contact ANSYS reference cases' in source and 'no production PLA coupon result' in source)
    check('Accepted thermal error values reported',all(v in text for v in ['0.005180700 °C','0.001700533%','0.157660518%']))
    check('Thermal choices typeset',all(v in text for v in ['80 °C','95 °C','110 °C','30 min','60 min','90 min']))
    check('Mathematical symbols preserved',all(c in text for c in 'Δεσρ∂∇√∑∈⊥'))
    check('All pages contain substantive text or a continued coefficient table',all(len(p.extract_text())>500 for p in reader.pages))
    geometry=json.loads((ROOT/'docs/stage_07_geometry_checks.json').read_text())
    check('Geometry preprocessing checks passed',geometry['passed'] and geometry['count']==17 and all(r['status']=='pass' for r in geometry['checks']))
    check('Geometry evidence remains construction-only',all(t in source for t in ['geometry-only Mechanical APDL build','contains no element type, mesh, material, load, analysis type or solve command','This is a sampling decision, not a prediction that contact cannot occur']))
    thermal=json.loads((ROOT/'docs/stage_08_thermal_checks.json').read_text())
    check('Stage 8 thermal verification checks passed',thermal['passed'] and thermal['count']==36 and thermal['maximum_absolute_error_C']==0.0051807)
    check('Published thermal comparison equals accepted run',digest(ROOT/'verification/thermal_verification.csv')==digest(ROOT/'simulation/verification/stage08_attempt_05/comparison.csv'))
    check('Production thermal gaps remain explicit',all(t in source for t in ['Compatible temperature-dependent Prusament functions remain absent','Radiation is omitted from this benchmark','no production PLA coupon solution']))
    structural=json.loads((ROOT/'docs/stage_09_structural_checks.json').read_text())
    check('Stage 9 comparisons pass',structural['passed'] and structural['comparison_count']==114)
    check('Stage 9 source hashes match',all(digest(ROOT/p)==h for p,h in structural['source_hashes'].items()))
    check('Structural evidence limits declared','synthetic eigenstrain' in source and 'non-isothermal clock' in source)
    check('All structural comparisons admitted',all(r['passed']=='True' for filename in ['structural_verification.csv','contact_verification.csv'] for r in csv.DictReader((ROOT/'verification'/filename).open())))
    with pdfplumber.open(PDF) as pdf:
        bad=[]
        for n,p in enumerate(pdf.pages,1):
            for c in p.chars:
                if c['text'].strip() and (c['x0']<48 or c['x1']>p.width-46 or c['top']<30 or c['bottom']>p.height-18): bad.append(n)
        check('All text lies inside page safety bounds',not bad)
    report={'stage':9,'date':'2026-09-13','checks':checks,'count':len(checks),'pdf_sha256':digest(PDF),'manuscript_sha256':digest(ROOT/'manuscript/current.md'),'material_manifest_sha256':digest(ROOT/'material/build_manifest.json'),'geometry_manifest_sha256':digest(ROOT/'simulation/geometry/stage07_plate_gap/manifest.json'),'thermal_manifest_sha256':digest(ROOT/'simulation/verification/stage08_attempt_05/manifest.json'),'scope':'Document, source, property, environment, geometry and genuine MAPDL plane-wall thermal verification integrity. No production PLA coupon solution or physical validation.'}
    (ROOT/'docs/integrity_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} integrity checks passed; PDF SHA-256 {digest(PDF)}')

if __name__=='__main__': main()
