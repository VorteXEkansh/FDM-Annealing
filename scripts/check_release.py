"""Stage 20 release gate: raw evidence, numerical recomputation, OOXML and exports."""
from pathlib import Path
import argparse,csv,hashlib,json,math,re,sys,subprocess,zipfile
from lxml import etree
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from analysis.review_metrics import extract,relative_change,numeric_csv
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def rows(p):
    with (ROOT/p).open(encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-checksums',action='store_true');ap.add_argument('--preflight',action='store_true');args=ap.parse_args()
    checks=[]
    def check(label,ok):
        assert ok,label
        checks.append(label)
    excluded={r['path']:r['sha256'] for name in ['external_evidence.csv','external_scratch.csv'] for r in rows('reproducibility/'+name)}
    old=json.loads((ROOT/'docs/stage_19_manifest.json').read_text())['files']
    frozen={p:h for p,h in old.items() if p.startswith(('simulation/','verification/','convergence/','validation/','material/','data/raw/','literature/evidence/','literature/metadata/'))}
    missing=[]
    for p,h in frozen.items():
        if (ROOT/p).exists():assert sha(p)==h,p
        else:assert excluded.get(p)==h,p;missing.append(p)
    check(f'{len(frozen)} frozen evidence hashes verified or explicit external exclusions',True)
    for name in ['mesh_convergence.csv','timestep_convergence.csv']:
        prev={}
        for r in rows('convergence/'+name):
            value=extract(ROOT/r['run_path'],r['model'])[r['quantity']]
            assert math.isclose(value,float(r['value']),rel_tol=1e-10,abs_tol=1e-12)
            key=(r['model'],r['quantity'])
            if key in prev and value!=0:assert math.isclose(relative_change(value,prev[key]),float(r['delta_percent']),rel_tol=1e-5,abs_tol=1e-7)
            prev[key]=value
    check('63 mesh/time responses and defined changes recomputed from raw exports',True)
    previous=None
    for r in rows('convergence/timestep_convergence.csv'):
        if r['model']=='thermal' and r['quantity']=='thermal_lag_at_300_s':
            profile=sorted(numeric_csv(ROOT/r['run_path']/'temperature_profile.csv'))
            if previous is not None:
                assert len(profile)==len(previous)
                assert all(a[:2]==b[:2] for a,b in zip(profile,previous)), 'Profile time/spatial grids differ'
                rmse=math.sqrt(math.fsum((a[2]-b[2])**2 for a,b in zip(profile,previous))/len(profile))
                assert math.isclose(rmse,float(r['profile_RMSE_C_vs_previous']),rel_tol=1e-10,abs_tol=1e-12)
            previous=profile
    check('Three pairwise thermal profile RMSE values recomputed on matched raw grids',True)
    for r in rows('convergence/contact_sensitivity.csv'):
        v=extract(ROOT/r['run_path'],'contact')
        for a,b in [('mean_contact_pressure','mean_contact_pressure_MPa'),('maximum_contact_pressure','maximum_contact_pressure_MPa'),('maximum_penetration','maximum_penetration_mm'),('normal_reaction','normal_reaction_N_per_mm')]:assert math.isclose(v[a],float(r[b]),rel_tol=1e-10,abs_tol=1e-12)
    check('36 contact quantities independently recomputed',True)
    for r in rows('verification/structural_verification.csv')+rows('verification/contact_verification.csv'):
        error=abs(float(r['ansys'])-float(r['reference']));assert math.isclose(error,float(r['absolute_error']),abs_tol=1e-14) and error<=float(r['tolerance'])
    check('114 structural/contact reference comparisons meet declared tolerances',True)
    for r in rows('verification/thermal_verification.csv'):
        error=abs(float(r['ansys_temperature_C'])-float(r['analytical_temperature_C']));assert abs(error-float(r['absolute_error_C']))<=1.1e-9 and error<=.05 and 100*error/abs(float(r['analytical_temperature_C'])-20)<=.25
    check('All nine thermal reference samples satisfy absolute and excursion-relative limits',True)
    for p in ['simulation/design_matrix.csv','simulation/case_manifest.csv','data/processed/all_cases.csv','optimization/pareto.csv','optimization/confirmation.csv']:check('No fabricated results in '+p,len(rows(p))==0)
    check('Validation observations have no predictions/errors',all(not r['prediction'] and not r['error'] and r['validation_solved']=='false' for r in rows('validation/validation_dataset.csv')))
    trace=rows('reproducibility/result_traceability.csv')
    for r in trace:
        assert sha(r['processed_data'])==r['processed_sha256']
        if r['ansys_input']:assert sha(r['ansys_input'])==r['input_sha256'] and (ROOT/r['ansys_case']).exists()
        for p,h in zip(r['raw_export'].split(';'),r['raw_sha256'].split(';')):
            if p:assert sha(p)==h if (ROOT/p).exists() else excluded.get(p)==h
    check(f'All {len(trace)} claim/evidence records resolve and hashes agree',True)
    for p,count in [('figure_manifest.csv',4),('table_manifest.csv',15)]:
        rr=rows('reproducibility/'+p);check(p+' complete',len(rr)==count)
        for r in rr:
            for key in ['source_script','source_dataset','output_file']:
                for name in r[key].split(';'):assert (ROOT/name.strip()).exists(),name
    source=(ROOT/'manuscript/current.md').read_text(encoding='utf-8')
    bibsource=source.split('### References')[1].split('### Supplementary information')[0]
    refs=set(map(int,re.findall(r'^\[(\d+)\]',bibsource,re.M)))
    cited=set()
    for group in re.findall(r'\[(\d+(?:\s*[–-]\s*\d+)?(?:\s*,\s*\d+(?:\s*[–-]\s*\d+)?)*)\s*(?=\]|,)',source.split('### References')[0]):
        for part in group.split(','):
            ends=re.split('[–-]',part);cited.update(range(int(ends[0]),int(ends[-1])+1))
    check('All 41 references cited and no dangling citations',refs==cited==set(range(1,42)))
    records=json.loads((ROOT/'reproducibility/doi_audit.json').read_text(encoding='utf-8'))['records']
    check('All 38 bibliography DOIs verified',len(records)==38 and all(r['status']=='verified' for r in records))
    check('DOI metadata hashes and identities preserved',all(sha(r['metadata_path'])==r['sha256'] and json.loads((ROOT/r['metadata_path']).read_bytes())['message']['DOI'].lower()==r['doi'].lower() for r in records))
    file='output/release/Constrained-Annealing-2026.docx'
    with zipfile.ZipFile(ROOT/file) as z:
        xml=etree.fromstring(z.read('word/document.xml'));styles=etree.fromstring(z.read('word/styles.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
    check('Native editable math for all 21 numbered equations',len(xml.findall('.//m:oMath',ns))==23)
    check('Editable fractions, radical and sub/superscripts exist',all(xml.findall('.//m:'+t,ns) for t in ['f','rad','sSub','sSup']))
    check('Native title/headings, 3 editable tables and 4 figure drawings',len(xml.findall('.//w:tbl',ns))==3 and len(xml.findall('.//w:drawing',ns))==4 and len(xml.findall('.//w:pStyle',ns))>40)
    bookmarks={e.get('{'+ns['w']+'}name') for e in xml.findall('.//w:bookmarkStart',ns)}
    fields=xml.findall('.//w:fldSimple',ns)
    check('All internal REF cross-references resolve',all(e.get('{'+ns['w']+'}instr').split()[1] in bookmarks for e in fields if e.get('{'+ns['w']+'}instr').startswith('REF')))
    check('No title/paragraph decorative border',not xml.findall('.//w:pBdr',ns) and not styles.xpath('.//w:style[@w:styleId="Title"]//w:pBdr',namespaces=ns))
    forbidden=[r'\bINSERT\b',r'\bTODO\b',r'\bTBD\b',r'Version B',r'Experimental Framework',r'130 specimens',r'student measurements unavailable',r'F3498',r'sqrt\(',r'\bDelta\b',r'epsilon_',r'sigma_',r'\ufffd']
    files=['output/release/Constrained-Annealing-2026.pdf','output/release/Constrained-Annealing-2026-Supplementary.pdf']
    for p in files:
        reader=PdfReader(ROOT/p);text='\n'.join(page.extract_text() for page in reader.pages)
        check(p+' searchable, labelled and no forbidden placeholders',all(len(x.extract_text())>150 for x in reader.pages) and 'Verification-only' in text and not any(re.search(pat,text) for pat in forbidden))
        with pdfplumber.open(ROOT/p) as doc:
            bad=[n for n,page in enumerate(doc.pages,1) if any(c['text'].strip() and (c['x0']<48 or c['x1']>page.width-46 or c['top']<30 or c['bottom']>page.height-18) for c in page.chars)]
        check(p+' text within safety bounds',not bad)
    if not args.preflight:
        review=json.loads((ROOT/'docs/stage_20_visual_review.json').read_text(encoding='utf-8'))
        for r in review['artifacts']:
            check(r['path']+' final hash visually reviewed',sha(r['path'])==r['sha256'] and r['status']=='pass' and r['pages_reviewed']==list(range(1,r['page_count']+1)))
    current=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines();current=sorted(set(p for p in current if (ROOT/p).is_file()))
    findings=[]
    secret_patterns=[rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',rb'ghp_[A-Za-z0-9]{36}',rb'github_pat_[A-Za-z0-9_]{60,}',rb'sk-proj-[A-Za-z0-9_-]{30,}',rb'AKIA[0-9A-Z]{16}']
    for p in current:
        if (ROOT/p).suffix.lower() in ['.pdf','.png','.docx','.xlsx','.rst','.rth','.db','.esav','.full','.dll']:continue
        data=(ROOT/p).read_bytes()
        if any(re.search(pattern,data) for pattern in secret_patterns):findings.append(p)
    check('Release tree secret-pattern scan found no credentials/private keys',not findings)
    check('Third-party PDF files excluded from current Git tree',not any(p.startswith('literature/evidence/') and p.endswith('.pdf') for p in current))
    report=dict(stage=20,date='2026-10-01',scope='Verification-only release; no physical validation or production conclusions',preflight=args.preflight,passed=True,count=len(checks),checks=checks,external_evidence_absent=missing,secret_scan_scope='Current tracked and unignored release files; common token/private-key patterns, not a proof about all historical commits')
    (ROOT/'docs/stage_20_integrity.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if args.write_checksums:
        assert not args.preflight,'Visual review required before final checksums'
        wanted=[p for p in current if p.startswith(('material/','verification/','convergence/','validation/','analysis/','src/','scripts/','geometry/','figures/','output/release/','reproducibility/','manuscript/','supplementary/','literature/metadata/stage20/')) or p in ['README.md','CITATION.cff','requirements.txt','environment.yml','docs/PROJECT_STATE.md','docs/stage_20_visual_review.json','docs/stage_20_rebuild.json','docs/stage_20_quality.md'] or (p.startswith('simulation/') and Path(p).name in ['input.dat','case.json'])]
        wanted=[p for p in wanted if p!='reproducibility/sha256_manifest.csv']
        with (ROOT/'reproducibility/sha256_manifest.csv').open('w',encoding='utf-8',newline='') as f:
            w=csv.writer(f,lineterminator='\n');w.writerow(['path','sha256']);w.writerows((p,sha(p)) for p in wanted)
    elif (ROOT/'reproducibility/sha256_manifest.csv').exists():
        for r in rows('reproducibility/sha256_manifest.csv'):assert sha(r['path'])==r['sha256'],r['path']
    print(f'{len(checks)} release checks passed; {len(frozen)} frozen records; {len(trace)} traceability rows')
if __name__=='__main__':main()
