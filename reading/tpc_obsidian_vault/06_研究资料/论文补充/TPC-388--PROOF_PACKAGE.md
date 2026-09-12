---
type: "source-reading"
source_path: "papers/tpc-388-c1-cross-family-slope-transfer/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-388"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-388-c1-cross-family-slope-transfer/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-388|TPC-388]] · [[00_开始阅读|首页]]

# TPC-388 proof package

## PROVED\_EXACT\_FINITE

-   The candidate grid, selected indices, origin roles, count roles, bands, and parent-slope freeze are fixed before current-family endpoint readout.
-   The current intervals are pairwise disjoint and disjoint from all listed prior panels.
-   The 13-point rational anchor has positive geometry and symmetric matrices for all four laws.
-   The TPC-387 parent certificate hash and cell-slope interface are checked.

## NUMERICALLY\_CERTIFIED\_FINITE

-   256 rows and 32 cells replay in ordinary and optimized Python modes.
-   All 32 frozen parent-slope forecasts and all 32 local controls pass the 3% finite transfer cap.
-   The stability census is `24/32`, `24/32`, `28/32`; the spectral diagnostic has 40 finite failures and the Schur diagnostic has none.
-   Twenty-five structural certificate mutations are rejected.

## OPEN

The finite transfer does not establish origin-uniformity, count-uniformity, source-valid normalization, a growing operator bound, or arithmetic `L2`. Route reassembly and any twin-prime conclusion remain open.
