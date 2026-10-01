"""Independently recompute archived extraction and correction views for Stage 19."""
from pathlib import Path
import csv, hashlib, json, math, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from analysis.review_metrics import extract, relative_change


def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def rows(p):
    with (ROOT/p).open(encoding='utf-8-sig') as f: return list(csv.DictReader(f))


def main():
    output=[]; paths=set(); checks=[]; undefined=0
    for filename in ['mesh_convergence.csv','timestep_convergence.csv']:
        previous={}
        for row in rows('convergence/'+filename):
            run=row['run_path']; model=row['model']; quantity=row['quantity']
            values=extract(ROOT/run,model)
            actual=values[quantity]
            assert math.isclose(actual,float(row['value']),rel_tol=1e-10,abs_tol=1e-12),(run,quantity)
            key=(model,quantity); old=previous.get(key)
            delta=None if old is None else relative_change(actual,old)
            if old is not None and actual==0:
                undefined+=1
            elif old is not None:
                assert math.isclose(delta,float(row['delta_percent']),rel_tol=1e-5,abs_tol=1e-7)
            output.append(dict(table=filename,run_path=run,quantity=quantity,value=actual,unit=row['unit'],
                               absolute_change='' if old is None else abs(actual-old),
                               delta_percent='' if delta is None else delta,
                               interpretation='undefined_zero_denominator' if old is not None and actual==0 else 'initial_level' if old is None else 'adjacent_refinement'))
            previous[key]=actual
            paths.add('convergence/'+filename)
            paths.update(p.relative_to(ROOT).as_posix() for p in (ROOT/run).iterdir() if p.name in ['top_nodes.csv','element_stress.csv','temperature_profile.csv','contact_values.csv','reaction.csv','input.dat','manifest.json'])
    checks.append('All 63 mesh/time response values independently recomputed from raw exports')
    for row in rows('convergence/contact_sensitivity.csv'):
        values=extract(ROOT/row['run_path'],'contact')
        for a,b in [('mean_contact_pressure','mean_contact_pressure_MPa'),('maximum_contact_pressure','maximum_contact_pressure_MPa'),('maximum_penetration','maximum_penetration_mm'),('normal_reaction','normal_reaction_N_per_mm')]:
            assert math.isclose(values[a],float(row[b]),rel_tol=1e-10,abs_tol=1e-12)
        paths.update(p.relative_to(ROOT).as_posix() for p in (ROOT/row['run_path']).iterdir() if p.name in ['contact_values.csv','reaction.csv','input.dat','manifest.json'])
    checks.append('All nine contact cases: pressure mean, peak, penetration and reaction independently recomputed')
    comparisons=rows('verification/structural_verification.csv')+rows('verification/contact_verification.csv')
    for row in comparisons:
        error=abs(float(row['ansys'])-float(row['reference']))
        assert math.isclose(error,float(row['absolute_error']),abs_tol=1e-14)
        assert error<=float(row['tolerance'])
    checks.append('114 structural/contact absolute errors and fixed tolerances independently checked')
    thermal=rows('verification/thermal_verification.csv')
    for row in thermal:
        error=abs(float(row['ansys_temperature_C'])-float(row['analytical_temperature_C']))
        assert abs(error-float(row['absolute_error_C']))<=1.1e-9
        assert error<=.05 and 100*error/abs(float(row['analytical_temperature_C'])-20)<=.25
    checks.append('Nine thermal samples: absolute and excursion-relative acceptance independently checked')
    old=json.loads((ROOT/'docs/stage_18_manifest.json').read_text())['files']
    frozen=[p for p in old if p.startswith(('simulation/','verification/','convergence/','validation/','material/','data/raw/','literature/evidence/','literature/metadata/'))]
    assert all(sha(p)==old[p] for p in frozen)
    checks.append(f'{len(frozen)} prior solver/material/validation/source evidence files unchanged')
    dest=ROOT/'convergence/stage_19_audited_refinement.csv'
    with dest.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(output[0]),lineterminator='\n');w.writeheader();w.writerows(output)
    paths.update(['analysis/review_metrics.py','scripts/audit_peer_review.py','tests/test_review_metrics.py','convergence/contact_sensitivity.csv','verification/structural_verification.csv','verification/contact_verification.csv','verification/thermal_verification.csv','convergence/stage_19_audited_refinement.csv'])
    report=dict(stage=19,passed=True,checks=checks,mesh_time_response_rows=len(output),contact_response_comparisons=36,structural_comparisons=len(comparisons),thermal_samples=len(thermal),corrected_zero_denominators=undefined,prior_evidence_files=len(frozen),new_solver_runs=0,solver_rerun_decision='No input or solver solution defect found; definitions corrected and derived values independently recomputed from immutable raw exports',source_hashes={p:sha(p) for p in sorted(paths)})
    (ROOT/'docs/stage_19_numerical_audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
