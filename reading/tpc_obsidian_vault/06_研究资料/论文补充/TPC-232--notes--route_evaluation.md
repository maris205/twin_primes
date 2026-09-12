---
type: "source-reading"
source_path: "papers/tpc-232-subcritical-growing-resonance-depth/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-232"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-232-subcritical-growing-resonance-depth/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-232|TPC-232]] · [[00_开始阅读|首页]]

# TPC-232 route evaluation

## Route A

`(A0,A1,A2,A3,A4)=(false,false,false,false,false)`. Route A is not addressed.

## Route B

-   `L0`: exact growing-depth support and channel compiler.
-   `L1`: source-backed arithmetic obstruction in the declared model.
-   `L2`: `NONE`.
-   full Gate B: `OPEN`.
-   strict $1/400$: `UNPAID_GLOBAL`.

## Extracted state

-   strongest positive result: uniform $O_A(LQ\log\log(3LQ)/\log^2Q)$ channel count.
-   strongest obstruction: every $L=o(\log Q/\log\log Q)$ remains too sparse.
-   open theorem: critical-depth mass/degree behavior and V59 attachment.
-   reusable structure: one-wrap compiler plus weighted coefficient-channel sieve.
-   `ROUND2_CLUE`: `TEST_CRITICAL_DEPTH_CLOCK_MASS_AND_DEGREE_BEFORE_V59_ATTACHMENT`.

## Verdict

`GO` as a genuine growing-family obstruction paper. `ARITHMETIC_ADVANCE=NO`.
