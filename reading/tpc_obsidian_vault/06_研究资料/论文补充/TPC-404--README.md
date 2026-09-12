---
type: "source-reading"
source_path: "papers/tpc-404-c1-local-normalization-boundary/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-404"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-404-c1-local-normalization-boundary/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-404|TPC-404]] · [[00_开始阅读|首页]]

# TPC-404: C1 Local-Normalization Boundary

TPC-404 audits the next question forced by TPC-403: does its large raw adjacent coefficient survive the local diagonal normalization? On the same finite CRT proxy profile, the answer is an exact finite boundary calculation. If `T_1=H^2/(H^2+1)`, `S_0=sum_{d=1}^{N-1}T_d^2`, and `S_1=sum_{d=1}^{N-2}T_d^2+T_1^2`, then

```text
V_minus = sum_{odd i} a_{p_i}^2, V_plus = sum_{even i} a_{p_i}^2,
G(o)   = V_minus S_0,
G(o+1) = V_minus S_1 + V_plus (S_1-T_1^2),
M(o,o+1) = T_1 P_minus.
```

Consequently the locally normalized square is exactly `(T_1 P_minus)^2/(G(o)G(o+1))`. For `m=1,2,3,4` selected shell-prime profiles, its float64 square-root observations are respectively `0.013630716999888`, `0.013610790517299`, `0.013594253931078`, and `0.013570927022735`. The exact certificate stores all underlying quantities as rational strings; the decimals are observations only.

Only the selected primes are included in the proxy operator and its geometry; this is not a replacement for the complete shell. This is a finite/model audit of one entry, not an upper bound on the full operator norm. It does not prove a growing normalized obstruction, identify the arithmetic sign, pay an arithmetic `L2` estimate, or advance Route B toward twin primes.

Status: `PROVED_EXACT_FINITE_LOCAL_NORMALIZATION_BOUNDARY_AUDIT`; `ARITHMETIC_ADVANCE=NO`; `FIXED_POWER_CREDIT=0`; `FULL_GATE_B=OPEN`; `TWIN_PRIME_RESULT=NONE`.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/tpc404_c1_local_normalization_boundary.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc404_independent_checker.py --check
PYTHONDONTWRITEBYTECODE=1 python -B experiments/tpc404_adversarial_certificate_stress.py --check
```

The next clue is `TEST_C1_LOCAL_NORMALIZATION_SCALE_LADDER`.
