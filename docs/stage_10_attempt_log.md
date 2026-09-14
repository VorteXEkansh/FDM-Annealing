# Stage 10 attempt and disposition log

All 43 run directories under `simulation/convergence/` are preserved. Twenty-eight unique run directories contribute to the published Stage 10 tables; fifteen directories are excluded or rejected from conclusions.

## Structural measurand revisions

- `stage10_structural_mesh_coarse_a01` solved, but homogeneous free recovery left the 95th-percentile stress at approximately 1.75 × 10⁻⁸ MPa. It is rejected because percentage stress convergence is not identifiable at that numerical scale.
- `stage10_structural_mesh_coarse_a02` solved with an endpoint support, but top-edge curvature and displacement were at numerical-noise scale. It is rejected as a joint-measurand design.
- Revision 3 introduced the declared two-layer relaxation-time mismatch and free post-unload recovery. `stage10_structural_mesh_coarse_a03` and all subsequent structural refinement cases use that configuration.
- Revision 4 added `stage10_structural_mesh_ultra_fine_a01` after the fine-to-extra-fine W_max comparison missed the 2% limit.

## Contact input and control revisions

The following twelve attempt-01 surface-contact directories are rejected because the shared real-constant set placed the requested FKN value in target-geometry slot R1 while MAPDL used default FKN = 1:

`stage10_contact_augmented_fkn_0p1_a01`, `stage10_contact_augmented_fkn_10_a01`, `stage10_contact_augmented_mu_0p1_a01`, `stage10_contact_augmented_mu_0p3_a01`, `stage10_contact_mesh_coarse_a01`, `stage10_contact_mesh_medium_a01`, `stage10_contact_mesh_fine_a01`, `stage10_contact_mesh_extra_fine_a01`, `stage10_contact_normal_lagrange_a01`, `stage10_contact_penalty_fkn_0p1_a01`, `stage10_contact_penalty_fkn_1_a01`, and `stage10_contact_penalty_fkn_10_a01`.

`stage10_contact_penalty_fkn_0p1_a02` uses the corrected real-constant slot, but KEYOPT(10) = 2 updated stiffness each equilibrium iteration and erased the intended final FKN sensitivity. It is rejected from conclusions.

Revision 7 fixes KEYOPT(10) = 1. All accepted contact-control comparisons use attempt 03, corrected FKN slot 3, and solver-summary verification. The accepted normal-Lagrange mesh sequence uses revision 6 and attempt 03.

Technical solver completion alone does not make a run scientifically admissible. Every excluded directory retains its input, solver output, extracted data, result record, script snapshot, and manifest hashes.
