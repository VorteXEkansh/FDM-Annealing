# ANSYS automation boundary

This directory contains fail-closed automation for Ansys 2026 R1. `run_case.py`
accepts an explicit JSON case, validates units and evidence gates, records hashes,
and can invoke MAPDL only when every production admission gate is true. The only
admitted Stage 6 execution is the zero-analysis environment smoke case.

Stage 8 executes one MAPDL transient-thermal plane-wall benchmark with SOLID70
elements and convection on two opposed faces. The benchmark is a code
verification problem, not a PLA coupon prediction. `thermal_model.py` defines
and enforces the still-blocked production thermal data contract.

Installed Workbench/Mechanical templates remain evidence of software presence,
not proof that every GUI system can obtain a license.
