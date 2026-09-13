# ANSYS automation boundary

This directory contains fail-closed automation for Ansys 2026 R1. `run_case.py`
accepts an explicit JSON case, validates units and evidence gates, records hashes,
and can invoke MAPDL only when every production admission gate is true. The only
admitted Stage 6 execution is the zero-analysis environment smoke case.

No `.rst`, `.wbpj`, mesh, geometry, or production material card is supplied at
this stage. Installed Workbench/Mechanical templates are evidence of software
presence, not proof that every system can obtain a license.

