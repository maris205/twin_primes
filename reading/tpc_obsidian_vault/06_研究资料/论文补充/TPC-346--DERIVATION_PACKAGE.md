---
type: "source-reading"
source_path: "papers/tpc-346-third-panel-hostile-replication/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-346"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-346-third-panel-hostile-replication/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-346|TPC-346]] · [[00_开始阅读|首页]]

# TPC-346 derivation package

For panel p, let Y\_p be the stacked twin-target row means and let N\_p be the matrix whose columns are the three nuisance-category means. The shared three-panel model uses

```text
N_shared = [N_1; N_2; N_3].
```

The panel-adaptive model uses the block matrix

```text
N_adapt = diag(N_1,N_2,N_3).
```

The shared column space is contained in the adaptive block space: a common coefficient vector (c\_1,c\_2,c\_3) is represented by the block coefficient (c,c,c). Therefore finite orthogonal projection gives

```text
||(I-P_adapt)Y||_2 <= ||(I-P_shared)Y||_2.
```

This is only a finite nested-model monotonicity statement. It does not say that the additional panel-specific columns have a source-independent arithmetic meaning.

For a training collection T and held-out panel p, the transfer diagnostic fits N\_T c to Y\_T by least squares and measures

```text
||Y_p-N_p c||_2^2 / ||Y_p||_2^2.
```

It is a prediction residual, not an orthogonal projection identity. Equal-row weighting divides each row target and nuisance column by the positive norm of that row’s twin target before stacking. The hostile fresh control-LOO diagnostic uses the omitted control’s twin output as target and the mean of the other eight controls for each nuisance column.
