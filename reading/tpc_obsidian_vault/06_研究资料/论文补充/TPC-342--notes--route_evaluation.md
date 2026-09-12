---
type: "source-reading"
source_path: "papers/tpc-342-independent-fresh-holdout-reproduction/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-342"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-342-independent-fresh-holdout-reproduction/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-342|TPC-342]] · [[00_开始阅读|首页]]

# TPC-342 route evaluation

The available evidence is:

-   an exact finite orthogonal-projection identity;
-   a TPC-341 protocol-locked producer on three disjoint new windows;
-   a reverse-shell independent replay;
-   six fail-closed mutation tests;
-   a compiled and audited PDF; and
-   a local Bridge-B wrapper with normal/optimized equality.

The Session-named propose.md, skills/route-a-evaluator.md, and skills/route-b-evaluator.md files are absent in this checkout. Therefore:

```text
Route-A = NOT_EVALUATED_OFFICIAL
Route-B = LOCAL_FAIL_CLOSED_FALLBACK
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```

The strongest positive result is independent finite replication of the aggregate-versus-holdout split. The strongest obstruction is that all 27 held-out tests remain above the predeclared residual guard. The next clue is cross-panel pooling, not an arithmetic promotion.
