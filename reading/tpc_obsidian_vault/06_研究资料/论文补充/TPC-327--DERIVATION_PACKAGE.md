---
type: "source-reading"
source_path: "papers/tpc-327-three-origin-scale-triangulation/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-327"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-327-three-origin-scale-triangulation/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-327|TPC-327]] · [[00_开始阅读|首页]]

# TPC-327 derivation package

## 1. Frozen finite operator

For

$$  I_N=[20001,20000+N/2]\cap\mathbb Z,  \qquad N\in\{320,640,1280,2560\}, $$

and a prime `p` in `(Q,2Q]`, retain the literal block

$$ B_{p,N}^{(s)}(u,t)=p\frac{66^{2s}}{(66^2+(u-t)^2)^s} \left({\bf1}_{p\mid u-t}-\frac1{p-1}\right) {\bf1}_{u\ne t}{\bf1}_{p\nmid u}{\bf1}_{p\nmid t}. $$

Set `G_0=sum_p B_p^*B_p` and `G_e=(sum_p e_pB_p)^*(sum_p e_pB_p)`. Only the source origin changes from the two released panels.

## 2. Three-origin observables

For each scale, let `T(o)` be the all-plus TV lower envelope and `E(o)` the all-plus energy upper envelope at origin `o`. The new certificate records

$$  \operatorname{range}_T(N)=\max_{o\in\{12001,16001,20001\}}T(o)                          -\min_oT(o), $$

with the analogous `range_E(N)`. The predeclared finite controls require `max_N range_T(N)<0.001` and `max_N range_E(N)<0.005`, while requiring both ranges to be nonzero so the test is not vacuous.

## 3. Exact finite typing and boundary

Each Gram is positive semidefinite and its trace-normalized spectrum is a probability vector when its trace is positive. These are finite algebraic facts; the numerical profile comparisons are separately certified. The three-origin range does not imply a source-uniform limit, an arithmetic `L2` estimate, or a twin-prime result.
