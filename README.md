# FDM-Annealing

Computational research on quantified gap-controlled constraint during sub-melting annealing of FFF-printed PLA.

**Read [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md) first.** This is a staged research repository, not a completed ANSYS study. Stage 7 defines a 60 mm × 10 mm × 4 mm plate specimen, opposed AISI 304 fixture plates and a normalized clearance screen, and verifies their three-volume construction in a geometry-only MAPDL run. Missing bulk irreversible strain, thermal functions, discretization, contact inputs and the fixture expansion convention still block production ANSYS annealing predictions.

## Structure

- `docs/`: authoritative state, conversion audit, restructuring map and quality records.
- `data/source/`: immutable user-supplied base paper and extraction.
- `data/literature/`: historical verification and empty property/validation registries.
- `literature/`: current XLSX matrix, BibTeX, curated JSON, DOI metadata and search evidence.
- `data/processed/`: traceable derived numerical data, when available.
- `models/ansys/`: genuine ANSYS model inputs and run documentation, when available.
- `results/`: solver provenance registry; no placeholder results.
- `manuscript/`: complete editable manuscript source.
- `material/`: formulation-specific source tables, uncertainty gaps and calculated reference conversion.
- `geometry/`: authoritative specimen/fixture definition and candidate-clearance audit.
- `simulation/geometry/`: hashed geometry-only MAPDL input, raw output and saved database.
- `src/`: tested constitutive reference relations; no ANSYS solver wrapper yet.
- `scripts/`: reproducible PDF build and integrity checks.
- `tests/`: checks appropriate to the research stage.
- `output/pdf/`: current complete manuscript PDF.

## Reproduce

Python 3.11 or later, with dependencies in `requirements.txt`, and Poppler for visual rendering:

```text
python scripts/build_manuscript.py
python scripts/build_material_database.py
python scripts/build_constitutive_reference.py
python scripts/check_materials.py 5
python scripts/check_constitutive.py
python scripts/check_geometry.py
python scripts/check_integrity.py
python scripts/check_literature.py 7
pdftoppm -r 150 -png output/pdf/Constrained-Annealing-2026-DRAFT.pdf tmp/pdfs/current
```

The builder uses Windows Times New Roman, Arial and Segoe UI Symbol by default. On other systems set `RESEARCH_FONT_DIR` to a directory containing `times.ttf`, `timesbd.ttf`, `timesi.ttf`, `arial.ttf`, `arialbd.ttf` and `seguisym.ttf`. Fonts are not redistributed. Rendered pages must be visually reviewed after changes. Artifact regeneration alone is not scientific verification.

Source paper authorship is retained; the original course cover and institutional logo are omitted. No journal submission or institutional approval is claimed. No license to third-party publications is implied.

## Literature reproducibility

The XLSX is generated from `literature/literature_matrix.json` by `scripts/build_literature.mjs`, using the Codex bundled `@oai/artifact-tool` dependency runtime. A `scripts/node_modules` junction to that runtime is local and ignored. Run `node scripts/build_literature.mjs` in that environment. `scripts/curate_literature.py` regenerates the curated matrix JSON and BibTeX from verified metadata and explicit appraisal notes. It does not extract or invent missing properties. `scripts/verify_literature.py` reuses archived Crossref responses and verifies their identity; a new search/date must be recorded as a later stage, not silently overwrite raw evidence.

The maintained complete manuscript is `manuscript/current.md`; `manuscript/literature_review.md` is the literature-section working source with citation keys, not a second deliverable. Source and output hashes, known access limitations and quality checks accompany the stage records.
