"""Reproduce Stage 9 references from immutable MAPDL output and validate provenance."""
import csv,hashlib,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from scripts.run_structural_verification import compare,parse,write_csv,digest
ACCEPTED=['free_01','fixed_01','eigen_free_01','eigen_fixed_01','contact_03','visco_02']
def main():
    structural=[]; contact=[]; counts={}; warnings={}
    for suffix in ACCEPTED:
        run=ROOT/'simulation/verification'/('stage09_'+suffix)
        m=json.loads((run/'manifest.json').read_text()); assert m['accepted'] and m['returncode']==0
        for name,h in m['files'].items(): assert digest(run/name)==h,(run,name)
        c=json.loads((run/'case.json').read_text()); rows=compare(c,parse(run/'values.csv'))
        assert all(r['passed'] for r in rows),suffix
        archived=list(csv.DictReader((run/'comparison.csv').open()))
        assert len(rows)==len(archived)
        for r,a in zip(rows,archived):
            for k in ['ansys','reference','absolute_error','tolerance']: assert float(a[k])==r[k],(suffix,k)
        text=(run/'mapdl.out').read_text(errors='replace')
        assert '*** ERROR ***' not in text
        assert 'BUILD= 26.1' in text and 'UP20260202' in text
        for r in rows: r['run_path']=str(run.relative_to(ROOT)).replace('\\','/')
        (contact if c['kind']=='contact' else structural).extend(rows)
        counts[c['kind']]=len(rows); warnings[c['kind']]=text.count('*** WARNING ***')
    for suffix in ['contact_01','contact_02','visco_01']:
        run=ROOT/'simulation/verification'/('stage09_'+suffix); m=json.loads((run/'manifest.json').read_text()); assert not m['accepted']
        for name,h in m['files'].items(): assert digest(run/name)==h,(run,name)
    write_csv(ROOT/'verification/structural_verification.csv',structural)
    write_csv(ROOT/'verification/contact_verification.csv',contact)
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_structural_verification.py')
    r=unittest.TextTestRunner().run(suite); assert r.wasSuccessful()
    report=dict(stage=9,passed=True,accepted_runs=ACCEPTED,comparisons=counts,comparison_count=sum(counts.values()),unit_tests=r.testsRun,warnings=warnings,maximum_error_by_quantity={q:max(x['absolute_error'] for x in structural+contact if x['quantity']==q) for q in sorted({x['quantity'] for x in structural+contact})},source_hashes={p:digest(ROOT/p) for p in ['scripts/run_structural_verification.py','scripts/check_structural_stage.py','ansys/structural_model.py','tests/test_structural_verification.py']})
    (ROOT/'docs/stage_09_structural_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
