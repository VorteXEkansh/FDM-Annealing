# Numerical verification of a thermo-mechanical framework for gap-constrained annealing of FFF-printed PLA

Aadit Jain · Dheeraj Yadav · Ekansh Malhotra

Production and Industrial Engineering, Delhi Technological University

Computational research manuscript · 30 September 2026

### Abstract

Quantified fixture clearance is a potential means of controlling deformation during annealing of fused-filament-fabricated polylactic acid, but prediction requires compatible material data and verified thermal, mechanical and contact implementations. This study develops and numerically verifies components of such a framework using Ansys Mechanical APDL 2026 R1. A formulation-specific, 23-branch generalized-Maxwell reference is combined with separate thermal, structural and contact benchmarks. The transient plane-wall comparison gives a maximum temperature error of 0.005180700 °C and maximum excursion-relative error of 0.157660518%. Six structural/contact reference cases pass 114 scalar comparisons; the isothermal Prony calculation has maximum stress error 3.8271 × 10⁻⁶ MPa. Refinement from a 90 × 12 to a 120 × 16 structural grid changes benchmark warpage by 0.9327% and interior residual stress by 2.0266%. A 40-to-60-element normal-Lagrange contact refinement changes mean pressure by 0.12698%, with zero reported penetration. These results verify declared numerical configurations, not production annealing behavior. Compatible thermal functions, bulk irreversible strain, a non-isothermal ANSYS adapter and independent physical validation remain incomplete. Consequently no production clearance benefit, processing optimum or uncertainty interval is established. The contribution is a reproducible verification foundation and an explicit account of the evidence still required for predictive constrained-annealing analysis.

<b>Keywords:</b> fused filament fabrication; polylactic acid; annealing; fixture clearance; numerical verification; viscoelasticity; contact

<!-- PAGE -->
### 1. Introduction

Thermal post-processing of FFF-printed PLA can alter dimensions and mechanical response [1,2,27,28]. Geometric support introduces an additional constraint: suppressed deformation during a hot hold need not persist after cooling and release. Predicting released dimensions therefore requires the actual thermal history, history-dependent material response and evolving contact, with validation specific to the observable being claimed.

The primary research question is how temperature, attained-temperature holding time and initial fixture clearance influence transient exposure, irreversible dimensional response, warpage and residual stress relative to free annealing. A rectangular coupon and opposed-plate fixture define the intended comparison. This article reports the numerical verification achieved so far and distinguishes it from production predictions that the available material and validation evidence cannot yet support.

The objectives are to establish traceable material and geometry definitions, verify component calculations, quantify discretization effects, assess independent validation readiness and delimit defensible sensitivity and decision analysis. The achieved contribution is component verification with immutable solver evidence. Prediction of a clearance–distortion–stress trade-off remains an unachieved objective. No first-use claim is made for supported annealing, ANSYS, Prony series or optimization.

### 2. Background and research gap

Supported annealing is established. Powder-mould experiments [11], treatment in different media [12], mould-supported processing [26], salt-assisted remelting [25] and tough-PLA encapsulation [24] preclude novelty claims based solely on support. High-heat PLA conditioning [13], porosity/interlayer studies [29] and crystallization/bonding competition [30] show why grades and print architectures must not be pooled as interchangeable evidence. Remelting is outside the proposed sub-melting domain.

Wijnen et al. [6] modeled deformation and examined annealing dimensions; Trofimov et al. [7] compared thermal and distortion predictions with experiments. Bute et al. [5] separated irreversible directional strain from subsequent-cycle expansion and related recovery to ANSYS printing stresses. Issabayeva and Shishkovsky [9] used viscoelastic representations, while Chapuis et al. [8] developed a pre-strain/Maxwell laminate model for thermally activated shape change. Temperature shifting [31], relaxation measurements [22] and viscoelastic–viscoplastic characterization [21] support history dependence but do not independently validate a bulk fixture-constrained coupon.

Orthotropic FFF mechanics [16], thermal/deformation calculations [10], composite crystallization modeling [15], thermal mesh adaptation [32] and finite-difference thermal studies [37] establish relevant component methods. Virgin/processed PLA crystallization [17], nucleation [18], filament kinetics [19], deformation-assisted annealing [20], phase-field mechanics [33] and injection-moulded grade comparisons [34] provide context rather than transferable coefficients. Constitutive calibration must retain formulation, initial state, architecture and temperature-domain compatibility.

Annealing optimization [23], multiscale FE/desirability analysis [14] and physics-informed recycled-PLA optimization [35] precede this work. Derringer–Suich desirability [4] is established methodology, not evidence of physical validity. ASTM F3489-23 [3] supports appraisal of material-extrusion mechanical data; it does not certify a simulation or supply an annealing law.

The targeted review covers verified records through 12 September 2026; it is not an exhaustive search through this revision date. In the accessible evidence, no study was identified demonstrating the entire chain of quantified annealing-fixture clearance, evolving contact, irreversible directional response and independently supported released geometry/stress with uncertainty. This is a bounded search finding, not proof of absence. Supplementary Table S1 compares the ten closest studies. The proposed gap remains an evidence requirement, not an achieved predictive capability.

<!-- PAGE -->
### 3. Computational methodology
### 3.1. Research framework

