---
type: "source-reading"
source_path: "papers/tpc-358-fresh-origin-spectral-holdout/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-358"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-358-fresh-origin-spectral-holdout/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-358|TPC-358]] · [[00_开始阅读|首页]]

# TPC-358 proof and scope package

## Proposition 1: finite norm envelope

For every finite real symmetric matrix, the induced-norm inequality and the singular-value decomposition give the Schur row-sum and Frobenius envelopes. This is an exact finite statement.

## Proposition 2: fresh finite congruence

The declared fresh panel has positive unsigned geometry on every row. Thus the position-aware diagonal congruence is defined and remains symmetric.

## Proposition 3: certified transfer replay

The canonical certificate contains 288 unique law-level rows and 144 spectral metrics. The fresh normalized Schur maximum is `0.80850510742101689`, below the frozen `0.83` threshold; the all-plus spectral maximum is `0.62663944469203836`, below `0.64`. The reverse-shell checker reproduces the rows within the declared tolerance and confirms the exact anchor.

## Proposition 4: finite scale obstruction

Among 54 adjacent fresh count transitions, normalized all-plus spectral values have 13 increases, 34 decreases, and 7 flats under guard `10^-6`. Hence nonincreasing decay is false on this finite ladder, without implying an asymptotic nonmonotonicity theorem.

## Scope firewall

The maximum status is `NUMERICALLY_CERTIFIED_FINITE`. No source response is used, no arithmetic advance or fixed-power credit is paid, the official Route-A/Route-B evaluator files are absent, and full Gate B remains open.
