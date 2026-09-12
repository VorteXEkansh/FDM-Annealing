# Stage 2 quality record — 12 September 2026

Scope: literature appraisal and manuscript revision, not ANSYS execution or physical validation.

- Read authoritative state and base conversion audit before work.
- Retained 34 exact-match DOI journal records, with primary-source appraisal and access limitations, plus the existing officially verified ASTM standard.
- Created requested XLSX matrix, BibTeX, search strategy and novelty audit. Ten closest competitors are discussed explicitly; broad novelty claims were rejected.
- Maintained full manuscript: 18 pages, 35 bibliography entries, one schematic and three numbered tables. All references are cited. No numerical result plots or placeholder data were added.
- `scripts/check_integrity.py`: 40 checks passed, including immutable base PDF, preserved audit, empty result/property/validation registries, typography, page bounds and byte-for-byte PDF rebuild.
- `scripts/check_literature.py`: 122 checks passed, including DOI/source hashes, cutoff eligibility, complete appraisal schema, bibliography correspondence, XLSX row identities, numeric years, frozen panes and absence of error/formula cells.
- Workbook authored with the bundled artifact-tool runtime. Both worksheets were rendered and reviewed. Main matrix conditions and appraisal regions were additionally inspected. No numerical calculations are implied by the workbook.
- Every PDF page was rendered and visually inspected. Corrected spill pages, duplicated table captions, journal HTML entities and an outdated table cross-reference. Individually rendered 150 dpi pages confirmed full heading glyphs after low-resolution Poppler renders inconsistently omitted leading glyphs. Final manuscript has no spill-only or blank pages.
- Metadata and acquired-source hashes are traceable. Local article review copies remain outside Git; publisher source text is not edited or redistributed as project-owned work.

PDF SHA-256 and all stage source/code/output hashes are in `docs/stage_02_manifest.json`. Remote verification is recorded separately after the content push. No author funding/contribution declaration, journal submission, numerical validation or optimized treatment is claimed.
