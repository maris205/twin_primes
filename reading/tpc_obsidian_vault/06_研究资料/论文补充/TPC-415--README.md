---
type: "source-reading"
source_path: "papers/tpc-415-c1-three-shell-height-extension/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-415"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-415-c1-three-shell-height-extension/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-415|TPC-415]] · [[00_开始阅读|首页]]

# TPC-415: Three-shell height extension

TPC-415 extends the TPC-414 three-shell pooled profile to `H=16,32,66,128`, always with `N=4H`. The shells at `Q=65536,131072,262144` retain `5709+10749+20390=36848` primes; shell-local amplitudes and pooled equal parity counts `m_minus=m_plus=18424` are retained at every height.

The exact certificate, fresh-sieve literal replay of every mask, and 11 mutation tests pass. The four normalized observations are `0.021769164863228`, `0.010801304431278`, `0.005213074464832`, and `0.002681992180281`; these are finite numerical observations only.

Status: `PROVED_EXACT_FINITE_THREE_SHELL_HEIGHT_EXTENSION`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`. Full operator, physical `h_0`, arithmetic sign/`L2`, fixed-power, Route-B, and twin-prime claims remain open or none.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc415_c1_three_shell_height_extension.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc415_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc415_adversarial_certificate_stress.py --check
```
