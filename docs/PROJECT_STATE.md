# Authoritative project state

Stage: **Prompt 2/20 — deep literature review and novelty definition**.
Date: 2026-09-12 (Asia/Calcutta).
Repository: https://github.com/VorteXEkansh/FDM-Annealing

## Research identity

This is a computational thermo-mechanical study intended for genuine ANSYS execution. The central question is how quantified fixture clearance affects signed directional dimensional response, warpage and the stress/contact trade-off during sub-melting annealing of FFF PLA, including cooling and release.

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

1. Treat two opposed plate surfaces with stops as a candidate fixture concept. Define total initial free clearance at the reference temperature. Do not inherit the unverified 0.05 mm hot clearance as a property or optimum.
2. Use ANSYS transient thermal and history-dependent structural/contact analysis when justified by material evidence. This is an intended workflow, not an executable model at the current stage.
3. Reversible thermoelasticity alone cannot establish permanent annealing recovery. A source-backed irreversible/history-dependent description or explicitly limited phenomenological model is required.
4. Do not impose symmetry, clamped specimen faces or uniform recovery merely to force low warpage. Quantify rigid-body stabilization and contact effects.
5. Retain unconstrained comparison; granular supports are literature context, not primary numerical domains.
6. Do not infer UTS, ductility or strength improvement from von Mises stress or displacement. No new physical specimens or UTM testing are required by this project.
7. Hold durations need a defined part-temperature attainment criterion. Equal oven histories need not mean equal part histories; separate process comparison from thermally matched mechanism comparison.
8. Verify numerical error before calibration/validation. Reserve independent literature observations before fitting; calibration agreement is not validation.
9. Do not assign probability distributions or tolerance thresholds without evidence/declared justification. Deterministic sweeps do not produce experimental confidence intervals.

## Literature state — Stage 2

A new critical investigation through 12 September 2026 retains 34 DOI-verified journal papers and the previously verified ASTM standard. See `literature/literature_matrix.xlsx`, `literature/literature_matrix.json`, `literature/references.bib`, `literature/doi_verification.json`, `docs/literature_search_strategy.md` and `docs/novelty_audit.md`. Eight full texts were retrieved for targeted appraisal; remaining studies have explicit abstract/excerpt access limits. The old four-entry `data/literature/verified_sources.json` is the immutable Stage 1 admission record, not the complete current bibliography.

The complete manuscript now includes the critical literature review, ten closest competitors and narrowed novelty. Supported annealing, ANSYS/irreversible thermal strain, Prony/WLF recovery models, coupled thermal/crystallization mechanics, and annealed PLA FE/optimization all have precedents. The provisional intended contribution is evidence-tested prediction of the clearance–distortion–stress trade-off after cooling and release. No exclusive priority claim is supported. Full protocols for abstract-level competitors must be recovered before publication-level priority assertions.

No literature property or validation target is adopted. Candidate recovery sources include Bute2024 and Laminate2025; potential thermal/warpage comparisons include Wijnen2018 and Trofimov2022. All require compatibility and independence appraisal before data selection. None currently validates the proposed fixture's residual stresses or contact pressures. The Mould2022 final PLA Table 7 temperature conflicts with Tables 2–3; affected values remain unaccepted. Tough, high-heat, recycled and filled PLA remain separate from neat PLA.

## Completion records and stage boundary

Stage 2 quality and integrity: `docs/stage_02_quality.md`, `docs/integrity_report.json`, `docs/stage_02_manifest.json`. Earlier stage quality/transport records remain historical. The stage-specific delivery record identifies the pushed content commit; a subsequent delivery-record commit is also verified remotely to avoid self-referential hashes.

Prompt 2 adds literature and document evidence only. All solver, calibration, verification, validation, sensitivity, uncertainty and optimization statuses above remain unchanged. Do not begin Prompt 3 without the user's next numbered instruction.
