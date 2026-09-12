---
type: "source-reading"
source_path: "papers/tpc-398-c1-interpolation-endpoint-microgrid/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-398"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-398-c1-interpolation-endpoint-microgrid/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-398|TPC-398]] · [[00_开始阅读|首页]]

# TPC-398 derivation package

For a prime p in (Q,2Q\], with Q=8192, H=66, and exponent one, define the finite component

```text
 K_p(u,v) = p (p/Q)^2 H^2/(H^2+(u-v)^2)
            (1_{p | u-v} - 1/(p-1))
            1_{u != v} 1_{p not|u} 1_{p not|v}.
```

Let

```text
 G(u) = sum_{p in (Q,2Q]} sum_v K_p(u,v)^2.
```

The two finite endpoint matrices are

```text
 M_all_plus          = sum_p K_p
 M_alternating_index = sum_p (-1)^index(p) K_p
```

where index(p) is the ascending index in the prime shell. TPC-398 forms the exact finite combinations with coefficients 7/8, 15/16, 31/32, and 1:

```text
 M_lambda = (1-lambda) M_all_plus + lambda M_alternating_index
```

This is an exact linear-algebra identity. At the 13-point rational anchor it is checked with Fraction arithmetic; it is not a claim that a fractional coefficient is an arithmetic character or a new sign law.

For each origin, divide the 1024 coordinates into eight blocks of length 128 and retain block pairs whose block-index difference is at most three. The local normalization uses M(u,v)/sqrt(G(u)G(v)). The other normalizations divide the masked base metrics by, respectively, the pooled calibration mean, the current-origin mean, or the first calibration-origin mean. Write S\_lambda(o) for the resulting spectral diagnostic. The origin spread is

```text
 (max_o S_lambda(o) - min_o S_lambda(o)) / mean_o S_lambda(o)
```

TPC-397 supplies two frozen scalar endpoints: its all-origin means for blend\_3\_4 and blend\_1. For a current coefficient define

```text
 t = (lambda - 3/4)/(1/4)
 B_lambda = (1-t) B_3/4 + t B_1
```

The parent-relative calibration and holdout errors are the corresponding new cohort means divided by B\_lambda, minus one. This scalar interpolation is a response-blind modeling baseline; it does not assert that spectral means are linear in the coefficient in the underlying arithmetic problem.

All six current origins use N=1024; the first three are calibration and the last three holdout. Every statement in this package is finite and scoped to the declared proxy.