The workflow separates material characterization, numerical verification, discretization assessment, independent physical validation and production inference. Actual field solutions in this article are reference problems. The full coupon/fixture annealing model is not executable with the present evidence, and no production campaign was run. Missing values remain unavailable rather than zero.

Mechanical APDL reports release 2026 R1, build 26.1, update 20260202 with the Ansys Mechanical Enterprise Academic Student product. Workbench and Mechanical executables report 26.1. The batch workflow uses explicit case files and input/output hashes. Student limits reported for this release are 128,000 nodes/elements and up to four HPC cores [40]. The host has eight physical cores, 16 logical processors and 15.82 GiB RAM. PyMechanical is not used; installed DesignXplorer/optiSLang were not exercised. Claims are limited to the capabilities actually run.

### 3.2. Geometry

The intended solid coupon is 60 mm × 10 mm × 4 mm, adopting only the regular-plate dimensions in Trofimov et al. [7, Fig. 4(a)]. Their Raise3D properties and validation outcomes are not transferred to Prusament PLA. Two candidate AISI 304 plates each measure 70 mm × 20 mm × 5 mm, leaving a 5 mm plan margin on each side. A geometry-only Mechanical APDL build created three volumes; it contains no element type, mesh, material, load, analysis type or solve command.

The total initial clearance and normalized clearance are defined at a common reference temperature by

EQ: g<sub>0</sub> = H<sub>0</sub> − h<sub>0</sub>, &nbsp;&nbsp; γ = g<sub>0</sub>/h<sub>0</sub>. &nbsp;&nbsp; (1)

Here H₀ is the inside plate spacing and h₀ is specimen thickness. The initially centered coupon has half the clearance above and below. Geometry screening uses γ = 0, 0.0025, 0.005, 0.01 and 0.02, corresponding to g₀ = 0, 0.01, 0.02, 0.04 and 0.08 mm. These are design choices, not approved treatment levels or predictions of contact onset. FREE omits the fixture; it is not the zero-gap contact condition.

FIGURE: gap
CAPTION: Figure 1. Candidate coupon and opposed-plate geometry at the reference state. The schematic contains no solved mesh, temperature, contact or deformation field.

### 3.3. Material properties

Prusament PLA is the formulation-specific constitutive reference. Chapuis et al. [8, supplementary Tables B.1–B.2] provide E<sub>∞</sub> = 10.598 MPa, ν = 0.35, α = 68.0 µm m⁻¹ K⁻¹, T<sub>g</sub> = 65 °C and 23 branch pairs. Direct characterization spans 23–85 °C. The source-calculated instantaneous modulus is 1691.594 MPa. Supplementary Table S2 retains the full spectrum. Supplier density of 1240 kg m⁻³ has no reported test temperature [36] and remains screening information, not an admitted production law.

Compatible temperature-dependent Prusament functions remain absent for k(T) and c<sub>p</sub>(T). A complete orthotropic property set, initial printed stress, bulk recovery law and crystallization parameters are absent. Other formulations [5,16,22,37] remain comparators. Supplier modulus intervals and same-source bilayer identification brackets are not bulk annealing distributions. No cross-grade uncertainty envelope is assigned.

AISI 304 is the candidate fixture material [38, Table 1]. Its reported density, heat capacity, conductivity, expansion, modulus and Poisson ratio are tabulated at 20 °C, 100 °C and 200 °C (Supplementary Table S3). Implemented interpolation is

EQ: p(T) = p<sub>a</sub> + (p<sub>b</sub> − p<sub>a</sub>)(T − T<sub>a</sub>)/(T<sub>b</sub> − T<sub>a</sub>). &nbsp;&nbsp; (2)

The code reproduces knots and rejects extrapolation. The expansion table's tangent-versus-mean convention and reference temperature remain unresolved; interpolation therefore does not authorize fixture thermal strain.

### 3.4. Constitutive model

The executable material-point core is small-strain isotropic linear viscoelasticity with constant Poisson ratio. Its strain partition is

EQ: ε = ε<sup>e</sup> + ε<sup>ve</sup> + ε<sup>th</sup>,<br/>ε<sup>m</sup> = ε − ε<sup>th</sup>. &nbsp;&nbsp; (3)

This matches the update routine. Effective elastic strain is instantaneous compliance applied to stress; delayed strain is mechanical strain minus that elastic contribution. No bulk irreversible-strain evolution term is implemented. Its absence is a limitation, not a physical zero assigned to production PLA. The separate imposed-eigenstrain benchmark does not supply such a law.

Reversible expansion and isotropic stiffness are

EQ: ε<sup>th</sup>(T) = α(T − T<sub>r</sub>)I,<br/>α = 68.0 × 10<sup>−6</sup> K<sup>−1</sup>. &nbsp;&nbsp; (4)

EQ: C(E,ν) : A = 2G A + λ tr(A)I,<br/>G = E/[2(1 + ν)], &nbsp; λ = Eν/[(1 + ν)(1 − 2ν)]. &nbsp;&nbsp; (5)

I is the identity tensor, T<sub>r</sub> the reference temperature, A a symmetric strain tensor, G the shear modulus and λ the Lamé parameter. The code uses tensor shear; engineering-shear interfaces require conversion. The three-dimensional isotropic extension of the source laminate model is an assumption, not measured FFF isotropy.

In reduced time ξ, the network, Prony normalization and isothermal relaxation modulus are

