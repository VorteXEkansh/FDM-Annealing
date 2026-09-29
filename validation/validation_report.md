# Stage 12 independent validation execution assessment

Date: 29 September 2026. **Scientific validation remains incomplete.** Six source-specific case specifications were built and submitted to the execution admission check; all were rejected before solver launch. No ANSYS validation prediction exists, no comparison metric is computable, and no production sweep is permitted. This is neither poor measured agreement nor an ANSYS convergence failure. It is an unresolved physical-model definition.

## Frozen protocol and execution evidence

The Stage 11 protocol in `docs/validation_protocol.md`, observations and calibration register are unchanged. The primary reserved observations remain the six mould-free conditions of Lluch-Cerezo et al., DOI [10.3390/polym14132607](https://doi.org/10.3390/polym14132607), Table 5. All 18 signed directional means remain reserved. The three secondary maxima remain quarantined; neither dataset was fitted.

`simulation/cases/validation/LC22_free_*.json` records the source geometry, print orientation, oven ramp, treatment duration and target temperature for each condition. Missing physical inputs are null. Geometry is nominal; it does not invent individual initial dimensions. The 80 mm × 10 mm × 4 mm bar is distinct from the project's 60 mm production concept. The source's 120 min treatment is retained, rather than replacing it with the production design's 30–90 min. L aligns with the roads, H with the build direction and W with the transverse direction.

Command: `python -X utf8 scripts/run_validation_cases.py --execute`. Its expected exit status 2 indicates rejection before solver execution. The immutable admission record is `simulation/validation/stage12_admission_01/admission.json`: every case has `solver_started=false`, no solver command and no solver return code. Its input hashes identify the case specifications, frozen protocol, observations, material database and code. No MAPDL deck, result file, contour or history was fabricated. The installed solver remains the previously verified Ansys Student MAPDL 2026 R1; solver availability is not the present blocker.

## Source reappraisal and unresolved inputs

The archived source XML was re-read at §§2.1–2.4, Table 5 and the Data Availability Statement. Geometry, print architecture and selected oven settings are specified. Grade-compatible thermal functions, elevated-temperature constitutive evolution, initial printed state, actual specimen thermal history and mould-free support/release details are not supplied. The Data Availability Statement supplies no further dataset. This is a limitation of the accessed evidence, not proof that no additional records exist.

A targeted search on 29 September 2026 used: `"Ultimaker" "Pearl White" PLA annealing thermal conductivity relaxation shrinkage`; `"10.3390/polym14132607" data availability`; `site.ultimaker.com PLA technical data sheet thermal expansion shrinkage`; `"Ultimaker" "PLA" "Prony" annealing`; and `"Pearl White" "PLA" "specific heat"`. The supplier's complete three-page [PLA data sheet](https://um-support-files.ultimaker.com/materials/2.85mm/tds/PLA/Ultimaker-PLA-TDS-v5.00.pdf) was retrieved and archived with SHA-256 under `literature/evidence/stage_12/`. Its filename contains v5.00, while the document itself says v2.00, 20 April 2022; this discrepancy is retained. Pages 2–3 report mechanical tests and thermal transition properties, but no annealing recovery law, Prony/shift set or k(T)/cₚ(T) functions. The print architecture differs from the validation specimens. No supplier numbers were admitted to a solver card. Search hits for other colors/formulations or creep after heat treatment do not independently identify the required Pearl White annealing history model. They were not substituted for it. The search was targeted, not an exhaustive claim of absence.

The nine pre-solver blockers in each case are: compatible thermal functions; compatible mechanical law; irreversible strain and initial state; complete specimen thermal history; support/gravity/release; observation state and landmark mapping; verified non-isothermal adapter; case-specific convergence; and implemented source-specific solver adapter. The separate numerical and measurement bounds are also absent. Those comparison bounds prevent a validation acceptance claim even if descriptive predictions later become possible.

`validation/validation_deviations.csv` lists every currently identified difference or unresolved match between the source and available project implementation. There are no executed simulation deviations because there are no executed simulations. A changed source-specific model requires a new versioned case/admission record; the present record must not be overwritten.

## Results and predeclared metrics

`validation/validation_results.csv` retains all 18 primary observations with explicit blocked status. Prediction, signed error, absolute error, relative error and solver provenance cells are blank. `validation/validation_metrics.csv` contains the three prespecified directional groups: each requires six matched conditions and currently has zero predictions. MAE, RMSE and worst absolute error are therefore blank, not zero. The predeclared metric implementation is unchanged. R² is not calculated.

`figures/validation_observations.png` and its SVG show only the published observations, with no invented error bars. This is a source-data figure, not a prediction comparison. A parity plot requires paired experimental and solver values; none can honestly be generated at this stage. No nominal-dimension conversion is used to manufacture displacement targets. Height change is not renamed warpage.

## Diagnosis and permissible recovery

No measured mismatch can yet be attributed to a cause. The following are prospective obstacles, not a fitted explanation of residuals:

| Issue | Evidence and consequence | Required recovery before a new run |
|---|---|---|
| PLA grade | Prusament calibration differs from Ultimaker Pearl White | Independently characterized source-compatible law; declared calibration lineage must be revised before any new fitting |
| Constitutive assumptions | Isotropic relaxation core lacks directional irreversible annealing strain and initial printed state | Independently measured recovery/initial-state evidence; do not fit reserved final dimensions |
| Thermal boundary | Oven ramp does not determine part temperature or cooling/support path | Source history or independently justified bounded scenarios, with thermal properties and heat-transfer coefficients |
| Annealing-strain uncertainty | No compatible evolution law or supported parameter bounds | Identify a law and calibration evidence before solving; do not impose the final observed strain |
| Geometry and orientation | Nominal bar and road axes known; production coupon differs | Source-specific mesh, landmark extraction and convergence; raw initial dimensions where needed for uncertainty |
| Measurement uncertainty | Instrument accuracy is not condition scatter or uncertainty of percentage change | Source-compatible measurement bounds, including initial/final measurements and their dependence |

No recalibration was performed. The declared Chapuis calibration set concerns Prusament and does not supply missing Pearl White recovery information. Repeating that calibration cannot establish cross-grade validity. Any future use of reserved outcomes for model selection or fitting requires reclassifying whole correlated condition groups and obtaining genuinely independent validation evidence. No undocumented split or optimization of agreement is allowed.

**Decision:** the current model cannot be credibly independently validated against the reserved experiments. Validation execution is blocked and scientifically incomplete; documentation, source appraisal and admission accounting are complete. No successful validation, residual-stress/contact validation, production recommendation or optimum is claimed. Stop at Prompt 12.
