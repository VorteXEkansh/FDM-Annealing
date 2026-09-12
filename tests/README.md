# Constitutive unit tests

Run `python scripts/check_constitutive.py` from the repository root. The standard-library unittest suite in `test_constitutive.py` checks source-based material relations against analytical or synthetic cases. It does not execute ANSYS or create validation data. Strains, durations, quadrature panels and any toy moduli in tests are explicit numerical fixtures and never enter the property database.

Individual outcomes and input/code hashes are recorded in `docs/stage_05_constitutive_tests.json`. If a test run fails, its report is additionally preserved under `tests/failure_records/` using a content-hash filename.
