# Master investigation delivery report

Date: 1 November 2026. **The original validated production study is incomplete;
this is an evidence-limited numerical verification and feasibility package.**
The manuscript is not certified publication-ready, and no official release tag
or journal submission is made.

| Requested field | Established outcome |
|---|---|
| Final title | Contact feasibility and non-isothermal verification for gap-constrained annealing of FFF-printed PLA |
| Target journal | Progress in Additive Manufacturing, conditional scope match; submission as a completed predictive processing study is not recommended. Current instructions and alternatives are recorded in `master_journal_fit.md`. |
| Achieved contribution | An auditable temperature-shift implementation and a demonstrated distinction between fixture mounts that can reverse contact at the same nominal clearance. No exclusive priority is claimed for the elementary contact relation, ANSYS, a fixture or optimization. |
| Material | Source-identified Prusament PLA. Alternative Black Devil Design and Ultrafuse data were examined, not silently merged. |
| Constitutive model | 23-branch generalized Maxwell reference with Arrhenius/WLF reduced time, reversible expansion, constant assumed Poisson ratio, and an explicitly assumed equal normalized shear/bulk extension. A separate scalar programmed-road calculation initializes balanced internal stresses. The latter is not a production ANSYS recovery law. |
| Solver | ANSYS Student 2026 R1, Mechanical APDL 26.1, update 20260202. |
| Temperature validity | Source characterization: 23–85 °C. Verified transient reference: 23–80–23 °C. Independently physically validated coupon annealing range: none established. Characterization coverage does not validate long holds. |
| Production simulations | Zero approved and zero completed. Six new reference attempts accepted among 13 recorded attempts; launch, equilibrium, accuracy and contact-normal failures/exclusions remain traceable. |
| Independent validation errors | Not calculable. Six additional published means are reserved without fitting or prediction; earlier observations remain intact. Numerical-reference errors below are not experimental validation errors. |
| Non-isothermal verification | All 26 final samples pass the predeclared mixed tolerance. Maximum absolute stress difference 0.0001063963 MPa; RMSE 0.0000364250 MPa. |
| Temporal refinement | Final step 0.025 s. Halving 0.05 s to 0.025 s changes sampled stress by at most 0.0000933036 MPa; halving the shift-table interval to 0.125 °C changes it by at most 0.00000607967 MPa. Both comparisons pass the declared mixed criterion. Independent reference-step halving changes stress by at most 0.00000000844200 MPa. These are reference-history checks, not production error bounds. |
| Mesh convergence | Prior 28 selected convergence runs and 63 audited mesh/time response records remain verified and reusable for their reference configurations. No production-specific 3-D mesh convergence is claimed. |
| Contact finding | At 80 °C and 0.020 mm total clearance, critical signed free thickness strains are +0.1124%, +0.2041% and −0.1156% for fixed inner spacing, expanding inner spacers and fixed outer faces. The last elastic reference carries 7.350 N and separates on cooling. All 36 corrected stop states pass gap, force and status checks. |
| Dimensional response | Scalar initialized recovery approaches its programmed 5.6175% limit. This is a source-conditioned numerical mechanism check, not an observed or predicted bulk coupon contraction. |
| Warpage and residual stress | No released coupon field is predicted. Rigid-motion-invariant measurement operators are tested. The restrained thermal reference stress cannot be reclassified as released residual stress. |
| Sensitivity and uncertainty | Ninety deterministic contact scenarios; no physical-input probability distributions, global sensitivity indices or uncertainty intervals. Mount alternatives are designs, not uncertainty samples. |
| Pareto processing region | Not established; optimization registry remains empty. |
| Independent confirmation | No optimized production condition exists to confirm. Numerical refinement runs are not optimization confirmations. |
| References | Main article: 13 references, including ten verified DOI identities. Supplement: retained 41-entry legacy reference key for prior tables. |
| Figures and tables | Main: three code-generated figures, one table and eight editable equations. Supplement: 17 tables. No AI-generated scientific figure. |
| Word and page counts | Main prose: 3,009 words, excluding headings, displayed equations, tables, captions and references; abstract: 180 words. Main PDF: eight pages; Supplementary PDF: 32 pages. |
| Visual review | All 40 final PDF pages inspected; main PDF exported from the editable Word document. Exact artifact and render hashes are in `master_visual_review.json`. |
| Reproducibility | 98 unit tests pass; 1,121 frozen evidence records checked; 274 new trace records accompany the retained 384-record index. Figure/table, equation, source and artifact manifests are maintained. Repeating solver work requires licensed compatible ANSYS; rebuilding the main PDF requires the recorded Word environment. |
| Git checkpoint and milestones | Baseline `d23a9ecd097072bf8165a36fa731e8e15910122f`; safe checkpoint `1608028`; scientific milestone `31dcc70`. The final document commit and remote equality are reported in the delivery response; this avoids embedding a self-referential commit hash. Branch: `codex/master-research-completion`. |

The ordered remaining requirements are in `master_remaining_blockers.md`:
compatible printed initial state and directional recovery histories, thermal
closure, a physically specified fixture and release protocol, coupled production
implementation, production convergence, independent physical validation, and
only then the campaign and downstream analysis. Further benchmarks or arbitrary
cross-grade coefficients would not resolve these evidence gaps.

The authoritative documents are in `output/master/`. The complete current main
PDF also updates the evolving DRAFT path. Historical Stage 20 documents and all
legitimate solver evidence are preserved. No old benchmark was rerun merely to
increase the result count.
