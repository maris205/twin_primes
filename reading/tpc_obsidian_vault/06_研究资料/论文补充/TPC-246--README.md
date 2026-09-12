---
type: "source-reading"
source_path: "papers/tpc-246-weighted-covariance-disk-reassembly/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-246"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-246-weighted-covariance-disk-reassembly/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-246|TPC-246]] · [[00_开始阅读|首页]]

# TPC-246: Weighted Covariance-Disk Reassembly

This project closes the first exact aggregate geometry problem created by TPC-245. If the joint local feasible set is the full Cartesian product of disks `c_h+r_h Dbar`, then arbitrary complex weights `lambda_h` produce exactly

```text
sum_h lambda_h(c_h+r_h Dbar)
  = C+R Dbar,
C = sum_h lambda_h c_h,
R = sum_h |lambda_h|r_h.
```

This gives an exact cancellation criterion `|C|<=R`, exact minimum modulus `max(|C|-R,0)`, and a sharp phase sector when `R<|C|`.

For the TPC-244 common-multiplier geometry, `lambda_h=|M_h|^2`. After the TPC-243 hard-window error `E=epsilon||W||||B||` is paid, every selected covariance lies in `C_0+(R_0+E)Dbar`; hence

```text
|C_0| > R_0+E
```

is a rigorous conditional robust-nonvanishing criterion.

## Main progress

-   proves exact complex-weighted Minkowski reassembly, including all degenerate cases and an explicit inverse construction;
-   proves exact aggregate zero-feasibility, minimum-modulus, and phase geometry;
-   turns the TPC-245 local disks and TPC-244 weights into one exact coefficient disk under blockwise product realizability;
-   pays the TPC-243 hard-window leakage as an additive radius and obtains a strict nonvanishing margin;
-   proves that local moment/energy data are insufficient whenever the aggregate disk contains zero;
-   separates full disks from one-dimensional circles and Cartesian products from source-coupled families.

## Physical boundary

The aggregate coefficient theorem is unconditional in its stated abstract model. Its V59 interpretation is conditional: the committed source does not yet provide the literal two-lane primitive attachment, canonical local block directions, blockwise product realization of all local disks, or payable norms and moments. The hard-window conclusion is containment, not exact realization of every error phase.

## Artifacts

-   `PROOF_PACKAGE.md`: complete theorem, reverse construction, and exclusions;
-   `DERIVATION_PACKAGE.md`: derivation and source boundary;
-   `results/tpc246_certificate.json`: exact Gaussian-rational certificate;
-   `code/tpc246_weighted_disk_certificate.py`: producer/checker;
-   `experiments/tpc246_independent_checker.py`: independent strict checker;
-   `experiments/tpc246_weighted_disk_stress.py`: exact finite stress suite;
-   `paper/paper.pdf`: compiled manuscript.

## Reproduction

Run from this project directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc246_weighted_disk_certificate.py --write
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc246_weighted_disk_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -O -B code/tpc246_weighted_disk_certificate.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc246_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -O -B experiments/tpc246_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc246_weighted_disk_stress.py --check
PYTHONDONTWRITEBYTECODE=1 python -O -B experiments/tpc246_weighted_disk_stress.py --check
```

All finite calculations use exact Gaussian-rational arithmetic and are `NUMERICAL_FINITE_ILLUSTRATION_ONLY`; the theorem is proved symbolically.

## Maximum status

`PROVED_STRUCTURAL_L1_WEIGHTED_COVARIANCE_DISK_REASSEMBLY`.

`ARITHMETIC_ADVANCE = NO`. Arithmetic `L2`, fixed-atom credit, strict `1/400`, full Gate B, and every twin-prime conclusion remain open.
