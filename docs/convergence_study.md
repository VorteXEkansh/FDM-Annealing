# Stage 10 numerical convergence and discretization study

## Evidence boundary

This stage contains genuine ANSYS Mechanical APDL 2026 R1 solutions and reproducible calculations from their archived nodal and element outputs. The values qualify three declared verification configurations. They are not predictions for a Prusament annealing coupon, a validated fixture, or a production process. Compatible Prusament thermal functions, a bulk irreversible annealing-strain law, the non-isothermal constitutive adapter, three-dimensional surface contact, friction, and thermal-contact inputs remain unresolved.

Accordingly, this stage selects discretizations for the verification configurations only. It does not select a production mesh and does not admit a production sweep. That restriction follows from missing model inputs rather than from failed numerical execution.

## Predeclared comparison

For a response q, adjacent levels use

δ_q = |q_fine − q_medium| / |q_fine| × 100%.

The same form is used for extra-fine versus fine and for the supplemental structural level. A percentage is not reported when the selected denominator is zero; if both values are zero, the absolute change is zero. Before execution, the limits were fixed at 2% for global mesh responses, 5% for a local stress percentile or peak contact pressure, 1% for global time-step responses, and 3% for local time-step stress. The immutable design is `simulation/cases/stage10_convergence_design.json`.

## Verification configurations

The structural model is a 60 mm × 4 mm plane-stress cantilever of unit thickness at 65 °C. Both layers use the source-backed Prusament instantaneous modulus, ν = 0.35, and the 23 normalized shear and bulk Prony amplitudes. The upper layer uses every source relaxation time multiplied by 10 as a declared synthetic mismatch fixture; the lower layer uses the source times. A total end force ramps from zero to −0.001 N over 1 s, is held through 31 s, returns to zero by 32 s, and remains zero to 62 s. The factor of 10 and the load are not material measurements or uncertainty bounds. At 62 s, W_max is the maximum signed-normal residual from a least-squares line fitted to the deformed top edge. Residual displacement is the largest top-edge displacement magnitude. Residual stress is the 95th percentile of element-centroid von Mises stress in 6 mm ≤ x ≤ 54 mm, excluding the clamped-edge neighborhood.

The thermal model reuses the analytically verified Stage 8 plane wall and numerical fixtures: k = 0.5 W m⁻¹ K⁻¹, c_p = 1000 J kg⁻¹ K⁻¹, ρ = 1000 kg m⁻³, h = 5 W m⁻² K⁻¹, and a 10 mm wall. Both faces follow the 20–80–20 °C ramp–hold–cool ambient history through 1800 s. Thermal lag is 80 °C minus the center temperature at 300 s. The reported gradient is the absolute center-to-mean-surface difference divided by 5 mm. Profiles are archived at 300 s, 900 s, 1200 s, and 1800 s.

The contact model is a 10 mm × 4 mm plane-strain block under a rigid line target with a 0.020 mm initial gap. E = 2000 MPa, ν = 0.3, α = 10⁻⁴ K⁻¹, and the uniform 20–120 °C load are numerical fixtures. They are chosen to close contact and do not represent PLA annealing data. Normal reaction is per unit out-of-plane depth. Pressure and penetration come from CONTA172 element output. Positive pressure at every contact element is the closure check; averaged status values at the boundary element are retained but are not rounded into a false discrete state.

## Mesh convergence

The structural sequence used 15 × 2, 30 × 4, 60 × 8, and 90 × 12 elements. Medium-to-fine changes were 9.9345% for W_max, 7.9763% for residual displacement, and 29.8796% for the residual-stress percentile, so the original fine grid failed. Fine-to-extra-fine W_max still changed by 2.3059%, marginally above its 2% limit. A recorded 120 × 16 supplemental grid then changed W_max by 0.9327%, displacement by 0.5821%, and stress by 2.0266% relative to 90 × 12. The 90 × 12 grid is therefore selected for this structural verification configuration, confirmed by the 120 × 16 solve.

The thermal sequence used 8, 16, 32, and 64 elements through thickness with Δt = 0.25 s. From 32 to 64 elements, the 300 s thermal lag changed by 0.0009423% and the temperature gradient by 0.0060073%. The 32-element grid is selected for the thermal verification configuration and confirmed by 64 elements.

