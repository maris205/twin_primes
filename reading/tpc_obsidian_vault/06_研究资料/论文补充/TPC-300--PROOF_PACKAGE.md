---
type: "source-reading"
source_path: "papers/tpc-300-native-budget-dual-certificate/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-300"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-300-native-budget-dual-certificate/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-300|TPC-300]] · [[00_开始阅读|首页]]

# TPC-300 proof package

## Theorem 1 — weak native-budget dual

Let M be positive definite, let V and b be finite real data, let R\>=0, and let rho\>0. Define c\_rho by

```text
(V^T V+rho M)c_rho=V^T b
```

and

```text
D_rho=(||b||^2-R^2-b^T Vc_rho)/rho.
```

Then D\_rho \<= B\_R(b), where B\_R(b)=min{c\^T M c:\|\|Vc-b\|\|\<=R} whenever the feasible set is nonempty.

### Proof

Put mu=1/rho. The matrix in the quadratic Lagrangian

```text
L(c,mu)=c^T M c+mu(||Vc-b||^2-R^2)
```

is positive definite, and its unique minimizer is c\_rho. Multiplying the normal equation by c\_rho\^T gives

```text
inf_c L(c,mu)=(||b||^2-R^2-b^T Vc_rho)/rho=D_rho.
```

For every primal-feasible c, L(c,mu)\<=c\^T M c; taking the infimum on the left and then the minimum on the right proves the claim.

## Theorem 2 — strong duality at the active frontier

If dist(b,range(V))\<R\<\|\|b\|\|, there is a unique rho\_*\>0 such that \|\|Vc\_rho\_*-b\|\|=R, and

```text
D_rho_*=B_R(b)=c_rho_*^T M c_rho_*.
```

### Proof

Whiten with y=M\^(1/2)c and W=VM\^(-1/2). In singular coordinates, the residual is

```text
||b_perp||^2+sum_j (rho/(sigma_j^2+rho))^2 a_j^2.
```

It is continuous, starts at the least-squares residual, and tends to \|\|b\|\|\^2; strict increase holds when the target has a visible component. The intermediate value theorem gives the unique rho\_*. At this point the constraint is active and mu=1/rho\_* satisfies the KKT conditions. The convex Slater condition gives equality of primal and dual values.

## Theorem 3 — reciprocal convention

If mu is the KKT multiplier of the squared residual constraint, then rho=1/mu. Thus a path written as

```text
(V^T V+rho M)c=V^T b
```

uses a ridge parameter, not the KKT multiplier itself. This follows directly from stationarity

```text
M c+mu V^T(Vc-b)=0.
```

## Theorem 4 — exact rational certificate compiler

If M,V,b,R\^2,rho are rational and rho\>0, then c\_rho and D\_rho are rational. Exact Gaussian elimination over Q computes both, and the identity in Theorem 1 is an exact arithmetic lower-bound certificate.

## Scope

The finite atlas uses R^2=(1/2)^2\|S\|, literal source profiles, and the frozen TPC-299 physical shell. It is not an asymptotic theorem.
