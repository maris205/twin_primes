---
type: "source-reading"
source_path: "papers/tpc-390-c1-recursive-slope-composition/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-390"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-390-c1-recursive-slope-composition/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-390|TPC-390]] · [[00_开始阅读|首页]]

# TPC-390 proof package

## PROVED\_EXACT\_FINITE

-   The candidate grid and selected indices are response-blind and fixed.
-   Calibration/holdout roles and all count levels are fixed before readout.
-   Current intervals are pairwise disjoint and disjoint from listed prior panels.
-   The 13-point rational `Q=8` anchor has positive geometry and symmetric matrices for all four sign laws.
-   The TPC-389 producer hash, certificate hash, schema, and frozen-slope interface are checked.
-   The sequential and direct parent-composition formulas are the same declared finite power-law expression, with a separately audited numerical residual.

## NUMERICALLY\_CERTIFIED\_FINITE

-   The producer rebuilds a complete 256-row, 32-cell panel.
-   The independent checker rebuilds it in descending prime-shell order without importing the producer.
-   One-step parent, local-control, and recursive-composition forecasts are recomputed from the rows and certificate summary.
-   The spectral and Schur failure censuses are recomputed, not trusted as metadata.
-   The adversarial certificate stress rejects altered hashes, roles, rows, summaries, and claim-firewall fields.

## OPEN / NOT CLAIMED

This package does not prove a count-uniform or origin-uniform law, a source-valid normalization, a growing operator bound, source-uniform arithmetic `L2`, Route-A/Route-B closure, or any twin-prime theorem. A finite recursive pass would not be an asymptotic composition theorem; a finite recursive failure is likewise only a scoped obstruction.
