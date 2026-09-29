"""Stage 12 execution admission record. Never substitutes a verification problem.

The source-specific solver adapter is not implemented: this entry point cannot
launch MAPDL merely by toggling an admission flag. A future admitted adapter
must implement and verify physical inputs before changing that behavior.
"""
from pathlib import Path
import argparse, csv, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=('source_compatible_thermal_functions','source_compatible_mechanical_law',
          'irreversible_strain_and_initial_state','complete_part_thermal_history',
          'support_gravity_and_release','observation_state_and_landmarks',
          'validated_nonisothermal_adapter','case_specific_convergence')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def blockers(case):
    evidence=case.get('required_evidence',{})
    missing=[key for key in REQUIRED if not isinstance(evidence.get(key),dict) or not evidence[key].get('path') or not evidence[key].get('sha256')]
    # Presence alone is not admission; check any future referenced evidence bytes.
    for key in REQUIRED:
        item=evidence.get(key)
        if key not in missing:
            path=(ROOT/item['path']).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file() or sha(path)!=item['sha256']:
                missing.append(key)
    missing.append('source_specific_solver_adapter_not_implemented')
    return missing

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--execute',action='store_true');args=ap.parse_args()
    out=ROOT/'simulation/validation/stage12_admission_01'
    if out.exists(): raise FileExistsError('Admission record is immutable; choose a new version for changed evidence')
    out.mkdir(parents=True)
    cases=[]; hashes={}
    for p in sorted((ROOT/'simulation/cases/validation').glob('LC22_free_*.json')):
        case=json.loads(p.read_text(encoding='utf-8')); reasons=blockers(case)
        cases.append({'case_id':case['case_id'],'temperature_C':case['oven_protocol']['target_C'],
                      'status':'blocked_before_solver','blockers':reasons,'observation_ids':case['observation_ids'],
                      'solver_started':False,'solver_command':None,'solver_returncode':None,
                      'comparison_status':'not_evaluated_no_prediction'})
        hashes[p.relative_to(ROOT).as_posix()]=sha(p)
    if len(cases)!=6: raise ValueError('All six frozen conditions must be retained')
    for name in ['scripts/run_validation_cases.py','scripts/build_validation_cases.py','docs/validation_protocol.md','validation/validation_dataset.csv','validation/calibration_register.csv','material/pla_properties.csv']:
        hashes[name]=sha(ROOT/name)
    report={'stage':12,'date':'2026-09-29','execution_requested':args.execute,
            'cases':cases,'solver_cases_started':0,'validation_completed':False,'input_hashes':hashes,
            'meaning':'Pre-solver evidence rejection, not an ANSYS failure or numerical solution'}
    (out/'admission.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Six cases rejected before solver execution; see '+str(out/'admission.json'))
    return 2 if args.execute else 0

if __name__=='__main__': raise SystemExit(main())
