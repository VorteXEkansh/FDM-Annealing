# Stage 10 quality record

- Scope: formal mesh, time-step, and contact-control convergence for genuine MAPDL verification configurations.
- Solver: ANSYS Mechanical APDL Student 2026 R1, build 26.1, update 20260202; one process and one core per sequential run.
- Raw runs: 43 preserved directories, including technically completed but scientifically rejected designs.
- Published evidence: 39 mesh rows, 24 time-step rows, and 9 contact-sensitivity rows, each linked to a raw run.
- Numerical checks: all selected raw-file hashes, MAPDL version strings, return codes, error counts, contact algorithm summaries, and requested FKN factors are rechecked by `scripts/check_convergence_stage.py`.
- Unit checks: 6 Stage 10 tests pass.
- Regression checks: 73 repository unit tests pass; the literature, material, constitutive, software-environment, geometry, thermal and structural stage checkers also pass.
- Integrated integrity: 77 manuscript, evidence, provenance and reproducibility checks pass.
- Figures: three 300 dpi plots generated directly from the published CSV tables and visually inspected.
- Evidence boundary: selected settings apply only to the declared verification problems. No production mesh or production sweep is admitted.
- Manuscript: complete draft updated in place; no experimental-looking production Results added.
- PDF review: all 38 pages were inspected from fresh 100 dpi Poppler renders; convergence pages 26–28 were also inspected individually. The reviewed PDF SHA-256 is `c66d29e46a432b11c5ffb19eed5ffbd407ac73621d320c39281cd4bf2bec6eca`.
