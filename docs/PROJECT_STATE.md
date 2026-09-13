# Authoritative project state

Stage: **Prompt 7/20 — parametric specimen and fixture geometry**.
Date: 2026-09-13 (Asia/Calcutta).
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

Genuine ANSYS field runs: **none**. A zero-analysis MAPDL environment/license probe succeeded; it is not a research simulation or result.
ANSYS environment: **Ansys Student 2026 R1; MAPDL release 2026 R1, build 26.1, update 20260202; Student Mechanical product checkout confirmed**. Workbench and Mechanical 26.1 plus the named thermal/structural templates are installed, but their GUI entitlements have not been separately exercised. PyMechanical is not installed.
Geometry/CAD: **60 mm × 10 mm × 4 mm rectangular specimen and two 70 mm × 20 mm × 5 mm plates selected; a geometry-only MAPDL build created and saved three volumes**. Mesh: **not generated**.
Reference PLA formulation: **Prusament PLA selected for constitutive development; production ANSYS material card not admitted**.
Property tables: **created and source-audited; compatible k(T), c_p(T), bulk irreversible strain and complete orthotropy remain unavailable**.
Constitutive implementation: **small-strain isotropic 23-branch Prusament reference implemented; 38 analytical/synthetic unit tests pass; no ANSYS adapter or physical calibration/validation**.
Fixture material: **AISI 304 stainless steel selected as candidate plate material with a 20–200 °C tabulated property set**. Plate dimensions and normalized reference-gap levels are fixed as geometry design choices. Friction, thermal contact conductance and physical spacer geometry remain unselected. Thermal-strain use of the fixture alpha table is blocked until its tangent/mean convention and reference temperature are established.
Initial residual stress, recovery strain and crystallization kinetics: **unavailable**.
Boundary histories, reference temperature, release rule and environmental heat transfer: **not fixed**.
Mesh/time-step/contact convergence: **not performed**.
Independent validation datasets: **not extracted or accepted**.
Sensitivity indices, uncertainty intervals and optimization results: **none**.
No performance improvement, optimal process condition or experimental confirmation is claimed.

## Software and automation state — Stage 6

`docs/software_environment.md` is the exact environment record. The installed package is R261RC2P01. The host is Windows 11 build 10.0.26200 on an AMD Ryzen 7 7435HS with 8 physical cores, 16 logical processors and 15.82 GiB installed RAM. The official 2026 R1 Student page states a 128,000-node/element structural limit, no geometry export and up to four HPC CPU cores.

`ansys/run_case.py` provides a direct MAPDL batch path with explicit JSON parameters and admission gates. `simulation/cases/production_template.json` remains blocked because geometry, compatible thermal data, irreversible strain, the Ansys constitutive adapter, boundary history and extraction definitions are unresolved. `analysis/extract_results.py` rejects empty or untraceable output tables. No full campaign was run.

The only execution is `simulation/runs/stage06_mapdl_smoke/`, generated from `ansys/apdl/environment_smoke.dat`. MAPDL exited 0 after `/STATUS` and `/EXIT,NOSAVE`; it created no geometry, nodes, elements, loads or solution. Its case, input, command, raw log and output hashes are recorded. DesignXplorer and optiSLang 26.1.0 revision 1878 are present on disk but unexercised. Their availability must not be described as a completed optimization capability.

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

Prusament PLA is the reference formulation because Chapuis2025 provides grade-specific DMA characterization, k₀ = 10.598 MPa, ν = 0.35, T_g = 65 °C, C₁ = 17.4, C₂ = 51.6 K, C₃ = 35 000 K, α = 68.0 µm m⁻¹ K⁻¹ and 23 Maxwell branch pairs. Direct characterization spans 23–85 °C. The calculated reference instantaneous modulus is E₀ = k₀ + ∑kᵢ = 1691.594 MPa; this is an arithmetic model quantity, not a new experiment. The published piecewise shift uses Arrhenius below T_g and WLF at or above T_g. No native ANSYS conversion has been verified.

The inherited 80 °C candidate lies inside the direct characterization interval. The 95 °C and 110 °C candidates lie outside it and are not admitted through extrapolation. The supplier's ρ = 1240 kg m⁻³ is retained only as a screening value because its test temperature is not reported. No compatible Prusament k(T) or c_p(T) functions, signed bulk irreversible annealing-strain law, complete E₁/E₂/E₃/G₁₂/G₂₃/G₁₃/ν₁₂/ν₂₃/ν₁₃ set, directional α₁/α₂/α₃ set, or crystallization-kinetic coefficients were found. Missing lower/upper bounds remain blank with status `no bound invented`.

The Chapuis programmed ε₁₁^AM values are retained with same-source method brackets but are not accepted as bulk annealing shrinkage. Bute2024 directional irreversible strain, Li2024 FormFutura orthotropy, Relaxation2022 SUNLU PLA Plus relaxation, Luberto2024 unidentified-PLA thermal constants and Trofimov2022 mixed-source Raise3D properties remain clearly labelled comparators. No numerical property is transferred across formulations.

AISI 304 stainless steel is the candidate opposed-plate material. Meng2026 Table 1 provides ρ(T), c_p(T), k(T), α(T), E(T) and ν(T) at 20 °C, 100 °C and 200 °C, bracketing 20–110 °C without extrapolation. The fixture property table is a candidate engineering input. Actual alloy heat, dimensions, surface condition, friction and PLA–steel contact conductance remain open.

