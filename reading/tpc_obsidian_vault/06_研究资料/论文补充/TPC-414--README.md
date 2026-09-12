---
type: "source-reading"
source_path: "papers/tpc-414-c1-three-shell-pooled-extension/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-414"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-414-c1-three-shell-pooled-extension/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-414|TPC-414]] · [[00_开始阅读|首页]]

# TPC-414: Three-shell pooled extension

TPC-414 adds the complete shell at `Q=262144` to the TPC-411/412 pooled profile. The three shells contain `5709`, `10749`, and `20390` primes, for `36848` total; at `H=66,N=264`, pooled alternating CRT has `m_minus=m_plus=18424` and shell-local amplitudes are retained.

The exact rational certificate, fresh-sieve literal replay of every mask, and 9 mutation tests pass. This is a finite synthetic adjacent normalized proxy entry; full operator, physical `h_0`, arithmetic sign/`L2`, fixed-power, Route-B, and twin-prime claims remain open or none.

Status: `PROVED_EXACT_FINITE_THREE_SHELL_POOLED_EXTENSION`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc414_c1_three_shell_pooled_extension.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc414_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc414_adversarial_certificate_stress.py --check
```

The next scoped question is `TEST_C1_THREE_SHELL_POOLED_EXTENSION`.
