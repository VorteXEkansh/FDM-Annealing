# Stage 8 quality record

Stage 8 executes and analytically verifies a transient-thermal plane-wall model.
It does not claim a Prusament PLA coupon result. The production thermal contract
remains blocked where the property and boundary evidence is incomplete.

The accepted MAPDL run is `simulation/verification/stage08_attempt_05`. The
authoritative comparison is `verification/thermal_verification.csv`; raw input,
solver output, binary result, extracted values and code hashes are preserved.
Earlier failed attempts remain traceable.

The accepted maximum absolute center-temperature error is 0.005180700 °C. The
maximum conventional relative error is 0.001700533% on the absolute kelvin
scale, and the maximum error normalized by temperature excursion is 0.157660518%.
The predeclared limits were 0.05 °C and 0.25% excursion-relative error.

The comparison verifies only the declared constant-property, convection-only,
one-dimensional reference problem. No production mesh convergence, radiation,
thermal contact, fixture heat-transfer prediction, physical validation, stress,
warpage, dimensional response, sensitivity, uncertainty or optimization result
is supplied.
