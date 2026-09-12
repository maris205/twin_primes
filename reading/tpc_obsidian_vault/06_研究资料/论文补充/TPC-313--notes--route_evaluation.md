---
type: "source-reading"
source_path: "papers/tpc-313-outward-budget-interval-certificate/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-313"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-313-outward-budget-interval-certificate/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-313|TPC-313]] · [[00_开始阅读|首页]]

# TPC-313 local route evaluation

The Session-named `propose.md` and `skills/route-a-evaluator.md`/ `route-b-evaluator.md` are absent from this checkout. This is a fail-closed local assessment using the proof package, exact certificate, independent replay, stress suite, and Bridge-B checker.

```text
ROUTE_A = NOT_EVALUATED_OFFICIALLY
ROUTE_B = SCOPED_ADVANCE_ONLY
ROUTE_B_FINITE_INTERFACE = YES
ROUTE_B_ASYMPTOTIC_ARITHMETIC = NO
ROUTE_B_EXTERNAL_INDEPENDENCE = NO
ROUTE_B_FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```

Strongest positive: a formal outward-rounded rational budget interface on a new source-shell panel, with strict finite thresholds on a common prefix.

Strongest obstruction: the weighted label is still generated from the same physical Gram, and no canonical/external weighting law follows.

Open theorem: a weighting law justified independently of the target Gram that survives a genuinely fresh physical holdout and admits a growing estimate.

Reusable structure: `source profile -> exact image/Gram -> first feasible prefix -> rational primal/dual pair -> outward interval -> threshold audit`.

`ROUND2_CLUE = AUDIT_EXTERNALLY_JUSTIFIED_WEIGHTING_ON_A_FRESH_PHYSICAL_HOLDOUT_AFTER_FORMAL_BUDGET_CERTIFICATION`.
