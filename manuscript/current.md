# Gap-controlled constraint during sub-melting annealing of FFF-printed PLA
## A computational thermo-mechanical research framework

Aadit Jain · Dheeraj Yadav · Ekansh Malhotra

Production and Industrial Engineering, Delhi Technological University

Computational manuscript draft · 12 September 2026

### Abstract

Annealing of fused-filament-fabricated (FFF) polylactic acid (PLA) raises a coupled question: how can geometric restraint limit distortion without transferring unacceptable stress into the part? This study is formulated around quantified clearance between a printed part and a mechanical fixture during sub-melting thermal treatment. The proposed ANSYS investigation will resolve heating, holding, cooling and fixture release, with signed directional dimensional change and out-of-plane warpage as primary responses. Contact pressure, fixture reactions and residual stress will describe the mechanical cost of restraint. Candidate annealing temperatures of 80 °C, 95 °C and 110 °C and hold durations of 30 min, 60 min and 90 min are retained as design choices; their applicability remains conditional on the selected PLA and constitutive evidence. The framework separates reversible expansion from history-dependent recovery, numerical verification from physical validation, and deterministic parameter effects from uncertainty. Independent published observations must be reserved for validation before calibration, and multi-objective ranking will require verified solver responses and declared acceptance criteria. This draft establishes the computational formulation and evidence requirements. No ANSYS results, validated material law, convergence findings or optimum are reported. The intended contribution is a reproducible assessment of the clearance–distortion–stress trade-off rather than an experimental strength claim.

Keywords: fused filament fabrication; PLA; annealing; fixture clearance; thermo-mechanical modeling; contact; warpage; numerical verification

### 1. Rationale and scope

Post-print thermal treatment can alter the dimensional and mechanical response of FFF thermoplastics. Butt and Bhaskar investigated annealing in several printed thermoplastic systems [1]. Their study motivates material-specific assessment rather than treating a thermal cycle as a universal improvement. Stojković et al. investigated layer height, annealing temperature and time together with strength and dimensional accuracy [2]. These studies support retaining geometric response alongside mechanical considerations; neither supplies validation of the plate fixture proposed here.

The present research concerns a virtual printed PLA body restrained by opposed fixture surfaces. The key controlled quantity is the initial free clearance, not an unspecified clamp force or a binary “supported” label. A physically meaningful comparison must account for contact activation, fixture expansion, friction and release. A small shape deviation while the part remains inside the fixture is insufficient evidence of stable final geometry.

The study is computational. Physical tensile testing, flexural confirmation and a new specimen campaign are outside its methodology. Strength enhancement will not be inferred from a thermal-stress simulation.

<!-- PAGE -->
### 1.1. Literature context and limits of transfer

Published annealing studies provide candidate mechanisms and possible comparison datasets, but different grades, print architectures and temperature histories cannot be pooled as though they described the same material. The experimental variables in [2] illustrate why geometry and prior processing must accompany an annealing condition. A temperature–duration pair alone is not a complete specification of the material state or boundary conditions.

ASTM F3489-23 identifies material handling and static mechanical evaluation considerations for polymer material extrusion [3]. It is relevant when appraising published material data and their comparability. It does not certify a thermal-contact simulation, supply a PLA constitutive law or establish the accuracy of predicted recovery. The standard designation and official title used here correct the inconsistent entry in the base proposal.

Granular and mould-based support concepts in the base paper remain background candidates for later source appraisal. They are not interchangeable with opposed plate contact: a confining medium has its own thermal and mechanical behavior. This draft does not import their reported outcomes into the computational model.

### 2. Research questions and objectives

The central question is whether a quantified range of fixture clearance can reduce released dimensional error and warpage while avoiding unfavorable contact and residual-stress responses under a specified sub-melting thermal history. The current literature selection motivates this question but does not establish that no prior study has addressed it.

1. Define a reproducible virtual geometry, material orientation, reference clearance and thermal–mechanical boundary description for an ANSYS analysis.
2. Quantify directional dimensional change, warpage and contact/stress response after numerical verification of the relevant solution quantities.
3. Assess predictive adequacy against independently reserved, compatible literature observations, distinguishing calibration from validation.
4. Evaluate the influence and uncertainty of material history, thermal boundaries and fixture/contact parameters using justified ranges or distributions.
5. Identify conditional multi-objective trade-offs using traceable solver evidence and confirm selected candidates with additional genuine computations.

