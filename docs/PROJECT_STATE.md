# Authoritative project state

Stage: **Prompt 3/20 — research question, scope, objectives and contributions**.
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
Material grade and property tables: **not selected**.
Constitutive law/calibration: **not implemented**.
Fixture material, dimensions, numerical gap levels, friction and thermal contact conductance: **not selected**.
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

No literature property or validation target is adopted. Candidate recovery sources include Bute2024 and Laminate2025; potential thermal/warpage comparisons include Wijnen2018 and Trofimov2022. All require compatibility and independence appraisal before data selection. None currently validates the proposed fixture's residual stresses or contact pressures. The Mould2022 final PLA Table 7 temperature conflicts with Tables 2–3; affected values remain unaccepted. Tough, high-heat, recycled and filled PLA remain separate from neat PLA.

## Scope finalized in Stage 3

Candidate title: **Free and gap-constrained annealing of FFF-printed PLA: a thermo-mechanical computational study**.

`docs/research_scope.md` records one primary question, five secondary questions (SQ1–SQ5), five objectives and four testable numerical propositions (H1–H4). The manuscript incorporates their full text, an explicit intended contribution and excluded claims. The structured abstract contains context/question, planned approach, results status and intended contribution, without invented numerical findings.

The core study uses one selected formulation, fixed print architecture and representative three-dimensional plate-like coupon geometry. Their identities and dimensions remain evidence-dependent implementation choices, not fabricated finalized inputs. Full deposition-process simulation, printing-parameter optimization and comparisons across PLA grades are outside the primary study.

The main comparison applies the same external thermal schedule; matched part-temperature diagnostic cases may isolate mechanical restraint. Final responses are evaluated at a common reference temperature with an explicitly declared release/observation time. In-fixture dimensions, released warpage and conditional residual stress remain separate. Hypotheses concern a resolved clearance effect, release effect, interaction and geometric/stress trade-off; none assumes a favorable or monotonic result. Numerical resolution/extraction criteria must be specified before assessing them.

The intended contribution is an evidence-tested clearance–distortion–stress assessment. It is not an achieved result or exclusive-priority claim. Stress/contact validation cannot be inferred from geometric agreement. No new experiments, strength/ductility enhancement, universal law, granular-support superiority, certification, durability or global optimum are promised. Processing recommendations require an independently supported benefit criterion as well as verified responses.

## Completion records and stage boundary

Stage 3 quality and integrity: `docs/stage_03_quality.md`, `docs/integrity_report.json`, `docs/stage_03_literature_integrity.json` and `docs/stage_03_manifest.json`. Prior stage records remain historical. The stage-specific delivery record identifies the pushed content commit; the subsequent delivery-record commit is also verified remotely to avoid self-referential hashes.

Prompt 3 finalizes research scope and manuscript framing only. All solver, property, calibration, verification, validation, sensitivity, uncertainty and optimization evidence statuses remain unchanged. Do not begin Prompt 4 without the user's next numbered instruction.
