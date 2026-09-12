---
type: "source-reading"
source_path: "papers/tpc-382-c1-origin-family-magnitude-audit/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-382"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-382-c1-origin-family-magnitude-audit/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-382|TPC-382]] · [[00_开始阅读|首页]]

# TPC-382 proof package

## Proposition (finite locked aggregation)

Given the three parent certificate byte strings named by the embedded SHA-256 locks, the TPC-382 producer and independent checker compute the same 12 same-count cells, 12 scale-control cells, and 12 matched-count contrasts. Each cell statistic is the stated finite minimum/maximum/mean transform of its listed values.

## Verification status

The proposition is checked by canonical JSON, parent source/certificate hashes, complete row-key censuses, recomputed arithmetic, and normal/optimized replay. The adversarial checker mutates 25 semantic fields and requires every mutation to be rejected.

## Boundary

This is a finite certificate-level proposition. It is not a proof of origin uniformity, scale uniformity, a source-valid normalization, an arithmetic estimate, a growing operator bound, or any twin-prime assertion.
