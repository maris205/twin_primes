---
type: "source-reading"
source_path: "papers/tpc-5-prime-weighted-sieve-kernel-transfer/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-005"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-5-prime-weighted-sieve-kernel-transfer/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-005|TPC-005]] · [[00_开始阅读|首页]]

# TPC-5: Prime-weighted sieve-kernel transfer

This directory contains the fifth paper in the twin-prime-correlation (`tpc`) theory branch.

## Rigorous scope

For the centered CRT pair kernel associated with `Q = product(w < p <= w^2)`, the paper proves:

-   coefficient-uniform complete and subpower-short shift RMS cancellation for arbitrary bounded factor coefficients;
-   a fixed-shift multiplicative-large-sieve bound, yielding cancellation for power-sized boxes whose volume satisfies `M * N / Q -> infinity`;
-   complete and short-shift RMS cancellation for double von Mangoldt factor weights on every pair of fixed positive power scales;
-   fixed-shift double-von-Mangoldt cancellation when the two power exponents have sum greater than one;
-   after removing prime powers, a weighted and unweighted asymptotic for prime pairs `(p, q)` such that `p*q + h` avoids the primes in the window defining `Q`.

The last condition makes `p*q + h` only window-rough. The paper does not prove that `p*q + h` is prime, does not estimate `Lambda(n)Lambda(n+2)`, and does not give a twin-prime lower bound. The ambient-volume threshold `M * N = Q` marks the edge of the range supplied by the present large-sieve method, not a claimed barrier.

## Files

-   `main.tex` and `sections/` – manuscript source
-   `references.bib` – bibliography
-   `experiments/` – exact integer/rational finite diagnostics and tests
-   `prime-weighted-sieve-kernel-transfer.pdf` – compiled manuscript

## Build

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Test

From `experiments/`:

```bash
python exact_weighted_diagnostics.py --output data/exact-certificate.json
python -m unittest -v test_exact_weighted_diagnostics.py
```
