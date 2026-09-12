---
type: "source-reading"
source_path: "papers/tpc-381-c1-origin-family-replay/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-381"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-381-c1-origin-family-replay/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-381|TPC-381]] · [[00_开始阅读|首页]]

# TPC-381 proof and audit package: c=1 origin-family replay

1.  The affine grid, selected origins, `N=2048` count, eight-block partition, four sign laws, Q ladder, beta, exponent, height, caps, and c=1 mask are literal constants. The producer constructs all 36 rows before computing the profile summary.
2.  Exact integer endpoint inequalities certify disjointness from the largest declared TPC-376–380 windows. This is finite disjointness only.
3.  The normalization is one nonnegative square-energy sum shared by all laws. The q=8 anchor `[1400001,1400014)` independently checks positive rational geometry and symmetry for every law; it is fixed before metric readout.
4.  Each row checks finite spectral, Schur, Frobenius, symmetry, eigenvector residual, norm, and band-plus-tail Rayleigh identities.
5.  The producer locks TPC-380’s source and canonical certificate. The independent checker uses a direct sieve through 20000 and reverse shell order, reconstructing all rows without importing the producer.
6.  The 25-mutation stress suite rejects altered selection, count, law, row, census, clue, and firewall fields. Normal and optimized runs require empty stderr and identical summaries. Local Bridge-B locks stable project artifacts and repeats the checks.

Every item above certifies a finite artifact. No arithmetic gate or twin-prime claim is promoted.
