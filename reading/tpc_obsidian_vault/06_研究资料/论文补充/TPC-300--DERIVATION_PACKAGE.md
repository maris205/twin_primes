---
type: "source-reading"
source_path: "papers/tpc-300-native-budget-dual-certificate/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-300"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-300-native-budget-dual-certificate/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-300|TPC-300]] · [[00_开始阅读|首页]]

# TPC-300 derivation package

Let M be positive definite, V be the finite physical image map, b be the target, and R be the allowed Euclidean residual radius. The primal frontier is

```text
B_R(b)=min{c^T M c: ||Vc-b||_2 <= R}.
```

For a positive ridge parameter rho, let

```text
(V^T V+rho M)c_rho=V^T b.
```

The Lagrangian multiplier is mu=1/rho. Completing the square in

```text
c^T M c + mu(||Vc-b||_2^2-R^2)
```

gives the dual value

```text
D_rho=(||b||_2^2-R^2-b^T V c_rho)/rho.
```

For every rho\>0, weak duality gives D\_rho\<=B\_R(b). If the least-squares distance is strictly below R\<\|\|b\|\|, the residual along the ridge path is continuous and strictly increasing in rho; the unique rho\_\* with \|\|Vc\_rho-b\|\|\_2=R attains equality.

For the TPC profile map, V=A\^T U and M=U\^T U. All entries are rational on the finite fixture. Choosing rational rho therefore makes c\_rho and D\_rho rational. The certificate stores hashes of the exact fraction and exact coefficient vector, while decimal intervals are only presentation enclosures.