### 2.1. Testable propositions

P1. Changing clearance can change released warpage and directional dimensions relative to an otherwise comparable unconstrained case. An effect must exceed the numerical resolution of the comparison before it is interpreted.

P2. Suppression of deformation during contact need not persist after release; geometric improvement may coexist with increased contact loading or residual stress. Both in-fixture and released states must therefore be examined.

P3. Temperature and hold duration may interact with clearance through evolving material response and contact. Ranking stability must be evaluated against uncertain inputs; a monotonic trend or central optimum is not assumed.

These are untested propositions. Repeating an identical deterministic solution does not generate independent experimental replication or justify a significance test.

<!-- PAGE -->
### 3. Computational domain and controlled constraint

The candidate domain comprises a PLA body and two opposed fixture surfaces separated by stops. A full three-dimensional body is preferred unless a reduced model can retain the deformation modes of interest. The part dimensions, surface landmarks, fixture dimensions, material grade and build/raster axes remain to be selected against available validation evidence. No CAD model or mesh is represented as completed.

Let x and y denote reference in-plane material axes and z the thickness direction. Define h<sub>0</sub> as the initial part thickness and H<sub>0</sub> as the separation between the effective opposing contact surfaces at the common reference temperature T<sub>ref</sub>. Release films, if represented, must be included in those effective surfaces or modeled as separate layers without double-counting their thickness. The total initial clearance and its dimensionless form are

EQ: g<sub>0</sub> = H<sub>0</sub> − h<sub>0</sub>, &nbsp;&nbsp; γ = g<sub>0</sub>/h<sub>0</sub>. &nbsp;&nbsp; (1)

A symmetric initial placement assigns half the total clearance to each face. A gravity-seated arrangement places the part on the lower surface and assigns the available clearance above it. These configurations are mechanically distinct and must be identified in each case. Figure 1 illustrates only the symmetric geometric definition.

FIGURE: gap

CAPTION: Figure 1. Initial clearance definition for opposed fixture surfaces. Schematic, not to scale; no mesh, simulated deformation or solver result is shown. The illustration assumes symmetric placement only.

The base proposal's single hot allowance is replaced by a parameterized reference gap. Thermal expansion of the plates and stops, plate compliance and part deformation determine subsequent local separation. No numerical clearance levels, friction coefficients, contact conductance or preload are assigned here. Bonding the specimen faces or prescribing zero displacement over them would eliminate the intended gap-controlled mechanism.

The unconstrained comparison removes the upper restraining surface while explicitly documenting any lower support and gravity. Numerical rigid-body stabilization must not suppress shrinkage, lateral slip or bowing. Symmetry conditions require justification; they must not exclude asymmetric warpage by construction.

<!-- PAGE -->
### 3.1. Thermal design and reporting states

Table 1 retains the thermal levels requested from the base proposal. They are planned inputs, not measured histories, solver outputs or recommended processing settings. Their sub-melting applicability must be checked for the selected grade and source-supported model range.

TABLE: Thermal design choices
Factor | Candidate levels | Interpretation
Annealing temperature | 80 °C; 95 °C; 110 °C | Inherited design choices; no established optimum
Hold duration | 30 min; 60 min; 90 min | Inherited choices; attainment rule still required
Constraint | Unconstrained; gap-controlled fixture | Explicit contact and support definitions required
Initial clearance | Not selected | Continuous geometric parameter; bounds need justification

The three temperature and three duration levels define nine thermal combinations before clearance, verification or uncertainty cases are added. This is design arithmetic, not a count of completed simulations. The total run count is not yet fixed.

Heating ramps, environmental temperature, convection, possible radiation, cooling and release must be specified with units and source or design justification. Hold time will be distinguished from total exposure: a criterion based on the part temperature field must define attainment. That criterion and its band are not yet fixed. Temperatures used in absolute-temperature laws must be converted consistently to kelvin.

