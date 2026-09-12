"""Retrieve DOI registration records; never substitute invented bibliography."""
import json, urllib.request, urllib.parse, hashlib, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
SEEDS='''Bute2024|10.5755/j02.ms.35076
Wijnen2018|10.1007/s40964-018-0052-4
Trofimov2022|10.1016/j.addma.2022.102693
Laminate2025|10.1088/1361-665X/adeee4
Prediction2023|10.3390/polym15051162
Process2025|10.3390/ma18194537
Mould2022|10.3390/polym14132607
Wijnbergen2021|10.1108/RPJ-04-2021-0090
HighHeat2026|10.1002/pen.70250
Multiscale2026|10.1007/s43939-026-00769-2
SCF2023|10.1080/20550340.2023.2171940
Orthotropic2024|10.1016/j.tws.2024.111800
Pantani2010|10.1016/j.polymdegradstab.2010.04.018
Nucleation2011|10.1016/j.tca.2011.05.034
Kinetics2025|10.1002/mame.202500204
Deformation2025|10.1002/pol.20240703
Viscoplastic2017|10.1002/pen.24404
Relaxation2022|10.3390/ma15103509
Kahya2025|10.1016/j.polymertesting.2025.108735
Encapsulation2025|10.3390/jfb16090334
Salt2022|10.1016/j.engfailanal.2021.105932
Moulds2022|10.1177/16878132221120737
Wach2018|10.1002/mame.201800169
Benwood2018|10.1021/acsomega.8b00129
Windheim2021|10.1108/RPJ-08-2020-0205
Bonding2024|10.1016/j.mtcomm.2024.109266
Stojkovic2023|10.3390/ma16134574
Butt2020|10.3390/jmmp4020038
Derringer1980|10.1080/00224065.1980.11980968
WLF1955|10.1021/ja01619a008
Heat2023|10.1016/j.jmapro.2023.03.030
Phase2025|10.1007/s40964-024-00891-8
Grades2026|10.1002/app.71150
PINN2026|10.1016/j.rineng.2026.110279'''
def fetch(line):
 key,doi=line.split('|'); path=ROOT/'literature/metadata'/f'{key}.json'; path.parent.mkdir(parents=True,exist_ok=True)
 url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')
 for attempt in range(3):
  try:
   if path.exists(): raw=path.read_bytes()
   else:
    raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'FDM-Annealing-literature-audit/2.0'}),timeout=30).read();path.write_bytes(raw)
   m=json.loads(raw)['message'];assert m['DOI'].lower()==doi.lower()
   return dict(key=key,doi=m['DOI'],title=m['title'][0],authors='; '.join(x.get('given','')+' '+x.get('family','') for x in m.get('author',[])),journal=m.get('container-title',[''])[0],year=m.get('published',m.get('issued'))['date-parts'][0][0],publication_dates={k:m[k]['date-parts'] for k in ['published','published-online','published-print'] if k in m},volume=m.get('volume',''),issue=m.get('issue',''),pages=m.get('page',m.get('article-number','')),type=m['type'],verification='Crossref DOI exact match; primary source appraisal recorded separately',retrieved='2026-09-12',metadata_url=url,metadata_sha256=hashlib.sha256(raw).hexdigest())
  except Exception as e:
   if attempt==2:return dict(key=key,doi=doi,error=str(e))
   time.sleep(2)
if __name__=='__main__':
 rows=list(ThreadPoolExecutor(max_workers=4).map(fetch,SEEDS.splitlines()))
 (ROOT/'literature/doi_verification.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps([{'key':r['key'],'title':r.get('title'),'error':r.get('error'),'dates':r.get('publication_dates')} for r in rows],ensure_ascii=False))
