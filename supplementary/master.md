# Supplementary information for constrained annealing verification

Numerical verification and feasibility supplement · 1 November 2026

This supplement documents genuine reference calculations and published material data. No production simulation, independent validation prediction, sensitivity index, uncertainty interval, Pareto solution or optimization confirmation exists. Missing results are not zero responses. Tables S1–S12 retain the earlier reference evidence. Their numeric citations use the legacy reference key in Section M4 below, not the shorter main article bibliography. Sections M1–M3 document the new investigation. Statements about production incompleteness remain applicable; non-isothermal reference verification has now been added.


### S1. Literature comparison and reproducibility tables

Literature values below are source evidence, not new experiments or solver findings. Full matrices, formulation flags and exact locators remain in the repository. Reference identities were checked against the bibliography. The focused September 2026 audit adds an ABS clearance precedent [41] without treating it as PLA material evidence.

SUPPTABLE: Closest competing studies and implications for scope
Study | Established overlap | Distinction still requiring evidence
Bute et al. [5] | Irreversible strain and ANSYS printing stress | Predictive annealing-clearance/contact relation
Chapuis et al. [8] | Viscoelastic pre-strain recovery FE | Fixture-controlled dimensional preservation
Issabayeva and Shishkovsky [9] | ANSYS, DMA, Prony and thermal response | Released fixture geometry and stress
Wijnen et al. [6] | Warpage model and annealing dimensions | Quantified annealing restraint
Trofimov et al. [7] | Thermal/deformation prediction and comparison | Post-print annealing contact cycle
Lluch-Cerezo et al. [11] | Powder-supported dimensional control | Explicit clearance and contact mechanics
Wijnbergen et al. [12] | Tough-PLA annealing media | Compatible grade and plate-gap prediction
Chiscop et al. [24] | Encapsulation across geometries | Contact-clearance response under release
De Assis et al. [13] | Geometry/mechanics and thermal conditioning | Transient fixture-contact model
Ben Amor and Souissi [14] | Annealed PLA, FE and optimization | Released dimensions–warpage–stress decision

SUPPTABLE: Prusament PLA generalized-Maxwell coefficients at T<sub>g</sub> = 65 °C from Chapuis et al. [8, supplementary Table B.2]
i | k<sub>i</sub> (MPa) | τ<sub>i</sub> (s)
1 | 6.228 | 1.176 × 10<sup>−14</sup>
2 | 1.806 | 1.228 × 10<sup>−14</sup>
3 | 7.849 | 2.878 × 10<sup>−14</sup>
4 | 12.751 | 1.701 × 10<sup>−12</sup>
5 | 20.857 | 9.178 × 10<sup>−12</sup>
6 | 31.104 | 6.034 × 10<sup>−11</sup>
7 | 45.566 | 6.187 × 10<sup>−9</sup>
8 | 64.036 | 1.102 × 10<sup>−7</sup>
9 | 92.484 | 1.047 × 10<sup>−6</sup>
10 | 135.916 | 6.903 × 10<sup>−6</sup>
11 | 113.488 | 2.582 × 10<sup>−5</sup>
12 | 128.266 | 5.363 × 10<sup>−5</sup>
13 | 173.470 | 1.838 × 10<sup>−4</sup>
14 | 93.393 | 4.386 × 10<sup>−4</sup>
15 | 163.804 | 7.577 × 10<sup>−4</sup>
16 | 134.311 | 1.795 × 10<sup>−3</sup>
17 | 119.266 | 2.292 × 10<sup>−3</sup>
18 | 100.596 | 6.576 × 10<sup>−3</sup>
19 | 80.534 | 9.920 × 10<sup>−3</sup>
20 | 61.624 | 3.290 × 10<sup>−2</sup>
21 | 44.508 | 5.374 × 10<sup>−2</sup>
22 | 30.529 | 6.586 × 10<sup>−2</sup>
23 | 18.610 | 3.503 × 10<sup>1</sup>

SUPPTABLE: Candidate AISI 304 fixture properties from Meng et al. [38, Table 1]
Property | 20 °C | 100 °C / 200 °C
ρ | 7910 kg m⁻³ | 7876 / 7840 kg m⁻³
c<sub>p</sub> | 456 J kg⁻¹ K⁻¹ | 494 / 532 J kg⁻¹ K⁻¹
k | 16.2 W m⁻¹ K⁻¹ | 16.6 / 17.45 W m⁻¹ K⁻¹
α | 15.5 µm m⁻¹ K⁻¹ | 16.3 / 16.7 µm m⁻¹ K⁻¹
E | 200 GPa | 191.4 / 183.5 GPa
ν | 0.290 | 0.285 / 0.289

SUPPTABLE: Reserved experimental dimensional means from Lluch-Cerezo et al. [11, Table 5], without mould
T (°C) | Length change (%) | Width change (%) | Height change (%)
63 | −0.13 | −0.06 | 0.00
75 | −1.60 | −0.11 | 2.74
86 | −2.30 | −0.16 | 2.62
98 | −2.88 | 0.15 | 2.60
109 | −3.05 | 0.30 | 3.94
132 | −3.58 | 0.18 | 3.69

SUPPTABLE: Genuine ANSYS–analytical center-temperature comparison for the plane-wall verification
Time (s) | ANSYS / analytical (°C) | Absolute / excursion-relative error
150 | 21.892109254 / 21.889130841 | 0.002978413 °C / 0.157660518%
300 | 27.631062216 / 27.625947421 | 0.005114795 °C / 0.067070946%
450 | 34.805348857 / 34.801718199 | 0.003630658 °C / 0.024528625%
600 | 41.003870402 / 41.001387994 | 0.002482407 °C / 0.011820207%
900 | 50.967098637 / 50.966218772 | 0.000879865 °C / 0.002841371%
1050 | 53.056900023 / 53.059537028 | 0.002637005 °C / 0.007976533%
1200 | 50.753732030 / 50.758912731 | 0.005180700 °C / 0.016842924%
1500 | 42.903452036 / 42.906520281 | 0.003068244 °C / 0.013394633%
1800 | 37.051786082 / 37.053501761 | 0.001715679 °C / 0.010060566%

SUPPTABLE: Isothermal Prony finite-ramp stress verification at 65 °C
Time (s) | ANSYS stress (MPa) | Analytical stress (MPa) | Absolute error (MPa)
1 | 0.0375536568 | 0.0375574835 | 0.0000038266
11 | 0.0243886374 | 0.0243886379 | 0.0000000005
31 | 0.0183896348 | 0.0183896352 | 0.0000000005
32 | −0.0193833038 | −0.0193871309 | 0.0000038271
62 | −0.0045757745 | −0.0045757747 | 0.0000000001

SUPPTABLE: Contact-control sensitivity on the 40-element interface
Control | Maximum penetration (mm) | Mean / peak pressure (MPa)
Penalty or augmented, F<sub>KN</sub> = 0.1 | 1.12141 × 10<super>−3</super> | 16.9989 / 17.9426
Penalty or augmented, F<sub>KN</sub> = 1 | 1.52677 × 10<super>−4</super> | 17.5368 / 24.4284
Penalty or augmented, F<sub>KN</sub> = 10 | 1.80923 × 10<super>−5</super> | 17.6242 / 28.9476
Normal Lagrange, μ = 0 | 0 | 17.5721 / 21.3788
Augmented, F<sub>KN</sub> = 1, μ = 0.1 | 1.97427 × 10<super>−4</super> | 18.4343 / 31.5883
Augmented, F<sub>KN</sub> = 1, μ = 0.3 | 3.24243 × 10<super>−4</super> | 20.0334 / 51.8788

### S2. Evidence and reproduction boundaries

The original literature matrix contains 34 journal studies; the separate audit addendum records the additional ABS clearance study [41]. The base paper is immutable. Property records preserve units, temperatures, formulation, exact source location and use restrictions. Full convergence CSVs contain 39 mesh, 24 time-step and nine contact-control rows; these are response records, not independent experiments. All 43 technical convergence directories remain archived, including 15 excluded attempts.

Verification constants, load schedules, relaxation mismatch and clearance screens are design choices. The assembly construction is not a solved annealing model. The validation archive retains 45 published observations: 18 reserved means, 24 context records and three quarantined maxima. Prediction/error fields remain blank. Empty registries do not mean zero physical response.

Each run preserves input, script, command, raw output and extraction hashes. Corrections create new derived records or attempts; raw evidence is not overwritten. The supplementary files support numerical reproduction and do not supply missing physical validation.

### S3. Full scalar verification and refinement records

The following tables reproduce every accepted scalar comparison and each audited mesh/time response record. Raw nodal and element exports, complete input decks, warnings and rejected attempts remain in the repository at the paths indexed by result_traceability.csv. Units follow each quantity; reaction is force in the structural verification and force per unit depth in plane-strain contact convergence. Percent errors at a zero reference are undefined, not zero.

