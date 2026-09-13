# Free and gap-constrained annealing of FFF-printed PLA: a thermo-mechanical computational study
## Sub-melting exposure, dimensional change and released-state response

Aadit Jain · Dheeraj Yadav · Ekansh Malhotra

Production and Industrial Engineering, Delhi Technological University

Computational manuscript draft · 13 September 2026

### Abstract — structured research draft

<b>Context and question.</b> Annealing of fused-filament-fabricated (FFF) polylactic acid (PLA) can change dimensions while geometric restraint introduces contact loading. This computational study asks how temperature, holding time and quantified initial fixture clearance influence thermal exposure and the dimensional change, warpage and residual stress assessed after cooling and release for a specified PLA grade, print architecture and geometry.

<b>Planned approach.</b> Genuine ANSYS analysis will compare mechanically free annealing with opposed-face gap restraint for a 60 mm × 10 mm × 4 mm rectangular plate over an evidence-supported sub-melting domain. Candidate levels are 80&nbsp;°C, 95&nbsp;°C and 110&nbsp;°C, with holds of 30 min, 60 min and 90 min; their admission depends on the selected material evidence. Temperature-dependent, history-dependent behavior and contact will be represented only to the extent supported by data. Thermal histories, signed dimensions and released warpage will be distinguished from contact pressure and conditional stress predictions. Numerical verification, independent literature-based validation and uncertainty assessment will precede multi-objective interpretation.

<b>Results status.</b> One verification-only ANSYS transient thermal field solution is complete; no production PLA coupon result, convergence claim, physical validation finding or optimum exists. For a constant-property plane wall with a ramp–hold–cool ambient history, genuine MAPDL center temperatures agree with a 200-term analytical solution to a maximum absolute error of 0.005180700&nbsp;°C. The maximum conventional relative error is 0.001700533% using kelvin, and the maximum error normalized by temperature excursion is 0.157660518%. The accepted model uses 1025 nodes, 640 SOLID70 elements and a fixed 0.25&nbsp;s step. These constants and temperatures are numerical verification fixtures, not PLA data. The production model remains blocked by compatible Prusament k(T) and c<sub>p</sub>(T), physical boundary/contact inputs and irreversible-strain evidence.

<b>Intended contribution.</b> The study will assess the clearance–distortion–stress trade-off and distinguish temporary geometric suppression from released stability. Prior supported annealing and numerical optimization preclude a broad first-of-kind claim. No strength improvement or industrial treatment recommendation is asserted.

Keywords: fused filament fabrication; PLA; annealing; fixture clearance; thermo-mechanical modeling; contact; warpage; numerical verification

### 1. Rationale and scope

Annealing studies by Butt and Bhaskar [1] and Stojković et al. [2] motivate assessing dimensional response alongside material behavior. They do not validate the proposed plate fixture. The present computational study compares free annealing with quantified fixture clearance, accounting for contact activation, thermal exposure and release.

Dimensional suppression inside a fixture is insufficient evidence of stable final geometry. The research therefore evaluates cooled, released response and restricts claims to observables supported by independent evidence. New physical testing and strength enhancement inferred from thermal stress are outside scope.

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

Recent injection-moulded grade comparisons [34] address secondary shrinkage and mechanical trade-offs. Their online publication predates this review cutoff even though the assigned issue date is later. They are useful mechanistic context, but their initial state and manufacturing route differ from FFF. No constitutive coefficient is transferred from these moulding comparisons. The admitted Prusament relaxation parameters come from the separate FFF-specific evidence [8].

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

This evidence motivates a focused comparison of mechanically free annealing and quantified opposed-face gap restraint for one specified FFF-PLA system. The research question, objectives and testable propositions below distinguish transient exposure from cooled, released response. The intended contribution is a conditional clearance–distortion–stress assessment, not a claim of novelty for the component methods. Physical validation will be restricted to independently supported observables.

ASTM F3489-23 [3] remains relevant to appraisal of polymer material-extrusion mechanical data. It does not certify the proposed simulation or provide an annealing constitutive law. Published support effects are literature findings, not results of this study.

<!-- PAGE -->
### 2. Research question and finalized scope

<b>Primary research question.</b> For a specified FFF-PLA grade, print architecture and geometry, how do annealing temperature, holding time and initial fixture clearance influence transient thermal exposure and the irreversible dimensional change, warpage and residual stress evaluated after cooling and fixture release, relative to free annealing within an evidence-supported sub-melting domain?

Temperature and duration are process inputs, while clearance is the total initial part-to-fixture separation at a common reference temperature. Transient quantities are evaluated during heating, holding and cooling. “Residual” refers to the declared cooled, released state and observation time; it does not imply an infinite-time equilibrium. Irreversible dimensional change is evaluated relative to the initial geometry at the same reference temperature, separating it from temporary thermal expansion.

### 2.1. Secondary research questions

SQ1. How does fixture presence and contact engagement change part-temperature histories, spatial gradients and thermal lag under the same external heating and cooling schedule?

SQ2. At a given thermal condition, how does initial clearance change signed directional dimensions and released warpage relative to the free baseline, and which differences persist when part-temperature histories are matched for a diagnostic comparison?

SQ3. How do contact pressure, fixture reactions and cooled residual-stress measures vary with clearance, and how much of any in-fixture geometric suppression remains after release?

SQ4. Which temperature–duration–clearance interactions and material/contact uncertainties materially affect the predicted responses, and are these effects distinguishable from numerical error and constitutive ambiguity?

SQ5. Within the admissible and verified domain, which conditions offer nondominated dimensional-error, warpage and stress trade-offs, and how stable are those comparisons to uncertainty and declared decision preferences?

### 2.2. Domain and comparison rules

The primary study uses Prusament PLA as its reference formulation, with one fixed print architecture and one representative three-dimensional plate-like coupon geometry to be selected for evidence compatibility. The property audit and constitutive reference do not supply the remaining thermal and recovery data. Material directions will be recorded for the signed responses; the currently supported stiffness closure is isotropic. A complete simulation of nozzle deposition is not required: initial printed-state evidence may instead support a calibrated recovery representation without double-counting initial stress.

The two primary conditions are FREE, an ideal mechanically unrestrained body with traction-free surfaces and only numerically verified rigid-body stabilization, and GAP, the same body initially centered between opposed fixture faces with specified total clearance and no applied preload. Gravity is omitted in this primary paired comparison as a declared isolation assumption. A support- or gravity-dependent literature reproduction must be labeled separately; it cannot silently replace FREE. No symmetry restriction may exclude the warpage modes being investigated.

