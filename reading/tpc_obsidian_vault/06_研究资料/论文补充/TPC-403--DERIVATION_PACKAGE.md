---
type: "source-reading"
source_path: "papers/tpc-403-c1-crt-origin-proxy-obstruction/DERIVATION_PACKAGE.md"
snapshot_date: "2026-09-12"
owner: "TPC-403"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-403-c1-crt-origin-proxy-obstruction/DERIVATION_PACKAGE.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-403|TPC-403]] · [[00_开始阅读|首页]]

# Derivation package

Let `I_o={o,...,o+N-1}` and `T_1=H^2/(H^2+1)`. For distinct primes `p_i>N`, impose

`o = 0 (mod p_{2k})`, `o = -N (mod p_{2k+1})`.

CRT gives one residue class modulo `P=product p_i`, and adding multiples of `P` gives an origin above every prescribed bound `B`. In the window, an even prime divides only `o`, while an odd prime would first divide `o+N`, outside the half-open window. No selected prime divides `o-(o+1)=-1`.

For `a_i=p_i^3/(Q^2(p_i-1))`, `sigma_i=(-1)^i`, write `P_+=sum_even a_i`, `P_-=sum_odd a_i`, and `A_sigma=P_+-P_-`. Then `b_sigma(o)=P_+`, `b_sigma(o+1)=0`, so TPC-402 gives

`M_sigma(o,o+1)=T_1[-A_sigma+P_+]=T_1 P_-`.

The construction is exact for raw coefficients. It does not identify the synthetic alternating law with a physical arithmetic sign law and does not control any normalization denominator.
