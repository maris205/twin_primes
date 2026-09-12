---
type: "source-reading"
source_path: "papers/tpc-377-c1-window-scale-holdout/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-377"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-377-c1-window-scale-holdout/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-377|TPC-377]] · [[00_开始阅读|首页]]

# TPC-377 proof and audit package

1.  The count ladder, origins, Q anchors, signs, beta, exponent, block length, and c=1 mask are literal constants in the producer and checker.
2.  The full-window square-energy diagonal is positive because it is a finite sum of nonnegative rational squares; the exact anchor checks this with rational arithmetic.
3.  The three windows at each origin are nested prefixes, so the scale relation is proved exactly at the protocol level.
4.  The band/tail decomposition is an entrywise finite mask identity.
5.  The selected full eigenvector gives the exact finite Rayleigh decomposition; residual, norm, symmetry, and Schur/Frobenius envelopes are checked numerically.
6.  A reverse-shell independent replay and mutation stress test certify only the declared 27-row finite certificate. No arithmetic or asymptotic gate is promoted.
