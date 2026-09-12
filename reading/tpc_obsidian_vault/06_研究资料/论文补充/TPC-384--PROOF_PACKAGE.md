---
type: "source-reading"
source_path: "papers/tpc-384-c1-bandwidth-normalization-phase-diagram/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-384"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-384-c1-bandwidth-normalization-phase-diagram/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-384|TPC-384]] · [[00_开始阅读|首页]]

# TPC-384 proof package

## Finite proposition

For the predeclared affine panel, the producer constructs the complete `3 origins × 3 Q × 4 laws × 4 bandwidths × 2 normalizations = 288` row panel from one common raw component geometry per origin and Q. The certificate contains all rows, all 96 origin-spread cells, the failure census, and the exact q=8 anchor.

## Verification

The independent checker does not import the producer. It sieves the prime shell, accumulates in reverse shell order, rebuilds all bandwidth masks and normalizations, and compares every spectral value and phase statistic. The adversarial checker applies 25 schema, protocol, row, phase, and claim-firewall mutations. The local Bridge-B locks the source, certificate, proof materials, PDF, and documentation, then repeats producer, independent, and stress checks in normal and optimized modes.

## What is proved and what is not

The protocol, exact anchor, finite row identity, and finite numerical replay are the only claims paid by this package. `TPC384_BANDWIDTH_MONOTONICITY` is OPEN: the observed all-plus means increase over this four-point panel, but no monotonicity theorem is asserted. Neither normalization is declared source-valid, and no arithmetic (L\^2), power saving, Route-B reassembly, or twin-prime conclusion follows.
