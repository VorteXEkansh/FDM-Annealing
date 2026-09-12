# Stage 4 material-property audit

Date: 2026-09-12

Scope: Prompt 4/20 only

## Decision

Prusament PLA is the reference formulation for constitutive development because Chapuis, Teufen and Shea report grade-specific dynamic mechanical characterization, a 23-branch generalized Maxwell representation, a piecewise WLF/Arrhenius shift law, Poisson ratio, thermal expansion and process-specific programmed pre-strain. The directly characterized temperature interval is 23–85 °C. This decision admits the 80 °C candidate condition for later implementation studies but does not, by itself, admit 95 °C or 110 °C.

The database is deliberately incomplete for a production annealing simulation. No compatible temperature-dependent density, conductivity or specific-heat functions were located for Prusament PLA. The supplier reports a typical density but not its test temperature. The grade-specific source reports thin-bilayer programmed pre-strain, not a signed three-dimensional bulk annealing-strain law. No complete grade-specific orthotropic stiffness/expansion set or crystallization-kinetic parameter set was located. These fields remain blocked rather than being filled from another PLA.

AISI 304 stainless steel is the candidate plate-fixture material. Meng et al. tabulate ρ(T), cₚ(T), k(T), α(T), E(T) and ν(T) at 20 °C, 100 °C and 200 °C, which brackets the planned 20–110 °C cycle. These values are candidate engineering inputs for the fixture only; the actual alloy heat, plate thickness, surface finish and contact conductance remain future design choices.

## Evidence classes

| Class | Meaning | Current examples |
|---|---|---|
| Admissible within source domain | Same named PLA formulation and directly reported model quantity | Prusament ν, α, T_g, k₀, 23 Maxwell branches, WLF/Arrhenius constants over the characterized 23–85 °C interval |
| Calculated candidate | Deterministic calculation from directly tabulated values | E₀ = k₀ + ∑kᵢ = 1691.594 MPa; normalized branch fractions retained in row notes |
| Screening only | Same grade but missing temperature or time-scale information | Prusament supplier density and room-condition printed tensile moduli |
| Not a bulk annealing input | Same grade but geometry-calibrated for direct 4D-printing bilayers | ε₁₁^AM values in Chapuis et al. Table 5 |
| Incompatible comparator | Different or unidentified PLA formulation | Luberto thermal constants, SUNLU PLA Plus relaxation, FormFutura orthotropy |
| Incompatible source mixture | A published FE table that itself combines one filament with functions/data from other literature | Raise3D table in Trofimov et al. |
| Unresolved | No compatible bounds or parameters found | Prusament k(T), cₚ(T), complete orthotropy, bulk irreversible strain, crystallization kinetics |

## Grade-specific constitutive evidence

Chapuis et al. used at least three ASTM D638 Type IV specimens per material and frequency sweeps from 1 Hz to 18 Hz in 5 °C increments between 23 °C and 85 °C for Prusament PLA. Their supplementary Table B.1 reports k₀ = 10.598 MPa, ν = 0.35, T_g = 65 °C, C₁ = 17.4, C₂ = 51.6 K, C₃ = 35 000 K and α = 68.0 µm m⁻¹ K⁻¹. Supplementary Table B.2 reports 23 pairs of branch stiffness kᵢ and reference relaxation time τᵢ.

The arithmetic instantaneous reference modulus is

E₀ = k₀ + ∑ᵢ₌₁²³ kᵢ = 1691.594 MPa.

For later ANSYS work, the Maxwell data must be converted to the convention required by the selected element/material model and verified against the source relaxation curve. Assuming constant ν may permit the normalized Young-modulus fractions kᵢ/E₀ to equal the normalized shear-relaxation fractions, but that equivalence is not yet accepted as an implementation result. The published shift law is piecewise: Arrhenius below T_g and WLF at or above T_g. A native ANSYS command set or tabulated shift function must reproduce the same sign, logarithm base, reference temperature and time scaling before use.

