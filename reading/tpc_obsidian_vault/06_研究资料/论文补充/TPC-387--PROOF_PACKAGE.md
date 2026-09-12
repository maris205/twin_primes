---
type: "source-reading"
source_path: "papers/tpc-387-c1-count-ladder-renormalization/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-387"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-387-c1-count-ladder-renormalization/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-387|TPC-387]] · [[00_开始阅读|首页]]

# TPC-387 proof package

## PROVED\_EXACT\_FINITE

-   Candidate grid, origin indices, count roles, band modes, and fit rule are fixed before holdout readout.
-   Current intervals are pairwise disjoint and disjoint from listed prior panels.
-   The rational 13-point anchor has positive geometry and symmetric matrices for all four laws.
-   Parent code and certificate hashes, JSON canonicality, and row digest are checked.

## NUMERICALLY\_CERTIFIED\_FINITE

-   256 rows and 32 cells replay in ordinary and optimized Python modes.
-   All 32 calibration-slope endpoint predictions pass the predeclared 3% cap.
-   The inherited spectral diagnostic has 40 finite failures and the Schur diagnostic has none; these counts are independently reproduced.
-   Twenty-five structural mutations are rejected.

## OPEN

The finite slope does not establish count uniformity, a growing operator bound, or validity of the source normalization. Arithmetic reassembly and a twin-prime theorem remain outside the certificate.
