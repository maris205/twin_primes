---
type: "source-reading"
source_path: "papers/tpc-283-source-attachment-stability-radius/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-283"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-283-source-attachment-stability-radius/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-283|TPC-283]] · [[00_开始阅读|首页]]

# TPC-283 derivation package

For `S != 0`, let `L_S(u)=<u,S>` and `H_S=ker(L_S)`. If `C=<w,S>`, `W=||w||^2`, and `Y=||S||^2`, orthogonal projection onto the line spanned by `S` gives

```text
w_* = w - (C/Y) S,
<w_*,S>=0,
||w-w_*||^2=C^2/Y.
```

Every `u` in `H_S` satisfies `w-u=(w-w_*)+(w_*-u)` with orthogonal summands, so `w_*` is the unique closest point in `H_S`. Dividing by `W` yields the relative squared radius `C^2/(WY)`. The TPC-282 interval for this quantity is therefore also an interval for the zeroing radius squared.
