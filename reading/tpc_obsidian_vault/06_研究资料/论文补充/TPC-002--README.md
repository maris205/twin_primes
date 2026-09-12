---
type: "source-reading"
source_path: "papers/tpc-2-rough-pair-parity-transitions/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-002"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-2-rough-pair-parity-transitions/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-002|TPC-002]] · [[00_开始阅读|首页]]

# Polynomial-Scale Rough Pairs

This directory contains the source, reproducible experiments, figures, and compiled PDF for the next theory paper in the twin-prime branch of the prime-dynamics program.

## Intended scope

The paper studies two quantitative gaps between finite rough-pair counts and genuine prime-pair counts:

-   the gap between the range where a baseline dimension-two lower sieve is positive and the range where every rough survivor is exactly a prime or semiprime;
-   the additional parity-allocation gap between a positive rough-pair count and a positive prime-prime sector.

The paper does not prove a twin-prime lower bound. Its rigorous results concern beta-sieve envelopes, Buchstab parity bias, slow-cutoff logarithmic parity balance, finite-factor sector inversion, and a complete-period local bilinear spectrum. The experiments are diagnostics, not substitutes for Type-II estimates.

## Files

-   `main.tex` - manuscript source
-   `references.bib` - bibliography
-   `experiments/` - reproducible counting and plotting code
-   `experiments/data/` - retained exact counts for `X=10^8` and four even shifts
-   `figures/` - generated figures used in the manuscript
-   `polynomial-rough-pair-parity-transitions.pdf` - compiled manuscript

## Build

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The production experiment, compiler information, and SHA-256 hashes are recorded in `experiments/MANIFEST.md`. The count and histogram fields are deterministic; the `elapsed_seconds` column is intentionally machine-dependent.
