# Stage 9 structural and contact verification

## Implemented scope and limits

The executable reference decks use Ansys Mechanical APDL Student 2026 R1,
build 26.1, update 20260202. Each elastic test uses one eight-node SOLID185
brick, 10 mm × 1 mm × 1 mm. These are uniform-field patch tests, not a
production specimen mesh or convergence demonstration. Orthotropy is not used:
no compatible complete directional property set is admitted.

The elastic constants E = 2000 MPa, ν = 0.3 and α = 10⁻⁵ K⁻¹ are declared
verification fixtures, not PLA measurements. Axial displacement is fixed at
x = 0. Transverse symmetry conditions fix uᵧ at y = 0 and u_z at z = 0;
they admit the exact homogeneous expansion and Poisson contraction fields.
The x = 10 mm face has coupled axial displacement, with node 2 as master.
The rest of that face is free transversely. No inertia, gravity, geometric
nonlinearity or manufacturing residual stress is included.

The thermal comparison imposes a spatially uniform temperature only to verify
the structural material response. It does not replace the Stage 8 thermal
model. The sequence begins at a stress-free thermal reference of 20 °C and
has load-step endpoints 30 °C, 80 °C and 20 °C, at pseudo-times 1, 2 and 3.
Each ramp uses ten substeps. FREE allows axial motion; FIXED restrains the
right-face axial master. Stresses are extracted from the solid element;
left-face reactions are summed over nodes 1, 4, 5 and 8.

## Analytical thermal and retained-eigenstrain relations

Let e = α(T − Tᵣ) + εᵃⁿⁿ, with L = 10 mm and A = 1 mm².
For free expansion, uₓ = Le, σₓ = 0 and Rₓ = 0.
For axial restraint, uₓ = 0, σₓ = −Ee and Rₓ = −Aσₓ.
In either case εᵧ = ε_z = e − νσₓ/E.

The retained strain εᵃⁿⁿ = −0.001 is a synthetic isotropic eigenstrain.
It is initialized by INISTATE as σᵢ = −C:εᵃⁿⁿ, giving 5 MPa in each normal
component before equilibrium for this declared elastic material. This is the
small-strain equivalent of an imposed stress-free contraction. It is present
from the first equilibrium step, retained through heating/cooling and not
regenerated from temperature. It does not represent a kinetic law or claim
that Prusament contracts by this amount. EIGEN_FIXED releases the axial
right-face restraint in a fourth step at 20 °C. No fictitious temperature
increment is used to encode the retained strain.

## Isothermal viscoelastic adapter

SOLID185 receives the 23 normalized shear and bulk branches in
material/constitutive_reference.json through TB,PRONY. E = 1691.594 MPa and
ν = 0.35 are the source-derived reference values; both spectra use the same
fractions. This retains the Stage 5 assumption of constant ν in the
three-dimensional extension. The source is Chapuis et al. (2025), DOI
10.1088/1361-665X/adeee4, supplementary Tables B.1–B.2. Temperature and TREF
are both 65 °C. No temperature-shift law is invoked in this isothermal check.
The full piecewise non-isothermal clock is still unverified in ANSYS.

The prescribed axial strain ramps from zero to 0.001 over 0–1 s, remains
there through 31 s, ramps back to zero over 31–32 s and remains zero through
62 s. Zero displacement after unloading is imposed, not free recovery.
Negative post-unload stress is viscoelastic memory at a fixed strain and
must not be interpreted as permanent annealing strain.

For each ramp [a,b] with constant strain rate v, q = min(t,b), the exact
stress contribution (when q > a) is

σ(t) = E∞v(q − a) + ∑ Eᵢvτᵢ[exp(−(t − q)/τᵢ) − exp(−(t − a)/τᵢ)].

Contributions from loading and unloading are added. Reaction is −Aσ;
lateral strain is −νε. The reference integrates each finite ramp exactly,
so it does not compare a ramped solver load with an ideal step solution.

## Gap closure

A single frictionless CONTA178 joins the right-face master to a fixed node
at x = 10.002 mm, giving a 0.002 mm geometric gap. KEYOPT(2) = 4 uses normal
Lagrange enforcement; KEYOPT(5) = 1 specifies the +x normal. Weak springs
are disabled. Absolute normal penetration and tensile-force tolerances are
10⁻⁹ mm and 10⁻⁹ N. The contact area defaults to 1 mm²; this node-to-node
verification does not resolve a fixture pressure distribution.

