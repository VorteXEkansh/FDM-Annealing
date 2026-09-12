# Stage 5 reference constitutive formulation

This document defines the implemented material relations, numerical conventions and intended ANSYS mapping. Material coefficients come exclusively from the maintained CSV database. The authoritative decision is `docs/constitutive_model_decision.md`. No finite-element solver is executed in this stage.

## Variables and units

The reference implementation uses small symmetric strain, Cauchy stress in MPa, moduli in MPa, time in seconds and temperatures supplied in °C. Symmetric tensors are ordered (xx, yy, zz, xy, yz, xz) with **tensor shear strain**. An ANSYS interface using engineering shear must divide its shear-strain components by two before applying these tensor functions; stress components do not receive that factor. Material reference temperature is 23 °C for code verification; the shift reference is Tᵍ = 65 °C. Temperature calls outside 23–85 °C raise `EvidenceGapError`.

## Selected strain accounting

ε = εᵉ + εᵛᵉ + εᵗʰ + εᵃⁿⁿ; εᵐ = ε − εᵗʰ − εᵃⁿⁿ.

Operationally, εᵉ = Cᵢₙₛₜ⁻¹ : σ and εᵛᵉ = εᵐ − εᵉ. `strain_parts` implements this identity. The effective delayed strain need not equal an individual branch dashpot strain. The simpler elastic-plus-thermal-plus-annealing decomposition is the limit with no delayed component; it is not sufficient to represent the published relaxation.

The branch implementation tracks stresses. For interpretation, each Maxwell branch has σᵢ = Cᵢ : (εᵐ − zᵢ), where zᵢ is that branch's dashpot strain. Positive branch moduli and relaxation times give nonnegative dissipation. The tests check this through the positive quadratic form σᵢ : Cᵢ⁻¹ : σᵢ / τᵢ. No separate macroscopic viscosity or creep coefficient is added.

## Thermal strain

For the constant source coefficient, εᵗʰ(T) = α(T − Tᵣ)I with α = 68.0 × 10⁻⁶ K⁻¹. `thermal_strain` implements the same relation on heating and cooling. It is isotropic and reversible. The source provides no independent αₓ(T), αᵧ(T), α𝓏(T) functions or bulk annealing strain. Do not use irreversible shrinkage to modify this expansion coefficient.

`annealing_strain` always raises an evidence-gap error. The intended εᵃⁿⁿ is an irreversible, signed, history-dependent stress-free distortion relative to the common reference state. There is no supported magnitude, tensor orientation law or rate law. Scalar free shrinkage or thin-bilayer programmed pre-strain cannot identify a general tensor field. No constitutive parameter for it is fabricated. Reference tests explicitly omit that mechanism; production does not.

## Isotropic generalized-Maxwell core

For any symmetric tensor A, C(E,ν) : A = 2G A + λ tr(A)I, with G = E/[2(1+ν)] and λ = Eν/[(1+ν)(1−2ν)]. The equilibrium tensor uses E∞ = 10.598 MPa; each branch uses its tabulated kᵢ; all use ν = 0.35.

σ = C∞ : εᵐ + ∑ᵢ σᵢ,

∂σᵢ/∂ξ + σᵢ/τᵢ = Cᵢ : ∂εᵐ/∂ξ.

The kernel is Eᵣ(ξ) = E∞ + ∑ᵢ kᵢ exp(−ξ/τᵢ). For an isothermal elapsed time t, ξ = t/aₜ. `relaxation_modulus`, `stress` and `advance_reduced` implement these relations. The 23 branches are read from the database without refitting or pruning.

Eᵢₙₛₜ = E∞ + ∑ᵢkᵢ = 1691.594 MPa. Define gᵢ = kᵢ/Eᵢₙₛₜ. The corresponding instantaneous shear and bulk moduli are Gᵢₙₛₜ = Eᵢₙₛₜ/[2(1+ν)] and Kᵢₙₛₜ = Eᵢₙₛₜ/[3(1−2ν)]. Both normalized kernels use gᵢ with identical τᵢ. The long-term fraction is E∞/Eᵢₙₛₜ. `normalized_prony` and `shear_bulk` implement the conversion. An independent, constant bulk modulus with only shear relaxation changes ν and is not this model.

No independent E(T) curve is multiplied by these kernels. The instantaneous and equilibrium coefficients remain those of the thermorheologically simple model; apparent stiffness at a fixed loading duration changes with temperature through reduced time. The room-condition supplier tensile moduli cannot substitute for the instantaneous relaxation modulus. Complete FFF orthotropy, evolving anisotropy, plasticity, damage and finite-strain response are excluded.

