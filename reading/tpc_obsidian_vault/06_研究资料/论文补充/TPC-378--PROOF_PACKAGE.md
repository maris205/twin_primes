---
type: "source-reading"
source_path: "papers/tpc-378-c1-scale-origin-crossholdout/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-378"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-378-c1-scale-origin-crossholdout/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-378|TPC-378]] · [[00_开始阅读|首页]]

# TPC-378 proof and audit package

1.  The affine candidate grid, selected indices, origins, endpoint counts, signs, beta, exponent, height, Q anchors, and c=1 mask are literal constants in the producer and independent checker. Selection is declared response-blind and the complete panel is built before metrics are read.
2.  Current intervals and the inherited largest intervals are disjoint by exact integer endpoint inequalities. This proves only the finite coordinate separation recorded in the protocol.
3.  The full-window geometry is a finite sum of nonnegative rational squares; the exact anchor checks positivity and symmetry.
4.  The c=1 band/tail decomposition is an entrywise finite mask identity. For each computed extremal eigenvector, residual, norm, symmetry, and the band-plus-tail Rayleigh identity are checked numerically.
5.  The producer locks TPC-377’s code and canonical certificate. A separate reverse-shell checker rebuilds the prime shell and all 18 eigensystems without importing the TPC-378 producer. A 24-mutation stress suite rejects altered protocol, result, and firewall documents.
6.  Normal and optimized runs must return zero, write no stderr, and emit byte-identical summaries. These checks certify the finite artifact only; they do not promote an arithmetic or asymptotic gate.