The exact solution is uₓ = min(Le,g), σₓ = E(uₓ/L − e), Rₓ = −Aσₓ,
and open separation = max(g − uₓ,0). Contact force is compressive-negative.
SMISC 1 gives normal force; NMISC 1 gives status; NMISC 3 gives USEP.
Positive opening is −USEP. Raw status 1 is open, and 2 or 3 is closed.
Heating crosses the clearance; cooling must reopen it without tensile
adhesion. This verifies a fixed stop and unilateral gap, not the deformable
AISI 304 surface-contact assembly, friction or thermal-contact conductance.

## Acceptance and reproducibility

Before execution each comparison quantity was assigned an absolute tolerance
of 10⁻⁷ in its declared unit plus 0.1% of the absolute reference value.
A zero analytical value has no defined relative error; its CSV cell is blank,
and the absolute tolerance governs. Contact state is also checked exactly.
All comparisons include three displacements, axial stress and summed reaction;
the contact case adds normal force, state and opening.

Each immutable run includes its executed input, case, runner snapshot, binary
result, raw extraction, return code, logs and SHA-256 hashes. Local scratch is
used for solver execution. Attempts are sequential because a concurrent
Student checkout was rejected. Published CSVs admit accepted comparisons only.

## Official implementation references

- CONTA178 input/output definitions, Ansys 2026 R1:
  https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_elem/Hlp_E_CONTA178.html
- INISTATE initial-state command, Ansys 2026 R1:
  https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_cmd/Hlp_C_INISTATE.html
- Structural Analysis Guide, Ansys 2026 R1, viscoelastic TB,PRONY usage:
  https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/pdf/ANSYS_Mechanical_APDL_Structural_Analysis_Guide.pdf

Accessed 13 September 2026. These are software documentation, not material-property
sources. The executed command files are the primary implementation evidence.

## Warning and failed-attempt audit

Contact attempt 01 failed the USEP opening-sign conversion; attempt 02 failed
a concurrent Student license checkout. Attempt 03 is accepted. Its six warnings
concern constrained transverse DOFs on contact nodes, sparse-solver pivoting,
three near-zero force scaling notices, and an unsupported solid NMISC request.
The normal specimen DOF is free before closure; contact quantities are read
from element 2 only. The analytical displacement, force and opening comparisons
independently check these outputs. No MAPDL error occurs in the accepted run.
Viscoelastic attempt 01 failed the ramp-end accuracy limit at a 0.01 s step.
The refined attempt uses 0.0001 s ramps and 0.1 s holds. Failed runs remain
immutable. This is benchmark refinement, not production convergence.

## Accepted comparison results

### Structural reference checks: selected genuine outputs
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

The six accepted cases pass all 114 comparisons, including transverse displacement, reaction, stress and contact state. The maximum axial displacement error is 2.331 × 10⁻¹⁴ mm; the maximum gap error is 9.500 × 10⁻¹¹ mm. Contact is open at 30 °C, closed at 80 °C and open after cooling. The thermally cycled elastic body returns to its original dimensions, whereas the imposed retained-eigenstrain body contracts after cooling and release. These are numerical patch-test findings and prescribed eigenstrain consequences, not measured PLA responses.

### Isothermal Prony finite-ramp stress verification at 65 °C
Time (s) | ANSYS stress (MPa) | Analytical stress (MPa) | Absolute error (MPa)
1 | 0.0375536568 | 0.0375574835 | 0.0000038266
11 | 0.0243886374 | 0.0243886379 | 0.0000000005
31 | 0.0183896348 | 0.0183896352 | 0.0000000005
32 | -0.0193833038 | -0.0193871309 | 0.0000038271
62 | -0.0045757745 | -0.0045757747 | 0.0000000001

The maximum stress error is 3.8271 × 10⁻⁶ MPa and the maximum stress-relative error is 0.019740%. The maximum reaction error is 3.8280 × 10⁻⁶ N. The refined isothermal adapter passes; the complete non-isothermal clock and bulk irreversible-strain evolution remain unimplemented in ANSYS. The negative stress after unloading is followed under a held-zero-strain boundary, so it does not establish free post-cooling warpage or annealing residual stress.

The accepted viscoelastic run has four warnings: three small reference-force notices and one elapsed-time/CPU performance notice. No solver error is present; both independently extracted stress and reaction pass the unchanged analytical limits.
