---
type: "source-reading"
source_path: "papers/tpc-121-fiber-phase-coherence-certificate/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-121"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-121-fiber-phase-coherence-certificate/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-121|TPC-121]] · [[00_开始阅读|首页]]

# TPC-121: Fiber phase-coherence certificate

This paper refines the open determinant-energy input isolated in TPC-110 and TPC-112.

For a literal post-bin coefficient

```text
A(n) = sum_{t in F_n} u_t,
D = sum_n |A(n)|^2,
E = sum_t |u_t|^2,
```

it proves the exact mean-fluctuation splitting

```text
E = C + V,
D = sum_n m_n C_n,
```

where `C_n` is the energy of the fiber mean and `V` is the within-fiber fluctuation energy.

It then gives a coefficient-specific phase-sector certificate. If a good subset of a fiber lies in a common sector with cosine margin `kappa`, while the bad absolute mass is at most `theta` times the good absolute mass, then

```text
|A(n)| >= (kappa - theta) sum_good |u_t|.
```

Let `R_cert` be the effective participation ratio of the good absolute mass inside determinant fibers. A lower bound for the diagonal mass, a participation gain `gamma_R`, and a phase margin then produce the explicit determinant exponent

```text
lambda_D_cert = (lambda_E + 2 lambda_phi - gamma_R)_+.
```

The paper does not prove either growing input for the actual coefficient. In particular, TPC-110’s diagonal ceiling shows that participation growth is indispensable for reaching `lambda_D < 1`. The exact identities are L0 and their attachment to the literal TPC-110 fibers is L1. No L2 fixed-shift arithmetic saving, parity breach, or twin-prime conclusion is claimed.

## Reproduce

```powershell
python experiments/tpc121_phase_coherence_audit.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Archival PDF:

`tpc-121-fiber-phase-coherence-certificate.pdf`

SHA-256:

`631fde72dc07c348e7fd3e82c3b84e0af1236200f131738349f6047997c6f3ac`
