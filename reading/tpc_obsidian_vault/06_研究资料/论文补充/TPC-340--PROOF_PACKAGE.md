---
type: "source-reading"
source_path: "papers/tpc-340-schur-frobenius-hybrid-envelope/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-340"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-340-schur-frobenius-hybrid-envelope/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-340|TPC-340]] · [[00_开始阅读|首页]]

# TPC-340 proof and scope package

## Proposition 1 — Schur envelope

For every finite symmetric matrix `A`, `||Ax||_2^2 <= R^2||x||_2^2`, where `R=max_i sum_j |A(i,j)|`.

**Proof.** For a symmetric matrix the induced 1- and infinity-norms are both `R`. The inequality `||A||_2^2 <= ||A||_1||A||_infty` proves the claim. `QED`.

## Proposition 2 — hybrid envelope

For vectors supported on `S`, `||Ax||^2 <= min(F(S)^2,R^2)||x||^2`.

**Proof.** Apply the TPC-339 support Frobenius inequality and Proposition 1, then take their minimum. `QED`.

## Finite certificate

All 216 records pass the hybrid bound. The Schur branch is active in 54 records, exactly the nine zero-support placements in each of six windows; the Frobenius branch is active in the other 162 records. The zero-support Frobenius gain is reduced by factors `1.250245--4.698443`. Broad-mask hybrid occupancy remains below `0.1868550366`, so the sharpening does not close the uniform tightness gate.

## Scope boundary

The norm inequalities are general finite statements. Branch counts and occupancy ranges are finite observations for the declared panel and do not provide a growing arithmetic estimate or fixed-power credit.
