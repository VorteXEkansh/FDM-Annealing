# Gap-controlled constraint during sub-melting annealing of FFF-printed PLA
## A computational thermo-mechanical research framework

Aadit Jain · Dheeraj Yadav · Ekansh Malhotra

Production and Industrial Engineering, Delhi Technological University

Computational manuscript draft · 12 September 2026

### Abstract

Annealing of fused-filament-fabricated (FFF) polylactic acid (PLA) raises a coupled question: how can geometric restraint limit distortion without transferring unacceptable stress into the part? This study is formulated around quantified clearance between a printed part and a mechanical fixture during sub-melting thermal treatment. The proposed ANSYS investigation will resolve heating, holding, cooling and fixture release, with signed directional dimensional change and out-of-plane warpage as primary responses. Contact pressure, fixture reactions and residual stress will describe the mechanical cost of restraint. Candidate annealing temperatures of 80 °C, 95 °C and 110 °C and hold durations of 30 min, 60 min and 90 min are retained as design choices; their applicability remains conditional on the selected PLA and constitutive evidence. The framework separates reversible expansion from history-dependent recovery, numerical verification from physical validation, and deterministic parameter effects from uncertainty. Independent published observations must be reserved for validation before calibration, and multi-objective ranking will require verified solver responses and declared acceptance criteria. A literature investigation through 12 September 2026 identifies prior supported annealing, viscoelastic recovery models and annealing-related numerical optimization. The remaining contribution is provisionally narrowed to a quantified clearance–contact assessment after cooling and release. This draft establishes the computational formulation and evidence requirements. No ANSYS results, validated material law, convergence findings or optimum are reported. The intended contribution is a reproducible assessment of the clearance–distortion–stress trade-off rather than an experimental strength claim.

Keywords: fused filament fabrication; PLA; annealing; fixture clearance; thermo-mechanical modeling; contact; warpage; numerical verification

### 1. Rationale and scope

Post-print thermal treatment can alter the dimensional and mechanical response of FFF thermoplastics. Butt and Bhaskar investigated annealing in several printed thermoplastic systems [1]. Their study motivates material-specific assessment rather than treating a thermal cycle as a universal improvement. Stojković et al. investigated layer height, annealing temperature and time together with strength and dimensional accuracy [2]. These studies support retaining geometric response alongside mechanical considerations; neither supplies validation of the plate fixture proposed here.

The present research concerns a virtual printed PLA body restrained by opposed fixture surfaces. The key controlled quantity is the initial free clearance, not an unspecified clamp force or a binary “supported” label. A physically meaningful comparison must account for contact activation, fixture expansion, friction and release. A small shape deviation while the part remains inside the fixture is insufficient evidence of stable final geometry.

The study is computational. Physical tensile testing, flexural confirmation and a new specimen campaign are outside its methodology. Strength enhancement will not be inferred from a thermal-stress simulation.

<!-- PAGE -->
### 1.1. Evidence base and scope of the review

The literature investigation was updated through 12 September 2026 using publisher records, author repositories, Europe PMC full text and DOI registration metadata. The evidence matrix records 34 journal papers, their bibliographic verification, accessible methods, missing fields and intended use. This is a critical, targeted investigation, not a claim of exhaustive systematic-review coverage. DOI verification establishes bibliographic identity; it does not establish methodological quality, transferable properties or independent validation.

The closest work falls into three overlapping groups: supported thermal post-processing, prediction of printing or thermally activated deformation, and annealing-related mechanical optimization. The intersection matters more than any one keyword. A support medium is mechanically different from a plate fixture, printing-induced distortion differs from post-print recovery, and a thermodynamic constraint in a learning algorithm is not physical fixture restraint.

### 1.2. What annealing and support studies already establish

Wach et al. [27], Benwood et al. [28], Butt and Bhaskar [1], and Stojković et al. [2] establish substantial prior work on thermal post-treatment and printed-polymer response. Their findings motivate a material-specific balance between dimensional stability and mechanical behavior. They do not justify assuming that all PLA grades benefit from the same cycle. Work on porosity, crystallinity and interlayer adhesion [29], including competition between crystallization and bonding [30], further challenges a simple rule that greater crystallinity necessarily means a stronger printed part.

