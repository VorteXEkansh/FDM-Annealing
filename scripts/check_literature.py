"""Bibliographic, workbook and material-source integrity (not solver validation)."""
from pathlib import Path
import json,re,hashlib,zipfile,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((ROOT/'literature/literature_matrix.json').read_text(encoding='utf-8'))
checks=[]
def check(name,test):
 assert test,name
 checks.append({'check':name,'status':'pass'})
check('34 unique DOI-verified journal records',len(rows)==len({r['doi'].lower() for r in rows})==34)
for r in rows:
 raw=ROOT/'literature/metadata'/f"{r['key']}.json"
 m=json.loads(raw.read_bytes())['message']
 check(r['key']+' DOI identity and immutable metadata hash',m['DOI'].lower()==r['doi'].lower() and digest(raw)==r['metadata_sha256'])
 check(r['key']+' complete appraisal schema',all(r.get(f) for f in ['authors','title','journal','PLA grade','geometry','print condition','annealing temperature','holding time','support/constraint','mechanical data','dimensional data','thermal data','constitutive properties','simulation method','validation usefulness','limitations','relevance','source locator','source URL']))
 dates=r['publication_dates'];earliest=min(tuple(x[0]+[1]*(3-len(x[0]))) for x in dates.values())
 check(r['key']+' available by cutoff',earliest<=(2026,9,12))
bib=(ROOT/'literature/references.bib').read_text(encoding='utf-8')
property_sources=[]
property_path=ROOT/'material/property_sources.csv'
if property_path.exists():
 import csv
 with property_path.open(encoding='utf-8-sig') as f:property_sources=list(csv.DictReader(f))
property_dois={r['doi_or_reference'].lower() for r in property_sources if re.fullmatch(r'10\.\S+',r['doi_or_reference'])}
check('BibTeX DOI set corresponds to verified matrix, material sources and ASTM',set(x.lower() for x in re.findall(r'doi = \{([^}]+)\}',bib))=={r['doi'].lower() for r in rows}|property_dois|{'10.1520/f3489-23'})
source=(ROOT/'manuscript/current.md').read_text(encoding='utf-8')
check('No unresolved citation keys or doubled HTML entities','[@' not in source and '&amp;amp;' not in source)
check('All journal DOIs in complete manuscript',all(r['doi'] in source for r in rows))
check('All DOI-bearing material sources in complete manuscript',all(doi in source for doi in property_dois))
body=source[:source.index('### References')]
expected_citations=set(range(1,40)) if "[39] ANSYS" in source else set(range(1,39)) if property_sources else set(range(1,36))
check('Every bibliography entry cited in body',set(map(int,re.findall(r'\[(\d+)(?:\]|,)',body)))==expected_citations)
check('No duplicated table labels',not re.search(r'TABLE: Table \d',source))
for a in json.loads((ROOT/'literature/acquisition_manifest.json').read_text()):
 local=ROOT/a['local_review_copy']
 if local.exists():check(a['key']+' acquisition hash',digest(local)==a['sha256'])
for r in property_sources:
 local=ROOT/r['local_evidence']
 check(r['source_key']+' material-source evidence hash',local.exists() and digest(local)==r['sha256'])
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(ROOT/'literature/literature_matrix.xlsx') as z:
 shared=ET.fromstring(z.read('xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in z.namelist() else None
 strings=[''.join(n.itertext()) for n in shared] if shared is not None else []
 sheet=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
 cells={}
 for c in sheet.findall('.//s:sheetData/s:row/s:c',ns):
  v=c.find('s:v',ns)
  if c.attrib.get('t')=='s':value=strings[int(v.text)]
  elif c.attrib.get('t')=='inlineStr':value=''.join(c.find('s:is',ns).itertext())
  else:value=v.text if v is not None else ''
  cells[c.attrib['r']]=(value,c.attrib.get('t'))
 check('Workbook has 34 complete data rows',len(sheet.findall('.//s:sheetData/s:row',ns))==35)
 check('Workbook record identities match JSON',all(cells[f'A{i+2}'][0]==r['key'] and cells[f'F{i+2}'][0]==r['doi'] for i,r in enumerate(rows)))
 check('Workbook years are numeric',all(cells[f'C{i+2}'][1] not in ['s','inlineStr'] for i in range(34)))
 check('Workbook has no error cells',not sheet.findall('.//s:c[@t="e"]',ns))
 check('Workbook has no formulas implying calculated results',not sheet.findall('.//s:f',ns))
 check('Workbook frozen header and record ID',sheet.find('.//s:pane',ns) is not None)
stage=int(sys.argv[1]) if len(sys.argv)>1 else 2
report={'stage':stage,'checks':checks,'count':len(checks),'scope':'Bibliography, source hashes and workbook integrity only'}
(ROOT/('docs/literature_integrity_report.json' if stage==2 else f'docs/stage_{stage:02d}_literature_integrity.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
print(f'{len(checks)} literature integrity checks passed')
