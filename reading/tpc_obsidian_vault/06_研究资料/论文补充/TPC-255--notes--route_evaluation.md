---
type: "source-reading"
source_path: "papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/notes/route_evaluation.md"
snapshot_date: "2026-09-12"
owner: "TPC-255"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-255-exact-adjoint-diagonal-boundary-compiler/notes/route_evaluation.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-255|TPC-255]] · [[00_开始阅读|首页]]

# Route evaluation

Strongest positive result: the literal V59 adjoint Haar scalar is exactly one `B_Q`-weighted beta midpoint plus explicit input-unit, hard-window, and child-jump corrections; the complete-lattice centered alias is zero.

Strongest obstruction: complete-lattice Poisson removes only the centered alias. Deleting the physical diagonal returns at shell scale `B_Q`, and no TPC-255 input estimates that beta midpoint collectively with the two boundary lanes.

Open theorem: estimate the signed sum of all surviving lanes on the same V59 clock without triangulating the prime shell or either unit correction.

Reusable structure:

```text
literal adjoint test
-> complete unit-centered lattice
-> Poisson zero
-> deleted-diagonal return
-> outer hard-window leakage
-> inner child-jump leakage
-> one literal beta linear form
```

`ROUND2_CLUE`: attack the `B_Q`-weighted literal beta rank midpoint together with the two boundary corrections; do not count the complete-lattice zero as a Gate payment.
