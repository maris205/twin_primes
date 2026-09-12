---
type: "source-reading"
source_path: "papers/tpc-326-cross-origin-scale-replication/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-326"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-326-cross-origin-scale-replication/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-326|TPC-326]] · [[00_开始阅读|首页]]

# TPC-326 proof package

## Proposition 1 — finite profile typing

The direct and coherent matrices on each new ladder rung are positive semidefinite with positive trace, so their trace-normalized sorted spectra are probability vectors.

**Proof.** They are Gram matrices of finite block operators. The producer and independent replay check finite positive traces; spectral decomposition gives the assertion. `[PROVED_EXACT_FINITE]`

## Proposition 2 — cross-origin geometry

The four new intervals are strictly nested and disjoint from all parent panels. A one-step source shift changes at least one active residue mask for each `(scale,Q)` cell.

**Proof.** Endpoint comparison proves nesting and disjointness. The stress suite directly enumerates divisibility masks for the original and shifted source ranges and finds a change in all sixteen cells. `[PROVED_EXACT_FINITE]`

## Finite certified statement

At origin `16001`, all-plus profile majorization holds on `32/32` rows. The full profile and energy censuses equal those in the TPC-325 certificate, and the four new envelope values satisfy the declared cross-origin thresholds. These are finite numerical statements certified by producer, independent replay, stress suite, and local Bridge-B. `[NUMERICALLY_CERTIFIED_FINITE]`

## Non-claims

No uniform source theorem, scale limit, arithmetic cancellation, source-native `L2` estimate, fixed-power credit, strict `1/400` payment, official evaluator pass, or twin-prime result follows.
