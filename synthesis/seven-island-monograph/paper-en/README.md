# English edition

**A Seven-Island Framework for Twin-Prime Research: Exact Structures, Analytic Obstructions, and Two Bridging Problems**

This is the complete English version of the [Chinese synthesis](../paper/main.pdf), with nine main sections, two appendices, and the same twelve bibliography entries. It preserves the proofs, hypotheses, conditional estimates, and limitations; it is not an abbreviated English abstract or a new numbered TPC paper.

- [Read the PDF](main.pdf) — authoritative mathematical layout and numbering.
- [Read the Markdown copy](main.md) — convenient searchable text; Pandoc citation keys refer to [references.bib](references.bib), and PDF numbering takes precedence.
- [Full-resolution English map](figures/tpc_route_en.png) — the exact user-supplied image, reproduced without edits.
- [LaTeX master](main.tex) and [section sources](sections/).
- [Core source matrix](../CORE_SOURCE_MATRIX.md) and [420-directory catalog](../SOURCE_CATALOG.md) — shared with the Chinese edition, not independently retranslated or reclassified.

The map is navigation, not a proof certificate. Map Bridge A contains both analytic Gate A and Gate B; map Bridge B concerns the distinguished arithmetic seed. The manuscript does not prove the twin-prime conjecture.

## Rebuild and checks

From the parent synthesis directory:

```sh
python -B tools/build_english.py
python -B tools/check_english.py
python -B tools/render_english.py
```

Requirements: `latexmk`, `pdflatex`, `bibtex`, the LaTeX packages named in `main.tex`, `pandoc`, and Poppler's `pdfinfo`, `pdftotext`, `pdffonts`, and `pdftoppm`. Builds and page images use new external scratch directories. These scripts do not rebuild or modify the Chinese edition or historical manuscripts. The rendering manifest records scratch image locations, which may not survive transfer to another machine; rerun the renderer to regenerate them.

The checks verify all 30 preserved Chinese files against [their hash lock](chinese_baseline_lock.json), exact map and bibliography identity, matching labels/citations/formal-statement/proof counts in each of twelve section files, source-catalog hashes, resolved references, embedded fonts, and layout diagnostics. Count parity is not semantic verification. See [translation checks](translation_checks.json), [compiler log](main.log), [fonts](fonts.txt), and [render manifest](render_manifest.json). Independent review scope and final presentation status are recorded in [the QA report](QA_REPORT.md).

Authorship and target venue remain unspecified. This is a source-traceable synthesis draft, not a novelty certification or a submission-ready claim.
