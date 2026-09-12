---
type: "source-reading"
source_path: "papers/tpc-383-c1-pooled-normalization-audit/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-383"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-383-c1-pooled-normalization-audit/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-383|TPC-383]] · [[00_开始阅读|首页]]

# TPC-383 route evaluation

The official Session evaluator files are absent from this checkout. This is local fail-closed evidence, not an official Route-A/Route-B verdict.

```text
rows = 72 (3 origins x 3 Q x 4 laws x 2 normalizations)
local stable cells = 9/12
pooled stable cells = 9/12
all-plus high-Q transfer = TRUE
pooled/local all-plus high-Q relative shift = 0.036457251256851203
arithmetic advance = NO
fixed power credit = 0
full Gate B = OPEN
```

The strongest positive result is transfer of all-plus high-Q origin stability to a common pooled scalar normalization. The strongest obstruction is the nonzero absolute calibration shift and the continuing law-dependent instability of alternating-index. Reusable structure: fresh affine holdout, common raw geometry, two law-independent normalizations, complete law/Q panel, and reverse-shell replay. Next clue: `TEST_C1_BANDWIDTH_NORMALIZATION_PHASE_DIAGRAM`.
