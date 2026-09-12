---
type: "source-reading"
source_path: "papers/tpc-406-c1-local-normalization-complete-shell-entry-boundary/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-406"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-406-c1-local-normalization-complete-shell-entry-boundary/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-406|TPC-406]] · [[00_开始阅读|首页]]

# TPC-406: C1 Complete-Shell Local-Entry Boundary

TPC-406 closes the finite shell-selection gap left by TPC-405 for the same synthetic proxy entry. For each of the five heights `H=16,32,66,128,256`, it selects every one of the 872 primes in `8192<p<=16384`, uses the alternating CRT residues `0,-N` with `N=4H`, and reconstructs an origin above `10^6`.

The exact local identity is unchanged. With `m=436`, `G_0=V_-S_0`, `G_1=V_-S_1+V_+(S_1-t_1^2)`, and `M=t_1P_-`,

```text
0 <= z <= t_1/(a_min sqrt(S_0 S_1)) <= 4/(a_min H) <= 4/H.
```

The certificate contains five exact rational rows, the complete shell, CRT data, and a literal independent masked-energy replay. This is a complete- shell finite audit of one adjacent synthetic proxy entry. It is not a full operator norm theorem, a physical `h_0` result, an arithmetic sign or `L2` theorem, a fixed-power saving, Route-B closure, or a twin-prime result.

Status: `PROVED_EXACT_FINITE_COMPLETE_SHELL_LOCAL_ENTRY_BOUNDARY`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`; `TWIN_PRIME_RESULT=NONE`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc406_c1_local_normalization_complete_shell_entry_boundary.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc406_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc406_adversarial_certificate_stress.py --check
```

The next clue is `TEST_C1_COMPLETE_SHELL_LOCAL_ENTRY_SCALE_EXTENSION`.
