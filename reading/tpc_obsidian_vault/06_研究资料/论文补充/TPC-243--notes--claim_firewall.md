---
type: "source-reading"
source_path: "papers/tpc-243-hard-window-near-isometry-bilinear-transfer/notes/claim_firewall.md"
snapshot_date: "2026-09-12"
owner: "TPC-243"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-243-hard-window-near-isometry-bilinear-transfer/notes/claim_firewall.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-243|TPC-243]] · [[00_开始阅读|首页]]

# Claim firewall

## Proved statements

-   The hard rectangular Gram row bound with `R_delta=delta^(-1) H_floor(1/(2delta))`.
-   The two-sided normalized frame estimate.
-   The signed bilinear estimate with its exact orientation.
-   Primitive reduced rational spacing at `U^(-2)`.
-   The V59 coefficient `133/100` and exponent `-67/200`.
-   The abstract TPC-242 selected-mode transfer `N^(-1)<Tw,Tz> -> <w,z>`.

## Required interpretation

`SIGNED BILINEAR TRANSFER` means that a bilinear coefficient-space quantity is approximated by its hard-window synthesis counterpart. It does not mean that the quantity is small, nonzero, positive, negative, or arithmetically cancelled.

## Forbidden promotions

The following remain false, absent, or open:

```text
COEFFICIENT_NORM_BOUND = NONE
LITERAL_TOP_PRIME_ATTACHMENT = OPEN
SIGNED_C_H_THEOREM = NONE
ARITHMETIC_L2 = NONE
FIXED_ATOM_CREDIT = 0
STRICT_1_OVER_400 = UNPAID_GLOBAL
FULL_GATE_B = OPEN
TWIN_PRIME_RESULT = NONE
```

TPC-217’s standard upper large-sieve scale must not be described as a new TPC-243 upper theorem. TPC-238’s triangular result must not be described as incorrect; the present theorem has a different direct rectangular mechanism and a different error regime.

## Finite-computation boundary

Every executable fixture and enumeration is `NUMERICAL_FINITE_ILLUSTRATION_ONLY`. Exact rational arithmetic prevents rounding ambiguity, but exactness of a finite computation is not evidence for an asymptotic theorem. The proof package is the theorem evidence.
