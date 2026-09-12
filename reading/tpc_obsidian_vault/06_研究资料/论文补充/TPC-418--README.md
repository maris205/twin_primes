---
type: "source-reading"
source_path: "papers/tpc-418-c1-shell-parity-envelope/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-418"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-418-c1-shell-parity-envelope/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-418|TPC-418]] · [[00_开始阅读|首页]]

# TPC-418 — finite-family shell-parity envelope

This package proves a finite synthetic theorem for any declared finite family of disjoint ordered complete prime shells. The corrected parity variable is

```text
epsilon_j = (-1)^(sum before block j)       # start sign
sigma_j   = epsilon_j * (-1)^(n_j+1)         # signed-block sign
```

The envelope groups `b_j` by `sigma_j`, not by `epsilon_j`. A mixed-parity fixture records that the old grouping can fail. The fixed four-shell replay retains the TPC417 shell family and all 75483 primes; a small complete-shell fixture and the regression fixture provide independent audit coverage.

All theorem quantities are exact `Fraction` values serialized as canonical rational strings. The release is finite and synthetic only. It asserts no growing uniform theorem, physical `h0`, arithmetic sign or `L2` result, fixed-power credit, Route-B closure, or twin-prime result.

Commands:

```bash
python -B papers/tpc-418-c1-shell-parity-envelope/code/tpc418_c1_shell_parity_envelope.py --write
python -B papers/tpc-418-c1-shell-parity-envelope/code/tpc418_c1_shell_parity_envelope.py --check
python -B papers/tpc-418-c1-shell-parity-envelope/experiments/tpc418_independent_checker.py --check
python -B papers/tpc-418-c1-shell-parity-envelope/experiments/tpc418_adversarial_certificate_stress.py --check
python -B research/tpc-big-road/tpc_bridge_b_tpc418_c1_shell_parity_envelope_checker.py --check
```

Each command is also run with `python -O -B`. The Bridge-B checker verifies the exclusive package, certificate digest, independent replay, mutation tests, and compiled PDFs when they are available.
