---
type: "source-reading"
source_path: "papers/tpc-249-sharp-weighted-shared-lane-contraction/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-249"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-249-sharp-weighted-shared-lane-contraction/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-249|TPC-249]] · [[00_开始阅读|首页]]

# Route evaluation

Route A is unchanged. Route B gains an exact structural contraction that removes the artificial tagged-copy radius and preserves within-lane cancellation. Actual Gram asymptotics remain the arithmetic gate.

-   strongest positive result: exact radius `sum rho_c sqrt(lambda_c*G_c lambda_c)`;
-   strongest obstruction: fixed marginals allow exact radius anywhere down to zero;
-   open theorem: estimate literal V59 Gram quadratic forms;
-   reusable structure: weighted probe vector + Gram support + budget ledger;
-   `ROUND2_CLUE`: `ESTIMATE_LITERAL_GRAM_QUADRATIC_FORMS_OR_BOUND_THEM_FROM_COMPUTABLE_COHERENCE_DATA`.
