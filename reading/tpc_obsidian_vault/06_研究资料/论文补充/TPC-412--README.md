---
type: "source-reading"
source_path: "papers/tpc-412-c1-pooled-complete-shell-extension/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-412"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-412-c1-pooled-complete-shell-extension/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-412|TPC-412]] · [[00_开始阅读|首页]]

# TPC-412: Pooled complete-shell extension

TPC-412 extends the TPC-411 pooled two-shell profile from `H=66` to `H=16,32,66,128`, always with `N=4H`. The two complete shells contain `5709+10749=16458` primes; shell-local amplitudes are retained and pooled alternating CRT has `m_minus=m_plus=8229`.

The exact rational certificate, fresh-sieve literal replay of every mask, and 11 mutation tests pass. The observed `z` values are respectively `0.021785036050694`, `0.010809175951931`, `0.005216872683870`, and `0.002683946067759`; these are finite numerical observations.

Status: `PROVED_EXACT_FINITE_POOLED_COMPLETE_SHELL_EXTENSION`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`. This remains one synthetic adjacent normalized proxy entry, with full operator, physical `h_0`, arithmetic sign/`L2`, Route-B and twin-prime claims open or none.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc412_c1_pooled_complete_shell_extension.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc412_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc412_adversarial_certificate_stress.py --check
```

The next scoped question is `TEST_C1_POOLED_COMPLETE_SHELL_EXTENSION`.
