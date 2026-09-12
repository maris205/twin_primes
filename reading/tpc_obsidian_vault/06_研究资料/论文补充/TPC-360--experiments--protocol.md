---
type: "source-reading"
source_path: "papers/tpc-360-schur-tightness-law-uniform-audit/experiments/protocol.md"
snapshot_date: "2026-09-12"
owner: "TPC-360"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-360-schur-tightness-law-uniform-audit/experiments/protocol.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-360|TPC-360]] · [[00_开始阅读|首页]]

# TPC-360 frozen protocol

1.  Inherit exactly the three TPC-359 origins `(267175,261267,269074)`.
2.  Use counts `256,512`, `Q=24,54,80`, exponents `1,2`, and the four fixed laws `all_plus`, `alternating_index`, `mod4_character`, `half_split`.
3.  For every one of the 144 rows compute normalized Schur row sum, Frobenius norm, extreme eigenvalue norm, and the two ratios spectral/Schur and spectral/Frobenius.
4.  Compare the four laws within each of the 36 `(origin,count,Q,exponent)` settings; do not select a law based on a response.
5.  Lock the finite inequalities and rational anchor, run reverse-shell replay, 14 mutation tests, and normal/optimized Bridge-B.

All conclusions are finite and scoped; no source response is used.
