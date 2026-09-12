---
type: "source-reading"
source_path: "papers/tpc-315-fresh-source-locked-weight-holdout/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-315"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-315-fresh-source-locked-weight-holdout/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-315|TPC-315]] · [[00_开始阅读|首页]]

# TPC-315 local route evaluation

The Session-named `propose.md` and `skills/route-a-evaluator.md` / `skills/route-b-evaluator.md` are absent from this checkout. This is a local fail-closed assessment using the proof package, canonical certificate, independent replay, stress suite, and Bridge-B checker.

```text
ROUTE_A = NOT_EVALUATED_OFFICIALLY
ROUTE_B = SCOPED_ADVANCE_ONLY
ROUTE_B_FRESH_CLASS_REPLICATION = YES_FINITE_8_OF_8_ROWS
ROUTE_B_WEIGHTED_CASES = YES_FINITE_24_PLUS_24
ROUTE_B_ORDER_OBSTRUCTION = YES_FINITE_3_MINIMUM_TYPES_2_POSITIVE_TYPES
ROUTE_B_EXTERNAL_INDEPENDENCE = NO_SAME_LOCKED_TPC268_ENGINE
ROUTE_B_ASYMPTOTIC_ARITHMETIC = NO
ROUTE_B_FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```

Strongest positive: all three locked laws retain the strict finite class on the fresh source panel, with exact target recomputation and independent endpoint replay.

Strongest obstruction: the detailed law ordering changes, and the fresh minimum census has three types rather than a single canonical order.

Open theorem: connect the fresh literal outputs to an arithmetic `L2` bound, then separately investigate any growing statement.

ROUND2\_CLUE = PROBE\_LITERAL\_ARITHMETIC\_L2\_INTERFACE\_ON\_THE\_FRESH\_PANEL\_BEFORE\_ANY\_GROWING\_CLAIM
