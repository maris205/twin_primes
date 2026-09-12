---
type: "source-reading"
source_path: "papers/tpc-337-control-covariance-masked-response/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-337"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-337-control-covariance-masked-response/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-337|TPC-337]] · [[00_开始阅读|首页]]

# TPC-337 proof and scope package

## Proposition 1 — finite covariance decomposition

Equations (1)–(3) in `DERIVATION_PACKAGE.md` hold for every finite matrix, every finite family of vectors, and the declared coordinate controls.

**Proof.** Write each vector as its mean plus its centered part. The sum of the centered parts is zero, so the two mixed terms vanish after averaging. The class-pair identity follows by the same expansion. `QED`.

## Proposition 2 — covariance-Gram positivity

The class covariance matrix `K` is positive semidefinite.

**Proof.** Equation (4) is a sum of squared Euclidean norms divided by five. `QED`.

## Finite certificate

The producer and an independent reverse-shell implementation recompute six windows, four masks, and five controls. The full centered fraction is above `0.75` in all six rows and the coherent fraction is below `0.25`. The twin/background covariance is positive in `6/6` rows; twin/zero and background/zero are negative in `6/6`. The numerical eigenvalue guard is nonnegative up to the stated floating-point tolerance.

## Scope boundary

This is a finite control-orbit covariance result. It does not establish a growing covariance theorem, a canonical sign law, an arithmetic cancellation estimate, a fixed-power credit, or a twin-prime conclusion. In particular, the negative covariance signs are observations of this panel, not universal sign assertions.
