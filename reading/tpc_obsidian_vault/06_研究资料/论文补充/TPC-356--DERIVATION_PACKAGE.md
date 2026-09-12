---
type: "source-reading"
source_path: "papers/tpc-356-geometry-adversarial-normalization-holdout/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-356"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-356-geometry-adversarial-normalization-holdout/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-356|TPC-356]] · [[00_开始阅读|首页]]

# TPC-356 derivation package

Let $I=[x,x+N-1]\cap\mathbb Z$, let $S_Q$ be the primes in $(Q,2Q]$, and write

$$ B_p(u,t)=p\,\frac{H^{2s}}{(H^2+(u-t)^2)^s}  \left(\mathbf 1_{p\mid u-t}-\frac1{p-1}\right)  \mathbf 1_{u\ne t}\mathbf 1_{p\nmid u}\mathbf 1_{p\nmid t}. $$

The unsigned geometry energy is

$$  G_u=\sum_{p\in S_Q}\sum_{t\in I}B_p(u,t)^2. $$

TPC-355 defines $D_G=\operatorname{diag}(G_u)$ and $A^\#=D_G^{-1/2}AD_G^{-1/2}$ whenever the finite diagonal is positive. TPC-356 does not alter this operator. It changes only the origin-selection protocol, selecting origins from unsigned pilot geometry before any source response is evaluated.

For the finite source residual $\beta=\Lambda-b$, either $T=A$ or $T=A^\#$ satisfies the exact expansion

$$  \|T\beta\|_2^2=\|T\Lambda\|_2^2+\|Tb\|_2^2  -2\langle T\Lambda,Tb\rangle. $$

The reported coefficient is $\kappa(T)=2\langle T\Lambda,Tb\rangle/ (\|T\Lambda\|_2^2+\|Tb\|_2^2)$. All remaining statements are finite computations under the inherited V59 source model.