Constrained annealing has already been studied. Lluch-Cerezo et al. [11] compared alumina-powder mould support with unsupported treatment and measured directional dimensions and flexural behavior. Wijnbergen et al. [12] examined different annealing media for tough PLA, including sand. Mould-supported processing [26] and salt-assisted annealing/remelting [25] are additional precedents. Remelting outcomes belong to a different physical regime and cannot establish performance of the proposed sub-melting process.

Chiscop et al. [24] extended encapsulation-based thermal processing to several geometries using tough PLA. De Assis et al. [13] connected thermal conditioning, dimensional response and mechanical prediction for high-heat PLA. These formulations cannot be treated as interchangeable with neat PLA. Together, the studies rule out novelty based on support, dimensional preservation, annealing itself or combining dimensional and mechanical endpoints.

The powder-mould source also illustrates why exact extraction matters: its PLA treatment tables identify a final temperature of 155 °C, whereas its Table 7 labels the final PLA row 240 °C [11, Tables 2–3 and 7]. The inconsistent row is not accepted as validation data. A plausible correction is not a verified observation.

<!-- PAGE -->
### 1.3. Thermo-mechanical prediction and irreversible response

Wijnen et al. [6] developed a deformation model for printed PLA walls, calibrated thermal behavior and compared predicted curvature with measurements; they also examined directional annealing changes. Trofimov et al. [7] used sequential thermal and mechanical simulations and separate temperature and distortion comparisons. These are direct precedents for coupled process modeling and physical comparison. Ramos et al. [32] addressed computational efficiency and thermal validation through adaptive treatment of the deposition mesh.

Bute et al. [5] are particularly close to the present problem. They measured irreversible directional thermal strain and distinguished it from expansion during a subsequent thermal cycle. Their ANSYS printing simulations related residual thermal stress to observed recovery. Therefore, neither irreversible annealing strain nor an ANSYS connection between stress and deformation is new. Correlation with printing stress, however, does not by itself demonstrate a predictive annealing-contact law under a variable fixture clearance.

The shape-memory study of Issabayeva and Shishkovsky [9] incorporates thermomechanical characterization and ANSYS modeling with a Prony representation and temperature shifting. Chapuis et al. [8] provide an even stronger constitutive precedent: programmed pre-strain, a modified generalized Maxwell formulation and laminate finite elements predict thermally activated shape change and mechanical response. A first-use claim for temperature-dependent PLA recovery, Prony series, WLF shifting or viscoelastic finite elements would therefore be indefensible.

Temperature–relaxation shifting has a much older foundation in Williams, Landel and Ferry [31]. Its use still requires evidence that the chosen material is sufficiently thermorheologically simple over the modeled range. Relaxation measurements on printed PLA [22] and temperature-dependent viscoelastic–viscoplastic behavior [21] motivate testing the adequacy of a linear law rather than selecting one solely because ANSYS supports it. A fitted DMA curve does not independently validate released warpage or residual stress.

Jiang et al. [15] combined thermal, thermoelastic and crystallization-kinetic models for short-carbon-fibre/PLA printing. Farh and Gribniak [10] modeled printing, cooling and detachment with temperature-dependent behavior. Coupling crystallization with mechanics, or including a release stage, cannot be claimed as new in isolation. Composite-specific data and printing-bed detachment also cannot directly validate opposed-face annealing contact.

Thermal contact remains an evidence need. Existing printing models demonstrate the importance of the thermal boundary, but their bed conditions do not supply a measured conductance for the proposed PLA–fixture interface. Clearance may change both heat transfer and mechanical engagement. Prescribed uniform part temperature would omit that interaction; one-way thermal loading is defensible only if its adequacy is demonstrated.

<!-- PAGE -->
### 1.4. Anisotropy, crystallization and competing strain mechanisms

Li et al. [16] provide direct evidence and modeling of orthotropic FFF-PLA mechanics. Raster orientation, road spacing and interlayer architecture must therefore accompany a property dataset. The road air gap in a printing study is distinct from the free clearance between an annealing fixture and the finished part. Ambient directional stiffness alone also cannot define behavior throughout heating, holding and cooling.

Crystallization kinetics depend on thermal and processing history. Pantani et al. [17] compared virgin and processed PLA, while nucleation/kinetic work [18] and recent filament-focused analysis [19] supply candidate mechanisms. These studies support distinguishing cold crystallization of a printed state from crystallization after erasing its history by melting. Phase-field work [33] already connects thermal/morphological evolution to effective mechanics. Simultaneous deformation and annealing studies [20] additionally motivate checking whether mechanical restraint changes the kinetics assumed by the model.

