---
type: "source-reading"
source_path: "papers/tpc-266-end-to-end-claim-firewall/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-266"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-266-end-to-end-claim-firewall/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-266|TPC-266]] · [[00_开始阅读|首页]]

# TPC-266 derivation package

All powers below use the common clock inherited from TPC-261–265:

```text
E0 = 5/3,
E* = 1997/1200,
Delta* = E0-E* = 1/400.
```

## 1. Typed lane interface

For a lane with baseline exponent `E0`, saving `delta`, and reassembly loss `lambda`, define its effective saving by

```text
sigma = delta-lambda.
```

The admissible evidence types are:

```text
FIXED_LOG      x^E0/(log x)^M       -- no fixed-power credit
POWER          x^(E0-delta+lambda+epsilon)
SIGNED_PHASE   a signed endpoint bound of the same power form
MISSING        no bound for the lane
DELETED        the lane was removed from the expression
```

Only `POWER` and `SIGNED_PHASE` with `sigma>Delta*` can pay a lane. This is a type rule, not a heuristic interpretation of a numerical slope.

## 2. Composition

TPC-263 contributes a source-backed `FIXED_LOG` center channel `C_3`. TPC-264 contributes a residual Schur set `|z|<=R` (or its dimension-one circle), not a power estimate for `R`. TPC-265 contributes the exact support rule

```text
sup |c+z| = |c|+R.
```

Therefore the legal composite endpoint has two lanes, `center` and `radius`. The compiler may return `CLOSED_CONDITIONAL` only when both lanes are paid and the residual is retained.

## 3. Hostile test matrix

The certificate uses exact rational fixtures for six states:

```text
strict pair       -> CLOSED_CONDITIONAL
fixed-log center  -> OPEN_LOG_CENTER
missing radius    -> OPEN_RADIUS
borderline lane   -> BORDERLINE
subcritical lane  -> INSUFFICIENT
deleted residual  -> UNSOUND_RESIDUAL_DELETION
```

The last state is especially important: deleting `z` reports only `c`, while the Schur set still permits the aligned endpoint `c+z`.
