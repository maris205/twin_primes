---
type: "source-reading"
source_path: "papers/tpc-407-c1-complete-shell-q-scale-ladder/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-407"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-407-c1-complete-shell-q-scale-ladder/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-407|TPC-407]] · [[00_开始阅读|首页]]

# TPC-407: Complete-Shell C1 Q-Scale Ladder

TPC-407 extends the TPC-406 complete-shell local-entry boundary along the prime-shell scale. At fixed `H=66` and `N=264`, it selects every prime in each of the four even complete shells `Q=4096,8192,16384,32768`, containing respectively `464,872,1612,3030` primes. The alternating CRT residues are `0` on even indices and `-N` on odd indices, with a reconstructed origin above `10^6`.

For every scale, the exact local proxy entry obeys

```text
0 <= z <= t_1/(a_min sqrt(S_0 S_1)) <= 4/(a_min H) <= 4/H.
```

The four rows contain exact rational CRT, kernel, amplitude, and local-energy data. An independent checker literally replays both masked row energies at all scales, and eight mutation tests reject altered scales, shell counts, domain, bounds, cases, and firewall fields. The decimal scale values are finite observations only. `Q=65536` is not included because its complete shell has odd cardinality and is outside the declared alternating `2m` profile.

This remains one adjacent entry of a synthetic proxy; it is not a full operator estimate, physical `h_0` theorem, arithmetic sign or `L2` theorem, fixed-power saving, Route-B closure, or twin-prime result.

Status: `PROVED_EXACT_FINITE_COMPLETE_SHELL_Q_SCALE_LADDER`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc407_c1_complete_shell_q_scale_ladder.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc407_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc407_adversarial_certificate_stress.py --check
```

The next clue is `TEST_C1_COMPLETE_SHELL_Q_SCALE_EXTENSION`.
