---
type: "source-reading"
source_path: "papers/tpc-359-geometry-adversarial-high-origin-holdout/experiments/protocol.md"
snapshot_date: "2026-09-12"
owner: "TPC-359"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-359-geometry-adversarial-high-origin-holdout/experiments/protocol.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-359|TPC-359]] · [[00_开始阅读|首页]]

# TPC-359 frozen protocol

1.  Candidate origins are exactly `260001+211j`, `0<=j<=50`.
2.  Pilot count is 256. For each candidate, compute only unsigned `G` at `(Q,s)` in `{24,54,80} x {1,2}` and score by the largest `max(G)/min(G)`.
3.  Sort by decreasing score and origin, greedily retain origins separated by at least 1536, and require `(267175,261267,269074)`.
4.  Replay counts `(256,512,1024,2048)`, the three shell anchors, two kernel exponents, and four fixed sign laws. Compute spectra only for all-plus.
5.  Record canonical JSON, run the independent reverse-shell checker and 14 certificate mutations, then run the local Bridge-B checker in normal and optimized modes.

The score is fixed before signed matrices are evaluated. All conclusions are finite and scoped to this protocol.