<!-- PAGE -->
### 2.3. Computational objectives

1. Establish a traceable ANSYS thermal–mechanical/contact model for FREE and GAP, including material orientation, reference clearance, irreversible response, thermal boundaries, cooling and release; document every evidence source and assumption. This addresses SQ1–SQ3.
2. Quantify thermal histories, signed dimensions, released warpage, contact loading and declared residual-stress measures over admissible temperature, duration and clearance conditions, with mesh, time-step and contact verification. This addresses SQ1–SQ3.
3. Assess predictive adequacy against independently reserved, compatible published observations and state validation separately for each observable; distinguish calibration, verification and physical validation. This supports all five secondary questions.
4. Evaluate parameter interactions, uncertainty and identifiability for the responses and compare effects with numerical resolution. This addresses SQ4 and supports SQ5.
5. Construct conditional multi-objective comparisons using verified solver responses, declared feasibility/benefit criteria and uncertainty-aware interpretation; recompute selected candidates with the genuine solver. This addresses SQ5.

The inherited 80 °C, 95 °C and 110 °C temperatures and 30 min, 60 min and 90 min durations remain candidate design levels. Conditions outside the chosen grade's supported sub-melting or constitutive domain will be excluded or revised with an explicit record. A nominal treatment grid cannot authorize material-law extrapolation. Clearance bounds and any contact, thermal-attainment or acceptance thresholds require a later evidence-based specification before runs are interpreted.

### 2.4. Testable numerical propositions

H1 — Clearance effect. Within the admissible domain, at least one engaged-contact GAP condition changes released warpage or a signed directional dimension relative to FREE by more than the verified numerical resolution. The proposition is unsupported if no such difference is resolved. Thermally matched diagnostic cases will distinguish contact restraint from differing heat exposure.

H2 — Release effect. At least one GAP condition has a resolved change in warpage or directional dimension between its cooled, still-constrained state and its cooled, released state. Compare the same landmarks and reference temperature, recording release relaxation time. No resolved change in the investigated domain leaves this proposition unsupported.

H3 — Interaction. For at least one response, the effect of changing clearance differs between two admissible temperatures or holding durations beyond the uncertainty attributable to numerical solution. Evaluate the difference between paired clearance effects; if those differences are unresolved throughout the tested domain, interaction is not established.

H4 — Trade-off. At least one verified condition that reduces released dimensional error or warpage relative to another admissible condition increases the declared residual-stress measure by a resolved amount. A uniformly improving or unresolved response set does not support this proposition. Contact pressure is reported separately and is not equated with residual stress.

These are untested, domain-limited propositions, not expected findings. Their null interpretations are absence of a resolved effect in the sampled domain, not proof of universal absence. Numerical resolution criteria and extraction rules must be fixed before hypothesis assessment; plausible input uncertainty will then test robustness. Deterministic reruns do not provide independent samples, p-values or experimental confidence intervals.

<!-- PAGE -->
### 2.5. Intended contribution and limits of claim

The intended contribution is an evidence-tested account of how quantified fixture clearance changes the relationship between annealing exposure and released dimensional stability for a specified FFF-PLA system, together with the accompanying model-predicted stress cost. Its three connected elements are: a reproducible FREE–GAP comparison that separates thermal exposure from restraint; a verified response description distinguishing in-fixture suppression from released geometry; and an uncertainty-aware assessment of conditional design trade-offs. Their scientific value depends on genuine numerical evidence and the independently supported predictive domain.

Prior work already establishes supported annealing, irreversible strain analysis, thermo-viscoelastic recovery modeling and annealing-related numerical optimization [5], [8], [9], [11], [14]. The study therefore makes no claim to invent these ingredients or to be the first constrained-annealing investigation. The reviewed gap remains provisional, especially where closest-study access is limited. The proposed contribution is not yet an achieved numerical result.

The main comparison uses identical external thermal schedules to measure the combined effect of fixture presence and restraint. A separate diagnostic may impose matched part-temperature histories to isolate mechanical effects; it is an attribution calculation, not evidence that the two physical processes share a thermal history. A supported-reference reproduction, if needed for validation, must preserve that source's actual support and release protocol and remain distinct from the primary FREE condition.

Sand, salt, powder moulds and encapsulation remain literature context [11], [12], [24]–[26]. The numerical scope excludes discrete-element modeling of granular media, powder compaction and salt remelting. A two-condition study cannot establish that the proposed plate fixture outperforms these alternatives. Their published deformation reductions will not be treated as results of this model.

The paper will not claim tensile-strength, stiffness or ductility enhancement from residual stress; experimental confirmation by newly manufactured specimens; a universal PLA material law; validated crystallinity or kinetics without compatible evidence; or a unique separation of strain mechanisms from final dimensions alone. It will not claim physical validation of unobserved stress or contact pressure, nor infer such validation from dimensional agreement. These outputs remain conditional predictions if independent evidence is unavailable.

The study will not establish fatigue life, long-term aging, service creep, moisture durability, biological suitability, sterilization qualification, production cost savings or certification. It will not generalize across grades, reinforced/recycled formulations, print architectures or geometries beyond evidence. Neither a globally optimal treatment nor a universally safe stress/contact limit will be claimed from a finite numerical design space.

Multi-objective comparisons are restricted to admissible, numerically verified conditions with explicit response definitions. A low-distortion mild treatment is not automatically useful annealing: any recommendation requires a separately supported processing-benefit or application criterion. If that criterion or independent validation remains unavailable, the paper will report conditional trade-offs and the limitation, not an industrial processing recommendation.

The scope is finalized as a computational research commitment. The Prusament reference law is implemented and unit-tested. Ansys Student 2026 R1, a Mechanical APDL Student checkout and the parameterized three-volume geometry build are verified on the host. A separate plane-wall ANSYS field solution verifies the transient conduction and convection implementation against an analytical history; it is not a PLA prediction. Production discretization, missing material closures and validation datasets remain open.

<!-- PAGE -->
### 3. Parametric computational geometry and controlled constraint

The selected specimen is a solid rectangular plate measuring 60 mm × 10 mm × 4 mm in x, y and z. It reproduces the regular-plate dimensions of Trofimov et al. [7, Fig. 4(a)]. That source selected the regular plate for reliable thermal observation and used a separate bridge-like structure for distortion validation. The present study transfers only the dimensions. It does not transfer Raise3D Premium PLA properties, print-induced stress, thermal data or validation outcomes to Prusament PLA.

