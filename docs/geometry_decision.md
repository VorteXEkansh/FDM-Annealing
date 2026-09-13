# Parametric specimen and fixture geometry decision

## Selected specimen

The computational specimen is a solid rectangular plate measuring **60 mm ×
10 mm × 4 mm** in x, y and z. This reproduces the regular-plate dimensions in
Trofimov et al. (2022), Figure 4(a), DOI 10.1016/j.addma.2022.102693. That paper
used the regular plate for thermal observation and a separate bridge for
distortion validation. The present study transfers only the geometry; it does
not transfer Raise3D Premium PLA properties, printing residual stress, thermal
data or validation results to Prusament PLA.

The rectangular plate gives signed dimensions in three orthogonal directions,
a 60 mm span over which released bow can be measured, two flat 600 mm² faces for
opposed contact, and a simple three-volume assembly. Its derived geometric
ratios are L/h = 15, W/h = 2.5 and L/W = 6. These are calculations from the
declared dimensions, not response findings. A tensile coupon was rejected
because shoulders and a narrow gauge complicate contact and make global
dimensional change ambiguous. The source bridge was rejected for the primary
domain because its supports introduce additional contact and local geometry;
it remains a possible separate validation geometry.

## Fixture

The GAP fixture comprises two 70 mm × 20 mm × 5 mm rectangular AISI 304 plates.
The coupon is centered, leaving a 5 mm planform margin on every side. Plate
edges therefore do not coincide with specimen edges. The plate dimensions are
declared computational design choices. Plate deformation will not be suppressed
by treating the metal as infinitely rigid once a production model is admitted.

At the reference state, plate separation is H₀ = h₀ + g₀. The total initial
clearance g₀ is divided equally above and below the coupon and no preload is
applied. Physical spacer/standoff solids are not yet included: their geometry,
attachment and thermal expansion cannot be fixed until the fixture thermal-
strain convention is resolved. The separation is therefore an explicit
kinematic geometry parameter, not a manufactured tolerance.

## Clearance screen

The declared dimensionless screening levels are γ = 0, 0.0025, 0.005, 0.01 and
0.02. For h₀ = 4 mm these correspond by g₀ = γh₀ to total clearances of 0 mm,
0.01 mm, 0.02 mm, 0.04 mm and 0.08 mm. Each nonzero gap is split equally. These
levels bracket initial contact through a 2% thickness clearance with finer
resolution near contact. They are design levels for later numerical screening,
not measured fixture tolerances, literature-derived optima or admitted
production bounds. Their adequacy must be revisited after an irreversible-strain
law, mesh/contact resolution and dimensional uncertainty are established.

The absolute candidate levels in Prompt 7 were evaluated against the 4 mm
thickness rather than accepted as an arbitrary millimetre series:

| Candidate total gap | γ for h₀ = 4 mm | Stage 7 disposition | Reason |
|---:|---:|---|---|
| 0.000 mm | 0 | Retained | Coincident initial contact is the lower endpoint. |
| 0.025 mm | 0.00625 | Represented within the screen | It is mechanically interpretable and lies between γ = 0.005 and 0.01; a separate level would duplicate the near-contact region. |
| 0.050 mm | 0.0125 | Represented within the screen | It is mechanically interpretable and lies between γ = 0.01 and 0.02. |
| 0.100 mm | 0.025 | Deferred | It exceeds the primary 2% thickness screen; no supported deformation scale yet warrants trading near-contact resolution for it. |
| 0.200 mm | 0.05 | Deferred | It is 5% of thickness and lacks a supported deformation scale for primary screening. |

“Deferred” does not mean mechanically impossible or permanently excluded. The
larger levels may be admitted after a supported free-deformation scale is
available. The dispositions and calculations are recorded in
`geometry/candidate_clearance_audit.csv`.

The Stage 7 ANSYS geometry build uses γ = 0.01 (g₀ = 0.04 mm) solely as a
representative nonzero parameterization check. It is not a preferred condition.
The geometry-only MAPDL deck creates lower plate, specimen and upper plate
volumes, names their volume components and saves a database. It contains no
elements, material assignment, boundary condition, thermal history or solve.

## Coordinate and reporting rules

x is the 60 mm specimen length and selected primary print-path direction; y is
the 10 mm width; z is the 4 mm build/thickness direction. The initial geometry
is centered without geometric symmetry constraints. Warpage will be evaluated
on the released 60 mm × 10 mm face after rigid-motion removal. Nominal contact
area is a geometric 600 mm² per face; actual contacting area and pressure are
solver responses and remain unknown.
