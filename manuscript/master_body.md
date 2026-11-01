# Contact feasibility and non-isothermal verification for gap-constrained annealing of FFF-printed PLA

Aadit Jain, Dheeraj Yadav and Ekansh Malhotra

Delhi Technological University, Delhi, India

Computational verification and feasibility study · 1 November 2026

### Abstract

Opposed plates can influence annealing only when the evolving specimen shape reaches them. Predicting this interaction requires a printed material state as well as a nominal clearance. This study examines these prerequisites using a literature-derived Prusament PLA relaxation spectrum, an independent material-point recovery calculation and genuine Mechanical APDL reference problems. Non-isothermal temperature shifting is tested over a prescribed 23–80–23 °C cycle against an independent scalar integration. Three-dimensional elastic stop tests distinguish fixed inner spacing, expanding inner spacers and fixed outer faces. At 80 °C and a 0.020 mm total clearance, these arrangements require signed free thickness recovery strains of +0.112%, +0.204% and −0.116%, respectively, to reach first contact. The same nominal gap therefore does not define the same restraint. A source-conditioned programmed-road calculation approaches its prescribed 5.62% contraction limit; this checks stored-strain recovery without establishing bulk coupon shrinkage. The achieved contribution is an auditable contact-feasibility and constitutive-verification framework. Independent coupon validation remains unresolved because the printed initial state, compatible heat-transfer functions and matched fixture observations are missing. Consequently, no validated warpage suppression, residual-stress reduction or optimal annealing window is inferred.

Keywords: fused filament fabrication; polylactic acid; annealing; viscoelasticity; mechanical contact; numerical verification

### 1. Introduction

Thermal post-processing can change the dimensions and morphology of fused filament fabrication (FFF) PLA. The resulting response depends on formulation, printing history, orientation and exposure, so a geometric fixture is not by itself a predictive process model. Opposed plates are already used for PLA annealing [3], and mould-clearance comparisons have been reported for ABS [4]. Neither the use of ANSYS nor the existence of a controlled gap constitutes a novelty claim. The unresolved issue is whether a specified clearance produces a measurable mechanical interaction for the actual printed state and thermal cycle.

Several studies establish the relevant mechanisms without supplying a universal constitutive law. Bute et al. [2] measured directional irreversible thermal strain and found that printing-stress relaxation alone did not explain it. Chapuis et al. [1] combined viscoelasticity with calibrated print-programmed strain for thermally deployed laminates. Frölich et al. [5] separated directional reorientation and cold-crystallization signatures in Ultrafuse PLA. These data cannot be combined silently into a single Prusament material card. Experimentally compared thermal and distortion simulations also exist for the deposition process [10], while annealed-PLA multiscale modeling and multiobjective optimization have precedents [9]. A new process recommendation must therefore be supported by the particular material, observable and restraint being modeled.

Contact is especially sensitive to the sign of dimensional change. Published PLA datasets contain thickness growth alongside in-plane shortening [7,8]. It would be incorrect to infer separation from longitudinal shrinkage alone. Conversely, placing a flat specimen inside a fixture does not guarantee contact, and zero clearance does not prescribe preload. Thermal expansion of the stops and plates may enlarge or reduce the opening depending on the mounting arrangement. A stress-free symmetric model also supplies no measured source of bending; artificial material mismatch cannot establish an annealing benefit.

The immediate research question is therefore: how do support kinematics and signed free thickness change determine contact feasibility, and can the temperature-shifted constitutive implementation reproduce independently calculated transient responses? The broader question concerning temperature, hold duration and clearance effects on released dimensions, warpage and residual stress remains conditional on physical identification and validation. This article contributes a verified numerical diagnostic and a documented limit on extrapolation. It does not assert an exclusive new material law or an experimentally established processing window.

### 2. Computational methodology
### 2.1. Material basis and admissible scope

Three material strategies were evaluated: extend the existing Prusament law, change formulation, or restrict its domain. Restriction was selected for component verification. The source DMA characterization spans 23–85 °C and 1–18 Hz [1]; this is not a blanket validation of long holds, bulk sections or multiaxial recovery. Extending the original 95 and 110 °C proposals would require additional material evidence. Black Devil Design and BASF Ultrafuse offer valuable thermal and directional-strain measurements [2,5], but their observed ramp trajectories and limited mechanical frequency data do not uniquely identify a Prusament hold-time response. Supplementary Information retains the full material inventory and formulation restrictions.

