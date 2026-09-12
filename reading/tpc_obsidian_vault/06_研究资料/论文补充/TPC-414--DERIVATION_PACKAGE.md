---
type: "source-reading"
source_path: "papers/tpc-414-c1-three-shell-pooled-extension/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-414"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-414-c1-three-shell-pooled-extension/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-414|TPC-414]] · [[00_开始阅读|首页]]

# TPC-414 derivation package

The third complete shell is disjoint from the first two and all its primes remain larger than `N=264`. Pooling therefore preserves the masked local identities. The total count `36848` is even, restoring equal parity classes; the shell-local amplitude normalization still satisfies `a_i>1`, so the same Cauchy–Schwarz proof yields `z<=4/H`.