SUPPTABLE: All structural reference comparisons
Case | t (s) | Quantity | ANSYS | Reference | Absolute error
free | 1 | ux (mm) | 0.001 | 0.001 | 2.998903 × 10<sup>−16</sup>
free | 1 | uy (mm) | 0.0001 | 0.0001 | 2.999174 × 10<sup>−17</sup>
free | 1 | uz (mm) | 0.0001 | 0.0001 | 2.999174 × 10<sup>−17</sup>
free | 1 | stress x (MPa) | 1.15001 × 10<sup>−15</sup> | 0 | 1.15001 × 10<sup>−15</sup>
free | 1 | reaction x (N) | -1.15001 × 10<sup>−15</sup> | 0 | 1.15001 × 10<sup>−15</sup>
free | 2 | ux (mm) | 0.006 | 0.006 | 8.396062 × 10<sup>−16</sup>
free | 2 | uy (mm) | 0.0006 | 0.0006 | 7.892992 × 10<sup>−17</sup>
free | 2 | uz (mm) | 0.0006 | 0.0006 | 7.795414 × 10<sup>−17</sup>
free | 2 | stress x (MPa) | 6.911789 × 10<sup>−15</sup> | 0 | 6.911789 × 10<sup>−15</sup>
free | 2 | reaction x (N) | -6.911789 × 10<sup>−15</sup> | 0 | 6.911789 × 10<sup>−15</sup>
free | 3 | ux (mm) | 0 | 0 | 0
free | 3 | uy (mm) | 0 | 0 | 0
free | 3 | uz (mm) | 0 | 0 | 0
free | 3 | stress x (MPa) | 0 | 0 | 0
free | 3 | reaction x (N) | 0 | 0 | 0
fixed | 1 | ux (mm) | 0 | 0 | 0
fixed | 1 | uy (mm) | 0.00013 | 0.00013 | 3.897707 × 10<sup>−17</sup>
fixed | 1 | uz (mm) | 0.00013 | 0.00013 | 3.897707 × 10<sup>−17</sup>
fixed | 1 | stress x (MPa) | −0.2 | −0.2 | 2.980232 × 10<sup>−9</sup>
fixed | 1 | reaction x (N) | 0.2 | 0.2 | 5.99798 × 10<sup>−14</sup>
fixed | 2 | ux (mm) | 0 | 0 | 0
fixed | 2 | uy (mm) | 0.00078 | 0.00078 | 1.049508 × 10<sup>−16</sup>
fixed | 2 | uz (mm) | 0.00078 | 0.00078 | 1.038666 × 10<sup>−16</sup>
fixed | 2 | stress x (MPa) | −1.2 | −1.2 | 4.768372 × 10<sup>−8</sup>
fixed | 2 | reaction x (N) | 1.2 | 1.2 | 1.598721 × 10<sup>−13</sup>
fixed | 3 | ux (mm) | 0 | 0 | 0
fixed | 3 | uy (mm) | 0 | 0 | 0
fixed | 3 | uz (mm) | 0 | 0 | 0
fixed | 3 | stress x (MPa) | 0 | 0 | 0
fixed | 3 | reaction x (N) | 0 | 0 | 0
eigen free | 1 | ux (mm) | −0.009 | −0.009 | 2.688821 × 10<sup>−16</sup>
eigen free | 1 | uy (mm) | −0.0009 | −0.0009 | 3.198396 × 10<sup>−17</sup>
eigen free | 1 | uz (mm) | −0.0009 | −0.0009 | 2.992398 × 10<sup>−17</sup>
eigen free | 1 | stress x (MPa) | -7.882584 × 10<sup>−15</sup> | 0 | 7.882584 × 10<sup>−15</sup>
eigen free | 1 | reaction x (N) | 7.882583 × 10<sup>−15</sup> | 0 | 7.882583 × 10<sup>−15</sup>
eigen free | 2 | ux (mm) | −0.004 | −0.004 | 7.901665 × 10<sup>−16</sup>
eigen free | 2 | uy (mm) | −0.0004 | −0.0004 | 7.995991 × 10<sup>−17</sup>
eigen free | 2 | uz (mm) | −0.0004 | −0.0004 | 7.697835 × 10<sup>−17</sup>
eigen free | 2 | stress x (MPa) | -3.108625 × 10<sup>−15</sup> | -1.084202 × 10<sup>−16</sup> | 3.000204 × 10<sup>−15</sup>
eigen free | 2 | reaction x (N) | 3.108624 × 10<sup>−15</sup> | 1.084202 × 10<sup>−16</sup> | 3.000204 × 10<sup>−15</sup>
eigen free | 3 | ux (mm) | −0.01 | −0.01 | 1.00614 × 10<sup>−16</sup>
eigen free | 3 | uy (mm) | −0.001 | −0.001 | 1.951564 × 10<sup>−18</sup>
eigen free | 3 | uz (mm) | −0.001 | −0.001 | 0
eigen free | 3 | stress x (MPa) | -1.032507 × 10<sup>−14</sup> | 0 | 1.032507 × 10<sup>−14</sup>
eigen free | 3 | reaction x (N) | 1.032507 × 10<sup>−14</sup> | 0 | 1.032507 × 10<sup>−14</sup>
eigen fixed | 1 | ux (mm) | 0 | 0 | 0
eigen fixed | 1 | uy (mm) | −0.00117 | −0.00117 | 4.011548 × 10<sup>−17</sup>
eigen fixed | 1 | uz (mm) | −0.00117 | −0.00117 | 4.011548 × 10<sup>−17</sup>
eigen fixed | 1 | stress x (MPa) | 1.8 | 1.8 | 4.768372 × 10<sup>−8</sup>
eigen fixed | 1 | reaction x (N) | −1.8 | −1.8 | 5.995204 × 10<sup>−14</sup>
eigen fixed | 2 | ux (mm) | 0 | 0 | 0
eigen fixed | 2 | uy (mm) | −0.00052 | −0.00052 | 1.03975 × 10<sup>−16</sup>
eigen fixed | 2 | uz (mm) | −0.00052 | −0.00052 | 9.996344 × 10<sup>−17</sup>
eigen fixed | 2 | stress x (MPa) | 0.8 | 0.8 | 1.192093 × 10<sup>−8</sup>
eigen fixed | 2 | reaction x (N) | −0.8 | −0.8 | 1.609823 × 10<sup>−13</sup>
eigen fixed | 3 | ux (mm) | 0 | 0 | 0
eigen fixed | 3 | uy (mm) | −0.0013 | −0.0013 | 0
eigen fixed | 3 | uz (mm) | −0.0013 | −0.0013 | 0
eigen fixed | 3 | stress x (MPa) | 2 | 2 | 0
eigen fixed | 3 | reaction x (N) | −2 | −2 | 0
eigen fixed | 4 | ux (mm) | −0.01 | −0.01 | 1.00614 × 10<sup>−16</sup>
eigen fixed | 4 | uy (mm) | −0.001 | −0.001 | 1.951564 × 10<sup>−18</sup>
eigen fixed | 4 | uz (mm) | −0.001 | −0.001 | 0
eigen fixed | 4 | stress x (MPa) | -1.032507 × 10<sup>−14</sup> | 0 | 1.032507 × 10<sup>−14</sup>
eigen fixed | 4 | reaction x (N) | 1.032507 × 10<sup>−14</sup> | 0 | 1.032507 × 10<sup>−14</sup>
visco | 1 | ux (mm) | 0.01 | 0.01 | 9.020562 × 10<sup>−17</sup>
visco | 1 | uy (mm) | −0.00035 | −0.00035 | 4.011548 × 10<sup>−18</sup>
visco | 1 | uz (mm) | −0.00035 | −0.00035 | 4.011548 × 10<sup>−18</sup>
visco | 1 | stress x (MPa) | 0.03755366 | 0.03755748 | 3.826628 × 10<sup>−6</sup>
visco | 1 | reaction x (N) | −0.03755366 | −0.03755748 | 3.827983 × 10<sup>−6</sup>
visco | 11 | ux (mm) | 0.01 | 0.01 | 6.071532 × 10<sup>−17</sup>
visco | 11 | uy (mm) | −0.00035 | −0.00035 | 2.005774 × 10<sup>−18</sup>
visco | 11 | uz (mm) | −0.00035 | −0.00035 | 2.005774 × 10<sup>−18</sup>
visco | 11 | stress x (MPa) | 0.02438864 | 0.02438864 | 4.999321 × 10<sup>−10</sup>
visco | 11 | reaction x (N) | −0.02438864 | −0.02438864 | 4.555384 × 10<sup>−15</sup>
visco | 31 | ux (mm) | 0.01 | 0.01 | 0
visco | 31 | uy (mm) | −0.00035 | −0.00035 | 0
visco | 31 | uz (mm) | −0.00035 | −0.00035 | 9.75782 × 10<sup>−19</sup>
visco | 31 | stress x (MPa) | 0.01838963 | 0.01838964 | 4.545142 × 10<sup>−10</sup>
visco | 31 | reaction x (N) | −0.01838964 | −0.01838964 | 2.428613 × 10<sup>−15</sup>
visco | 32 | ux (mm) | 2.330601 × 10<sup>−14</sup> | 0 | 2.330601 × 10<sup>−14</sup>
visco | 32 | uy (mm) | -8.15734 × 10<sup>−16</sup> | 0 | 8.15734 × 10<sup>−16</sup>
visco | 32 | uz (mm) | -8.150692 × 10<sup>−16</sup> | 0 | 8.150692 × 10<sup>−16</sup>
visco | 32 | stress x (MPa) | −0.0193833 | −0.01938713 | 3.82709 × 10<sup>−6</sup>
visco | 32 | reaction x (N) | 0.0193833 | 0.01938713 | 3.827983 × 10<sup>−6</sup>
visco | 62 | ux (mm) | 0 | 0 | 0
visco | 62 | uy (mm) | -3.187388 × 10<sup>−19</sup> | 0 | 3.187388 × 10<sup>−19</sup>
visco | 62 | uz (mm) | 6.912625 × 10<sup>−19</sup> | 0 | 6.912625 × 10<sup>−19</sup>
visco | 62 | stress x (MPa) | −0.004575775 | −0.004575775 | 1.14099 × 10<sup>−10</sup>
visco | 62 | reaction x (N) | 0.004575775 | 0.004575775 | 1.56819 × 10<sup>−15</sup>

