"""Stage 17 admission audit. This does not execute optimization or ANSYS."""
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
    inputs = ['data/processed/all_cases.csv', 'simulation/design_matrix.csv',
              'simulation/case_manifest.csv', 'docs/stage_16_surrogate_checks.json',
              'data/processed/surrogate_availability.csv',
              'material/uncertainty_ranges.csv', 'docs/stage_12_validation_checks.json']
    frozen = json.loads((ROOT / 'docs/stage_16_manifest.json').read_text())['files']
    for path in inputs:
        assert sha(ROOT / path) == frozen[path], path
    assert all(not rows(path) for path in inputs[:3]), 'New cases require numerical analysis, not this empty-source audit'
    surrogate = json.loads((ROOT / inputs[3]).read_text())
    assert surrogate['surrogates_fitted'] == surrogate['eligible_cases'] == 0
    assert not surrogate['uncertainty_propagated']
    validation = json.loads((ROOT / inputs[-1]).read_text())
    assert not validation['physical_validation_completed']
    assert {p.relative_to(ROOT / 'data/raw').as_posix() for p in (ROOT / 'data/raw').rglob('*') if p.is_file()} == {'README.md'}
    schemas = {
        'optimization/pareto.csv': ['case_id', 'temperature_C', 'holding_time_min', 'constraint', 'total_reference_clearance_mm', 'W_max_mm', 'combined_dimensional_error', 'residual_stress_MPa', 'maximum_contact_pressure_MPa', 'cycle_time_s', 'objective_definition_path', 'feasibility_status', 'feasibility_reason', 'nondominated', 'source_manifest_path', 'source_manifest_sha256'],
        'optimization/confirmation.csv': ['confirmation_case_id', 'confirmation_role', 'selected_case_id', 'response', 'unit', 'frozen_prediction', 'prediction_source_sha256', 'new_ansys_solution', 'signed_error', 'absolute_error', 'relative_error_percent', 'solver_status', 'failure_reason', 'mesh_version', 'timestep_version', 'contact_version', 'thermal_match_status', 'raw_manifest_path', 'raw_manifest_sha256'],
    }
    for path, columns in schemas.items():
        target = ROOT / path
        if target.exists():
            assert not rows(path), 'Refusing to overwrite recorded optimization or confirmation evidence'
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('w', encoding='utf-8', newline='') as stream:
            csv.writer(stream, lineterminator='\n').writerow(columns)
    paths = inputs + list(schemas) + ['optimization/README.md', 'docs/optimization_protocol.md', 'scripts/check_optimization_stage.py']
    report = {'stage': 17, 'date': '2026-09-30', 'passed': True,
              'scope': 'Evidence admission and empty registry integrity only',
              'eligible_predictions': 0, 'pareto_computed': False,
              'feasibility_evaluated': False, 'priorities_evaluated': [],
              'desirability_used': False, 'robust_window_identified': False,
              'confirmation_points_selected': 0, 'new_ansys_runs_launched': 0,
              'confirmation_completed': False, 'prediction_errors_computed': False,
              'source_hashes': {path: sha(ROOT / path) for path in paths}}
    (ROOT / 'docs/stage_17_optimization_checks.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('Stage 17 admission audit passed; optimization and new confirmation remain unexecuted')


if __name__ == '__main__':
    main()
