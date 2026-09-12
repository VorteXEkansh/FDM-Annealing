"""Stage 3 document/provenance checks, not numerical solver verification."""
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
    check('Retained references and citations correspond',citations==set(range(1,36)))
    check('Retained DOIs present',all(r['doi'] in source for r in refs))
    check('Objectives numbered 1 through 5',re.findall(r'^(\d)\. ',source,re.M)==['1','2','3','4','5'])
    check('Equations numbered consecutively',re.findall(r'\((\d)\)\s*$', '\n'.join(l for l in source.splitlines() if l.startswith('EQ:')),re.M)==list(map(str,range(1,10))))
    check('No duplicated or result figures',source.count('FIGURE:')==1 and source.count('CAPTION: Figure 1.')==1)
    for path in ['results/run_registry.csv','data/literature/property_registry.csv','data/literature/validation_registry.csv']:
        with (ROOT/path).open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
        check('No invented data in '+path,len(rows)==0)
    check('No dummy ANSYS binaries',not any((ROOT/'models/ansys').glob('*.rst')) and not any((ROOT/'models/ansys').glob('*.wbpj')))
    check('One primary research question',source.count('<b>Primary research question.</b>')==1)
    check('Five secondary research questions',re.findall(r'^SQ([1-5])\.',source,re.M)==list('12345'))
    check('Four testable propositions',re.findall(r'^H([1-4]) —',source,re.M)==list('1234'))
    check('Scope and non-claims explicit',all(t in source for t in ['FREE','GAP','traction-free','Gravity is omitted','discrete-element','Intended contribution','Results status.']))
    before=digest(PDF)
    subprocess.run([sys.executable,str(ROOT/'scripts/build_manuscript.py')],check=True,cwd=ROOT,capture_output=True)
    check('PDF reproducible byte-for-byte',digest(PDF)==before)
    reader=PdfReader(PDF)
    check('Complete twenty-page manuscript without spill pages',len(reader.pages)==20)
    text='\n'.join(p.extract_text() for p in reader.pages)
    for pattern in [r'F3498',r'sqrt\s*\(',r'epsilon_ann',r'Delta L',r'95 C',r'3 x 3',r'130 physical specimens',r'\bTODO\b',r'\bTBD\b',r'\ufffd']:
        check('Forbidden manuscript pattern absent: '+pattern,not re.search(pattern,text))
    check('Evidence absence explicitly reported','No ANSYS results' in text and 'No ANSYS runs' in text)
    check('Thermal choices typeset',all(v in text for v in ['80 °C','95 °C','110 °C','30 min','60 min','90 min']))
    check('Mathematical symbols preserved',all(c in text for c in 'Δεσρ∂∇√∑∏∈⊥'))
    check('All pages contain substantive text',all(len(p.extract_text())>1800 for p in reader.pages))
    with pdfplumber.open(PDF) as pdf:
        bad=[]
        for n,p in enumerate(pdf.pages,1):
            for c in p.chars:
                if c['text'].strip() and (c['x0']<48 or c['x1']>p.width-46 or c['top']<30 or c['bottom']>p.height-18): bad.append(n)
        check('All text lies inside page safety bounds',not bad)
    report={'stage':3,'date':'2026-09-12','checks':checks,'count':len(checks),'pdf_sha256':digest(PDF),'manuscript_sha256':digest(ROOT/'manuscript/current.md'),'scope':'Document and evidence integrity only. No solver verification or validation performed.'}
    (ROOT/'docs/integrity_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'{len(checks)} integrity checks passed; PDF SHA-256 {digest(PDF)}')

if __name__=='__main__': main()
