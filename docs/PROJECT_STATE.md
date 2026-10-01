# Authoritative project state

Stage: **Prompt 19/20 — scientific audit and corrections; production study remains incomplete**.
Date: 2026-10-01 (Asia/Calcutta).
Repository: https://github.com/VorteXEkansh/FDM-Annealing

## Research identity

This is a computational thermo-mechanical study intended for genuine ANSYS execution. The finalized primary question is: for a specified FFF-PLA grade, print architecture and geometry, how do annealing temperature, holding time and initial fixture clearance influence transient thermal exposure and irreversible dimensional change, warpage and residual stress evaluated after cooling and release, relative to free annealing within an evidence-supported sub-melting domain?

Current manuscript: `manuscript/current.md`.
Current PDF: `output/pdf/Constrained-Annealing-2026-DRAFT.pdf`.
Base source: `data/source/DTU_Constrained_Annealing_Final_Submission.pdf`; immutable, with SHA-256 in `data/source/manifest.json`.

## Completed in Stage 1

- Read all 24 base pages, including references, figures, tables and both appendices; visually reviewed the page renders.
- Created section-level conversion audit, figure/table disposition inventory and restructuring map.
- Replaced experimental allocation, tensile/flexural confirmation and literature-only Results with a computational formulation and evidence requirements.
- Retained proposed 80 °C, 95 °C, 110 °C and 30 min, 60 min, 90 min as inherited design levels, not validated treatment recommendations.
- Defined clearance, signed dimensions, aggregate error, warpage reference, cooled/released reporting state and independent validation requirements.
- Corrected ASTM F3498 in base Table 7 to F3489-23 and corrected its title in the retained bibliography. Its role is literature appraisal, not certification of a simulation.
- Replaced objective numbering beginning at 7 with objectives 1–5; removed duplicated base Figures 3/5 from the new manuscript.
- Initialized repository structure, provenance registries, PDF build and stage integrity checks.

## Evidence status — authoritative

Genuine ANSYS field evidence now includes **one accepted Stage 8 thermal reference case, six accepted Stage 9 structural/contact reference cases, and 28 unique Stage 10 runs selected for convergence tables**. Stage 10 preserves 43 technical run directories in total; 15 superseded or defective-measurand/input-control attempts are excluded from conclusions. None is a Prusament PLA coupon prediction or physical validation. A zero-analysis MAPDL environment/license probe and a geometry-only build also succeeded.
ANSYS environment: **Ansys Student 2026 R1; MAPDL release 2026 R1, build 26.1, update 20260202; Student Mechanical product checkout confirmed**. Workbench and Mechanical 26.1 plus the named thermal/structural templates are installed, but their GUI entitlements have not been separately exercised. PyMechanical is not installed.
Geometry/CAD: **60 mm × 10 mm × 4 mm rectangular specimen and two 70 mm × 20 mm × 5 mm plates selected; a geometry-only MAPDL build created and saved three volumes**. Production specimen/fixture mesh: **not generated**. The separate plane-wall verification mesh is documented below.
Reference PLA formulation: **Prusament PLA selected for constitutive development; production ANSYS material card not admitted**.
Property tables: **created and source-audited; compatible Prusament k(T), c_p(T), bulk irreversible strain and complete orthotropy remain unavailable**. Stage 8 verification constants are numerical fixtures kept outside the material database.
Constitutive implementation: **small-strain isotropic 23-branch Prusament reference implemented; 38 analytical/synthetic unit tests pass; isothermal ANSYS Prony adapter checked in Stage 9; no non-isothermal adapter or physical validation**.
Fixture material: **AISI 304 stainless steel selected as candidate plate material with a 20–200 °C tabulated property set**. Plate dimensions and normalized reference-gap levels are fixed as geometry design choices. Friction, thermal contact conductance and physical spacer geometry remain unselected. Thermal-strain use of the fixture alpha table is blocked until its tangent/mean convention and reference temperature are established.
Initial residual stress, recovery strain and crystallization kinetics: **unavailable**.
Production boundary histories, reference temperature, release rule, convection, radiation and thermal contact: **not fixed**. The separate verification history is fully specified and must not be transferred as a physical protocol.
Mesh/time-step/contact convergence: **passed for three declared Stage 10 verification configurations only**. Structural, thermal, and normal-Lagrange contact benchmark grids plus thermal and structural time increments were selected and confirmed. No three-dimensional production mesh or production time step is selected.
Independent validation datasets: **45 published observations extracted; 18 mould-free means reserved for conditional source-specific reproduction, 24 context records excluded, and three secondary maxima quarantined. No validation solve or physical validity claim.**
Sensitivity indices, uncertainty intervals and optimization results: **none**.
No performance improvement, optimal process condition or experimental confirmation is claimed.

## Software and automation state — Stage 6

`docs/software_environment.md` is the exact environment record. The installed package is R261RC2P01. The host is Windows 11 build 10.0.26200 on an AMD Ryzen 7 7435HS with 8 physical cores, 16 logical processors and 15.82 GiB installed RAM. The official 2026 R1 Student page states a 128,000-node/element structural limit, no geometry export and up to four HPC CPU cores.