EQ: σ = C<sub>∞</sub> : ε<sup>m</sup> + ∑<sub>i=1</sub><sup>23</sup> s<sub>i</sub>,<br/>∂s<sub>i</sub>/∂ξ + s<sub>i</sub>/τ<sub>i</sub> = C<sub>i</sub> : ∂ε<sup>m</sup>/∂ξ. &nbsp;&nbsp; (6)

EQ: E<sub>inst</sub> = E<sub>∞</sub> + ∑<sub>i=1</sub><sup>23</sup> k<sub>i</sub>, &nbsp; g<sub>i</sub> = k<sub>i</sub>/E<sub>inst</sub>,<br/>G<sub>inst</sub> = E<sub>inst</sub>/[2(1 + ν)], &nbsp; K<sub>inst</sub> = E<sub>inst</sub>/[3(1 − 2ν)]. &nbsp;&nbsp; (7)

EQ: E<sub>r</sub>(t,T) = E<sub>∞</sub> + ∑<sub>i=1</sub><sup>23</sup> k<sub>i</sub> exp[−t/(a<sub>T</sub>τ<sub>i</sub>)]. &nbsp;&nbsp; (8)

Branch stresses are sᵢ, relaxation times τᵢ and source tensile moduli kᵢ. Equal fractional shear and bulk spectra preserve constant ν. E<sub>r</sub> is the isothermal relaxation modulus. Temperature changes the clock; no separate modulus multiplier is added. Native ANSYS spectra were checked only at 65 °C [39], without shifting.

The source piecewise clock and reduced time are

EQ: log<sub>10</sub>a<sub>T</sub> = C₃(1/T<sub>K</sub> − 1/T<sub>g,K</sub>), &nbsp; T &lt; T<sub>g</sub>;<br/>log<sub>10</sub>a<sub>T</sub> = −C₁(T − T<sub>g</sub>)/[C₂ + (T − T<sub>g</sub>)], &nbsp; T ≥ T<sub>g</sub>. &nbsp;&nbsp; (9)

EQ: ξ(t) = ∫<sub>0</sub><sup>t</sup> [a<sub>T</sub>(T(s))]<sup>−1</sup> ds. &nbsp;&nbsp; (10)

C₁ = 17.4, C₂ = 51.6 K and C₃ = 35 000 K [8]; T<sub>K</sub> and T<sub>g,K</sub> are kelvin temperatures. The base-10 shift multiplies reference relaxation times. The code rejects values outside 23–85 °C and splits ramps at 65 °C. Composite Simpson quadrature integrates the clock for a linear temperature path; this utility is distinct from the frozen-temperature substep update.

For strain linear in reduced time, the implemented update is

EQ: r<sub>i</sub> = Δξ/τ<sub>i</sub>, &nbsp; A<sub>i</sub> = exp(−r<sub>i</sub>),<br/>B<sub>i</sub> = [1 − exp(−r<sub>i</sub>)]/r<sub>i</sub>,<br/>s<sub>i</sub><sup>n+1</sup> = A<sub>i</sub>s<sub>i</sub><sup>n</sup> + B<sub>i</sub>C<sub>i</sub> : Δε<sup>m</sup>. &nbsp;&nbsp; (11)

The exponential difference is evaluated accurately near zero. The physical-time update uses midpoint temperature to approximate reduced-time increments; it is exact for an isothermal linear-strain segment and requires refinement for a changing temperature. No verified full non-isothermal ANSYS adapter exists. Positive moduli and times support the isothermal reference, not validity under arbitrary strain, duration or annealing history.

### 3.5. Thermal formulation

The executed transient conduction reference solves

EQ: ρc<sub>p</sub> ∂T/∂t = ∇ · (k ∇T). &nbsp;&nbsp; (12)

Here ρ, c<sub>p</sub> and k are density, heat capacity and conductivity. The verified problem uses constant fixtures and convection, specified in Section 3.9. Radiation is omitted from this benchmark to retain an analytical comparison. Production still needs compatible thermal functions, physical convection, a radiation decision and thermal-contact conductance; no absent coefficient is replaced by zero.

### 3.6. Mechanical formulation

The static reference cases solve small-strain equilibrium without body force,

EQ: ∇ · σ = 0. &nbsp;&nbsp; (13)

Uniform expansion, imposed eigenstrain and isothermal memory are isolated before contact is introduced. Production extraction would require fixed landmarks, aligned signed dimensions and a declared cooled/released state. The three-dimensional dimensional-error and best-fit-plane extractors are not implemented and are not presented as executed equations. The convergence benchmark instead measures the maximum normal residual from a fitted line along a deformed two-dimensional top edge.

### 3.7. Annealing strain

No bulk annealing-induced irreversible-strain relation is parameterized. Prusament programmed pre-strains refer to thin bilayers [8]; another grade's directional strain [5] is not transferable. Explicit evidence-gap errors prevent production use of absent laws. Initial stress and a recovery field cannot be combined without checking identifiability and double-counting.

No crystallization kinetic equation is included. Compatible initial state and non-isothermal kinetics are lacking [17–20]; an isothermal Avrami law is not evaluated instantaneously along a temperature ramp. Reversible expansion, finite-time delayed deformation and irreversible distortion remain distinct.

### 3.8. Fixture and contact

