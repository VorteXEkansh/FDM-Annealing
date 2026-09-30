# Stage 18 full manuscript reconstruction

Date: 30 September 2026. The assertion that all scientific computation should now be complete is not supported by the repository. Numerical verification exists; production annealing, independent physical validation, global sensitivity, propagated uncertainty, optimization and new optimum confirmation do not. The article is therefore reconstructed as a numerical-verification contribution with explicit limits, not as a completed production study. No new solver result is generated in this stage.

## Article-wide changes

- Replaced the title with “Numerical verification of a thermo-mechanical framework for gap-constrained annealing of FFF-printed PLA.” Names and affiliation remain as supplied, without inventing author declarations.
- Replaced the long stage-by-stage abstract with an article abstract reporting actual thermal, structural, Prony and convergence results and their numerical-fixture scope.
- Rebuilt Introduction and Background around prior supported annealing, constitutive precedents and a bounded research gap. The literature search cutoff remains 12 September 2026; bibliographic checks do not imply a new exhaustive search.
- Reorganized methodology into Sections 3.1–3.16, separating executed reference methods from unimplemented production requirements. Reference geometry, schedules, synthetic inputs, units, errors and thresholds remain explicit.
- Reorganized Results into Sections 4.1–4.18. Verification and discretization have actual values; unavailable production/validation/optimization results are described as unavailable without dummy rows or plots.
- Rewrote Discussion and seven quantitative Conclusions around archived evidence. The missing scientific work remains an explicit publication limitation. Data Availability, Code Availability and Declarations are now article sections.
- Moved the competitor matrix, 23-branch coefficient table, full fixture property table, validation means, detailed thermal/Prony comparisons and contact-control table to integrated Supplementary Tables S1–S7. Full machine-readable matrices remain in the repository. Removed the repeated observation-only validation plot from the main article; its original file remains immutable and available.
- Retained and checked the 40-entry reference list against existing bibliographic evidence. No new DOI, source finding, author declaration or search claim is invented.

## Equation audit and correction

The previous 24-equation map remains a historical artifact. `docs/manuscript_equation_map.csv` is the current 21-equation map, recording each new number and its former number. The formulas were checked against `src/constitutive.py`, thermal/structural reference generators, convergence calculation and validation metric functions.

The former strain-partition equation included an annealing strain term not used by the material-point update. The current equation states the implemented elastic + delayed + thermal core; absent bulk irreversible strain is discussed explicitly in Section 3.7. The independently imposed eigenstrain benchmark remains a synthetic verification problem. No material law was added or silently zero-filled.

Former equations 15 and 16 (production landmark dimensions and aggregate dimensional error) are omitted as numbered formulas because their extraction was not implemented. Former equation 17 described a three-dimensional area-weighted plane-fit warpage extractor that was not implemented; the actual two-dimensional fitted-line benchmark definition is stated in words with its region. No unused crystallization, desirability or sensitivity equation is added. All retained numbered equations have actual implementation mappings, while their applicability remains limited to reference/calculation cases.

The heat-reference diffusivity and structural thermal-expansion symbols are distinguished in the surrounding definition. The Prony ramp's Eᵢ is explicitly the same source branch modulus kᵢ. Identical normalized shear/bulk kernels and midpoint temperature approximation remain disclosed.

## Quantitative evidence and correction

The abstract and seven conclusion findings trace to `verification/thermal_verification.csv`, `verification/structural_verification.csv`, `verification/contact_verification.csv`, `convergence/mesh_convergence.csv`, `convergence/timestep_convergence.csv` and `docs/stage_10_convergence_checks.json`. They are not experimental findings or production recommendations.

The rewritten contact discussion compares friction using the same augmented-Lagrange control and FKN = 1, rather than mixing it with a normal-Lagrange endpoint. At μ = 0 and 0.3 the genuine mean pressures are 17.5367683291 and 20.0333528221 MPa; peaks are 24.4283504486 and 51.8788375854 MPa. The manuscript rounds these to four decimal places. Source: `convergence/contact_sensitivity.csv`. The raw file is unchanged.

Publication versions of the three convergence plots are redrawn from unchanged CSV data under figures/publication/. Their titles omit project-stage labels; the original images remain intact. The publication plotter and its input/output hashes are recorded separately.

## Completion boundary

Reconstruction, equation audit, regression checks, PDF production and repository delivery are this stage's work. They do not complete the missing research. Authorship contributions, funding, conflicts and corresponding-author details require human confirmation before journal submission. Stop at Prompt 18.