The 60 mm span gives a length-to-thickness ratio of 15 while the width-to-thickness ratio is 2.5. The two nominal fixture-facing surfaces are each 600 mm<super>2</super>. These are geometry calculations. The plate retains three signed dimensions, supports plane-fit released-warpage extraction and avoids the stress concentrators of a tensile coupon. The source bridge is reserved as a possible separate validation geometry because its supports and deck introduce additional boundaries.

GAP contains the specimen and two 70 mm × 20 mm × 5 mm AISI 304 plates. The 5 mm plan margin on every specimen side prevents the fixture edge from coinciding with the nominal contact boundary. Plate dimensions are declared computational design choices. The plates will be deformable when the field model is admitted; they are not ideal rigid walls. FREE contains the same specimen without fixture volumes or contact.

Let x be the specimen length and primary print-path direction, y the width and z the build/thickness direction. Define h<sub>0</sub> as the 4 mm initial thickness and H<sub>0</sub> as the separation between the effective opposing plate faces at T<sub>ref</sub>. The specimen is centered, the total gap is split equally between the two faces and no preload is applied. The total initial clearance and its dimensionless form are

EQ: g<sub>0</sub> = H<sub>0</sub> − h<sub>0</sub>, &nbsp;&nbsp; γ = g<sub>0</sub>/h<sub>0</sub>. &nbsp;&nbsp; (1)

The five declared screening levels are γ ∈ {0, 0.0025, 0.005, 0.01, 0.02}, corresponding to g<sub>0</sub> ∈ {0, 0.01, 0.02, 0.04, 0.08} mm. Thus H<sub>0</sub> ranges from 4.00 mm to 4.08 mm. These levels are design choices, not measured fixture tolerances, material properties or an admitted optimum. They span coincident contact to 2% of thickness and must be revised if contact activation is unresolved relative to the later mesh, numerical tolerances or supported irreversible-strain range.

The proposed absolute gaps 0.000 mm, 0.025 mm, 0.050 mm, 0.100 mm and 0.200 mm correspond to γ = 0, 0.00625, 0.0125, 0.025 and 0.05 for this specimen. Zero gap is retained. The 0.025 mm and 0.050 mm candidates are mechanically interpretable and lie within the normalized screen, where neighboring dimensionless levels provide more systematic near-contact resolution. The 0.100 mm and 0.200 mm candidates are deferred because they exceed the primary 2% thickness screen and no supported free-deformation scale yet justifies spending primary cases at those clearances. This is a sampling decision, not a prediction that contact cannot occur.

The primary GAP condition is initially centered and gravity is omitted. A gravity-seated or supported reproduction of a published protocol is a separate validation configuration. Figure 1 gives top and side views of the geometry; it does not impose a symmetry boundary condition.

FIGURE: gap

CAPTION: Figure 1. Dimensioned specimen and opposed-plate fixture geometry at the reference state. The total clearance g<sub>0</sub> is divided equally above and below the centered 60 mm × 10 mm × 4 mm specimen. Schematic, not to scale; no mesh, deformation or field result is shown.

TABLE: Geometry definition and status
Quantity | Selected value | Evidence status
Specimen | 60 mm × 10 mm × 4 mm | Geometry from Trofimov et al. [7, Fig. 4(a)]; source material data not transferred
Fixture plates | 70 mm × 20 mm × 5 mm each | Declared AISI 304 design; deformation retained in future field model
Nominal face area | 600 mm<super>2</super> per specimen face | Reproducible calculation, not actual contact area
Clearance γ | 0; 0.0025; 0.005; 0.01; 0.02 | Screening design; no measured tolerance or optimum
Total gap g<sub>0</sub> | 0; 0.01; 0.02; 0.04; 0.08 mm | Calculated from g<sub>0</sub> = γh<sub>0</sub>

The base proposal's single hot allowance is replaced by this normalized reference-gap design. Thermal expansion of the plates and any physical spacers, plate compliance and specimen deformation determine subsequent local separation. Spacer geometry is deferred because its expansion convention and attachment are unresolved; H<sub>0</sub> is an explicit reference-state kinematic dimension. Friction and contact conductance remain unassigned. Bonding the specimen faces or prescribing zero displacement over them would eliminate the intended gap-controlled mechanism.

A geometry-only Mechanical APDL build instantiated the three solid volumes for γ = 0.01, so g<sub>0</sub> = 0.04 mm. MAPDL reported three selected volumes and saved the database. This single clearance is a construction check, not a preferred treatment or simulation case. The input contains no element type, mesh, material, load, analysis type or solve command. The complete thermal–mechanical campaign remains blocked.

FREE has traction-free mechanical surfaces and no fixture contact or gravity in the primary comparison. Numerical rigid-body stabilization must not suppress shrinkage, lateral slip or bowing. A supported part must be labeled as a separate configuration. Symmetry conditions require justification; they must not exclude asymmetric warpage by construction.

<!-- PAGE -->
### 3.1. Thermal design and reporting states

Table 3 retains the thermal levels requested from the base proposal. They are planned inputs, not measured histories, solver outputs or recommended processing settings. Their sub-melting applicability must be checked for the selected grade and source-supported model range.

TABLE: Thermal design choices
Factor | Candidate levels | Interpretation
Annealing temperature | 80 °C; 95 °C; 110 °C | Inherited design choices; no established optimum
Hold duration | 30 min; 60 min; 90 min | Inherited choices; attainment rule still required
Constraint | FREE; GAP fixture | Explicit contact and support definitions required
Initial clearance | γ = 0–0.02; g<sub>0</sub> = 0–0.08 mm | Declared geometry-screening range; later admission required

The three temperature and three duration levels define nine thermal combinations before clearance, verification or uncertainty cases are added. This is design arithmetic, not a count of completed simulations. The total run count is not yet fixed.

Heating ramps, environmental temperature, convection, possible radiation, cooling and release must be specified with units and source or design justification. Hold time will be distinguished from total exposure: a criterion based on the part temperature field must define attainment. That criterion and its band are not yet fixed. Temperatures used in absolute-temperature laws must be converted consistently to kelvin. The Stage 8 plane-wall benchmark exercises a complete ramp, hot hold and cooling history, but its declared schedule is a numerical verification fixture and does not fix this production protocol.

A process comparison can apply the same external thermal cycle to constrained and unconstrained domains, allowing part histories to differ. A separate thermally matched comparison is needed to isolate mechanical restraint from fixture-induced thermal lag. The two comparisons answer different questions and must not be conflated.

### 4. Constitutive decision and governing equations

