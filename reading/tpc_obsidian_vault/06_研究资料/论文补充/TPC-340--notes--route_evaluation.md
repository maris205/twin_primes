---
type: "source-reading"
source_path: "papers/tpc-340-schur-frobenius-hybrid-envelope/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-340"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-340-schur-frobenius-hybrid-envelope/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-340|TPC-340]] · [[00_开始阅读|首页]]

# TPC-340 route evaluation

The local evidence is the finite Schur/Frobenius proof, parent-locked producer, independent reverse-shell replay, mutation stress, PDF audit, and fail-closed Bridge-B wrapper.

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` files are absent:

```text
Route-A = NOT_EVALUATED_OFFICIAL
Route-B = LOCAL_FAIL_CLOSED_FALLBACK
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```

The Schur branch materially improves the zero-support envelope, but the broad-mask tightness obstruction remains. The next step is a structural cross-class compensation/orthogonalization test or a fresh adversarial holdout.
