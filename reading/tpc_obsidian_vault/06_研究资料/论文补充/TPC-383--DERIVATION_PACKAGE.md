---
type: "source-reading"
source_path: "papers/tpc-383-c1-pooled-normalization-audit/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-383"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-383-c1-pooled-normalization-audit/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-383|TPC-383]] · [[00_开始阅读|首页]]

# TPC-383 derivation package

Let `M_{o,Q,ell}` be the finite raw law matrix and `g_{o,Q}(i)` its common square-energy geometry. The two audited matrices are

`A^loc_{ij}=M_{ij}/sqrt(g(i)g(j))`, `A^pool_{ij}=M_{ij}/G_Q`,

where `G_Q` is the arithmetic mean of all `g_{o,Q}(i)` over the three fixed origins and all coordinates. The same block-distance-one mask is applied to both matrices. The reported observable is the largest absolute eigenvalue of the masked matrix.

For each law/Q/normalization cell, the origin spread is `(max s-min s)/mean s`. All constants, origins, laws, and the one-percent predicate are fixed before the matrix metrics are read.

The finite exact component is the common geometry and law-independent pooled scalar construction. The spectral values are numerical finite outputs, recomputed by an independent reverse-shell implementation. Neither normalization is identified with a source-valid arithmetic law, and no limit or power credit is inferred.