Recent injection-moulded grade comparisons [34] address secondary shrinkage and mechanical trade-offs. Their online publication predates this review cutoff even though the assigned issue date is later. They are useful mechanistic context, but their initial state and manufacturing route differ from FFF. No kinetic coefficient, Prony term, shift constant or annealing-strain value is transferred into the present model at this stage.

The physical distinction is consequential: reversible expansion vanishes on return to the reference state, whereas recovery and crystallization-related strain can persist. A single effective expansion curve may reproduce one heating path yet fail after cooling or under restraint. Conversely, adding independently fitted recovery and crystallization terms risks counting the same measured strain twice. Identifiability must be assessed with more than a final dimension; thermal history and compatible time-resolved observations are needed where available.

### 1.5. Optimization is established; the decision target must differ

Kahya et al. [23] already optimized thermal annealing for printed PLA performance. More directly, Ben Amor and Souissi [14], published online in June 2026, combine multiscale finite elements, annealed/non-annealed PLA and multi-objective desirability. Their accessible publisher abstract concerns tensile behavior, raster orientation and strain rate. It does not establish prediction of released geometry under quantified annealing-fixture contact. The early unedited publication nevertheless decisively rules out claiming annealing plus finite elements plus optimization as a new combination.

A 2026 physics-informed learning study [35] also reports annealing-aware optimization of recycled PLA. Its “thermo-constrained” terminology refers to model/optimization restrictions rather than physical fixture contact. Repeated load-curve records must not be treated as independent specimens when appraising validation. Desirability itself is established methodology [4]; novelty must lie in the physical question and supported predictive capability, not the ranking formula.

<!-- PAGE -->
### 1.6. Closest competing studies and the remaining claim

The ten closest studies were selected by overlap with the intended physical response or computational mechanism, rather than citation count. The order below is an editorial grouping, not a calculated similarity score. The complete matrix records access limits and evidence locators.

TABLE: Closest competing studies and implications for scope
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

The broad proposed gap is narrowed. In the accessible evidence reviewed, no study was identified that demonstrates the complete chain of a quantified initial annealing-fixture clearance, evolving thermal/mechanical contact, irreversible directional response, and a verified assessment of released dimensions, warpage and residual stress with explicit uncertainty. This is a bounded search finding, not proof of absence or a claim of priority. Partial access to several competitors limits a stronger assertion.

The defensible intended contribution is a reproducible, evidence-tested evaluation of the clearance–distortion–stress trade-off for a specified FFF-PLA material and fixture. Integrating transient thermal exposure, a justified history-dependent material law and irreversible strain is a means to that end. The contribution remains conditional: it must be demonstrated by genuine computations, numerical verification and compatible independent observations. If stress or contact cannot be physically validated, those outputs must remain conditional model predictions, with validation claims restricted to supported observables.

ASTM F3489-23 [3] remains relevant to appraisal of polymer material-extrusion mechanical data. It does not certify the proposed simulation or provide an annealing constitutive law. Published support effects are literature findings, not results of this study.

<!-- PAGE -->
### 2. Research questions and objectives

The central question is whether a quantified range of fixture clearance can reduce released dimensional error and warpage while avoiding unfavorable contact and residual-stress responses under a specified sub-melting thermal history. The reviewed literature supports investigating this specific trade-off; it does not establish an unprecedented combination of annealing, finite elements and optimization.

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

Table 2 retains the thermal levels requested from the base proposal. They are planned inputs, not measured histories, solver outputs or recommended processing settings. Their sub-melting applicability must be checked for the selected grade and source-supported model range.

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

The current contribution is a critically delimited computational research question, a verified literature matrix, consistent response definitions and a traceable evidence structure. Table 3 identifies what remains necessary before numerical findings can be reported. Missing evidence is not represented by zero values, example contours or synthetic data.

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

The candidate temperature range remains unverified for a selected grade. Aging, moisture, fatigue, service creep, damage and strength are outside current evidence. Geometry transfer also requires validation.

### 9. Conclusions

The literature establishes prior supported annealing, irreversible strain analysis, thermo-viscoelastic finite elements and annealing-related optimization. The proposed contribution is therefore restricted to evidence-tested prediction of the clearance–distortion–stress trade-off after cooling and release, conditional on the remaining validation needs. The formulation retains signed directional response, warpage, thermal design levels and multi-response decision logic while making fixture clearance, thermal history, constitutive recovery and release explicit.

