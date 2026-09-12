---
type: "source-reading"
source_path: "papers/tpc-344-panel-contrast-nuisance-basis/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-344"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-344-panel-contrast-nuisance-basis/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-344|TPC-344]] · [[00_开始阅读|首页]]

# TPC-344 route evaluation

The Session-named `propose.md`, `skills/route-a-evaluator.md`, and `skills/route-b-evaluator.md` files are absent from this checkout. This note therefore records the available fail-closed local evaluation only; it must not be called an official Route-A or Route-B pass.

```text
ROUTE_A = OPEN
ROUTE_B = FINITE_CERTIFICATE_ONLY
TPC344_FINITE_RESULT = NUMERICALLY_CERTIFIED_FINITE_PANEL_CONTRAST_BASIS_AUDIT
TPC344_EXACT_STRUCTURE = PROVED_EXACT_FINITE_DECLARED_MODEL
TPC344_RAW_GUARD = PASS_SCOPED
TPC344_EQUAL_ROW_GUARD = REFUTED_SCOPED
TPC344_CROSSFIT_TRANSFER = REFUTED_SCOPED
TPC344_ARITHMETIC_ADVANCE = NO
TPC344_FIXED_POWER_CREDIT = 0
TPC344_FULL_GATE_B = OPEN
TPC344_TWIN_PRIME_RESULT = NONE
```

Strongest positive: a predeclared panel contrast crosses the raw pooled threshold and is exactly equivalent to panel-adaptive shared coefficients.

Strongest obstruction: the threshold crossing disappears under equal-row weighting, and no low-residual cross-panel prediction transfers.

Open theorem: identify a canonical, source-uniform nuisance or response structure that survives weighting and pays the arithmetic Route-B loss ledger.

Reusable structure:

```text
shared span -> signed panel contrast -> panel-adaptive reparameterization
            -> weighting sensitivity -> cross-fit transfer audit
```

`ROUND2_CLUE = PRINCIPAL_ANGLE_GRASSMANN_STABILITY_AUDIT`.
