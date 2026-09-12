---
type: "source-reading"
source_path: "papers/tpc-12-short-shift-factor-ray-energy/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-012"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-12-short-shift-factor-ray-energy/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-012|TPC-012]] · [[00_开始阅读|首页]]

# TPC-12 - Exceptional-Set Transfer for Short-Shift Factor-Ray Energies

This paper advances the TPC-11 shift-average theorem by proving the previously open intermediate range

```text
X^(2/15 + epsilon) <= H <= X.
```

## Main results

-   A weighted exceptional-set transfer shows that the exceptional centers in the Guth–Maynard almost-all short-interval prime number theorem cannot concentrate on factor products `r = mn` with the diagonal source weight.

-   The centered and raw factor-ray energies have an explicit short-shift asymptotic with main term

    ```text
    (1/2) H X I0(G) I2(W) log(X) ((log X)^2 - (log D)^2).
    ```

-   The first-moment model, hard Mellin band, exact Fejer band, and parity-conditioned even-shift ensemble extend to the same range.

-   A sign-coherent family proves that uniform fixed-shift cancellation is false on locally obstructed rays.

-   The admissible ray `(a,b,h)=(6,1,1)` exactly embeds the weighted prime sum for `6 k^2 + 1`.

-   An exact minimax formula quantifies the radial information lost by the one-Mellin ray compression.

The paper does not prove a fixed-shift prime-pair asymptotic, a twin-prime lower bound, a prime number theorem for a fixed quadratic polynomial, a new level of distribution, or a breach of the sieve parity barrier.

## Build

```powershell
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Reproducibility certificate

```powershell
python experiments/short_shift_certificate.py
python -m unittest experiments.test_short_shift_certificate
```

The certificate uses only the Python standard library and checks finite identities, not the analytic short-interval input or an open prime asymptotic.
