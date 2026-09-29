"""Enforce Stage 13's validation prerequisite; no production cases are generated."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    checks=[]
    def check(name,ok):
        assert ok,name
        checks.append({'check':name,'status':'pass'})
    evidence=json.loads((ROOT/'simulation/validation/stage12_admission_01/admission.json').read_text())
    check('Validation remains unexecuted',evidence['solver_cases_started']==0 and evidence['validation_completed'] is False)
    check('All six external cases remain blocked',len(evidence['cases'])==6 and all(c['status']=='blocked_before_solver' for c in evidence['cases']))
    for path,fields in [
        ('simulation/design_matrix.csv',['case_id','temperature_C','hold_time_min','constraint','total_reference_clearance_mm','material_id','geometry_id','validation_domain','admission_status']),
        ('simulation/case_manifest.csv',['case_id','case_input_path','case_input_sha256','solver_version','solver_command','run_directory','solver_status','raw_output_manifest_path','extraction_path','extraction_sha256','units_contract_path'])]:
        with (ROOT/path).open(encoding='utf-8') as f:
            r=csv.DictReader(f);rows=list(r)
            check(path+' schema and zero approved cases',r.fieldnames==fields and rows==[])
    prior=json.loads((ROOT/'docs/stage_12_manifest.json').read_text())['files']
    frozen=['docs/validation_protocol.md','validation/validation_results.csv','validation/calibration_register.csv','material/pla_properties.csv','simulation/validation/stage12_admission_01/admission.json']
    check('Validation and material evidence unchanged',all(sha(ROOT/p)==prior[p] for p in frozen))
    template=json.loads((ROOT/'simulation/cases/production_template.json').read_text())
    check('Existing production gates remain closed',all(v is False for v in template['admission'].values()))
    doc=(ROOT/'docs/simulation_design.md').read_text(encoding='utf-8')
    check('No dry-run success or production approval','not a finalized design' in doc and 'No successful dry run is claimed' in doc)
    paths=frozen+['simulation/design_matrix.csv','simulation/case_manifest.csv','docs/simulation_design.md','scripts/check_simulation_design.py','simulation/cases/production_template.json']
    report={'stage':13,'date':'2026-09-29','passed':True,'count':len(checks),'checks':checks,'entry_condition_met':False,'design_finalized':False,'production_cases_approved':0,'dry_run_status':'not_started_validation_prerequisite_unmet','full_sweep_authorized':False,'source_hashes':{p:sha(ROOT/p) for p in paths}}
    (ROOT/'docs/stage_13_design_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} entry/scope integrity checks pass; no production design or dry run admitted')
if __name__=='__main__':main()
