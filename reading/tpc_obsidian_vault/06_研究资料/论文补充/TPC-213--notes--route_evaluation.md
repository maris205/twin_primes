---
type: "source-reading"
source_path: "papers/tpc-213-physical-profile-cross-gram/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-213"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-213-physical-profile-cross-gram/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-213|TPC-213]] · [[00_开始阅读|首页]]

# Route Evaluation

## Route A

```text
A0 = NOT_APPLICABLE
A1 = NOT_APPLICABLE
A2 = NOT_APPLICABLE
A3 = NOT_APPLICABLE
A4 = NOT_APPLICABLE
```

This remains the analytic prime/twin-prime Route-B session, not the dynamical spectral Route-A family.

## Route B

```text
STRUCTURAL_THRESHOLD_A = PASS
PHYSICAL_PROFILE_EMITTER_PULLBACK = PROVED_EXACT
RESIDUE_LIFT_GCD_ALIASING = PROVED_EXACT
CROSS_DIVISOR_FREQUENCY_GRAM = PROVED_EXACT_FINITE
PHYSICAL_DIRECT_SUM_REPLACEMENT = REFUTED_SCOPED
LITERAL_V46_ASYMPTOTIC_GRAM_BOUND = OPEN
PRIME_SHELL_REASSEMBLY = OPEN
FULL_GATE_B = OPEN
STRICT_1_OVER_400 = UNPAID
ARITHMETIC_ADVANCE = NO
L2 = NONE
FIXED_ATOM_CREDIT = 0
```

## Strongest positive result

The literal residual can be pulled back to one common physical support before any outer absolute value, and its cross-divisor Gram is exactly a frequency intersection sum. The residue-lift cross blocks are governed by gcd/lcm compatibility rather than orthogonality.

## Strongest obstruction

The cross-divisor terms are not automatically a saving: the exact unit-weight fixture has positive off-diagonal Gram values `560` and `770`. Therefore a future estimate must exploit the actual smooth weights, signs, and profile structure; it cannot infer cancellation from coupling alone.

## Open theorem

Prove a fixed-power bound for the literal joint pullback kernel in the V46 transition window, retaining `psi`, `mu(d) log(d)/d`, four-packet signs, the zero-axis, and the prime shell.

## Reusable structure

```text
common physical support
  -> residue lift C_d
  -> additive transform
  -> reciprocal emitter pullback K_d
  -> common-source collapse K=sum_d K_d
  -> gcd/lcm lift aliasing and frequency-intersection Gram
  -> literal joint Gram theorem required
```

## ROUND2\_CLUE

Use the frequency-intersection formula to group nested divisor pairs by a shared rational frequency before any `d`- or `q`-triangle. Test whether the `mu(d) log(d)` signs and the V46 smooth `psi` produce a signed cancellation on these shared-frequency clusters; if not, record the resulting positive-Gram obstruction and pivot to prime-only reassembly.