The strongest parameterized model in the present evidence set is a small-strain isotropic generalized-Maxwell model for Prusament PLA, with reversible thermal expansion and a piecewise temperature shift [8]. Stage 5 implements its material-point reference relations and analytical tests. A complete production annealing model remains blocked by missing thermal functions, bulk irreversible recovery and initial-state evidence. No production ANSYS material card or coupon result is represented as complete.

Chapuis et al. [8] characterize Prusament PLA using frequency sweeps of 1–18 Hz across 23–85 °C. This interval defines the code's temperature admission envelope, not proof of validity for every dwell, strain amplitude, ramp or bulk geometry. The inherited 30 min, 60 min and 90 min holds still need time-domain support. The 95 °C and 110 °C levels remain outside the envelope. The reference tests use 23 °C as a thermal-strain reference; this does not fix the production cycle. A 20 °C PLA start is not admitted by extrapolation.

The source routine implements plane-stress shells with programmed pre-strain. The present three-dimensional isotropic extension preserves its constant-Poisson stiffness algebra, which is checked through a plane-stress reduction. It is an explicit mathematical closure, not independent evidence of bulk isotropy or volumetric relaxation. FormFutura orthotropy [16], SUNLU PLA Plus relaxation [22] and Black Devil Design irreversible strain [5] remain separate comparators.

TABLE: Constitutive admission and unresolved closures
Relation | Implemented reference | Production limitation
Reversible thermal strain | Constant Prusament α [8] | No directional expansion functions
Relaxation | 23 source Maxwell branches [8] | Duration, strain and bulk transfer remain conditional
Temperature dependence | Piecewise Arrhenius/WLF clock [8] | No separate same-grade E(T) multiplier
Irreversible annealing strain | Evidence-gap error | No identified signed bulk law or initial recovery state
PLA heat transfer | Plane-wall verification only | Compatible Prusament k(T) and c<sub>p</sub>(T) missing
Fixture behavior | AISI 304 interpolation and elastic response [38] | Expansion convention and contact behavior open

The ANSYS transient heat balance, with no internal heat source in the verified reference problem, is

EQ: ρc<sub>p</sub> ∂T/∂t = ∇ · (k ∇T). &nbsp;&nbsp; (2)

The conductivity k is isotropic in the selected material closure. Stage 8 implements Eq. (2) for a constant-property analytical benchmark. Compatible temperature-dependent Prusament functions remain absent. Omitting crystallization and dissipative heating requires a physical justification before production use; the present omission does not establish that these effects vanish. Supplier density [36] and unidentified-PLA constants [37] cannot supply a complete Prusament thermal law.

<!-- PAGE -->
### 4.1. Strain partition and reversible expansion

The selected small-strain accounting is

EQ: ε = ε<sup>e</sup> + ε<sup>ve</sup> + ε<sup>th</sup> + ε<sup>ann</sup>,<br/>ε<sup>m</sup> = ε − ε<sup>th</sup> − ε<sup>ann</sup>. &nbsp;&nbsp; (3)

Here ε is total strain, ε<sup>m</sup> is mechanical strain, ε<sup>th</sup> is reversible thermal strain and ε<sup>ann</sup> denotes an irreversible stress-free distortion relative to the common reference state. The macroscopic elastic and delayed components are defined operationally as ε<sup>e</sup> = C<sub>inst</sub><sup>−1</sup> : σ and ε<sup>ve</sup> = ε<sup>m</sup> − ε<sup>e</sup>. This is a network identity; the delayed component is not the sum of the individual dashpot strains. No additional creep law is added to the Prony response.

The simpler elastic-plus-thermal-plus-annealing model is the limit without the delayed component. It cannot reproduce the published relaxation, and it still lacks a supported bulk annealing-strain law. The more complete accounting in Eq. (3) therefore selects the viscoelastic core while retaining the unresolved irreversible mechanism explicitly.

For the source constant linear expansion coefficient,

EQ: ε<sup>th</sup>(T) = α(T − T<sub>r</sub>)I,<br/>α = 68.0 × 10<sup>−6</sup> K<sup>−1</sup>. &nbsp;&nbsp; (4)

I is the identity tensor and T<sub>r</sub> is the declared thermal reference. The relation is identical on heating and cooling; a closed free thermal cycle gives zero net thermal strain. It must not be altered to encode irreversible shrinkage. Directional expansion functions are not identified for this formulation.

The implementation uses symmetric tensors in the order xx, yy, zz, xy, yz, xz, with tensor shear strains. An interface using engineering shear must convert its shear strain components before applying this tensor law. The source uses ν = 0.35. The isotropic stiffness action for any symmetric strain tensor A is

EQ: C(E,ν) : A = 2G A + λ tr(A)I,<br/>G = E/[2(1 + ν)], &nbsp; λ = Eν/[(1 + ν)(1 − 2ν)]. &nbsp;&nbsp; (5)

The equilibrium and branch tensors use this same operation with their respective source moduli. Tensor symmetry, inverse compliance, hydrostatic response and engineering-shear conversion are checked numerically. Finite rotations or strains require a separately verified finite-deformation implementation; the linear material-point core does not establish that a proposed warpage case is within its kinematic range.

<!-- PAGE -->
### 4.2. Generalized-Maxwell model and Prony conversion

In reduced time ξ, the implemented stress and branch evolution are

EQ: σ = C<sub>∞</sub> : ε<sup>m</sup> + ∑<sub>i=1</sub><sup>23</sup> s<sub>i</sub>,<br/>∂s<sub>i</sub>/∂ξ + s<sub>i</sub>/τ<sub>i</sub> = C<sub>i</sub> : ∂ε<sup>m</sup>/∂ξ. &nbsp;&nbsp; (6)

s<sub>i</sub> is the stress in branch i; C<sub>∞</sub> uses E<sub>∞</sub> = k₀ = 10.598 MPa and C<sub>i</sub> uses k<sub>i</sub> from Table 4 [8]. The zero-state reference tests initialize all stresses to zero. The printed coupon's internal state is not known. The source's balanced programmed branch stresses are not transferred from thin bilayers to the bulk coupon, nor combined with a separate shrinkage field without an identifiability argument.

The instantaneous modulus and normalized Prony conversion are

EQ: E<sub>inst</sub> = E<sub>∞</sub> + ∑<sub>i=1</sub><sup>23</sup> k<sub>i</sub>, &nbsp; g<sub>i</sub> = k<sub>i</sub>/E<sub>inst</sub>,<br/>G<sub>inst</sub> = E<sub>inst</sub>/[2(1 + ν)], &nbsp; K<sub>inst</sub> = E<sub>inst</sub>/[3(1 − 2ν)]. &nbsp;&nbsp; (7)