A process comparison can apply the same external thermal cycle to constrained and unconstrained domains, allowing part histories to differ. A separate thermally matched comparison is needed to isolate mechanical restraint from fixture-induced thermal lag. The two comparisons answer different questions and must not be conflated.

### 4. Material response and intended ANSYS formulation

The intended implementation couples transient thermal analysis to history-dependent structural analysis with contact. Sequential temperature transfer is a candidate only when mechanical feedback on heat transfer is negligible or acceptably bounded. If contact opening materially alters thermal conductance, an iterated or coupled strategy must be justified. ANSYS availability, version, elements and solution controls have not yet been established.

For a continuum description, a candidate heat balance is

EQ: ρc<sub>p</sub> ∂T/∂t = ∇ · (k ∇T) + q. &nbsp;&nbsp; (2)

Here ρ is density, c<sub>p</sub> specific heat capacity, k the conductivity tensor, and q a volumetric heat source, if justified. The symbol t denotes time throughout. Property temperature dependence and any crystallization heat must be supported by evidence; omitting a source term is a model assumption to evaluate, not proof that the underlying mechanism is absent.

<!-- PAGE -->
### 4.1. Irreversible response and identifiability

A small-strain bookkeeping form, useful before selecting an implementation, is

EQ: ε = ε<sup>e</sup> + ε<sup>th</sup> + ε<sup>v</sup> + ε<sup>a</sup>, &nbsp;&nbsp; ∇ · σ + ρb = 0. &nbsp;&nbsp; (3)

The terms denote elastic strain, reversible thermal strain, time-dependent mechanical strain and an annealing-related recovery/transformation strain, respectively; σ is stress and b is body acceleration. This is a candidate decomposition, not a calibrated constitutive equation. Its terms must be defined so that the same relaxation or transformation is not counted twice. Finite-deformation kinematics are needed if the observed strains or rotations invalidate the small-strain approximation.

A stress-free body with reversible thermal expansion alone returns to its initial dimensions after a closed, unloaded thermal cycle. Permanent annealing distortion therefore cannot be claimed from that model merely by applying an oven temperature. A physically justified description of recovery, initial stress, inelastic deformation or structural evolution is required. Conversely, importing a fitted free-shrinkage strain and a residual-stress field that encode the same recovery would risk double-counting.

Required evidence includes temperature-dependent thermal properties, directional stiffness where appropriate, thermal expansion, time-dependent response and the initial printed state. A phenomenological recovery law may be usable within a declared domain, but its parameters must be identifiable and its calibration data distinguished from independent observations. Literature cannot be mixed across neat, filled and modified PLA without an explicit transfer argument and uncertainty treatment.

### 4.2. Contact and release

For ideal unilateral normal contact, local gap g<sub>n</sub> and compressive pressure p<sub>n</sub> satisfy

EQ: g<sub>n</sub> ≥ 0, &nbsp;&nbsp; p<sub>n</sub> ≥ 0, &nbsp;&nbsp; g<sub>n</sub>p<sub>n</sub> = 0. &nbsp;&nbsp; (4)

These ideal conditions explain the mechanism; an actual contact algorithm permits a controlled numerical approximation that must be verified. Frictional traction, contact stiffness and heat transfer require documented choices. Contact pressure is an output rather than a synonym for initial clearance. Sharp edges can produce mesh-sensitive local stress maxima, so both local and spatially averaged quantities need declared extraction rules.

Cooling must retain the intended fixture contact until the specified release event. Final responses are evaluated after release and equilibration at T<sub>ref</sub> at a declared elapsed time. The release temperature, post-release duration and material relaxation state remain open choices. Reports must distinguish hot in-fixture deformation, cooled constrained geometry and final released geometry.

<!-- PAGE -->
### 5. Dimensional and mechanical response definitions

Use identical material landmarks or consistently defined feature sets before and after treatment. Let d<sub>i,0</sub> and d<sub>i,f</sub> be the reference and final lengths associated with i ∈ {x, y, z}; these may represent length, width and thickness. Remove rigid translation and rotation through a declared alignment before measuring directional dimensions. Do not allow a change of bounding-box orientation to masquerade as recovery.

