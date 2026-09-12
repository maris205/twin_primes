---
type: "source-reading"
source_path: "papers/tpc-382-c1-origin-family-magnitude-audit/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-382"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-382-c1-origin-family-magnitude-audit/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-382|TPC-382]] · [[00_开始阅读|首页]]

# TPC-382 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` are absent from this checkout. This document is therefore local fail-closed evidence, not an official evaluator verdict.

```text
same-count values = 72
same-count stable cells at 1% = 8/12
all-plus high-Q relative spread = 8.0645464844910632e-6
all-plus high-Q N2048/N1024 absolute contrast = 0.020813995160269608
arithmetic advance = NO
fixed power credit = 0
full Gate B = OPEN
```

The strongest positive result is finite all-plus high-Q magnitude stability across six origins at the matched count. The strongest obstruction is that the one-percent stability census is law-dependent and the matched-count magnitude is not one-percent invariant under the declared N=1024 scale control. The reusable structure is hash-locked certificate aggregation with separate same-count and scale cohorts. The next clue is `TEST_C1_POOLED_NORMALIZATION_CROSS_ORIGIN`.
