---
type: "source-reading"
source_path: "papers/tpc-324-source-profile-holdout/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-324"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-324-source-profile-holdout/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-324|TPC-324]] · [[00_开始阅读|首页]]

# TPC-324 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` are absent from this checkout. No official Route-A or Route-B pass is asserted.

Available fail-closed evidence:

1.  exact conditional covariance proof;
2.  producer certificate locked to TPC-323;
3.  independent reverse/einsum replay on both holdout panels;
4.  disjointness, covariance, and nontrivial-offset stress suite;
5.  local Bridge-B checker with sealed hashes and normal/optimized equality.

```text
ROUTE_B_LOCAL = YES_SCOPED_SOURCE_LOCATION_HOLDOUT_REPLICATION
ARITHMETIC_ROUTE_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```