SUPPTABLE: All gap-contact reference comparisons
Case | t (s) | Quantity | ANSYS | Reference | Absolute error
contact | 1 | ux (mm) | 0.001 | 0.001 | 2.998903 × 10<sup>−16</sup>
contact | 1 | uy (mm) | 0.0001 | 0.0001 | 2.999174 × 10<sup>−17</sup>
contact | 1 | uz (mm) | 0.0001 | 0.0001 | 2.999174 × 10<sup>−17</sup>
contact | 1 | stress x (MPa) | -2.801724 × 10<sup>−17</sup> | 0 | 2.801724 × 10<sup>−17</sup>
contact | 1 | reaction x (N) | 2.801724 × 10<sup>−17</sup> | 0 | 2.801724 × 10<sup>−17</sup>
contact | 1 | C force (N) | 0 | 0 | 0
contact | 1 | C closed | 0 | 0 | 0
contact | 1 | gap (mm) | 0.001 | 0.001 | 4.749745 × 10<sup>−11</sup>
contact | 2 | ux (mm) | 0.002 | 0.002 | 6.700369 × 10<sup>−16</sup>
contact | 2 | uy (mm) | 0.00072 | 0.00072 | 8.391725 × 10<sup>−17</sup>
contact | 2 | uz (mm) | 0.00072 | 0.00072 | 8.391725 × 10<sup>−17</sup>
contact | 2 | stress x (MPa) | −0.8 | −0.8 | 1.192093 × 10<sup>−8</sup>
contact | 2 | reaction x (N) | 0.8 | 0.8 | 2.68674 × 10<sup>−14</sup>
contact | 2 | C force (N) | −0.8 | −0.8 | 1.192093 × 10<sup>−8</sup>
contact | 2 | C closed | 1 | 1 | 0
contact | 2 | gap (mm) | 0 | 0 | 0
contact | 3 | ux (mm) | 2.001532 × 10<sup>−16</sup> | 0 | 2.001532 × 10<sup>−16</sup>
contact | 3 | uy (mm) | 2.001784 × 10<sup>−17</sup> | 0 | 2.001784 × 10<sup>−17</sup>
contact | 3 | uz (mm) | 2.001356 × 10<sup>−17</sup> | 0 | 2.001356 × 10<sup>−17</sup>
contact | 3 | stress x (MPa) | 8.932265 × 10<sup>−18</sup> | 0 | 8.932265 × 10<sup>−18</sup>
contact | 3 | reaction x (N) | -8.932262 × 10<sup>−18</sup> | 0 | 8.932262 × 10<sup>−18</sup>
contact | 3 | C force (N) | 0 | 0 | 0
contact | 3 | C closed | 0 | 0 | 0
contact | 3 | gap (mm) | 0.002 | 0.002 | 9.49949 × 10<sup>−11</sup>

SUPPTABLE: All audited mesh and time refinement responses
Study | Case / level | Quantity | Value | Unit | Change (%)
Mesh | S mesh coarse a03 | W<sub>max</sub> | 0.008170221 | mm |
Mesh | S mesh coarse a03 | resid. disp. | 0.05963922 | mm |
Mesh | S mesh coarse a03 | resid. stress p95 | 9.965 × 10<sup>−5</sup> | MPa |
Mesh | S mesh medium a01 | W<sub>max</sub> | 0.01125978 | mm | 27.43893
Mesh | S mesh medium a01 | resid. disp. | 0.07853777 | mm | 24.06301
Mesh | S mesh medium a01 | resid. stress p95 | 0.000494075 | MPa | 79.831
Mesh | S mesh fine a01 | W<sub>max</sub> | 0.01250177 | mm | 9.934494
Mesh | S mesh fine a01 | resid. disp. | 0.08534517 | mm | 7.976313
Mesh | S mesh fine a01 | resid. stress p95 | 0.0007046092 | MPa | 29.87957
Mesh | S mesh extra fine a01 | W<sub>max</sub> | 0.01279686 | mm | 2.305902
Mesh | S mesh extra fine a01 | resid. disp. | 0.08674431 | mm | 1.612952
Mesh | S mesh extra fine a01 | resid. stress p95 | 0.0007082847 | MPa | 0.5189303
Mesh | S mesh ultra fine a01 | W<sub>max</sub> | 0.01291733 | mm | 0.9326807
Mesh | S mesh ultra fine a01 | resid. disp. | 0.08725225 | mm | 0.5821426
Mesh | S mesh ultra fine a01 | resid. stress p95 | 0.0007229355 | MPa | 2.026572
Mesh | T mesh coarse a01 | T lag at 300 s | 52.37903 | °C |
Mesh | T mesh coarse a01 | temp. grad. at 300 s | 252.1411 | K m⁻¹ |
Mesh | T mesh medium a01 | T lag at 300 s | 52.37115 | °C | 0.01505384
Mesh | T mesh medium a01 | temp. grad. at 300 s | 252.384 | K m⁻¹ | 0.09626966
Mesh | T mesh fine a01 | T lag at 300 s | 52.36917 | °C | 0.003767935
Mesh | T mesh fine a01 | temp. grad. at 300 s | 252.4447 | K m⁻¹ | 0.02403675
Mesh | T mesh extra fine a01 | T lag at 300 s | 52.36868 | °C | 0.0009422631
Mesh | T mesh extra fine a01 | temp. grad. at 300 s | 252.4599 | K m⁻¹ | 0.006007273
Mesh | C mesh lagrange coarse a03 | mean C press. | 16.98722 | MPa |
Mesh | C mesh lagrange coarse a03 | max. C press. | 19.76897 | MPa |
Mesh | C mesh lagrange coarse a03 | max. penetration | 0 | mm |
Mesh | C mesh lagrange coarse a03 | normal reaction | 172.4908 | N mm⁻¹ |
Mesh | C mesh lagrange medium a03 | mean C press. | 17.44909 | MPa | 2.646943
Mesh | C mesh lagrange medium a03 | max. C press. | 20.98779 | MPa | 5.807288
Mesh | C mesh lagrange medium a03 | max. penetration | 0 | mm |
Mesh | C mesh lagrange medium a03 | normal reaction | 177.2646 | N mm⁻¹ | 2.69307
Mesh | C mesh lagrange fine a03 | mean C press. | 17.57206 | MPa | 0.6997847
Mesh | C mesh lagrange fine a03 | max. C press. | 21.37878 | MPa | 1.82884
Mesh | C mesh lagrange fine a03 | max. penetration | 0 | mm |
Mesh | C mesh lagrange fine a03 | normal reaction | 178.5694 | N mm⁻¹ | 0.7306797
Mesh | C mesh lagrange extra fine a03 | mean C press. | 17.5944 | MPa | 0.1269802
Mesh | C mesh lagrange extra fine a03 | max. C press. | 21.45629 | MPa | 0.3612721
Mesh | C mesh lagrange extra fine a03 | max. penetration | 0 | mm |
Mesh | C mesh lagrange extra fine a03 | normal reaction | 178.8167 | N mm⁻¹ | 0.1383057
Time | S time coarse a01 | W<sub>max</sub> | 0.01248075 | mm |
Time | S time coarse a01 | resid. disp. | 0.085201 | mm |
Time | S time coarse a01 | resid. stress p95 | 0.0007069894 | MPa |
Time | S time medium a01 | W<sub>max</sub> | 0.01249482 | mm | 0.1126111
Time | S time medium a01 | resid. disp. | 0.08529745 | mm | 0.1130754
Time | S time medium a01 | resid. stress p95 | 0.0007080892 | MPa | 0.155314
Time | S mesh fine a01 | W<sub>max</sub> | 0.01250177 | mm | 0.05561255
Time | S mesh fine a01 | resid. disp. | 0.08534517 | mm | 0.05591337
Time | S mesh fine a01 | resid. stress p95 | 0.0007046092 | MPa | 0.4938889
Time | S time extra fine a01 | W<sub>max</sub> | 0.01250216 | mm | 0.00309372
Time | S time extra fine a01 | resid. disp. | 0.08534791 | mm | 0.003212977
Time | S time extra fine a01 | resid. stress p95 | 0.0007036497 | MPa | 0.136358
Time | T time coarse a01 | T lag at 300 s | 52.2638 | °C |
Time | T time coarse a01 | temp. grad. at 300 s | 251.9462 | K m⁻¹ |
Time | T time coarse a01 | temp. profile L2 excursion | 23.72262 | °C |
Time | T time medium a01 | T lag at 300 s | 52.35208 | °C | 0.1686272
Time | T time medium a01 | temp. grad. at 300 s | 252.3786 | K m⁻¹ | 0.1713168
Time | T time medium a01 | temp. profile L2 excursion | 23.74377 | °C | 0.08906041
Time | T mesh extra fine a01 | T lag at 300 s | 52.36868 | °C | 0.03169506
Time | T mesh extra fine a01 | temp. grad. at 300 s | 252.4599 | K m⁻¹ | 0.03220043
Time | T mesh extra fine a01 | temp. profile L2 excursion | 23.74776 | °C | 0.01683771
Time | T time extra fine a01 | T lag at 300 s | 52.37145 | °C | 0.005284926
Time | T time extra fine a01 | temp. grad. at 300 s | 252.4734 | K m⁻¹ | 0.005369188
Time | T time extra fine a01 | temp. profile L2 excursion | 23.74843 | °C | 0.002810575

### S4. Material property inventory and use restrictions

The property registry below preserves all recorded numerical PLA values, including comparator formulations that are not admitted to the reference material card. P = Prusament PLA; all other formulations are comparator evidence. Exact print settings, confidence, full source locators, temperature context and ANSYS-use restrictions are retained in material/pla_properties.csv. A number in this inventory is not authorization to mix formulations. Tables S2–S3 provide the reference spectrum and candidate fixture data.

