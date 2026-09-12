---
type: "source-reading"
source_path: "papers/tpc-375-bandwidth-stability-minimal-cutoff/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-375"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-375-bandwidth-stability-minimal-cutoff/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-375|TPC-375]] · [[00_开始阅读|首页]]

# TPC-375 proof and certificate package

## Exact finite statements

1.  The beta=2 panel, all origins, all Q anchors, block partition, and cutoff list `{0,1,2,3}` are fixed before any band metric is read.
2.  The full-window geometry is a finite sum of nonnegative rational squares and is shared by the full matrix and all four bands.
3.  The nested masks give `T=B_c+(T-B_c)` entrywise for every declared cutoff.
4.  Each full, band, and tail object is a finite symmetric matrix; the full extremal-mode selection rule is deterministic with an explicit tie break.
5.  The band and tail Rayleigh terms sum to the selected full eigenvalue by linearity.

## Certificate contents

`results/tpc375_certificate.json` stores all nine rows, full and four-band metrics, tail and Rayleigh fields, cutoff-specific failure keys, minimal-cutoff census, inherited parent locks, exact-anchor digests, and the claim firewall. The independent checker uses a separate sieve and descending shell order and rebuilds the matrices and eigensystems. The stress suite mutates protocol, provenance, bands, rows, metrics, phase counts, anchor, firewall, and clue.

Local Bridge-B reruns producer, independent replay, and stress in normal and optimized Python modes, requiring empty stderr and byte-identical output. The official Route-A/Route-B evaluator files are absent; no official pass is claimed.

## Finite status

The first cutoff reproducing the parent six-key spectral failure set is `c=1`. Cutoff `c=0` has no beta=2 spectral failure, while `c=1,2,3` each have all six. This is a finite minimal-cutoff result only: `ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, `FULL_GATE_B=OPEN`, and the twin-prime result is `NONE`.
