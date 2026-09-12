---
type: "source-reading"
source_path: "papers/tpc-401-c1-diagonal-deletion-decomposition/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-401"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-401-c1-diagonal-deletion-decomposition/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-401|TPC-401]] · [[00_开始阅读|首页]]

# TPC-401 derivation package

Let `I_o={o,...,o+N-1}`, `T_uv=H^2/(H^2+(u-v)^2)`, and `D_p=diag(1_{p not divide u})`. For `u != v`, if `N<Q<p`, then `1 <= |u-v| <= N-1 < p`, so `1_{p|(u-v)}=0`. With `a_p=p(p/Q)^2/(p-1)`, the literal component is therefore `K_p(u,v)=-a_p T_uv D_p(u)D_p(v)` off diagonal and is zero on the diagonal. Since `T_uu=1` and `D_p^2=D_p`, this gives the exact matrix identity

```text
K_p = -a_p (D_p T D_p - D_p).
```

If `r_p(o)` is the unique multiple of `p` in the interval when it exists and `S_o(u)=sum_{v != u} T_uv^2`, then the geometry is exactly

```text
G_o(u) = sum_{p not divide u} a_p^2
         (S_o(u)-1_{r_p(o) exists} T_{u,r_p(o)}^2).
```

The condition is production-domain specific. At the anchor `N=13,Q=8`, the pair `(u,v)=(0,11)` and `p=11` violates it, so the anchor is retained as an explicit boundary counterexample. The sign laws in earlier panels remain modeling choices and are not upgraded by this identity.
