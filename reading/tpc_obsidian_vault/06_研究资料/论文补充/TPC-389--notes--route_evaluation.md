---
type: "source-reading"
source_path: "papers/tpc-389-c1-long-horizon-slope-stress/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-389"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-389-c1-long-horizon-slope-stress/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-389|TPC-389]] · [[00_开始阅读|首页]]

# TPC-389 route evaluation

The Session files `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` are absent from this checkout. Applying the available fail-closed local authority:

```text
ROUTE_A = OPEN
ROUTE_B = OPEN
FINITE_CERTIFICATE = PASS (producer + independent replay + stress)
LONG_HORIZON_PARENT_TRANSFER = FINITE_SCOPED_PASS
RECURSIVE_COMPOSITION = FINITE_SCOPED_PASS
SPECTRAL_CAP = FINITE_OBSTRUCTION (64/256)
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
```

The local Bridge-B checker verifies provenance, certificate semantics, both replay modes, PDF identity, and the claim firewall. It is not an official Route-B evaluator and cannot close the missing arithmetic gates.
