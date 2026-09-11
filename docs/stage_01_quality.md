# Stage 1 quality record

Date: 2026-09-12.

## Source review

All 24 base pages were read through page-labeled extraction and visually reviewed in rendered page sheets. The repeated support schematic on pages 8 and 12 was confirmed; the old conceptual Pareto graphic has a clipped left label. Original source evidence remains immutable.

## Manuscript visual review

The complete ten-page PDF was rendered with Poppler at 105 dpi and every page inspected individually. Initial pagination spill pages were corrected before final review. Missing gradient/membership/perpendicular symbols and schematic subscript glyphs in the initial font configuration were repaired with explicit font support. The builder now checks paragraph glyph coverage.

| Pages | Review outcome |
|---|---|
| 1 | Title, authors, abstract, keywords and opening scope readable; no clipped text |
| 2 | Objectives 1–5 and propositions P1–P3 fit; no orphan continuation page |
| 3 | One conceptual figure; clearance labels and caption readable; no duplicate figure |
| 4 | Thermal-choice table and heat equation readable; gradient glyph repaired |
| 5 | Strain/contact equations, sub/superscripts and release text checked |
| 6 | Signed response, RMS, tolerance and warpage equations checked; membership/perpendicular glyphs repaired |
| 7 | Verification and validation text complete and clearly prospective |
| 8 | Desirability equation, indices, inequality signs and decision text checked |
| 9 | Evidence-status table and conclusions fit on one page |
| 10 | Four cited references and provenance supplement readable; DOI links present |

No clipping, missing glyph boxes, overlapping table text or blank/spill pages remained in the reviewed build. The final reviewed PDF SHA-256 is recorded in `integrity_report.json`.

## Integrity and scientific review

`python scripts/check_integrity.py`: 40 checks passed. Checks cover source hash, audit inventories, complete reference catalog, retained references/citations, objective/equation sequence, empty numerical registries, deterministic PDF regeneration, page bounds and scientific typography. `git diff --check` is also run before each commit.

These checks are document and provenance checks. They do not constitute ANSYS mesh/time-step verification, physical validation or a completed numerical investigation. No solver has been run. The manuscript explicitly records these limits, and property/validation/run registries contain headers only.

Stage 1 is the conversion and audit only. No later numbered stage was started.
