# Stage 5 constitutive-model decision

Date: 12 September 2026. Scope: Prompt 5 only.

## Decision and evidence boundary

The strongest presently parameterized model is a small-strain, isotropic, thermorheologically simple generalized-Maxwell reference model for Prusament PLA. Its 23 source branches, equilibrium modulus, constant Poisson ratio, constant linear expansion and piecewise Arrhenius/WLF shift are implemented in `src/constitutive.py`. This is a material-point implementation for analytical verification. A complete production thermo-mechanical annealing model is **not supportable yet**. `production_annealing_model()` raises an evidence-gap error.

The constitutive architecture is fixed for implementation work, while its permission to predict the research endpoints remains conditional. No ANSYS availability, compiled user-material routine, contact model or finite-element result is claimed. The paper must not describe this as a validated constitutive law for bulk annealed PLA.

## Evaluated alternatives

| Option | Assessment | Decision |
|---|---|---|
| ε = εᵉ + εᵗʰ + εᵃⁿⁿ with elastic stress | A useful thermoelastic limit, but no supported bulk εᵃⁿⁿ law exists; omits source-supported relaxation | Retain the elastic limit only as an analytical check, not the selected annealing law |
| ε = εᵉ + εᵛᵉ + εᵗʰ + εᵃⁿⁿ | Includes the supported history dependence; εᵛᵉ must have an operational definition for a parallel network | Select the viscoelastic core; εᵃⁿⁿ remains an unparameterized production requirement |
| Source programmed pre-strain with balanced branch stresses | Chapuis et al. calibrate thin laminate recovery, not this bulk coupon/print architecture | Do not transfer the calibrated values or silently initialize internal stresses |
| Three-dimensional orthotropic viscoelasticity | No complete same-grade elastic, expansion or relaxation tensor data | Exclude at this stage; the isotropic extension is an explicit assumption |
| Additional temperature-dependent E(T) multiplied by shifted Prony response | No separate same-grade vertical modulus shift is identified; this can double-count temperature dependence | Exclude; temperature acts through the relaxation clock |
| Shear-only Prony response with constant bulk modulus | Does not preserve the selected constant Poisson ratio | Reject as an equivalent implementation; use identical fractional shear and bulk kernels for this closure |
| Isothermal Avrami or non-isothermal crystallization model | No compatible initial crystallinity or kinetic parameters; a changing temperature is not an isothermal dwell | Exclude; do not evaluate an isothermal Avrami expression at instantaneous ramp temperature |
| Arbitrary empirical shrinkage, residual stress or cross-grade coefficients | Unidentified and potentially double-counted with relaxation/recovery | Exclude |

## What “supported” means here

Chapuis, Teufen and Shea (2025), DOI 10.1088/1361-665X/adeee4, §§2.1–2.2, Eq. (6), supplementary Tables B.1–B.2 and the supplied `UMAT_SMPViscoShells.f`, support the source spectrum and shift convention. The source's executable routine implements a plane-stress shell branch. The present three-dimensional isotropic tensor core is a mathematical extension with the same constant-Poisson closure, not a verified three-dimensional version of the authors' solver. A plane-stress reduction test reproduces that stiffness algebra.

The 23–85 °C direct characterization interval is a temperature admission envelope, not proof of validation for every duration, strain amplitude, ramp rate or bulk geometry. The 30 min, 60 min and 90 min design holds still need time-domain evidence. The 95 °C and 110 °C conditions and a 20 °C PLA starting state are rejected by the reference API. Test reference temperature is explicitly 23 °C; the relaxation reference is 65 °C. Neither fixes the final production thermal cycle.

At each source temperature, the frequency characterization was 1–18 Hz. Time–temperature superposition and the published fitted master curve motivate the relaxation representation, but analytical tests cannot extend physical validity beyond independently supported observations. This stage provides no new confidence intervals or uncertainty distribution.

## Implementation consequences

- Normalize branch moduli by the instantaneous modulus, not by the equilibrium modulus. Both the volumetric and deviatoric kernels use the same fractional spectrum to retain constant ν. This is a closure assumption, not an independent bulk-relaxation measurement.
- Retain the source's base-10 shift convention and absolute kelvin in the Arrhenius branch. Use the full reduced-time history; current temperature cannot replace an entire heating/cooling path.
- Do not translate the authors' ABAQUS UMAT directly into an ANSYS material card. The future adapter must establish installed-release conventions, strain/shear ordering, stress-state initialization and temperature-shift direction, then pass the reference tests and genuine ANSYS material-point benchmarks. ANSYS 2026 R1 Theory Reference §4.9 provides the convention check; it does not establish the installed version.
- A single native WLF branch is not equivalent over the full envelope. The full piecewise clock requires a verified custom or otherwise equivalent representation. No unsupported ANSYS command sequence is generated here.
- The macro εᵛᵉ is computed from instantaneous compliance and network stress. It is not an independently added creep law. Branch dashpot strains differ, and their sum is not the macroscopic delayed strain.
- Zero annealing strain and zero initial branch stresses are allowed only in identified reference tests. Missing production recovery is never defaulted to zero. A fully relaxed, stress-free Maxwell solid with positive equilibrium stiffness cannot generate permanent bulk annealing shrinkage from a reversible free thermal cycle.

## Fixture and reproducibility corrections

AISI 304 property interpolation and instantaneous isotropic stiffness are implemented from Meng et al. (2026), Table 1, DOI 10.1038/s41598-026-45542-w. Its tabulated expansion coefficient does not clearly identify a tangent coefficient or a mean coefficient with a reference temperature. Interpolating the table is testable; integrating it into fixture thermal strain is blocked until that convention is resolved. This qualifies the Stage 4 assumption and prevents an unsupported hot-clearance prediction.

Three comparator evidence files previously referenced an ignored `tmp/` directory. Immutable byte copies are now archived in Stage 5 evidence and the database points there. Git attributes preserve raw evidence and hashed generated bytes, including original line endings. The Stage 4 SUNLU relaxation-source author field was corrected against its archived DOI metadata to Bertocco et al.; the source values are unchanged. Prior stage records remain historical.

## Admission gates still open

Compatible PLA thermal functions; an identifiable signed bulk irreversible-strain law or justified printed-state recovery initialization; independent calibration/validation separation; duration and strain-amplitude applicability; crystallization omission assessment; fixture expansion convention; installed ANSYS adapter and genuine solver material-point checks; finite-deformation assessment; contact/boundary/geometry evidence. Passing code unit tests closes none of these physical-evidence gates. Prompt 6 is not started.
