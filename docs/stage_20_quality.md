# Stage 20 release audit and integrity statements

Date: 1 October 2026. Scope explicitly authorized by the user: **clearly labelled verification-only package**. This is a reproducibility release, not completion of the proposed production annealing article. No v1.0.0 tag is assigned.

## Scientific integrity

| Requested statement | Truthful release finding |
|---|---|
| No numerical result fabricated | Confirmed for the release. All reported values retain solver, reproducible calculation or published-source evidence. Design inputs are identified as choices. |
| All major quantitative claims traceable | 384 claim/evidence records link reference comparisons, refinement/contact responses, material values and literature observations to source files and hashes. Geometry is a documented design, not a solver result. |
| No AI-generated scientific image | Confirmed. Three plotted reference datasets and one code-drawn geometry schematic. |
| Mesh convergence verified | Only the declared numerical reference configurations; not a production coupon mesh. |
| Time-step convergence verified | Only the declared thermal/structural numerical reference histories; not a production annealing cycle. |
| Model verification completed | Component/reference checks completed within documented scope. The full coupled production model is incomplete. |
| Independent validation completed | No. Published observations are reserved; no independent validation prediction exists. |
| Sensitivity/uncertainty completed where claimed | No production sensitivity or uncertainty analysis is claimed or provided. Contact-control perturbations remain numerical reference checks. |
| Optimization confirmed with new solver runs | No. No optimum, Pareto front, recommendation or confirmation run exists. |
| Superscripts/subscripts checked | Native Word OMML, native inline super/subscripts and PDF glyph/layout review performed. |
| Mathematical symbols checked | Δ, ε, σ, ρ, α, ν, ∂, ∇, √, ∑, × and degree notation checked where used. No product operator ∏ is required by the implemented equations; none was inserted decoratively. |
| No placeholder remains | Forbidden placeholder/pseudo-math strings absent from final PDFs. Honest missing-science statements and author-confirmation requirements are retained, not disguised as results. |
| No secret pushed | Current release-tree credential/private-key pattern scan is clear. An expired third-party signed retrieval URL was excluded from the current tree. Older history is not certified secret-free or purged. |
| All files visually inspected | Main PDF: 18 pages; supplementary PDF: 21 pages; native-Word rendered output: 17 pages. Full evolving draft: 22 pages, with pages 1–18 pixel-identical to the reviewed main PDF and pages 19–22 separately reviewed. |

## Evidence and checks

The pre-release Stage 19 suite passed 115 checks before document changes. Stage 20 runs 85 unit tests, 137 literature checks, 29 material checks, an independent release gate, and live Crossref identity verification of all 38 DOIs. Every one of the 41 main bibliography entries is cited. The release gate rechecks 1,121 frozen evidence records, 63 mesh/time responses, 36 contact quantities, 114 structural/contact comparisons and nine thermal samples. It does not invoke ANSYS or imply new physical validation.

The final three deliverables rebuild byte-for-byte from source. SHA-256 records cover the artifacts, source/data/code, model decks and release instructions. All raw evidence retained locally remains unchanged. Third-party PDFs and one large superseded scratch file were untracked without deleting local bytes. Earlier Git history remains available and was not rewritten.

## Visual/export corrections

Word title border removed, title/heading styles made explicit, table headers kept with the first data row, and editable number-only bookmarks/cross-reference fields checked after native Word updates. The supplementary inventory uses readable column widths, wrapped values, repeated table headers and scientific SI notation. Table captions cannot be stranded at the bottom of a page. The bundled DOCX renderer was attempted and diagnosed as lacking soffice.exe; installed Microsoft Word performed the read-only render instead. Every rendered page was viewed, with an additional higher-resolution check of a dense supplementary table. None of these editorial corrections changes a solver value.

Authorship roles, corresponding-author details, funding and competing interests still require the named authors' confirmation before submission. No journal submission or scientific completion is asserted.
