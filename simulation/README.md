# Simulation records

`cases/` holds explicit parameter records. `runs/<case_id>/` holds solver logs
and a hash manifest. Case inputs never receive silent defaults for temperature,
hold time, fixture gap, or material identity. Failed runs remain in place.

The full thermo-mechanical production template remains non-executable. Stage 8
adds a separate transient-thermal production contract with explicit initial,
heating, approach, holding, cooling and final-observation phases. Missing
same-grade PLA heat-transfer functions and boundary/contact evidence keep its
admission gates closed.

`verification/stage08_attempt_01` through `stage08_attempt_05` preserve the
thermal benchmark history, including failed extraction, accuracy and I/O
attempts. Attempt 05 is the accepted plane-wall verification run. Its declared
constants are numerical fixtures and are not PLA material data.