Ideal unilateral normal contact satisfies

EQ: g<sub>n</sub> ≥ 0, &nbsp; p<sub>n</sub> ≥ 0, &nbsp; g<sub>n</sub>p<sub>n</sub> = 0. &nbsp;&nbsp; (14)

Positive g<sub>n</sub> denotes separation and p<sub>n</sub> compressive pressure. CONTA178 node-to-stop and two-dimensional CONTA172/TARGE169 models verify limited forms of this relation. Penalty enforcement permits numerical penetration; normal-Lagrange comparison supplies the reported zero-penetration solution. Production three-dimensional fixture contact, friction, spacers and heat transfer are incomplete. A stiff plate is neither infinitely rigid nor thermally inert.

### 3.9. Boundary conditions

The thermal reference is a 1 mm × 1 mm × 10 mm wall with adiabatic side faces and equal convection on its two z faces. Numerical fixtures are k = 0.5 W m⁻¹ K⁻¹, c<sub>p</sub> = 1000 J kg⁻¹ K⁻¹, ρ = 1000 kg m⁻³ and h = 5 W m⁻² K⁻¹. The body starts at 20 °C. Ambient temperature rises to 80 °C during 0–300 s, holds through 900 s, falls to 20 °C through 1200 s and remains there through 1800 s. Half-thickness is 0.005 m and Bi = 0.05. These are numerical verification inputs, not a measured PLA cycle.

Intended FREE surfaces are traction-free with verified rigid-body stabilization. GAP is initially centered without preload. Gravity is omitted as an isolation assumption; symmetry must not suppress investigated warpage. Production convection, hold attainment, cooling, release and observation time remain unspecified. Same-oven and matched-part-temperature comparisons are distinct and neither exists as a solved production pair.

### 3.10. Mesh

The thermal reference uses SOLID70; uniform structural tests use one eight-node SOLID185 brick of 10 mm × 1 mm × 1 mm. Convergence is studied separately on a plane wall, a 60 mm × 4 mm two-layer Prony cantilever of unit thickness and a 10 mm × 4 mm plane-strain contact block with 0.020 mm stop gap. The 65 °C cantilever has an upper-layer relaxation-time multiplier of 10, a numerical fixture rather than a PLA property.

Structural refinement measures fitted-line warpage, residual displacement and the 95th percentile of interior element-centroid von Mises stress over 6 mm ≤ x ≤ 54 mm. Thermal refinement measures 300 s lag, gradient and profiles. Contact refinement measures pressures, reaction and penetration. Adjacent relative change is

EQ: δ<sub>q</sub> = |q<sub>fine</sub> − q<sub>medium</sub>| / |q<sub>fine</sub>| × 100%. &nbsp;&nbsp; (15)

A zero denominator leaves percentage change undefined. Two zero values establish only zero absolute change. Predeclared limits are 2% for global mesh responses and 5% for local stress/peak pressure. The full matrices remain archived. No production mesh is selected from these differently configured problems.

### 3.11. Time stepping

The thermal time-step study compares 5 s, 1 s, 0.25 s and 0.125 s on a 64-element wall. Structural refinement compares ramp/hold pairs 0.1/1 s, 0.05/0.5 s, 0.01/0.1 s and 0.005/0.05 s on a fixed 60 × 8 grid. The −0.001 N cantilever load rises over 0–1 s, holds through 31 s, unloads through 32 s and remains zero through 62 s. Limits are 1% for global time-step responses and 3% for local stress. The uniform Prony patch test needs finer ramp increments; settings are not transferred between problems.

### 3.12. Verification

The plane-wall center reference uses step response and Duhamel superposition,

EQ: S<sub>c</sub>(t) = 1 − ∑<sub>n=0</sub><sup>∞</sup> A<sub>n</sub> exp(−ζ<sub>n</sub><sup>2</sup>αt/L<sup>2</sup>), &nbsp; ζ<sub>n</sub> tan ζ<sub>n</sub> = Bi,<br/>A<sub>n</sub> = 4 sin ζ<sub>n</sub>/(2ζ<sub>n</sub> + sin 2ζ<sub>n</sub>), &nbsp; T<sub>c</sub>(t) = T<sub>i</sub> + ∫<sub>0</sub><sup>t</sup> S<sub>c</sub>(t − τ) dT<sub>∞</sub>(τ). &nbsp;&nbsp; (16)

In this equation α = k/(ρc<sub>p</sub>) is thermal diffusivity, distinct from the structural expansion coefficient; L is half-thickness. The implementation uses 200 roots and analytical integration over each linear ambient segment. The accepted comparison uses 640 elements, 1025 nodes, 40 elements through thickness and 0.25 s steps. Limits are 0.05 °C absolute error and 0.25% relative to the reference excursion from 20 °C; kelvin-based error is also retained.

Elastic/eigenstrain checks use E = 2000 MPa, ν = 0.3 and α = 10⁻⁵ K⁻¹ as fixtures. Transverse symmetry permits homogeneous Poisson response; the x = 0 face is restrained axially and the opposing face is coupled in x. Temperature cycles from 20 °C to 30 °C to 80 °C and back with ten substeps per ramp. For uniform free strain e, L = 10 mm and A = 1 mm², references are