`ansys/run_case.py` provides a direct MAPDL batch path with explicit JSON parameters and admission gates. `simulation/cases/production_template.json` remains blocked because compatible thermal data, irreversible strain, the Ansys constitutive adapter, boundary history and extraction definitions are unresolved. Stage 8 adds `ansys/thermal_model.py` and `simulation/cases/thermal_production_template.json`; they require all thermal phases and reject missing PLA functions, convection, radiation decisions, thermal contact and production extraction rules. `analysis/extract_results.py` rejects empty or untraceable output tables. No production campaign was run.

The Stage 6 execution is `simulation/runs/stage06_mapdl_smoke/`, generated from `ansys/apdl/environment_smoke.dat`. MAPDL exited 0 after `/STATUS` and `/EXIT,NOSAVE`; it created no geometry, nodes, elements, loads or solution. Its case, input, command, raw log and output hashes are recorded. DesignXplorer and optiSLang 26.1.0 revision 1878 are present on disk but unexercised. Their availability must not be described as a completed optimization capability.

## Decisions and scientific safeguards

1. Use two opposed plate surfaces with stops as the primary GAP fixture concept. Define total initial free clearance at the reference temperature. Do not inherit the unverified 0.05 mm hot clearance as a property or optimum.
2. Use ANSYS transient thermal and history-dependent structural/contact analysis when justified by material evidence. The material-point reference is executable; the full thermal/contact workflow is not yet an executable production model.
3. Reversible thermoelasticity alone cannot establish permanent annealing recovery. A source-backed irreversible/history-dependent description or explicitly limited phenomenological model is required.
4. Do not impose symmetry, clamped specimen faces or uniform recovery merely to force low warpage. Quantify rigid-body stabilization and contact effects.
5. FREE is mechanically traction-free with no fixture contact; GAP is initially centered between opposed faces, without preload. Omit gravity in the primary paired comparison as an explicit isolation assumption. Any supported/gravity-dependent literature reproduction is a separate labeled configuration. Granular supports are literature context; DEM, sand/salt modeling and remelting are excluded.
6. Do not infer UTS, ductility or strength improvement from von Mises stress or displacement. No new physical specimens or UTM testing are required by this project.
7. Hold durations need a defined part-temperature attainment criterion. Equal oven histories need not mean equal part histories; separate process comparison from thermally matched mechanism comparison.
8. Verify numerical error before calibration/validation. Reserve independent literature observations before fitting; calibration agreement is not validation.
9. Do not assign probability distributions or tolerance thresholds without evidence/declared justification. Deterministic sweeps do not produce experimental confidence intervals.

## Literature state — Stage 2

A new critical investigation through 12 September 2026 retains 34 DOI-verified journal papers and the previously verified ASTM standard. See `literature/literature_matrix.xlsx`, `literature/literature_matrix.json`, `literature/references.bib`, `literature/doi_verification.json`, `docs/literature_search_strategy.md` and `docs/novelty_audit.md`. Eight full texts were retrieved for targeted appraisal; remaining studies have explicit abstract/excerpt access limits. The old four-entry `data/literature/verified_sources.json` is the immutable Stage 1 admission record, not the complete current bibliography.

The complete manuscript now includes the critical literature review, ten closest competitors and narrowed novelty. Supported annealing, ANSYS/irreversible thermal strain, Prony/WLF recovery models, coupled thermal/crystallization mechanics, and annealed PLA FE/optimization all have precedents. The provisional intended contribution is evidence-tested prediction of the clearance–distortion–stress trade-off after cooling and release. No exclusive priority claim is supported. Full protocols for abstract-level competitors must be recovered before publication-level priority assertions.

Stage 4 adopts a restricted Prusament constitutive evidence set and a candidate AISI 304 fixture table; no validation target is adopted. Bute2024 remains a recovery-mechanism comparator because it uses Black Devil Design PLA. Wijnen2018 and Trofimov2022 remain thermal/warpage comparators; Trofimov's property table is not merged because it combines Raise3D measurements with transferred literature functions. None validates the proposed fixture's residual stresses or contact pressures. The Mould2022 final PLA Table 7 temperature conflicts with Tables 2–3; affected values remain unaccepted. Tough, high-heat, recycled and filled PLA remain separate from neat PLA.

## Scope finalized in Stage 3

Candidate title: **Free and gap-constrained annealing of FFF-printed PLA: a thermo-mechanical computational study**.

`docs/research_scope.md` records one primary question, five secondary questions (SQ1–SQ5), five objectives and four testable numerical propositions (H1–H4). The manuscript incorporates their full text, an explicit intended contribution and excluded claims. The structured abstract contains context/question, planned approach, results status and intended contribution, without invented numerical findings.

The core study uses one selected formulation, fixed print architecture and a three-dimensional 60 mm × 10 mm × 4 mm plate coupon. The formulation was selected in Stage 4 and the geometry in Stage 7; print architecture remains an evidence-dependent implementation choice. Full deposition-process simulation, printing-parameter optimization and comparisons across PLA grades are outside the primary study.

