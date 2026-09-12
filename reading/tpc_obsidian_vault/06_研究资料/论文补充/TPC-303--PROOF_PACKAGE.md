---
type: "source-reading"
source_path: "papers/tpc-303-cardinality-monotonicity-obstruction/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-303"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-303-cardinality-monotonicity-obstruction/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-303|TPC-303]] · [[00_开始阅读|首页]]

# TPC-303 proof package

## Proposition 1 - interval order

If (x\in[L_x,U_x]), (y\in[L_y,U_y]), and (U\_y\<L\_x), then (y\<x). Likewise (L\_y\>U\_x) implies (y\>x). This is immediate from the definition of an interval and is the exact certificate used for every transition.

## Proposition 2 - scoped finite refutation

Let (B(Q)) be the represented budget on the declared finite Q-spine. If one adjacent pair satisfies (B(Q\_{j+1})\<B(Q\_j)), then (B) is not nondecreasing on that spine. The conclusion is purely finite and makes no claim about an eventual asymptotic sequence.

## Proposition 3 - same-prefix firewall

If the two budgets use the same profile prefix index (k), their source profile space and all three row/prefix normalizers are held at the same declared prefix. A certified budget descent in such a pair therefore cannot be explained by a change in the number of available profiles. It may still come from the moving physical shell or from the source-first target label.

## Numerical status

The parent TPC-302 intervals are frozen by SHA-256. Recomputing their order gives 21 certified descents, 33 certified ascents, and no interval overlap over 54 transitions. This is a finite obstruction, not arithmetic (L\^2) evidence.