No probability distribution is assigned. Reported supplier intervals and same-source method brackets are preserved without reinterpreting them as confidence intervals. Cross-formulation minima and maxima are not treated as Prusament uncertainty bounds.

## Constitutive-model decision — Stage 5

`docs/constitutive_model_decision.md` and `docs/model_formulation.md` fix the strongest currently supported core: small-strain isotropic thermorheologically simple generalized-Maxwell response for Prusament PLA, with constant ν and reversible α, and the full source Arrhenius/WLF clock. `src/constitutive.py` implements the reference; `material/constitutive_reference.json` records the calculated shear/bulk conversion and evidence gates. It is not an ANSYS material card.

The macroscopic elastic-plus-delayed strain partition is defined through instantaneous compliance; branch stress evolution supplies the delayed response. Identical normalized shear and bulk spectra preserve the assumed constant ν. The source is a plane-stress shell model; its three-dimensional isotropic extension remains a constitutive assumption. No independent E(T) multiplier, orthotropic law, crystallization kinetics or bulk irreversible annealing-strain law is added.

The implemented temperature guard is 23–85 °C, with 23 °C used only as a numerical-test thermal reference and 65 °C as the relaxation reference. The 20 °C PLA start and the inherited 95 °C/110 °C conditions are rejected. The temperature interval does not itself validate 30–90 min holds, arbitrary strains or bulk geometries. The algorithm integrates history through reduced time and requires temperature subdivision at 65 °C; material-point refinement tests are not ANSYS time-step convergence.

Irreversible annealing strain, crystallization, production assembly and fixture thermal strain raise explicit evidence-gap errors. No missing mechanism is defaulted to a physical zero. The AISI 304 table can be interpolated and used for instantaneous elastic reference calculations, but its expansion convention is unresolved. Thermal-field closures, initial printed state, duration/strain applicability and physical validation remain open.

`tests/test_constitutive.py` and `scripts/check_constitutive.py` execute 38 numerical unit tests; individual outcomes and input/code hashes are in `docs/stage_05_constitutive_tests.json`. Analytical checks and synthetic cases are not independent material validation data. No ANSYS run has been executed. `docs/equation_implementation_map.csv` maps every manuscript governing equation to its reference function or designated future field/postprocessing operation. No optional crystallization or desirability equation is retained.

Three ignored temporary comparator evidence files were copied byte-for-byte into `literature/evidence/stage_05/` and the material source paths were repaired. Raw evidence and hashed database/report bytes are protected against Git line-ending conversion. The SUNLU paper's author metadata was corrected to Bertocco et al. without altering reported property values. Stage 4 records are retained as historical snapshots; the current database build manifest is Stage 5.

## Geometry state — Stage 7

`docs/geometry_decision.md` and `geometry/geometry_definition.json` are authoritative for geometry. The specimen dimensions reproduce the regular plate in Trofimov et al. (2022), Figure 4(a), DOI 10.1016/j.addma.2022.102693. Only the geometry is reused: the source's Raise3D Premium PLA, deposition history and response data are not transferred to Prusament PLA. The selected plate has a 2400 mm³ volume, 600 mm² nominal area per opposed face, and aspect ratios L/h = 15, W/h = 2.5 and L/W = 6.

GAP uses two 70 mm × 20 mm × 5 mm AISI 304 plates, each with 5 mm plan margin around the centered specimen. FREE omits those volumes. The total reference clearance is g₀ = H₀ − h₀ and γ = g₀/h₀. Declared screening levels γ = 0, 0.0025, 0.005, 0.01 and 0.02 give g₀ = 0, 0.01, 0.02, 0.04 and 0.08 mm. They are geometric design levels, not measured tolerances or an optimum.

The Prompt 7 absolute candidates are explicitly evaluated in `geometry/candidate_clearance_audit.csv`. The 0 mm endpoint is retained. The 0.025 mm and 0.050 mm candidates are represented inside the normalized near-contact screen rather than added as redundant levels. The 0.100 mm and 0.200 mm candidates are deferred, not ruled out, because no supported free-deformation scale yet justifies reducing near-contact resolution to include 2.5% and 5% thickness gaps.

`scripts/build_geometry.py` validates the definition, calculates the gap table and writes a parameterized MAPDL deck. One geometry-only invocation at γ = 0.01 exited 0, reported three volumes and saved `stage07_plate_gap.db`. The immutable input/output hashes are in `simulation/geometry/stage07_plate_gap/manifest.json`. There is no mesh, element type, material assignment, boundary condition, load, analysis type or solve command. Spacer geometry is deferred because its thermal expansion convention and attachment are unresolved.

## Completion records and stage boundary

Stage 7 quality and integrity records are `docs/stage_07_quality.md`, `docs/integrity_report.json`, `docs/stage_07_geometry_checks.json`, `docs/stage_07_literature_integrity.json`, `docs/stage_07_material_integrity.json`, `docs/stage_07_pdf_review.json` and `docs/stage_07_manifest.json`.

Prompt 7 establishes the parametric specimen/fixture geometry and preprocessing evidence only. The complete production thermo-mechanical annealing model remains blocked by material and boundary evidence. No mesh, field solution, mesh/time-step/contact convergence, physical validation, sensitivity, propagated uncertainty or optimization is complete. Do not begin Prompt 8 without the user's next numbered instruction.