The deterministic modulus sum is E<sub>inst</sub> = 1691.594 MPa. Both normalized shear and bulk kernels use the same g<sub>i</sub> and τ<sub>i</sub>, retaining the assumed constant ν. The remaining equilibrium fraction is E<sub>∞</sub>/E<sub>inst</sub>. A shear-only relaxation model with fixed bulk modulus would change this assumption. The conversion is algebraically tested, but an installed ANSYS adapter has not been executed. The official ANSYS theory specifies separate shear and bulk kernels and instantaneous elastic inputs [39].

For an isothermal strain-step test, the tensile relaxation modulus is

EQ: E<sub>r</sub>(t,T) = E<sub>∞</sub> + ∑<sub>i=1</sub><sup>23</sup> k<sub>i</sub> exp[−t/(a<sub>T</sub>τ<sub>i</sub>)]. &nbsp;&nbsp; (8)

The fast and fully relaxed limits are E<sub>inst</sub> and E<sub>∞</sub>. Positive branch moduli and times imply positive, non-increasing isothermal relaxation. Temperature changes the clock; no separate E(T) reduction is multiplied into the spectrum. This avoids counting the same measured temperature dependence twice. The supplier's tensile moduli [36] are screening comparisons, not substitutes for the instantaneous relaxation modulus.

<!-- PAGE -->
TABLE: Prusament PLA generalized-Maxwell coefficients at T<sub>g</sub> = 65 °C from Chapuis et al. [8, supplementary Table B.2]
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


<!-- PAGE -->
### 4.3. Temperature shift and non-isothermal history

The published shift is piecewise [8, Eq. (6) and supplementary Table B.1]:

EQ: log<sub>10</sub>a<sub>T</sub> = C₃(1/T<sub>K</sub> − 1/T<sub>g,K</sub>), &nbsp; T &lt; T<sub>g</sub>;<br/>log<sub>10</sub>a<sub>T</sub> = −C₁(T − T<sub>g</sub>)/[C₂ + (T − T<sub>g</sub>)], &nbsp; T ≥ T<sub>g</sub>. &nbsp;&nbsp; (9)

T<sub>g</sub> = 65 °C, C₁ = 17.4, C₂ = 51.6 K and C₃ = 35 000 K. T<sub>K</sub> and T<sub>g,K</sub> are absolute kelvin. The source routine confirms a base-10 exponent and multiplication of each reference relaxation time by a<sub>T</sub>. Both branches give a<sub>T</sub> = 1 at T<sub>g</sub>; equality of their derivatives is not assumed. The implemented Arrhenius interval is 23–65 °C and the WLF interval is 65–85 °C. The code rejects temperatures outside the combined envelope.

The physical history enters through reduced time,

EQ: ξ(t) = ∫<sub>0</sub><sup>t</sup> [a<sub>T</sub>(T(s))]<sup>−1</sup> ds. &nbsp;&nbsp; (10)

Only an isothermal history permits replacing this integral by t/a<sub>T</sub>. Using the final temperature for the entire ramp would discard its history. The reference quadrature uses the prescribed temperature path and splits at T<sub>g</sub>. The WLF theory [31] and ANSYS reduced-time formulation [39] support the clock concept; the coefficients remain those of the specific Prusament source.

For a strain increment linear in reduced time, the branch update is

EQ: r<sub>i</sub> = Δξ/τ<sub>i</sub>, &nbsp; A<sub>i</sub> = exp(−r<sub>i</sub>),<br/>B<sub>i</sub> = [1 − exp(−r<sub>i</sub>)]/r<sub>i</sub>,<br/>s<sub>i</sub><sup>n+1</sup> = A<sub>i</sub>s<sub>i</sub><sup>n</sup> + B<sub>i</sub>C<sub>i</sub> : Δε<sup>m</sup>. &nbsp;&nbsp; (11)

The implementation evaluates the exponential difference accurately near zero. Its physical-time substep freezes the shift at the midpoint temperature, approximating Δξ by Δt/a<sub>T</sub>(T<sub>mid</sub>), and requires splitting at T<sub>g</sub>. It is exact for an isothermal linear-strain increment and is refined for a changing temperature. The quadrature utility and the substep update are distinct: accurate integration of reduced time alone does not make an arbitrary strain history exact.

The intended ANSYS implementation must reproduce the full piecewise clock, both relaxation kernels, state persistence and shear convention. A single native WLF branch is not equivalent over the full interval. A verified custom or otherwise equivalent adapter is required before any production run; the present reference implementation does not claim that this adapter exists.

<!-- PAGE -->
### 4.4. Fixture constitutive relations

AISI 304 stainless steel remains the candidate plate material [38]. The source table brackets the planned thermal interval; each property p is interpolated between adjacent source knots as

EQ: p(T) = p<sub>a</sub> + (p<sub>b</sub> − p<sub>a</sub>)(T − T<sub>a</sub>)/(T<sub>b</sub> − T<sub>a</sub>). &nbsp;&nbsp; (12)

The code reproduces all table knots, interpolates within 20–200 °C, and rejects extrapolation. Instantaneous fixture stress uses Eq. (5) with interpolated E and ν; GPa is converted to MPa. Thermal conductivity, heat capacity and density remain property lookups until the field model is built.

TABLE: Candidate AISI 304 fixture properties from Meng et al. [38, Table 1]
Property | 20 °C | 100 °C / 200 °C
ρ | 7910 kg m⁻³ | 7876 / 7840 kg m⁻³
c<sub>p</sub> | 456 J kg⁻¹ K⁻¹ | 494 / 532 J kg⁻¹ K⁻¹
k | 16.2 W m⁻¹ K⁻¹ | 16.6 / 17.45 W m⁻¹ K⁻¹
α | 15.5 µm m⁻¹ K⁻¹ | 16.3 / 16.7 µm m⁻¹ K⁻¹
E | 200 GPa | 191.4 / 183.5 GPa
ν | 0.290 | 0.285 / 0.289


The expansion coefficient's tangent-versus-mean convention and reference temperature are not clear in the source table. Stage 5 therefore blocks conversion of these values into fixture thermal strain until that definition is resolved. This qualification is necessary because fixture expansion changes the operating gap. Interpolation of a reported coefficient is not proof that its integral is the correct thermal strain. The code raises an evidence-gap error for that operation.

The selected alloy heat, fixture geometry, contact conductance and friction remain open. A stiff metal fixture is not an infinitely rigid or thermally inert boundary. Its restraint and heat-transfer effects must be represented in the future comparison.

