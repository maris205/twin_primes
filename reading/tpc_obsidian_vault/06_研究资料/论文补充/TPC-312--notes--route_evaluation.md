---
type: "source-reading"
source_path: "papers/tpc-312-new-source-shell-separation-atlas/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-312"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-312-new-source-shell-separation-atlas/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-312|TPC-312]] · [[00_开始阅读|首页]]

# TPC-312 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` are absent from this checkout. The following is therefore a local fail-closed assessment, not an official evaluator result.

```text
ROUTE_A = NOT_EVALUATED_OFFICIAL_FILE_ABSENT
ROUTE_B = LOCAL_FAIL_CLOSED_NEW_SOURCE_FINITE_ATLAS_ONLY
POSITIVE = 8 exact new source-shell rows; 8/8 full modular rank; strict sign
           separation and exact Q/exponent ordering
OBSTRUCTION = same-engine new rows do not establish external independence or
              a uniform growing preference
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
L2 = NONE
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
ROUND2_CLUE = CERTIFY_NEW_PANEL_PROFILE_BUDGETS_WITH_OUTWARD_ROUNDING_BEFORE_ANY_HOLDOUT_PREFERENCE_CLAIM
```

The next paper should audit the profile-budget layer on these exact rows with outward rounding; merely reweighting this panel would not close the external holdout gap.
