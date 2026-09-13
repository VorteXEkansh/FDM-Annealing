# Stage 8 transient thermal model and analytical verification

## Evidence boundary

Stage 8 contains one genuine Ansys Mechanical APDL transient thermal field
solution and a separate analytical calculation. It is a numerical verification
problem, not a Prusament PLA annealing prediction. The benchmark constants are
declared numerical fixtures and do not enter `material/pla_properties.csv`.

The production FREE/GAP model remains fail closed. Compatible Prusament
conductivity and heat-capacity functions have not been identified, the supplier
density lacks a test temperature, and the external oven history, convection,
surface emissivity, enclosure temperature and PLA–AISI 304 thermal-contact
conductance are not established. No cross-formulation comparator was substituted.

## Executed plane-wall benchmark

The reference domain is a 1 mm × 1 mm × 10 mm rectangular wall. The two faces
normal to z exchange heat by convection; the other four faces are adiabatic.
The resulting field is one-dimensional and corresponds to the classical
plane-wall solution. The declared constants are:

| Quantity | Verification value | Status |
|---|---:|---|
| Thermal conductivity, k | 0.5 W m⁻¹ K⁻¹ | numerical fixture |
| Specific heat, cₚ | 1000 J kg⁻¹ K⁻¹ | numerical fixture |
| Density, ρ | 1000 kg m⁻³ | numerical fixture |
| Convection coefficient, h | 5 W m⁻² K⁻¹ | numerical fixture |
| Half-thickness, L | 0.005 m | geometry calculation |
| Biot number, Bi = hL/k | 0.05 | reproducible calculation |

The solid starts uniformly at 20 °C. The ambient changes linearly from 20 °C
to 80 °C over 0–300 s, remains at 80 °C through 900 s, changes linearly back to
20 °C over 900–1200 s, and remains at 20 °C through 1800 s. This cycle contains
the initial state, heating, approach/hot hold, cooling and ambient recovery. It
is a verification schedule and does not define a physical annealing protocol.

MAPDL 2026 R1 build 26.1 update 20260202 used SOLID70, a mapped mesh of 640
elements and 1025 nodes, a full transient solution and a fixed 0.25 s time
increment. Each edge is 0.25 mm, yielding 40 elements through thickness and four
in each adiabatic direction. Nine center temperatures were retained. The solver
ran with one core in a local scratch directory; closed files were copied into
the repository and hashed. This avoids OneDrive file-mapping interference while
preserving exact evidence bytes.

Radiation is omitted only from this linear benchmark so that the analytical
boundary condition is identical. The benchmark has no fixture interface and
therefore does not verify thermal contact. These omissions are not findings that
radiation or contact is negligible in the annealing assembly.

## Analytical reference

For a wall with half-thickness L and two equal convective boundaries, the center
step response is

S_c(t) = 1 − ∑ Aₙ exp(−ζₙ²αt/L²),

where ζₙ tan ζₙ = Bi, Aₙ = 4 sin ζₙ/(2ζₙ + sin 2ζₙ), α = k/(ρcₚ), and Bi = hL/k.
For the piecewise-linear ambient history, Duhamel superposition gives

T_c(t) = Tᵢ + ∫₀ᵗ S_c(t − τ) dT∞(τ).

`scripts/run_thermal_verification.py` evaluates each linear segment in closed
form using 200 characteristic roots. Five unit tests verify the configuration,
root equation, initial modal coefficient sum, initial condition and qualitative
heating/cooling behavior. The analytical temperature is evidence class B, a
reproducible numerical calculation.

The absolute error is |T_ANSYS − T_ref|. The reported conventional relative
error uses absolute temperature in kelvin. Because a small absolute error can
look artificially small on that scale, the acceptance decision also uses the
temperature excursion from the 20 °C initial state:

e<sub>exc</sub> = 100|T<sub>ANSYS</sub> − T<sub>ref</sub>|/|T<sub>ref</sub> − 20 °C|.

Before accepted execution, the limits were fixed at 0.05 °C maximum absolute
error and 0.25% maximum excursion-relative error over the nine comparison times.

