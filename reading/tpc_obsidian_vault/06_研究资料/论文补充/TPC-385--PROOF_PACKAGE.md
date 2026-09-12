---
type: "source-reading"
source_path: "papers/tpc-385-c1-bandwidth-origin-holdout/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-385"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-385-c1-bandwidth-origin-holdout/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-385|TPC-385]] · [[00_开始阅读|首页]]

# TPC-385 proof package

## Finite proposition

For the predeclared five-origin panel, the producer constructs exactly `5 origins x 2 Q x 4 laws x 2 bandwidths x 2 normalizations = 160` rows. The three calibration origins alone determine each pooled training scalar; the two holdout origins do not enter it. The canonical certificate records every row, all 32 role-separated cells, the four locked parent forecast errors, and the exact rational anchor.

## Verification

The independent checker does not import the producer. It re-sieves the prime shell, accumulates in reverse shell order, rebuilds the masks and training-only pooled scalars, and compares all metrics, cells, forecasts, and exact-anchor digests. The mutation suite attacks schema, selection, role, row, phase, and claim-firewall fields. The local Bridge-B locks all project artifacts and runs producer, independent replay, and stress checks in normal and optimized modes.

## What is proved and what is not

The finite protocol, coordinate separation, role split, rational anchor, and the recorded numerical replay are the only paid claims. The four under-one- percent all-plus forecast errors establish only a finite, declared holdout transfer. They do not prove bandwidth monotonicity, law/origin/count uniformity, source-valid normalization, a growing operator bound, arithmetic (L\^2), power saving, Route-B reassembly, or the twin-prime conjecture.
