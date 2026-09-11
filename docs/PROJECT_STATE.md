# Authoritative project state

Stage: **Prompt 1/20 — base paper audit and computational conversion**.
Date: 2026-09-12 (Asia/Calcutta).
Repository: https://github.com/VorteXEkansh/FDM-Annealing

## Research identity

This is a computational thermo-mechanical study intended for genuine ANSYS execution. The central question is how quantified fixture clearance affects signed directional dimensional response, warpage and the stress/contact trade-off during sub-melting annealing of FFF PLA, including cooling and release.

Current manuscript: `manuscript/current.md`.
Current PDF: `output/pdf/Constrained-Annealing-2026-DRAFT.pdf`.
Base source: `data/source/DTU_Constrained_Annealing_Final_Submission.pdf`; immutable, with SHA-256 in `data/source/manifest.json`.

## Completed at this stage

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

1. Treat two opposed plate surfaces with stops as a candidate fixture concept. Define total initial free clearance at the reference temperature. Do not inherit the unverified 0.05 mm hot clearance as a property or optimum.
2. Use ANSYS transient thermal and history-dependent structural/contact analysis when justified by material evidence. This is an intended workflow, not an executable model in Stage 1.
3. Reversible thermoelasticity alone cannot establish permanent annealing recovery. A source-backed irreversible/history-dependent description or explicitly limited phenomenological model is required.
4. Do not impose symmetry, clamped specimen faces or uniform recovery merely to force low warpage. Quantify rigid-body stabilization and contact effects.
5. Retain unconstrained comparison; granular supports are literature context, not primary numerical domains.
6. Do not infer UTS, ductility or strength improvement from von Mises stress or displacement. No new physical specimens or UTM testing are required by this project.
7. Hold durations need a defined part-temperature attainment criterion. Equal oven histories need not mean equal part histories; separate process comparison from thermally matched mechanism comparison.
8. Verify numerical error before calibration/validation. Reserve independent literature observations before fitting; calibration agreement is not validation.
9. Do not assign probability distributions or tolerance thresholds without evidence/declared justification. Deterministic sweeps do not produce experimental confidence intervals.

## Literature state

Only references retained in the current manuscript are treated as checked for the limited claims shown in `data/literature/verified_sources.json`. The base paper's 50 entries are preserved in an audit catalog; unretained entries have not been promoted to verified evidence merely because the base labels them verified. No quantitative literature values are adopted as material inputs or validation targets at Stage 1.

## Completion records and stage boundary

Integrity and visual review: see `docs/stage_01_quality.md` and `docs/integrity_report.json`.
Git transport/remote verification is recorded in `docs/stage_01_delivery.json`; it identifies the pushed content commit. That record is committed separately to avoid a self-referential hash. The final delivery-record commit is also checked against the remote.

Do not begin Prompt 2 without the user's next numbered instruction. Later stages must resolve the open evidence and implementation items within their assigned scope before promoting any numerical claim.
