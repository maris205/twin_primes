---
type: "source-reading"
source_path: "papers/tpc-134-boundary-complete-dyadic-prefix-tail-archive/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-134"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-134-boundary-complete-dyadic-prefix-tail-archive/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-134|TPC-134]] · [[00_开始阅读|首页]]

# TPC-134: Boundary-complete dyadic prefix-tail archive

Paper title:

> *A Boundary-Complete Dyadic Prefix–Tail Path Archive: Exact Column Conservation and Fixed-Shift Provenance*

## Result

TPC-134 turns every TPC-133 native atom into an actual finite path family. It uses an explicit normalized smooth dyadic partition and a declared integer `D0` policy. Every native divisor record enters exactly one of

```text
PREFIX: d <= D0
TAIL:   D0 < d <= V.
```

The edge weights are symbolic `psi` expression trees. Their exact sum is proved from the normalized bump identity, not estimated in floating point. The executable check verifies the exact finite child-index set and binds each child to its parent checksum; the symbolic theorem, not a numerical tolerance, supplies column conservation. For the complete path matrix,

```text
1^T M_134 = 1^T.
```

The native tuple, fixed `h0`, and unique physical normalization are preserved on every nonzero path. This yields an exact growing block identity, but it does not prove that any prefix or tail is small.

The partition identities are L0 and the literal TPC-15-to-block attachment is L1. No positive L2 estimate, physical cover, parity advance, or twin-prime theorem is claimed.

## Reproduce

Default deterministic write:

```powershell
python experiments/tpc134_branch_archive.py
```

Read-only check:

```powershell
python experiments/tpc134_branch_archive.py --check
```

Compile:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