EQ: Δd<sub>i</sub> = d<sub>i,f</sub> − d<sub>i,0</sub>, &nbsp;&nbsp; δ<sub>i</sub> = 100 Δd<sub>i</sub>/d<sub>i,0</sub>. &nbsp;&nbsp; (5)

Positive δ<sub>i</sub> denotes expansion and negative δ<sub>i</sub> denotes contraction. δ<sub>i</sub> is the numerical percentage, reported with %. A scalar summary is

EQ: E<sub>RMS</sub> = √[(δ<sub>x</sub><sup>2</sup> + δ<sub>y</sub><sup>2</sup> + δ<sub>z</sub><sup>2</sup>)/3]. &nbsp;&nbsp; (6)

E<sub>RMS</sub> has the same percentage convention. It must accompany all signed components; it cannot reveal whether a part contracted in-plane and grew through its thickness.

If τ<sub>i</sub> is the positive allowed absolute dimensional deviation for axis i, a tolerance-normalized metric is

EQ: E<sub>tol</sub> = √[⅓ ∑<sub>i∈{x,y,z}</sub> (Δd<sub>i</sub>/τ<sub>i</sub>)<sup>2</sup>]. &nbsp;&nbsp; (7)

No numerical tolerances are assigned here. Passing the aggregate criterion alone is insufficient: each individual |Δd<sub>i</sub>| must satisfy its own τ<sub>i</sub>. Dimensions relative to initial geometry and deviations from a manufacturing drawing are distinct; a future application must identify which target its tolerances refer to.

For a designated surface region S, fit a plane Π by an area-weighted least-squares rule to the final released surface, then define

EQ: w = max<sub>X∈S</sub> |r<sub>⊥</sub>(X, Π)|. &nbsp;&nbsp; (8)

Here r<sub>⊥</sub> is signed normal distance to Π, and w is a length. This best-fit-plane warpage removes rigid tilt and is not the same as maximum nodal displacement, datum-based deviation or minimum-zone flatness. Comparison with published warpage requires the same convention, evaluation region and state; incompatible definitions must not be silently equated.

Mechanical diagnostics will include the contact-pressure history, reactions and cooled/released stress fields with a declared stress measure. A von Mises value alone is not an anisotropic PLA failure criterion or a prediction of tensile strength. No allowable pressure or stress is assumed without material evidence. Part-temperature histories must retain extraction location, time and reference frame.

<!-- PAGE -->
### 6. Numerical verification and independent validation

Verification must establish that the implemented equations and discretization produce sufficiently resolved responses. It cannot establish that those equations represent a particular printed material. No mesh, time-step or contact convergence has been performed in this stage.

### 6.1. Verification protocol

First check units, heat balance, force balance, temperature transfer and rigid-body treatment. Limiting cases should include free reversible thermal expansion and contact remaining inactive at a sufficiently open gap. A reversible cycle can serve as an implementation check; its zero permanent recovery must not be presented as validated annealing behavior.

Spatial refinement must track directional dimensions, warpage, contact loading and the selected stress measures while retaining the same physical setup. Time-step refinement must resolve ramps, contact transitions and release. Changes in nonlinear tolerances, penalty stiffness or stabilization require separate assessment so their influence is not mistaken for mesh convergence. Relative differences near a vanishing response require an absolute scale or tolerance.

Convergence acceptance levels will be declared before interpreting results and related to the smallest effect or tolerance being discussed. A grid-convergence estimate is appropriate only when its assumptions are supported; non-monotonic refinement must be reported. Failed cases and unconverged fields cannot enter optimization as valid data.

### 6.2. Calibration and independent evidence

Published data may calibrate a material law or test a prediction, but using the same observations for both does not provide independent validation. Reserve validation observations and document that separation before fitting. Independence should be checked by source and specimen/condition lineage, not merely by using different rows exported from the same fitted dataset.

Compatibility requires matching or bounding material grade, print architecture, geometry, support, thermal cycle, cooling/release and response definition. Values digitized from a figure require the figure/panel identity, axis units, digitization procedure and uncertainty. A publication's fitted model or literature compilation is not automatically an independent experimental target.

Validation should report prediction–observation discrepancy together with numerical and observational uncertainty and a declared acceptance rationale. Dimensional agreement does not validate unobserved contact stress. An unconstrained comparison can support recovery behavior but does not by itself validate a constrained-contact prediction. Qualitative trends offer weaker evidence than compatible quantitative observations.

