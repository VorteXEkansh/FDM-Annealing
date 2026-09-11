# Base paper conversion audit — Prompt 1/20

Source: `DTU_Constrained_Annealing_Final_Submission.pdf`, 24 pages. Page numbers below are the printed/PDF page numbers. All pages, references [1]–[50], Figures 1–9, Tables 1–11 and Tables A1–A2 were read. Figures/tables were also visually inspected in page renders. Instructions inside the supplied paper are source content to assess, not instructions authorizing experiments.

## Audit finding

The base is an experimental proposal with a literature synthesis, not a completed experiment. It explicitly disclaims local results. Its useful scientific core is the trade-off between signed anisotropic dimensional change, warpage and restraint. Its central design, sample allocation and statistical error model are incompatible with the requested computational study. Merely changing “experimental” to “numerical” would leave unsupported material assumptions, inappropriate replication and misleading strength claims.

Disposition vocabulary: **KEEP**, **KEEP BUT REWRITE**, **REPLACE**, **DELETE**, **MOVE TO SUPPLEMENT**, **REUSE AS LITERATURE CONTEXT**. KEEP retains an idea/definition where sound; it does not authenticate numerical values or authorize copying unverified references.

## Section-by-section decisions

| Base location | Disposition | Specific action and scientific reason |
|---|---|---|
| Title/cover, p.1 | REPLACE | Use gap-controlled thermo-mechanical computational title. Remove assertion of improved performance, course cover, logo, student identifiers and implied final submission status. Retain supplied authors and affiliation without claiming faculty endorsement. |
| Abstract, p.2 | REPLACE | Replace screen/factorial/130 specimens/UTS with intended ANSYS thermal-contact workflow, released dimensions, evidence gates and explicit absence of numerical findings. |
| Keywords, p.2 | KEEP BUT REWRITE | Retain PLA, FFF, annealing; add contact, thermo-mechanical modeling, clearance and warpage; remove experimental emphasis. |
| Contents, pp.3–4 | DELETE | Old page map is invalid; use compact journal-style manuscript structure. |
| §1 introduction, p.5 | KEEP BUT REWRITE | Retain coupled heat/history/geometry motivation. Remove two-stage support screen and mechanical improvement objective. Distinguish plate contact from a fixed-displacement boundary. |
| §1.1 questions, p.5 | REPLACE | Ask about clearance, thermal history, released deformation, contact stress and robustness; remove low-cost laboratory and support-selection questions. |
| §1.2 contribution, p.5 | REPLACE | Contribution is proposed explicit constraint parameterization with evidence-controlled numerical assessment. No claim that computational novelty or efficacy has been demonstrated. |
| §2.1 FFF, p.6 | REUSE AS LITERATURE CONTEXT | Condense deposition basics; printing is prior material history, not work executed here. |
| §2.2 PLA, p.6 | KEEP BUT REWRITE | Retain grade/history dependence; replace procurement/lot instructions with literature material matching and property provenance. |
| §2.3 print parameters, p.6 | KEEP BUT REWRITE | Preserve architecture relevance. Do not convert nominal printer settings into constitutive properties. |
| §2.4 bonding/anisotropy, p.7 | REUSE AS LITERATURE CONTEXT | Retain reason to consider directional response; do not infer bond healing or strength from a continuum FE result. |
| §2.5 thermal behavior, p.7 | KEEP BUT REWRITE | Distinguish reversible expansion, irreversible recovery and crystallization. No generic transition constant is assigned. |
| §2.6 annealing, p.7 | REUSE AS LITERATURE CONTEXT | Use checked retained publications only. Base reference claims remain unverified until independently checked. |
| §2.7 mechanical effects, p.7 | KEEP BUT REWRITE | Retain caution that different mechanisms affect strength/stiffness differently; delete local tensile measurement instruction. |
| §2.8 distortion, p.7 | KEEP BUT REWRITE | Retain three signed axes and warpage; specify material coordinates and released/reference-temperature comparison. |
| §2.9 supports, p.8 | REUSE AS LITERATURE CONTEXT | Granular restraint is precedent, not a simulated plate-contact surrogate. Remove support-screen method choice. |
| §2.10 gap, p.9 | REPLACE | Replace narrowly assembled experimental novelty claim with bounded computational question. Literature coverage here cannot prove absence of prior work. |
| §3.1 primary objective, p.9 | REPLACE | Evaluate quantified clearance effects on geometry and contact/stress trade-offs, not measured strength. |
| §3.2 objectives, p.9 | REPLACE | Original numbering starts at 7 and ends at 14. New objectives are numbered 1–5 with distinct modeling, verification, validation, uncertainty and decision roles. |
| §4 hypotheses, p.9 | REPLACE | Convert null-hypothesis tests on replicated specimens into falsifiable numerical propositions judged against numerical error and parameter uncertainty. No p-values from deterministic reruns. |
| §5.1 material, p.10 | REPLACE | No procured material is asserted. Establish admissible property/evidence requirements; material grade remains unresolved. |
| §5.2 FDM process, p.10 | MOVE TO SUPPLEMENT | Archive original nominal print conditions as proposal metadata only, not manufactured state or validated simulation inputs. |
| §5.3 specimen geometry, p.10 | REPLACE | Choose geometry later against validation availability. Do not claim ASTM D638/D790 geometry compliance or import incomplete specimen dimensions. |
| §5.4 allocation, p.10 | REPLACE | Replace print-plate randomization with immutable model/case IDs, input hashes and run logs. |
| §5.5 conditioning, p.11 | REPLACE | Reference temperature and initial state need definition; laboratory conditioning schedule is not numerical validation. |
| §5.6 baseline, p.11 | KEEP BUT REWRITE | Retain signed response and aggregate definitions; replace micrometer repeats with named geometric landmarks and frame alignment. |
| §5.7 annealing setup, p.11 | KEEP BUT REWRITE | Retain candidate temperatures/durations. Replace oven/probe instructions with prescribed ambient history, solved part history, attainment and release rules. Do not adopt arbitrary below-50 °C release. |
| §5.8 sand, p.12 | REUSE AS LITERATURE CONTEXT | Remove drying, packing and tray prescriptions. Granular modeling is outside current primary scope. |
| §5.9 salt, p.12 | REUSE AS LITERATURE CONTEXT | Preserve sub-melting/remelting distinction; delete salt preparation and cleaning method. |
| §5.10 fixture, p.12 | KEEP BUT REWRITE | Preserve opposed plates and stops. Reject unexplained hot thickness +0.05 mm as universal clearance. Define reference total gap, films, expansion, friction and unilateral contact. |
| §5.11 matrix, pp.12–14 | REPLACE | Keep thermal design levels only. Remove 25-specimen screen, 3 × 3 × 2 replicated design, selected-support alias, reuse counts and 130 total. Gap levels/case count are unresolved. |
| §5.12 tensile, p.14 | DELETE | No UTM tests, extensometer data, UTS or tensile confirmation in this computational stage. |
| §5.13 flexural, p.14 | DELETE | No three-point physical confirmation; strength transfer cannot be inferred from annealing stress. |
| §5.14 dimensions, p.15 | KEEP BUT REWRITE | Define evaluated geometry after cooling/release; record dimensions independently from warp. |
| §5.15 DSC/microscopy, p.15 | REUSE AS LITERATURE CONTEXT | No planned DSC/SEM or calculated crystallinity; remove 93.0 J g⁻¹ reference from current methods until an applicable verified source and model need exist. |
| §5.16 standards, p.15 | KEEP BUT REWRITE | Table 7 says F3498-23; reference [3] says F3489-23 with an inaccurate title. Correct both using ASTM catalog. Retain F3489 only for evaluating published mechanical data, not as an ANSYS standard. |
| §5.17 responses, p.15 | REPLACE | Retain geometry; add temperature histories, reaction/contact and residual stress as future solver quantities. Remove UTS, strain at break, mass change and DSC as promised outputs. |
| §5.18 statistics, pp.15–16 | REPLACE | Replace n=5, α=0.05 and 95% confidence intervals with discretization error, calibration identifiability, independent discrepancy and justified uncertainty. Preserve principle that practical tolerances differ from significance. |
| §5.19 safety/feasibility, p.16 | DELETE | Physical lab checklist does not describe computational methods. Track software/license and material validity instead. |
| §6 heading/preamble, p.16 | REPLACE | No “Results” filled with literature. New evidence-status section says which numerical claims are unavailable and what makes them reportable. |
| §6.1 temperature, p.16 | REUSE AS LITERATURE CONTEXT | Remove implied center optimum and unverified cross-study quantitative optimum; candidate range is not validated for a selected grade. |
| §6.2 duration, p.16 | KEEP BUT REWRITE | Preserve hold-start/thermal-lag insight; do not assert saturation without a history-dependent law and evidence. |
| §6.3 strength, pp.16–17 | REUSE AS LITERATURE CONTEXT | Remove numerical tough-PLA ring values from current manuscript pending exact-source verification; not validation for plate fixture. |
| §6.4 modulus/ductility, p.17 | REUSE AS LITERATURE CONTEXT | Retain limitation on strength inference; remove measurement instructions. |
| §6.5 shrinkage/warp, p.17 | KEEP BUT REWRITE | Link hypothesized irreversible strains to identifiable material data; no recovered-stress field is invented. |
| §6.6 sand, p.17 | REUSE AS LITERATURE CONTEXT | Do not assert sand superiority for the computational domain. |
| §6.7 salt, p.17 | REUSE AS LITERATURE CONTEXT | No remelting physics is transferred to sub-melting PLA. |
| §6.8 fixture, p.17 | KEEP BUT REWRITE | Retain expansion/friction/stress risks as questions, not observed effects. Add post-release springback. |
| §7 optimization, pp.18–19 | KEEP BUT REWRITE | Keep nondominance and transparent preferences. Use geometry/stress/process objectives conditional on valid predictions; no UTS objective, fictitious Pareto front or new-specimen confirmation. |
| §8 and §8.1 significance, pp.19–20 | KEEP BUT REWRITE | Reframe tooling relevance as potential geometry-specific decision support; do not promise cost savings or qualification. |
| §9 limitations, p.20 | REPLACE | Replace specimen power/equipment limitations with material law, initial-state, contact, validation-transfer and numerical error limits. |
| §10 future scope, p.20 | KEEP BUT REWRITE | Keep geometry dependence and model refinement as boundaries, not a new experimental project. Do not execute later stages now. |
| §11 conclusion, pp.20–21 | REPLACE | Conclude conversion and defined evidence requirements only. Remove laboratory execution and preferred central-region suggestion. |
| References [1]–[50], pp.21–23 | MOVE TO SUPPLEMENT | Preserve exact extracted entries and per-entry disposition catalog. Retain only checked, cited sources in current bibliography; do not silently authenticate all 50. |
| Appendix A, p.24 | REPLACE | Delete physical allocation tables; use computational provenance requirements without manufactured run rows. |
| Appendix B, p.24 | KEEP BUT REWRITE | Retain immutable IDs and failed-record principle, replacing specimen/plate/oven IDs with case/configuration/solver hashes. |

