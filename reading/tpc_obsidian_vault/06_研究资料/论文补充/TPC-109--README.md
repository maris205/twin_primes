---
type: "source-reading"
source_path: "papers/tpc-109-coherent-prime-square-saturation/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-109"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-109-coherent-prime-square-saturation/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-109|TPC-109]] · [[00_开始阅读|首页]]

# TPC-109: Coherent Prime-Square Saturation

This paper resolves the coefficient-blind part of the coherent terminal-prime square proposed in TPC-MVP1.

Main exact result:

$$ \left\{\left|\sum_p a_p e^{i\theta_p}\right|^2\right\} = \left[(2a_{\max}-\sum_pa_p)_+^2,\,       (\sum_pa_p)^2\right]. $$

Consequences:

-   the coherent-prime Gram matrix is rank one;
-   the Bessel factor `number of active primes` is sharp;
-   terminal-prime injectivity, occupancy, moduli, and diagonal energy do not force a coherent saving or a coherent lower bound;
-   any continuation must use the literal arithmetic phases or a proved dominant-prime statistic.

This is an L0/L1 saturation and route-switch certificate. It is not an L2 fixed-shift estimate and does not prove parity cancellation, prime pairs, or twin primes.

## Reproduction

```powershell
python experiments/tpc109_audit.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Stable archival PDF:

`tpc-109-coherent-prime-square-saturation.pdf`

SHA-256:

`8F37C934F47D526C5282A86384A59E453DD44F76786EC7D60E5A43B04A693108`

Release QA: 5 A4 pages, all fonts embedded, no Type 3 fonts, and all pages rendered and visually inspected.
