"""Stage 4 document, provenance and property checks; not solver verification."""
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
    check('Retained references and citations correspond',citations==set(range(1,39)))
    check('Retained DOIs present',all(r['doi'] in source for r in refs))
    check('Objectives numbered 1 through 5',re.findall(r'^(\d)\. ',source,re.M)==['1','2','3','4','5'])
    check('Equations numbered consecutively',re.findall(r'\((\d+)\)\s*$', '\n'.join(l for l in source.splitlines() if l.startswith('EQ:')),re.M)==list(map(str,range(1,12))))
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
    before=digest(PDF)
    subprocess.run([sys.executable,str(ROOT/'scripts/build_manuscript.py')],check=True,cwd=ROOT,capture_output=True)
    check('PDF reproducible byte-for-byte',digest(PDF)==before)
    reader=PdfReader(PDF)
    check('Complete twenty-five-page manuscript without spill pages',len(reader.pages)==25)
    text='\n'.join(p.extract_text() for p in reader.pages)
    for pattern in [r'F3498',r'sqrt\s*\(',r'epsilon_ann',r'Delta L',r'95 C',r'3 x 3',r'130 physical specimens',r'\bTODO\b',r'\bTBD\b',r'\ufffd']:
        check('Forbidden manuscript pattern absent: '+pattern,not re.search(pattern,text))
    check('Evidence absence explicitly reported','No ANSYS results' in text and 'No ANSYS runs' in text)
    check('Thermal choices typeset',all(v in text for v in ['80 °C','95 °C','110 °C','30 min','60 min','90 min']))
    check('Mathematical symbols preserved',all(c in text for c in 'Δεσρ∂∇√∑∏∈⊥'))
    check('All pages contain substantive text or a continued coefficient table',all(len(p.extract_text())>500 for p in reader.pages))
    with pdfplumber.open(PDF) as pdf:
        bad=[]
        for n,p in enumerate(pdf.pages,1):
            for c in p.chars:
                if c['text'].strip() and (c['x0']<48 or c['x1']>p.width-46 or c['top']<30 or c['bottom']>p.height-18): bad.append(n)
        check('All text lies inside page safety bounds',not bad)
    report={'stage':4,'date':'2026-09-12','checks':checks,'count':len(checks),'pdf_sha256':digest(PDF),'manuscript_sha256':digest(ROOT/'manuscript/current.md'),'material_manifest_sha256':digest(ROOT/'material/build_manifest.json'),'scope':'Document, source and property integrity only. No solver verification or validation performed.'}
    (ROOT/'docs/integrity_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'{len(checks)} integrity checks passed; PDF SHA-256 {digest(PDF)}')

if __name__=='__main__': main()
