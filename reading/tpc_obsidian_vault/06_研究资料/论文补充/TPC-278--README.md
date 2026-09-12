---
type: "source-reading"
source_path: "papers/tpc-278-cross-scale-gain-stability/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-278"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-278-cross-scale-gain-stability/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-278|TPC-278]] · [[00_开始阅读|首页]]

# TPC-278 — Cross-scale signed-gain stability and a shell/clock counterexample

**Author:** Liang Wang, School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

On the same literal source and four-packet projection used by TPC-277, changing only the declared prime-shell endpoint `Q` or the clock `H` flips the sign of the net packet cross term in four of twelve exact finite rows. For example, at `N=192,s=2`, the natural `Q=6` row has `D/G≈1.006248`, while `Q=7` has `D/G≈0.866928`. Thus the finite statement `D/G>=1` is not stable under this declared interface perturbation.

This is a finite stability obstruction, not an asymptotic counterexample: the source-level Q/H schedule needed by the twin-prime route remains open.

## Claim ceiling

```text
NUMERICALLY_CERTIFIED_FINITE = 12 exact source rows and 4 sign flips
REFUTED_SCOPED = finite r>=1 stability under declared Q/H perturbations
OPEN = source-level uniform shell/clock stability and coherence theorem
FIXED_POWER_CREDIT = 0
ARITHMETIC_ADVANCE = NO
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc278_cross_scale_gain_stability_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc278_independent_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc278_stability_stress.py
```

The manuscript is [paper/paper.pdf](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-278-cross-scale-gain-stability/paper/paper.pdf). TPC-277 is locked by code and result hashes; no synthetic packet or floating-point classification is used.
