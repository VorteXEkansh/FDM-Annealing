"""Record input, code and output byte hashes without implying numerical evidence."""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--stage',type=int,required=True)
args=ap.parse_args()
paths=['docs/PROJECT_STATE.md','docs/novelty_audit.md','docs/research_scope.md','docs/manuscript_restructure_map.md','docs/integrity_report.json',f'docs/stage_{args.stage:02d}_quality.md',f'docs/stage_{args.stage:02d}_literature_integrity.json','literature/literature_matrix.json','literature/literature_matrix.xlsx','literature/references.bib','manuscript/current.md','manuscript/research_scope.md','scripts/build_manuscript.py','scripts/check_integrity.py','scripts/check_literature.py','scripts/verify_delivery.py','scripts/record_stage_manifest.py','output/pdf/Constrained-Annealing-2026-DRAFT.pdf']
if args.stage >= 4:
    paths += ['docs/material_property_audit.md',f'docs/stage_{args.stage:02d}_material_integrity.json','material/pla_properties.csv','material/property_sources.csv','material/uncertainty_ranges.csv','material/fixture_properties.csv','material/build_manifest.json','scripts/build_material_database.py','scripts/check_materials.py']
scope = 'Material-property source audit and manuscript update; no solver execution or simulation findings.' if args.stage >= 4 else 'Document scope finalization; no solver execution or new quantitative findings.'
if args.stage >= 5:
    paths += ['docs/model_formulation.md','docs/constitutive_model_decision.md','docs/equation_implementation_map.csv','docs/stage_05_constitutive_tests.json','docs/stage_05_source_review.json','docs/stage_05_pdf_review.json','src/constitutive.py','tests/test_constitutive.py','scripts/check_constitutive.py','scripts/build_constitutive_reference.py','material/constitutive_reference.json','.gitattributes']
    scope = 'Constitutive reference implementation and analytical/synthetic unit tests; no ANSYS execution or physical validation.'
if args.stage >= 6:
    paths += ['docs/software_environment.md','docs/stage_06_ansys_checks.json','docs/stage_06_pdf_review.json','ansys/README.md','ansys/run_case.py','ansys/apdl/environment_smoke.dat','simulation/README.md','simulation/cases/environment_smoke.json','simulation/cases/production_template.json','simulation/runs/stage06_mapdl_smoke/mapdl.out','simulation/runs/stage06_mapdl_smoke/stage06_mapdl_smoke.err','simulation/runs/stage06_mapdl_smoke/stage06_mapdl_smoke.log','simulation/runs/stage06_mapdl_smoke/manifest.json','analysis/README.md','analysis/extract_results.py','tests/test_ansys_automation.py','scripts/check_ansys_stage.py','environment.yml','requirements.txt']
    scope='Installed Ansys environment inspection, zero-analysis MAPDL probe, and fail-closed automation; no field solution or simulation campaign.'
if args.stage >= 7:
    paths += ['.gitignore','docs/geometry_decision.md','docs/stage_07_geometry_checks.json','docs/stage_07_pdf_review.json','geometry/geometry_definition.json','geometry/candidate_clearance_audit.csv','scripts/build_geometry.py','scripts/check_geometry.py','tests/test_geometry.py','simulation/geometry/stage07_plate_gap/geometry.dat','simulation/geometry/stage07_plate_gap/gap_design.csv','simulation/geometry/stage07_plate_gap/mapdl_geometry.out','simulation/geometry/stage07_plate_gap/stage07_geometry.err','simulation/geometry/stage07_plate_gap/stage07_geometry.log','simulation/geometry/stage07_plate_gap/stage07_plate_gap.db','simulation/geometry/stage07_plate_gap/manifest.json']
    scope='Parametric specimen/fixture geometry and geometry-only MAPDL construction verification; no mesh, field solution or simulation campaign.'