The main comparison applies the same external thermal schedule; matched part-temperature diagnostic cases may isolate mechanical restraint. Final responses are evaluated at a common reference temperature with an explicitly declared release/observation time. In-fixture dimensions, released warpage and conditional residual stress remain separate. Hypotheses concern a resolved clearance effect, release effect, interaction and geometric/stress trade-off; none assumes a favorable or monotonic result. Numerical resolution/extraction criteria must be specified before assessing them.

The intended contribution is an evidence-tested clearance–distortion–stress assessment. It is not an achieved result or exclusive-priority claim. Stress/contact validation cannot be inferred from geometric agreement. No new experiments, strength/ductility enhancement, universal law, granular-support superiority, certification, durability or global optimum are promised. Processing recommendations require an independently supported benefit criterion as well as verified responses.

## Material-property state — Stage 4

Authoritative files are `material/pla_properties.csv`, `material/property_sources.csv`, `material/uncertainty_ranges.csv`, `material/fixture_properties.csv` and `material/build_manifest.json`. `scripts/build_material_database.py` deterministically regenerates the four CSV files. `docs/material_property_audit.md` records the compatibility reasoning. Raw Stage 4 evidence copies and their hashes are preserved under `literature/evidence/stage_04/`.

Prusament PLA is the reference formulation because Chapuis2025 provides grade-specific DMA characterization, k₀ = 10.598 MPa, ν = 0.35, T_g = 65 °C, C₁ = 17.4, C₂ = 51.6 K, C₃ = 35 000 K, α = 68.0 µm m⁻¹ K⁻¹ and 23 Maxwell branch pairs. Direct characterization spans 23–85 °C. The calculated reference instantaneous modulus is E₀ = k₀ + ∑kᵢ = 1691.594 MPa; this is an arithmetic model quantity, not a new experiment. The published piecewise shift uses Arrhenius below T_g and WLF at or above T_g. The native isothermal Prony conversion is checked in Stage 9; full temperature shifting remains unverified.

The inherited 80 °C candidate lies inside the direct characterization interval. The 95 °C and 110 °C candidates lie outside it and are not admitted through extrapolation. The supplier's ρ = 1240 kg m⁻³ is retained only as a screening value because its test temperature is not reported. No compatible Prusament k(T) or c_p(T) functions, signed bulk irreversible annealing-strain law, complete E₁/E₂/E₃/G₁₂/G₂₃/G₁₃/ν₁₂/ν₂₃/ν₁₃ set, directional α₁/α₂/α₃ set, or crystallization-kinetic coefficients were found. Missing lower/upper bounds remain blank with status `no bound invented`.

The Chapuis programmed ε₁₁^AM values are retained with same-source method brackets but are not accepted as bulk annealing shrinkage. Bute2024 directional irreversible strain, Li2024 FormFutura orthotropy, Relaxation2022 SUNLU PLA Plus relaxation, Luberto2024 unidentified-PLA thermal constants and Trofimov2022 mixed-source Raise3D properties remain clearly labelled comparators. No numerical property is transferred across formulations.

AISI 304 stainless steel is the candidate opposed-plate material. Meng2026 Table 1 provides ρ(T), c_p(T), k(T), α(T), E(T) and ν(T) at 20 °C, 100 °C and 200 °C, bracketing 20–110 °C without extrapolation. The fixture property table is a candidate engineering input. Actual alloy heat, dimensions, surface condition, friction and PLA–steel contact conductance remain open.

No probability distribution is assigned. Reported supplier intervals and same-source method brackets are preserved without reinterpreting them as confidence intervals. Cross-formulation minima and maxima are not treated as Prusament uncertainty bounds.

## Constitutive-model decision — Stage 5

`docs/constitutive_model_decision.md` and `docs/model_formulation.md` fix the strongest currently supported core: small-strain isotropic thermorheologically simple generalized-Maxwell response for Prusament PLA, with constant ν and reversible α, and the full source Arrhenius/WLF clock. `src/constitutive.py` implements the reference; `material/constitutive_reference.json` records the calculated shear/bulk conversion and evidence gates. It is not an ANSYS material card.

The macroscopic elastic-plus-delayed strain partition is defined through instantaneous compliance; branch stress evolution supplies the delayed response. Identical normalized shear and bulk spectra preserve the assumed constant ν. The source is a plane-stress shell model; its three-dimensional isotropic extension remains a constitutive assumption. No independent E(T) multiplier, orthotropic law, crystallization kinetics or bulk irreversible annealing-strain law is added.

The implemented temperature guard is 23–85 °C, with 23 °C used only as a numerical-test thermal reference and 65 °C as the relaxation reference. The 20 °C PLA start and the inherited 95 °C/110 °C conditions are rejected. The temperature interval does not itself validate 30–90 min holds, arbitrary strains or bulk geometries. The algorithm integrates history through reduced time and requires temperature subdivision at 65 °C; material-point refinement tests are not ANSYS time-step convergence.

