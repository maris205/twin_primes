---
type: "source-reading"
source_path: "papers/tpc-185-prefix-block-equivalence/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-185"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-185-prefix-block-equivalence/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-185|TPC-185]] · [[00_开始阅读|首页]]

# TPC-185: Prefix Maxima and Consecutive Blocks: An Exact Deterministic Equivalence

## Exact result

For every finite sequence, the largest consecutive-block sum is at most twice the largest prefix sum, while every prefix is itself a consecutive block. Thus a uniform block theorem and the desired prefix theorem are equivalent up to the literal factor two, with no phase, scale, support, or power change.

```text
classification = REDUCTION_L1
verdict = EXACT_FACTOR_TWO_EQUIVALENCE
selected_route = O161.bad_endpoint_pointwise_fixed_atom
smallest_missing = NAMED_ATOM_CONSECUTIVE_BLOCK_POWER_SAVING

fixed_atom_decay_obtained = false
named_atom_endpoint_credit = 0
strict_1/400 = UNPAID
```

The result is L0/L1 only. Any `STOP_SCOPED` declaration applies only to the named method cell and does not stop an O161 pointwise parent or the global architecture. No program-positive L2, prime-pair lower bound, or twin-prime theorem is claimed.

## Reproduce

```powershell
python experiments/tpc185_prefix_block_equivalence.py
python experiments/tpc185_prefix_block_equivalence.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
