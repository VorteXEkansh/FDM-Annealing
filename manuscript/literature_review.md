### 1.1. Evidence base and scope of the review

The literature investigation was updated through 12 September 2026 using publisher records, author repositories, Europe PMC full text and DOI registration metadata. The evidence matrix records 34 journal papers, their bibliographic verification, accessible methods, missing fields and intended use. This is a critical, targeted investigation, not a claim of exhaustive systematic-review coverage. DOI verification establishes bibliographic identity; it does not establish methodological quality, transferable properties or independent validation.

The closest work falls into three overlapping groups: supported thermal post-processing, prediction of printing or thermally activated deformation, and annealing-related mechanical optimization. The intersection matters more than any one keyword. A support medium is mechanically different from a plate fixture, printing-induced distortion differs from post-print recovery, and a thermodynamic constraint in a learning algorithm is not physical fixture restraint.

### 1.2. What annealing and support studies already establish

Wach et al. [@Wach2018], Benwood et al. [@Benwood2018], Butt and Bhaskar [1], and Stojković et al. [2] establish substantial prior work on thermal post-treatment and printed-polymer response. Their findings motivate a material-specific balance between dimensional stability and mechanical behavior. They do not justify assuming that all PLA grades benefit from the same cycle. Work on porosity, crystallinity and interlayer adhesion [@Windheim2021], including competition between crystallization and bonding [@Bonding2024], further challenges a simple rule that greater crystallinity necessarily means a stronger printed part.

Constrained annealing has already been studied. Lluch-Cerezo et al. [@Mould2022] compared alumina-powder mould support with unsupported treatment and measured directional dimensions and flexural behavior. Wijnbergen et al. [@Wijnbergen2021] examined different annealing media for tough PLA, including sand. Mould-supported processing [@Moulds2022] and salt-assisted annealing/remelting [@Salt2022] are additional precedents. Remelting outcomes belong to a different physical regime and cannot establish performance of the proposed sub-melting process.

Chiscop et al. [@Encapsulation2025] extended encapsulation-based thermal processing to several geometries using tough PLA. De Assis et al. [@HighHeat2026] connected thermal conditioning, dimensional response and mechanical prediction for high-heat PLA. These formulations cannot be treated as interchangeable with neat PLA. Together, the studies rule out novelty based on support, dimensional preservation, annealing itself or combining dimensional and mechanical endpoints.

The powder-mould source also illustrates why exact extraction matters: its PLA treatment tables identify a final temperature of 155 °C, whereas its Table 7 labels the final PLA row 240 °C [@Mould2022, Tables 2–3 and 7]. The inconsistent row is not accepted as validation data. A plausible correction is not a verified observation.

<!-- PAGE -->
### 1.3. Thermo-mechanical prediction and irreversible response

Wijnen et al. [@Wijnen2018] developed a deformation model for printed PLA walls, calibrated thermal behavior and compared predicted curvature with measurements; they also examined directional annealing changes. Trofimov et al. [@Trofimov2022] used sequential thermal and mechanical simulations and separate temperature and distortion comparisons. These are direct precedents for coupled process modeling and physical comparison. Ramos et al. [@Heat2023] addressed computational efficiency and thermal validation through adaptive treatment of the deposition mesh.

Bute et al. [@Bute2024] are particularly close to the present problem. They measured irreversible directional thermal strain and distinguished it from expansion during a subsequent thermal cycle. Their ANSYS printing simulations related residual thermal stress to observed recovery. Therefore, neither irreversible annealing strain nor an ANSYS connection between stress and deformation is new. Correlation with printing stress, however, does not by itself demonstrate a predictive annealing-contact law under a variable fixture clearance.

The shape-memory study of Issabayeva and Shishkovsky [@Prediction2023] incorporates thermomechanical characterization and ANSYS modeling with a Prony representation and temperature shifting. Chapuis et al. [@Laminate2025] provide an even stronger constitutive precedent: programmed pre-strain, a modified generalized Maxwell formulation and laminate finite elements predict thermally activated shape change and mechanical response. A first-use claim for temperature-dependent PLA recovery, Prony series, WLF shifting or viscoelastic finite elements would therefore be indefensible.

Temperature–relaxation shifting has a much older foundation in Williams, Landel and Ferry [@WLF1955]. Its use still requires evidence that the chosen material is sufficiently thermorheologically simple over the modeled range. Relaxation measurements on printed PLA [@Relaxation2022] and temperature-dependent viscoelastic–viscoplastic behavior [@Viscoplastic2017] motivate testing the adequacy of a linear law rather than selecting one solely because ANSYS supports it. A fitted DMA curve does not independently validate released warpage or residual stress.

Jiang et al. [@SCF2023] combined thermal, thermoelastic and crystallization-kinetic models for short-carbon-fibre/PLA printing. Farh and Gribniak [@Process2025] modeled printing, cooling and detachment with temperature-dependent behavior. Coupling crystallization with mechanics, or including a release stage, cannot be claimed as new in isolation. Composite-specific data and printing-bed detachment also cannot directly validate opposed-face annealing contact.

Thermal contact remains an evidence need. Existing printing models demonstrate the importance of the thermal boundary, but their bed conditions do not supply a measured conductance for the proposed PLA–fixture interface. Clearance may change both heat transfer and mechanical engagement. Prescribed uniform part temperature would omit that interaction; one-way thermal loading is defensible only if its adequacy is demonstrated.