if args.stage >= 8:
    paths += ['docs/thermal_model.md','docs/stage_08_thermal_checks.json','docs/stage_08_pdf_review.json','ansys/thermal_model.py','scripts/run_thermal_verification.py','scripts/check_thermal_stage.py','tests/test_thermal_verification.py','tests/test_thermal_model.py','simulation/cases/thermal_verification_plane_wall.json','simulation/cases/thermal_production_template.json','verification/thermal_verification.csv']
    durable_names={'manifest.json','input.dat','case.json','mapdl.out','comparison.csv','solver_center_temperature.csv','mesh_counts.csv','runner_stdout.log','runner_stderr.log','script_snapshot.py'}
    paths += [str(p.relative_to(ROOT)).replace('\\','/') for p in sorted((ROOT/'simulation/verification').rglob('*')) if p.is_file() and p.name in durable_names]
    paths += [str(p.relative_to(ROOT)).replace('\\','/') for p in sorted((ROOT/'simulation/verification/stage08_attempt_05').iterdir()) if p.is_file() and p.suffix.lower() in {'.rth','.rdb','.r001','.full','.esav','.ldhi','.dsp','.mntr'}]
    paths = list(dict.fromkeys(paths))
    scope='Genuine MAPDL plane-wall transient thermal verification and fail-closed production thermal contract; no production PLA coupon solution or physical validation.'
if args.stage >= 9:
    paths += ['docs/structural_model.md','docs/stage_09_structural_checks.json','docs/stage_09_pdf_review.json','ansys/structural_model.py','scripts/run_structural_verification.py','scripts/check_structural_stage.py','tests/test_structural_verification.py','verification/structural_verification.csv','verification/contact_verification.csv']
    paths += [str(p.relative_to(ROOT)).replace('\\','/') for directory in sorted((ROOT/'simulation/verification').glob('stage09_*')) for p in sorted(directory.iterdir()) if p.is_file()]
    paths = list(dict.fromkeys(paths))
    scope = 'Thermal plus six genuine structural/contact reference cases; no production annealing or independent physical validation.'
if args.stage >= 10:
    paths += ['docs/convergence_study.md','docs/stage_10_attempt_log.md','docs/stage_10_convergence_checks.json','docs/stage_10_pdf_review.json','scripts/run_convergence_study.py','scripts/check_convergence_stage.py','tests/test_convergence.py','simulation/cases/stage10_convergence_design.json','simulation/cases/stage10_convergence_design_revision_02.json','simulation/cases/stage10_convergence_design_revision_03.json','simulation/cases/stage10_convergence_design_revision_04.json','simulation/cases/stage10_convergence_design_revision_05.json','simulation/cases/stage10_convergence_design_revision_06.json','simulation/cases/stage10_convergence_design_revision_07.json','convergence/mesh_convergence.csv','convergence/timestep_convergence.csv','convergence/contact_sensitivity.csv','figures/mesh_convergence.png','figures/timestep_convergence.png','figures/contact_sensitivity.png','requirements.txt']
    paths += [str(p.relative_to(ROOT)).replace('\\','/') for p in sorted((ROOT/'simulation/convergence').rglob('*')) if p.is_file()]
    paths = list(dict.fromkeys(paths))
    scope = 'Genuine MAPDL mesh, time-step and contact-control convergence for verification configurations; no production mesh, production sweep or physical validation.'
if args.stage >= 11:
    paths += ['docs/validation_protocol.md','docs/stage_11_validation_checks.json','docs/stage_11_pdf_review.json','scripts/build_validation_dataset.py','scripts/check_validation_stage.py','analysis/validation_metrics.py','tests/test_validation_metrics.py']
    paths += [p.relative_to(ROOT).as_posix() for folder in ['validation','literature/evidence/stage_11'] for p in sorted((ROOT/folder).rglob('*')) if p.is_file()]
    paths = list(dict.fromkeys(paths))
    scope = 'Independent literature validation design and reserved source observations; no validation solve or production sweep.'