SUPPTABLE: Complete PLA property inventory with source and formulation
ID / source | Property / component | Value / unit | Temperature / formulation
PLA-001<br/>PrusamentTDS2022 | ρ / isotropic | 1240 kg m⁻³ | not reported<br/>Prusament PLA
PLA-002<br/>PrusamentTDS2022 | E / horizontal | 2300 MPa | not reported<br/>Prusament PLA
PLA-003<br/>PrusamentTDS2022 | E / vertical xz | 2400 MPa | not reported<br/>Prusament PLA
PLA-004<br/>Chapuis2025 | ν / isotropic | 0.35 | 23–85 °C<br/>Prusament PLA
PLA-005<br/>Chapuis2025 | α / isotropic | 68 µm m⁻¹ K⁻¹ | 23–85 °C<br/>Prusament PLA
PLA-006<br/>Chapuis2025 | T<sub>g</sub> / tan δ peak | 65 °C | 65 °C<br/>Prusament PLA
PLA-007<br/>Chapuis2025 | E<sub>∞</sub> / equilibrium Hookean element k₀ | 10.598 MPa | 65 °C<br/>Prusament PLA
PLA-008<br/>Chapuis2025 | E<sub>0</sub> / k₀ + Σkᵢ | 1691.594 MPa | 65 °C<br/>Prusament PLA
PLA-009<br/>Chapuis2025 | C₁ / above T<sub>g</sub> | 17.4 | ≥65 °C<br/>Prusament PLA
PLA-010<br/>Chapuis2025 | C₂ / above T<sub>g</sub> | 51.6 K | ≥65 °C<br/>Prusament PLA
PLA-011<br/>Chapuis2025 | C₃ / below T<sub>g</sub> | 35000 K | <65 °C<br/>Prusament PLA
PLA-012<br/>Chapuis2025 | kᵢ / branch 1 | 6.228 MPa | 65 °C<br/>Prusament PLA
PLA-013<br/>Chapuis2025 | τᵢ / branch 1 | 1.176 × 10<sup>−14</sup> s | 65 °C<br/>Prusament PLA
PLA-014<br/>Chapuis2025 | kᵢ / branch 2 | 1.806 MPa | 65 °C<br/>Prusament PLA
PLA-015<br/>Chapuis2025 | τᵢ / branch 2 | 1.228 × 10<sup>−14</sup> s | 65 °C<br/>Prusament PLA
PLA-016<br/>Chapuis2025 | kᵢ / branch 3 | 7.849 MPa | 65 °C<br/>Prusament PLA
PLA-017<br/>Chapuis2025 | τᵢ / branch 3 | 2.878 × 10<sup>−14</sup> s | 65 °C<br/>Prusament PLA
PLA-018<br/>Chapuis2025 | kᵢ / branch 4 | 12.751 MPa | 65 °C<br/>Prusament PLA
PLA-019<br/>Chapuis2025 | τᵢ / branch 4 | 1.701 × 10<sup>−12</sup> s | 65 °C<br/>Prusament PLA
PLA-020<br/>Chapuis2025 | kᵢ / branch 5 | 20.857 MPa | 65 °C<br/>Prusament PLA
PLA-021<br/>Chapuis2025 | τᵢ / branch 5 | 9.178 × 10<sup>−12</sup> s | 65 °C<br/>Prusament PLA
PLA-022<br/>Chapuis2025 | kᵢ / branch 6 | 31.104 MPa | 65 °C<br/>Prusament PLA
PLA-023<br/>Chapuis2025 | τᵢ / branch 6 | 6.034 × 10<sup>−11</sup> s | 65 °C<br/>Prusament PLA
PLA-024<br/>Chapuis2025 | kᵢ / branch 7 | 45.566 MPa | 65 °C<br/>Prusament PLA
PLA-025<br/>Chapuis2025 | τᵢ / branch 7 | 6.187 × 10<sup>−9</sup> s | 65 °C<br/>Prusament PLA
PLA-026<br/>Chapuis2025 | kᵢ / branch 8 | 64.036 MPa | 65 °C<br/>Prusament PLA
PLA-027<br/>Chapuis2025 | τᵢ / branch 8 | 1.102 × 10<sup>−7</sup> s | 65 °C<br/>Prusament PLA
PLA-028<br/>Chapuis2025 | kᵢ / branch 9 | 92.484 MPa | 65 °C<br/>Prusament PLA
PLA-029<br/>Chapuis2025 | τᵢ / branch 9 | 1.047 × 10<sup>−6</sup> s | 65 °C<br/>Prusament PLA
PLA-030<br/>Chapuis2025 | kᵢ / branch 10 | 135.916 MPa | 65 °C<br/>Prusament PLA
PLA-031<br/>Chapuis2025 | τᵢ / branch 10 | 6.903 × 10<sup>−6</sup> s | 65 °C<br/>Prusament PLA
PLA-032<br/>Chapuis2025 | kᵢ / branch 11 | 113.488 MPa | 65 °C<br/>Prusament PLA
PLA-033<br/>Chapuis2025 | τᵢ / branch 11 | 2.582 × 10<sup>−5</sup> s | 65 °C<br/>Prusament PLA
PLA-034<br/>Chapuis2025 | kᵢ / branch 12 | 128.266 MPa | 65 °C<br/>Prusament PLA
PLA-035<br/>Chapuis2025 | τᵢ / branch 12 | 5.363 × 10<sup>−5</sup> s | 65 °C<br/>Prusament PLA
PLA-036<br/>Chapuis2025 | kᵢ / branch 13 | 173.47 MPa | 65 °C<br/>Prusament PLA
PLA-037<br/>Chapuis2025 | τᵢ / branch 13 | 0.0001838 s | 65 °C<br/>Prusament PLA
PLA-038<br/>Chapuis2025 | kᵢ / branch 14 | 93.393 MPa | 65 °C<br/>Prusament PLA
PLA-039<br/>Chapuis2025 | τᵢ / branch 14 | 0.0004386 s | 65 °C<br/>Prusament PLA
PLA-040<br/>Chapuis2025 | kᵢ / branch 15 | 163.804 MPa | 65 °C<br/>Prusament PLA
PLA-041<br/>Chapuis2025 | τᵢ / branch 15 | 0.0007577 s | 65 °C<br/>Prusament PLA
PLA-042<br/>Chapuis2025 | kᵢ / branch 16 | 134.311 MPa | 65 °C<br/>Prusament PLA
PLA-043<br/>Chapuis2025 | τᵢ / branch 16 | 0.001795 s | 65 °C<br/>Prusament PLA
PLA-044<br/>Chapuis2025 | kᵢ / branch 17 | 119.266 MPa | 65 °C<br/>Prusament PLA
PLA-045<br/>Chapuis2025 | τᵢ / branch 17 | 0.002292 s | 65 °C<br/>Prusament PLA
PLA-046<br/>Chapuis2025 | kᵢ / branch 18 | 100.596 MPa | 65 °C<br/>Prusament PLA
PLA-047<br/>Chapuis2025 | τᵢ / branch 18 | 0.006576 s | 65 °C<br/>Prusament PLA
PLA-048<br/>Chapuis2025 | kᵢ / branch 19 | 80.534 MPa | 65 °C<br/>Prusament PLA
PLA-049<br/>Chapuis2025 | τᵢ / branch 19 | 0.00992 s | 65 °C<br/>Prusament PLA
PLA-050<br/>Chapuis2025 | kᵢ / branch 20 | 61.624 MPa | 65 °C<br/>Prusament PLA
PLA-051<br/>Chapuis2025 | τᵢ / branch 20 | 0.0329 s | 65 °C<br/>Prusament PLA
PLA-052<br/>Chapuis2025 | kᵢ / branch 21 | 44.508 MPa | 65 °C<br/>Prusament PLA
PLA-053<br/>Chapuis2025 | τᵢ / branch 21 | 0.05374 s | 65 °C<br/>Prusament PLA
PLA-054<br/>Chapuis2025 | kᵢ / branch 22 | 30.529 MPa | 65 °C<br/>Prusament PLA
PLA-055<br/>Chapuis2025 | τᵢ / branch 22 | 0.06586 s | 65 °C<br/>Prusament PLA
PLA-056<br/>Chapuis2025 | kᵢ / branch 23 | 18.61 MPa | 65 °C<br/>Prusament PLA
PLA-057<br/>Chapuis2025 | τᵢ / branch 23 | 35.03 s | 65 °C<br/>Prusament PLA
PLA-058<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / pattern-search identification | 0.05618 | 75 °C<br/>Prusament PLA
PLA-059<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / Timoshenko-bilayer identification | 0.05605 | 75 °C<br/>Prusament PLA
PLA-060<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / pattern-search identification | 0.04206 | 75 °C<br/>Prusament PLA
PLA-061<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / Timoshenko-bilayer identification | 0.04199 | 75 °C<br/>Prusament PLA
PLA-062<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / pattern-search identification | 0.1035 | 90 °C<br/>Prusament PLA
PLA-063<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / Timoshenko-bilayer identification | 0.1029 | 90 °C<br/>Prusament PLA
PLA-064<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / pattern-search identification | 0.07957 | 90 °C<br/>Prusament PLA
PLA-065<br/>Chapuis2025 | ε₁₁<sup>AM</sup> / Timoshenko-bilayer identification | 0.07926 | 90 °C<br/>Prusament PLA
PLA-066<br/>Luberto2024 | ρ / isotropic | 1240 kg m⁻³ | 20 °C<br/>Unidentified PLA filament
PLA-067<br/>Luberto2024 | c<sub>p</sub> / isotropic | 1800 J kg⁻¹ K⁻¹ | 20 °C<br/>Unidentified PLA filament
PLA-068<br/>Luberto2024 | k / isotropic | 0.13 W m⁻¹ K⁻¹ | 20 °C<br/>Unidentified PLA filament
PLA-069<br/>Trofimov2022 | E / isotropic model table | 1860 MPa | 25 °C<br/>Raise3D Premium PLA with transferred functions
PLA-070<br/>Trofimov2022 | E / isotropic model table | 1727 MPa | 40 °C<br/>Raise3D Premium PLA with transferred functions
PLA-071<br/>Trofimov2022 | E / isotropic model table | 1603 MPa | 50 °C<br/>Raise3D Premium PLA with transferred functions
PLA-072<br/>Trofimov2022 | E / isotropic model table | 1000 MPa | 60 °C<br/>Raise3D Premium PLA with transferred functions
PLA-073<br/>Trofimov2022 | E / isotropic model table | 300 MPa | 70 °C<br/>Raise3D Premium PLA with transferred functions
PLA-074<br/>Trofimov2022 | E / isotropic model table | 50 MPa | 80 °C<br/>Raise3D Premium PLA with transferred functions
PLA-075<br/>Trofimov2022 | E / isotropic model table | 10 MPa | 90 °C<br/>Raise3D Premium PLA with transferred functions
PLA-076<br/>Trofimov2022 | E / isotropic model table | 1 MPa | 100 °C<br/>Raise3D Premium PLA with transferred functions
PLA-077<br/>Trofimov2022 | E / isotropic model table | 1 MPa | 150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-078<br/>Trofimov2022 | α / isotropic low-temperature table value | 79 µm m⁻¹ K⁻¹ | 25–90 °C<br/>Raise3D Premium PLA with transferred functions
PLA-079<br/>Trofimov2022 | α / isotropic high-temperature table value | 147 µm m⁻¹ K⁻¹ | 100–150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-080<br/>Trofimov2022 | k / isotropic low-temperature table value | 0.11 W m⁻¹ K⁻¹ | 25–90 °C<br/>Raise3D Premium PLA with transferred functions
PLA-081<br/>Trofimov2022 | k / isotropic high-temperature table value | 0.19 W m⁻¹ K⁻¹ | 100–150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-082<br/>Trofimov2022 | c<sub>p</sub> / isotropic low-temperature table value | 1590 J kg⁻¹ K⁻¹ | 25–90 °C<br/>Raise3D Premium PLA with transferred functions
PLA-083<br/>Trofimov2022 | c<sub>p</sub> / isotropic high-temperature table value | 1950 J kg⁻¹ K⁻¹ | 100–150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-084<br/>Trofimov2022 | ν / isotropic | 0.36 | 25–150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-085<br/>Trofimov2022 | ρ / isotropic | 1250 kg m⁻³ | 25–150 °C<br/>Raise3D Premium PLA with transferred functions
PLA-086<br/>Li2024 | E₁ / road direction 1 | 2669 MPa | not reported<br/>FormFutura Premium PLA
PLA-087<br/>Li2024 | E₂ / transverse in-plane 2 | 2583 MPa | not reported<br/>FormFutura Premium PLA
PLA-088<br/>Li2024 | E₃ / build direction 3 | 2208 MPa | not reported<br/>FormFutura Premium PLA
PLA-089<br/>Li2024 | ν₁₂ / 12 | 0.43 | not reported<br/>FormFutura Premium PLA
PLA-090<br/>Li2024 | ν₁₃ / 13 | 0.37 | not reported<br/>FormFutura Premium PLA
PLA-091<br/>Li2024 | G₁₂ / 12 | 919 MPa | not reported<br/>FormFutura Premium PLA
PLA-092<br/>Li2024 | G₃₁ / 31 | 844 MPa | not reported<br/>FormFutura Premium PLA
PLA-093<br/>Relaxation2022 | E / 0° | 3045 MPa | not reported<br/>SUNLU PLA Plus
PLA-094<br/>Relaxation2022 | E / 45° | 2914 MPa | not reported<br/>SUNLU PLA Plus
PLA-095<br/>Relaxation2022 | E / 90° | 2932 MPa | not reported<br/>SUNLU PLA Plus
PLA-096<br/>Relaxation2022 | ΔE/E₀ / 0°/45°/90° summary | ≈11–13 % | not reported<br/>SUNLU PLA Plus

