# Stage 16: surrogate, sensitivity and uncertainty admission

Date: 30 September 2026. **Execution blocked: no eligible production responses and no admitted probabilistic input model.** This is a prospective project protocol and evidence audit, not an executed statistical study. Stage 8–10 verification configurations cannot substitute for the production response surface. Literature validation targets remain reserved and are not surrogate training data.

## Data and response contract

Use only traceable, successful, admitted production solver exports with case/input/output hashes, material and numerical versions, physical units, response definition, and common cooling/release observation state. Preserve failures and exclusions explicitly. Warpage, dimensional error, residual stress and contact pressure require separate response definitions and applicability domains. A released contact pressure is not interchangeable with peak in-fixture pressure. FREE is a distinct boundary condition, not a numeric zero-gap point; no-contact fixture responses must be resolved before fitting a smooth surface across contact onset. The current all_cases.csv is header-only. No fit, score or propagated result is possible.

## Conditional surrogate and cross-validation design

After an admitted design exists, compare a simple response surface with a Gaussian-process candidate only if the number, spacing and coverage of unique cases support estimation. Model family, term order, kernel, folds and acceptance limits remain unselected; selecting them now would invent a data-dependent design. Freeze case eligibility and groups before fitting. Keep each physical design condition, duplicate/restarted run, discretization variant and correlated response in the same outer fold. Fit scaling and any response transformations inside the training fold. If tuning or model selection is needed, use an inner training-only split; reserve outer predictions for performance assessment. If there are too few independent groups, decline the cross-validation claim and acquire more genuine cases.

Retain an out-of-fold prediction/error record for every eligible held-out case and report MAE and RMSE separately in each response's units. Retain signed errors and worst discrepancies. R² is conditional on enough varied held-out responses and a meaningful nonzero response variance; constant/near-constant targets and sparse folds require omission or explicit undefined status. Training scores alone are insufficient. Surrogate-to-solver agreement does not validate the physical model. Check contact-regime coverage and boundaries, and confirm consequential surrogate predictions with new genuine solver evaluations. No such folds, metrics or confirmations exist now.

## Deterministic design variation

Temperature, attained-temperature holding time and fixture clearance are design choices, not sampled material randomness. Compare FREE separately from the continuous GAP domain. Any global design ranking needs an explicitly declared domain and weighting measure; it is conditional on those choices. A finite deterministic response range is not a probability interval. Morris screening would require an admitted perturbation domain and actual trajectories; Sobol indices would require a justified joint input model, appropriate handling of dependence and estimator convergence. Neither method is executed or selected merely by name. Verification friction-control changes are not the production global sensitivity study.

## Uncertain physical inputs

The source audit in data/processed/uncertainty_input_audit.csv addresses E, α, k, cₚ, annealing strain, convection, friction and fixture CTE. Existing source tables remain unchanged. Supplier modulus intervals are cross-checks, not a temperature-dependent distribution. Bilayer pre-strain method brackets are not bulk shrinkage uncertainty. Missing thermal functions, boundary coefficients, friction and fixture expansion convention remain missing; arbitrary percentages or cross-grade extrema are inadmissible substitutes. Joint dependence and consistency among the Maxwell spectrum, relaxation clock and modulus must be established before perturbation, rather than scaling redundant properties independently.

Latin-hypercube or Monte Carlo propagation requires an admitted forward model, source-supported input bounds/marginals and dependence, plus a fixed conditional process design. With bounds alone, report deterministic scenario bounds with their scope instead of probability coverage. With a defensible probabilistic model, predeclare estimands, sampling/seed policy, sample-size convergence and the interval interpretation, retaining all failed samples and their impact on coverage. Gaussian-process predictive spread is surrogate approximation uncertainty, not physical-input uncertainty or physical validation. No input samples, output quantiles or intervals are generated in this stage.

## Separate uncertainty accounts

Report deterministic process variation separately from physical-input uncertainty. Keep production mesh/time/contact discretization assessment separate from both; the Stage 10 reference-case percentages are not error bars for unbuilt production cases. Track surrogate approximation error and physical model discrepancy as additional distinct limits. Do not add unrelated spreads into a single confidence interval or infer independent experimental replication from deterministic reruns.

## Current outcome and recovery

scripts/check_surrogate_stage.py verifies frozen Stage 15 inputs and generates blank-metric response availability and input-admission tables, with source/script/output hashes. Passing the audit does not mean a fitted surrogate or uncertainty analysis passed. Required recovery is source-compatible model/boundary closure, non-isothermal implementation, production convergence, acceptable independent validation, approved design/dry run and a genuine campaign; then establish uncertainty evidence and independent out-of-fold assessment. No optimization is performed. Stop at Prompt 16.
