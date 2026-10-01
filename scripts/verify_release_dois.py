"""Recheck every DOI in the final bibliography against live Crossref records."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, urllib.parse, json, re, hashlib
ROOT=Path(__file__).resolve().parents[1]
def main():
    dest=ROOT/'literature/metadata/stage20';dest.mkdir(exist_ok=True)
    dois=sorted(set(re.findall(r'doi = \{([^}]+)\}',(ROOT/'literature/references.bib').read_text(encoding='utf-8'))))
    def one(doi):
        path=dest/(hashlib.sha256(doi.encode()).hexdigest()[:16]+'.json')
        url='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')
        try:
            if not path.exists():
                req=urllib.request.Request(url,headers={'User-Agent':'FDM-Annealing-reproducibility-audit/0.20'})
                with urllib.request.urlopen(req,timeout=45) as r:content=r.read()
                path.write_bytes(content)
            m=json.loads(path.read_bytes())['message'];assert m['DOI'].lower()==doi.lower()
            return dict(doi=doi,status='verified',title=m.get('title'),publisher=m.get('publisher'),url=url,metadata_path=path.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        except Exception as e:return dict(doi=doi,status='unresolved',error=str(e),url=url)
    with ThreadPoolExecutor(max_workers=1) as pool:results=list(pool.map(one,dois))
    (ROOT/'reproducibility/doi_audit.json').write_text(json.dumps(dict(date='2026-10-01',verification='Crossref DOI identity; original source/title appraisal in prior literature audits',records=results),indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'records':len(results),'unresolved':[r for r in results if r['status']!='verified']},indent=2))
    if any(r['status']!='verified' for r in results):raise SystemExit(1)
if __name__=='__main__':main()
