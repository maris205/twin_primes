---
type: "source-reading"
source_path: "papers/tpc-220-prime-ap-collision-crosswalk/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-220"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-220-prime-ap-collision-crosswalk/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-220|TPC-220]] · [[00_开始阅读|首页]]

# TPC-220 Route A / Route B Evaluation

The named Session evaluator files are absent from this checkout; the fallback authority is `AGENTS.md`, `TPC_HANDOFF.md`, the parent proof, and the current theorem/checker package.

## Route A

NOT\_APPLICABLE.

## Route B

STRUCTURAL\_THRESHOLD\_A = PASS. The crosswalk acts on the literal row and retains q, h, primitive support, cutoff, and profile weight.

## Claim ceiling

```text
PROVED_STRUCTURAL_L1
REFUTED_SCOPED (no free off-diagonal orthogonality follows from the identity)
OPEN (quantitative off-diagonal collision control)
```

No arithmetic `L2`, fixed-atom credit, or strict `1/400` payment is awarded.

## Extraction

-   strongest positive result: exact weighted prime-AP/multiplicative collision crosswalk;
-   strongest obstruction: off-diagonal Gram is a genuine collision graph, not a diagonal;
-   open theorem: a source-valid estimate for that graph;
-   reusable structure: primitive AP incidence and diagonal/off-diagonal separation;
-   ROUND2\_CLUE: `QUANTIFY_THE_OFF_DIAGONAL_COLLISION_GRAPH_BEYOND_SCHUR`.
