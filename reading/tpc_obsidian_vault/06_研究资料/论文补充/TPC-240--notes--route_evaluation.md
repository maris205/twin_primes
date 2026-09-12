---
type: "source-reading"
source_path: "papers/tpc-240-top-prime-direct-energy-floor/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-240"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-240-top-prime-direct-energy-floor/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-240|TPC-240]] · [[00_开始阅读|首页]]

# Route Evaluation

## Route level

`PROVED_STRUCTURAL_L1_OBSTRUCTION`

`ARITHMETIC_ADVANCE = NO`

## Strongest positive result

For every fixed literal common profile, the exact top-prime q-split unsigned direct energy has leading constant `1197*kappa_psi*log(2)/800` and scale `x^(1/96)`.

## Strongest obstruction

This direct factor is not `o(Q^2/H)`. A fixed-power saving at this stage is false, so the remaining improvement must use q-collision structure, signs, or the actual four-packet projection rather than a smaller q-split direct norm.

## Open theorem

Determine the actual top-prime q-collapsed collision energy and decide whether it supplies the additional `x^(1/96)` factor that would make the TPC-239 `x^(1/48)` upper exponent sharp. The signed `C_h` and four-packet questions remain downstream.

## Reusable structure

`fixed-q signed-interval injectivity -> endpoint-safe lattice Riemann sum -> factorized weighted PNT`

## ROUND2\_CLUE

`TEST_THE_TOP_PRIME_Q_COLLAPSED_COLLISION_EXCESS_OVER_THE_EXACT_DIRECT_FLOOR_BEFORE_CLAIMING_X_1_OVER_48_SHARPNESS`

## Gate firewall

```text
TPC240_STATUS = PROVED_SOURCE_LOCKED_FIXED_PROFILE_UNSIGNED_TOP_PRIME_DIRECT_ENERGY_FLOOR
route_level = PROVED_STRUCTURAL_L1_OBSTRUCTION
ARITHMETIC_ADVANCE = NO
L2 = NONE
FULL_GATE_B = OPEN
STRICT_1_OVER_400 = UNPAID_GLOBAL
```
