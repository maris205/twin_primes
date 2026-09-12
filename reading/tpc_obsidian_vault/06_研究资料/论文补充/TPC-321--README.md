---
type: "source-reading"
source_path: "papers/tpc-321-cross-shell-profile-stability/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-321"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-321-cross-shell-profile-stability/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-321|TPC-321]] · [[00_开始阅读|首页]]

# TPC-321 — Cross-shell spectral-profile stability audit

**Author:** Liang Wang **Affiliation:** School of Mathematics and Statistics, Huazhong University of Science and Technology (HUST), Wuhan, China

## One-line result

For the same literal deleted-diagonal centered prime-shell Gram used in TPC-320, adjacent shell choices (Q o Q’) produce a visibly separated trace-normalized ordered spectrum in every one of 18 finite comparisons. The smallest outward total-variation lower bound is `0.03212981290619634`, and the smallest cumulative (Lorenz/Ky Fan) lower bound is `0.02339722207455566`.

## Status

```text
TPC321_MAXIMUM_CLAIM = NUMERICALLY_CERTIFIED_FINITE_CROSS_SHELL_PROFILE_SEPARATION_AUDIT
TPC321_ROUTE_ADVANCE = YES_SCOPED_CROSS_SHELL_PROFILE_OBSTRUCTION
TPC321_PROFILE_SEPARATION = NUMERICALLY_CERTIFIED_FINITE_18_OF_18
TPC321_TV_SEPARATION = NUMERICALLY_CERTIFIED_FINITE_ALL_GT_0_03
TPC321_LORENZ_KS_SEPARATION = NUMERICALLY_CERTIFIED_FINITE_ALL_GT_0_02
TPC321_MAJORISATION_PATTERN = NUMERICAL_OBSERVATION_3_FORWARD_2_REVERSE_13_MIXED
TPC321_UNIFORM_SHELL_PROFILE = REFUTED_FINITE_PANEL
TPC321_UNIFORM_MAJORISATION = REFUTED_FINITE_PANEL
TPC321_ARITHMETIC_ADVANCE = NO
TPC321_FIXED_POWER_CREDIT = 0
TPC321_FULL_GATE_B = OPEN
TPC321_TWIN_PRIME_RESULT = NONE
TPC321_STATUS = NUMERICALLY_CERTIFIED_FINITE_CROSS_SHELL_PROFILE_SEPARATION_AUDIT
```

## What is new

TPC-320 found scale-direction concentration changes after trace normalization. TPC-321 asks the next distinct question: at a fixed source scale (X) and kernel exponent (s), is the *whole ordered normalized profile* stable when the prime shell changes? For a profile (p=(p\_1,ldots,p\_N)), (p\_j=lambda\_j/operatorname{tr}(G)), we record

-   (D\_{ m TV}(p,q)=rac12sum\_j\|p\_j-q\_j\|);
-   (D\_{ m L}(p,q)=max\_{r\<N}\|sum\_{jle r}(p\_j-q\_j)\|);
-   the integrated partial-sum discrepancy (N\^{-1}sum\_{r\<N}\|sum\_{jle r}(p\_j-q\_j)\|).

These are explicitly rank-profile diagnostics. They are not presented as a claim about a limiting spectral measure on eigenvalue *locations*.

The panel is (Xin{640,1280,2560}), (Qin{24,36,54,80}), and (sin{1,2}). Both prime-order accumulations and a second eigensolver are used by the producer; an independent reverse-order/einsum replay checks the stored values. There are 24 rows and 18 adjacent-(Q) comparisons.

The majorization labels are `P_MAJORIZES_Q` in 3 comparisons, `Q_MAJORIZES_P` in 2, and `MIXED` in 13. Thus the finite panel rules out a single universal majorization direction, while leaving any asymptotic shell law open.

## Reproduction

```bash
python -B code/tpc321_cross_shell_profile.py --check
python -O -B code/tpc321_cross_shell_profile.py --check
python -B experiments/tpc321_independent_checker.py --check
python -O -B experiments/tpc321_independent_checker.py --check
python -B experiments/tpc321_profile_stress.py --check
python -O -B experiments/tpc321_profile_stress.py --check
```

The release PDF is `paper/paper.pdf`; the machine-readable certificate is `results/tpc321_certificate.json`. The associated local Bridge-B record is `research/tpc-big-road/bridge_b_tpc321_cross_shell_profile.md`.

Session-named `propose.md` and Route-A/Route-B evaluator files are absent from this checkout. The proof package, independent replay, stress suite, and fail-closed local bridge checker therefore document a scoped local result; they do not constitute an official evaluator pass.
