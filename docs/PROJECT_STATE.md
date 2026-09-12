# Authoritative project state

Stage: **Prompt 4/20 — PLA and fixture material-property database**.
Date: 2026-09-12 (Asia/Calcutta).
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

Genuine ANSYS runs: **none**. ANSYS availability, license and version: **not established**.
Geometry/CAD/mesh: **not selected or generated**.
Reference PLA formulation: **Prusament PLA selected for constitutive development; production ANSYS material card not admitted**.
Property tables: **created and source-audited; compatible k(T), c_p(T), bulk irreversible strain and complete orthotropy remain unavailable**.
Constitutive law/calibration: **23-branch Prusament generalized-Maxwell/WLF–Arrhenius candidate extracted; not implemented or ANSYS-verified**.
Fixture material: **AISI 304 stainless steel selected as candidate plate material with a 20–200 °C tabulated property set**. Fixture dimensions, numerical gap levels, friction and thermal contact conductance remain unselected.
Initial residual stress, recovery strain and crystallization kinetics: **unavailable**.
Boundary histories, reference temperature, release rule and environmental heat transfer: **not fixed**.
Mesh/time-step/contact convergence: **not performed**.
Independent validation datasets: **not extracted or accepted**.
Sensitivity indices, uncertainty intervals and optimization results: **none**.
No performance improvement, optimal process condition or experimental confirmation is claimed.

## Decisions and scientific safeguards

1. Use two opposed plate surfaces with stops as the primary GAP fixture concept. Define total initial free clearance at the reference temperature. Do not inherit the unverified 0.05 mm hot clearance as a property or optimum.
2. Use ANSYS transient thermal and history-dependent structural/contact analysis when justified by material evidence. This is an intended workflow, not an executable model at the current stage.
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

The core study uses one selected formulation, fixed print architecture and representative three-dimensional plate-like coupon geometry. Their identities and dimensions remain evidence-dependent implementation choices, not fabricated finalized inputs. Full deposition-process simulation, printing-parameter optimization and comparisons across PLA grades are outside the primary study.

The main comparison applies the same external thermal schedule; matched part-temperature diagnostic cases may isolate mechanical restraint. Final responses are evaluated at a common reference temperature with an explicitly declared release/observation time. In-fixture dimensions, released warpage and conditional residual stress remain separate. Hypotheses concern a resolved clearance effect, release effect, interaction and geometric/stress trade-off; none assumes a favorable or monotonic result. Numerical resolution/extraction criteria must be specified before assessing them.

The intended contribution is an evidence-tested clearance–distortion–stress assessment. It is not an achieved result or exclusive-priority claim. Stress/contact validation cannot be inferred from geometric agreement. No new experiments, strength/ductility enhancement, universal law, granular-support superiority, certification, durability or global optimum are promised. Processing recommendations require an independently supported benefit criterion as well as verified responses.

## Material-property state — Stage 4

Authoritative files are `material/pla_properties.csv`, `material/property_sources.csv`, `material/uncertainty_ranges.csv`, `material/fixture_properties.csv` and `material/build_manifest.json`. `scripts/build_material_database.py` deterministically regenerates the four CSV files. `docs/material_property_audit.md` records the compatibility reasoning. Raw Stage 4 evidence copies and their hashes are preserved under `literature/evidence/stage_04/`.

Prusament PLA is the reference formulation because Chapuis2025 provides grade-specific DMA characterization, k₀ = 10.598 MPa, ν = 0.35, T_g = 65 °C, C₁ = 17.4, C₂ = 51.6 K, C₃ = 35 000 K, α = 68.0 µm m⁻¹ K⁻¹ and 23 Maxwell branch pairs. Direct characterization spans 23–85 °C. The calculated reference instantaneous modulus is E₀ = k₀ + ∑kᵢ = 1691.594 MPa; this is an arithmetic model quantity, not a new experiment. The published piecewise shift uses Arrhenius below T_g and WLF at or above T_g. No native ANSYS conversion has been verified.

The inherited 80 °C candidate lies inside the direct characterization interval. The 95 °C and 110 °C candidates lie outside it and are not admitted through extrapolation. The supplier's ρ = 1240 kg m⁻³ is retained only as a screening value because its test temperature is not reported. No compatible Prusament k(T) or c_p(T) functions, signed bulk irreversible annealing-strain law, complete E₁/E₂/E₃/G₁₂/G₂₃/G₁₃/ν₁₂/ν₂₃/ν₁₃ set, directional α₁/α₂/α₃ set, or crystallization-kinetic coefficients were found. Missing lower/upper bounds remain blank with status `no bound invented`.

The Chapuis programmed ε₁₁^AM values are retained with same-source method brackets but are not accepted as bulk annealing shrinkage. Bute2024 directional irreversible strain, Li2024 FormFutura orthotropy, Relaxation2022 SUNLU PLA Plus relaxation, Luberto2024 unidentified-PLA thermal constants and Trofimov2022 mixed-source Raise3D properties remain clearly labelled comparators. No numerical property is transferred across formulations.

AISI 304 stainless steel is the candidate opposed-plate material. Meng2026 Table 1 provides ρ(T), c_p(T), k(T), α(T), E(T) and ν(T) at 20 °C, 100 °C and 200 °C, bracketing 20–110 °C without extrapolation. The fixture property table is a candidate engineering input. Actual alloy heat, dimensions, surface condition, friction and PLA–steel contact conductance remain open.

No probability distribution is assigned. Reported supplier intervals and same-source method brackets are preserved without reinterpreting them as confidence intervals. Cross-formulation minima and maxima are not treated as Prusament uncertainty bounds.

## Completion records and stage boundary

Stage 4 quality and integrity: `docs/stage_04_quality.md`, `docs/integrity_report.json`, `docs/stage_04_literature_integrity.json`, `docs/stage_04_material_integrity.json` and `docs/stage_04_manifest.json`. Prior stage records remain historical. The stage-specific delivery record identifies the pushed content commit; the subsequent delivery-record commit is also verified remotely to avoid self-referential hashes.

Prompt 4 establishes the material database and its admissibility limits only. No solver run, native ANSYS material card, calibration, numerical verification, validation, sensitivity analysis, propagated uncertainty or optimization is complete. Do not begin Prompt 5 without the user's next numbered instruction.
