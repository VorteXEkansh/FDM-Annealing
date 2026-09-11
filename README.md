# FDM-Annealing

Computational research on quantified gap-controlled constraint during sub-melting annealing of FFF-printed PLA.

**Read [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md) first.** This is a staged research repository, not a completed ANSYS study. Stage 1 converts and audits the supplied experimental proposal. No solver results exist.

## Structure

- `docs/`: authoritative state, conversion audit, restructuring map and quality records.
- `data/source/`: immutable user-supplied base paper and extraction.
- `data/literature/`: reference verification and evidence records.
- `data/processed/`: traceable derived numerical data, when available.
- `models/ansys/`: genuine ANSYS model inputs and run documentation, when available.
- `results/`: solver provenance registry; no placeholder results.
- `manuscript/`: complete editable manuscript source.
- `scripts/`: reproducible PDF build and integrity checks.
- `tests/`: checks appropriate to the research stage.
- `output/pdf/`: current complete manuscript PDF.

## Reproduce

Python 3.11 or later, with dependencies in `requirements.txt`, and Poppler for visual rendering:

```text
python scripts/build_manuscript.py
python scripts/check_integrity.py
pdftoppm -r 110 -png output/pdf/Constrained-Annealing-2026-DRAFT.pdf tmp/pdfs/current
```

The builder uses Windows Times New Roman, Arial and Segoe UI Symbol by default. On other systems set `RESEARCH_FONT_DIR` to a directory containing `times.ttf`, `timesbd.ttf`, `timesi.ttf`, `arial.ttf`, `arialbd.ttf` and `seguisym.ttf`. Fonts are not redistributed. Rendered pages must be visually reviewed after changes. Artifact regeneration alone is not scientific verification.

Source paper authorship is retained; the original course cover and institutional logo are omitted. No journal submission or institutional approval is claimed. No license to third-party publications is implied.
