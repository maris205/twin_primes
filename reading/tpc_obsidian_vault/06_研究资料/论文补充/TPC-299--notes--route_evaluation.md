---
type: "source-reading"
source_path: "papers/tpc-299-native-profile-budget-frontier/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-299"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-299-native-profile-budget-frontier/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-299|TPC-299]] · [[00_开始阅读|首页]]

# TPC-299 local route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` files are absent from this checkout. No official Route-A or Route-B pass is declared. The available fail-closed fallback is the theorem ledger, proof package, canonical certificate, independent source-first replay, exact stress suite, PDF audit, and Bridge-B checker.

```text
ROUTE_A = NOT_EVALUATED_SESSION_FILE_ABSENT
ROUTE_B = LOCAL_FAIL_CLOSED_CHECK_ONLY
ROUTE_B_FINITE_ADVANCE = YES_PROFILE_ANGLE_TO_NATIVE_BUDGET_FRONTIER
ROUTE_B_ARITHMETIC_ADVANCE = NO
ROUTE_B_FIXED_POWER_ADVANCE = NO
ROUTE_B_GATE_B = OPEN
```

Strongest positive: the exact KKT compiler turns a target tolerance into a native source-budget certificate.

Strongest obstruction: the weighted target needs more than `1e-3` of the frozen source norm on 14/18 first-threshold rows and 11/18 full-prefix rows, while the positive control stays below `1e-4` on all rows.

Open theorem: a uniform growing-shell bound for the restricted native profile budget frontier.

```text
ROUND2_CLUE = TEST_BUDGET_CONSTRAINED_PROFILE_FRONTIER_ON_GROWING_SHELLS_AND_SOURCE_NORMALIZATION
```