EQ: u<sub>x</sub> = Le, σ<sub>x</sub> = 0 (free); &nbsp; u<sub>x</sub> = 0, σ<sub>x</sub> = −Ee (fixed);<br/>R<sub>x</sub> = −Aσ<sub>x</sub>, &nbsp; ε<sub>y</sub> = ε<sub>z</sub> = e − νσ<sub>x</sub>/E. &nbsp;&nbsp; (17)

Synthetic retained-eigenstrain tests add −0.001 isotropic strain through equivalent initialized stress, then compare fixed, free and released states. This is not a calibrated annealing law. Node contact adds a frictionless rigid stop at a 0.002 mm gap, with penetration/force tolerances 10⁻⁹ mm and 10⁻⁹ N. Reaction, displacement, force, status and opening are checked independently.

The Prony test uses all branches at 65 °C with the same thermal reference, avoiding shifting. Axial strain rises to 0.001 over 0–1 s, holds through 31 s, returns to zero through 32 s and remains zero through 62 s. A ramp on [a,b] at strain rate v contributes, for q = min(t,b) > a,

EQ: σ(t) = E<sub>∞</sub>v(q − a) + ∑<sub>i=1</sub><sup>23</sup> E<sub>i</sub>vτ<sub>i</sub>[exp(−(t − q)/τ<sub>i</sub>) − exp(−(t − a)/τ<sub>i</sub>)]. &nbsp;&nbsp; (18)

Eᵢ denotes the branch modulus kᵢ; loading and unloading contributions are summed. Accepted increments are 0.0001 s on ramps and 0.1 s on holds. Each scalar error must be no greater than 10⁻⁷ in its unit plus 0.1% of the reference magnitude. Zero references have undefined relative error. Held-zero-strain stress after unloading measures memory, not free recovery.

### 3.13. Independent validation

The primary reserved dataset is Lluch-Cerezo et al. [11, Table 5]: six mould-free conditions, each with signed length, width and height means from five specimens. Ultimaker Pearl White PLA bars measure 80 mm × 10 mm × 4 mm, with longitudinal roads, full infill and 0.2 mm layers; the furnace ramp is 10 °C min⁻¹ and treatment duration 120 min. Actual mould-free support, specimen/cooling histories and observation delay remain unresolved. Supplementary Table S4 preserves the 18 literature means.

Chapuis et al. [8] supply calibration and are excluded from independent validation. External targets have not guided fitting; reservation is prospective but not blinded. Tuning to a condition would reclassify its correlated directions as calibration. Three selected maxima from Stojković et al. [2] remain quarantined owing to sign, selection and measurement limitations. Powder-supported or remelting cases cannot validate the plate fixture.

For matched prediction pᵢ and observation yᵢ, implemented metrics are

EQ: eᵢ = pᵢ − yᵢ, aᵢ = |eᵢ|, rᵢ = 100aᵢ/|yᵢ| (yᵢ ≠ 0). (19)

EQ: MAE = (1/n)∑ᵢ aᵢ, RMSE = √[(1/n)∑ᵢ eᵢ²]. (20)

EQ: aᵢ ≤ b<sub>num, i</sub> + b<sub>meas, i</sub>. (21)

The inequality is a deterministic discrepancy screen using independent numerical and measurement bounds, not a confidence interval. Missing bounds make classification indeterminate. Directional percentage-change errors use percentage points. Responses and grades are not pooled, and R² is not used for sparse validation. Metric functions are tested but no matched ANSYS prediction exists.

### 3.14. Parametric design

Candidate temperatures are 80 °C, 95 °C and 110 °C, with holds of 30 min, 60 min and 90 min. Only 80 °C overlaps direct Prusament characterization; overlap alone does not validate recovery or duration. Higher temperatures are not admitted by extrapolation. Geometry gaps remain candidates. Production case registries contain no approved cases because physical validity and production convergence are incomplete. No representative dry run or campaign was executed.

### 3.15. Sensitivity and uncertainty

No surrogate or cross-validation score exists. Future fitting needs traceable production cases and held-out assessment grouped by physical condition; preprocessing and tuning belong inside training folds. FREE is a distinct boundary condition, and contact transitions require sufficient sampling. Training agreement alone cannot establish prediction quality.

Deterministic process variation is distinct from physical-input uncertainty. No admitted probability distribution exists for modulus, expansion, conductivity, heat capacity, irreversible strain, convection, friction or fixture expansion. Morris, Sobol and Latin-hypercube/Monte Carlo methods remain conditional on supported domains, joint inputs and estimator convergence; none was executed. Verification discretization, surrogate error and physical-model discrepancy cannot substitute for propagated physical uncertainty.

### 3.16. Optimization and confirmation

Only actual outputs could support minimizing released warpage, dimensional error and defined residual stress. Contact limits, cycle time and annealing-benefit criteria need justification. Tensile strength is excluded because no validated strength/fracture model exists. Equal, dimensional-fidelity and stress/contact priorities have no assigned scales or thresholds; desirability is not used.

A future sampled Pareto set remains conditional on feasibility, resolution and uncertainty. A recommendation, two feasible neighbors and a thermally matched FREE case would require frozen predictions followed by new refined ANSYS runs. Identical oven programs do not establish thermal matching. No selection, processing window or confirmation error exists.

### 4. Results
### 4.1. Verification

