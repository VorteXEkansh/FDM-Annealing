# Prompt 2 — literature search and appraisal strategy

Search executed 12 September 2026; cutoff inclusive. The original audit and `docs/PROJECT_STATE.md` were read before work. This is a new targeted critical investigation with backward/forward and exact-title follow-up, not a PRISMA systematic review or a guaranteed exhaustive search. No Scopus/Web of Science subscription search is claimed.

## Search routes

Web scholarly discovery led to primary publisher pages (Elsevier, Springer Nature, Wiley, MDPI, IOP, Taylor & Francis, Emerald and Materials Science), institutional author repositories (Latvia, Michigan Tech, Polytechnique Montréal, ETH Zurich and UTS), Europe PMC full-text XML and Crossref registration metadata. ResearchGate/aggregators were discovery routes only; they were not treated as superior to publisher or author evidence. Publisher AI summaries were not used. Eight full texts were retrieved for targeted appraisal; remaining records are explicitly marked as primary-abstract/excerpt appraisal, not complete protocol extraction.

## Query design

Families combined PLA / polylactic acid with FFF / FDM / fused filament fabrication / material extrusion, then annealing / thermal treatment / recovery; warpage / residual stress / shrinkage / anisotropy; viscoelastic / Prony / WLF / relaxation; cold crystallization / kinetics; mould / mold / powder / sand / fixture / restraint / gap / clearance / contact; finite element / thermo-mechanical / validation; and multi-objective / optimization. Both spelling variants and mechanisms were searched because direct 4D printing and printing-process models are close constitutive competitors.

Examples of actual follow-up queries (derived discovery-source records are in `literature/search_logs/`):

- `"Multiscale modeling and multiobjective optimization" PLA`
- `"Williams" "Landel" "Ferry" 1955 10.1021`
- `"10.1016/j.jmapro.2023.03.030" contact`
- `PLA annealing fixture clearance contact finite element gap constraint simulation`
- `"10.1002/pen.70250" sand`
- `"10.1080/20550340.2023.2171940" crystallization`
- `"10.1108/RPJ-04-2021-0090" annealing temperature time`
- `"10.1007/s40964-018-0052-4" "annealing"`

The saved search batches preserve source URLs and hashes of raw responses; complete raw responses remain in the local ignored archive to avoid redistributing article excerpts. They are not a complete engine ranking history. No invented screening/duplicate counts or PRISMA flow numbers are reported.

## Eligibility and DOI verification

Retained 34 journal records, including methodological foundations. Included directly relevant FFF PLA and supported annealing work; included adjacent bulk PLA, composites, 4D printing and numerical methodology when necessary to challenge novelty, with transfer limitations. Excluded unverified-title/DOI leads from the retained bibliography, unreviewed promotional summaries and unrelated polymer protocols from parameter evidence. The existing verified ASTM standard is retained separately; it is not counted as a peer-reviewed research paper.

`scripts/verify_literature.py` queries Crossref for each journal DOI, checks an exact case-insensitive DOI match and saves returned title, authors, journal, publication dates and document type. Raw responses remain in `literature/metadata/`; hashes and retrieval date are recorded in `literature/doi_verification.json`. The title/topic identity was compared with the discovered primary record. DOI registration is an identity check, not validation of a paper's findings. Every DOI in the manuscript/BibTeX is either in these exact-match records or the previously verified official ASTM record.

Publication eligibility uses first availability no later than cutoff; the bibliography uses the assigned issue year when available. Online and issue dates are both retained. Grades2026 was available online in July despite an October issue assignment. The June 2026 Ben Amor–Souissi paper is an early unedited publisher article and is labeled accordingly. No retraction-free or exhaustive Crossmark audit is claimed.

## Extraction and quality appraisal

Each row preserves all requested fields plus access level, locator, source URL and adoption status. A missing field means **not extracted from accessible evidence**, never zero, not applicable or proven absent. Where protocols were accessible, numerical design conditions have section/table locators. Response cells mainly describe the type of data available, avoiding premature digitization or property adoption. No measurements are imported into property or validation registries.

Separate: printed versus injection-moulded material; neat versus tough/high-heat/recycled/fibre-filled PLA; printing-road gap versus annealing-fixture clearance; supported dimensions versus independently measured stress; calibration versus validation; and computational scenarios versus experimental replication. Source claims of validation are appraised for task relevance, not inherited as validation of this project.

Full-text acquisition hashes and URLs are in `literature/acquisition_manifest.json`. Review copies are local under ignored `tmp/literature/`; they are not redistributed as project source publications. Failed publisher access (403/429/robots/captcha) prompted repository/Europe PMC routes; an inaccessible protocol stays marked inaccessible. Original source files and metadata responses are not edited to fix source errors. Curated notes are separate.

The powder-mould Table 7 conflict is recorded in the novelty audit. Generic WLF constants, bulk PLA properties, manufacturer values quoted inside papers and unverified support descriptions are not promoted into ANSYS inputs. Raw parameter and independent validation extraction remain for an explicitly authorized later stage.

## Coverage map and outstanding limits

| Required topic family | Principal retained evidence |
|---|---|
| FFF PLA and annealing | Butt2020, Stojkovic2023, Wach2018, Benwood2018 |
| Warpage, residual stress, thermo-mechanical FE | Wijnen2018, Trofimov2022, Bute2024, Process2025, SCF2023 |
| Shrinkage, anisotropy and orthotropy | Bute2024, Mould2022, Orthotropic2024 |
| Temperature-dependent, viscoelastic and relaxation behavior | Prediction2023, Laminate2025, Relaxation2022, Viscoplastic2017 |
| Prony series and WLF | Prediction2023, Laminate2025, WLF1955 |
| Cold crystallization and kinetics | Pantani2010, Nucleation2011, Kinetics2025, Deformation2025, Phase2025 |
| Irreversible annealing strain | Bute2024, Wijnen2018, Laminate2025 |
| Constrained/mould-supported annealing and fixture restraint | Mould2022, Moulds2022, Wijnbergen2021, Encapsulation2025, Salt2022 |
| Thermal boundaries/contact and numerical polymer modeling | Trofimov2022, Process2025, Heat2023; fixture-specific conductance remains unestablished |
| FEA physical comparison and limits | Trofimov2022, Wijnen2018, Laminate2025, Prediction2023 |
| Multi-objective optimization | Multiscale2026, PINN2026, Kahya2025, Derringer1980 |

The search supports a provisional gap, not exclusivity. Obtain the remaining closest-study full protocols and refresh the search before publication. Do not advance to Prompt 3 automatically.