### S5. Geometry, discretization and run matrix

The intended coupon is 60 mm × 10 mm × 4 mm, with two 70 mm × 20 mm × 5 mm plates. The reference-state candidate total clearances are 0, 0.01, 0.02, 0.04 and 0.08 mm. These are design choices. No production geometry mesh, heat-transfer boundary history or released-state protocol is approved.

The complete accepted verification matrix comprises one plane-wall thermal run, six structural/contact cases and 28 unique convergence runs. The 43 convergence attempt directories include 15 excluded attempts; they are not independent experiments. The table below identifies every accepted convergence run. Complete case parameters, mesh counts, time histories, contact controls and solver messages are preserved in each case.json, input.dat and mapdl.out.

SUPPTABLE: Complete accepted convergence case matrix
Run directory beneath simulation/convergence | Scope
stage10 contact augmented fkn 0p1 a03 | Reference discretization / contact study; no production prediction
stage10 contact augmented fkn 10 a03 | Reference discretization / contact study; no production prediction
stage10 contact augmented mu 0p1 a03 | Reference discretization / contact study; no production prediction
stage10 contact augmented mu 0p3 a03 | Reference discretization / contact study; no production prediction
stage10 contact mesh fine a03 | Reference discretization / contact study; no production prediction
stage10 contact mesh lagrange coarse a03 | Reference discretization / contact study; no production prediction
stage10 contact mesh lagrange extra fine a03 | Reference discretization / contact study; no production prediction
stage10 contact mesh lagrange fine a03 | Reference discretization / contact study; no production prediction
stage10 contact mesh lagrange medium a03 | Reference discretization / contact study; no production prediction
stage10 contact normal lagrange a03 | Reference discretization / contact study; no production prediction
stage10 contact penalty fkn 0p1 a03 | Reference discretization / contact study; no production prediction
stage10 contact penalty fkn 10 a03 | Reference discretization / contact study; no production prediction
stage10 contact penalty fkn 1 a03 | Reference discretization / contact study; no production prediction
stage10 structural mesh coarse a03 | Reference discretization / contact study; no production prediction
stage10 structural mesh extra fine a01 | Reference discretization / contact study; no production prediction
stage10 structural mesh fine a01 | Reference discretization / contact study; no production prediction
stage10 structural mesh medium a01 | Reference discretization / contact study; no production prediction
stage10 structural mesh ultra fine a01 | Reference discretization / contact study; no production prediction
stage10 structural time coarse a01 | Reference discretization / contact study; no production prediction
stage10 structural time extra fine a01 | Reference discretization / contact study; no production prediction
stage10 structural time medium a01 | Reference discretization / contact study; no production prediction
stage10 thermal mesh coarse a01 | Reference discretization / contact study; no production prediction
stage10 thermal mesh extra fine a01 | Reference discretization / contact study; no production prediction
stage10 thermal mesh fine a01 | Reference discretization / contact study; no production prediction
stage10 thermal mesh medium a01 | Reference discretization / contact study; no production prediction
stage10 thermal time coarse a01 | Reference discretization / contact study; no production prediction
stage10 thermal time extra fine a01 | Reference discretization / contact study; no production prediction
stage10 thermal time medium a01 | Reference discretization / contact study; no production prediction

### S6. Validation and unavailable analyses

The validation registry contains 45 literature observations: 18 reserved source-specific means, 24 excluded context observations and three quarantined secondary maxima. No prediction or validation error is filled. The six temperature levels in Table S4 describe a separate published Ultimaker experiment and are not the proposed Prusament production matrix. Source material, cooling and thermal-contact closure remain insufficient for an independent solve.

The production design and case manifest, all-cases results, Pareto and confirmation tables contain zero result rows. There are no surrogate diagnostics, global sensitivity indices, material probability distributions, uncertainty intervals, Pareto solutions or confirmation runs. No additional production contours can be provided. This release does not claim completion of these studies.

### S7. Historical reproduction record

Tables S1–S12 retain the earlier accepted calculations and material inventory. Their historical build environment, hashes and quality checks remain in the Stage 20 records. Those records describe the earlier package; the current master build, checks and environment are specified in Section M3 and reproducibility/MASTER_README.md. Every archived attempt remains immutable. Neither reference-case convergence nor the current export quality establishes physical validation.

<!-- PAGE -->
### M1. New calculations and numerical verification

The source material-point check is deliberately uniaxial and print-conditioned. Its 23–75 °C history is prescribed and differs from the original spring experiment. The spring involved two PLA formulations; the reserved spring means and newer Prusament dog-bone observations are not calibration inputs and have no prediction column populated. The current main paper and repository decision documents explain why no physical validation accuracy is claimed.

The non-isothermal ANSYS test uses a source-derived 23-arm spectrum, full Newton iteration and a temperature-shift table. The original 0.0001 MPa + 0.002|reference stress| gate is retained. Coarse solver and accuracy failures are listed below. The reference discretization is independently halved. All accepted/rejected input, command, source snapshot, log and scalar export hashes are retained in each attempt directory. Binary result files remain local optional evidence; their manifests distinguish their absence from a changed scalar export.


SUPPTABLE: Every new solver attempt and disposition
Attempt | Disposition | Reason
coarse a01 | Excluded | Python FileNotFoundError [WinError 3]: scratch parent did not exist before solver launch. No solver output.
coarse a02 | Excluded | Solver returned nonzero
coarse a03 | Excluded | Accuracy or wrong-normal check failed
confirm a01 | Accepted | Numerical checks passed
fine a01 | Accepted | Numerical checks passed
medium a01 | Excluded | Accuracy or wrong-normal check failed
table confirm a01 | Accepted | Numerical checks passed
coexpanding inside spacers a01 | Excluded | Accuracy or wrong-normal check failed
coexpanding inside spacers a02 | Accepted | Numerical checks passed
fixed inside spacing a01 | Excluded | Accuracy or wrong-normal check failed
fixed inside spacing a02 | Accepted | Numerical checks passed
fixed outer faces a01 | Excluded | Accuracy or wrong-normal check failed
fixed outer faces a02 | Accepted | Numerical checks passed