Irreversible annealing strain, crystallization, production assembly and fixture thermal strain raise explicit evidence-gap errors. No missing mechanism is defaulted to a physical zero. The AISI 304 table can be interpolated and used for instantaneous elastic reference calculations, but its expansion convention is unresolved. Thermal-field closures, initial printed state, duration/strain applicability and physical validation remain open.

`tests/test_constitutive.py` and `scripts/check_constitutive.py` execute 38 numerical unit tests; individual outcomes and input/code hashes are in `docs/stage_05_constitutive_tests.json`. Analytical checks and synthetic cases are not independent material validation data. At the Stage 5 boundary, no ANSYS run had been executed. `docs/equation_implementation_map.csv` maps every manuscript governing equation to its reference function or designated future field/postprocessing operation. No optional crystallization or desirability equation is retained.

Three ignored temporary comparator evidence files were copied byte-for-byte into `literature/evidence/stage_05/` and the material source paths were repaired. Raw evidence and hashed database/report bytes are protected against Git line-ending conversion. The SUNLU paper's author metadata was corrected to Bertocco et al. without altering reported property values. Stage 4 records are retained as historical snapshots; the current database build manifest is Stage 5.

## Geometry state — Stage 7

`docs/geometry_decision.md` and `geometry/geometry_definition.json` are authoritative for geometry. The specimen dimensions reproduce the regular plate in Trofimov et al. (2022), Figure 4(a), DOI 10.1016/j.addma.2022.102693. Only the geometry is reused: the source's Raise3D Premium PLA, deposition history and response data are not transferred to Prusament PLA. The selected plate has a 2400 mm³ volume, 600 mm² nominal area per opposed face, and aspect ratios L/h = 15, W/h = 2.5 and L/W = 6.

GAP uses two 70 mm × 20 mm × 5 mm AISI 304 plates, each with 5 mm plan margin around the centered specimen. FREE omits those volumes. The total reference clearance is g₀ = H₀ − h₀ and γ = g₀/h₀. Declared screening levels γ = 0, 0.0025, 0.005, 0.01 and 0.02 give g₀ = 0, 0.01, 0.02, 0.04 and 0.08 mm. They are geometric design levels, not measured tolerances or an optimum.

The Prompt 7 absolute candidates are explicitly evaluated in `geometry/candidate_clearance_audit.csv`. The 0 mm endpoint is retained. The 0.025 mm and 0.050 mm candidates are represented inside the normalized near-contact screen rather than added as redundant levels. The 0.100 mm and 0.200 mm candidates are deferred, not ruled out, because no supported free-deformation scale yet justifies reducing near-contact resolution to include 2.5% and 5% thickness gaps.

`scripts/build_geometry.py` validates the definition, calculates the gap table and writes a parameterized MAPDL deck. One geometry-only invocation at γ = 0.01 exited 0, reported three volumes and saved `stage07_plate_gap.db`. The immutable input/output hashes are in `simulation/geometry/stage07_plate_gap/manifest.json`. There is no mesh, element type, material assignment, boundary condition, load, analysis type or solve command. Spacer geometry is deferred because its thermal expansion convention and attachment are unresolved.

## Transient thermal state — Stage 8

`docs/thermal_model.md` is the authoritative thermal-method record. Stage 8
executes a verification-only 1 mm × 1 mm × 10 mm plane wall with adiabatic side
faces and convection on both thickness faces. The numerical fixtures are k =
0.5 W m⁻¹ K⁻¹, c<sub>p</sub> = 1000 J kg⁻¹ K⁻¹, ρ = 1000 kg m⁻³ and h =
5 W m⁻² K⁻¹, giving Bi = 0.05. They are not PLA properties.

The reference begins at 20 °C, ramps the ambient to 80 °C over 0–300 s, holds
the ambient at 80 °C through 900 s, ramps it to 20 °C over 900–1200 s and holds
20 °C through 1800 s. MAPDL 2026 R1 used 640 mapped SOLID70 elements, 1025
nodes, 40 elements through thickness and a fixed 0.25 s step. The accepted run
is `simulation/verification/stage08_attempt_05`; it exited 0 with no MAPDL error
messages. Its exact input, raw binary result, solver output, extracted table,
code and hashes are preserved.

The reference calculation uses the exact one-dimensional plane-wall step
response, 200 roots of ζ tan ζ = Bi and Duhamel superposition integrated over
each linear ambient segment. Nine center temperatures are compared in
`verification/thermal_verification.csv`. The maximum absolute error is
0.005180700 °C; the maximum conventional relative error is 0.001700533% using
kelvin, and the maximum error relative to the temperature excursion is
0.157660518%. The predeclared acceptance limits were 0.05 °C and 0.25%
excursion-relative error, so the verification passes.

Four failed solver/postprocessing attempts remain traceable: attempt 01 had an
unusable APDL extraction; attempts 02 and 03 missed the unchanged numerical
accuracy limit at 5 s and 1 s; attempt 04 terminated with a Windows file-mapping
error in the OneDrive working directory. Attempt 05 ran the unchanged 0.25 s
problem in local scratch and copied closed files back. This is benchmark
time-integration refinement, not production time-step convergence.

