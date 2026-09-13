"""Stage 6 environment and automation integrity checks."""
import hashlib, io, json, re, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
def h(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    checks=[]
    def check(name,ok):
        assert ok,name; checks.append({"check":name,"status":"pass"})
    run=ROOT/'simulation/runs/stage06_mapdl_smoke'
    manifest=json.loads((run/'manifest.json').read_text())
    output=(run/'mapdl.out').read_text(errors='replace')
    deck=(ROOT/'ansys/apdl/environment_smoke.dat').read_text()
    check('MAPDL smoke returned zero',manifest['executed'] and manifest['returncode']==0)
    check('MAPDL banner is 2026 R1 build 26.1 update 20260202',all(x in output for x in ['RELEASE= 2026 R1','BUILD= 26.1','UP20260202']))
    check('Academic Student product checked out','Ansys Mechanical Enterprise Academic Student' in output)
    check('Smoke deck contains no solve or model commands',not re.search(r'(?im)^\s*(solve|antype|et|n|e|block|vmesh)\s*[,\n]',deck))
    check('Smoke hashes match',manifest['input_sha256']==h('simulation/cases/environment_smoke.json') and manifest['apdl_sha256']==h('ansys/apdl/environment_smoke.dat') and all(hashlib.sha256((run/name).read_bytes()).hexdigest()==value for name,value in manifest['outputs'].items()))
    prod=json.loads((ROOT/'simulation/cases/production_template.json').read_text())
    check('Production template has explicit parameters',set(prod['parameters'])=={'temperature_C','hold_time_s','fixture_gap_mm','material_id'})
    check('Production gates remain closed',all(v is False for v in prod['admission'].values()))
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_ansys_automation.py')
    result=unittest.TextTestRunner(stream=io.StringIO(),verbosity=1).run(suite)
    check('Automation unit tests pass',result.wasSuccessful() and result.testsRun==6)
    env=(ROOT/'docs/software_environment.md').read_text(encoding='utf-8')
    check('Environment report separates presence and entitlement',all(x in env for x in ['Present on disk','Invocation status','License/availability conclusion']))
    check('PyMechanical absence documented','PyMechanical' in env and 'not installed' in env)
    check('Student structural limit source documented','128,000 nodes/elements' in env)
    report={'stage':6,'date':'2026-09-13','passed':True,'checks':checks,'sha256':{p:h(p) for p in ['ansys/run_case.py','ansys/apdl/environment_smoke.dat','simulation/cases/environment_smoke.json','simulation/cases/production_template.json','analysis/extract_results.py']}}
    (ROOT/'docs/stage_06_ansys_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f'{len(checks)} Ansys environment/automation checks passed')
if __name__=='__main__': main()
