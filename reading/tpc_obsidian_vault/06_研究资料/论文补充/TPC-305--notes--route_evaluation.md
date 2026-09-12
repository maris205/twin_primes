---
type: "source-reading"
source_path: "papers/tpc-305-counterfactual-transported-label-budget/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-305"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-305-counterfactual-transported-label-budget/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-305|TPC-305]] · [[00_开始阅读|首页]]

# TPC-305 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` files are absent from this checkout. No official Route-A or Route-B evaluator pass is asserted.

Local fail-closed assessment:

```text
ROUTE_A = NOT_APPLICABLE
ROUTE_B_STRUCTURAL = POSITIVE_SCOPED_COUNTERFACTUAL_CONTROL
FIXED_OPERATOR_TARGET_SWAP = PROVED_EXACT_FINITE
COUNTERFACTUAL_BUDGET_ATLAS = NUMERICALLY_CERTIFIED_FINITE_18_CASES_36_TABLES
MIDDLE_RIGHT_LABEL_CHEAPER = NUMERICALLY_CERTIFIED_FINITE_5_OF_6
MIDDLE_SAME_PREFIX_RIGHT_LABEL_CHEAPER = NUMERICALLY_CERTIFIED_FINITE_3_OF_3
CAUSAL_TARGET_OPERATOR_SEPARATION = PARTIAL_COUNTERFACTUAL_ONLY
OPERATOR_INTERACTION_TERM = OPEN
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The genuine advance is a fixed-row target swap. It localizes a target effect inside each operator, while explicitly leaving cross-operator interaction for the next project.
