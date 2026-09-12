---
type: "source-reading"
source_path: "papers/tpc-301-budget-gap-robustness-audit/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-301"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-301-budget-gap-robustness-audit/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-301|TPC-301]] · [[00_开始阅读|首页]]

# TPC-301 - Budget-gap robustness audit

Author: Liang Wang, School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

TPC-301 attacks the finite obstruction left by TPC-300. It varies the relative target RMS tolerance over tau=1/4,1/2,3/4, evaluates weighted and all-positive targets in the same weighted-selected source prefix, and checks three source normalizations. The common-prefix weighted/positive budget gap is above 10 in all 18 rows at all three tolerances. Its minimum is

| relative RMS |  common-prefix minimum gap|  full-prefix minimum gap|
|--------------|--------------------------:|------------------------:|
| 1/4          |             155.1685273879|           155.1685273879|
| 1/2          |              69.9448236917|            47.3501392957|
| 3/4          |              39.2637006403|            27.7392664825|

The weighted common-prefix budget is above 3e-5 in all 54 row/tolerance cases under each of \|\|beta\|\|\^2, tr(M\_k)/k, and the first-profile norm normalizations. The three normalized gap values are algebraically identical at a common prefix; the numerical replay checks this in 54 cases.

## What is new

TPC-299 established a single tau=1/2 native budget obstruction with target-specific prefixes. TPC-300 transported it to exact finite dual witnesses. TPC-301 shows that the class separation survives a tolerance ladder and a common-prefix comparison, which removes the principal finite-dimensional normalization/prefix confounder.

The actual finite target census is 219 explicit shell targets across 18 rows. The inherited parent ledger also carries a 1,380-edge grid count; both are recorded separately so that the two notions are not conflated.

## Claim firewall

```text
PROVED_EXACT_FINITE = tolerance nesting, relative homogeneity,
threshold-prefix nesting, common-prefix normalization invariance
NUMERICALLY_CERTIFIED_FINITE = 324 frontier cases; 54 common gaps;
54/54 budget floors for each of three normalizations; 36 monotonicity checks
NUMERICAL_OBSERVATION = finite gap minima in the table above
MODELING_CHOICE = literal cutoff ladder, finite rows, target classes,
tolerance set, common-prefix protocol, source normalizers
OPEN = growing profile budget, arithmetic L2, fixed-power credit,
full Gate B, twin-prime theorem
```

## Reproduction

```text
export PYTHONDONTWRITEBYTECODE=1
python -B code/tpc301_budget_gap_robustness_audit.py --write
python -B code/tpc301_budget_gap_robustness_audit.py --check
python -B experiments/tpc301_independent_checker.py
python -B experiments/tpc301_stress.py
python -B research/tpc-big-road/tpc_bridge_b_tpc301_budget_gap_robustness_audit_checker.py --check
```

The manuscript is paper/paper.pdf. The Session-named Route-A/Route-B evaluator files are absent from this checkout; the local proof package, independent replay, stress suite, PDF audit, and Bridge-B checker are the available fail-closed validation path.
