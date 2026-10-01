# Supplementary information for constrained annealing verification

Verification-only release · 1 October 2026

This supplement documents genuine reference calculations and published material data. No production simulation, independent validation prediction, sensitivity index, uncertainty interval, Pareto solution or optimization confirmation exists. Missing results are not zero responses. Reference numbers refer to the accompanying main article.


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
Mesh | S coarse a03 | W<sub>max</sub> | 0.008170221 | mm |
Mesh | S coarse a03 | resid. disp. | 0.05963922 | mm |
Mesh | S coarse a03 | resid. stress p95 | 9.965 × 10<sup>−5</sup> | MPa |
Mesh | S medium a01 | W<sub>max</sub> | 0.01125978 | mm | 27.43893
Mesh | S medium a01 | resid. disp. | 0.07853777 | mm | 24.06301
Mesh | S medium a01 | resid. stress p95 | 0.000494075 | MPa | 79.831
Mesh | S fine a01 | W<sub>max</sub> | 0.01250177 | mm | 9.934494
Mesh | S fine a01 | resid. disp. | 0.08534517 | mm | 7.976313
Mesh | S fine a01 | resid. stress p95 | 0.0007046092 | MPa | 29.87957
Mesh | S extra fine a01 | W<sub>max</sub> | 0.01279686 | mm | 2.305902
Mesh | S extra fine a01 | resid. disp. | 0.08674431 | mm | 1.612952
Mesh | S extra fine a01 | resid. stress p95 | 0.0007082847 | MPa | 0.5189303
Mesh | S ultra fine a01 | W<sub>max</sub> | 0.01291733 | mm | 0.9326807
Mesh | S ultra fine a01 | resid. disp. | 0.08725225 | mm | 0.5821426
Mesh | S ultra fine a01 | resid. stress p95 | 0.0007229355 | MPa | 2.026572
Mesh | T coarse a01 | T lag at 300 s | 52.37903 | °C |
Mesh | T coarse a01 | temp. grad. at 300 s | 252.1411 | K m⁻¹ |
Mesh | T medium a01 | T lag at 300 s | 52.37115 | °C | 0.01505384
Mesh | T medium a01 | temp. grad. at 300 s | 252.384 | K m⁻¹ | 0.09626966
Mesh | T fine a01 | T lag at 300 s | 52.36917 | °C | 0.003767935
Mesh | T fine a01 | temp. grad. at 300 s | 252.4447 | K m⁻¹ | 0.02403675
Mesh | T extra fine a01 | T lag at 300 s | 52.36868 | °C | 0.0009422631
Mesh | T extra fine a01 | temp. grad. at 300 s | 252.4599 | K m⁻¹ | 0.006007273
Mesh | C lagrange coarse a03 | mean C press. | 16.98722 | MPa |
Mesh | C lagrange coarse a03 | max. C press. | 19.76897 | MPa |
Mesh | C lagrange coarse a03 | max. penetration | 0 | mm |
Mesh | C lagrange coarse a03 | normal reaction | 172.4908 | N mm⁻¹ |
Mesh | C lagrange medium a03 | mean C press. | 17.44909 | MPa | 2.646943
Mesh | C lagrange medium a03 | max. C press. | 20.98779 | MPa | 5.807288
Mesh | C lagrange medium a03 | max. penetration | 0 | mm |
Mesh | C lagrange medium a03 | normal reaction | 177.2646 | N mm⁻¹ | 2.69307
Mesh | C lagrange fine a03 | mean C press. | 17.57206 | MPa | 0.6997847
Mesh | C lagrange fine a03 | max. C press. | 21.37878 | MPa | 1.82884
Mesh | C lagrange fine a03 | max. penetration | 0 | mm |
Mesh | C lagrange fine a03 | normal reaction | 178.5694 | N mm⁻¹ | 0.7306797
Mesh | C lagrange extra fine a03 | mean C press. | 17.5944 | MPa | 0.1269802
Mesh | C lagrange extra fine a03 | max. C press. | 21.45629 | MPa | 0.3612721
Mesh | C lagrange extra fine a03 | max. penetration | 0 | mm |
Mesh | C lagrange extra fine a03 | normal reaction | 178.8167 | N mm⁻¹ | 0.1383057
Time | S coarse a01 | W<sub>max</sub> | 0.01248075 | mm |
Time | S coarse a01 | resid. disp. | 0.085201 | mm |
Time | S coarse a01 | resid. stress p95 | 0.0007069894 | MPa |
Time | S medium a01 | W<sub>max</sub> | 0.01249482 | mm | 0.1126111
Time | S medium a01 | resid. disp. | 0.08529745 | mm | 0.1130754
Time | S medium a01 | resid. stress p95 | 0.0007080892 | MPa | 0.155314
Time | S fine a01 | W<sub>max</sub> | 0.01250177 | mm | 0.05561255
Time | S fine a01 | resid. disp. | 0.08534517 | mm | 0.05591337
Time | S fine a01 | resid. stress p95 | 0.0007046092 | MPa | 0.4938889
Time | S extra fine a01 | W<sub>max</sub> | 0.01250216 | mm | 0.00309372
Time | S extra fine a01 | resid. disp. | 0.08534791 | mm | 0.003212977
Time | S extra fine a01 | resid. stress p95 | 0.0007036497 | MPa | 0.136358
Time | T coarse a01 | T lag at 300 s | 52.2638 | °C |
Time | T coarse a01 | temp. grad. at 300 s | 251.9462 | K m⁻¹ |
Time | T coarse a01 | temp. profile L2 excursion | 23.72262 | °C |
Time | T medium a01 | T lag at 300 s | 52.35208 | °C | 0.1686272
Time | T medium a01 | temp. grad. at 300 s | 252.3786 | K m⁻¹ | 0.1713168
Time | T medium a01 | temp. profile L2 excursion | 23.74377 | °C | 0.08906041
Time | T extra fine a01 | T lag at 300 s | 52.36868 | °C | 0.03169506
Time | T extra fine a01 | temp. grad. at 300 s | 252.4599 | K m⁻¹ | 0.03220043
Time | T extra fine a01 | temp. profile L2 excursion | 23.74776 | °C | 0.01683771
Time | T extra fine a01 | T lag at 300 s | 52.37145 | °C | 0.005284926
Time | T extra fine a01 | temp. grad. at 300 s | 252.4734 | K m⁻¹ | 0.005369188
Time | T extra fine a01 | temp. profile L2 excursion | 23.74843 | °C | 0.002810575

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

### S7. Reproduction and interpretation

Use Python 3.12 with the pinned requirements. The release was built with Python 3.12.14, ReportLab 4.4.9, python-docx 1.2.0, lxml 6.1.1 and latex2mathml 3.78.1. Windows fonts and the installed Office MathML-to-OMML stylesheet are required for the present export script; these are not redistributed. Word equations are native editable OMML.

Run the unit tests, check_release.py, and the commands in reproducibility/README.md. Archived solver decks require compatible Ansys Student 2026 R1 / MAPDL 26.1 update 20260202 and a usable license. A fresh result directory is mandatory. Do not overwrite archived attempts. Rerun comparison calculations before accepting newly solved cases. A later solver version need not produce identical binary files.

The SHA-256 manifest covers the final three files, critical data, input decks, analysis and build scripts. The traceability and figure/table manifests identify evidence paths. Historical third-party PDFs have been removed from the current release tree and remain unchanged locally; earlier Git history was not rewritten. Obtain those sources legally using external_evidence.csv. Published values are not new experiments. No scientific image was generated by AI.
