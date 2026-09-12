---
type: "source-reading"
source_path: "papers/tpc-269-growing-cutoff-profile-transfer/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-269"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-269-growing-cutoff-profile-transfer/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-269|TPC-269]] · [[00_开始阅读|首页]]

# TPC-269 proof and certificate package

## Finite identities

1.  The registered cutoff schedule is explicit and finite.
2.  The two-kernel mixture satisfies A\_theta=(1-theta)A\_1+theta A\_2 exactly.
3.  The rank-three projection gives C=C\_3+C\_perp exactly, with positive residual norm on every listed row.

## Certified result

The interval producer uses the TPC-268 rational interval engine and computes the mixture output as an exact Fraction combination of the two exact operator outputs. It classifies a row only when the upper endpoint of rho\^2 is below 1/16 or the lower endpoint is above 1/16.

The twelve rows contain eight contractions and four obstructions. The growing cutoff base already has two obstructions. At the same central row (N,H,Q)=(64,15,4), theta=9/10 is an obstruction while theta=24/25 is a contraction.

## Status firewall

-   `PROVED_EXACT_FINITE`: cutoff registry, affine profile identity, operator and projection algebra.
-   `NUMERICALLY_CERTIFIED`: all twelve outward interval classifications.
-   `REFUTED_SCOPED`: a universal quarter claim over the registered finite proxy family.
-   `OPEN`: uniformity for the actual source-level growing cutoff/profile, radius growth, arithmetic L2 and full Gate B.

The independent replay is intentionally a separate floating-point implementation and is an audit, not a replacement for the interval certificate.
