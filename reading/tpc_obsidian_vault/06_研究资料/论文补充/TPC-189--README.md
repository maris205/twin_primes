---
type: "source-reading"
source_path: "papers/tpc-189-direct-twist-literal-target-contract/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-189"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-189-direct-twist-literal-target-contract/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-189|TPC-189]] · [[00_开始阅读|首页]]

# TPC-189: A Literal Contract for the Direct Additive-Twist Fixed-Atom Target

## Exact result

The direct target is frozen as the q/N-normalized determinant-two core twist at the prescribed atom, uniformly in every deterministic scale and prefix. TPC-167 proves the exact phase Parseval identity, not this singleton theorem.

```text
classification = CONTRACT_L0_L1
verdict = TARGET_WELL_TYPED_OPEN
selected_route = O161.direct_additive_twist_fixed_atom
smallest_missing = DIRECT_ADDITIVE_TWIST_NAMED_ATOM_POWER_SAVING

fixed_atom_decay_obtained = false
named_atom_endpoint_credit = 0
strict_1/400 = UNPAID
```

The result is L0/L1 only. Any `STOP_SCOPED` declaration applies only to the named method cell and does not stop an O161 pointwise parent or the global architecture. No program-positive L2, prime-pair lower bound, or twin-prime theorem is claimed.

## Reproduce

```powershell
python experiments/tpc189_direct_twist_literal_target_contract.py
python experiments/tpc189_direct_twist_literal_target_contract.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
