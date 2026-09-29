"""Stage 16 empty-source admission audit; never a surrogate or UQ calculation."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    with (ROOT / path).open(encoding='utf-8') as stream:
        return list(csv.DictReader(stream))


def main():
    frozen = json.loads((ROOT / 'docs/stage_15_manifest.json').read_text())['files']
    inputs = ['data/processed/all_cases.csv', 'simulation/design_matrix.csv',
              'simulation/case_manifest.csv', 'material/uncertainty_ranges.csv',
              'material/pla_properties.csv', 'material/fixture_properties.csv',
              'docs/stage_15_postprocessing_checks.json']
    for path in inputs:
        assert sha(ROOT / path) == frozen[path], path
    assert not rows(inputs[0]), 'New data require genuine fitting, not this empty-source audit'
    assert not rows(inputs[1]) and not rows(inputs[2])
    assert all(r['probability_model'] == 'none' for r in rows(inputs[3]))
    assert {p.relative_to(ROOT / 'data/raw').as_posix() for p in (ROOT / 'data/raw').rglob('*') if p.is_file()} == {'README.md'}
    response_path = 'data/processed/surrogate_availability.csv'
    with (ROOT / response_path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(['response', 'status', 'eligible_cases', 'model', 'cv_mae', 'cv_rmse', 'cv_r_squared', 'temperature_sensitivity', 'holding_time_sensitivity', 'gap_sensitivity', 'interval_lower', 'interval_upper', 'interval_interpretation'])
        for response in ['warpage', 'dimensional_error', 'residual_stress', 'contact_pressure']:
            writer.writerow([response, 'blocked_no_production_outputs', 0] + [''] * 10)
    input_path = 'data/processed/uncertainty_input_audit.csv'
    audit = [
        ('E', 'material/uncertainty_ranges.csv:U-001,U-002,U-010', 'Supplier intervals are cross-checks; no admitted temperature-dependent modulus distribution'),
        ('alpha', 'material/uncertainty_ranges.csv:U-012', 'Reference expansion value does not establish uncertain bounds or distribution'),
        ('k', 'material/uncertainty_ranges.csv:U-008', 'Compatible thermal conductivity function and bounds unavailable'),
        ('c_p', 'material/uncertainty_ranges.csv:U-009', 'Compatible heat capacity function and bounds unavailable'),
        ('annealing_strain', 'material/uncertainty_ranges.csv:U-003 to U-006,U-016', 'Bilayer method brackets are not bulk irreversible-strain uncertainty'),
        ('convection', 'docs/thermal_model.md', 'Production boundary coefficient and source-supported bounds not fixed'),
        ('friction', 'docs/structural_model.md', 'Verification values are numerical choices; production friction not sourced'),
        ('fixture_CTE', 'material/fixture_properties.csv;docs/material_property_audit.md', 'Candidate table has unresolved expansion convention; uncertainty bounds unavailable'),
    ]
    with (ROOT / input_path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(['parameter', 'evidence_location', 'admission_reason', 'status', 'probability_distribution', 'joint_dependence'])
        for name, source, reason in audit:
            writer.writerow([name, source, reason, 'not_admitted_for_propagation', '', ''])
    assert all(not r[key] for r in rows(response_path) for key in list(rows(response_path)[0])[3:])
    paths = inputs + [response_path, input_path, 'docs/surrogate_uncertainty_protocol.md',
                      'docs/thermal_model.md', 'docs/structural_model.md',
                      'docs/material_property_audit.md', 'scripts/check_surrogate_stage.py']
    report = {'stage': 16, 'date': '2026-09-30', 'passed': True,
              'scope': 'Evidence admission audit only; no fitting, sensitivity or propagation',
              'eligible_cases': 0, 'response_count': 4, 'uncertain_input_count': 8,
              'surrogates_fitted': 0, 'cross_validation_executed': False,
              'global_sensitivity_executed': False, 'uncertainty_propagated': False,
              'source_hashes': {path: sha(ROOT / path) for path in paths}}
    (ROOT / 'docs/stage_16_surrogate_checks.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('Stage 16 audit passed: four responses and eight input admissions; no numerical analysis')


if __name__ == '__main__':
    main()
