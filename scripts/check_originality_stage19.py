"""Limited local exact-phrase screen, not a plagiarism certification."""
from pathlib import Path
import hashlib,html,json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]

def words(text):
    return re.findall(r"[a-z]+",html.unescape(re.sub(r'<[^>]+>',' ',text)).lower())

def main():
    manuscript=(ROOT/'manuscript/current.md').read_text(encoding='utf-8').split('### References')[0]
    prose='\n'.join(line for line in manuscript.splitlines() if not line.startswith(('EQ:','TABLE:','CAPTION:','FIGURE:','IMAGE:')) and ' | ' not in line)
    tokens=words(prose);n=12
    candidates={' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)}
    records=[]
    for p in sorted((ROOT/'literature/evidence').rglob('*')):
        if p.suffix.lower() not in ('.pdf','.html','.xml'): continue
        try:
            text='\n'.join(page.extract_text() or '' for page in PdfReader(p).pages) if p.suffix.lower()=='.pdf' else p.read_text(encoding='utf-8',errors='replace')
            t=words(text)
            matches=sorted(candidates.intersection(' '.join(t[i:i+n]) for i in range(len(t)-n+1)))
            records.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),words=len(t),exact_twelve_word_matches=matches))
        except Exception as exc:
            records.append(dict(path=p.relative_to(ROOT).as_posix(),access_error=type(exc).__name__))
    result=dict(stage=19,scope='Exact 12-word phrase screen of main article prose against available local source text. Excludes bibliography, equations and tables. Does not detect paraphrase or assess inaccessible sources; manual review remains necessary.',records=records,total_matches=sum(len(r.get('exact_twelve_word_matches',[])) for r in records),manuscript_sha256=hashlib.sha256((ROOT/'manuscript/current.md').read_bytes()).hexdigest())
    (ROOT/'docs/stage_19_originality_screen.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Sources screened:',len(records),'Exact phrase matches:',result['total_matches'])
    for r in records:
        if r.get('exact_twelve_word_matches'): print(r['path'],r['exact_twelve_word_matches'])

if __name__=='__main__':main()
