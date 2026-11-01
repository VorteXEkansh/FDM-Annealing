# Authoritative project state

Date: **1 November 2026**. Repository: https://github.com/VorteXEkansh/FDM-Annealing.
Branch: `codex/master-research-completion`. Checkpoint: `1608028`.

## Current scientific status

The master investigation has completed additional numerical verification,
fixture-feasibility calculations and an original reconstruction of the manuscript.
**The intended validated production annealing study remains incomplete.** There
are zero approved/completed production simulations, no independent physical
validation error, no production sensitivity/UQ, Pareto solution or confirmation.
Integrity checks and solver success do not establish physical accuracy.

Current article title: **Contact feasibility and non-isothermal verification for
gap-constrained annealing of FFF-printed PLA**. Its achieved question concerns
mount-dependent contact feasibility and verification of a transient constitutive
implementation. The broader question about temperature, holding time and clearance
effects on released dimensions, warpage and residual stress remains conditional.
No processing recommendation or publication-readiness claim is made.

Current sources are `manuscript/master_body.md`, generated `manuscript/master.md`,
`manuscript/master_equations.json` and `supplementary/master.md`. Authoritative
outputs are the three files in `output/master/`: the main PDF, editable DOCX and
Supplementary PDF named Constrained-Annealing-2026. The complete main PDF also
updates `output/pdf/Constrained-Annealing-2026-DRAFT.pdf`. `output/release/` and
`manuscript/current.md` preserve the historical Stage 20 package. The dated prior
state is retained in `docs/history/stage20_project_state.md`; its stage limitations
must not override the current status below. No official completion release tag.

## Reusable verified work

The earlier one accepted thermal reference, six structural/contact references and
28 selected convergence runs remain intact. Fifteen superseded attempts among
43 convergence directories remain excluded and traceable. The original property
inventory, 23-arm spectrum, literature matrix, 45-observation validation register,
reproduction manifests and supplementary tables are retained. New audits verify
1,121 frozen evidence records; none is relabeled as a production result.

The new non-isothermal ANSYS test prescribes 23–80–23 °C, with heating/cooling at
1 K s⁻¹ and 60 s holds at each endpoint, for 234 s total. It uses an axially
restrained, laterally free SOLID185 reference, temperature-shifted shear and bulk
Prony spectra, full Newton iteration and explicit SHIFT rate-multiplier entries.
The final 0.025 s step/0.125 °C table passes all 26 samples against an independent
scalar integrator. Maximum sampled absolute stress error is 0.0001063963 MPa;
RMSE is 0.0000364250 MPa. The accepted 0.05-to-0.025 s refinement and halved shift
table both pass the declared mixed criterion. This is neither an oven model nor
production convergence. Seven attempts include one launch failure, one equilibrium
failure, two accuracy exclusions and three accepted refinements.

The source-conditioned programmed-road Python calculation now initializes balanced
internal stresses and recovers toward its imposed 5.6175% strain. It avoids adding
a second annealing eigenstrain for the same mechanism. It is not a bulk tensor,
not a production ANSYS implementation and not new experimental calibration.

Ninety deterministic clearance calculations distinguish fixed inner spacing,
expanding inner spacers and fixed outer plate faces. The 304/4301 supplier
20–100 °C interval-mean coefficient is explicitly approximated as constant and
rebased to 23 °C. At 80 °C and 0.020 mm total gap, the critical signed thickness
strains are +0.1124%, +0.2041% and −0.1156%. Three corrected single-brick 3-D elastic
stop cases pass 36 load-state checks. The fixed-outer-face reference gives 7.350 N
at 80 °C and separates on cooling. Three wrong-normal attempts remain archived.
These are limiting references, not distributed fixture pressures or warpage data.

The new best-fit-plane and signed fiducial operators are rigid-motion invariant
and tested, but have no production field to process. Archive-overwrite and
nonfinite/untraceable extraction defects were fixed. All 98 unit tests pass.

## Material basis and validation

The selected option is restriction of Prusament characterization to **23–85 °C**
for numerical component work. This is not a validated annealing interval for
30–90 min holds or arbitrary geometry. The 95/110 °C proposals are not admitted.
The 23-arm generalized-Maxwell model uses the source Arrhenius/WLF reduced clock,
constant assumed Poisson ratio and reversible thermal expansion. Equal normalized
bulk/shear relaxation is a 3-D isotropic extension, not measured volumetric data.

Compatible thermal conductivity/heat capacity, bulk printed initial state and
signed directional recovery histories are still unavailable. Black Devil Design
and Ultrafuse alternatives were investigated, not merged into Prusament. No
unknown value is replaced with zero and no probability distribution is invented.

Six new reserved means are recorded separately: two spring metrics and four
Prusament dog-bone dimensional means. The spring combines active Prusament and
passive Dutch Filament; the dog-bones use different printing/support conditions
and lack measured thermal histories. Neither is fitted or scored. Earlier
Ultimaker observations remain reserved. Physical MAE/RMSE cannot be calculated.

## Literature, article and review

Targeted literature searching extends through 1 November 2026, with accessible
primary records and access limitations recorded in `literature/master_search.json`.
Opposed-plate PLA annealing and numerical/optimization precedents are explicit.
The article has 13 references, ten DOI records and separate publisher corrections
for incomplete author metadata. No exclusive novelty is claimed for ANSYS, gap
clearance, optimization, or the elementary contact relation. The defensible output
is the documented contact-mechanism distinction and verified transient adapter.

Progress in Additive Manufacturing is a conditional scope match; submission is
not recommended as a completed predictive processing study. Current author
instructions are recorded in `docs/master_journal_fit.md`. Named authors must
confirm authorship, funding, conflicts and submission details. AI assistance is
disclosed; no new laboratory experiment is claimed.

Read `docs/master_research_audit.md`, `docs/master_material_decision.md`,
`docs/master_validation_decision.md` and `docs/master_remaining_blockers.md` before
resuming science. The blockers are ordered: compatible printed state and thermal
closure; actual fixture/observation boundaries; full coupled implementation;
production convergence; independent validation; campaign and downstream analysis.
More benchmark solves alone cannot identify missing physical inputs.

## Reproducibility and delivery

ANSYS Student 2026 R1, MAPDL 26.1, update 20260202, is confirmed by solver logs.
The recorded machine has eight physical cores, sixteen logical processors and
15.82 GiB RAM. New reference solves use one CPU. Native Word export supplies the
main PDF; ReportLab supplies the Supplementary PDF. Every final page is subject
to rendered inspection. See `reproducibility/MASTER_README.md`, master trace and
checksum registries, `docs/master_integrity.json` and the final visual review.
No copyrighted publisher PDF, credential or unnecessary solver scratch is added.
Meaningful commits and remote verification accompany delivery; no completion tag.

The final main article is eight pages (3,009 prose words; 180-word abstract), with
13 references, three figures, one table and eight editable equations. The
supplement is 32 pages with 17 tables. All 40 pages have passed rendered internal
inspection. The 98-test execution log and 1,148-check integrity report are retained.
`docs/master_completion_report.md` records every requested outcome, including
unavailable production/validation results. Git-byte auditing corrected newline
normalization in two source files to match their existing manifest bytes; no
solver result was changed.