Numerical findings require genuine ANSYS execution, verified material evidence, discretization assessment and independent validation. No improvement, validated prediction or preferred annealing condition is concluded.

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


<!-- PAGE -->
### References (continued)

[9] Zhamila Issabayeva, Igor Shishkovsky. Prediction of The Mechanical Behavior of Polylactic Acid Parts with Shape Memory Effect Fabricated by FDM. <i>Polymers</i> 15(5), 1162 (2023). <link href="https://doi.org/10.3390/polym15051162" color="#24576b">doi:10.3390/polym15051162</link>.

[10] Mahmoud Farh, Viktor Gribniak. Thermo-Mechanical Approach to Material Extrusion Process During Fused Filament Fabrication of Polymeric Samples. <i>Materials</i> 18(19), 4537 (2025). <link href="https://doi.org/10.3390/ma18194537" color="#24576b">doi:10.3390/ma18194537</link>.

[11] Joaquín Lluch-Cerezo, María Desamparados Meseguer, Juan Antonio García-Manrique, Rut Benavente. Influence of Thermal Annealing Temperatures on Powder Mould Effectiveness to Avoid Deformations in ABS and PLA 3D-Printed Parts. <i>Polymers</i> 14(13), 2607 (2022). <link href="https://doi.org/10.3390/polym14132607" color="#24576b">doi:10.3390/polym14132607</link>.

[12] Diede Christine Wijnbergen, Merel van der Stelt, Luc Martijn Verhamme. The effect of annealing on deformation and mechanical strength of tough PLA and its application in 3D printed prosthetic sockets. <i>Rapid Prototyping Journal</i> 27(11), 81-89 (2021). <link href="https://doi.org/10.1108/rpj-04-2021-0090" color="#24576b">doi:10.1108/rpj-04-2021-0090</link>.

[13] Cleiton Lazaro Fazolo de Assis, Kelvin dos Santos Tiene, Gabriel Boni Magosse. Dimensional Stability and Mechanical Performance of Thermally Conditioned High‐Heat Polylactic Acid Parts Produced by Fused Filament Fabrication. <i>Polymer Engineering &amp; Science</i> 66(2), 941-958 (2026). <link href="https://doi.org/10.1002/pen.70250" color="#24576b">doi:10.1002/pen.70250</link>.

[14] Rania Ben Amor, Slim Souissi. Multiscale modeling and multiobjective optimization of the mechanical behavior of annealed and non-annealed material extrusion printed PLA. <i>Discover Materials</i>  (2026). <link href="https://doi.org/10.1007/s43939-026-00769-2" color="#24576b">doi:10.1007/s43939-026-00769-2</link>.

[15] Bingnong Jiang, Yuan Chen, Lin Ye et al. Residual stress and warpage of additively manufactured SCF/PLA composite parts. <i>Advanced Manufacturing: Polymer &amp; Composites Science</i> 9(1), 2171940 (2023). <link href="https://doi.org/10.1080/20550340.2023.2171940" color="#24576b">doi:10.1080/20550340.2023.2171940</link>.

[16] Meiyu Li, Yanan Xu, Jianguang Fang. Orthotropic mechanical properties of PLA materials fabricated by fused deposition modeling. <i>Thin-Walled Structures</i> 199, 111800 (2024). <link href="https://doi.org/10.1016/j.tws.2024.111800" color="#24576b">doi:10.1016/j.tws.2024.111800</link>.


<!-- PAGE -->
### References (continued)

[17] R. Pantani, F. De Santis, A. Sorrentino et al. Crystallization kinetics of virgin and processed poly(lactic acid). <i>Polymer Degradation and Stability</i> 95(7), 1148-1159 (2010). <link href="https://doi.org/10.1016/j.polymdegradstab.2010.04.018" color="#24576b">doi:10.1016/j.polymdegradstab.2010.04.018</link>.

[18] Felice De Santis, Roberto Pantani, Giuseppe Titomanlio. Nucleation and crystallization kinetics of poly(lactic acid). <i>Thermochimica Acta</i> 522(1-2), 128-134 (2011). <link href="https://doi.org/10.1016/j.tca.2011.05.034" color="#24576b">doi:10.1016/j.tca.2011.05.034</link>.