## Genuine comparison

The accepted `stage08_attempt_05` solver run exited with code 0 and no MAPDL
error messages. MAPDL reported one postprocessing warning because the convection
bulk temperature differs across retrieved result sets; the stored nodal
temperature solution is unaffected. The full machine-readable comparison is
`verification/thermal_verification.csv`.

| Time (s) | ANSYS center (°C) | Analytical center (°C) | Absolute error (°C) | Relative error (K, %) | Excursion-relative error (%) |
|---:|---:|---:|---:|---:|---:|
| 150 | 21.892109254 | 21.889130841 | 0.002978413 | 0.001009498 | 0.157660518 |
| 300 | 27.631062216 | 27.625947421 | 0.005114795 | 0.001700533 | 0.067070946 |
| 450 | 34.805348857 | 34.801718199 | 0.003630658 | 0.001178970 | 0.024528625 |
| 600 | 41.003870402 | 41.001387994 | 0.002482407 | 0.000790195 | 0.011820207 |
| 900 | 50.967098637 | 50.966218772 | 0.000879865 | 0.000271466 | 0.002841371 |
| 1050 | 53.056900023 | 53.059537028 | 0.002637005 | 0.000808378 | 0.007976533 |
| 1200 | 50.753732030 | 50.758912731 | 0.005180700 | 0.001599431 | 0.016842924 |
| 1500 | 42.903452036 | 42.906520281 | 0.003068244 | 0.000970790 | 0.013394633 |
| 1800 | 37.051786082 | 37.053501761 | 0.001715679 | 0.000553082 | 0.010060566 |

The authoritative values are the CSV, and integrity checks recalculate them
from the accepted raw solver output and analytical code. The
accepted maxima are 0.005180700 °C, 0.001700533% on the kelvin scale and
0.157660518% relative to the temperature excursion. These satisfy both fixed
limits.

## Attempt history

- `stage08_attempt_01`: MAPDL exited 0, but APDL character/header behavior and
  array output produced an unusable extraction; rejected.
- `stage08_attempt_02`: corrected extraction, fixed 5 s step; maximum absolute
  error 0.111278504 °C and excursion-relative error 3.374195718%; rejected.
- `stage08_attempt_03`: fixed 1 s step; maximum absolute error 0.021979832 °C
  but maximum excursion-relative error 0.666791416%; rejected.
- `stage08_attempt_04`: attempted 0.25 s step inside OneDrive; MAPDL terminated
  at 552 s with a Windows file-mapping error; no result accepted.
- `stage08_attempt_05`: unchanged 0.25 s numerical problem executed from local
  scratch, copied back after file closure, and passed both fixed limits.

This sequence is a recorded time-integration refinement for the benchmark. It
is not production time-step convergence and does not establish spatial mesh
convergence.

## Production transient thermal contract

`simulation/cases/thermal_production_template.json` defines the complete
production sequence: initial ambient, heating, approach-to-target criterion,
holding, cooling and final observation. It also requires temperature-dependent
PLA k(T), cₚ(T) and density treatment; the sourced temperature-dependent AISI
304 fixture table; convection; a radiation relevance decision; fixture initial
temperature; thermal-contact conductance for GAP; and temperature/energy
extraction rules.

`ansys/thermal_model.py` rejects deck admission while any evidence field or gate
is missing. Radiation cannot yet be dismissed because no emissivity or enclosure
history is available. Fixture heat transfer is included in the GAP contract,
but no contact conductance is invented. FREE has no plate/contact path. The
current blocked production record is therefore scientific evidence control, not
a completed coupon simulation.

## What this verifies

The accepted comparison verifies the implemented linear transient conduction,
two-face convection, ambient ramp/hold/cooling history, center-temperature
extraction and analytical postprocessing for the plane-wall case. It does not
verify Prusament thermal properties, radiation, PLA–steel contact, the 60 mm ×
10 mm × 4 mm coupon, fixture heat transfer, hold attainment, mesh convergence,
annealing strain, stress, warpage or physical predictive validity.