All solver results below are numerical reference responses, not production PLA coupon predictions or independent physical validation. The plane-wall maximum absolute error is 0.005180700 °C, maximum kelvin-based error 0.001700533% and maximum excursion-relative error 0.157660518%, meeting both limits. Four preceding attempts remain archived: extraction failure, two rejected time-step comparisons and a file-mapping termination.

Six structural/contact cases pass all 114 comparisons. Maximum axial-displacement and gap errors are 2.331 × 10⁻¹⁴ mm and 9.500 × 10⁻¹¹ mm. Contact is open at 30 °C, closed at 80 °C and open after cooling. Free elastic cycling recovers original dimensions; the imposed-eigenstrain case retains its prescribed contraction. These are implementation findings, not PLA shrinkage measurements.

TABLE: Structural reference checks: selected genuine outputs
Case and state | ANSYS value | Analytical value
Free, 80 °C: axial displacement | 0.006000000 mm | 0.006000000 mm
Fixed, 80 °C: axial stress | −1.200000048 MPa | −1.200000000 MPa
Fixed, 80 °C: left reaction | 1.200000000 N | 1.200000000 N
Free, cooled: axial displacement | 0 mm | 0 mm
Retained strain, cooled free: displacement | −0.010000000 mm | −0.010000000 mm
Retained strain, cooled fixed: stress | 2.000000000 MPa | 2.000000000 MPa
Retained strain, released: displacement | −0.010000000 mm | −0.010000000 mm
Contact, 80 °C: axial displacement | 0.002000000 mm | 0.002000000 mm
Contact, 80 °C: normal force | −0.800000012 N | −0.800000000 N
Contact, cooled: open separation | 0.002000000095 mm | 0.002000000000 mm

The Prony reference has maximum stress error 3.8271 × 10⁻⁶ MPa, maximum relative stress error 0.019740% and maximum reaction error 3.8280 × 10⁻⁶ N. The earlier 0.01 s ramp attempt failed the fixed criterion and remains archived. Negative stress after unloading is held-strain memory. Detailed thermal and Prony comparisons are in Supplementary Tables S5 and S6.

### 4.2. Mesh convergence

Initial medium-to-fine structural changes were 9.9345% for warpage, 7.9763% for displacement and 29.8796% for stress, requiring further refinement. The 90 × 12 grid then passed against 120 × 16. The 32-element thermal grid passed against 64, and the normal-Lagrange 40-element interface against 60.

TABLE: Selected verification meshes and confirmation changes
Configuration | Selected / confirmation grid | Confirmation changes, δ<sub>q</sub>
Two-layer Prony cantilever | 90 × 12 / 120 × 16 elements | W<sub>max</sub> 0.9327%; displacement 0.5821%; σ<sub>res,95</sub> 2.0266%
Plane-wall thermal field | 32 / 64 elements through thickness | 300 s lag 0.0009423%; gradient 0.0060073%
Normal-Lagrange contact | 40 / 60 interface elements | Mean pressure 0.12698%; peak pressure 0.36127%; reaction 0.13831%

IMAGE: figures/publication/mesh_convergence.png
CAPTION: Figure 2. Genuine MAPDL mesh-refinement responses for numerical structural, thermal and surface-contact configurations. Every point traces to an archived solver run; no point is a production annealing prediction.

These selections apply only to the benchmark configurations. Twenty-eight unique runs populate the convergence tables; all 43 technical directories, including 15 excluded attempts, remain archived. No production mesh or time step is selected.

### 4.3. Time-step convergence

TABLE: Selected verification time increments and confirmation changes
Configuration | Selected / confirmation increments | Confirmation changes, δ<sub>q</sub>
Plane-wall thermal history | 0.25 s / 0.125 s | Lag 0.005285%; gradient 0.005369%; profile L₂ 0.002811%; profile RMSE 0.00202088 °C
Two-layer structural history | 0.01/0.1 s / 0.005/0.05 s ramp/hold | W<sub>max</sub> 0.003094%; displacement 0.003213%; σ<sub>res,95</sub> 0.13636%

IMAGE: figures/publication/timestep_convergence.png
CAPTION: Figure 3. Thermal and structural time-step verification. The thermal profile comparison gives RMSE = 0.00202088 °C. Confirmation changes satisfy the predeclared benchmark limits.

Contact-control variation is distinct from discretization. At F<sub>KN</sub> = 10, an edge element is open and the all-elements-closed screen fails despite convergence. Penalty and augmented-Lagrange solutions coincide only for the declared monotonic frictionless benchmark. Under the same augmented-Lagrange F<sub>KN</sub> = 1 control, increasing μ from 0 to 0.3 changes mean pressure from 17.5368 to 20.0334 MPa and peak pressure from 24.4284 to 51.8788 MPa (Supplementary Table S7). This is numerical-fixture sensitivity, not a measured PLA–steel friction effect.

IMAGE: figures/publication/contact_sensitivity.png
CAPTION: Figure 4. Contact-control responses in the numerical fixture. Penalty stiffness and friction are declared perturbations rather than sourced production interface parameters. Algorithm differences must be retained when comparing cases.

### 4.4. Validation

All six source-specific cases were rejected before ANSYS launch because compatible material, initial-state, thermal/support and implementation inputs are incomplete. All 18 reserved means have blank predictions/errors. No recalibration was performed. This is missing-input rejection, not poor prediction–measurement agreement or physical validation. Imposing observed shrinkage as an input would destroy independence. Production sweeps remain blocked.

