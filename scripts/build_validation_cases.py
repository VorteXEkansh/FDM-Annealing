"""Build source-specific case specifications; unknown physical inputs remain null."""
from pathlib import Path
import csv, hashlib, json
ROOT = Path(__file__).resolve().parents[1]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    observations = list(csv.DictReader((ROOT/'validation/validation_dataset.csv').open(encoding='utf-8')))
    out = ROOT/'simulation/cases/validation'; out.mkdir(parents=True, exist_ok=True)
    for temperature in (63, 75, 86, 98, 109, 132):
        rows = [r for r in observations if r['dataset_role']=='reserved_validation' and int(r['temperature_C'])==temperature]
        case = {
            'case_id':f'LC22_free_{temperature}', 'kind':'independent_literature_validation',
            'source_doi':'10.3390/polym14132607', 'source_locator':'Sections 2.1–2.4; Tables 1–3 and 5',
            'material_identity':'Ultimaker Pearl White PLA',
            'nominal_geometry_mm':{'length':80, 'width':10, 'height':4},
            'orientation':{'roads':'longitudinal L', 'build':'H', 'transverse':'W', 'code':'XY+0'},
            'printing':{'infill_percent':100,'layer_mm':0.2,'line_mm':0.5,'nozzle_mm':0.4,'nozzle_C':215,'bed_C':60,'speed_mm_s':60},
            'oven_protocol':{'target_C':temperature,'ramp_C_min':10,'treatment_min':120,'cooling_description':'Furnace to room temperature explicitly for mould; mould-free equivalence unresolved'},
            'observation_ids':[r['observation_id'] for r in rows],
            'response':'100 (final dimension - initial dimension) / initial dimension; W and H averaged at three sections',
            'required_evidence':{k:None for k in (
                'source_compatible_thermal_functions','source_compatible_mechanical_law',
                'irreversible_strain_and_initial_state','complete_part_thermal_history',
                'support_gravity_and_release','observation_state_and_landmarks',
                'validated_nonisothermal_adapter','case_specific_convergence')},
            'comparison_bounds':{'numerical_percentage_points':None,'measurement_percentage_points':None},
            'solver_input':None, 'solver_version_target':'Ansys Student MAPDL 2026 R1 build 26.1 update 20260202',
            'calibration_changed':False,
            'protocol_sha256':sha(ROOT/'docs/validation_protocol.md'),
            'observations_sha256':sha(ROOT/'validation/validation_dataset.csv')}
        (out/(case['case_id']+'.json')).write_text(json.dumps(case,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print('Built six source-specific specifications; no solver input admitted')

if __name__=='__main__': main()