The reference spectrum contains 23 positive Maxwell branches, equilibrium modulus 10.598 MPa, Poisson ratio 0.35 and reversible expansion coefficient 68.0 µm m⁻¹ K⁻¹ [1]. Their calculated instantaneous modulus is 1691.594 MPa. Equal normalized shear and bulk spectra impose constant Poisson ratio; they are an isotropic extension of the source laminate model, not measured volumetric relaxation. An additional unrelated temperature-dependent elastic multiplier would change the identified spectrum. Compatible printed-state conductivity, heat capacity, recovery tensor and contact transport were not admitted. Missing values are not assigned zero.

### 2.2. Non-isothermal constitutive implementation

For the homogeneous uniaxial reference, mechanical strain excludes reversible thermal strain. Equilibrium and branch stresses obey

EQ: σ = E<sub>∞</sub>ε<sup>m</sup> + ∑<sub>j=1</sub><sup>23</sup>s<sub>j</sub>, &nbsp; ∂s<sub>j</sub>/∂ξ + s<sub>j</sub>/τ<sub>j</sub> = E<sub>j</sub>∂ε<sup>m</sup>/∂ξ. &nbsp; (1)

EQ: ξ(t) = ∫<sub>0</sub><sup>t</sup>[a<sub>T</sub>(T(u))]<sup>−1</sup> du, &nbsp; ε<sup>th</sup> = α<sub>p</sub>(T − T<sub>r</sub>). &nbsp; (2)

The source Arrhenius/WLF clock uses temperature in kelvin below the transition and temperature differences in kelvin above it [1]:

EQ: log<sub>10</sub>a<sub>T</sub> = 35 000(1/T<sub>K</sub> − 1/338.15) for T &lt; 65 °C;<br/>log<sub>10</sub>a<sub>T</sub> = −17.4(T − 65)/(51.6 + T − 65) for T ≥ 65 °C. &nbsp; (3)

Mechanical APDL 2026 R1, build 26.1, update 20260202, executes the Student solver. A 10 mm × 1 mm × 1 mm SOLID185 brick is axially restrained and laterally traction-free. Coordinate-plane displacement constraints remove transverse rigid motions. A spatially uniform prescribed material temperature rises from 23 to 80 °C at 1 K s⁻¹, holds for 60 s, cools at the same rate and remains at 23 °C for 60 s. This is a constitutive patch test, not an oven simulation or a released specimen. Temperatures are independently checked from extracted thermal strain.

The native Prony spectra are combined with a piecewise-linear SHIFT table [12]. Its entries are absolute temperature and log₁₀(1/a<sub>T</sub>), the rate multiplier rather than the source time multiplier. Table refinement brackets the transition explicitly. Full Newton iteration, fixed time increments and endpoint extraction are used. An independent scalar exponential integrator evaluates the exact source clock with midpoint subdivision; its 0.001 s step is checked against 0.0005 s. At 26 predeclared sample times, the numerical acceptance rule is absolute stress difference ≤ 0.0001 MPa + 0.002|σ<sub>reference</sub>|. Adjacent time/table refinements use the same mixed rule with the finer stress. These tolerances are verification choices and do not define physical validation accuracy.

### 2.3. Stored-strain recovery and separation from calibration

A programmed printed road need not have relaxed internal branches even when its total traction vanishes. Following the source initialization [1], a calibrated prestrain p sets opposing equilibrium and branch stresses:

EQ: h<sub>0</sub>(0) = E<sub>∞</sub>p, &nbsp; h<sub>j</sub>(0) = −h<sub>0</sub>(0)E<sub>j</sub>/∑<sub>k</sub>E<sub>k</sub>, &nbsp; ∑<sub>j=0</sub><sup>23</sup>h<sub>j</sub>(0) = 0. &nbsp; (4)

For a traction-free material point, zero stress at the end of an increment gives

EQ: Δε<sup>m</sup> = −(h<sub>0</sub><sup>n</sup> + ∑<sub>j</sub>A<sub>j</sub>h<sub>j</sub><sup>n</sup>)/(E<sub>∞</sub> + ∑<sub>j</sub>E<sub>j</sub>B<sub>j</sub>),<br/>A<sub>j</sub> = exp(−r<sub>j</sub>), &nbsp; B<sub>j</sub> = [1 − exp(−r<sub>j</sub>)]/r<sub>j</sub>. &nbsp; (5)