Chapuis et al. Table 5 reports ε₁₁^AM from 0.04199 to 0.10350 across different nozzle/activation conditions and two identification methods. Those values were fitted to thin bilayers for a direct shape-memory model. They are not uncertainty bounds for a bulk printed coupon and cannot be added to a residual-stress field without an identifiability check.

## Thermal-property gap

Luberto et al. report ρ = 1240 kg m⁻³, cₚ = 1800 J kg⁻¹ K⁻¹ and k = 0.13 W m⁻¹ K⁻¹ at 20 °C for an unidentified PLA filament, then hold them constant in a printing heat-transfer model up to 140 °C. Trofimov et al. report a temperature-dependent simulation table for Raise3D Premium PLA, but state that room-temperature mechanical measurements were reduced with another source's function and that thermal properties came from literature. Neither dataset is transferred to Prusament PLA.

The absence of compatible k(T) and cₚ(T) prevents a defensible production transient-thermal calculation. A later stage may either obtain grade-specific measurements/data, select another single formulation with a complete compatible dataset, or introduce a clearly declared calibration/uncertainty strategy. Cross-grade minima and maxima are not treated as probability bounds.

## Orthotropy and thermal expansion

Li, Xu and Fang report E₁, E₂, E₃, ν₁₂, ν₁₃, G₁₂ and G₃₁ for unidirectional FormFutura Premium PLA. Their Table 4 does not provide G₂₃ or ν₂₃, and the grade/road geometry differs from the selected Prusament evidence set. The values remain comparators and do not complete an ANSYS orthotropic matrix. No compatible α₁, α₂ and α₃ set was found.

The Prusament source therefore supports only an isotropic viscoelastic candidate at this stage. This is a model-scope decision, not evidence that FFF PLA is isotropic.

## Stress relaxation, WLF and Prony evidence

Giannella et al. measured relaxation of SUNLU PLA Plus at three infill orientations for 500 s and compared Maxwell, standard-linear-solid and Findley fits. The paper reports about 11–13% normalized modulus decay across the orientations, but it does not supply an annealing-temperature Prony/WLF law for Prusament PLA. It remains model-selection context.

The WLF constants in the database are taken from the grade-specific Chapuis source. The Williams–Landel–Ferry paper supplies the general theory, not the numerical constants used here.

## Irreversible strain and crystallization

Bute et al. directly demonstrate signed directional irreversible thermal strain in Black Devil Design PLA and separate first-cycle recovery from subsequent expansion. This supports the mechanism and response definition, but it does not supply a transferable Prusament law. Most values are graphical and were not digitized in Stage 4.

Pantani et al. and Sorrentino and Pantani establish formulation- and history-dependent crystallization kinetics. No coefficient is imported because the grade and thermal-path compatibility with Prusament PLA have not been established. A crystallization heat source or evolution law is therefore absent from the current ANSYS candidate model.

## Uncertainty policy

`material/uncertainty_ranges.csv` records only source-supported intervals and method brackets. It assigns no probability distribution. When a compatible lower and upper bound is absent, both are left blank with status `no bound invented`. Supplier ± intervals are retained as reported; they are not automatically interpreted as standard deviations or confidence intervals.

## Files and reproducibility

- `material/pla_properties.csv`: 96 property records with formulation, temperature, source, confidence, compatibility and intended ANSYS treatment.
- `material/property_sources.csv`: 11 audited sources with exact locators and evidence hashes.
- `material/uncertainty_ranges.csv`: reported intervals, same-source method brackets and explicit unresolved gaps.
- `material/fixture_properties.csv`: 18 AISI 304 fixture-property records at 20 °C, 100 °C and 200 °C.
- `material/build_manifest.json`: script, raw-evidence and output hashes plus arithmetic checks.
- `scripts/build_material_database.py`: deterministic database generator.

No ANSYS material card, solver input or numerical result is created in this stage.
