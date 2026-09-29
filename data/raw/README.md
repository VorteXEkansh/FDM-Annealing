# Immutable production solver exports

No production solver export exists at Stage 14. The approved design matrix is empty and the validation/dry-run prerequisites remain unmet. This file defines a storage boundary; it is not raw numerical evidence.

Future admitted runs must use a new case/attempt directory and preserve exact solver inputs, command, version, logs, result binaries, exported histories and an input/output SHA-256 manifest. Existing attempts must never be overwritten. Derived metrics belong under `data/processed/`; failed attempts remain traceable. The prior numerical verification evidence stays at its original hashed paths under `simulation/verification/` and `simulation/convergence/` and is not relabeled as production data.