Here r<sub>j</sub> = Δξ/τ<sub>j</sub>; the branch update is linear in reduced-time strain over each step. The equilibrium branch gains E<sub>∞</sub>Δε<sup>m</sup> and each Maxwell branch gains its exponential update. A separate Python implementation checks stress balance, a single-arm analytical solution, reversibility of an unprogrammed point and the temperature guard. Adding an eigenstrain for the same release would double count recovery.

The example p = 0.056175 is a bilayer-curvature calibration for a specific active-layer printing/activation condition, not a measured coupon contraction. The source example uses E<sub>∞</sub> = 10.5981 MPa before table rounding. A numerical 23→75 °C ramp over 30 s, 10 s hold and 10 s cooling to 23 °C is examined with 8–512 subdivisions per phase. The source spring program starts at 22 °C; using 23 °C keeps this material-point check inside the admitted range. No spring geometry prediction is claimed.

### 2.4. Fixture kinematics and three-dimensional stop reference

The candidate coupon is 60 mm × 10 mm × 4 mm and the opposed plates are 70 mm × 20 mm × 5 mm. These dimensions are design choices; only the coupon geometry is borrowed from [10]. Let h<sub>0</sub> be specimen thickness, g<sub>0</sub> total initial free clearance, U the change in unloaded inner spacing and e the signed nonthermal free thickness strain. For a flat centered specimen under uniform temperature,

EQ: c = g<sub>0</sub> + U − h<sub>0</sub>[α<sub>p</sub>ΔT + e], &nbsp; e<sub>crit</sub> = (g<sub>0</sub> + U)/h<sub>0</sub> − α<sub>p</sub>ΔT. &nbsp; (6)

First touch requires e = e<sub>crit</sub>; compression requires further incompatible free growth. The three mounting idealisations are

EQ: U = 0; &nbsp; U = (h<sub>0</sub> + g<sub>0</sub>)ε<sub>s</sub>; &nbsp; U = −2bε<sub>s</sub>. &nbsp; (7)

They correspond to fixed inner spacing, freely expanding inner spacers and fixed outer plate faces, with plate thickness b. The 304/4301 supplier interval-mean expansion of 16.0 µm m⁻¹ K⁻¹ over 20–100 °C [11] is treated as constant and rebased to 23 °C. This is a screening approximation, not a measured fixture tolerance or a pointwise tangent coefficient. Ninety deterministic combinations of six temperatures, five clearances and three mounts are calculated without assigning a recovery value.

The limiting elastic case e = 0 is independently checked in ANSYS at g<sub>0</sub> = 0.020 mm. A half-thickness SOLID185 solid and coupled planar top displacement represent the uniform full-area response; a rigid normal stop uses CONTA178 with normal Lagrange contact and an explicit Z normal [13]. The constant equilibrium modulus is a reference choice, not a measured hot elastic modulus. Twelve heating/cooling load states are prescribed; load index is not physical time. Analytical separation, normal force and contact state are compared using 10⁻⁷ mm gap and 10⁻⁴ N force tolerances. No surface pressure distribution, plate bending, friction, thermal contact or initial curvature is inferred from this reduced boundary problem.

### 2.5. Measurement operators and physical validation gates

For later released-surface extraction, orthogonal least squares fits a plane to predefined material points. Its normal n minimizes squared perpendicular distances; translation and rotation do not change the resulting metrics:

EQ: d<sub>i</sub> = (x<sub>i</sub> − x̄) · n, &nbsp; W<sub>max</sub> = max<sub>i</sub>|d<sub>i</sub>|, &nbsp; W<sub>RMS</sub> = √[(1/N)∑<sub>i</sub>d<sub>i</sub><sup>2</sup>]. &nbsp; (8)

The implementation rejects degenerate surfaces and passes rigid-transform and known-saddle tests. Equal nodal weights match Eq. (8); area weights define a separately labelled metric. Signed dimensions use distances between corresponding material fiducials along declared reference directions, not rotation-sensitive bounding boxes. These algorithms have no production field to process. Hot, cooled-under-restraint and post-release states must remain distinct.

