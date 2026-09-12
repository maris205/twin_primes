---
type: "source-reading"
source_path: "papers/tpc-221-collision-graph-schur-envelope/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-221"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-221-collision-graph-schur-envelope/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-221|TPC-221]] · [[00_开始阅读|首页]]

# TPC-221 derivation package

Let `B_q` be the vector of a fixed packet coordinate on primitive residues modulo `h` and let `Gamma(q,q')=<B_q,B_q'>`. For a finite weight vector `lambda`, expansion gives

```text
E(lambda)=sum_a |sum_q lambda_q B_q(a)|^2
         = sum_(q,q') lambda_q conjugate(lambda_q') Gamma(q,q').
```

The matrix `Gamma` is `A A^*`, hence Hermitian positive semidefinite. The elementary inequality `2|u v| <= t|u|^2+t^(-1)|v|^2` applied to the quadratic form gives, for every positive vector `p`,

```text
E(lambda) <= [max_q p_q^(-1) sum_q' |Gamma(q,q')| p_q'] ||lambda||_2^2.
```

Taking `p=1` is the usual Schur envelope. The collision formula from TPC-220 supplies the literal arithmetic entries:

```text
Gamma(q,q') = sum_(m,m') w_(m,q) conjugate(w_(m',q'))
                 1_(m q'=m' q mod h).
```

For the saturation fixture, `h=5`, `H=500`, `q=101,151,181,191`, and constant profile, the cutoff is one for every q. Since every q is `1 mod 5`, each row has exactly the two primitive coordinates `a=1,4`, so `B_q=e_1+e_4`. Therefore `Gamma=2 J_4`, its maximum row sum is `8`, its top eigenvalue is `8`, and equal weights have energy `32` while the diagonal total is `8`; the ratio is exactly `P=4`.

This is a finite literal obstruction to obtaining a sub-`P` theorem from absolute row sums alone. It does not assert that the same alignment persists at growing prime scale.
