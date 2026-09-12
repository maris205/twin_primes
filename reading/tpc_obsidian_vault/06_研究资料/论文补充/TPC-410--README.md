---
type: "source-reading"
source_path: "papers/tpc-410-c1-odd-complete-shell-height-replication/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-410"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-410-c1-odd-complete-shell-height-replication/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-410|TPC-410]] · [[00_开始阅读|首页]]

# TPC-410: Odd complete-shell height replication

TPC-410 fixes the odd complete shell `Q=131072`, containing all `10749` primes in `131072<p<=262144`, and tests the four heights `H=16,32,66,128` with `N=4H`. Every prime is retained. The explicit alternating index profile has `m_minus=5374` and `m_plus=5375`, so the proof does not silently assume an even shell cardinality.

For each row the exact local proxy obeys

```text
0 <= z <= t_1/(a_min sqrt(S_0 S_1)) <= 4/(a_min H) <= 4/H.
```

The exact rational certificate, independent literal CRT replay, and nine mutation tests pass. Decimal values are finite observations only. The result is one synthetic adjacent normalized proxy entry, not a full operator, physical `h_0`, arithmetic sign/`L2`, fixed-power, Route-B, or twin-prime theorem.

Status: `PROVED_EXACT_FINITE_ODD_COMPLETE_SHELL_HEIGHT_REPLICATION`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc410_c1_odd_complete_shell_height_replication.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc410_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc410_adversarial_certificate_stress.py --check
```

The next scoped question is `TEST_C1_ODD_COMPLETE_SHELL_HEIGHT_REPLICATION`.