If no adequate independent constrained dataset can be found, the manuscript must retain that limitation and restrict the claim. Agreement obtained by altering parameters after viewing reserved observations requires a new independent test. No validation data have yet been extracted or accepted.

<!-- PAGE -->
### 7. Sensitivity, uncertainty and multi-objective decisions

The intended analysis separates numerical error, uncertain inputs and model discrepancy. Candidate uncertain quantities include recovery-law parameters, initial state, expansion, relaxation, heat transfer, fixture gap and friction. Their bounds, dependence and probability distributions must come from sources or explicit engineering assumptions. A convenience range is not a measured distribution.

Sensitivity analysis will examine which inputs control each response and whether temperature, duration and clearance interact. The analysis method and sample design will be selected after the model and input evidence are established. A local perturbation measures a local effect, not a global sensitivity index. No sensitivity coefficients, indices or uncertainty bands are reported here.

When only plausible bounds exist, report scenario or interval results with those bounds. Probabilistic coverage requires a justified probabilistic model; deterministic case scatter is not an experimental confidence interval. Surrogate approximation error must be assessed separately from uncertainty propagated through the physical model.

### 7.1. Conditional decision problem

Let the design vector contain annealing temperature, hold duration and initial clearance. The candidate objectives are to minimize dimensional error, released warpage and an appropriately defined residual-stress measure. Contact-pressure limits and thermal/material admissibility may act as constraints only after their thresholds are justified. Cycle time may be included when an application defines its role. Strength and stiffness improvement are not optimization objectives in the absence of validated models for them.

Pareto comparison retains conditions for which no other feasible condition is no worse in every objective and better in at least one. Report the raw responses with any ranking; numerical uncertainty can make apparent dominance unresolved. A shorter or milder treatment with little distortion is not evidence of useful material improvement. An application requiring annealing benefit needs an independently supported benefit criterion before a processing recommendation is defensible.

An optional desirability score can provide a transparent preference rule following the multiple-response approach of Derringer and Suich [4]:

EQ: D = [∏<sub>j=1</sub><sup>m</sup> d<sub>j</sub><sup>ωⱼ</sup>]<sup>1/(∑ⱼ ωⱼ)</sup>, &nbsp;&nbsp; ω<sub>j</sub> &gt; 0, &nbsp;&nbsp; 0 ≤ d<sub>j</sub> ≤ 1. &nbsp;&nbsp; (9)

Here d<sub>j</sub> is a response desirability and ω<sub>j</sub> its positive preference weight; m is the number of scored responses. Limits and weights must be declared before selecting a preferred design. Report component desirabilities and vary defensible preferences to assess ranking stability. No weights or computed scores have been chosen.

Candidates selected through a surrogate must be recomputed with the genuine solver and assessed against the same verification and feasibility requirements. Such recomputation confirms the numerical candidate, not physical validity. This stage reports neither a Pareto front nor an optimum.

<!-- PAGE -->
### 8. Evidence status, engineering relevance and limitations

The current contribution is the conversion to an explicit computational research question, consistent response definitions and a traceable evidence structure. Table 2 identifies what remains necessary before numerical findings can be reported. Missing evidence is not represented by zero values, example contours or synthetic data.

TABLE: Evidence required for reportable findings
Claim family | Current evidence | Admission requirement
Temperature and deformation | No ANSYS runs | Archived model, input sources, solver outputs and logs
Stress and contact pressure | No model or fields | Verified contact solution and declared extraction rules
Numerical convergence | Not performed | Genuine mesh/time/contact refinement evidence
Physical predictive validity | No accepted dataset | Independent compatible observations and uncertainty
Sensitivity and uncertainty | Not calculated | Justified inputs and reproducible numerical analysis
Optimization | Not performed | Verified responses, feasibility rules and solver confirmation

A reliable prediction of released geometry could support decisions for planar guides, locating features and similar tolerance-sensitive parts. This is potential utility, not demonstrated qualification. A selected gap would remain conditional on part dimensions, fixture material, heating/cooling history, initial printed state and the validated material domain. No cost saving, production reliability or service-safety claim follows from the present framework.

