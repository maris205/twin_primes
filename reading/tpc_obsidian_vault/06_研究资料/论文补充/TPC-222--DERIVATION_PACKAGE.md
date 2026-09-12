---
type: "source-reading"
source_path: "papers/tpc-222-four-packet-cross-term-obstruction/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-222"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-222-four-packet-cross-term-obstruction/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-222|TPC-222]] · [[00_开始阅读|首页]]

# TPC-222 derivation package

Use the convention `⟨x,y⟩=sum_i conjugate(x_i)y_i`. For packet vectors `V_j`, define `G_(j,l)=⟨V_j,V_l⟩`. Then `G` is PSD and

```text
||sum_j c_j V_j||^2 = c^* G c.
```

For any two vectors, expansion of `||x+i^r y||^2` and the four roots of unity gives

```text
⟨x,y⟩ = 1/4 sum_(r=0)^3 i^(-r) ||x+i^r y||^2.
```

The trace bound follows from `G` being PSD: `lambda_max(G)<=tr(G)`, hence `c^*Gc<=tr(G)||c||^2`.

For the exact obstruction, let `u=(1,0)`, `s^+=(1,1,1,1)`, and `s^-=(1,-1,1,-1)`. Set `V_j^+=s_j^+u` and `V_j^-=s_j^-u`. Both Gram matrices have diagonal `(1,1,1,1)` and trace `4`, but for `c=(1,1,1,1)` the plus energy is `16` and the minus energy is `0`. Thus trace and individual packet norms do not identify the signed cross-term. The polarization residuals are nevertheless exactly zero: they recover the off-diagonal inner products only when the four phase-weighted energies are retained.
