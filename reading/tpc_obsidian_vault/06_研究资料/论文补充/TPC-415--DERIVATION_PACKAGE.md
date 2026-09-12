---
type: "source-reading"
source_path: "papers/tpc-415-c1-three-shell-height-extension/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-415"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-415-c1-three-shell-height-extension/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-415|TPC-415]] · [[00_开始阅读|首页]]

# TPC-415 derivation package

The three complete shells are disjoint and every retained prime is larger than the largest window `N=512`. Thus pooling preserves the local mask identities at all four heights. The even pooled count gives equal parity classes, while shell-local positivity gives `a_i>1`; the same Cauchy–Schwarz cancellation therefore yields the uniform finite bound `z<=4/H`.