### 4.5. Thermal response

No production part/fixture temperature history or gradient was computed. Plane-wall agreement establishes only its constant-property convection problem.

### 4.6. Free annealing

No production FREE solution exists. Free expansion and imposed-eigenstrain patch tests do not replace it.

### 4.7. Fixture-clearance effect

No matched FREE–GAP pair exists. Geometry construction and node-stop closure do not quantify released dimensional preservation.

### 4.8. Temperature effect

No production ranking is available; 95 °C and 110 °C remain outside the constitutive reference envelope.

### 4.9. Holding-time effect

No 30 min, 60 min or 90 min production hold was solved. Isothermal reference relaxation cannot establish their comparative performance.

### 4.10. Coupled response

Thermal–contact–recovery interactions remain uncomputed because the non-isothermal model, initial state and interfaces are incomplete.

### 4.11. Dimensional stability

No signed production dimensional change, combined error or suppression percentage exists. Reserved external means remain literature observations.

### 4.12. Warpage

Fitted-line warpage is a two-layer cantilever response, not released three-dimensional coupon best-fit-plane warpage.

### 4.13. Residual stress

Benchmark interior stress and held-strain Prony memory do not quantify production residual stress after cooling and release.

### 4.14. Contact pressure

Only reference pressures exist. No production pressure field, contact area, onset temperature or fixture reaction was predicted.

### 4.15. Sensitivity

No production global sensitivity indices or process-interaction estimates exist. Contact-control perturbations are verification cases.

### 4.16. Uncertainty

No propagated interval exists. Supplier intervals, method brackets and reference mesh differences are not confidence limits on a production prediction.

### 4.17. Optimization

No Pareto front, nondominated processing condition, preference ranking or robust window was computed. Empty registries record unavailable analysis, not established infeasibility.

### 4.18. Confirmation

No recommendation, neighbor or matched FREE point was selected. No new confirmation run or prediction error exists; reference refinements do not confirm an optimum.

### 5. Discussion

The findings support implementation-level confidence for specified thermal, elastic, imposed-eigenstrain, isothermal viscoelastic and contact problems. They also demonstrate why solver completion is insufficient: early time increments missed criteria, contact-control placement required correction, and one converged case failed its closure screen. Preserving these attempts prevents successful terminal status from being mistaken for adequacy.

The evidence does not yet answer the clearance–distortion–stress question. Initial printed state and irreversible strain are central: reversible expansion does not supply an absent annealing mechanism, and finite-time delayed deformation is not necessarily irreversible. Combining recovered pre-strain, initial stress and crystallization distortion without identification could count the same response twice. The implemented relaxation clock likewise cannot be multiplied by an unrelated modulus-reduction curve without justification.

Fixture engagement can alter thermal exposure and restraint. Attribution requires actual specimen/plate histories, resolved gap and contact status, pressure and penetration. Lower hot displacement need not imply lower released warpage. Fixture expansion, release relaxation and response state remain essential. No production mechanism, inconvenient trend or beneficial clearance is asserted because those fields do not exist.

Validation is blocked by compatibility, not demonstrated failure of finite elements to reproduce PLA. Prusament DMA parameters cannot supply Ultimaker recovery, furnace setpoint cannot reconstruct unknown cooling, and geometric agreement alone cannot validate stress or pressure. Reserved observations expose missing links before fitting. Verification convergence and surrogate agreement cannot replace independent physical validation.

Limitations include small-strain isotropy, absent thermal/recovery functions, unknown fixture expansion convention and unresolved boundaries. Orthotropy, crystallization and finite rotations require evidence and implementation rather than decorative equations. Sand/salt remains literature context; no discrete-element model or new physical experiment is claimed. The contribution is reproducible verification, not manufacturing qualification, strength enhancement or optimized treatment.

### 6. Conclusions

Seven quantitative findings are supported by archived numerical reference cases:

1. The plane-wall maximum absolute temperature error is 0.005180700 °C and maximum excursion-relative error 0.157660518%, below the declared 0.05 °C and 0.25% limits.
2. Six structural/contact cases pass 114 comparisons, with maximum displacement and gap errors of 2.331 × 10⁻¹⁴ mm and 9.500 × 10⁻¹¹ mm.
3. The 23-branch isothermal Prony reference has maximum stress error 3.8271 × 10⁻⁶ MPa and relative stress error 0.019740%. This checks the 65 °C adapter, not non-isothermal recovery.
4. Structural refinement from 90 × 12 to 120 × 16 elements changes fitted-line warpage, displacement and interior stress by 0.9327%, 0.5821% and 2.0266%.
5. Thermal refinement from 32 to 64 through-thickness elements changes 300 s lag by 0.0009423% and gradient by 0.0060073%.
6. The 0.25 s versus 0.125 s thermal comparison changes lag by 0.005285% and gives profile RMSE 0.00202088 °C. Structural ramp/hold refinement from 0.01/0.1 s to 0.005/0.05 s changes warpage by 0.003094% and stress by 0.13636%.
7. Normal-Lagrange refinement from 40 to 60 interface elements changes mean pressure, peak pressure and reaction by 0.12698%, 0.36127% and 0.13831%, with zero reported penetration.

