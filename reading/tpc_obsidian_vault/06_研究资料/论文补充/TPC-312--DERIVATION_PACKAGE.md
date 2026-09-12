---
type: "source-reading"
source_path: "papers/tpc-312-new-source-shell-separation-atlas/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-312"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-312-new-source-shell-separation-atlas/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-312|TPC-312]] · [[00_开始阅读|首页]]

# TPC-312 derivation package

Let `I={321,...,640}` and let `U=7` be the finite divisor cutoff selected by the locked source rule at scale 640. The literal source coefficient is

$$  \beta_t=\frac{1_{t=p^a}}{a}-\sum_{d\mid t,\ d\le U}\mu(d). $$

For a shell prime `p`, height `H=66`, and exponent `s` in `{1,2}`, define

$$  g_p(u)=\sum_{\substack{t\in I, t\ne u\\p\nmid ut}}  p\,\frac{H^{2s}}{(H^2+(u-t)^2)^s}  \left(1_{u\equiv t\pmod p}-\frac1{p-1}\right)\beta_t. $$

The new rows use `S_Q={p prime: Q<p<=2Q}` for `Q=24,36,54,80`. Their physical Gram matrix is

$$  G_{p,q}=\sum_{u\in I}g_p(u)g_q(u). $$

For a sign vector `c` define `E(c)=c^T Gc` and normalize by `tr(G)`. The producer fixes the first sign to `+1`, which quotients the global sign action because `E(-c)=E(c)`. It then traverses the remaining coordinates in reflected Gray order.

Every displayed ratio is a decimal rendering of an exact rational quotient. The certificate stores SHA-256 digests of the reduced minimum and maximum ratios; the independent checker recomputes those quotients directly.

The finite comparison statements are the strict inequalities

$$  r^-_{24,s}>r^-_{36,s}>r^-_{54,s}>r^-_{80,s},\qquad  r^+_{24,s}<r^+_{36,s}<r^+_{54,s}<r^+_{80,s}, $$

for each `s=1,2`, together with `r^-_{Q,2}<r^-_{Q,1}` and `r^+_{Q,2}>r^+_{Q,1}` for every declared `Q`.