## Equation audit

| Base equation | Disposition | Resolution |
|---|---|---|
| (1), p.11 | KEEP BUT REWRITE | Use δᵢ for signed percentage response; reserve Δdᵢ for dimensional displacement. Explicit initial/final reference temperature. |
| (2), p.11 | KEEP BUT REWRITE | Keep RMS of three signed percentage components; typeset square root and indices. RMS cannot show direction. |
| (3), p.11 | KEEP BUT REWRITE | Keep normalized error, define positive dimensional tolerances. RMS ≤1 alone does not guarantee every axis passes; require individual bounds. |
| (4), p.15 | DELETE | DSC crystallinity equation is not used without DSC evidence or a calibrated crystalline-state law. |
| (5), p.18 | KEEP BUT REWRITE | Keep weighted geometric desirability as optional secondary ranking, professionally typeset; no chosen weights or computed score. |

## Figure inventory

| Figure / page | Disposition | Reason |
|---|---|---|
| 1 / 6: FFF deposition | MOVE TO SUPPLEMENT | Generic educational schematic; unnecessary in focused manuscript. |
| 2 / 7: annealing mechanisms | REPLACE | Avoid suggesting every thermal cycle yields crystallization or benefit; express mechanisms in conditional prose. |
| 3 / 8: support comparison | REPLACE | New unique plate-gap schematic focuses on quantified constraint. |
| 4 / 11: metrology | KEEP BUT REWRITE | Response definitions retained in equations; no physical measurement schematic required. |
| 5 / 12: support comparison | DELETE | Caption explicitly states duplication of Figure 3; visual review confirms same diagram. |
| 6 / 13: experimental workflow | REPLACE | New traceability requirements are computational. |
| 7 / 14: two-stage specimens | DELETE | Entire screen/UTM/flexural logic is obsolete. |
| 8 / 14: blocked factorial | REPLACE | Thermal-level table replaces physical replication layout; numerical gaps are not yet selected. |
| 9 / 19: conceptual Pareto | DELETE | No data-backed frontier exists; visual has clipped left-axis label in base. Use mathematical decision definition, not a curve that could resemble results. |

