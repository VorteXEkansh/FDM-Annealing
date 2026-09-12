# Prompt 2 — novelty audit

Review cutoff: 12 September 2026. Scope: computational sub-melting annealing of FFF PLA with quantified fixture clearance. Read alongside `literature/literature_matrix.xlsx`, its JSON source and the DOI verification records. This is a critical search, not proof of priority.

## What is already known

- Annealing affects dimensions and mechanical behavior; effects depend on formulation and processing history (Butt2020, Stojkovic2023, Wach2018, Benwood2018).
- Supported annealing, powder moulds, sand and encapsulation have already been studied (Mould2022, Wijnbergen2021, Moulds2022, Salt2022, Encapsulation2025).
- Directional irreversible thermal strain and printing residual stress have already been connected through ANSYS work (Bute2024).
- Thermal/deformation modeling and comparison with measured temperature/warpage are established (Wijnen2018, Trofimov2022, Process2025).
- Prony/WLF modeling, thermally activated recovery and pre-strained laminate finite elements already exist for printed PLA (Prediction2023, Laminate2025).
- Thermal–mechanical–crystallization coupling exists in SCF/PLA printing (SCF2023). Composite and neat-PLA parameters are not interchangeable.
- Annealing optimization, multiscale FE plus annealing plus desirability, and physics-informed recycled-PLA optimization have precedents through 2026 (Kahya2025, Multiscale2026, PINN2026).

## What is not novel

Using ANSYS; choosing three temperatures or durations; annealing PLA; constraining a part; reporting signed shrinkage and warpage; using orthotropy, Prony series or WLF; adding crystallization kinetics; modeling release; comparing FE with measurements; uncertainty analysis or Pareto/desirability methods by themselves. A conjunction of generic method names is not a demonstrated contribution. Do not claim that constrained annealing has never been studied.

## Ten closest competing studies

This is an editorial proximity selection using overlap in physical mechanism, response and numerical method; there are no invented similarity scores. Keys resolve to exact verified DOI, authors and title in the matrix/BibTeX.

| Study | Why close | What it already establishes | Remaining distinction / evidence limit |
|---|---|---|---|
| Bute2024 — [paper](https://doi.org/10.5755/j02.ms.35076) | Irreversible directional response and ANSYS | Thermal strain and printing-stress relation | Does not demonstrate the proposed annealing-clearance/contact prediction |
| Laminate2025 — [paper](https://doi.org/10.1088/1361-665X/adeee4) | History-dependent thermal recovery FE | Pre-strain, Maxwell/Prony, shifting and shape benchmarks | Shape activation rather than preservation under an annealing plate gap |
| Prediction2023 — [paper](https://doi.org/10.3390/polym15051162) | PLA thermomechanical characterization in ANSYS | Prony/temperature shift and mechanical response | No clearance-controlled released-warpage validation identified |
| Wijnen2018 — [paper](https://doi.org/10.1007/s40964-018-0052-4) | Warpage prediction and annealing | Thermal calibration, curvature and directional dimensional change | Full protocol not acquired; no plate-gap study established by abstract |
| Trofimov2022 — [paper](https://doi.org/10.1016/j.addma.2022.102693) | Transient thermal–mechanical FE and comparison | Printing temperature and distortion prediction | Printing history differs from annealing contact |
| Mould2022 — [paper](https://doi.org/10.3390/polym14132607) | Dimensional control under restraint | Alumina support, thermal factors, directional measurements | Powder behavior is not a controlled face clearance; Table 7 discrepancy |
| Wijnbergen2021 — [paper](https://doi.org/10.1108/RPJ-04-2021-0090) | Annealing medium and directional response | Tough-PLA support/media comparisons | Full protocol missing; no transient plate-contact claim established |
| Encapsulation2025 — [paper](https://doi.org/10.3390/jfb16090334) | Supported thermal treatment across geometries | Salt/RTV encapsulation and dimensional precision | Different formulation and support mechanics |
| HighHeat2026 — [paper](https://doi.org/10.1002/pen.70250) | Joint geometric and mechanical prediction | High-heat PLA conditioning and machine learning | Abstract-level appraisal; fixture protocol not established |
| Multiscale2026 — [paper](https://doi.org/10.1007/s43939-026-00769-2) | Annealing + FE + optimization | Homogenized tensile modeling and desirability | Early unedited publisher abstract; full transient contact scope not established |

Other strong adjacent precedents: Farh and Gribniak (Process2025) for detachment; Jiang et al. (SCF2023) for crystallization coupling; Li et al. (Orthotropic2024) for directional constitutive response. They are explicitly discussed rather than suppressed to make the closest-ten comparison favorable.

## Decision on the proposed gap

**Retain only a narrowed, provisional claim.** In the accessible evidence searched through the cutoff, no demonstrated framework was identified that combines quantified initial annealing-fixture clearance, evolving thermal and mechanical contact, irreversible directional response and verified released dimensions/warpage/stress with explicit uncertainty. This is a bounded search finding, not an assertion that no such work exists. Abstract-only access to several close competitors prevents an exclusive first-of-kind claim.

Defensible intended novelty: an evidence-tested, reproducible assessment of the clearance–distortion–stress trade-off for a specified FFF-PLA body and fixture after heating, holding, cooling and release. The integrated physical ingredients are enabling methods already represented in prior literature. Novelty will depend on the demonstrated predictive capability and conditional design insight, not their names.

## Falsification and admission gates

1. A prior paper with an explicit annealing gap sweep, evolving contact, irreversible response and released-state validation would invalidate the proposed integration gap. Revise scope if encountered; do not conceal it.
2. Recover full protocols for abstract-level closest studies before a publication-priority claim. Verify current corrections/version status at submission.
3. Select grade/architecture-compatible properties and independently reserve observations before fitting. No data have been reserved or accepted in this stage.
4. Separate reversible expansion, stress relaxation, print-memory recovery and crystallization strain without double-counting. Compare simpler and richer laws only when evidence supports identification.
5. Establish numerical mesh, time and contact adequacy using actual solver outputs. Then test thermal and dimensional predictions against independent observations.
6. No identified paper currently validates this proposed fixture's residual stress or pressure. If independent evidence remains unavailable, state these as conditional model predictions, not physically validated fields. Dimensional agreement alone does not identify stress.
7. Report uncertainty and the benefit criterion needed to make annealing useful; a low-distortion untreated/mild condition is not automatically a useful optimum.

## Extraction cautions

- Mould2022 Tables 2–3 list the final PLA level as 155 °C; Table 7 labels it 240 °C. Preserve the discrepancy. No affected numeric validation target is admitted.
- Laminate2025 characterizes PLA over 23–85 °C (§2.2.1). Do not extrapolate a fitted law to 95 °C or 110 °C without evidence.
- HighHeat2026 is online in 2025 and in a 2026 issue. Grades2026 is online July 2026 with an October issue assignment; it is eligible by first availability. Neither indexing age nor crawl date defines eligibility.
- PINN2026 uses “thermo-constrained” for learning restrictions. It is not evidence of a mechanical fixture. Repeated records along a load curve cannot be treated as independent physical samples.

No numerical result, material law, optimum or validated fixture design is created by this audit.
