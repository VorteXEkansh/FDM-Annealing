# Reproduce the verification-only release

Release scope: one accepted thermal reference case, six structural/contact reference cases and 28 unique accepted convergence runs. These verify component numerics, not physical PLA annealing predictions. No production sweep, independent physical validation, surrogate, global sensitivity, uncertainty propagation, Pareto solution or new optimization confirmation is reported.

## Environment

The release export used Windows, Python 3.12.14, ReportLab 4.4.9, pypdf 6.10.0, Pillow 12.3.0, python-docx 1.2.0, lxml 6.1.1 and latex2mathml 3.78.1. Install the pinned requirements in a dedicated environment, or use environment.yml. Plotting uses matplotlib 3.10.8. The original solver/analysis execution environment and hardware are recorded separately in docs/software_environment.md; a later export interpreter does not change archived solver evidence.

The PDF builder requires Times New Roman, Arial and Segoe UI Symbol files. Set RESEARCH_FONT_DIR to the folder containing those licensed fonts. The Word builder transforms MathML to native OMML using Office's MML2OMML.XSL; set MML2OMML_XSL to a legally installed copy. Set PDFTOPPM to the Poppler executable. No commercial fonts, Office stylesheet or ANSYS installer is redistributed. PDF/DOCX appearance can vary with the renderer and fonts. Microsoft Word is used for local Word visual QA because LibreOffice is absent on this host.

## Read and check without ANSYS

Run from the repository root:

```powershell
python -m unittest discover -s tests -v
python scripts/check_literature.py 20
python scripts/check_materials.py 20
python scripts/check_release.py
```

The release checker verifies hashes and recomputes the reference response metrics from archived CSVs without an ANSYS license. It checks frozen raw evidence that is distributed in the release. Third-party PDF files excluded from the current tree are listed with original hashes in external_evidence.csv; obtain them legally if repeating full historical source-material audits. Traceability regeneration uses the registered external hash when an excluded PDF is unavailable; this does not verify its bytes afresh. Historical integrity scripts require the original local evidence layout and stage-specific manuscript hashes. They are not the current release entry point.

## Reconstruct and run numerical reference cases

Full solver reproduction requires compatible **Ansys Student 2026 R1 / MAPDL 26.1, update 20260202**, a valid license, and Student limits. The executable on the reference host is under `C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe`. Product/license behavior must be checked on the reproducing host. See docs/software_environment.md and the archived command in each manifest.json.

Each archived run contains case.json, input.dat, solver log, extracted CSVs and a hash manifest. Input decks fully reconstruct the reference geometry, material, mesh, boundary conditions and result extraction. Copy input.dat into a **new empty working directory**, then run:

```powershell
& $mapdlExe -b -i input.dat -o mapdl.out -j reproduce -np 1
```

Set `$mapdlExe` to the compatible installed solver. Use an absolute executable path, the new directory as the working directory, and preserve output. Never run in an archived evidence folder. Binary result hashes can differ between installations; compare declared extracted observables and tolerance criteria, not merely binary identity. Existing runners offer fresh attempts, for example:

```powershell
python scripts/run_structural_verification.py --kind free --attempt reproduction01
```

The runner rejects an existing attempt directory. Review the runner's installed executable path first. Other supported kinds are fixed, eigen_free, eigen_fixed, visco and contact. Accepted case paths are indexed in result_traceability.csv. Thermal and convergence reproduction use the corresponding archived decks and case.json. The geometry-only model is under simulation/geometry/stage07_plate_gap. Production templates remain blocked and must not be used as verified annealing models.

## Regenerate figures and the complete manuscript

```powershell
python scripts/build_review_figures.py
python scripts/prepare_release.py
python scripts/build_release.py
python scripts/check_release.py
```

The figure script regenerates the three genuine convergence plots without smoothing; build_release.py makes the geometry schematic, main PDF, supplementary PDF, native-equation DOCX and the full evolving DRAFT PDF. The canonical manuscript source is manuscript/current.md. Supplemental detailed tables are generated from evidence CSVs, not hand-entered results. The Word file contains native headings, text, tables, OMML equations, figures, captions, bibliography and cross-reference fields.

Rebuilding changes no raw solver result. After editing, render all PDFs and the Word file, inspect every page, update docs/stage_20_visual_review.json, and only then run the release checker with `--write-checksums`. A changed artifact invalidates the old visual review. Final SHA-256 records are in sha256_manifest.csv; their own hash is deliberately excluded to avoid self-reference.

## Archive boundaries

Publisher and supplier PDFs removed from the current release tree remain unchanged in local evidence storage. Prior Git history has not been rewritten, so older commits can still contain those PDFs. The 11.9 MB superseded solver scratch file listed in external_scratch.csv is similarly kept locally but omitted from the release tree; its original hash is preserved. Raw result binaries and logs needed for audit are retained, including rejected runs. No v1.0.0 completion tag is applied because the production study is incomplete.

An old search log containing an expired third-party signed download URL is also omitted from the current tree; external_search_log.csv preserves its hash. This was a publisher access-key identifier and signature in a public retrieval URL, not a discovered user secret key. The release tree passes the stated common-credential/private-key pattern scan. Older Git history was not purged or certified secret-free.

An independent user can verify the released numerical evidence. Reproducing a validated production study is not possible from this package because that study has not been completed.
