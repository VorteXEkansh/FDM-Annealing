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

The primary study will use one identified FFF-PLA formulation, one fixed print architecture and one representative three-dimensional plate-like coupon geometry selected for evidence compatibility. Dimensions, grade and property tables are implementation choices still to be established; scope finalization does not supply missing material data. The formulation will retain material directions and a justified irreversible/history-dependent response. It will not require a complete simulation of nozzle deposition: initial printed-state evidence may instead support a calibrated recovery representation without double-counting initial stress.

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

The scope is finalized as a computational research commitment. Solver availability, grade selection, numerical parameters and validation datasets remain open implementation items; no ANSYS results, accepted material law or completed verification are supplied by this stage.

<!-- PAGE -->