SUPPTABLE: Final non-isothermal sample comparisons; stresses in MPa
Time (s) | T (°C) | ANSYS σ | Reference σ | Absolute error
1 | 24 | −0.1149099 | −0.1149099 | 5.28719 × 10<sup>−9</sup>
10 | 33 | −1.114813 | −1.114815 | 1.476839 × 10<sup>−6</sup>
20 | 43 | −2.076544 | −2.076547 | 2.217426 × 10<sup>−6</sup>
30 | 53 | −1.684159 | −1.68418 | 2.094258 × 10<sup>−5</sup>
40 | 63 | −0.08241639 | −0.08252278 | 0.0001063963
42 | 65 | −0.08191326 | −0.08199766 | 8.439955 × 10<sup>−5</sup>
45 | 68 | −0.07270559 | −0.07274731 | 4.171689 × 10<sup>−5</sup>
50 | 73 | −0.03626523 | −0.03626813 | 2.898231 × 10<sup>−6</sup>
55 | 78 | −0.03964798 | −0.03965075 | 2.772462 × 10<sup>−6</sup>
57 | 80 | −0.04107951 | −0.04108327 | 3.76578 × 10<sup>−6</sup>
60 | 80 | −0.04107785 | −0.04107785 | 5.238453 × 10<sup>−10</sup>
70 | 80 | −0.04107785 | −0.04107785 | 5.238526 × 10<sup>−10</sup>
90 | 80 | −0.04107785 | −0.04107785 | 5.238552 × 10<sup>−10</sup>
117 | 80 | −0.04107785 | −0.04107785 | 5.238552 × 10<sup>−10</sup>
120 | 77 | −0.03889468 | −0.03889266 | 2.016738 × 10<sup>−6</sup>
125 | 72 | −0.03499196 | −0.03498697 | 4.991189 × 10<sup>−6</sup>
130 | 67 | −0.02878648 | −0.02873358 | 5.290454 × 10<sup>−5</sup>
132 | 65 | −0.02488581 | −0.02480134 | 8.447737 × 10<sup>−5</sup>
140 | 57 | 0.04362486 | 0.04368606 | 6.120436 × 10<sup>−5</sup>
150 | 47 | 0.644797 | 0.6448054 | 8.437489 × 10<sup>−6</sup>
160 | 37 | 1.674599 | 1.674601 | 1.577862 × 10<sup>−6</sup>
170 | 27 | 2.792315 | 2.792312 | 3.190741 × 10<sup>−6</sup>
174 | 23 | 3.249814 | 3.24981 | 3.3466 × 10<sup>−6</sup>
180 | 23 | 3.248701 | 3.248698 | 3.123272 × 10<sup>−6</sup>
200 | 23 | 3.247546 | 3.247543 | 3.246339 × 10<sup>−6</sup>
234 | 23 | 3.247008 | 3.247004 | 3.310843 × 10<sup>−6</sup>


SUPPTABLE: Programmed-road refinement; dimensionless mechanical and total strains
Substeps | Phase | Mechanical strain | Total strain | Net stress (MPa)
8 | heat | −0.05322308 | −0.04968708 | 3.6107 × 10<sup>−17</sup>
8 | hold | −0.056175 | −0.052639 | 4.22865 × 10<sup>−26</sup>
8 | cool | −0.056175 | −0.056175 | −8.24466 × 10<sup>−30</sup>
32 | heat | −0.0556399 | −0.0521039 | 7.90716 × 10<sup>−19</sup>
32 | hold | −0.056175 | −0.052639 | 8.34342 × 10<sup>−39</sup>
32 | cool | −0.056175 | −0.056175 | 1.50348 × 10<sup>−40</sup>
128 | heat | −0.05610269 | −0.05256669 | 2.54963 × 10<sup>−20</sup>
128 | hold | −0.056175 | −0.052639 | 2.79107 × 10<sup>−49</sup>
128 | cool | −0.056175 | −0.056175 | 9.84877 × 10<sup>−51</sup>
512 | heat | −0.05613575 | −0.05259975 | −1.92181 × 10<sup>−20</sup>
512 | hold | −0.056175 | −0.052639 | 3.57585 × 10<sup>−50</sup>
512 | cool | −0.056175 | −0.056175 | 9.46847 × 10<sup>−53</sup>

The following stop cases use half-thickness symmetry, rigid plane motion, a constant equilibrium spring, prescribed uniform temperature and no nonthermal recovery. Force is the full 600 mm² face resultant. Reported gap is the one-sided node-to-stop separation; total clearance is twice that value. These are benchmarks and not pressure distributions.


SUPPTABLE: Three-dimensional stop outputs; state 1 open, state 2 closed
Mount | Load | T (°C) | Gap (mm) | Force (N) | State
Inner fixed | 1 | 30 | 0.009048 | −0 | 1
Inner fixed | 2 | 45 | 0.007008 | −0 | 1
Inner fixed | 3 | 60 | 0.004968 | −0 | 1
Inner fixed | 4 | 70 | 0.003608 | −0 | 1
Inner fixed | 5 | 75 | 0.002928 | −0 | 1
Inner fixed | 6 | 80 | 0.002248 | −0 | 1
Inner fixed | 7 | 75 | 0.002928 | −0 | 1
Inner fixed | 8 | 70 | 0.003608 | −0 | 1
Inner fixed | 9 | 60 | 0.004968 | −0 | 1
Inner fixed | 10 | 45 | 0.007008 | −0 | 1
Inner fixed | 11 | 30 | 0.009048 | −0 | 1
Inner fixed | 12 | 23 | 0.01 | −0 | 1
Inner spacers | 1 | 30 | 0.009273109 | −0 | 1
Inner spacers | 2 | 45 | 0.007715486 | −0 | 1
Inner spacers | 3 | 60 | 0.006157863 | −0 | 1
Inner spacers | 4 | 70 | 0.005119448 | −0 | 1
Inner spacers | 5 | 75 | 0.00460024 | −0 | 1
Inner spacers | 6 | 80 | 0.004081032 | −0 | 1
Inner spacers | 7 | 75 | 0.00460024 | −0 | 1
Inner spacers | 8 | 70 | 0.005119448 | −0 | 1
Inner spacers | 9 | 60 | 0.006157863 | −0 | 1
Inner spacers | 10 | 45 | 0.007715486 | −0 | 1
Inner spacers | 11 | 30 | 0.009273109 | −0 | 1
Inner spacers | 12 | 23 | 0.01 | −0 | 1
Outer fixed | 1 | 30 | 0.008488026 | −0 | 1
Outer fixed | 2 | 45 | 0.005248085 | −0 | 1
Outer fixed | 3 | 60 | 0.002008142 | −0 | 1
Outer fixed | 4 | 70 | −0 | 0.482695 | 2
Outer fixed | 5 | 75 | −0 | 3.916386 | 2
Outer fixed | 6 | 80 | −0 | 7.350077 | 2
Outer fixed | 7 | 75 | −0 | 3.916386 | 2
Outer fixed | 8 | 70 | −0 | 0.482695 | 2
Outer fixed | 9 | 60 | 0.002008142 | −0 | 1
Outer fixed | 10 | 45 | 0.005248085 | −0 | 1
Outer fixed | 11 | 30 | 0.008488026 | −0 | 1
Outer fixed | 12 | 23 | 0.01 | −0 | 1

### M2. Complete deterministic clearance screen

The critical signed free thickness strain comes from geometry and thermal expansion; it is not an observed or fitted recovery strain. I = fixed inner spacing; S = coexpanding inner spacers; O = fixed outer faces. All calculations use h₀ = 4 mm and plate thickness 5 mm. The mean steel expansion is treated as constant within the manufacturer interval and rebased to 23 °C. No parameter probability or contact-pressure prediction is introduced.


SUPPTABLE: All 90 kinematic scenarios
T (°C) | g₀ (mm) | Mount | ΔH (mm) | e critical (%)
60 | 0 | I | 0 | −0.2516
60 | 0.01 | I | 0 | −0.0016
60 | 0.02 | I | 0 | 0.2484
60 | 0.04 | I | 0 | 0.7484
60 | 0.08 | I | 0 | 1.7484
60 | 0 | S | 0.002367886 | −0.1924028
60 | 0.01 | S | 0.002373806 | 0.05774515
60 | 0.02 | S | 0.002379726 | 0.3078931
60 | 0.04 | S | 0.002391565 | 0.8081891
60 | 0.08 | S | 0.002415244 | 1.808781
60 | 0 | O | −0.005919716 | −0.3995929
60 | 0.01 | O | −0.005919716 | −0.1495929
60 | 0.02 | O | −0.005919716 | 0.1004071
60 | 0.04 | O | −0.005919716 | 0.6004071
60 | 0.08 | O | −0.005919716 | 1.600407
65 | 0 | I | 0 | −0.2856
65 | 0.01 | I | 0 | −0.0356
65 | 0.02 | I | 0 | 0.2144
65 | 0.04 | I | 0 | 0.7144
65 | 0.08 | I | 0 | 1.7144
65 | 0 | S | 0.002687871 | −0.2184032
65 | 0.01 | S | 0.002694591 | 0.03176477
65 | 0.02 | S | 0.00270131 | 0.2819328
65 | 0.04 | S | 0.00271475 | 0.7822687
65 | 0.08 | S | 0.002741628 | 1.782941
65 | 0 | O | −0.006719677 | −0.4535919
65 | 0.01 | O | −0.006719677 | −0.2035919
65 | 0.02 | O | −0.006719677 | 0.04640806
65 | 0.04 | O | −0.006719677 | 0.5464081
65 | 0.08 | O | −0.006719677 | 1.546408
70 | 0 | I | 0 | −0.3196
70 | 0.01 | I | 0 | −0.0696
70 | 0.02 | I | 0 | 0.1804
70 | 0.04 | I | 0 | 0.6804
70 | 0.08 | I | 0 | 1.6804
70 | 0 | S | 0.003007856 | −0.2444036
70 | 0.01 | S | 0.003015375 | 0.005784382
70 | 0.02 | S | 0.003022895 | 0.2559724
70 | 0.04 | S | 0.003037934 | 0.7563484
70 | 0.08 | S | 0.003068013 | 1.7571
70 | 0 | O | −0.007519639 | −0.507591
70 | 0.01 | O | −0.007519639 | −0.257591
70 | 0.02 | O | −0.007519639 | −0.007590976
70 | 0.04 | O | −0.007519639 | 0.492409
70 | 0.08 | O | −0.007519639 | 1.492409
75 | 0 | I | 0 | −0.3536
75 | 0.01 | I | 0 | −0.1036
75 | 0.02 | I | 0 | 0.1464
75 | 0.04 | I | 0 | 0.6464
75 | 0.08 | I | 0 | 1.6464
75 | 0 | S | 0.00332784 | −0.270404
75 | 0.01 | S | 0.00333616 | −0.020196
75 | 0.02 | S | 0.003344479 | 0.230012
75 | 0.04 | S | 0.003361119 | 0.730428
75 | 0.08 | S | 0.003394397 | 1.73126
75 | 0 | O | −0.008319601 | −0.56159
75 | 0.01 | O | −0.008319601 | −0.31159
75 | 0.02 | O | −0.008319601 | −0.06159002
75 | 0.04 | O | −0.008319601 | 0.43841
75 | 0.08 | O | −0.008319601 | 1.43841
80 | 0 | I | 0 | −0.3876
80 | 0.01 | I | 0 | −0.1376
80 | 0.02 | I | 0 | 0.1124
80 | 0.04 | I | 0 | 0.6124
80 | 0.08 | I | 0 | 1.6124
80 | 0 | S | 0.003647825 | −0.2964044
80 | 0.01 | S | 0.003656944 | −0.04617639
80 | 0.02 | S | 0.003666064 | 0.2040516
80 | 0.04 | S | 0.003684303 | 0.7045076
80 | 0.08 | S | 0.003720781 | 1.70542
80 | 0 | O | −0.009119562 | −0.6155891
80 | 0.01 | O | −0.009119562 | −0.3655891
80 | 0.02 | O | −0.009119562 | −0.1155891
80 | 0.04 | O | −0.009119562 | 0.3844109
80 | 0.08 | O | −0.009119562 | 1.384411
85 | 0 | I | 0 | −0.4216
85 | 0.01 | I | 0 | −0.1716
85 | 0.02 | I | 0 | 0.0784
85 | 0.04 | I | 0 | 0.5784
85 | 0.08 | I | 0 | 1.5784
85 | 0 | S | 0.00396781 | −0.3224048
85 | 0.01 | S | 0.003977729 | −0.07215677
85 | 0.02 | S | 0.003987649 | 0.1780912
85 | 0.04 | S | 0.004007488 | 0.6785872
85 | 0.08 | S | 0.004047166 | 1.679579
85 | 0 | O | −0.009919524 | −0.6695881
85 | 0.01 | O | −0.009919524 | −0.4195881
85 | 0.02 | O | −0.009919524 | −0.1695881
85 | 0.04 | O | −0.009919524 | 0.3304119
85 | 0.08 | O | −0.009919524 | 1.330412

