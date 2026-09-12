---
type: "source-reading"
source_path: "papers/tpc-279-coherence-to-gain-theorem/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-279"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-279-coherence-to-gain-theorem/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-279|TPC-279]] · [[00_开始阅读|首页]]

# TPC-279 derivation package

Let `V_0,...,V_3` be four vectors, with

```text
D = sum_j ||V_j||^2 > 0
G = ||sum_j V_j||^2
E = sum_{j<k} Re <V_j,V_k>
q = G/D
r = D/G (when G>0)
Delta = 1-q = -2E/D
```

Expansion and Cauchy give `0<=q<=4` and `r=(1-Delta)^(-1)`. Therefore, for `b>0`, `gamma>=0`, and `X>=1`,

```text
r >= b X^gamma
<=> q <= b^(-1) X^(-gamma)
<=> Delta >= 1-b^(-1) X^(-gamma).
```

For `mu=max |<V_j,V_k>|/(||V_j||||V_k||)`, putting `a_j=||V_j||` gives

```text
G/D <= 1 + mu*((sum_j a_j)^2-D)/D <= 1+3mu,
G/D <= min(4,1+3mu),
r >= max(1/4,1/(1+3mu)).
```

The equicorrelation Gram matrix `(1-mu)I+mu 11*` attains equality for every `mu` in `[0,1]`. Orthogonal unit packets give `r=1`; aligned packets give `r=1/4`. The scalar family `(1,1,1,-(3-epsilon))` gives `D=3+(3-epsilon)^2`, `G=epsilon^2`, and unbounded `r` as epsilon tends to zero while `mu=1`.

The parent TPC-278 gain intervals are inverted exactly. Their independently stored cancellation intervals overlap the reciprocal-derived deficit intervals; the intersection is retained. The transfer has 8 positive and 4 negative deficit rows, matching the parent cross-sign census.
