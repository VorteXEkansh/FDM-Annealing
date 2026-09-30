"""Audit reconstructed article structure, equation scope and retained evidence."""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
def main():
    source=(ROOT/'manuscript/current.md').read_text(encoding='utf-8')
    checks=[]
    def check(name,value):
        assert value,name
        checks.append({'check':name,'status':'pass'})
    check('Main article sections',all('### '+s in source for s in ['Abstract','1. Introduction','2. Background','3. Computational','4. Results','5. Discussion','6. Conclusions','Data availability','Code availability','Declarations','References','Supplementary information']))
    check('Sixteen methodology and eighteen Results subsections',all(f'### 3.{i}. ' in source for i in range(1,17)) and all(f'### 4.{i}. ' in source for i in range(1,19)))
    eqs=[l for l in source.splitlines() if l.startswith('EQ:')]
    check('Twenty-one consecutive equations',[int(re.search(r'\((\d+)\)$',l)[1]) for l in eqs]==list(range(1,22)))
    with (ROOT/'docs/manuscript_equation_map.csv').open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
    check('All current equations mapped to implemented relations',[int(r['equation']) for r in rows]==list(range(1,22)) and not any(r['status'].startswith('pending') for r in rows))
    check('Unimplemented extraction formulas removed',not {15,16,17}.intersection(int(r['prior_equation']) for r in rows))
    check('Executable strain partition omits absent irreversible law','ann' not in eqs[2] and 'No bulk annealing-induced irreversible-strain relation is parameterized' in source)
    check('Supplement has seven detailed tables',source.count('SUPPTABLE:')==7 and source.count('\nTABLE:')==3)
    check('Seven quantitative conclusions',re.findall(r'^(\d)\. ',source,re.M)==list('1234567'))
    check('All regression tests passed','Ran 81 tests' in (ROOT/'docs/stage_18_tests.txt').read_text() and (ROOT/'docs/stage_18_tests.txt').read_text().rstrip().endswith('OK'))
    check('No completed production or submission claim',all(x in source for x in ['scientifically incomplete','no production campaign was run','not a completed production-annealing or optimization article ready for submission']))
    for p in ['data/processed/all_cases.csv','optimization/pareto.csv','optimization/confirmation.csv']:
        with (ROOT/p).open() as f: check('Empty actual registry: '+p,not list(csv.DictReader(f)))
    historical=json.loads((ROOT/'docs/stage_17_manifest.json').read_text())['files']
    evidence=[p for p in historical if p.startswith(('simulation/','verification/','convergence/','validation/','material/','literature/','data/raw/'))]
    check('Prior numerical and literature evidence unchanged',all(sha(p)==historical[p] for p in evidence))
    with (ROOT/'convergence/contact_sensitivity.csv').open() as f: contact=list(csv.DictReader(f))
    check('Same-control friction endpoints preserve actual values',all(token in (ROOT/'convergence/contact_sensitivity.csv').read_text() for token in ['17.5367683291','20.0333528221','24.4283504486','51.8788375854']) and all(token in source for token in ['17.5368 to 20.0334','24.4284 to 51.8788']))
    paths=['manuscript/current.md','docs/manuscript_equation_map.csv','docs/manuscript_reconstruction_audit.md','docs/stage_18_tests.txt','scripts/check_reconstruction_stage.py','scripts/build_manuscript.py','src/constitutive.py','scripts/run_thermal_verification.py','scripts/run_structural_verification.py','scripts/run_convergence_study.py','scripts/check_convergence_stage.py','analysis/validation_metrics.py','verification/thermal_verification.csv','verification/structural_verification.csv','verification/contact_verification.csv','convergence/mesh_convergence.csv','convergence/timestep_convergence.csv','convergence/contact_sensitivity.csv']
    result={'stage':18,'date':'2026-09-30','passed':True,'count':len(checks),'checks':checks,'equations':21,'unit_tests':81,'frozen_evidence_files_checked':len(evidence),'new_solver_runs':0,'production_science_complete':False,'source_hashes':{p:sha(p) for p in paths}}
    (ROOT/'docs/stage_18_reconstruction_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} reconstruction checks passed; {len(evidence)} evidence files unchanged')
if __name__=='__main__':main()