Material identifiability is the principal scientific limitation. Sparse final dimensions may not uniquely distinguish residual-stress relaxation, directional recovery and crystallization-related effects. A calibrated law may match those dimensions while predicting different stresses. Contact and thermal boundaries introduce additional uncertainty, and a homogenized continuum may omit road-scale deformation or damage. These limitations must constrain the interpretation of later computed fields.

The candidate temperature range has not been verified for a selected PLA formulation. Long-term aging, moisture response, fatigue, creep in service, damage and tensile strength are not established. Geometry transfer requires further evidence, and one best-fit-plane warp value cannot demonstrate that every critical feature meets a drawing requirement.

### 9. Conclusions

The base experimental proposal has been restructured into a computational investigation of quantified gap-controlled annealing. The formulation retains signed directional response, warpage, thermal design levels and multi-response decision logic while making fixture clearance, thermal history, constitutive recovery and release explicit.

The defensible next numerical claims depend on genuine ANSYS execution, verified material evidence, discretization assessment and independent literature-based validation. Until those requirements are met, the study supports a research formulation and reproducibility protocol only. No improvement, validated prediction or preferred annealing condition is concluded.

<!-- PAGE -->
### References

[1] J. Butt and R. Bhaskar. Investigating the Effects of Annealing on the Mechanical Properties of FFF-Printed Thermoplastics. <i>Journal of Manufacturing and Materials Processing</i> 4(2), 38 (2020). <link href="https://doi.org/10.3390/jmmp4020038" color="#24576b">doi:10.3390/jmmp4020038</link>.

[2] J. R. Stojković, R. Turudija, N. Vitković, F. Górski, A. Păcurar, A. Pleşa, A. Ianoşi-Andreeva-Dimitrova and R. Păcurar. An Experimental Study on the Impact of Layer Height and Annealing Parameters on the Tensile Strength and Dimensional Accuracy of FDM 3D Printed Parts. <i>Materials</i> 16(13), 4574 (2023). <link href="https://doi.org/10.3390/ma16134574" color="#24576b">doi:10.3390/ma16134574</link>.

[3] ASTM International. <i>Standard Guide for Additive Manufacturing of Polymers — Material Extrusion — Recommendation for Material Handling and Evaluation of Static Mechanical Properties</i>. ASTM F3489-23 (2023). <link href="https://doi.org/10.1520/F3489-23" color="#24576b">doi:10.1520/F3489-23</link>.

[4] G. Derringer and R. Suich. Simultaneous Optimization of Several Response Variables. <i>Journal of Quality Technology</i> 12(4), 214–219 (1980). <link href="https://doi.org/10.1080/00224065.1980.11980968" color="#24576b">doi:10.1080/00224065.1980.11980968</link>.

### Supplement A. Provenance and reproducibility requirements

The project repository is <link href="https://github.com/VorteXEkansh/FDM-Annealing" color="#24576b">VorteXEkansh/FDM-Annealing</link>. It contains the base-paper audit, the manuscript restructuring map, the complete current source and the authoritative research-state record. The base paper is preserved separately from the evolving manuscript. No solver dataset is available in this stage.

Each future case must preserve a unique identifier, the solver version, geometry and material orientation, input configuration, source references, units, boundary histories, mesh, time-integration and contact settings, execution status, raw-output location and file checksums. Failed cases remain in the record with their failure reason. Postprocessing must identify both the raw field and the script/equation producing each response.

Every quantitative result will be assigned to one of three evidence classes: A, genuine solver output; B, a reproducible numerical calculation; or C, a verified published source with an exact locator. Design choices remain labeled as inputs, never as findings. The temperatures and durations in Table 1 are inherited design choices; its nine-combination count follows directly from three temperature levels multiplied by three duration levels.

The bibliography is deliberately limited to the checked sources cited in this draft. The larger bibliography in the base proposal is archived for later appraisal and is not treated as a validated material database. No published numerical property, deformation value or uncertainty estimate is adopted here without extraction and applicability assessment.

Author names and affiliation follow the supplied base paper. Authorship contributions, funding and submission declarations require author confirmation before journal submission; no such declarations are inferred here.
