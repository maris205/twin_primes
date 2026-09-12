---
type: "source-reading"
source_path: "papers/tpc-323-signed-profile-majorization/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-323"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-323-signed-profile-majorization/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-323|TPC-323]] · [[00_开始阅读|首页]]

# TPC-323 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` are absent from this checkout. Therefore no official Route-A or Route-B pass is asserted.

Available fail-closed evidence:

1.  exact trace/profile factorisation in `PROOF_PACKAGE.md`;
2.  producer certificate with parent lock to TPC-322;
3.  independent reverse/einsum replay;
4.  deterministic profile stress suite;
5.  local Bridge-B checker, including normal/optimized subprocess equality and sealed source/PDF hashes.

Local route label:

```text
ROUTE_B_LOCAL = YES_SCOPED_FINITE_SIGNED_PROFILE_READOUT
ARITHMETIC_ROUTE_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```