These results apply to numerical fixtures and do not establish production mesh adequacy, annealing benefit, physical predictive validity or optimum. The full computational annealing study remains scientifically incomplete. Compatible material/boundary evidence, non-isothermal implementation and independent validation must precede production inference, uncertainty propagation and processing recommendations.

### Data availability

The <link href="https://github.com/VorteXEkansh/FDM-Annealing" color="#24576b">FDM-Annealing repository</link> contains solver evidence, failed/superseded attempts, case definitions, extraction tables and SHA-256 manifests. Literature-derived observations retain source locations and calibration/validation roles. Production and optimization registries are header-only; there are no withheld production results.

### Code availability

Material relations, MAPDL deck generation, analytical references, metric functions, checks and the PDF builder are maintained in the repository. The manuscript equation map identifies actual implementations and their scope. Ansys is proprietary software; the recorded installation defines the solver environment. No claim is made that every model runs without it.

### Declarations

No new physical specimens, human participants or animal studies form part of this computational work. Names and affiliation are retained from the supplied base manuscript. Author contributions, corresponding-author details, funding and competing-interest declarations require author confirmation before submission; absence is not inferred. This is not a completed production-annealing or optimization article ready for submission.

<!-- PAGE -->
### References
[1] Javaid Butt, Raghunath Bhaskar. Investigating the Effects of Annealing on the Mechanical Properties of FFF-Printed Thermoplastics. <i>Journal of Manufacturing and Materials Processing</i> 4(2), 38 (2020). <link href="https://doi.org/10.3390/jmmp4020038" color="#24576b">doi:10.3390/jmmp4020038</link>.

[2] Jelena R. Stojković, Rajko Turudija, Nikola Vitković et al. An Experimental Study on the Impact of Layer Height and Annealing Parameters on the Tensile Strength and Dimensional Accuracy of FDM 3D Printed Parts. <i>Materials</i> 16(13), 4574 (2023). <link href="https://doi.org/10.3390/ma16134574" color="#24576b">doi:10.3390/ma16134574</link>.

[3] ASTM International. <i>Standard Guide for Additive Manufacturing of Polymers — Material Extrusion — Recommendation for Material Handling and Evaluation of Static Mechanical Properties</i>. ASTM F3489-23 (2023). <link href="https://doi.org/10.1520/F3489-23" color="#24576b">doi:10.1520/F3489-23</link>.

[4] George Derringer, Ronald Suich. Simultaneous Optimization of Several Response Variables. <i>Journal of Quality Technology</i> 12(4), 214-219 (1980). <link href="https://doi.org/10.1080/00224065.1980.11980968" color="#24576b">doi:10.1080/00224065.1980.11980968</link>.

[5] Irina BUTE, Sergejs TARASOVS, Jevgenijs SEVCENKO, Andrey ANISKEVICH. Thermomechanical Analysis and Numerical Simulations of Fused Filament Fabricated Polylactic Acid Parts. <i>Materials Science</i> 30(2), 217-225 (2024). <link href="https://doi.org/10.5755/j02.ms.35076" color="#24576b">doi:10.5755/j02.ms.35076</link>.

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

<!-- PAGE -->

### Supplementary information
### S1. Literature comparison and reproducibility tables

Literature values below are source evidence, not new experiments or solver findings. Full matrices, formulation flags and exact locators remain in the repository. Reference identities were checked against the existing bibliography; no literature search beyond the stated review cutoff is claimed.

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
32 | -0.0193833038 | -0.0193871309 | 0.0000038271
62 | -0.0045757745 | -0.0045757747 | 0.0000000001

SUPPTABLE: Contact-control sensitivity on the 40-element interface
Control | Maximum penetration (mm) | Mean / peak pressure (MPa)
Penalty or augmented, F<sub>KN</sub> = 0.1 | 1.12141 × 10<super>−3</super> | 16.9989 / 17.9426
Penalty or augmented, F<sub>KN</sub> = 1 | 1.52677 × 10<super>−4</super> | 17.5368 / 24.4284
Penalty or augmented, F<sub>KN</sub> = 10 | 1.80923 × 10<super>−5</super> | 17.6242 / 28.9476
Normal Lagrange, μ = 0 | 0 | 17.5721 / 21.3788
Augmented, F<sub>KN</sub> = 1, μ = 0.1 | 1.97427 × 10<super>−4</super> | 18.4343 / 31.5883
Augmented, F<sub>KN</sub> = 1, μ = 0.3 | 3.24243 × 10<super>−4</super> | 20.0334 / 51.8788

### S2. Evidence and reproduction boundaries

The literature matrix contains 34 journal studies. The base paper is immutable. Property records preserve units, temperatures, formulation, exact source location and use restrictions. Full convergence CSVs contain 39 mesh, 24 time-step and nine contact-control rows; these are response records, not independent experiments. All 43 technical convergence directories remain archived, including 15 excluded attempts.

Verification constants, load schedules, relaxation mismatch and clearance screens are design choices. The assembly construction is not a solved annealing model. The validation archive retains 45 published observations: 18 reserved means, 24 context records and three quarantined maxima. Prediction/error fields remain blank. Empty registries do not mean zero physical response.

Each run preserves input, script, command, raw output and extraction hashes. Corrections create new derived records or attempts; raw evidence is not overwritten. The supplementary files support numerical reproduction and do not supply missing physical validation.