if args.stage >= 12:
    paths += ['docs/stage_12_validation_checks.json','docs/stage_12_pdf_review.json','scripts/build_validation_cases.py','scripts/run_validation_cases.py','scripts/build_validation_results.py','scripts/check_validation_execution.py','tests/test_validation_admission.py','figures/validation_observations.png','figures/validation_observations.svg']
    paths += [p.relative_to(ROOT).as_posix() for folder in ['simulation/cases/validation','simulation/validation','literature/evidence/stage_12'] for p in sorted((ROOT/folder).rglob('*')) if p.is_file()]
    paths = list(dict.fromkeys(paths))
    scope = 'Six predeclared validation specifications rejected before solver execution; physical validation incomplete; no predictions, error metrics or production sweep.'

if args.stage >= 13:
    paths += ['docs/simulation_design.md','docs/stage_13_design_checks.json','docs/stage_13_pdf_review.json','scripts/check_simulation_design.py','simulation/design_matrix.csv','simulation/case_manifest.csv']
    paths = list(dict.fromkeys(paths))
    scope = 'Production entry condition unmet; empty registries; no finalized design, dry run or full campaign.'

if args.stage >= 14:
    paths += ['docs/campaign_execution.md','docs/stage_14_campaign_checks.json','docs/stage_14_pdf_review.json','scripts/check_campaign_stage.py','data/raw/README.md','data/processed/README.md','data/processed/all_cases.csv']
    paths = list(dict.fromkeys(paths))
    scope = 'Campaign blocked with zero approved cases; no new raw production output or processed numerical response.'

if args.stage >= 15:
    paths += ['docs/postprocessing_status.md','docs/stage_15_postprocessing_checks.json','docs/stage_15_pdf_review.json','scripts/check_postprocessing_stage.py','data/processed/postprocessing_availability.csv']
    paths = list(dict.fromkeys(paths))
    scope = 'Stage 14 output availability audit only; no numerical response analysis, substitute data or plots.'

if args.stage >= 16:
    paths += ['docs/surrogate_uncertainty_protocol.md','docs/stage_16_surrogate_checks.json','docs/stage_16_pdf_review.json','scripts/check_surrogate_stage.py','data/processed/surrogate_availability.csv','data/processed/uncertainty_input_audit.csv']
    paths = list(dict.fromkeys(paths))
    scope = 'Surrogate and uncertainty admission audit; no eligible production responses, fitted models, sensitivity indices or propagated intervals.'

if args.stage >= 17:
    paths += ['docs/optimization_protocol.md','docs/stage_17_optimization_checks.json','docs/stage_17_pdf_review.json','scripts/check_optimization_stage.py','optimization/README.md','optimization/pareto.csv','optimization/confirmation.csv']
    paths = list(dict.fromkeys(paths))
    scope = 'Optimization and confirmation admission audit; no Pareto set, recommendation, robust window, new confirmation run or prediction error.'

if args.stage >= 18:
    paths += ['docs/manuscript_reconstruction_audit.md','docs/manuscript_equation_map.csv','docs/stage_18_reconstruction_checks.json','docs/stage_18_pdf_review.json','docs/stage_18_tests.txt','scripts/check_reconstruction_stage.py','scripts/build_publication_figures.py','docs/stage_18_figure_manifest.json','figures/publication/mesh_convergence.png','figures/publication/timestep_convergence.png','figures/publication/contact_sensitivity.png']
    paths = list(dict.fromkeys(paths))
    scope = 'Full verification-focused article reconstruction and regression checks; missing production science is explicitly unachieved.'

data={'stage':args.stage,'date':('2026-09-30' if args.stage >= 15 else '2026-09-29' if args.stage >= 12 else '2026-09-28' if args.stage >= 11 else '2026-09-14' if args.stage >= 10 else '2026-09-13'),'algorithm':'SHA-256','files':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'scope':scope}
(ROOT/f'docs/stage_{args.stage:02d}_manifest.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(f'Recorded {len(paths)} input/code/output hashes')
