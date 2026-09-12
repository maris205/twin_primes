---
type: "source-reading"
source_path: "papers/tpc-336-masked-signed-gram-response/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-336"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-336-masked-signed-gram-response/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-336|TPC-336]] · [[00_开始阅读|首页]]

# TPC-336 derivation package

Let `beta=sum_C beta_C` be the disjoint TPC-335 mask decomposition and let `y_C=C beta_C`. Finite bilinearity gives

```text
||C beta||^2 = ||sum_C y_C||^2
             = sum_C ||y_C||^2 + 2 sum_{C<D}<y_C,y_D>.
```

For each mask define the response gain `G_C=||C beta_C||^2/||beta_C||^2` when the denominator is nonzero. The certificate also records the coordinate diagonal and `O=E-D` for every self response. The pairwise Gram entries are retained because component energies alone cannot determine the full response.

The fixed operator is the all-plus deleted-diagonal prime-shell matrix at `Q=54`, exponent `1`, height `66`. All conclusions are finite and tied to the declared source cutoff.
