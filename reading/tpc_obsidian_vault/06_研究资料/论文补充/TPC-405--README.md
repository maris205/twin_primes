---
type: "source-reading"
source_path: "papers/tpc-405-c1-local-normalization-scale-ladder/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-405"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-405-c1-local-normalization-scale-ladder/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-405|TPC-405]] · [[00_开始阅读|首页]]

# TPC-405: C1 Local-Normalization Scale Ladder

TPC-405 turns the TPC-404 local identity into a parameter-uniform theorem for one adjacent entry of the selected-prime CRT proxy. Let H,N be integers with H\>=1, N\>=H+2, let Q\>N, and choose 2m distinct primes Q\<p\_i\<=2Q, with the explicit CRT residues o=0 (mod p\_i) for even i and o=-N (mod p\_i) for odd i. With the TPC-404 selected-prime local geometry,

```text
0 <= z <= t_1/(a_min sqrt(S_0 S_1)) <= 4/(a_min H) <= 4/H.
```

Here z is the locally normalized entry at (o,o+1), a\_min is the smallest selected amplitude, and S\_0,S\_1 are the two translated kernel energies. The proof is Cauchy–Schwarz plus G(o+1)\>=V\_minus S\_1, S\_0,S\_1\>=H/4, and a\_p\>1.

The exact certificate covers a 5-by-4 scale ladder with H in 16,32,66,128,256 and N=4H, all m=1,2,3,4 (20 cases). Decimal normalized values are observations, while the inequalities and stored quantities are exact rationals. The theorem is only for this one synthetic selected-prime proxy entry; it is not a full operator estimate, not a theorem for the physical h\_0, and not an arithmetic or twin-prime result.

Status: PROVED\_UNIFORM\_FINITE\_CRT\_PROXY\_ADJACENT\_ENTRY\_BOUND; ARITHMETIC\_ADVANCE=NO; FIXED\_POWER\_CREDIT=0; FULL\_GATE\_B=OPEN; TWIN\_PRIME\_RESULT=NONE.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc405_c1_local_normalization_scale_ladder.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc405_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc405_adversarial_certificate_stress.py --check
```

The next clue is TEST\_C1\_LOCAL\_NORMALIZATION\_COMPLETE\_SHELL\_ENTRY\_BOUNDARY.
