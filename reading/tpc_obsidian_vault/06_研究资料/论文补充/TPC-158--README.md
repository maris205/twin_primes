---
type: "source-reading"
source_path: "papers/tpc-158-additive-phase-major-minor-gate/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-158"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-158-additive-phase-major-minor-gate/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-158|TPC-158]] · [[00_开始阅读|首页]]

# TPC-158: Additive-phase major/minor gate

Paper title:

> *An Exact Major-Arc Gate for Additive Phases: Periodic Projection and a Minor-Arc Route Obstruction*

Let `I` be an interval of `L` consecutive fiber coordinates. If

```text
q*R <= (log X)^eta_0
L*|alpha-k/R| <= (log X)^(-A),
```

then a phase-aligned period-`R` function approximates `exp(-2*pi*i*alpha*z)` uniformly. TPC-157 therefore gives

```text
(q/N) |sum c_z exp(-2*pi*i*alpha*z)|
  << (log X)^(-kappa_0) + (log X)^(-A).
```

For a complete rectangle of length `K*R`, the normalized squared distance from the phase to the period-`R` subspace is exactly

```text
1 - | sin(pi*K*R*alpha) /
        (K*sin(pi*R*alpha)) |^2,
```

with the continuous limiting value used when the denominator vanishes. This also gives a normalized L1 lower bound equal to half the displayed quantity. For cells of length `L_n`, put `K_(n,R)=floor(L_n/R)`. If, uniformly over all allowed periods,

```text
inf_R K_(n,R) -> infinity,
inf_R K_(n,R)*||R*alpha_n|| -> infinity,
```

then the normalized L1 distance is at least `1/2-o(1)`, uniformly in the allowed period. Thus those phases cannot be handled by the periodic-approximation route. Pointwise separation for each fixed period is not enough when the selected period may drift with `n`.

The positive statement is `L1_ACTUAL_CORE_MAJOR_ARC`. The negative statement stops only the specified periodic-approximation route; it does not say that a minor-arc Mobius correlation is large. Generic phase cancellation, all prefixes, fixed-X power savings, `1/400`, and the twin-prime conjecture remain unproved.

Reproduce:

```powershell
python experiments/tpc158_phase_gate_audit.py
python experiments/tpc158_phase_gate_audit.py --check
```
