# Final document and reproducibility review

The internal review inspected all eight pages of the native Word-exported main
PDF and all 32 pages of the Supplementary PDF on 1 November 2026. Poppler renders
were inspected at 150 dpi. The first nine supplementary page images were also
byte-compared with the previously inspected render and were unchanged. This is
assistant-assisted internal quality control, not independent human peer review.

Corrections included a figure-panel title overlap, supplementary refinement-table
column spacing, ambiguous thermal mesh/time case labels, complete publisher
author lists where metadata was incomplete, and scientific exponent notation.
Editable Word fractions, radicals, subscripts and superscripts were checked in
the exported PDF. Tables, figure labels, page boundaries and reference text are
legible; no blank page, clipping, missing mathematical glyph or unresolved
placeholder was found. The eight Word equations, three figures and one main
table are also checked structurally. Visual review is bound to artifact hashes
and must be repeated after any document change.

The packaged LibreOffice renderer could not locate its executable. Native Word
export through pywin32 with explicit export settings and repagination succeeded;
the document was opened read-only. Earlier task-owned stalled export instances
were terminated. No solver evidence was affected. The final PDF identifies
Microsoft as its producer; the Word version and build are recorded separately.

All 98 unit tests pass. The master integrity check independently recomputes
archived mesh/time values, new transient and contact comparisons, checks raw
hashes and validates the citation/equation and empty-production registries.
Source and deliverable checksums include transitive build dependencies. Raw
solver whitespace and line endings are deliberately preserved; authored-source
whitespace checks must exclude those immutable archives. Hashes are checked
against staged Git blobs before committing to prevent newline normalization from
silently invalidating the scientific manifests.

The review does not overcome the physical-model limitations. No validation
accuracy, production warpage, released stress, uncertainty interval or optimum
is inferred from successful numerical checks or polished formatting.