The verification confirms the implemented linear conduction, two-face
convection, ramp/hold/cooling history and center-temperature extraction only.
Radiation and thermal contact are omitted to preserve the analytical problem.
It does not verify Prusament thermal properties, the production coupon/fixture,
fixture heat transfer, radiation, PLA–steel contact, mesh convergence, physical
predictive validity, dimensional change, warpage or stress. The full FREE/GAP
thermal model remains blocked; no missing property or boundary coefficient is
set to zero.

## Structural state — Stage 9

`docs/structural_model.md` defines six separate uniform-field cases: free and
fixed thermal expansion, free and fixed/released retained eigenstrain, a
node-to-node gap and 23-branch isothermal Prony response. Each brick is
10 mm × 1 mm × 1 mm, with one SOLID185 and eight nodes. Contact adds a fixed
ninth node and one CONTA178. These are verification choices, not the production
coupon geometry or mesh-convergence evidence.

Elastic constants and the −0.001 isotropic eigenstrain are synthetic fixtures.
Initial stress −C:εᵃⁿⁿ supplies the retained-eigenstrain test; no calibrated
bulk annealing-strain evolution law exists. Orthotropy is not used. The Prony
test uses the source-derived 23 equal normalized shear/bulk spectra at 65 °C,
with finite loading, holding, unloading and held-zero-strain relaxation.
It does not verify piecewise temperature shifting or physical validity.

`verification/structural_verification.csv` and `verification/contact_verification.csv`
record solver/reference values, errors, tolerances and run paths. Every run
preserves its script snapshot and input/output hashes. Contact sign-conversion
and license failures and the first relaxation accuracy failure are preserved.
Subsequent solver runs must be sequential under the observed Student limit.
Production remains blocked by thermal inputs, irreversible-strain evidence,
non-isothermal adaptation, fixture expansion convention, surface contact,
friction, release rules and independent validation.

## Convergence state — Stage 10

`docs/convergence_study.md` is authoritative for the numerical study. Raw MAPDL
evidence is under `simulation/convergence/`; every directory retains its input,
script snapshot, solver files, extraction, result and manifest hashes. The
published tables are `convergence/mesh_convergence.csv`,
`convergence/timestep_convergence.csv` and
`convergence/contact_sensitivity.csv`.

The structural benchmark is a 60 mm × 4 mm plane-stress, two-layer isothermal
Prony cantilever at 65 °C. A declared 10× relaxation-time mismatch creates
simultaneous post-unload curvature, displacement and self-equilibrated stress;
it is a numerical fixture, not a measured PLA layer property. A 90 × 12 grid is
confirmed by 120 × 16: changes are 0.9327% for Wₘₐₓ, 0.5821% for residual
displacement and 2.0266% for the interior 95th-percentile residual stress.

The Stage 8 plane-wall benchmark uses 8, 16, 32 and 64 through-thickness
elements. The 32-element grid is confirmed by 64; the 300 s lag and gradient
change by 0.0009423% and 0.0060073%. The selected verification step Δt = 0.25 s
is confirmed by 0.125 s; lag, gradient and the L₂ profile-excursion measure
change by 0.005285%, 0.005369% and 0.002811%.

The corrected 2D contact benchmark uses CONTA172/TARGE169. Normal Lagrange with
40 interface elements on a 40 × 16 solid grid is confirmed by 60 interface
elements on 60 × 24: mean pressure, peak pressure and reaction change by
0.12698%, 0.36127% and 0.13831%, and reported penetration remains 0 mm. This
selects a verification configuration only. Penalty/augmented FKN and μ = 0,
0.1, 0.3 sensitivities are genuine numerical fixtures; no production friction
coefficient is selected.

The structural time pair 0.01 s on ramps and 0.1 s on holds is confirmed by
0.005 s and 0.05 s; Wₘₐₓ, displacement and stress change by 0.003094%,
0.003213% and 0.13636%. All final verification refinement pairs meet the
predeclared limits. The earlier non-passing or defective attempts remain listed
in `docs/stage_10_attempt_log.md`.

Production discretization remains blocked because the production material,
irreversible strain, thermal boundary/contact, friction, release and 3D surface
contact definitions do not exist. Verification convergence cannot qualify an
unbuilt production model. No production sweep was run.

## Completion records and stage boundary

Current records: `docs/stage_10_convergence_checks.json`,
`docs/stage_10_quality.md`, `docs/stage_10_attempt_log.md`,
`docs/stage_10_pdf_review.json`, `docs/stage_10_manifest.json`,
`docs/stage_10_delivery.json` and `docs/integrity_report.json`.
No production campaign, physical validation, sensitivity, propagated uncertainty
or optimization is complete. Stage 10 contact-control variation is numerical
model sensitivity, not the later global physical-input sensitivity study. Stages 11 and 12 are documented below; the original Stage 10 records remain historical.

