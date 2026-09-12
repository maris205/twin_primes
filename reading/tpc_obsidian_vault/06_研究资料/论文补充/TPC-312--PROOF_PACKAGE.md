---
type: "source-reading"
source_path: "papers/tpc-312-new-source-shell-separation-atlas/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-312"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-312-new-source-shell-separation-atlas/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-312|TPC-312]] · [[00_开始阅读|首页]]

# TPC-312 proof package

## Proposition 1: Gram positivity

For any real vector `c`,

$$  c^T Gc=\sum_{u\in I}\left(\sum_{p\in S_Q}c_pg_p(u)\right)^2\ge0. $$

Thus each physical Gram matrix is positive semidefinite. All `g_p(u)` are rational because the source coefficients and kernels are rational.

## Proposition 2: global-sign reduction

`E(-c)=(-c)^TG(-c)=c^TGc=E(c)`. Every sign vector has exactly one representative with its first coordinate `+1`; hence `2^(|S_Q|-1)` states are enough for the finite extremum search.

## Proposition 3: Gray coverage

The reflected Gray map `g(k)=k xor (k>>1)` is a bijection on the integers `0,...,2^m-1`, and consecutive values differ in exactly one bit. The producer’s incremental update changes one sign at a time and visits every global-sign class once. The independent stress suite compares its visited energy multiset with direct enumeration on a four-dimensional rational Gram fixture.

## Proposition 4: modular rank certificate

After clearing rational denominators, a nonzero determinant modulo the declared prime `1000000007` implies a nonzero rational determinant, provided the cleared denominator is invertible modulo that prime. The checker verifies these conditions and obtains full rank for all eight rows. This is a finite rank certificate, not an asymptotic statement.

## Proposition 5: finite separation and ordering

The producer and independent checker compare exact `Fraction` values. They verify `r^-<1<r^+` in every row, the two strict Q-spine chains, and the four exponent-two strengthening inequalities. These are direct finite arithmetic facts recorded in the certificate and do not imply a limit law.
