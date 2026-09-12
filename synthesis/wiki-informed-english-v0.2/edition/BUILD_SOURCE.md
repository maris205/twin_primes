# Build the standalone English v0.2 sources

This ZIP contains the complete LaTeX source, bibliography, macros, notation guide, twelve section files, and the unchanged user-supplied English map. It does not include the historical research archive or wiki. The manuscript is a research synthesis, not a proof of the twin-prime conjecture.

From the extracted `paper` directory:

```sh
latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

Use a TeX distribution with `latexmk`, pdfLaTeX, BibTeX, Latin Modern, AMS packages, `mathtools`, `bm`, `geometry`, `graphicx`, `booktabs`, `longtable`, `array`, `tabularx`, `float`, `natbib`, `xcolor`, `hyperref`, and `microtype`. No private style files, network download, or shell escape is needed by the manuscript.

`SOURCE_MANIFEST.json` records the packaged file hashes. The complete workspace edition additionally supplies the original and two revision PDFs, source concordance, baseline-preservation check, full raw editorial reviews, and PDF QA. Those archive-preservation checks require the original sibling repository and are not part of this portable source-only bundle.

PDF metadata can vary between builds; the TeX sources define the content. Authorship and venue are intentionally unspecified.
