"""Audit Stage 12 non-execution without converting missing predictions to zero."""
from pathlib import Path
import csv,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    checks=[]
    def check(name,ok):
        assert ok,name
        checks.append({'check':name,'status':'pass'})
    a=json.loads((ROOT/'simulation/validation/stage12_admission_01/admission.json').read_text())
    check('Six frozen conditions considered',len(a['cases'])==6 and {c['temperature_C'] for c in a['cases']}=={63,75,86,98,109,132})
    check('No solver launch or invented solver status',a['execution_requested'] and a['solver_cases_started']==0 and not a['validation_completed'] and all(c['solver_started'] is False and c['solver_returncode'] is None and c['solver_command'] is None for c in a['cases']))
    check('Every case rejected for nine recorded blockers',all(c['status']=='blocked_before_solver' and len(c['blockers'])==9 for c in a['cases']))
    check('Immutable admission input hashes match',all(sha(ROOT/p)==h for p,h in a['input_hashes'].items()))
    previous=json.loads((ROOT/'docs/stage_11_manifest.json').read_text())['files']
    frozen=['docs/validation_protocol.md','validation/validation_dataset.csv','validation/calibration_register.csv','analysis/validation_metrics.py','material/pla_properties.csv']
    check('Protocol data calibration properties and metric code unchanged',all(sha(ROOT/p)==previous[p] for p in frozen))
    rows=list(csv.DictReader((ROOT/'validation/validation_results.csv').open(encoding='utf-8')))
    source={r['observation_id']:r for r in csv.DictReader((ROOT/'validation/validation_dataset.csv').open(encoding='utf-8')) if r['dataset_role']=='reserved_validation'}
    check('All 18 reserved observations retained exactly',len(rows)==18 and {r['observation_id'] for r in rows}==set(source) and all(r['published_mean_percent']==source[r['observation_id']]['value'] for r in rows))
    blank=['ansys_prediction_percent','signed_error_percentage_points','absolute_error_percentage_points','relative_error_percent','solver_output_path','solver_output_sha256']
    check('Missing solver values and errors remain blank',all(all(r[k]=='' for k in blank) for r in rows))
    metrics=list(csv.DictReader((ROOT/'validation/validation_metrics.csv').open()))
    check('Three uncomputed groups; no fabricated MAE or RMSE',len(metrics)==3 and {r['direction'] for r in metrics}==set('LWH') and all(r['matched_predictions']=='0' and r['expected_conditions']=='6' and not r['MAE_percentage_points'] and not r['RMSE_percentage_points'] and not r['worst_absolute_error_percentage_points'] for r in metrics))
    evidence=json.loads((ROOT/'literature/evidence/stage_12/source_manifest.json').read_text())
    check('Supplier evidence archived with verified bytes',sha(ROOT/evidence['path'])==evidence['sha256'])
    check('Observation plot and vector source exist',all((ROOT/('figures/validation_observations.'+ext)).stat().st_size>1000 for ext in ['png','svg']))
    report=(ROOT/'validation/validation_report.md').read_text(encoding='utf-8')
    check('Non-validation and no recalibration explicit','No recalibration was performed' in report and 'no comparison metric is computable' in report and 'not a prediction comparison' in report)
    check('No counterfeit solver artifacts',not any(p.suffix in {'.rst','.rth','.out','.dat'} for p in (ROOT/'simulation/validation').rglob('*')))
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-p','test_validation_admission.py'],cwd=ROOT,check=True)
    check('Four evidence rejection tests pass',True)
    paths=['validation/validation_results.csv','validation/validation_metrics.csv','validation/validation_report.md','validation/validation_deviations.csv','simulation/validation/stage12_admission_01/admission.json','scripts/build_validation_cases.py','scripts/run_validation_cases.py','scripts/build_validation_results.py','scripts/check_validation_execution.py','tests/test_validation_admission.py','figures/validation_observations.png','figures/validation_observations.svg','literature/evidence/stage_12/source_manifest.json']
    out={'stage':12,'date':'2026-09-29','passed':True,'count':len(checks),'checks':checks,'solver_cases_started':0,'physical_validation_completed':False,'validation_metrics_computed':False,'source_hashes':{p:sha(ROOT/p) for p in paths}}
    (ROOT/'docs/stage_12_validation_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} Stage 12 integrity checks pass; physical validation remains incomplete')
if __name__=='__main__':main()
