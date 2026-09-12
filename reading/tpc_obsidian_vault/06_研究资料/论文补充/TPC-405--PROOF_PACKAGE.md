---
type: "source-reading"
source_path: "papers/tpc-405-c1-local-normalization-scale-ladder/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-405"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-405-c1-local-normalization-scale-ladder/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-405|TPC-405]] · [[00_开始阅读|首页]]

# Proof package

## Theorem (uniform adjacent-entry proxy bound)

Let H,N,Q be integers with H\>=1, N\>=H+2, and Q\>N. Let p\_0\<…\<p\_{2m-1} be distinct primes in (Q,2Q\], with m\>=1, and let o be any CRT solution above a prescribed lower bound satisfying o=0 (mod p\_i) for even i and o=-N (mod p\_i) for odd i. Set t\_d=H^2/(H^2+d\^2), S\_0=sum\_{d=1}^{N-1}t\_d^2, and S\_1=sum\_{d=1}^{N-2}t\_d^2+t\_1\^2. For a\_i=p\_i\^3/\[Q\^2(p\_i-1)\], define P\_- = sum\_{i odd}a\_i, V\_- = sum\_{i odd}a\_i\^2, and V\_+ = sum\_{i even}a\_i\^2. In the TPC-404 selected-prime local proxy, G\_0=V\_-S\_0, G\_1=V\_-S\_1+V\_+(S\_1-t\_1\^2), and M=t\_1P\_-. If z=M/sqrt(G\_0G\_1) and a\_min=min\_i a\_i, then

```text
0 <= z <= t_1/(a_min sqrt(S_0S_1)) <= 4/(a_min H) <= 4/H.
```

## Proof

All amplitudes and t\_d are positive, so z\>=0 and the two energies are positive. Since S\_1-t\_1^2=sum\_{d=1}^{N-2}t\_d\^2\>=0, G\_1\>=V\_-S\_1. Cauchy–Schwarz gives P\_-\^2\<=mV\_-, while the m odd indices give V\_-\>=m a\_min\^2. Thus

```text
z^2 <= t_1^2(mV_-)/[(V_-S_0)(V_-S_1)]
     =  t_1^2 m/(V_-S_0S_1)
     <= t_1^2/(a_min^2 S_0S_1).
```

For 1\<=d\<=H, t\_d\>=1/2. Since N\>=H+2, these terms occur in both finite sums, so S\_0,S\_1\>=H/4. Also a\_i=(p\_i/Q)\^2 p\_i/(p\_i-1)\>1 because p\_i\>Q. Taking square roots proves the sharp and coarse bounds. No asymptotic or source-identification step is used.

The theorem is PROVED\_UNIFORM only for the single selected-prime adjacent proxy entry. It says nothing about the full operator norm or the arithmetic source.