<!-- PAGE -->
### 1.4. Anisotropy, crystallization and competing strain mechanisms

Li et al. [@Orthotropic2024] provide direct evidence and modeling of orthotropic FFF-PLA mechanics. Raster orientation, road spacing and interlayer architecture must therefore accompany a property dataset. The road air gap in a printing study is distinct from the free clearance between an annealing fixture and the finished part. Ambient directional stiffness alone also cannot define behavior throughout heating, holding and cooling.

Crystallization kinetics depend on thermal and processing history. Pantani et al. [@Pantani2010] compared virgin and processed PLA, while nucleation/kinetic work [@Nucleation2011] and recent filament-focused analysis [@Kinetics2025] supply candidate mechanisms. These studies support distinguishing cold crystallization of a printed state from crystallization after erasing its history by melting. Phase-field work [@Phase2025] already connects thermal/morphological evolution to effective mechanics. Simultaneous deformation and annealing studies [@Deformation2025] additionally motivate checking whether mechanical restraint changes the kinetics assumed by the model.

Recent injection-moulded grade comparisons [@Grades2026] address secondary shrinkage and mechanical trade-offs. Their online publication predates this review cutoff even though the assigned issue date is later. They are useful mechanistic context, but their initial state and manufacturing route differ from FFF. No kinetic coefficient, Prony term, shift constant or annealing-strain value is transferred into the present model at this stage.

The physical distinction is consequential: reversible expansion vanishes on return to the reference state, whereas recovery and crystallization-related strain can persist. A single effective expansion curve may reproduce one heating path yet fail after cooling or under restraint. Conversely, adding independently fitted recovery and crystallization terms risks counting the same measured strain twice. Identifiability must be assessed with more than a final dimension; thermal history and compatible time-resolved observations are needed where available.

### 1.5. Optimization is established; the decision target must differ

Kahya et al. [@Kahya2025] already optimized thermal annealing for printed PLA performance. More directly, Ben Amor and Souissi [@Multiscale2026], published online in June 2026, combine multiscale finite elements, annealed/non-annealed PLA and multi-objective desirability. Their accessible publisher abstract concerns tensile behavior, raster orientation and strain rate. It does not establish prediction of released geometry under quantified annealing-fixture contact. The early unedited publication nevertheless decisively rules out claiming annealing plus finite elements plus optimization as a new combination.

A 2026 physics-informed learning study [@PINN2026] also reports annealing-aware optimization of recycled PLA. Its “thermo-constrained” terminology refers to model/optimization restrictions rather than physical fixture contact. Repeated load-curve records must not be treated as independent specimens when appraising validation. Desirability itself is established methodology [4]; novelty must lie in the physical question and supported predictive capability, not the ranking formula.

<!-- PAGE -->
### 1.6. Closest competing studies and the remaining claim

The ten closest studies were selected by overlap with the intended physical response or computational mechanism, rather than citation count. The order below is an editorial grouping, not a calculated similarity score. The complete matrix records access limits and evidence locators.

TABLE: Closest competing studies and implications for scope
Study | Established overlap | Distinction still requiring evidence
Bute et al. [@Bute2024] | Irreversible strain and ANSYS printing stress | Predictive annealing-clearance/contact relation
Chapuis et al. [@Laminate2025] | Viscoelastic pre-strain recovery FE | Fixture-controlled dimensional preservation
Issabayeva and Shishkovsky [@Prediction2023] | ANSYS, DMA, Prony and thermal response | Released fixture geometry and stress
Wijnen et al. [@Wijnen2018] | Warpage model and annealing dimensions | Quantified annealing restraint
Trofimov et al. [@Trofimov2022] | Thermal/deformation prediction and comparison | Post-print annealing contact cycle
Lluch-Cerezo et al. [@Mould2022] | Powder-supported dimensional control | Explicit clearance and contact mechanics
Wijnbergen et al. [@Wijnbergen2021] | Tough-PLA annealing media | Compatible grade and plate-gap prediction
Chiscop et al. [@Encapsulation2025] | Encapsulation across geometries | Contact-clearance response under release
De Assis et al. [@HighHeat2026] | Geometry/mechanics and thermal conditioning | Transient fixture-contact model
Ben Amor and Souissi [@Multiscale2026] | Annealed PLA, FE and optimization | Released dimensions–warpage–stress decision

The broad proposed gap is narrowed. In the accessible evidence reviewed, no study was identified that demonstrates the complete chain of a quantified initial annealing-fixture clearance, evolving thermal/mechanical contact, irreversible directional response, and a verified assessment of released dimensions, warpage and residual stress with explicit uncertainty. This is a bounded search finding, not proof of absence or a claim of priority. Partial access to several competitors limits a stronger assertion.

The defensible intended contribution is a reproducible, evidence-tested evaluation of the clearance–distortion–stress trade-off for a specified FFF-PLA material and fixture. Integrating transient thermal exposure, a justified history-dependent material law and irreversible strain is a means to that end. The contribution remains conditional: it must be demonstrated by genuine computations, numerical verification and compatible independent observations. If stress or contact cannot be physically validated, those outputs must remain conditional model predictions, with validation claims restricted to supported observables.

ASTM F3489-23 [3] remains relevant to appraisal of polymer material-extrusion mechanical data. It does not certify the proposed simulation or provide an annealing constitutive law. Published support effects, property enhancement and best processing conditions are treated as literature findings, never as results of this computational study.

<!-- PAGE -->
