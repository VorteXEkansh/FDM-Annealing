# Stage 13 production design entry decision

Date: 29 September 2026. **Blocked: validation is not acceptable for the research objectives because it has not been executed.** The user's explicit entry condition prevents finalizing the production matrix or launching representative cases. Stage 12's failed admission is not poor agreement and is not successful validation.

## Current evidence and authorized boundary

`validation/validation_report.md` and `simulation/validation/stage12_admission_01/admission.json` establish that all six predeclared source-specific conditions were rejected before solver launch. The 18 external means have no matched predictions. Compatible material/recovery/initial-state evidence, physical histories and support definitions, a verified source-specific adapter, reproduction convergence and comparison uncertainty remain unresolved. The distinct Prusament production formulation and plate-gap fixture have no independent predictive validation. Earlier verification and convergence cannot substitute for that evidence.

`simulation/design_matrix.csv` and `simulation/case_manifest.csv` intentionally contain headers and no cases. They are empty registries, not a finalized design or a zero-response campaign. No case IDs, low/middle/severe selections, solver jobs or run directories are assigned. `docs/stage_13_design_checks.json` records this entry decision and evidence hashes; its passing software checks do not imply a passing dry run.

## Candidate factors are not approved conditions

The requested 80 °C, 95 °C and 110 °C with 30 min, 60 min and 90 min remain inherited candidate factors. Only 80 °C lies inside the direct 23–85 °C Prusament characterization interval, and that overlap alone admits neither its holding times nor the bulk recovery model. No extrapolation to 95 °C or 110 °C is permitted by the present evidence.

The Stage 7 gap screen is geometric: total clearances 0, 0.01, 0.02, 0.04 and 0.08 mm. None is a physically approved production level. The user examples G025 and G050 must not silently override that screen or be read as approved 0.025 mm and 0.050 mm cases. FREE and initially touching GAP are different boundary conditions even at zero clearance. FREE has no fixture clearance; it must never be encoded as a zero-gap contact case.

## Deferred identifier and execution contract

After acceptable validation and explicit scope/domain admission, use a deterministic naming convention: T followed by zero-padded integer degrees Celsius, H followed by zero-padded whole holding minutes, and FREE or G followed by zero-padded total clearance in micrometres. G025 would denote 25 µm = 0.025 mm, never 25 mm or per-face clearance. Values requiring fractions of these encoding units need a documented naming revision, not rounding. No executable IDs are generated now.

Before selecting low, middle and severe cases, establish which physical severity measure matters: temperature, duration and contact engagement do not define a guaranteed monotonic ranking. Select representatives only from the validated and admitted domain; document their purpose and ensure that FREE and contact behavior are exercised. Each dry run must archive input/script hashes, exact solver version and command, unique local run directory, raw fields and solver logs, convergence assessment, extraction definition and units. Path and naming checks alone are insufficient.

Required checks remain **not run**: production automation, solver convergence, field extraction, solver-unit conversion and raw solver preservation. CSV schemas and their empty status were checked. No successful dry run is claimed, no full sweep is authorized, and no Prompt 14 work starts.

## Recovery requirement

Resolve the Stage 12 physical-model and validation barriers without tuning reserved observations, then assess applicability to the production grade, thermal range, geometry and fixture objectives. Freeze the resulting admitted model, boundary history, release/observation rules and production convergence before final design selection. A documented scope reduction may be necessary if only a narrower observable or temperature domain can be validated; this record does not grant such a reduction or reinterpret missing validation as acceptance.