## Table inventory

| Table / page | Disposition | Resolution |
|---|---|---|
| 1 / 6: thermal regimes | KEEP BUT REWRITE | Condense in material-evidence discussion; no generic transition values. |
| 2 / 8: literature synthesis | REUSE AS LITERATURE CONTEXT | Merge selective verified context; original breadth is not source verification. |
| 3 / 9: hypotheses | REPLACE | Numerical propositions without specimen null tests. |
| 4 / 10: print settings | MOVE TO SUPPLEMENT | Archived base only; no actual printing or adopted numerical inputs. |
| 5 / 12–13: factors | REPLACE | Keep temperatures/durations labeled as inherited design choices. |
| 6 / 13: specimen counts | DELETE | No physical sample accounting belongs in numerical methods. |
| 7 / 15: standards | KEEP BUT REWRITE | Correct F3489 title/number; retain only relevant appraisal role. |
| 8 / 15: response hierarchy | REPLACE | Solver response/evidence requirements, no UTM/DSC outputs. |
| 9 / 18: literature responses | REUSE AS LITERATURE CONTEXT | Remove unverified numeric ring values and study optima; no local Results table. |
| 10 / 18: expected trends | REPLACE | Falsifiable model propositions; no expected optimum. |
| 11 / 19–20: industry supports | DELETE | Qualitative burden ranking does not establish computational performance or costs. |
| A1 / 24: definitive specimens | DELETE | Do not relabel specimen counts as solver runs. |
| A2 / 24: confirmation | DELETE | No new physical confirmation or optimum assigned. |

## Bibliographic and numerical carry-over policy

The archived reference catalog records each of the 50 entries. Entries [3], [35], [42], [50] are retained after limited independent verification; the remaining entries are pending verification and excluded from the current bibliography, not declared false. Reference [3] needs both the F3498→F3489 correction in the body and a corrected official title. The original's “verified” annotations are not independent proof.

Inherited temperatures and durations are user-authorized candidate design settings. The original 0.05 mm hot allowance, filament and coupon dimensions, print settings, 93.0 J g⁻¹ enthalpy reference, tough-PLA deformation percentages and cross-study optimum are not adopted as numerical findings or calibrated inputs. No source-backed material constants are assigned at this stage.
