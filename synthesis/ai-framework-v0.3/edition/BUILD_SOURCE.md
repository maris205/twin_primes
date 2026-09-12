# Build the English v0.3 source package

This ZIP is source-only and self-contained for PDF compilation. It does not contain or require the research archive, the wiki, the baseline edition, or this edition's review/validation scripts. Mathematical provenance remains described in the manuscript and the separate companion source matrices.

Required tools: pdfLaTeX, BibTeX, latexmk, and standard TeX packages used by paper/main.tex. The original route-map PNG is included.

From the extracted package, enter the paper directory and run:

    latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex

The output is paper/main.pdf. Source-file SHA-256 values are listed in SOURCE_MANIFEST.json inside the ZIP. Byte-identical PDFs are not promised across build times or TeX installations.

The source package contains author-supplied attribution and is not anonymous. No journal/conference template, page limit, or submission approval has been specified. Successful compilation is a presentation check, not theorem certification.
