---
type: "source-reading"
source_path: "papers/tpc-339-mask-aware-frobenius-envelope/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-339"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-339-mask-aware-frobenius-envelope/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-339|TPC-339]] · [[00_开始阅读|首页]]

# TPC-339 proof and scope package

## Proposition 1 — support-restricted Frobenius envelope

For every finite real matrix `A` and every vector supported on `S`, `||A x||^2 <= F(S)^2 ||x||^2`, where `F(S)^2 = ||A[:,S]||_F^2`.

**Proof.** The induced Euclidean operator norm of `A_S` is at most its Frobenius norm. Apply this inequality to `x_S`. `QED`.

## Finite certificate

The producer evaluates 216 control/mask records on six windows. All 216 support envelopes pass the bound guard. There are 198 nonempty records. The global nonempty occupancy range is `0.0074766258--1.0000000000`; the broad mask classes (twin, non-twin, and zero-support) have occupancy at most `0.1868550366`. The background maximum is `0.0558500985` and the zero-support maximum is `0.0320675913`.

## Scope boundary

The inequality is a general finite theorem, but the occupancy census is tied to one operator, source panel, and nine controls. Low occupancy shows that this elementary envelope is loose; it does not prove that no sharper bound exists. No source-uniform estimate, arithmetic power credit, or twin-prime conclusion follows.
