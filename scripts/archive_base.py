"""Archive user-supplied source and build an auditable reference inventory."""
from pathlib import Path
import hashlib, json, re, shutil, argparse
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('source',type=Path)
    args=ap.parse_args()
    dest=ROOT/'data/source'/args.source.name
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        assert hashlib.sha256(dest.read_bytes()).digest()==hashlib.sha256(args.source.read_bytes()).digest(), 'Refusing to overwrite differing archived evidence'
    else: shutil.copyfile(args.source,dest)
    reader=PdfReader(dest)
    pages=[p.extract_text() for p in reader.pages]
    extracted='\n'.join(f'--- PAGE {i+1} ---\n{p}' for i,p in enumerate(pages))
    (dest.parent/'base_extracted.txt').write_text('\n'.join(line.rstrip() for line in extracted.splitlines()).rstrip()+'\n',encoding='utf-8')
    manifest={'source_name':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'pages':len(pages),'role':'User-supplied experimental proposal, not solver evidence','archived_date':'2026-09-12'}
    (dest.parent/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    refs='\n'.join(pages[20:23]).split('References',1)[1]
    entries=re.split(r'\[(\d+)\]',refs)
    catalog=[]
    for i in range(1,len(entries),2):
        n=int(entries[i]); raw=' '.join(entries[i+1].split())
        catalog.append({'base_id':n,'base_entry_extracted':raw,'disposition':'KEEP BUT REWRITE' if n in (3,35,42,50) else 'MOVE TO SUPPLEMENT','verification_status':'retained_limited_scope_checked' if n in (3,35,42,50) else 'pending_independent_verification','current_id':{35:1,42:2,3:3,50:4}.get(n)})
    assert len(catalog)==50
    (ROOT/'data/literature/base_reference_catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Archived',len(pages),'pages and',len(catalog),'reference entries')

if __name__=='__main__': main()
