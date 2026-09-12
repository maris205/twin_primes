---
type: "source-reading"
source_path: "papers/tpc-334-cross-term-support-ledger/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-334"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-334-cross-term-support-ledger/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-334|TPC-334]] · [[00_开始阅读|首页]]

# TPC-334 derivation package

## 1. Exact support implication

In the declared model,

```text
b(t)=0                 if t is even,
Lambda(t+2)=0          unless t+2=p^k for a prime p and k>=1.
```

Therefore a nonzero coordinate of `Lambda(t+2)b(t)` lies in the set `{t odd, t+2=p^k}`.

## 2. Disjoint partition

Split this set into

```text
k=1 and t prime       -> twin_prime,
k=1 and t not prime   -> non_twin_prime_shift,
k>=2                  -> prime_power_shift.
```

All remaining coordinates have zero cross contribution. The four category masses are consequently nonnegative and sum exactly to `<Lambda,b>` in the finite array.

## 3. Fractions

For total cross mass `X>0`, define `f_C = X_C/X`. The certificate records `f_C` for all four categories, together with counts and the floating-point partition residual. These fractions are finite diagnostics; no asymptotic limit is taken.
