---
type: "source-reading"
source_path: "papers/tpc-363-bulk-persistence-localization/experiments/protocol.md"
snapshot_date: "2026-09-12"
owner: "TPC-363"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-363-bulk-persistence-localization/experiments/protocol.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-363|TPC-363]] · [[00_开始阅读|首页]]

# TPC-363 frozen protocol

1.  Inherit exactly the TPC-361 ordered high-origin panel `(313030,311166,321651)` and the TPC-362 literal operator. No response, source vector, or adaptive sign is used.
2.  Use counts `N={256,512}`, shell anchors `Q={80,128,256}`, exponents `s={1,2}`, and the four fixed laws `all_plus`, `alternating_index`, `mod4_character`, and `half_split`.
3.  Record all `3*2*3*2*4=144` normalized matrices and true spectra. For each row record the Schur row-mass maximum, the extremal-eigenvector mass profile, and the two deterministic principal restrictions below.
4.  Set `k=floor(N/20)`. Remove the `k` rows with largest normalized Schur row mass, and separately remove the `k` coordinates with largest squared mass in the eigenvector belonging to the largest absolute eigenvalue. Ties are resolved by stable descending score and then original index. Recompute the spectral norm of each resulting principal submatrix.
5.  Use `0.64` only as the inherited finite working spectral cap. Compare the `Q=80` control rows with the first-failure `Q=128` rows and the stress `Q=256` rows. A persistence statement means that both five-percent restrictions still exceed `0.64` for a row that already exceeds `0.64`.
6.  Rebuild the complete certificate with the producer, an independent reverse-shell implementation, a 16-mutation certificate stress test, and the local fail-closed Bridge-B checker in normal and optimized modes. The rational `Q=4`, exponent-1 anchor on `[313060,313073]` is retained.

This protocol tests whether the observed failure is concentrated in a small row/eigenvector spike. It is a finite localization/obstruction audit. It does not imply that every possible normalization fails, and it does not promote a finite cap failure to an asymptotic statement.
