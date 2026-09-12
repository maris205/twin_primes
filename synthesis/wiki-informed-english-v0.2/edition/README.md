# Seven-island synthesis: English revision v0.2

This is a separate, wiki-informed editorial revision of the existing English synthesis. The original English v0.1 and Chinese edition remain unchanged.

- [Revised English PDF](paper/main.pdf)
- [Searchable Markdown edition](paper/main.md) — PDF numbering and layout are authoritative.
- [LaTeX master](paper/main.tex) and [section sources](paper/sections/)
- [Portable LaTeX source ZIP](english_v0.2_source.zip) — [standalone build instructions](BUILD_SOURCE.md).
- [Complete editorial TeX diff](REVISION_DIFF.patch).
- [Original English PDF](paper/main_round0_original.pdf)
- [Wiki-to-paper reading concordance](WIKI_REVISION_CROSSWALK.md)
- [Revision plan and claim freeze](REVISION_PLAN.md)
- [Revision and review log](PAPER_IMPROVEMENT_LOG.md)
- [Quality-assurance report](QA_REPORT.md)

The article reorganizes existing results. It does not prove the twin-prime conjecture, add a new numbered TPC paper, reopen stopped research, or claim novelty/submission readiness. Authorship and target venue are unspecified.

## Build and check

From this directory:

```sh
python -B tools/edition.py build --round 2
python -B tools/edition.py check
python -O -B tools/edition.py check
python -B tools/edition.py render
```

Requirements: Python 3, latexmk/pdflatex/BibTeX with the packages in the master, Pandoc, and Poppler (`pdfinfo`, `pdftotext`, `pdffonts`, `pdftoppm`). Compilation runs without shell escape in a new scratch directory. The renderer records all final page images and hashes in `render_manifest.json`; regenerate if temporary images are no longer present.

The [JSON source matrix](CORE_SOURCE_MATRIX.json) is copied unchanged. The [readable matrix](CORE_SOURCE_MATRIX.md) preserves its claims and hashes but rebases navigation links to the sibling `twin_primes` repository. The original [420-directory catalog](../twin_primes/synthesis/seven-island-monograph/SOURCE_CATALOG.md) remains available there. The validation script checks source hashes and the protected original editions/wiki cards against `baseline_lock.json`. It also requires unchanged formal statements/proof blocks and original displayed mathematics, retained labels/citations, unchanged bibliography/macros/map, resolved references, and embedded fonts. These are preservation and presentation checks, not mathematical certification of the archive.