<!-- PAGE -->
### 4.5. Irreversibility, excluded mechanisms and field implementation

No bulk annealing-induced irreversible-strain relation is parameterized. Its intended role is signed permanent stress-free distortion, distinguished from reversible expansion and delayed viscoelastic recovery. The source's programmed Prusament pre-strains are thin-bilayer calibrations [8]. Bute et al. demonstrate directional irreversible behavior for another grade [5]; neither supplies a transferable three-dimensional Prusament law. Requests for a production annealing-strain value raise an explicit evidence-gap error.

Zero annealing strain is used only in the labelled reference tests. It is not the production default. A free, initially relaxed Maxwell solid with positive equilibrium stiffness and reversible expansion returns to its reference dimensions after a closed thermal cycle. Delayed deformation retained during a finite cooling/observation interval is not automatically irreversible annealing strain. Contact loading may create a history-dependent residual state, but its magnitude and persistence require the solved cycle and cannot be inferred from these unit tests.

No crystallization kinetic equation, evolving crystal fraction or latent-heat source is included. Compatible formulation, initial crystallinity and non-isothermal kinetic evidence are absent [17–19]. An isothermal Avrami expression must not be evaluated at the instantaneous temperature of a ramp. The present model does not assert that crystallization is physically absent; its omission remains a limitation to assess before annealing predictions are admitted.

The designated future ANSYS mechanical field obeys quasi-static equilibrium. Gravity is omitted in the primary paired comparison, giving

EQ: ∇ · σ = 0. &nbsp;&nbsp; (13)

For ideal unilateral normal contact, local gap g<sub>n</sub> and compressive pressure p<sub>n</sub> satisfy

EQ: g<sub>n</sub> ≥ 0, &nbsp; p<sub>n</sub> ≥ 0, &nbsp; g<sub>n</sub>p<sub>n</sub> = 0. &nbsp;&nbsp; (14)

These are implementation targets for the future field solver, not executed equations in the material-point tests. The actual contact formulation permits a controlled numerical approximation; its penetration, friction and heat-transfer treatment must be verified. Cooling must retain the intended contact until the declared release event, followed by evaluation at the common reference state. Spatial averaging and extraction rules must distinguish contact pressure from residual stress and avoid unqualified edge maxima.

### 4.6. Material-relation verification status

Thirty-eight numerical unit tests pass for the implemented material relations. They compare source sums and shift conventions, analytical elastic and relaxation limits, exact isothermal increments, thermal reversibility, shear/bulk conversion and numerical refinement for a prescribed temperature ramp. Ten further tests cover the Stage 8 thermal reference and production admission contract. Synthetic test inputs are numerical fixtures, not measured PLA data or coupon simulation results. Missing annealing strain, crystallization and production closures are tested to raise errors.

Each governing equation is mapped to its implemented function or designated future solver/postprocessing operation in the repository. The full test record preserves input and code hashes. The verified thermal case adds genuine ANSYS field evidence for Eq. (2), but only for the declared plane-wall problem. These checks do not establish ANSYS viscoelastic material-point agreement, production mesh convergence, physical validation or validity of the proposed annealing holds.

### 4.7. Solver environment and automated execution boundary

The identified host installation is Ansys Student 2026 R1 under the v261 product tree. Workbench `RunWB2.exe` reports product version 26.1; the Mechanical executable `AnsysWBU.exe` reports product version 26.1; and optiSLang reports 26.1.0 revision 1878. Installed Workbench templates include Static Structural, Transient Structural and Transient Thermal. File presence is not treated as a license checkout. Mechanical APDL reported release 2026 R1, build 26.1, update 20260202 and the `Ansys Mechanical Enterprise Academic Student` product in both the Stage 6 zero-analysis probe and the accepted Stage 8 transient thermal execution.

The official 2026 R1 Student description states a structural limit of 128,000 nodes/elements, no geometry export and up to four HPC CPU cores [40]. The host provides eight physical cores, 16 logical processors and 15.82 GiB installed memory; production launch settings will remain within the four-core license statement. Solver-generated contact and auxiliary entities must be included when checking the structural limit. The accepted verification mesh contains 1025 nodes and 640 elements; no production specimen/fixture mesh exists.

The project uses explicit JSON case records and a fail-closed Python runner. A production record must provide annealing temperature in °C, hold time in seconds, fixture gap in mm and a material identifier. Execution is rejected while any geometry, thermal-property, irreversible-strain, material-adapter, boundary-history or extraction gate remains false. This makes parameters reproducible without silently converting unresolved choices into model inputs. PyMechanical was not found in the system environment and is not a dependency of the current direct MAPDL batch path. DesignXplorer and optiSLang are present on disk but were not used; no design study, sensitivity index or optimization result was generated.

Every run directory retains the exact command, case and APDL hashes, return code and hashes of generated logs. Failed cases are preserved. The Stage 7 preprocessing-only run stores the MAPDL database, output and five-level gap table. Stage 8 preserves five thermal attempts, including rejected extraction/accuracy cases and an I/O failure; attempt 05 is the accepted verification run. The full production campaign remains blocked.

<!-- PAGE -->
### 5. Dimensional and mechanical response definitions

Use identical material landmarks or consistently defined feature sets before and after treatment. Let d<sub>i,0</sub> and d<sub>i,f</sub> be the reference and final lengths associated with i ∈ {x, y, z}; these may represent length, width and thickness. Remove rigid translation and rotation through a declared alignment before measuring directional dimensions. Do not allow a change of bounding-box orientation to masquerade as recovery.

EQ: Δd<sub>i</sub> = d<sub>i,f</sub> − d<sub>i,0</sub>, &nbsp;&nbsp; δ<sub>i</sub> = 100 Δd<sub>i</sub>/d<sub>i,0</sub>. &nbsp;&nbsp; (15)
Positive δ<sub>i</sub> denotes expansion and negative δ<sub>i</sub> denotes contraction. δ<sub>i</sub> is the numerical percentage, reported with %. A scalar summary is

EQ: E<sub>RMS</sub> = √[(δ<sub>x</sub><sup>2</sup> + δ<sub>y</sub><sup>2</sup> + δ<sub>z</sub><sup>2</sup>)/3]. &nbsp;&nbsp; (16)
E<sub>RMS</sub> has the same percentage convention. It must accompany all signed components; it cannot reveal whether a part contracted in-plane and grew through its thickness.

No numerical tolerances are assigned. Acceptance metrics will be implemented only after a supported dimensional specification is selected. Dimensions relative to initial geometry and deviations from a manufacturing drawing are distinct; any later application must identify its reference target.

