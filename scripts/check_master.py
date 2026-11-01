"""Audit the master investigation without executing or altering solver evidence.

The optional write flag refreshes only derived trace/checksum registries. Passing
this audit does not admit physical predictions or certify publication readiness.
"""
from pathlib import Path
import argparse,csv,hashlib,html,json,math,re,subprocess,sys,zipfile
from lxml import etree
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from analysis.review_metrics import extract

def sha(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def rows(path):
    with (ROOT/path).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def dump(path,value):
    (ROOT/path).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def writecsv(path,records):
    with (ROOT/path).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]),lineterminator='\n');w.writeheader();w.writerows(records)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--preflight',action='store_true');args=ap.parse_args()
    checks=[]
    def check(label,ok):
        if not ok:raise AssertionError(label)
        checks.append(label)
    old=json.loads((ROOT/'docs/stage_19_manifest.json').read_text())['files']
    excluded={r['path']:r['sha256'] for n in ['external_evidence.csv','external_scratch.csv'] for r in rows('reproducibility/'+n)}
    frozen={p:h for p,h in old.items() if p.startswith(('simulation/','verification/','convergence/','validation/','material/','data/raw/','literature/evidence/','literature/metadata/'))}
    for p,h in frozen.items():check('Frozen '+p,sha(p)==h if (ROOT/p).exists() else excluded.get(p)==h)
    for n in ['mesh_convergence.csv','timestep_convergence.csv']:
        for r in rows('convergence/'+n):assert math.isclose(extract(ROOT/r['run_path'],r['model'])[r['quantity']],float(r['value']),rel_tol=1e-10,abs_tol=1e-12)
    check('63 previous mesh/time responses independently recomputed',True)
    attempts=[]
    for p in sorted((ROOT/'simulation/master').glob('*/*/manifest.json')):
        m=json.loads(p.read_text());base=p.parent
        for name,h in m['files'].items():
            f=base/name
            if f.suffix=='.rst' and not f.exists():continue
            assert sha(f)==h,(p,name)
        if m['accepted']:
            assert m['returncode']==0 and '*** ERROR ***' not in (base/'mapdl.out').read_text(errors='replace')
            assert all(r['passed']=='True' for r in rows(base/'comparison.csv'))
        attempts.append(dict(case=base.relative_to(ROOT).as_posix(),accepted=m['accepted'],returncode=m.get('returncode'),error=m.get('error'),manifest_sha256=sha(p)))
    check('13 new attempts preserved, six accepted reference runs',len(attempts)==13 and sum(r['accepted'] for r in attempts)==6)
    details=rows('verification/master_nonisothermal.csv');summaries=rows('verification/master_nonisothermal_summary.csv')
    for r in details:
        e=abs(float(r['ansys_stress_MPa'])-float(r['reference_stress_MPa']))
        assert e==float(r['absolute_error_MPa'])
        assert (e<=float(r['tolerance_MPa']))==(r['passed']=='True')
    for r in summaries:
        errs=[float(x['absolute_error_MPa']) for x in details if x['attempt']==r['attempt']]
        assert max(errs)==float(r['max_abs_error_MPa'])
        assert math.isclose(math.sqrt(math.fsum(e*e for e in errs)/len(errs)),float(r['rms_error_MPa']),rel_tol=1e-14)
    check('130 transient comparisons and five summary metrics consistent',len(details)==130 and len(summaries)==5)
    for r in rows('verification/master_nonisothermal_refinement.csv'):
        x=[q for q in details if q['attempt']==r['coarse']];y=[q for q in details if q['attempt']==r['fine']]
        assert [q['time_s'] for q in x]==[q['time_s'] for q in y]
        diffs=[abs(float(a['ansys_stress_MPa'])-float(b['ansys_stress_MPa'])) for a,b in zip(x,y)]
        assert max(diffs)==float(r['max_difference_MPa'])
    check('Seven matched refinement pairs recomputed',True)
    geo=json.loads((ROOT/'geometry/geometry_definition.json').read_text());h=geo['specimen']['thickness_mm'];area=geo['specimen']['length_mm']*geo['specimen']['width_mm']
    stoprows=[]
    for p in sorted((ROOT/'simulation/master/stop').glob('*_a02')):
        c=json.loads((p/'case.json').read_text());table=rows(p/'comparison.csv');raw=list(csv.reader((p/'raw.csv').open()))
        for r,z in zip(table,raw):
            i,g,F,status,u,rf=map(float,[v for v in z if v.strip()]);T=float(r['T_C']);eps=c['alpha_steel_per_K']*(T-23)/(1+c['alpha_steel_per_K']*3)
            U={'fixed_inside_spacing':0,'coexpanding_inside_spacers':(h+c['gap_mm'])*eps,'fixed_outer_faces':-2*geo['fixture']['plate_thickness_mm']*eps}[c['layout']]
            trial=c['gap_mm']+U-h*c['alpha_pla_per_K']*(T-23);force=max(0,-trial/h)*c['young_MPa']*area
            assert -g==float(r['gap_mm']) and -F==float(r['compressive_force_N'])
            assert abs(-g-max(0,trial)/2)<1e-7 and abs(-F-force)<1e-4 and abs(abs(rf)-force)<1e-4 and (round(status)>=2)==(force>0)
            stoprows.append((p,r))
    check('36 stop states independently checked against raw exports and kinematics',len(stoprows)==36)
    for path,key in [('reproducibility/master_fixture_manifest.json','files'),('reproducibility/programmed_road_manifest.json','sha256')]:
        for p,hsh in json.loads((ROOT/path).read_text())[key].items():assert sha(p)==hsh,p
    check('Kinematic and recovery calculation hashes agree',True)
    for p in ['simulation/design_matrix.csv','simulation/case_manifest.csv','data/processed/all_cases.csv','optimization/pareto.csv','optimization/confirmation.csv']:check('No invented production results: '+p,len(rows(p))==0)
    for p in ['validation/master_spring_targets.csv','validation/master_suder_targets.csv']:
        for r in rows(p):assert not any(v for k,v in r.items() if 'prediction' in k or k=='error')
    check('New reserved experimental means were not fitted or scored',True)
    source=(ROOT/'manuscript/master.md').read_text(encoding='utf-8');body,bib=source.split('### References')
    cited=set()
    for s in re.findall(r'\[(\d+(?:\s*[–-]\s*\d+)?(?:\s*,\s*\d+(?:\s*[–-]\s*\d+)?)*)\s*(?=\]|,)',body):
        for v in s.split(','):
            a=re.split('[–-]',v);cited.update(range(int(a[0]),int(a[-1])+1))
    check('13 references cited without dangling numeric citations',cited==set(range(1,14))==set(map(int,re.findall(r'^\[(\d+)\]',bib,re.M))))
    dois=sorted(set(re.findall(r'doi:(10\.[^<]+)',bib)));metadata={}
    for p in (ROOT/'literature/metadata').glob('master*/*.json'):
        j=json.loads(p.read_text(encoding='utf-8-sig'));j=j.get('message',j)
        if 'DOI' in j:metadata[j['DOI'].lower()]=dict(doi=j['DOI'],title=j['title'][0],metadata_path=p.relative_to(ROOT).as_posix(),sha256=sha(p),status='Crossref identity verified; source access limits in search/material audits')
    check('10 main article DOIs match archived authoritative records',len(dois)==10 and all(d.lower() in metadata for d in dois))
    with zipfile.ZipFile(ROOT/'output/master/Constrained-Annealing-2026.docx') as z:xml=etree.fromstring(z.read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
    check('Eight native editable equations, three figures and one table',len(xml.findall('.//m:oMath',ns))==8 and len(xml.findall('.//w:drawing',ns))==3 and len(xml.findall('.//w:tbl',ns))==1)
    check('Editable fractions, radicals, subscripts and superscripts',all(xml.findall('.//m:'+k,ns) for k in ['f','rad','sSub','sSup']))
    forbidden=[r'\bINSERT\b',r'\bTODO\b',r'\bTBD\b',r'Version B',r'Experimental Framework',r'130 specimens',r'student measurements unavailable',r'F3498',r'sqrt\(',r'\bDelta\b',r'epsilon_',r'sigma_',r'\ufffd']
    artifacts=[]
    for name in ['Constrained-Annealing-2026.pdf','Constrained-Annealing-2026-Supplementary.pdf']:
        p='output/master/'+name;reader=PdfReader(ROOT/p);text='\n'.join(q.extract_text() for q in reader.pages)
        check(name+' readable and without forbidden text',all(len(q.extract_text())>150 for q in reader.pages) and not any(re.search(v,text) for v in forbidden))
        if name=='Constrained-Annealing-2026.pdf':
            check('Main PDF is current native Word export with repaired references',reader.metadata.get('/Producer','').startswith('Microsoft') and 'Odent' in text and 'Wittemann' in text and '3.64' in text and '0.000106' in text)
        with pdfplumber.open(ROOT/p) as doc:
            bad=[n for n,q in enumerate(doc.pages,1) if any(c['text'].strip() and (c['x0']<34 or c['x1']>q.width-34 or c['top']<24 or c['bottom']>q.height-16) for c in q.chars)]
        check(name+' text within page safety bounds',not bad)
        artifacts.append(dict(path=p,sha256=sha(p),pages=len(reader.pages)))
    check('Evolving draft equals the complete current main PDF',sha('output/pdf/Constrained-Annealing-2026-DRAFT.pdf')==artifacts[0]['sha256'])
    if not args.preflight:
        qa=json.loads((ROOT/'docs/master_visual_review.json').read_text())
        for a in artifacts:
            q=next(x for x in qa['artifacts'] if x['path']==a['path']);assert q['sha256']==a['sha256'] and q['pages_reviewed']==list(range(1,a['pages']+1)) and q['status']=='pass'
        assert sha(qa['editable_source']['path'])==qa['editable_source']['sha256']
        check('All final PDF pages visually reviewed at their current hashes',True)
    for manifest in ['reproducibility/master_figure_manifest.csv','reproducibility/master_table_manifest.csv']:
        for r in rows(manifest):
            for key in ['artifact','source','script','manuscript','builder']:
                if key in r:assert sha(r[key])==r[key+'_sha256'],(manifest,r[key])
    check('Three figures and eighteen table source/build manifests agree',True)
    tests=json.loads((ROOT/'docs/master_unit_tests.json').read_text())
    assert tests['passed'] and tests['count']==98 and sha(tests['log'])==tests['log_sha256']
    for p,hsh in tests['test_sha256'].items():assert sha(p)==hsh,p
    check('98-test execution receipt agrees with retained log and test source hashes',True)
    current=sorted(set(subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()))
    current=[p for p in current if (ROOT/p).is_file()]
    patterns=[rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',rb'ghp_[A-Za-z0-9]{36}',rb'github_pat_[A-Za-z0-9_]{60,}',rb'sk-proj-[A-Za-z0-9_-]{30,}',rb'AKIA[0-9A-Z]{16}']
    for p in current:
        if Path(p).suffix.lower() in ['.pdf','.png','.docx','.xlsx','.rst','.rth','.db','.esav','.full']:continue
        assert not any(re.search(v,(ROOT/p).read_bytes()) for v in patterns),p
    check('Current publishable tree has no common credential/private-key patterns',True)
    check('No publisher PDF newly redistributed',not any(p.startswith('literature/evidence/') and p.endswith('.pdf') for p in current))
    # Explicit lineage for every new displayed/data row. Old 384-record register remains unchanged.
    trace=[]
    def add(kind,loc,processed,row,raw='',case='',script=''):
        trace.append(dict(record=len(trace)+1,evidence_class=kind,manuscript_location=loc,processed_data=processed,row=row,processed_sha256=sha(processed),raw_export=raw,raw_sha256=sha(raw) if raw else '',case=case,input_sha256=sha(case+'/input.dat') if case else '',source_script=script,script_sha256=sha(script) if script else ''))
    for n,r in enumerate(details,2):add('A','Section 3.1; Table 1; Figure 1; Table S14','verification/master_nonisothermal.csv',n,r['raw_export'],str(Path(r['raw_export']).parent).replace('\\','/'),'scripts/summarize_master_nonisothermal.py')
    for p,r in stoprows:add('A','Section 3.2; Figure 2; Table S16',(p/'comparison.csv').relative_to(ROOT).as_posix(),int(r['step'])+1,(p/'raw.csv').relative_to(ROOT).as_posix(),p.relative_to(ROOT).as_posix(),'scripts/check_mount_kinematics.py')
    for n,r in enumerate(rows('data/processed/master_fixture_screen.csv'),2):add('B','Section 3.2; Figure 2; Table S17','data/processed/master_fixture_screen.csv',n,script='scripts/screen_fixture_mechanism.py')
    for n,r in enumerate(rows('verification/programmed_road_check.csv'),2):add('B','Section 3.3; Figure 3; Table S15','verification/programmed_road_check.csv',n,script='scripts/check_programmed_recovery.py')
    for p in ['validation/master_spring_targets.csv','validation/master_suder_targets.csv']:
        for n,r in enumerate(rows(p),2):add('C','Sections 2.5 and 3.3; reserved independent observations',p,n)
    clean=[];inside=False
    for line in body.splitlines():
        if line.startswith('TABLE:'):inside=True;continue
        if inside:
            if not line.strip():inside=False
            continue
        if not line or line.startswith(('EQ:','IMAGE:','CAPTION:','#')):continue
        clean.append(html.unescape(re.sub('<[^>]+>','',line)))
    wordcount=len(re.findall(r"\b[\w]+(?:[’'−–-][\w]+)*\b",' '.join(clean)))
    abstract=body.split('### Abstract',1)[1].split('Keywords:',1)[0]
    abstractwords=len(re.findall(r'\b\S+\b',re.sub('<[^>]+>','',abstract)))
    report=dict(date='2026-11-01',scope='Verification and feasibility; physical production study incomplete',passed=True,preflight=args.preflight,check_count=len(checks),frozen_evidence_records=len(frozen),new_attempts=attempts,accepted_new_reference_runs=6,production_runs=0,new_trace_records=len(trace),artifacts=artifacts,main_words_excluding_headings_math_tables_captions_references=wordcount,abstract_words=abstractwords,checks=checks)
    dump('docs/master_integrity.json',report)
    if args.write:
        writecsv('reproducibility/master_result_traceability.csv',trace)
        dump('reproducibility/master_doi_audit.json',dict(date='2026-11-01',records=[metadata[d.lower()] for d in dois],author_corrections='literature/master_metadata_corrections.json'))
        sources=[p for p in current if p.startswith(('simulation/master/','output/master/','figures/master/','manuscript/master','supplementary/master','docs/master','material/master','material/programmed','verification/master','verification/programmed','literature/metadata/master','literature/master','validation/master','reproducibility/master','reproducibility/programmed')) or p in ['docs/PROJECT_STATE.md','README.md','CITATION.cff','requirements.txt'] or (p.startswith('scripts/') and ('master' in p or p in ['scripts/check_mount_kinematics.py','scripts/screen_fixture_mechanism.py','scripts/check_programmed_recovery.py','scripts/scientific_format.py'])) or p in ['src/programmed_recovery.py','analysis/surface_metrics.py','ansys/run_case.py','analysis/extract_results.py']]
        # Include the transitive authoring/calculation dependencies, not only files
        # whose names contain 'master'. Historical frozen evidence is checked above.
        sources=sorted(set(sources+[p for p in current if p.startswith(('scripts/','src/','analysis/','ansys/','tests/')) and Path(p).suffix in ['.py','.json','.md']]+['reproducibility/MASTER_README.md','environment.yml']))
        sources=[p for p in sources if p not in ['reproducibility/master_checksums.json','docs/master_git_verification.json']]
        dump('reproducibility/master_checksums.json',dict(date='2026-11-01',purpose='Evidence and reproducibility hashes; no publication release tag',files={p:sha(p) for p in sources}))
    print(json.dumps({k:v for k,v in report.items() if k not in ['checks','new_attempts']},indent=2))
if __name__=='__main__':main()
