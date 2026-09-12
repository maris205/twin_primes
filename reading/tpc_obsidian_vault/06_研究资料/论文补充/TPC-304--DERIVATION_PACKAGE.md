---
type: "source-reading"
source_path: "papers/tpc-304-overlapping-shell-label-transport/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-304"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-304-overlapping-shell-label-transport/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-304|TPC-304]] · [[00_开始阅读|首页]]

# TPC-304 derivation package

Let `S` and `T` be adjacent finite prime shells and let `a:S->{-1,+1}` and `b:T->{-1,+1}` be their source-first weighted labels. On the nonempty overlap `O=S cap T`, define

```text
rho(a,b) = max_{epsilon in {-1,+1}} |O|^{-1} sum_{p in O} a(p) epsilon b(p)
d(a,b)   = min_{epsilon in {-1,+1}} |O|^{-1} #{p in O:a(p) != epsilon b(p)}.
```

Because `a(p)b(p)` is binary,

```text
rho(a,b) = |sum_O a(p)b(p)|/|O|,
d(a,b) = (1-rho(a,b))/2.
```

Independent global sign choices for either label multiply the inner product by `+1` or `-1`, so both quantities are gauge invariant. The producer records the optimizing sign, restricted labels, exact mismatch primes, and rational fractions. TPC-304 then groups the six exponent/pair rows by the three Q transitions and attaches the independently replayed TPC-303 descent census.

The crosswalk is descriptive: a low overlap correlation identifies a candidate label-switching location. It does not evaluate a counterfactual budget with a transported label, so it cannot separate label switching from physical operator change causally.
