---
type: "source-reading"
source_path: "papers/tpc-104-resolved-principal-mass-disintegration/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-104"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-104-resolved-principal-mass-disintegration/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-104|TPC-104]] · [[00_开始阅读|首页]]

# TPC-104: Resolved principal-mass disintegration

Paper title:

> *Resolved Principal Mass Before Width Grouping: Exact Endpoint Return and an Inverse-Length Equivalence*

## Exact result

For the actual remaining invertible opened atoms, define the full `N=1,2` endpoint mass `E_X` and the long inverse-length mass

```text
L_X = sum_{3 <= N_beta <= q_X} M_beta^inv / N_beta.
```

The principal coefficient is exactly one at `N=1,2`; its nonprincipal width factor is exactly zero. For `3 <= N <= q`,

```text
1/N <= 2 floor(q/N)/(q-1) <= 2q/((q-1)N).
```

Therefore

```text
E_X + L_X <= P_X <= E_X + (2q_X/(q_X-1)) L_X.
```

So Gate P is equivalent, in the same physical normalization, to bounding the actual endpoint mass and inverse-length mass separately. The paper also proves sharp abstract countermodels showing that the `1/N` factor does not remove a polynomial branch census and that long-fiber estimates cannot return `N=1,2`.

## Claim level

-   Coefficient identities and sharpness examples are L0.
-   Their exact attachment to the actual fixed-`h0` opened census is an L1 reduction.
-   Neither `E_X` nor `L_X` is bounded at the required growing scale. No L2 saving, route stop, parity breakthrough, or prime-pair theorem is claimed.

## Reproduce

```powershell
python experiments/tpc104_principal_mass_audit.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Archival PDF:

`resolved-principal-mass-disintegration.pdf`

SHA-256:

`CF5CFD55CDE7002B9B1555530B31C20A2829725503DBCECC9CD4496310081109`