Stage 9 result: all 114 comparisons pass. Maximum stress error is 3.8271 × 10⁻⁶ MPa; maximum reaction error is 3.8280 × 10⁻⁶ N. Accepted runs are free_01, fixed_01, eigen_free_01, eigen_fixed_01, contact_03 and visco_02 under simulation/verification/stage09_.

Stage 10 result: all final verification refinement pairs pass the predeclared
limits. The authoritative values are the three CSV files under `convergence/`.
No production mesh, physical validation result or production response is claimed.


## Validation design — Stage 11 (frozen protocol)

docs/validation_protocol.md is the pre-solve protocol. The existing literature matrix was screened; two primary full-text XML sources and fresh Crossref DOI metadata are archived under literature/evidence/stage_11/, with hashes in validation/source_manifest.json. The old literature matrix is a historical appraisal; this protocol supersedes its candidate-validation status without overwriting evidence.

validation/validation_dataset.csv contains 45 actual published observations, reproducibly extracted by scripts/build_validation_dataset.py: all 42 PLA entries in Lluch-Cerezo et al. (2022), Table 5, plus the three PLA maxima in Stojković et al. (2023), Table 8. Predictions, errors and unavailable response scatter remain blank.

The primary reserved set is 18 directional means at 63, 75, 86, 98, 109 and 132 °C without a powder mould. It requires a separate 80 mm × 10 mm × 4 mm Ultimaker Pearl White PLA reproduction; the project Prusament coefficients are not transferable. Powder-supported values remain context. The 155 °C group is excluded for overlap with the source melting range; the Table 7 temperature conflict remains unresolved. Lower-temperature Table 5 rows are independently unambiguous. Actual cooling/support histories, material law, initial state and response uncertainty still gate execution.

The secondary PrimaSelect PLA PRO records are reported maxima, not case means, and their sign/selection semantics and detailed protocol are insufficient for admitted quantitative validation. They remain quarantined. No R², pooled dimensional score, stress/contact/warpage validation or uncertainty intervals are claimed.

validation/calibration_register.csv fixes Chapuis2025 DMA/Maxwell/shift and bilayer pre-strain lineage as calibration-related. External reserved observations have not been used for fitting. Reservation is prospective but not blinded. Any tuning to a reserved condition reclassifies all its correlated directions as calibration and requires a new independent set.

analysis/validation_metrics.py implements signed and absolute error, zero-safe relative error, MAE, RMSE and deterministic discrepancy interpretation. Four synthetic arithmetic tests pass. Missing measurement or numerical bounds yield indeterminate status; compatible bounds are not proof of validity. Six condition means per direction are not independent specimen residuals. The complete manuscript now includes source selection, the reserved experimental table, split rules, response mapping, metrics and admission limits.

Stage 11 creates no new solver output and no production sweep. The production model and physical validation remain blocked by the previously identified material, boundary and metrology gaps. Current records are docs/stage_11_validation_checks.json, docs/stage_11_quality.md, docs/stage_11_pdf_review.json, docs/stage_11_manifest.json, docs/stage_11_delivery.json and docs/integrity_report.json. Stage 12 was subsequently authorized; retain this protocol unchanged.


## Validation execution — Stage 12 (unchanged evidence)

Scientific status: **independent validation remains incomplete and blocked**. No ANSYS validation run started. The six source-specific case specifications in simulation/cases/validation/ retain the published nominal geometry, architecture, oven ramp and treatment. Missing material/history/boundary inputs remain null. scripts/run_validation_cases.py --execute rejected all six before solver launch; simulation/validation/stage12_admission_01/admission.json preserves nine blockers per case and input/code hashes. This is an evidence rejection, not a numerical convergence failure or a measured mismatch.

The primary source protocol was re-read and a targeted supplier/material search was conducted on 29 September 2026. The three-page manufacturer PLA data sheet is archived with its URL and hash in literature/evidence/stage_12/. It does not supply the required annealing recovery law or thermal functions and uses different print conditions. No coefficients were transferred into the material database. The Stage 11 protocol, calibration register, observed values, metric implementation and material values remain unchanged. No recalibration occurred.

validation/validation_results.csv records all 18 primary means with blank predictions/errors. validation/validation_metrics.csv retains three groups with six expected conditions and zero matched predictions; no MAE or RMSE is computable. validation/validation_deviations.csv records the known differences and unresolved matches. validation/validation_report.md explains the attempted admission, limitations, source search and required recovery. figures/validation_observations.png and .svg show only source observations; no parity plot can exist without predictions.

Four evidence-admission tests and the full 81-test repository suite pass. These are code tests, not physical validation. Required recovery includes source-compatible thermal/mechanical/irreversible-strain characterization and initial state, complete specimen thermal and mechanical boundaries, observation mapping, non-isothermal adapter, source-specific convergence and comparison uncertainty. New fitting needs an explicitly declared calibration lineage and cannot consume the reserved observations without reclassification and a new independent validation set.

The full manuscript has an integrated validation-execution results/diagnosis section and revised abstract, evidence status and conclusions. Current integrity/delivery records use the stage_12 prefix. No validation success, production sweep, optimization or physical recommendation is authorized by this outcome. Documentation is complete; the requested numerical validation remains scientifically unachieved. Stop at Prompt 12; do not proceed automatically to Prompt 13.


