---
type: "source-reading"
source_path: "papers/tpc-146-frontier-four-map-completion-certificate/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-146"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-146-frontier-four-map-completion-certificate/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-146|TPC-146]] · [[00_开始阅读|首页]]

# TPC-146: Frontier four-map completion certificate

This paper assembles the exact map-route contract for frontier totalization. The certificate keeps the two legitimate routes separate:

1.  a fully typed map route with a conservative occurrence lift, total `Q_D`, `Q_Z`, `G`, downstream `P_h0`, compatibility squares, physical cover, reconnection, and occurrence registry;
2.  an independent theorem proving the complete original-scale frontier scalar is `o(X)`, together with a theorem-backed disposition of every `ELIGIBLE_TAIL_OPEN` path.

The map route is represented by the zero-defect vector

```text
(D_L, D_QD, D_QZ, D_G, D_P, D_DZ, D_GP, D_cover, D_rec)
```

All components need theorem-backed exact matrices before they can be evaluated. Unknown is not zero. The audited domain is exactly `ALL_NONSOFT = ELIGIBLE_TAIL_OPEN + FRONTIER_UNMAPPED`; a finite empty eligible-tail census is not an asymptotic theorem.

The current verdict is:

```text
H1.frontier_totalization = NOT_TESTABLE
first missing = H1.frontier_occurrence_lift
```

The current-schema-only derivation is a scoped stopped route. The occurrence-augmented route and the scalar-plus-eligible-tail route are not stopped.

Run:

```bash
python experiments/tpc146_frontier_completion_audit.py
python experiments/tpc146_frontier_completion_audit.py --check
```
