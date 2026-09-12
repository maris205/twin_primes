---
type: "source-reading"
source_path: "papers/tpc-272-correlation-margin-budget-compiler/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-272"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-272-correlation-margin-budget-compiler/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-272|TPC-272]] · [[00_开始阅读|首页]]

# TPC-272 — Correlation-margin to endpoint-budget compiler

**Author:** Liang Wang, School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

TPC-272 proves the conditional budget `|C_perp|` saving `sigma_c` plus a source-level correlation margin `m=|C_perp|/R >= x^(-eta)` yields endpoint saving `sigma_c-eta`, so the strict TPC target requires `sigma_c-eta>1/400`; a two-dimensional exact converse shows phase sign alone cannot supply that margin.

## What is new

-   exact finite identity `m^6=Xi_C/Xi`, avoiding square roots in certification;
-   a sharp conditional endpoint compiler for the `E0=5/3` to `E*=1997/1200` budget;
-   an exact negative-phase witness with arbitrary `0<m<=1`;
-   nine rational finite margin records and four dyadic audits inherited from the locked TPC-271 physical interface;
-   independent replay and hostile mutation rejection.

The strongest finite diagnostic is the `96->192` pair: its sixth-power margin ratio is below `(1/32)^6` although both phase labels stay on the negative real axis. This is a finite stability audit, not an asymptotic counterexample.

## Claim ceiling

```text
PROVED_CONDITIONAL = scalar saving + margin lower bound -> endpoint saving
PROVED_EXACT = two-dimensional sign-only converse and finite identities
NUMERICALLY_CERTIFIED = nine margin rows and four dyadic ratios
OPEN = source-level margin bound, arithmetic L2, full Gate B
FIXED_POWER_CREDIT = 0
TWIN_PRIME_RESULT = NONE
```

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc272_correlation_margin_budget_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc272_independent_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc272_margin_stress.py --check
```

The final manuscript is [paper/paper.pdf](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-272-correlation-margin-budget-compiler/paper/paper.pdf). The local Session-named `propose.md` and route evaluator files were absent, so the proof/checker/theorem-ledger fallback is recorded explicitly in the route evaluation.
