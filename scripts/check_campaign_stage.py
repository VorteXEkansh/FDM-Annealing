"""Audit the actual empty Stage 14 campaign; do not manufacture excluded cases."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(path):
    with (ROOT/path).open(encoding='utf-8') as f:
        reader=csv.DictReader(f)
        return reader.fieldnames,list(reader)
def main():
    checks=[]
    def check(name,ok):
        assert ok,name
        checks.append({'check':name,'status':'pass'})
    design=rows('simulation/design_matrix.csv')[1]
    manifest=rows('simulation/case_manifest.csv')[1]
    fields,results=rows('data/processed/all_cases.csv')
    gate=json.loads((ROOT/'docs/stage_13_design_checks.json').read_text())
    check('Validation and dry-run prerequisites remain unmet',not gate['entry_condition_met'] and not gate['full_sweep_authorized'] and gate['dry_run_status']=='not_started_validation_prerequisite_unmet')
    check('No approved or fabricated campaign cases',design==manifest==results==[])
    check('All planned case IDs accounted for without invented exclusions',{r['case_id'] for r in design}=={r['case_id'] for r in results})
    required=['mesh_version','material_model_version','timestep_version','runtime_s','warnings','temperature_history_path','maximum_thermal_gradient_K_per_mm','time_to_setpoint_s','delta_length_mm','delta_width_mm','delta_thickness_mm','residual_strain_L','residual_strain_W','residual_strain_H','W_max_mm','residual_displacement_mm','maximum_principal_stress_MPa','residual_stress_MPa','von_mises_stress_MPa','maximum_contact_pressure_MPa','mean_contact_pressure_MPa','contact_area_mm2','reaction_force_N']
    check('Requested response and version fields have explicit schemas',all(k in fields for k in required) and len(fields)==len(set(fields)))
    check('No raw production output or dummy result files',{p.relative_to(ROOT/'data/raw').as_posix() for p in (ROOT/'data/raw').rglob('*') if p.is_file()}=={'README.md'})
    old=json.loads((ROOT/'docs/stage_13_manifest.json').read_text())['files']
    frozen=['simulation/design_matrix.csv','simulation/case_manifest.csv','validation/validation_results.csv','validation/calibration_register.csv','material/pla_properties.csv','simulation/validation/stage12_admission_01/admission.json']
    check('Design validation and property evidence unchanged',all(sha(ROOT/p)==old[p] for p in frozen))
    raw=[p for p in old if p.startswith(('simulation/verification/','simulation/convergence/'))]
    check('All prior raw reference evidence unchanged',all(sha(ROOT/p)==old[p] for p in raw))
    document=(ROOT/'docs/campaign_execution.md').read_text(encoding='utf-8')
    check('Blocked scope and unrun anomaly screens explicit','not 100% completion' in document and 'not run' in document and 'storage reservations' in document)
    paths=frozen+['docs/campaign_execution.md','data/raw/README.md','data/processed/all_cases.csv','scripts/check_campaign_stage.py','docs/stage_13_design_checks.json']
    report={'stage':14,'date':'2026-09-29','passed':True,'count':len(checks),'checks':checks,'campaign_status':'blocked_no_approved_cases_and_validation_dry_run_unmet','campaign_completed':False,'approved_cases':0,'launched_cases':0,'case_status_counts':{'SUCCESS':0,'FAILED':0,'EXCLUDED WITH DOCUMENTED REASON':0},'anomaly_screens':{k:'not_run_no_production_output' for k in ['NaNs','failed_convergence','contact_penetration','rigid_body_motion','material_validity','unrealistic_values']},'source_hashes':{p:sha(ROOT/p) for p in paths}}
    (ROOT/'docs/stage_14_campaign_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} campaign-accounting checks pass; zero approved cases; campaign blocked')
if __name__=='__main__':main()
