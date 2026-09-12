---
type: "source-reading"
source_path: "papers/tpc-412-c1-pooled-complete-shell-extension/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-412"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-412-c1-pooled-complete-shell-extension/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-412|TPC-412]] · [[00_开始阅读|首页]]

# TPC-412 derivation package

The pooled two-shell profile remains valid as `H` grows through `16,32,66,128` because every retained prime exceeds the largest window `N=512`. The shell-local amplitude contract is unchanged. Equal pooled parity counts and the same Cauchy–Schwarz cancellation therefore give the uniform finite bound `z<=4/H` at all four heights.