### M3. Reproduction, unresolved results and data separation

Run the Python unit suite and scripts/screen_fixture_mechanism.py, scripts/check_programmed_recovery.py, scripts/summarize_master_nonisothermal.py --audit-reference, and scripts/check_master.py from the repository root. The first two perform numerical calculations; the third recomputes comparison summaries from immutable exports. No ANSYS license is needed for these checks. scripts/plot_master.py draws the figures; scripts/build_master.py and scripts/build_master_supplement.py regenerate the documents from their maintained sources. The exact tested dependency versions and font/Office requirements are documented in reproducibility/MASTER_README.md. The main PDF is a native Word export of the editable manuscript; this supplement is typeset separately.

To repeat a solver case, use compatible Ansys Student 2026 R1/MAPDL26.1 with a valid license and a new empty working directory; run its archived input.dat with the recorded command adapted to the new path. Never reuse an archived attempt directory. The master runners accept a new attempt identifier and preserve accepted and failed evidence. They do not assemble a validated production coupon. One SOLID185 plus one CONTA178 in the stop test is far below the documented Student node limit but is not a converged production surface mesh.

No production design is approved. All production, sensitivity, uncertainty, surrogate, optimization and confirmation registries remain empty. These absences are not zero errors, zero warpage, an empty feasible set or a failed physical validation score. Source-specific reserved observations are in validation/master_spring_targets.csv and validation/master_suder_targets.csv; their original cohorts and limitations are retained. Earlier Ultimaker means remain in the legacy register. No dataset is both fitted and independently validated here.

The code-generated figures contain no AI-generated result imagery. Raw scalar evidence, equation/source links and all final artifacts are hashed. The prior full numerical tables are retained above; the duplicate thermal case-label ambiguity in S10 is corrected by keeping mesh/time in the names. The following legacy bibliography permits independent interpretation of all prior numeric citations. New citations in the main article use its own bibliography.

### M4. Legacy reference key for Tables S1–S12

[1] Javaid Butt, Raghunath Bhaskar. Investigating the Effects of Annealing on the Mechanical Properties of FFF-Printed Thermoplastics. <i>Journal of Manufacturing and Materials Processing</i> 4(2), 38 (2020). <link href="https://doi.org/10.3390/jmmp4020038" color="#24576b">doi:10.3390/jmmp4020038</link>.

[2] Jelena R. Stojković, Rajko Turudija, Nikola Vitković et al. An Experimental Study on the Impact of Layer Height and Annealing Parameters on the Tensile Strength and Dimensional Accuracy of FDM 3D Printed Parts. <i>Materials</i> 16(13), 4574 (2023). <link href="https://doi.org/10.3390/ma16134574" color="#24576b">doi:10.3390/ma16134574</link>.

[3] ASTM International. <i>Standard Guide for Additive Manufacturing of Polymers — Material Extrusion — Recommendation for Material Handling and Evaluation of Static Mechanical Properties</i>. ASTM F3489-23 (2023). <link href="https://doi.org/10.1520/F3489-23" color="#24576b">doi:10.1520/F3489-23</link>.

[4] George Derringer, Ronald Suich. Simultaneous Optimization of Several Response Variables. <i>Journal of Quality Technology</i> 12(4), 214-219 (1980). <link href="https://doi.org/10.1080/00224065.1980.11980968" color="#24576b">doi:10.1080/00224065.1980.11980968</link>.

[5] Irina Bute, Sergejs Tarasovs, Jevgenijs Sevcenko, Andrey Aniskevich. Thermomechanical Analysis and Numerical Simulations of Fused Filament Fabricated Polylactic Acid Parts. <i>Materials Science</i> 30(2), 217-225 (2024). <link href="https://doi.org/10.5755/j02.ms.35076" color="#24576b">doi:10.5755/j02.ms.35076</link>.

[6] Bas Wijnen, Paul Sanders, Joshua M. Pearce. Improved model and experimental validation of deformation in fused filament fabrication of polylactic acid. <i>Progress in Additive Manufacturing</i> 3(4), 193-203 (2018). <link href="https://doi.org/10.1007/s40964-018-0052-4" color="#24576b">doi:10.1007/s40964-018-0052-4</link>.

[7] Anton Trofimov, Jérémy Le Pavic, Sébastien Pautard et al. Experimentally validated modeling of the temperature distribution and the distortion during the Fused Filament Fabrication process. <i>Additive Manufacturing</i> 54, 102693 (2022). <link href="https://doi.org/10.1016/j.addma.2022.102693" color="#24576b">doi:10.1016/j.addma.2022.102693</link>.

[8] Joël N Chapuis, Gian Teufen, Kristina Shea. Thermo-viscoelastic laminate-based finite element modeling of fused filament fabrication direct 4D printing. <i>Smart Materials and Structures</i> 34(7), 075034 (2025). <link href="https://doi.org/10.1088/1361-665x/adeee4" color="#24576b">doi:10.1088/1361-665x/adeee4</link>.


[9] Zhamila Issabayeva, Igor Shishkovsky. Prediction of The Mechanical Behavior of Polylactic Acid Parts with Shape Memory Effect Fabricated by FDM. <i>Polymers</i> 15(5), 1162 (2023). <link href="https://doi.org/10.3390/polym15051162" color="#24576b">doi:10.3390/polym15051162</link>.

[10] Mahmoud Farh, Viktor Gribniak. Thermo-Mechanical Approach to Material Extrusion Process During Fused Filament Fabrication of Polymeric Samples. <i>Materials</i> 18(19), 4537 (2025). <link href="https://doi.org/10.3390/ma18194537" color="#24576b">doi:10.3390/ma18194537</link>.

[11] Joaquín Lluch-Cerezo, María Desamparados Meseguer, Juan Antonio García-Manrique, Rut Benavente. Influence of Thermal Annealing Temperatures on Powder Mould Effectiveness to Avoid Deformations in ABS and PLA 3D-Printed Parts. <i>Polymers</i> 14(13), 2607 (2022). <link href="https://doi.org/10.3390/polym14132607" color="#24576b">doi:10.3390/polym14132607</link>.

[12] Diede Christine Wijnbergen, Merel van der Stelt, Luc Martijn Verhamme. The effect of annealing on deformation and mechanical strength of tough PLA and its application in 3D printed prosthetic sockets. <i>Rapid Prototyping Journal</i> 27(11), 81-89 (2021). <link href="https://doi.org/10.1108/rpj-04-2021-0090" color="#24576b">doi:10.1108/rpj-04-2021-0090</link>.

[13] Cleiton Lazaro Fazolo de Assis, Kelvin dos Santos Tiene, Gabriel Boni Magosse. Dimensional Stability and Mechanical Performance of Thermally Conditioned High‐Heat Polylactic Acid Parts Produced by Fused Filament Fabrication. <i>Polymer Engineering &amp; Science</i> 66(2), 941-958 (2026). <link href="https://doi.org/10.1002/pen.70250" color="#24576b">doi:10.1002/pen.70250</link>.

[14] Rania Ben Amor, Slim Souissi. Multiscale modeling and multiobjective optimization of the mechanical behavior of annealed and non-annealed material extrusion printed PLA. <i>Discover Materials</i>  (2026). <link href="https://doi.org/10.1007/s43939-026-00769-2" color="#24576b">doi:10.1007/s43939-026-00769-2</link>.

[15] Bingnong Jiang, Yuan Chen, Lin Ye et al. Residual stress and warpage of additively manufactured SCF/PLA composite parts. <i>Advanced Manufacturing: Polymer &amp; Composites Science</i> 9(1), 2171940 (2023). <link href="https://doi.org/10.1080/20550340.2023.2171940" color="#24576b">doi:10.1080/20550340.2023.2171940</link>.