The first augmented-Lagrange contact mesh sequence failed because its automatically scaled penalty response remained mesh-dependent. After contact-control diagnosis, normal Lagrange enforcement was used on 10, 20, 40, and 60 interface elements over 10 × 4, 20 × 8, 40 × 16, and 60 × 24 solid grids. From 40 to 60 contact elements, mean pressure changed by 0.12698%, peak pressure by 0.36127%, and normal reaction by 0.13831%; reported penetration remained 0 mm. The 40-element interface on the 40 × 16 solid grid is selected for this contact verification configuration and confirmed by 60 elements.

The complete results, including every earlier non-passing pair, are in `convergence/mesh_convergence.csv`.

## Time-step convergence

The thermal strategies used fixed increments of 5 s, 1 s, 0.25 s, and 0.125 s on the 64-element wall. Relative to 0.125 s, the 0.25 s result differs by 0.005285% in thermal lag, 0.005369% in the 300 s gradient, and 0.002811% in the L2 profile-excursion measure. The pointwise profile RMSE across all four stored times is 0.00202088 °C. A fixed 0.25 s increment is selected for this thermal verification history.

The structural strategies used ramp/hold pairs of 0.1/1 s, 0.05/0.5 s, 0.01/0.1 s, and 0.005/0.05 s on the 60 × 8 grid. Relative to the smallest increments, the 0.01/0.1 s strategy differs by 0.003094% in W_max, 0.003213% in residual displacement, and 0.13636% in the residual-stress percentile. The 0.01/0.1 s pair is selected for this structural verification history.

The complete time-step values and adjacent comparisons are in `convergence/timestep_convergence.csv`.

## Contact-control and friction sensitivity

An input audit rejected the first surface-contact attempts because FKN had been placed in the target-geometry real-constant slot. A corrected attempt then showed that updating stiffness each equilibrium iteration erased the intended FKN comparison. The accepted design places FKN in real-constant slot 3 and holds its initial stiffness through the load step. The MAPDL contact summaries are checked against each requested algorithm and factor.

For frictionless penalty and augmented-Lagrange runs, increasing FKN from 0.1 to 1 to 10 reduced maximum penetration from 1.12141 × 10⁻³ mm to 1.52677 × 10⁻⁴ mm and 1.80923 × 10⁻⁵ mm. Mean pressure changed from 16.9989 MPa to 17.5368 MPa and 17.6242 MPa. At FKN = 10, one edge element had zero pressure, so that case fails the all-elements-closed requirement even though MAPDL converged. The simple monotonic frictionless benchmark gives numerically identical final penalty and augmented-Lagrange values at each factor; this does not establish general equivalence of the algorithms.

Normal Lagrange produced zero reported penetration, a mean pressure of 17.5721 MPa, and a peak of 21.3788 MPa, and its mesh sequence passed. It is selected only for this contact verification configuration.

At augmented Lagrange FKN = 1, changing μ from 0 to 0.1 and 0.3 increased mean pressure from 17.5368 MPa to 18.4343 MPa and 20.0334 MPa; peak pressure increased from 24.4284 MPa to 31.5883 MPa and 51.8788 MPa. Converged-message counts increased from 31 to 43 and 133. Friction is therefore a material physical-model sensitivity in this fixture, not a numerical nuisance that can be ignored. No production μ is selected because the PLA–steel interface lacks evidence.

The full matrix, solver warnings, convergence counts, closure checks, and raw-run paths are in `convergence/contact_sensitivity.csv`.

## Numerical decision

All final verification refinement pairs satisfy the predeclared limits. The selected verification settings are 90 × 12 structural elements, 32 thermal elements through thickness, 40 normal-Lagrange contact elements over a 40 × 16 solid grid, Δt = 0.25 s for the thermal history, and 0.01/0.1 s for structural ramps/holds. These choices are local to the exact verification problems.

No three-dimensional production mesh or time-step strategy is selected. The real coupon/fixture assembly changes topology, surface-contact dimensionality, thermal properties, contact conductance, friction, irreversible strain evolution, and release behavior. Those inputs and the resulting production fields must exist before their own convergence criteria can be passed. Production sweeps remain blocked.
