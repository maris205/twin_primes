---
type: "source-reading"
source_path: "papers/tpc-273-margin-stability-matrix/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-273"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-273-margin-stability-matrix/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-273|TPC-273]] · [[00_开始阅读|首页]]

# Route evaluation

```text
ROUTE_A = NOT_APPLICABLE_TO_THIS_FINITE_BRIDGE_B_AUDIT
ROUTE_B = YES_SCOPED_FINITE_MARGIN_STABILITY_OBSTRUCTION
MAXIMUM_CLAIM = NUMERICALLY_CERTIFIED_FINITE_MARGIN_STABILITY_OBSTRUCTION
STRONGEST_POSITIVE = 32_ROW_OUTWARD_MARGIN_MATRIX_WITH_INDEPENDENT_REPLAY
STRONGEST_OBSTRUCTION = FIXED_SCALE_CUTOFF_FLIPS_ACROSS_MARGIN_BANDS
OPEN_THEOREM = SOURCE_LEVEL_MARGIN_UNIFORMITY_FOR_REGISTERED_GROWING_CUTOFF
REUSABLE_STRUCTURE = MARGIN2_INTERVAL -> TWO_THRESHOLD_BANDS -> HOSTILE_TRANSITION
ROUND2_CLUE = TEST_SOURCE_LEVEL_MARGIN_UNIFORMITY_ON_THE_LITERAL_GROWING_CUTOFF
```

The Session-named `propose.md` and evaluator files are absent from this checkout. The proof package, theorem ledger, producer, independent upstream engine replay, stress audit, bridge checker, and `AGENTS.md` are the fail-closed fallback. The obstruction is explicitly model-relative and finite; no asymptotic promotion is made.
