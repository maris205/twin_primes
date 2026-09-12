---
type: "source-reading"
source_path: "papers/tpc-411-c1-pooled-odd-complete-shells/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-411"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-411-c1-pooled-odd-complete-shells/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-411|TPC-411]] · [[00_开始阅读|首页]]

# TPC-411: Pooled odd complete shells

TPC-411 pools the full odd shells at `Q=65536` and `Q=131072`, retaining all `5709+10749=16458` primes. At fixed `H=66`, `N=264`, the pooled ordered profile has `m_minus=m_plus=8229`; each amplitude uses the shell scale of its own prime. The exact local proxy satisfies `0<=z<=4/H`.

The rational certificate, independent literal pooled CRT replay, and nine mutation tests pass. This is one finite synthetic adjacent normalized proxy entry; full operator norm, physical `h_0`, arithmetic sign/`L2`, fixed-power, Route-B, and twin-prime claims remain open or none.

Status: `PROVED_EXACT_FINITE_POOLED_ODD_COMPLETE_SHELLS`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc411_c1_pooled_odd_complete_shells.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc411_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc411_adversarial_certificate_stress.py --check
```

The next scoped question is `TEST_C1_POOLED_COMPLETE_SHELL_EXTENSION`.
