# FDM Annealing

**Numerical verification and contact feasibility — 1 November 2026.** This repository preserves genuine ANSYS reference calculations toward gap-controlled annealing of FFF-printed PLA. It is not a completed or independently validated production annealing study. Read [PROJECT_STATE](docs/PROJECT_STATE.md) before changing research scope.

The master investigation adds six accepted ANSYS reference runs among thirteen preserved attempts: three non-isothermal refinements and three elastic stop checks. It also adds a source-conditioned programmed-road recovery calculation and ninety mount/clearance screens. The earlier one thermal reference, six structural/contact references and 28 selected convergence runs remain intact. These checks do not establish production coupon performance, an optimal clearance or released residual warpage. There are zero production cases.

## Manuscripts

- [Main PDF](output/master/Constrained-Annealing-2026.pdf)
- [Editable Word manuscript](output/master/Constrained-Annealing-2026.docx)
- [Supplementary PDF](output/master/Constrained-Annealing-2026-Supplementary.pdf)
- [Complete evolving draft](output/pdf/Constrained-Annealing-2026-DRAFT.pdf)

The current title is **Contact feasibility and non-isothermal verification for gap-constrained annealing of FFF-printed PLA**. Outputs retain the verification label. Author and declaration approval remains necessary before journal submission. No official completion release or v1.0.0 tag is assigned. `output/release/` preserves the historical Stage 20 package.

The [master delivery report](docs/master_completion_report.md) records achieved findings, document counts and unresolved requirements. The main PDF has eight pages; the supplement has 32. All pages were inspected and all 98 unit tests pass. These checks do not establish physical validation.

## Evidence and reproduction

Start with [current reproduction instructions](reproducibility/MASTER_README.md), [new claim traceability](reproducibility/master_result_traceability.csv), [equation map](docs/master_equation_map.csv), [checksums](reproducibility/master_checksums.json) and [remaining scientific dependencies](docs/master_remaining_blockers.md). The earlier trace, figure/table manifests and release instructions remain unchanged historical records. Solver repetition requires compatible licensed ANSYS; recalculating and checking archived exports does not.

| Directory | Contents |
|---|---|
| docs | Authoritative state, decisions, scientific audits and checks |
| literature / material | Verified references, appraisal matrix, formulation-specific properties and restrictions |
| geometry / ansys / simulation | Candidate geometry, automation, archived input decks and genuine raw solver evidence |
| verification / convergence | Analytical comparisons and reference discretization results |
| validation | Reserved literature observations and explicit unsolved validation status |
| data/raw / data/processed | Production evidence registries; no invented campaign data |
| analysis / src / tests | Reproducible calculations, constitutive material-point code and unit tests |
| sensitivity / uncertainty / optimization | Explicit status and admission limits; no manufactured findings |
| figures / tables / supplementary | Scientific plots, source tables and detailed supplementary manuscript |
| reproducibility | Traceability, release audits, checksums and instructions |

The current release omits third-party PDF redistribution and a large superseded scratch file while retaining their original local hashes. Older Git commits were not rewritten and may still contain those files. See the reproduction README. No repository license is invented for third-party material; comply with each source's terms.

## Scientific boundaries

Non-isothermal shifting now passes its defined reference checks, but compatible thermal properties, bulk recovery/initial state and physical fixture/contact inputs remain missing. The Prusament characterization envelope is 23–85 °C, not a validated annealing recommendation. Independent physical validation, production sweeps, surrogate fitting, global sensitivity, uncertainty propagation and optimization confirmation have not been performed. Reserved published observations are not ANSYS validation results. Simulation repetitions are not independent physical specimens.

Every numerical result is solver-backed, a reproducible calculation or verified published evidence. Design values are labelled choices. Raw evidence is immutable. Future work must satisfy the missing evidence and validation gates before making process recommendations.
