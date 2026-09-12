---
type: "source-reading"
source_path: "papers/tpc-306-two-way-operator-target-interaction/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-306"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-306-two-way-operator-target-interaction/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-306|TPC-306]] · [[00_开始阅读|首页]]

# TPC-306 derivation package

For one adjacent shell pair, write the four positive normalized budget cells with operator first and target second:

```text
B_LL = left operator on native left target
B_LR = left operator on transported right target
B_RL = right operator on transported left target
B_RR = right operator on native right target
```

The two target-switch effects for the common intervention `left -> right` are

```text
d_L = log(B_LR/B_LL),
d_R = log(B_RR/B_RL).
```

TPC-305 stores `R_L=B_LR/B_LL` and `R_R=B_RL/B_RR`, so `d_L=log(R_L)` and `d_R=-log(R_R)`. Define

```text
m = (d_L+d_R)/2                 target main contrast,
i = (d_L-d_R)/2                 operator interaction contrast,
q = |i|/|m|                     interaction-to-main magnitude ratio.
```

Then `d_L=m+i`, `d_R=m-i`, and hence

```text
m^2-i^2 = d_L*d_R.
```

When both effects are strict and have the same sign, `m^2>i^2`, so the main target contrast dominates. Opposite signs imply `i^2>m^2`, so interaction dominates. Multiplying both cells in either operator row by a positive factor leaves the corresponding log effect unchanged.

This is a decomposition of a finite shell-specific table. The transported target has a native off-overlap completion on each row, so the table is not a common-ambient causal experiment. The decomposition makes that limitation quantitative rather than hiding it.
