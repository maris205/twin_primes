---
type: "source-reading"
source_path: "papers/tpc-416-c1-four-shell-odd-pooled-extension/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-416"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-416-c1-four-shell-odd-pooled-extension/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-416|TPC-416]] · [[00_开始阅读|首页]]

# TPC-416: Four-shell odd pooled extension

TPC-416 adds the complete shell at `Q=524288` to the three-shell pooled profile. The four shells contain `5709`, `10749`, `20390`, and `38635` primes, for `75483` total. At `H=66,N=264`, shell-local amplitudes and pooled alternating CRT give the explicit odd counts `m_minus=37741,m_plus=37742`.

The exact rational certificate, fresh-sieve literal replay of every mask, and 10 mutation tests pass. This is a finite synthetic adjacent normalized proxy entry; full operator, physical `h_0`, arithmetic sign/`L2`, fixed-power, Route-B, and twin-prime claims remain open or none.

Status: `PROVED_EXACT_FINITE_FOUR_SHELL_ODD_POOLED_EXTENSION`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc416_c1_four_shell_odd_pooled_extension.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc416_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc416_adversarial_certificate_stress.py --check
```
