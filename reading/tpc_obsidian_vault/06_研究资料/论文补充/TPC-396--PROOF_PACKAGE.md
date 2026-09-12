---
type: "source-reading"
source_path: "papers/tpc-396-c1-signed-law-interpolation/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-396"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-396-c1-signed-law-interpolation/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-396|TPC-396]] · [[00_开始阅读|首页]]

# TPC-396 proof package

## Proved finite facts

1.  The six selected current intervals are pairwise disjoint and disjoint from the declared prior c=1 panels through TPC-395.
2.  The TPC-395 producer and certificate are normalized-LF hash-locked before any parent endpoint mean is read.
3.  Grid indices, calibration/holdout roles, count, coefficients, laws, normalizations, and caps are response-blind and fixed before readout.
4.  At `[6000001,6000014)` with `Q=8` and shell `{11,13}`, the geometry is positive, the endpoint matrices are symmetric, and all four rational interpolation identities hold exactly.
5.  The certificate contains the complete 96-row/16-cell Cartesian panel with canonical JSON and row/payload hashes.
6.  The independent checker reconstructs the shell in descending order, while the 28-case mutation suite rejects altered certificate contracts.

## Numerically certified finite facts

Twelve of sixteen cells pass the one-percent origin-spread rule: all four normalizations pass for `blend_0`, `blend_1_3`, and `blend_2_3`, while none pass for `blend_1`. Parent-relative holdout comparisons pass in all 16 cells. Parent calibration passes are `4/4` for local normalization and `3/4` for each scalar normalization. Within-family transfer passes are `4/4` locally and `3/4` for each scalar normalization. Spectral failures are `24/96` and Schur failures are `0/96`.

## Strongest obstruction

The alternating endpoint retains a roughly nine-percent origin spread on the fresh family, and three scalar-normalized transfer cells exceed the fixed three-percent cap. The result identifies a finite change between the tested values `lambda=2/3` and `lambda=1`; the interior interval `(2/3,1)` remains untested, and no universal threshold is claimed.

## Open theorem and route status

An analytic source-valid explanation, a growing origin-uniform estimate, and source-uniform arithmetic `L2` remain open. Route-A and Route-B are not closed; the official evaluator files are absent from this checkout. No fixed power credit, arithmetic advance, or twin-prime conclusion is assigned.

## Reusable structure and next clue

The reusable structure is a hash-locked endpoint interface, exact finite matrix interpolation, a fresh calibration/holdout family, independent reverse-order replay, and explicit failure caps. The next clue is

```text
ROUND2_CLUE = TEST_C1_INTERPOLATION_TRANSITION_REPLICATION
```