## Temperature shift and non-isothermal history

log₁₀aₜ = C₃(1/Tₖ − 1/Tᵍₖ) below 65 °C;

log₁₀aₜ = −C₁(T − Tᵍ)/[C₂ + T − Tᵍ] at or above 65 °C.

Tₖ and Tᵍₖ are absolute kelvin; C₁ = 17.4, C₂ = 51.6 K and C₃ = 35 000 K. The two expressions meet continuously at aₜ = 1, but need not have the same derivative. WLF is used only on 65–85 °C; Arrhenius is used on 23–65 °C. These constants come from Chapuis supplementary Table B.1 and Eq. (6), not universal WLF constants. The archived source UMAT independently confirms the base-10 exponent, sign and multiplication of τᵢ by aₜ.

ξ(t) = ∫₀ᵗ [aₜ(T(s))]⁻¹ ds. A current-temperature substitution t/aₜ(T(t)) is valid only for an isothermal history. `reduced_time` applies composite Simpson quadrature to a specified linear-temperature ramp and splits at 65 °C. Its numerical panel count is a quadrature choice, not a material parameter or validated thermal history.

For a substep linear in reduced time:

rᵢ = Δξ/τᵢ, Aᵢ = exp(−rᵢ), Bᵢ = [1−exp(−rᵢ)]/rᵢ,

σᵢⁿ⁺¹ = Aᵢσᵢⁿ + BᵢCᵢ : Δεᵐ.

`advance_reduced` implements this exact exponential increment. It evaluates Bᵢ using `expm1` to avoid cancellation and preserves state between calls. `advance` uses a midpoint frozen-temperature estimate Δξ = Δt/aₜ((Tⁿ+Tⁿ⁺¹)/2), with linear mechanical strain on the substep. It rejects a substep that crosses Tᵍ; callers split there. This approximation is exact for an isothermal linear-strain increment and must be refined for a general coupled ramp. The tests demonstrate material-point refinement, not ANSYS time-step convergence. Neither the authors' old-temperature update nor this midpoint reference is represented as an exact arbitrary-temperature solution.

## Fixture relations

For each tabulated property p, p(T) = pₐ + (pᵦ − pₐ)(T − Tₐ)/(Tᵦ − Tₐ), within adjacent source knots. `fixture_property` implements this without extrapolation beyond 20–200 °C. `fixture_elastic_stress` uses interpolated E and ν, converting GPa to MPa. Density, conductivity and heat capacity are only interpolated property lookups; no thermal field is solved.

The source does not resolve whether tabulated α is tangent or mean relative to a stated temperature. `fixture_thermal_strain` raises an evidence-gap error; there is no silent integral or secant interpretation. The eventual fixture thermal-strain law and ANSYS expansion convention must be specified before operating clearance is predicted. All 18 source property values remain unchanged.

## Crystallization and thermal balance

There is no crystallization state variable, kinetic equation, Avrami exponent, latent heat or crystallization-strain coupling in the admitted code. The physical mechanism is not asserted to be absent. A future coupled thermal calculation without its heat contribution must justify that omission for the chosen grade and path. No isothermal Avrami expression is evaluated along a changing temperature history.

The manuscript's transient heat balance, quasi-static equilibrium and contact complementarity are the designated future ANSYS field equations; their material closures or boundary data are not ready. They are mapped explicitly to implementation targets in `docs/equation_implementation_map.csv`. Code-verifiable material equations are distinguished from field equations that require genuine solver execution.

## Numerical verification and provenance

Run `python scripts/check_constitutive.py`. It executes 38 analytical/synthetic tests and records individual outcomes plus input/code hashes in `docs/stage_05_constitutive_tests.json`. Failed runs, if any, remain in `tests/failure_records/` by content hash. No failed run is discarded or relabelled as a successful physical simulation.

Tests cover source sums; shift signs, base and continuity; temperature rejection; reversible expansion; Prony normalization and limits; shear/bulk consistency; stiffness/compliance inversion; engineering/tensor shear; hydrostatic and plane-stress limits; effective strain partition; analytical step relaxation and ramp response; partition invariance; zero loading/free heating; restrained-heating sign; reduced-time quadrature; ramp refinement; positive dissipation; small-step stability; unresolved mechanisms; and fixture interpolation/units.

Synthetic strain magnitudes, durations, constitutive test coefficients and subdivisions are explicitly numerical fixtures. They do not enter the material database and do not constitute calibration or validation data. Passing these tests verifies algebra and code behavior; the ANSYS adapter and physical applicability remain open.
