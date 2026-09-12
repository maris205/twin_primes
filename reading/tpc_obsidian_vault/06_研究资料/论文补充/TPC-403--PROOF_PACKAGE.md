---
type: "source-reading"
source_path: "papers/tpc-403-c1-crt-origin-proxy-obstruction/PROOF_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-403"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-403-c1-crt-origin-proxy-obstruction/PROOF_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-403|TPC-403]] · [[00_开始阅读|首页]]

# Proof package

`PROVED_EXACT_FINITE_CRT_PROXY_OBSTRUCTION`: for every finite set of distinct primes `p_i>N` and every `B`, the displayed CRT congruences have a positive solution `o>B`. Since `0<=r<N<p_i`, the congruence `o=-N (mod p_i)` has no zero in `o+r` for `0<=r<N`, while `o=0 (mod p_i)` has exactly the zero at `r=0`. The difference of the witness pair is `-1`, so the difference mask is zero. Substitution into the exact TPC-402 coefficient identity proves `M_sigma(o,o+1)=T_1P_-`.

The code checks this theorem for four finite cases and records exact rational values. The result is not a normalized growing lower bound, not an arithmetic sign theorem, and not a twin-prime result.