For a designated surface region S, fit a plane Π by an area-weighted least-squares rule to the final released surface, then define

EQ: w = max<sub>X∈S</sub> |r<sub>⊥</sub>(X, Π)|. &nbsp;&nbsp; (17)
Here r<sub>⊥</sub> is signed normal distance to Π, and w is a length. This best-fit-plane warpage removes rigid tilt and is not the same as maximum nodal displacement, datum-based deviation or minimum-zone flatness. Comparison with published warpage requires the same convention, evaluation region and state; incompatible definitions must not be silently equated.

Mechanical diagnostics will include the contact-pressure history, reactions and cooled/released stress fields with a declared stress measure. A von Mises value alone is not an anisotropic PLA failure criterion or a prediction of tensile strength. No allowable pressure or stress is assumed without material evidence. Part-temperature histories must retain extraction location, time and reference frame.

<!-- PAGE -->
### 6. Numerical verification and independent validation

Verification must establish that the implemented equations and discretization produce sufficiently resolved responses. It cannot establish that those equations represent a particular printed material. Stage 8 verifies one transient thermal reference problem; production mesh, time-step and contact convergence remain unperformed.

### 6.1. Verification protocol

The executed reference is a 1 mm × 1 mm × 10 mm wall with adiabatic side faces and equal convection on its two z faces. Declared verification constants are k = 0.5 W m<super>−1</super> K<super>−1</super>, c<sub>p</sub> = 1000 J kg<super>−1</super> K<super>−1</super>, ρ = 1000 kg m<super>−3</super> and h = 5 W m<super>−2</super> K<super>−1</super>. They are numerical fixtures, not PLA properties. With half-thickness L = 0.005 m, Bi = hL/k = 0.05. The body begins uniformly at 20 °C; the ambient ramps to 80 °C over 0–300 s, remains at 80 °C through 900 s, ramps to 20 °C over 900–1200 s and remains at 20 °C through 1800 s. This schedule tests initial state, heating, approach/hold and cooling without imposing an instantaneous uniform body temperature.

For the exact one-dimensional plane-wall center response,

EQ: S<sub>c</sub>(t) = 1 − ∑<sub>n=0</sub><sup>∞</sup> A<sub>n</sub> exp(−ζ<sub>n</sub><sup>2</sup>αt/L<sup>2</sup>), &nbsp; ζ<sub>n</sub> tan ζ<sub>n</sub> = Bi,<br/>A<sub>n</sub> = 4 sin ζ<sub>n</sub>/(2ζ<sub>n</sub> + sin 2ζ<sub>n</sub>), &nbsp; T<sub>c</sub>(t) = T<sub>i</sub> + ∫<sub>0</sub><sup>t</sup> S<sub>c</sub>(t − τ) dT<sub>∞</sub>(τ). &nbsp;&nbsp; (18)

The reference calculation uses 200 roots and exact integration over each linear ambient segment. MAPDL 2026 R1 used 640 mapped SOLID70 elements, 1025 nodes, 40 elements through thickness and a fixed 0.25 s step. Before the accepted run, the maximum limits were fixed at 0.05 °C absolute error and 0.25% error relative to |T<sub>ref</sub> − 20 °C|. A conventional relative error based on absolute temperature in kelvin is also reported.

TABLE: Genuine ANSYS–analytical center-temperature comparison for the plane-wall verification
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

The maximum absolute error is 0.005180700 °C, the maximum kelvin-based relative error is 0.001700533% and the maximum excursion-relative error is 0.157660518%; both predeclared acceptance limits are satisfied. Four earlier attempts remain archived: an extraction failure, two rejected time-step comparisons and a OneDrive file-mapping termination. The accepted 0.25 s case executed in local scratch and was copied back only after MAPDL closed its files. This verifies the linear conduction, convection, ramp/hold/cooling history and extraction implementation. It is neither production time-step convergence nor physical validation.

Radiation is omitted from this benchmark to preserve the linear analytical boundary. No fixture interface exists in the reference case. The production contract requires a radiation relevance decision, the sourced temperature-dependent AISI 304 properties and PLA–steel thermal-contact conductance. It rejects execution because compatible Prusament k(T) and c<sub>p</sub>(T), convection, emissivity/enclosure history, contact conductance, hold-attainment rule and production extraction definitions remain unresolved. No missing input is set to zero.

Future spatial refinement must track directional dimensions, warpage, contact loading and selected stress measures while retaining the same physical setup. Time-step refinement must resolve ramps, contact transitions and release. Changes in nonlinear tolerances, penalty stiffness or stabilization require separate assessment. Failed cases and unconverged fields cannot enter optimization as valid data.

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

Preference aggregation is deferred. The primary decision target is the conditional Pareto comparison; no desirability function or weights are selected for implementation. The established multiple-response literature [4] remains context for any later, explicitly justified preference rule.

Candidates selected through a surrogate must be recomputed with the genuine solver and assessed against the same verification and feasibility requirements. Such recomputation confirms the numerical candidate, not physical validity. This stage reports neither a Pareto front nor an optimum.

<!-- PAGE -->
### 8. Evidence status, engineering relevance and limitations

The current contribution includes a finalized computational scope, a formulation-audited property database, a tested material-point reference implementation, a parameterized three-volume geometry and an analytically verified transient thermal reference. Prusament PLA is the reference constitutive formulation, and AISI 304 is the candidate fixture material. The verification result establishes code behavior for a declared plane wall; it does not establish a PLA prediction. Missing production evidence is represented by explicit blocked fields rather than zero values, example contours or synthetic data.

TABLE: Evidence required for reportable findings
Claim family | Current evidence | Admission requirement
Temperature and deformation | One accepted ANSYS plane-wall verification; no PLA coupon solution or deformation field | Compatible production properties, boundary history, verified discretization and archived outputs
PLA transient thermal response | No compatible Prusament k(T) or c<sub>p</sub>(T) | Compatible functions or a declared calibration/uncertainty strategy
Bulk irreversible strain | Only thin-bilayer programmed pre-strain for Prusament | Identifiable signed three-dimensional law without double-counting
Stress and contact pressure | No model or fields | Verified contact solution and declared extraction rules
Numerical convergence | Not performed | Genuine mesh/time/contact refinement evidence
Physical predictive validity | No accepted dataset | Independent compatible observations and uncertainty
Sensitivity and uncertainty | Not calculated | Justified inputs and reproducible numerical analysis
Optimization | Not performed | Verified responses, feasibility rules and solver confirmation

