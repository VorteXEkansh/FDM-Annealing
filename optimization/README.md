# Optimization registries

Both CSV files are header-only in Stage 17 because there are no eligible model predictions and no selected confirmation conditions. Blank registries mean analysis unavailable, not no feasible solution or no trade-off.

- `pareto.csv`: eventual case-level objective and feasibility records. `combined_dimensional_error` requires the declared dimensionless metric definition; no metric is computed here. `residual_stress_MPa` and `maximum_contact_pressure_MPa` require their distinct spatial/time definitions. `cycle_time_s` must include the declared full cycle. `nondominated` is not assigned until the feasible comparison set exists. Preference-specific rankings remain conditional on explicit scaling and limits.
- `confirmation.csv`: eventual long-form, one response per new run. `confirmation_role` distinguishes recommendation, neighbor 1, neighbor 2 and thermally matched FREE. Frozen predictions and new solver responses must have the same definition and `unit`. Signed error is prediction minus the new ANSYS solution; relative error uses the new solution's nonzero magnitude. Preserve failed runs with blank unavailable responses and reasons once actual attempts exist. No attempts are fabricated now.

Protocol: `docs/optimization_protocol.md`. Physical strength, robust-window claims, desirability scores and numerical acceptance thresholds are not supplied by these schemas. Raw evidence remains immutable at its original location; future confirmation paths must identify new run artifacts and hashes.
