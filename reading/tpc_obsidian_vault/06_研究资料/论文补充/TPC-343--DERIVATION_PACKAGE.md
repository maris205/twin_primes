---
type: "source-reading"
source_path: "papers/tpc-343-cross-panel-meta-certificate/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-343"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-343-cross-panel-meta-certificate/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-343|TPC-343]] · [[00_开始阅读|首页]]

# TPC-343 derivation package

Let `y_r` be the twin-mean output for row `r`, and let `N_r=(n_{r,1},n_{r,2},n_{r,3})` be the three nuisance means. For the six rows, the row-block model uses

```text
N_block = diag(N_1,...,N_6).
```

The shared model uses the three vertically concatenated columns

```text
n_j^shared = (n_{1,j},...,n_{6,j})^T,   j=1,2,3.
```

For either matrix `N`, write `P_N` for the Euclidean orthogonal projector onto its column space. The finite identity is

```text
||Y||_2^2 = ||P_N Y||_2^2 + ||(I-P_N)Y||_2^2.
```

For equal-row weighting, each row is transformed by the same scalar within its target/nuisance block:

```text
Y_r -> Y_r / ||y_r||_2,     n_{r,j} -> n_{r,j} / ||y_r||_2.
```

This preserves each row’s projection geometry while changing the meta weight; it is a declared sensitivity model, not a canonical normalization theorem.

The row-block energy is additive because its columns have disjoint row supports. Consequently its residual retention is the target-energy-weighted average of the six row residual retentions. The shared model can only use one coefficient vector and is therefore a different, strictly smaller candidate span in the declared finite experiment.

The holdout version fixes an omitted control `j`, constructs nuisance means from the other eight controls in every row, and repeats the same two stackings. No probabilistic independence or asymptotic passage is used.