Published data are reserved separately from calibration. Lluch-Cerezo et al. [7] provide Ultimaker means at one hold duration; Suder et al. [8] provide independent Prusament means at 80 °C but different printing/support conditions. The spring height data in [6] involve Prusament active layers and Dutch Filament passive layers, whereas the later model assigns matching spectra. Neither dataset establishes the bulk printed initial state or measures the proposed fixture's pressure and residual stress. No calibration is performed on these reserved observations. Physical MAE, RMSE or R² are therefore not reported, and model-based process optimization is not admitted.

### 3. Results
### 3.1. Constitutive verification

{{NONISO_RESULT}}

IMAGE: figures/master/nonisothermal.png
CAPTION: Figure 1. Independent scalar reference and actual ANSYS samples during the restrained thermal cycle, with time-increment error at fixed shift-table spacing. Near-zero stress makes relative error alone unsuitable. These are constitutive checks, not a measured annealing response.

The existing thermal benchmark retains a maximum sampled absolute error of 0.00518 °C. Its prior mesh and time refinements, six structural/contact cases and isothermal Prony check remain available in Supplementary Tables S5–S10. They are not rerun as independent evidence and do not qualify a three-dimensional production mesh. The new transient results extend the temperature-shift verification; they do not establish the thermal transport or initial state of a printed coupon. Tables S13–S16 record the new attempts and numerical comparisons; Table S17 contains the complete kinematic screen.

### 3.2. Contact feasibility and boundary-condition dependence

At 80 °C, 0.020 mm clearance and 4 mm thickness, the critical signed recovery strain is +0.1124% for fixed inner spacing, +0.2041% for expanding inner spacers and −0.1156% for fixed outer faces. Thus zero nonthermal thickness change leaves the first two configurations open and loads the third. All three corrected ANSYS stop cases pass their twelve gap, force and state checks. The fixed-outer-face reference carries 7.350 N at 80 °C and loses contact during cooling. The positive load is a consequence of the specified mount; it does not demonstrate a physical fixture benefit.

IMAGE: figures/master/contact.png
CAPTION: Figure 2. Mount-dependent contact feasibility at 0.020 mm total clearance. Panel (a) shows the signed recovery threshold; panel (b) compares the analytical and ANSYS elastic stop forces on heating. Expanding inner spacers and fixed inner spacing both remain open in this zero-recovery reference. Prescribed equal temperatures isolate kinematics and do not represent equal oven programs.

For the expanding-spacer model at 80 °C and 0.010 mm gap, thickness contraction exceeding approximately 0.0462% avoids closure in the flat uniform-temperature screen. Thickness growth instead promotes engagement. At the original reference temperature, a flat shape requires e ≥ g<sub>0</sub>/h<sub>0</sub> to span the opening. A bowed part can contact one plate before this full-thickness condition; a compliant plate changes the opening after contact. Consequently, these thresholds cannot replace a three-dimensional evolving surface calculation.

### 3.3. Recovery calculation and empirical limits

The initialized equilibrium stress and Maxwell stresses balance at zero resultant. The uniaxial single-arm reduction approaches its independent analytical recovery solution under refinement. For the source-conditioned 23-arm example, 512 subdivisions per phase give end-heating mechanical strain −0.056136 and cooled strain −0.056175. The latter is the programmed long-time limit, not a newly identified experimental shrinkage. The unprogrammed traction-free point returns to zero total strain after cooling.

IMAGE: figures/master/recovery.png
CAPTION: Figure 3. Phase-end mechanical strain in the programmed-road calculation. Agreement with the programmed limit checks the internal-state implementation; it does not validate a coupon's initial condition. All values are reproducible numerical calculations rather than laboratory observations.

Independent literature observations challenge any direction-independent recovery assumption. At 80 °C, Suder et al. [8, Table 2] report thickness growth while the other measured dimensions shorten. Their modified dog-bones, printing at 215 °C with 0.2 mm layers, and perforated support differ from the laminate calibration. Fitting the programmed coefficient to those final dimensions and scoring them again would be circular. No released coupon dimensional change, warpage, residual stress or distributed contact pressure has therefore been predicted in this study.

### 4. Discussion

The useful result is the dependence of contact on the complete mechanical support path. Specifying plate alloy and nominal gap without specifying stops can reverse the contact outcome even with an identical uniform temperature. The dimensionless ratio g<sub>0</sub>/h<sub>0</sub> is a necessary geometric descriptor, but it is insufficient without signed free dimensional change and the change in opening. This motivates measuring hot clearance and the unrestrained surface envelope before running a large treatment matrix. It does not establish a preferred plate material, gap or holding time.