A reliable prediction of released geometry could support decisions for planar guides, locating features and similar tolerance-sensitive parts. This is potential utility, not demonstrated qualification. A selected gap would remain conditional on part dimensions, fixture material, heating/cooling history, initial printed state and the validated material domain. No cost saving, production reliability or service-safety claim follows from the present framework.

Material identifiability remains the principal scientific limitation. The tested grade-specific relaxation core does not supply the missing transient-thermal or bulk irreversible-strain laws, and the fixture expansion convention remains unresolved. Sparse final dimensions may not uniquely distinguish residual-stress relaxation, directional recovery and crystallization-related effects. A calibrated law may match those dimensions while predicting different stresses. Contact and thermal boundaries introduce additional uncertainty, and a homogenized continuum may omit road-scale deformation or damage. These limitations must constrain the interpretation of later computed fields.

Only 80 °C lies inside the direct 23–85 °C Prusament characterization interval. The 95 °C and 110 °C candidates remain outside that interval and are not admitted by extrapolation. Aging, moisture, fatigue, service creep, damage and strength are outside current evidence. Geometry transfer also requires validation.

### 9. Conclusions

The literature establishes prior supported annealing, irreversible strain analysis, thermo-viscoelastic finite elements and annealing-related optimization. Stage 5 fixes and implements the supported Prusament viscoelastic core and the AISI 304 interpolation/elastic relations, while preserving grade boundaries. Stage 7 selects the literature-traceable 60 mm × 10 mm × 4 mm plate and two 70 mm × 20 mm × 5 mm fixture plates. Five normalized screening clearances span γ = 0–0.02, equivalent to g<sub>0</sub> = 0–0.08 mm. A geometry-only MAPDL build at γ = 0.01 created and saved the intended three volumes without a mesh or solution.

Stage 8 adds a genuine MAPDL transient thermal reference solution. For the declared plane-wall cycle, the maximum center-temperature difference from the 200-term analytical solution is 0.005180700 °C; the maximum kelvin-based relative error is 0.001700533%, and the maximum excursion-relative error is 0.157660518%. The accepted 0.25 s case satisfies the predeclared 0.05 °C and 0.25% limits. These are verification values for numerical fixtures, not Prusament material response or independent physical validation.

The Prusament evidence provides ν, α, T<sub>g</sub>, a 23-branch Maxwell spectrum and WLF/Arrhenius shifting over a directly characterized 23–85 °C interval. Thirty-eight analytical and synthetic unit tests verify the reference material relations. Compatible k(T), c<sub>p</sub>(T), complete orthotropy, crystallization kinetics and a bulk irreversible-strain law remain unavailable; fixture thermal strain awaits its expansion convention.

The proposed contribution remains restricted to evidence-tested prediction of the clearance–distortion–stress trade-off after cooling and release. The scope compares FREE with initially centered GAP restraint for one specified material/architecture/geometry, while retaining signed response and excluding granular-media simulation and unverified strength claims.

Numerical findings require genuine ANSYS field execution, verified material evidence, discretization assessment and independent validation. The successful geometry-only build is not a thermal or mechanical simulation result, and γ = 0.01 is not a preferred clearance. No improvement, validated prediction or preferred annealing condition is concluded.

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

[36] Prusa Polymers a.s. <i>Technical datasheet: Prusament PLA</i>. Version 1.1, 27 July 2022. <link href="https://prusament.com/materials/pla/" color="#24576b">prusament.com/materials/pla</link>.

[37] Luca Luberto, Volker Böß, Kristin M. de Payrebrune. Finite Difference Modeling and Experimental Investigation of Cyclic Thermal Heating in the Fused Filament Fabrication Process. <i>3D Printing and Additive Manufacturing</i> 11(3), e1064–e1072 (2024). <link href="https://doi.org/10.1089/3dp.2022.0282" color="#24576b">doi:10.1089/3dp.2022.0282</link>.

[38] Longhui Meng, Aqib Mashood Khan, Yicai Shan, Khalid A. Al-Ghamdi. Saturation behavior and full-field reconstruction of residual stress in quenched AISI 304 stainless steel via the contour method. <i>Scientific Reports</i> 16, 11694 (2026). <link href="https://doi.org/10.1038/s41598-026-45542-w" color="#24576b">doi:10.1038/s41598-026-45542-w</link>.

[39] ANSYS, Inc. <i>Mechanical APDL Theory Reference</i>, Release 2026 R1, §4.9, Viscoelasticity. <link href="https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_thry/thy_mat6.html" color="#24576b">Official theory reference</link>. Accessed 12 September 2026.

[40] Ansys, Inc. <i>Ansys Student — Free Software Download</i>, 2026 R1 product page. <link href="https://www.ansys.com/en-in/academic/students/ansys-student" color="#24576b">Official product page</link>. Accessed 13 September 2026.

<!-- PAGE -->

### Supplement A. Provenance and reproducibility requirements

The project repository is <link href="https://github.com/VorteXEkansh/FDM-Annealing" color="#24576b">VorteXEkansh/FDM-Annealing</link>. It contains the DOI-verified literature matrix, novelty audit, search strategy, base-paper audit, the manuscript restructuring map, the complete current source, the authoritative research-state record, the property database, constitutive implementation/tests, parametric geometry and Stage 8 thermal-verification evidence. The base paper is preserved separately from the evolving manuscript. Solver artifacts include the accepted plane-wall thermal field result and all failed attempts; no production PLA field result exists.

Each future case must preserve a unique identifier, the solver version, geometry and material orientation, input configuration, source references, units, boundary histories, mesh, time-integration and contact settings, execution status, raw-output location and file checksums. Failed cases remain in the record with their failure reason. Postprocessing must identify both the raw field and the script/equation producing each response.

Every quantitative result will be assigned to one of three evidence classes: A, genuine solver output; B, a reproducible numerical calculation; or C, a verified published source with an exact locator. Design choices remain labeled as inputs, never as findings. The temperatures and durations in Table 3 are inherited design choices; its nine-combination count follows directly from three temperature levels multiplied by three duration levels.

The bibliography is deliberately limited to the checked sources cited in this draft. The larger bibliography in the base proposal is archived for later appraisal and is not treated as a validated material database. Each Stage 4 numerical property has a source locator, formulation decision and intended ANSYS treatment in the repository. No cross-formulation value is admitted merely because it falls within a plausible PLA range.

Author names and affiliation follow the supplied base paper. Authorship contributions, funding and submission declarations require author confirmation before journal submission; no such declarations are inferred here.