## Production design entry — Stage 13 (unchanged prerequisite)

The user's condition “Only proceed if validation is acceptable for the research objectives” is not met. Stage 12 supplies no validation predictions or errors, and the production grade and fixture objectives remain unvalidated. The production matrix is not finalized and no representative low/middle/severe run starts.

simulation/design_matrix.csv and simulation/case_manifest.csv are header-only registries with zero approved cases. docs/simulation_design.md documents the entry decision, candidate-versus-approved distinction, deferred identifier/units contract and requirements for resumption. Example G025/G050 names do not approve new gaps. FREE is not zero-gap contact. No identifiers or production solver jobs are generated. The frozen validation protocol, calibration split, material database and Stage 12 evidence remain unchanged.

scripts/check_simulation_design.py verifies the blocked condition and empty registries. Passing these integrity checks is not a passing automation dry run. Production automation, field extraction, convergence and raw-output preservation have not been tested on production cases. The manuscript's simulation-design section, abstract and conclusions now reflect that boundary.

Current stage records use stage_13. Documentation and delivery are complete when those records pass; production design and dry-run objectives remain unachieved. Recovery first requires acceptable independent validation and applicability to the admitted production material, domain and objectives, followed by production-specific convergence. Do not advance to Prompt 14 or execute a full sweep.


## Parametric campaign — Stage 14 (unchanged source evidence)

No approved rows exist in simulation/design_matrix.csv; the case manifest is also empty. Independent validation and representative dry-run prerequisites remain unmet. No production ANSYS job was launched and no full campaign was completed. SUCCESS, FAILED and EXCLUDED case counts are all zero because the approved plan is empty, not because a sweep succeeded. No candidate cases were fabricated as exclusions.

Created data/processed/all_cases.csv as a header-only response/metadata registry. data/raw/ contains only its storage policy; no actual production export exists. Prior immutable solver verification evidence stays at its original paths and is not relabeled. docs/campaign_execution.md records scope, units, absent responses and recovery conditions. scripts/check_campaign_stage.py checks actual approved-case accounting, frozen inputs and prior raw-evidence hashes. All production anomaly screens remain not run, including NaNs, convergence, penetration, rigid-body motion, material validity and plausibility; none is claimed to pass.

The full manuscript now integrates production result availability and campaign status with revised abstract/conclusions. Stage 14 integrity records distinguish documentation from scientific completion. Required recovery remains independent validation, applicability to the production objectives/domain, an approved design and a passed representative dry run. No sensitivity, optimization or processing claim is enabled. Stop at Prompt 14; do not advance automatically to Prompt 15.


## Postprocessing — Stage 15 (unchanged source evidence)

The user restricts numerical analysis to Stage 14 genuine solver outputs. There are none: all_cases.csv is header-only, data/raw/ contains only its policy, and no matched FREE/GAP pair exists. No earlier verification case or literature observation is substituted. No additional simulation, smoothing, imputation, trend fit or numerical plot was performed.

scripts/check_postprocessing_stage.py audits this source boundary and generates data/processed/postprocessing_availability.csv for the nine requested analysis topics. All actual-change, percentage-change and range cells are blank, not zero. docs/postprocessing_status.md records the comparison and interpretation limits. docs/stage_15_postprocessing_checks.json records exact source hashes and explicitly incomplete numerical analysis.

Results were rewritten around the unavailable comparisons and observable requirements. Discussion now distinguishes mechanistic hypotheses from inferred causes and explains why thermal expansion, relaxation, irreversible strain, stiffness, contact and cooling cannot be attributed without actual matched fields/histories. No unexpected trend was observed or ruled out, no inconvenient result removed and no fixture benefit claimed. The full manuscript, state and delivery evidence are updated. Actual postprocessing remains unachieved until the validation, admitted design, dry-run and campaign prerequisites are resolved. Stop at Prompt 15; do not proceed automatically to Prompt 16.


## Surrogates, global sensitivity and uncertainty — Stage 16 (unchanged source evidence)

No eligible production response exists for fitting or held-out assessment. No surrogate, cross-validation metric, sensitivity index or uncertainty interval was calculated. Reference verification runs and reserved experimental observations are not substitutes. Source material tables and uncertainty ranges remain unchanged; no probability distribution is admitted.

The new docs/surrogate_uncertainty_protocol.md defines conditional case eligibility, grouped outer validation, training-only preprocessing/tuning, response-specific error reporting, FREE/GAP separation, contact-regime checks and solver confirmation. It separates deterministic process variation, physical-input uncertainty, production discretization error, surrogate approximation and model discrepancy. No model family, fold count, sampling budget or distribution is invented before the input/domain evidence exists.

scripts/check_surrogate_stage.py verifies the frozen inputs and generates data/processed/surrogate_availability.csv for four response families and data/processed/uncertainty_input_audit.csv for eight requested uncertain inputs. Metric/interval/distribution fields remain blank. docs/stage_16_surrogate_checks.json records source, script and output hashes. Passing these checks establishes audit integrity only, not successful fitting or propagation.