The programmed-road model resolves a conceptual deficiency of an initially relaxed Maxwell material: zero external stress does not imply zero stored internal strain. Its implementation can release a print-conditioned state without adding a duplicate phenomenological annealing strain. Transfer to an ordinary coupon remains uncertain because road direction, through-thickness variation, aging and processing affect that state. The source coefficient was inferred from bilayer curvature, and the independent spring architecture uses two formulations. Neither a one-axis coefficient nor its agreement with its own asymptote supplies a bulk tensor or a validation error.

The thermal and non-isothermal tests isolate numerical components. A production thermal cycle would additionally require compatible conductivity and heat capacity, oven convection, radiation decisions and fixture heat transfer. Measured part temperatures could support a narrower structural reproduction, but they would not establish a general oven-to-part prediction. Likewise, a normal stop can suppress a particular displacement only after engagement; in-plane strain transfer depends on friction and support. Without initial curvature or a supported heterogeneous mechanism, manufacturing warpage cannot be inferred by deliberately breaking symmetry.

All reported discretization differences are deterministic numerical checks. The ninety gap scenarios are not a probability sample, and the alternative mounts are different designs rather than uncertainty bounds. No physical-input distributions were invented. Sparse final dimensions at one duration do not separately identify the rate and saturation of a recovery law, and matching geometry would not validate residual stresses. Production sensitivity, uncertainty intervals, Pareto solutions and independent confirmation therefore remain unresolved. An optimizer operating on the present reference cases would optimize the benchmark assumptions rather than annealing performance.

The achieved scope is a numerical verification and feasibility contribution. The proposed manufacturing study requires formulation- and print-matched free recovery histories, initial geometry, measured part/fixture temperatures, controlled clearance and independent released-shape observations. A full production mesh/time/contact study must then be conducted on that model. The present result does not justify a publication-readiness claim for a validated processing article, and no exclusive priority is asserted for the elementary contact relations.

### 5. Conclusions

1. Restricting the material to its 23–85 °C characterization envelope avoids unsupported 95/110 °C extrapolation but does not identify the printed coupon's initial state.

2. {{NONISO_CONCLUSION}}

3. At 80 °C and 0.020 mm clearance, three plausible mounting idealisations yield critical thickness strains of +0.112%, +0.204% and −0.116%. Mounting details therefore change whether nominally identical clearances engage.

4. Thirty-six sampled states from the corrected three-dimensional elastic stop problems satisfy the predeclared gap, force and contact-state checks. The 7.350 N fixed-outer-face force at 80 °C is a reference response, not a predicted annealing pressure.

5. Balanced internal stresses reproduce a programmed-road contraction toward 5.6175% while preserving zero external traction. This verifies the initialized mechanism, not its applicability to a homogeneous coupon.

6. Independent physical validation, production warpage/stress predictions and a robust processing window remain unestablished. The archived code and evidence identify the additional physical inputs required before these claims can be tested.

### Data availability

Numerical input decks, solver logs, scalar exports, processed comparisons, literature observation registers and claim manifests are available in the FDM-Annealing repository at https://github.com/VorteXEkansh/FDM-Annealing. Superseded and failed attempts remain traceable. Publisher PDFs are not redistributed. Supplementary Information preserves the earlier verification/property tables with their original reference key and adds the new calculations. Source coefficients and generated reference values are distinguished from experimental observations.

### Code availability

Python scripts reproduce the analytical comparisons, stored-strain recovery, kinematic screen, surface metrics and figures. Full solver repetition requires compatible licensed ANSYS; the reference environment is Student 2026 R1. Binary scratch/result archives retained locally are optional for checking the distributed scalar exports. The reproduction instructions record the exact software and the distinction between a supported numerical calculation and a physical prediction.

### Declarations

The author names and affiliation are retained from the supplied project. Authorship contributions, corresponding-author information, funding and competing interests require confirmation by the named authors before submission. Language-model assistance was used for literature screening, code development, numerical auditing and manuscript drafting. It is not an author or an independent experimental source. No new physical specimens or laboratory measurements were generated for this study. Human scientific review and author approval remain required.

### References

{{REFERENCES}}
