---
type: "source-reading"
source_path: "papers/tpc-342-independent-fresh-holdout-reproduction/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-342"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-342-independent-fresh-holdout-reproduction/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-342|TPC-342]] · [[00_开始阅读|首页]]

# TPC-342 proof and scope package

## Proposition 1 — orthogonal projection decomposition

Let N be a finite real matrix and let P\_N be the Euclidean orthogonal projector onto its column space. For every finite vector y,

```text
||y||_2^2 = ||P_N y||_2^2 + ||(I-P_N)y||_2^2.
```

**Proof.** The range of P\_N and the nullspace of P\_N are orthogonal. The two displayed vectors lie in those spaces and sum to y; apply the Pythagorean identity. QED.

## Proposition 2 — bounded residual fraction

If y != 0, then

```text
rho_N(y) = ||(I-P_N)y||_2^2 / ||y||_2^2
```

belongs to \[0,1\].

**Proof.** Both squared norms are nonnegative, and Proposition 1 makes the residual energy no larger than the target energy. QED.

## Proposition 3 — scoped replication decision

On the declared TPC-342 panel, the in-sample guard max rho\_J \< 0.30 and the hostile holdout guard min rho\^LOO\_j \> 0.40 both hold.

**Evidence.** The canonical certificate contains 108 raw records, 81 nonempty records, three in-sample projections, and 27 held-out projections. The producer and reverse-shell checker independently recompute the same finite values under parent locks; the stress suite rejects six semantic/geometry mutations. The observed ranges are 0.2701410521–0.2951006120 and 0.5894842476–0.9429165296.

## Scope boundary

The result is a numerically certified finite reproduction of a protocol and a scoped finite control-stability obstruction. It is not an asymptotic estimate, a probability law, a source-uniform L2 bound, a signed cancellation theorem, a Route-A/Route-B official pass, or a twin-prime theorem. The nuisance span remains a declared modeling choice.
