---
type: "source-reading"
source_path: "papers/tpc-283-source-attachment-stability-radius/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-283"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-283-source-attachment-stability-radius/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-283|TPC-283]] · [[00_开始阅读|首页]]

# TPC-283 — Source-attachment stability radius and adversarial zeroing

**Author:** Liang Wang, School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

For a nonzero projected output `S` and source representative `w`, the exact relative distance from `w` to the zero-attachment hyperplane is `C^2/(||w||^2||S||^2)`. Applied to the TPC-282 literal rows, every attachment can be zeroed by an information-model perturbation smaller than `30%` of the source norm; six of twelve have a certified radius below `10%`.

## What advances

-   proves the minimum-norm zeroing perturbation `w_* = w-(C/||S||^2)S`;
-   identifies the squared relative radius with the normalized attachment coefficient already measured on the actual source;
-   transfers the result to all 12 TPC-282 rows with a hash-locked parent;
-   separates an unrestricted Hilbert-space adversary from physically admissible source perturbations.

## Claim ceiling

```text
PROVED_EXACT = Hilbert-space distance-to-zero-attachment formula
NUMERICALLY_CERTIFIED_FINITE = all 12 rows have positive radius and radius < 3/10
NUMERICALLY_CERTIFIED_FINITE = 6 rows have radius < 1/10
INFORMATION_MODEL_ONLY = zeroing adversary need not be a literal source
OPEN = admissible literal-source stability and arithmetic L2
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
```

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc283_source_attachment_stability_certificate.py --write
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc283_source_attachment_stability_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -O -B code/tpc283_source_attachment_stability_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc283_independent_checker.py
PYTHONDONTWRITEBYTECODE=1 python -O -B experiments/tpc283_independent_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc283_stability_stress.py
```

The manuscript is [paper/paper.pdf](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-283-source-attachment-stability-radius/paper/paper.pdf). The adversarial radius is a geometric obstruction and is not presented as a mutation of the physical prime source.
