---
type: "source-reading"
source_path: "papers/tpc-336-masked-signed-gram-response/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-336"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-336-masked-signed-gram-response/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-336|TPC-336]] · [[00_开始阅读|首页]]

# TPC-336 proof and scope package

## Proposition 1 — finite output-Gram expansion

For any finite matrix `C` and vectors `beta_C` with `beta=sum_C beta_C`,

```text
||C beta||^2 = sum_C ||C beta_C||^2
               + 2 sum_{C<D}<C beta_C,C beta_D>.
```

**Proof.** Expand the squared Euclidean norm of the finite sum and pair the two symmetric cross terms. `QED`.

## Proposition 2 — finite response certificate

For the fixed all-plus operator and six declared windows, the output-Gram expansion is replayed, the gain ordering is identical in all six rows, and the self-energy sum exceeds the full response energy in all six rows.

**Evidence.** The producer and an independent reverse-shell implementation recompute the matrices and masks. A stress suite rejects five mutations. The response identity is a finite numerical certificate; its small residual is explicitly bounded rather than promoted to an exact floating-point claim.

## Scope boundary

The result refutes only the scoped idea that the TPC-335 source-share ordering can be transferred unchanged through this fixed operator. It supplies no uniform operator estimate, arithmetic cancellation theorem, or twin-prime conclusion.