[16] Meiyu Li, Yanan Xu, Jianguang Fang. Orthotropic mechanical properties of PLA materials fabricated by fused deposition modeling. <i>Thin-Walled Structures</i> 199, 111800 (2024). <link href="https://doi.org/10.1016/j.tws.2024.111800" color="#24576b">doi:10.1016/j.tws.2024.111800</link>.


[17] R. Pantani, F. De Santis, A. Sorrentino et al. Crystallization kinetics of virgin and processed poly(lactic acid). <i>Polymer Degradation and Stability</i> 95(7), 1148-1159 (2010). <link href="https://doi.org/10.1016/j.polymdegradstab.2010.04.018" color="#24576b">doi:10.1016/j.polymdegradstab.2010.04.018</link>.

[18] Felice De Santis, Roberto Pantani, Giuseppe Titomanlio. Nucleation and crystallization kinetics of poly(lactic acid). <i>Thermochimica Acta</i> 522(1-2), 128-134 (2011). <link href="https://doi.org/10.1016/j.tca.2011.05.034" color="#24576b">doi:10.1016/j.tca.2011.05.034</link>.

[19] Targol Hashemi, Sara Liparoti, Valentina Volpe et al. Analysis of Crystallization Kinetics of PLA Filament for Fused Filament Fabrication. <i>Macromolecular Materials and Engineering</i> 310(12), e00204 (2025). <link href="https://doi.org/10.1002/mame.202500204" color="#24576b">doi:10.1002/mame.202500204</link>.

[20] Todsapol Kajornprai, Jiradet Sringam, Anucha Seejuntuek et al. Crystal Evolution of Amorphous Poly(lactic acid) During Simultaneous Multi‐step Tensile Deformation and Annealing. <i>Journal of Polymer Science</i> 63(1), 192-203 (2025). <link href="https://doi.org/10.1002/pol.20240703" color="#24576b">doi:10.1002/pol.20240703</link>.

[21] Necmi Dusunceli, Aleksey D. Drozdov, Naseem Theilgaard. Influence of temperature on viscoelastic–viscoplastic behavior of poly(lactic acid) under loading–unloading. <i>Polymer Engineering &amp; Science</i> 57(3), 239-247 (2017). <link href="https://doi.org/10.1002/pen.24404" color="#24576b">doi:10.1002/pen.24404</link>.

[22] Alcide Bertocco, Matteo Bruno, Enrico Armentani et al. Stress Relaxation Behavior of Additively Manufactured Polylactic Acid (PLA). <i>Materials</i> 15(10), 3509 (2022). <link href="https://doi.org/10.3390/ma15103509" color="#24576b">doi:10.3390/ma15103509</link>.

[23] Çağlar Kahya, Oğuz Tunçel, Onur Çavuşoğlu, Kenan Tüfekci. Thermal annealing optimization for improved mechanical performance of PLA parts produced via 3D printing. <i>Polymer Testing</i> 144, 108735 (2025). <link href="https://doi.org/10.1016/j.polymertesting.2025.108735" color="#24576b">doi:10.1016/j.polymertesting.2025.108735</link>.

[24] Florina Chiscop, Carmen-Cristiana Cazacu, Dragos-Alexandru Cazacu, Costel Emil Cotet. Sustainable Thermal Post-Processing of PLA 3D Prints: Increased Dimensional Precision and Autoclave Compatibility. <i>Journal of Functional Biomaterials</i> 16(9), 334 (2025). <link href="https://doi.org/10.3390/jfb16090334" color="#24576b">doi:10.3390/jfb16090334</link>.


[25] Agnieszka Szust, Grzegorz Adamski. Using thermal annealing and salt remelting to increase tensile properties of 3D FDM prints. <i>Engineering Failure Analysis</i> 132, 105932 (2022). <link href="https://doi.org/10.1016/j.engfailanal.2021.105932" color="#24576b">doi:10.1016/j.engfailanal.2021.105932</link>.

[26] Miloš Vorkapić, Ivana Mladenović, Toni Ivanov et al. Enhancing mechanical properties of 3D printed thermoplastic polymers by annealing in moulds. <i>Advances in Mechanical Engineering</i> 14(8), 16878132221120737 (2022). <link href="https://doi.org/10.1177/16878132221120737" color="#24576b">doi:10.1177/16878132221120737</link>.

[27] Radoslaw A. Wach, Piotr Wolszczak, Agnieszka Adamus‐Wlodarczyk. Enhancement of Mechanical Properties of FDM‐PLA Parts via Thermal Annealing. <i>Macromolecular Materials and Engineering</i> 303(9), 1800169 (2018). <link href="https://doi.org/10.1002/mame.201800169" color="#24576b">doi:10.1002/mame.201800169</link>.

[28] Claire Benwood, Andrew Anstey, Jacek Andrzejewski et al. Improving the Impact Strength and Heat Resistance of 3D Printed Models: Structure, Property, and Processing Correlationships during Fused Deposition Modeling (FDM) of Poly(Lactic Acid). <i>ACS Omega</i> 3(4), 4400-4411 (2018). <link href="https://doi.org/10.1021/acsomega.8b00129" color="#24576b">doi:10.1021/acsomega.8b00129</link>.

[29] Natalia von Windheim, David W. Collinson, Trent Lau et al. The influence of porosity, crystallinity and interlayer adhesion on the tensile strength of 3D printed polylactic acid (PLA). <i>Rapid Prototyping Journal</i> 27(7), 1327-1336 (2021). <link href="https://doi.org/10.1108/rpj-08-2020-0205" color="#24576b">doi:10.1108/rpj-08-2020-0205</link>.

[30] Ali Ghasemkhani, Gholamreza Pircheraghi, Nima Rashidi Mehrabadi, Asma Eshraghi. Effects of heat treatment on the mechanical properties of 3D-printed polylactic acid: Study of competition between crystallization and interlayer bonding. <i>Materials Today Communications</i> 39, 109266 (2024). <link href="https://doi.org/10.1016/j.mtcomm.2024.109266" color="#24576b">doi:10.1016/j.mtcomm.2024.109266</link>.

[31] Malcolm L. Williams, Robert F. Landel, John D. Ferry. The Temperature Dependence of Relaxation Mechanisms in Amorphous Polymers and Other Glass-forming Liquids. <i>Journal of the American Chemical Society</i> 77(14), 3701-3707 (1955). <link href="https://doi.org/10.1021/ja01619a008" color="#24576b">doi:10.1021/ja01619a008</link>.

[32] Nathalie Ramos, Christoph Mittermeier, Josef Kiendl. Efficient simulation of the heat transfer in fused filament fabrication. <i>Journal of Manufacturing Processes</i> 94, 550-563 (2023). <link href="https://doi.org/10.1016/j.jmapro.2023.03.030" color="#24576b">doi:10.1016/j.jmapro.2023.03.030</link>.


[33] Ahmed Elmoghazy, Anselm Heuer, Aron Kneer et al. Phase-field modeling of the morphological and thermal evolution of additively manufactured polylactic acid layers and their influence on the effective elastic mechanical properties. <i>Progress in Additive Manufacturing</i> 10(8), 5093-5115 (2025). <link href="https://doi.org/10.1007/s40964-024-00891-8" color="#24576b">doi:10.1007/s40964-024-00891-8</link>.

[34] Edson A. dos Santos Filho, Edda Valentina Veracierta Rodriguez, Simon Debrie et al. Thermal Annealing of Injection‐Molded PLA Grades: Trade‐Offs Between Crystallinity Development, Dimensional Stability, Secondary Shrinkage, and Mechanical Performance. <i>Journal of Applied Polymer Science</i> 143(37), e71150 (2026). <link href="https://doi.org/10.1002/app.71150" color="#24576b">doi:10.1002/app.71150</link>.

[35] Natrayan Lakshmaiya. Thermo-constrained physics informed neural network based optimization of mechanical performance in recycled PLA additive manufacturing. <i>Results in Engineering</i> 30, 110279 (2026). <link href="https://doi.org/10.1016/j.rineng.2026.110279" color="#24576b">doi:10.1016/j.rineng.2026.110279</link>.

[36] Prusa Polymers a.s. <i>Technical datasheet: Prusament PLA</i>. Version 1.1, 27 July 2022. <link href="https://prusament.com/materials/pla/" color="#24576b">prusament.com/materials/pla</link>.

[37] Luca Luberto, Volker Böß, Kristin M. de Payrebrune. Finite Difference Modeling and Experimental Investigation of Cyclic Thermal Heating in the Fused Filament Fabrication Process. <i>3D Printing and Additive Manufacturing</i> 11(3), e1064–e1072 (2024). <link href="https://doi.org/10.1089/3dp.2022.0282" color="#24576b">doi:10.1089/3dp.2022.0282</link>.

[38] Longhui Meng, Aqib Mashood Khan, Yicai Shan, Khalid A. Al-Ghamdi. Saturation behavior and full-field reconstruction of residual stress in quenched AISI 304 stainless steel via the contour method. <i>Scientific Reports</i> 16, 11694 (2026). <link href="https://doi.org/10.1038/s41598-026-45542-w" color="#24576b">doi:10.1038/s41598-026-45542-w</link>.

[39] ANSYS, Inc. <i>Mechanical APDL Theory Reference</i>, Release 2026 R1, §4.9, Viscoelasticity. <link href="https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_thry/thy_mat6.html" color="#24576b">Official theory reference</link>. Accessed 12 September 2026.

[40] Ansys, Inc. <i>Ansys Student — Free Software Download</i>, 2026 R1 product page. <link href="https://www.ansys.com/en-in/academic/students/ansys-student" color="#24576b">Official product page</link>. Accessed 13 September 2026.

[41] Heba Hussam, MEmad S. Soliman, Ibrahim M. Hassab-Allah, Yasser Abdelrhman. Effect of annealing on FDM-manufactured ABS parts. <i>The International Journal of Advanced Manufacturing Technology</i> 138, 2233–2243 (2025). <link href="https://doi.org/10.1007/s00170-025-15455-5" color="#24576b">doi:10.1007/s00170-025-15455-5</link>.
