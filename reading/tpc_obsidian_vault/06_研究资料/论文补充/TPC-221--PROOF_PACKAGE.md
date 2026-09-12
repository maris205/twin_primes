---
type: "source-reading"
source_path: "papers/tpc-221-collision-graph-schur-envelope/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-221"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-221-collision-graph-schur-envelope/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-221|TPC-221]] · [[00_开始阅读|首页]]

# TPC-221 proof package

## Theorem 1: PSD and exact energy identity

For `B_q in C^A`, define `Gamma(q,q')=<B_q,B_q'>`. Then `Gamma` is positive semidefinite and, for every finite complex vector `lambda`,

```text
sum_a |sum_q lambda_q B_q(a)|^2 = lambda^* Gamma lambda.
```

## Theorem 2: weighted Schur envelope

For any positive weights `p_q`,

```text
lambda^* Gamma lambda
 <= max_q [p_q^(-1) sum_q' |Gamma(q,q')| p_q'] ||lambda||_2^2.
```

In particular the unweighted row-sum bound uses `p_q=1`.

## Theorem 3: literal saturation

For `h=5`, `H=500`, constant profile, and `Q={101,151,181,191}`, every literal row is `e_1+e_4`. Hence `Gamma=2 J_4`, the Schur envelope is `8`, and the equal-weight Rayleigh quotient is `8`. The diagonal total is `8`, so the coherent-to-diagonal ratio is `4=P`.

All three statements are proved symbolically in the proof record and checked by exact integer/rational certificates. The saturation statement is explicitly finite and scoped.
