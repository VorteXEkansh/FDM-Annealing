# FDM Annealing

**Verification-only research package — 1 October 2026.** This repository preserves genuine ANSYS reference calculations toward gap-controlled annealing of FFF-printed PLA. It is not a completed or independently validated production annealing study. Read [PROJECT_STATE](docs/PROJECT_STATE.md) before changing research scope.

The release contains one accepted thermal reference case, six structural/contact reference cases and 28 unique accepted convergence runs. Forty-three convergence attempt directories retain 15 excluded attempts. The component verification and discretization findings cannot establish production coupon performance, an optimal clearance or released residual warpage.

## Manuscripts

- [Main PDF](output/release/Constrained-Annealing-2026.pdf)
- [Editable Word manuscript](output/release/Constrained-Annealing-2026.docx)
- [Supplementary PDF](output/release/Constrained-Annealing-2026-Supplementary.pdf)
- [Complete evolving draft](output/pdf/Constrained-Annealing-2026-DRAFT.pdf)

All outputs are explicitly labelled verification-only. Author and declaration approval remains necessary before journal submission. No completion tag v1.0.0 is assigned.

## Evidence and reproduction

Start with [reproduction instructions](reproducibility/README.md), [claim traceability](reproducibility/result_traceability.csv), [figure manifest](reproducibility/figure_manifest.csv), [table manifest](reproducibility/table_manifest.csv) and [checksums](reproducibility/sha256_manifest.csv). Solver reproduction requires compatible licensed ANSYS; reading, recalculating and checking archived exports does not.

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

Compatible thermal properties, bulk irreversible strain, printed initial state, physical fixture/contact inputs and a non-isothermal ANSYS material adapter are incomplete. Independent physical validation, production sweeps, surrogate fitting, global sensitivity, uncertainty propagation and optimization confirmation have not been performed. Reserved published observations are not ANSYS validation results. Simulation repetitions are not independent physical specimens.

Every numerical result is solver-backed, a reproducible calculation or verified published evidence. Design values are labelled choices. Raw evidence is immutable. Future work must satisfy the missing evidence and validation gates before making process recommendations.
