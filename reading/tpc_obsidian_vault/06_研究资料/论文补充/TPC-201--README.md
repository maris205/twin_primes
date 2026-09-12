---
type: "source-reading"
source_path: "papers/tpc-201-degenerate-shift-fejer-absorption/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-201"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-201-degenerate-shift-fejer-absorption/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-201|TPC-201]] · [[00_开始阅读|首页]]

# TPC-201: Absorbing the Unique Degenerate Fejer Shift into the Diagonal Ledger

## Result

In the normalized TPC-130 Fejer inequality, the unique q=1,h=2 degenerate correlation is bounded by the same energy E as the diagonal. It changes the diagonal coefficient from 2 to at most 6 in units of 1/(H p), leaving only nondegenerate four-Mobius shifts.

```text
classification = ANALYTIC_REDUCTION_L1
verdict = PROVED_DEGENERATE_SHIFT_ABSORPTION
first_missing = UNIFORM_NONDEGENERATE_FOUR_MOBIUS_OFFDIAGONAL_POWER_BOUND
next_route = NONDEGENERATE_FEJER_OFFDIAGONAL
TPC193_DECLARED_CANDIDATE_MECHANISM_CORPUS_V1 = STOP_SCOPED
bad_endpoint_O161_parent = OPEN
direct_twist_O161_parent = OPEN
global_architecture = OPEN
fixed_atom_decay_obtained = false
named_atom_endpoint_credit = 0
strict_1/400 = UNPAID
```

This is an L0/L1 artifact. It claims no program-positive L2 result, prime-pair lower bound, or twin-prime theorem.

## Reproduce

```powershell
python experiments/tpc201_degenerate_shift_fejer_absorption.py
python experiments/tpc201_degenerate_shift_fejer_absorption.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