The complete manuscript replaces the earlier brief sensitivity plan with the explicit surrogate assessment and uncertainty-admission method, and updates abstract, evidence table, conclusions and provenance. Recovery requires model/boundary evidence, non-isothermal implementation, production convergence, acceptable independent validation, approved design/dry run and genuine campaign data, followed by supported uncertainty inputs. Stop at Prompt 16; do not proceed automatically to optimization.


## Multi-objective optimization and confirmation — Stage 17 (unchanged source evidence)

There are no eligible production predictions or validated surrogates, no propagated input uncertainty and no admissible basis for selecting confirmation points. No Pareto set was computed, feasibility was not evaluated and no robust window or optimum was identified. No new ANSYS confirmation run was launched; no prediction error exists. The empty registries do not mean the feasible set was found empty.

Created optimization/pareto.csv and optimization/confirmation.csv with headers only. optimization/README.md defines objective/confirmation field semantics; docs/optimization_protocol.md records the conditional objective, feasibility, preference, robustness and new-run requirements. Equal, dimensional-fidelity and stress/contact priorities remain unexecuted; no numerical weights, limits or desirability thresholds were invented. Strength is excluded. The requested recommendation, two neighbors and thermally matched FREE roles have no assigned case IDs or coordinates.

scripts/check_optimization_stage.py audits frozen source hashes and prevents overwriting populated registries. docs/stage_17_optimization_checks.json distinguishes integrity from scientific execution. No raw data, material properties or earlier validation/calibration records were altered. The manuscript now integrates unavailable optimization results, conditional priorities, explicit confirmation requirements and limitations in Discussion and Conclusions. Recovery requires the earlier model, validation, production and uncertainty prerequisites. Stop at Prompt 17; do not advance automatically.


## Journal-article reconstruction — Stage 18 (current)

The current title is **Numerical verification of a thermo-mechanical framework for gap-constrained annealing of FFF-printed PLA**. This supersedes the earlier candidate title to reflect achieved evidence. The original research question is retained; production annealing, independent validation, surrogate/UQ, optimization and confirmation remain unachieved. The instruction's assumption that all computation is complete is not supported and is not asserted.

The full manuscript is rebuilt with Introduction, Background, 16 methodology subsections, 18 Results subsections, Discussion, seven quantitative reference-case Conclusions, data/code availability, declarations, references and integrated Supplementary Information. Real verification and convergence values enter the new abstract and conclusions. No production or experimental findings are invented. Oversized source/coefficient/comparison tables move to Supplementary Tables S1–S7. The observation-only validation plot remains in the repository but is removed from the main article.

Current numbered equations map through docs/manuscript_equation_map.csv. There are 21 implemented reference/calculation relations. The former three unimplemented production extraction formulas are omitted, and the strain partition now matches the actual thermal-plus-viscoelastic update without an unimplemented bulk annealing term. The earlier equation map remains historical. docs/manuscript_reconstruction_audit.md details scope, corrections and quantitative provenance.

All 81 repository unit tests were rerun successfully in this stage; no new solver run occurred. Publication readiness is not claimed: required production science and author declarations remain missing. Stop at Prompt 18; do not automatically continue.


## Scientific peer-review-style audit — Stage 19 (current)

The title is now **Thermal, viscoelastic and contact verification toward gap-constrained annealing of FFF-printed PLA**. Six internal reviewer perspectives led to 18 documented findings in docs/peer_review_audit.md. This is not external peer review. The manuscript corrects vertical fitted-line warpage, secant thermal gradient, element-pressure averaging and engagement, contact-force sign, actual NLGEOM ON contact kinematics/boundaries, finite-time clamped residuals and sampled-error scope. Adjacent convergence is not an error bound or combined mesh/time convergence.

A focused literature update adds Hussam2025, DOI 10.1007/s00170-025-15455-5, as ABS annealing mould-clearance precedent. Reference 41 and the addendum are current; the original 34-study matrix remains historical. Quantified clearance alone is not novel. No ABS property or clearance recommendation is transferred.

Independent extraction reproduces 63 mesh/time response values and 36 contact response comparisons, and checks 114 structural/contact errors plus nine thermal samples. Three zero-denominator percentages in the historical mesh CSV used zero sentinels; current analysis/review_metrics.py and convergence/stage_19_audited_refinement.csv report undefined percentages and absolute zero change. Original files remain unchanged. The current equation map points to the corrected function.

All 85 current unit tests pass; the local exact-phrase screen finds no 12-word main-prose matches across 14 accessible documents, with coverage limits disclosed. No input/solution defect required a new ANSYS run. The same missing material, recovery, boundary, non-isothermal and validation prerequisites block production, sensitivity, UQ and optimization. This is an audited verification draft, not a publication-ready completed annealing study. Stop at Prompt 19; do not continue automatically.

Stage 19 audit and page inspection occurred on 30 September; final Git integrity and delivery were completed on 1 October 2026. The PDF retains its audit revision date.
