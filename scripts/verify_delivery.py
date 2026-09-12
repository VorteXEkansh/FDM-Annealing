"""Verify GitHub branch commit and PDF blob without exposing credentials."""
from pathlib import Path
import subprocess, json, argparse, hashlib

ROOT=Path(__file__).resolve().parents[1]

def run(*args):
    return subprocess.check_output(args,cwd=ROOT,text=True,encoding='utf-8').strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--record',action='store_true')
    ap.add_argument('--stage',type=int,default=2)
    args=ap.parse_args()
    branch=run('git','branch','--show-current')
    head=run('git','rev-parse','HEAD')
    remote=run('git','ls-remote','origin','refs/heads/'+branch).split()[0]
    assert head==remote,'Remote branch differs from local HEAD'
    api=run('gh','api','repos/VorteXEkansh/FDM-Annealing/commits/'+head,'--jq','.sha')
    assert api==head,'GitHub API commit differs'
    pdf='output/pdf/Constrained-Annealing-2026-DRAFT.pdf'
    local_blob=run('git','hash-object',pdf)
    remote_blob=run('gh','api','--method','GET','repos/VorteXEkansh/FDM-Annealing/contents/'+pdf,'-f','ref='+head,'--jq','.sha')
    assert local_blob==remote_blob,'Remote PDF differs'
    record={'stage':args.stage,'repository':'https://github.com/VorteXEkansh/FDM-Annealing','branch':branch,'content_commit':head,'remote_commit':remote,'github_api_commit':api,'pdf_git_blob':remote_blob,'pdf_sha256':hashlib.sha256((ROOT/pdf).read_bytes()).hexdigest(),'status':'Push, remote branch, GitHub commit and PDF blob verified','date':'2026-09-12'}
    if args.record:
        (ROOT/f'docs/stage_{args.stage:02d}_delivery.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,indent=2))

if __name__=='__main__': main()
