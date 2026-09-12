---
type: "source-reading"
source_path: "papers/tpc-306-two-way-operator-target-interaction/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-306"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-306-two-way-operator-target-interaction/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-306|TPC-306]] · [[00_开始阅读|首页]]

# TPC-306 proof package

## Proposition 1: four-cell log decomposition

For positive cells `B_LL,B_LR,B_RL,B_RR`, let `d_L=log(B_LR/B_LL)` and `d_R=log(B_RR/B_RL)`. With `m=(d_L+d_R)/2` and `i=(d_L-d_R)/2`,

```text
d_L=m+i,  d_R=m-i,  m^2-i^2=d_L*d_R.
```

**Proof.** The first two identities follow by adding and subtracting the definitions. Expanding the difference of squares gives `((d_L+d_R)^2-(d_L-d_R)^2)/4=d_L*d_R`. ∎

## Proposition 2: dominance criterion

If `d_L` and `d_R` are nonzero, then they have the same sign exactly when `|m|>|i|`, and opposite signs exactly when `|i|>|m|`.

**Proof.** By Proposition 1, `m^2-i^2=d_L*d_R`. The sign of the product is positive for equal signs and negative for opposite signs. Strictness follows from nonzero effects. ∎

## Proposition 3: positive row-scaling invariance

Replacing `(B_LL,B_LR)` by `(sB_LL,sB_LR)` with `s>0` leaves `d_L` unchanged; the analogous statement holds for the right row. Therefore `m`, `i`, and `q` are invariant under independent positive row normalizations.

**Proof.** The positive factor cancels in the ratio inside the logarithm. ∎

## Numerical certificate statement

Applying the definitions to the locked TPC-305 ratio enclosures gives 54 normalizer rows over 18 cases. Twelve cases have target-main dominance and six have interaction dominance, with no unresolved row. The central transition has five target-main and one interaction case; all three inherited same-prefix cases have target-main dominance. The largest main-dominant `q` is below `0.88`, the smallest interaction-dominant `q` is above `1.2`, and the largest central same-prefix `q` is below `0.64`.

These are finite numerical certifications derived from high-precision parent intervals. They do not constitute an asymptotic or causal theorem.
