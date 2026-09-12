---
type: "source-reading"
source_path: "papers/tpc-349-prime-balanced-signed-defect-witness/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-349"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-349-prime-balanced-signed-defect-witness/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-349|TPC-349]] · [[00_开始阅读|首页]]

# TPC-349 — Prime-balanced signed incidence witnesses for a literal mask defect

**Author:** Liang Wang **Affiliation:** School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

TPC-349 turns the TPC-348 coordinate defect witness into a deterministic zero-sum prime-incidence contrast. For the ordered shell, equal positive and negative prime coefficients (with one neutral middle prime when necessary) give an exact prime-incidence Gram expansion and the finite lower bound

```text
||D_I||_(2->2) >= ||D_I b_I||_2 / ||b_I||_2.
```

On the locked 192-row panel, every signed vector is nonzero and has positive response; it beats the best mask-hit coordinate baseline on `136/192` rows and reaches at least half the defect spectral norm on `175/192` rows. The finite response/defect range is `0.39083565842--0.954375010719`. The remaining 56 rows refute any universal balanced-gain claim even on this panel.

This is a finite structural certificate, not a growing lower bound. It gives no source-uniform arithmetic `L2`, no uniform masked-operator bound, no fixed-power credit, and no twin-prime conclusion.

## Main contributions

-   An exact zero-sum prime split and an incidence-vector definition that retains multiply-divisible positions.
-   An exact cross-prime Gram expansion for the defect image.
-   A normalized induced-norm lower-witness theorem independent of eigenvectors.
-   A 192-row producer/reverse-shell replay, an exact multi-hit rational anchor, and six hostile mutation tests.
-   A scoped obstruction: the signed witness is often stronger than the coordinate baseline but not uniformly so.

## Claim firewall

```text
SIGNED_INCIDENCE_LOWER_WITNESS = PROVED_EXACT_FINITE_LINEAR_ALGEBRA
PRIME_BALANCE_AND_GRAM = PROVED_EXACT_FINITE_DECLARED_MODEL
FINITE_SIGNED_AUDIT = NUMERICALLY_CERTIFIED_FINITE_192_ROWS
UNIVERSAL_BALANCED_GAIN = REFUTED_SCOPED
ARITHMETIC_ADVANCE = NO
FIXED_POWER_CREDIT = 0
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

The Session-named official evaluator files are absent in this checkout; `notes/route_evaluation.md` records the local fail-closed assessment.

## Reproduction

From the repository root:

```bash
export PYTHONDONTWRITEBYTECODE=1
python -B papers/tpc-349-prime-balanced-signed-defect-witness/code/tpc349_prime_balanced_signed_defect_witness.py --write
python -B papers/tpc-349-prime-balanced-signed-defect-witness/code/tpc349_prime_balanced_signed_defect_witness.py --check
python -O -B papers/tpc-349-prime-balanced-signed-defect-witness/code/tpc349_prime_balanced_signed_defect_witness.py --check
python -B papers/tpc-349-prime-balanced-signed-defect-witness/experiments/tpc349_independent_checker.py --check
python -O -B papers/tpc-349-prime-balanced-signed-defect-witness/experiments/tpc349_independent_checker.py --check
python -B papers/tpc-349-prime-balanced-signed-defect-witness/experiments/tpc349_signed_witness_stress.py
python -O -B papers/tpc-349-prime-balanced-signed-defect-witness/experiments/tpc349_signed_witness_stress.py
python -B research/tpc-big-road/tpc_bridge_b_tpc349_prime_balanced_signed_defect_witness_checker.py --check
```

The canonical result is [results/tpc349\_certificate.json](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-349-prime-balanced-signed-defect-witness/results/tpc349_certificate.json.txt), and the compiled manuscript is [paper/paper.pdf](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-349-prime-balanced-signed-defect-witness/paper/paper.pdf).

## Package contents

`PAPER_PLAN.md`, `DERIVATION_PACKAGE.md`, `PROOF_PACKAGE.md`, `notes/`, `code/`, `experiments/`, `results/`, and `paper/` form the auditable project package. The next route question is whether this signed incidence Gram survives fresh growing panels.