[19] Targol Hashemi, Sara Liparoti, Valentina Volpe et al. Analysis of Crystallization Kinetics of PLA Filament for Fused Filament Fabrication. <i>Macromolecular Materials and Engineering</i> 310(12), e00204 (2025). <link href="https://doi.org/10.1002/mame.202500204" color="#24576b">doi:10.1002/mame.202500204</link>.

[20] Todsapol Kajornprai, Jiradet Sringam, Anucha Seejuntuek et al. Crystal Evolution of Amorphous Poly(lactic acid) During Simultaneous Multi‐step Tensile Deformation and Annealing. <i>Journal of Polymer Science</i> 63(1), 192-203 (2025). <link href="https://doi.org/10.1002/pol.20240703" color="#24576b">doi:10.1002/pol.20240703</link>.

[21] Necmi Dusunceli, Aleksey D. Drozdov, Naseem Theilgaard. Influence of temperature on viscoelastic–viscoplastic behavior of poly(lactic acid) under loading–unloading. <i>Polymer Engineering &amp; Science</i> 57(3), 239-247 (2017). <link href="https://doi.org/10.1002/pen.24404" color="#24576b">doi:10.1002/pen.24404</link>.

[22] Alcide Bertocco, Matteo Bruno, Enrico Armentani et al. Stress Relaxation Behavior of Additively Manufactured Polylactic Acid (PLA). <i>Materials</i> 15(10), 3509 (2022). <link href="https://doi.org/10.3390/ma15103509" color="#24576b">doi:10.3390/ma15103509</link>.

[23] Çağlar Kahya, Oğuz Tunçel, Onur Çavuşoğlu, Kenan Tüfekci. Thermal annealing optimization for improved mechanical performance of PLA parts produced via 3D printing. <i>Polymer Testing</i> 144, 108735 (2025). <link href="https://doi.org/10.1016/j.polymertesting.2025.108735" color="#24576b">doi:10.1016/j.polymertesting.2025.108735</link>.

[24] Florina Chiscop, Carmen-Cristiana Cazacu, Dragos-Alexandru Cazacu, Costel Emil Cotet. Sustainable Thermal Post-Processing of PLA 3D Prints: Increased Dimensional Precision and Autoclave Compatibility. <i>Journal of Functional Biomaterials</i> 16(9), 334 (2025). <link href="https://doi.org/10.3390/jfb16090334" color="#24576b">doi:10.3390/jfb16090334</link>.


<!-- PAGE -->
### References (continued)

[25] Agnieszka Szust, Grzegorz Adamski. Using thermal annealing and salt remelting to increase tensile properties of 3D FDM prints. <i>Engineering Failure Analysis</i> 132, 105932 (2022). <link href="https://doi.org/10.1016/j.engfailanal.2021.105932" color="#24576b">doi:10.1016/j.engfailanal.2021.105932</link>.

[26] Miloš Vorkapić, Ivana Mladenović, Toni Ivanov et al. Enhancing mechanical properties of 3D printed thermoplastic polymers by annealing in moulds. <i>Advances in Mechanical Engineering</i> 14(8), 16878132221120737 (2022). <link href="https://doi.org/10.1177/16878132221120737" color="#24576b">doi:10.1177/16878132221120737</link>.

[27] Radoslaw A. Wach, Piotr Wolszczak, Agnieszka Adamus‐Wlodarczyk. Enhancement of Mechanical Properties of FDM‐PLA Parts via Thermal Annealing. <i>Macromolecular Materials and Engineering</i> 303(9), 1800169 (2018). <link href="https://doi.org/10.1002/mame.201800169" color="#24576b">doi:10.1002/mame.201800169</link>.

[28] Claire Benwood, Andrew Anstey, Jacek Andrzejewski et al. Improving the Impact Strength and Heat Resistance of 3D Printed Models: Structure, Property, and Processing Correlationships during Fused Deposition Modeling (FDM) of Poly(Lactic Acid). <i>ACS Omega</i> 3(4), 4400-4411 (2018). <link href="https://doi.org/10.1021/acsomega.8b00129" color="#24576b">doi:10.1021/acsomega.8b00129</link>.

