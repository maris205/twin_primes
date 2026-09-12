---
type: "source-reading"
source_path: "papers/tpc-265-schur-endpoint-budget-compiler/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-265"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-265-schur-endpoint-budget-compiler/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-265|TPC-265]] · [[00_开始阅读|首页]]

# TPC-265 route evaluation

```text
ROUTE_B = YES_SCOPED_RESIDUAL_RADIUS_BUDGET_COMPILER
POSITIVE = sharp worst-case Schur reassembly envelope |c|+R
POSITIVE = exact strict two-lane threshold 1/400
OBSTRUCTION = a disk always contains the aligned residual endpoint
OPEN_THEOREM = literal V59 radius saving or signed phase restriction
ROUND2_CLUE = TEST_LITERAL_RESIDUAL_RADIUS_OR_PHASE_AGAINST_THE_TWO_LANE_BUDGET
```

Route A remains inactive for the twin-prime endpoint. No arithmetic `L2` or full Gate-B payment is claimed.
