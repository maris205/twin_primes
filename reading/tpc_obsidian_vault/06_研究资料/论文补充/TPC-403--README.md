---
type: "source-reading"
source_path: "papers/tpc-403-c1-crt-origin-proxy-obstruction/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-403"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-403-c1-crt-origin-proxy-obstruction/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-403|TPC-403]] · [[00_开始阅读|首页]]

# TPC-403: CRT-origin proxy obstruction for signed deletion

TPC-403 turns the TPC-402 signed coefficient identity into an explicit adversarial construction for the declared finite proxy. For alternating index signs, choose any distinct primes `p_0<...<p_{2m-1}` with `p_i>N` and use CRT congruences `o=0 (mod p_{2k})` and `o=-N (mod p_{2k+1})`. The positive sign primes hit the first window point and the negative sign primes first hit the exterior point at offset `N`. Hence, for the active pair `(o,o+1)`, `M_sigma(o,o+1)=T_1 P_-`, even when the global scalar `A_sigma=P_+-P_-` is small.

The exact certificate covers `m=1,2,3,4` using the first eight primes in the `Q=8192` shell, with `N=1024`, `H=66`, and an origin lower bound `B=10^6`. All four CRT constructions, masks, coefficients, and identities are exact. The result is a proxy-level obstruction, not a source-valid arithmetic or normalized growing theorem.

```bash
python -B papers/tpc-403-c1-crt-origin-proxy-obstruction/code/tpc403_c1_crt_origin_proxy_obstruction.py --check
python -B papers/tpc-403-c1-crt-origin-proxy-obstruction/experiments/tpc403_independent_checker.py --check
python -B papers/tpc-403-c1-crt-origin-proxy-obstruction/experiments/tpc403_adversarial_certificate_stress.py --check
```

`PROVED_EXACT_FINITE_CRT_PROXY_OBSTRUCTION`, `ARITHMETIC_ADVANCE=NO`, `FIXED_POWER_CREDIT=0`, `FULL_GATE_B=OPEN`, and `ROUND2_CLUE=TEST_C1_CRT_PROXY_NORMALIZATION_BOUNDARY`.