[29] Natalia von Windheim, David W. Collinson, Trent Lau et al. The influence of porosity, crystallinity and interlayer adhesion on the tensile strength of 3D printed polylactic acid (PLA). <i>Rapid Prototyping Journal</i> 27(7), 1327-1336 (2021). <link href="https://doi.org/10.1108/rpj-08-2020-0205" color="#24576b">doi:10.1108/rpj-08-2020-0205</link>.

[30] Ali Ghasemkhani, Gholamreza Pircheraghi, Nima Rashidi Mehrabadi, Asma Eshraghi. Effects of heat treatment on the mechanical properties of 3D-printed polylactic acid: Study of competition between crystallization and interlayer bonding. <i>Materials Today Communications</i> 39, 109266 (2024). <link href="https://doi.org/10.1016/j.mtcomm.2024.109266" color="#24576b">doi:10.1016/j.mtcomm.2024.109266</link>.

[31] Malcolm L. Williams, Robert F. Landel, John D. Ferry. The Temperature Dependence of Relaxation Mechanisms in Amorphous Polymers and Other Glass-forming Liquids. <i>Journal of the American Chemical Society</i> 77(14), 3701-3707 (1955). <link href="https://doi.org/10.1021/ja01619a008" color="#24576b">doi:10.1021/ja01619a008</link>.

[32] Nathalie Ramos, Christoph Mittermeier, Josef Kiendl. Efficient simulation of the heat transfer in fused filament fabrication. <i>Journal of Manufacturing Processes</i> 94, 550-563 (2023). <link href="https://doi.org/10.1016/j.jmapro.2023.03.030" color="#24576b">doi:10.1016/j.jmapro.2023.03.030</link>.


<!-- PAGE -->
### References (continued)

[33] Ahmed Elmoghazy, Anselm Heuer, Aron Kneer et al. Phase-field modeling of the morphological and thermal evolution of additively manufactured polylactic acid layers and their influence on the effective elastic mechanical properties. <i>Progress in Additive Manufacturing</i> 10(8), 5093-5115 (2025). <link href="https://doi.org/10.1007/s40964-024-00891-8" color="#24576b">doi:10.1007/s40964-024-00891-8</link>.

[34] Edson A. dos Santos Filho, Edda Valentina Veracierta Rodriguez, Simon Debrie et al. Thermal Annealing of Injection‐Molded PLA Grades: Trade‐Offs Between Crystallinity Development, Dimensional Stability, Secondary Shrinkage, and Mechanical Performance. <i>Journal of Applied Polymer Science</i> 143(37), e71150 (2026). <link href="https://doi.org/10.1002/app.71150" color="#24576b">doi:10.1002/app.71150</link>.

[35] Natrayan Lakshmaiya. Thermo-constrained physics informed neural network based optimization of mechanical performance in recycled PLA additive manufacturing. <i>Results in Engineering</i> 30, 110279 (2026). <link href="https://doi.org/10.1016/j.rineng.2026.110279" color="#24576b">doi:10.1016/j.rineng.2026.110279</link>.

### Supplement A. Provenance and reproducibility requirements

The project repository is <link href="https://github.com/VorteXEkansh/FDM-Annealing" color="#24576b">VorteXEkansh/FDM-Annealing</link>. It contains the DOI-verified literature matrix, novelty audit, search strategy, base-paper audit, the manuscript restructuring map, the complete current source and the authoritative research-state record. The base paper is preserved separately from the evolving manuscript. No solver dataset is available in this stage.

Each future case must preserve a unique identifier, the solver version, geometry and material orientation, input configuration, source references, units, boundary histories, mesh, time-integration and contact settings, execution status, raw-output location and file checksums. Failed cases remain in the record with their failure reason. Postprocessing must identify both the raw field and the script/equation producing each response.

Every quantitative result will be assigned to one of three evidence classes: A, genuine solver output; B, a reproducible numerical calculation; or C, a verified published source with an exact locator. Design choices remain labeled as inputs, never as findings. The temperatures and durations in Table 2 are inherited design choices; its nine-combination count follows directly from three temperature levels multiplied by three duration levels.

The bibliography is deliberately limited to the checked sources cited in this draft. The larger bibliography in the base proposal is archived for later appraisal and is not treated as a validated material database. No published numerical property, deformation value or uncertainty estimate is adopted here without extraction and applicability assessment.

Author names and affiliation follow the supplied base paper. Authorship contributions, funding and submission declarations require author confirmation before journal submission; no such declarations are inferred here.
