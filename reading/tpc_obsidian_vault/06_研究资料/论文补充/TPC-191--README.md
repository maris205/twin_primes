---
type: "source-reading"
source_path: "papers/tpc-191-pointwise-frontier-integration/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-191"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-191-pointwise-frontier-integration/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-191|TPC-191]] · [[00_开始阅读|首页]]

# TPC-191: Integration of the Two Pointwise Fixed-Atom Audits

## Exact result

The bad-endpoint route reduces exactly to fixed-atom local oscillation; the direct route requires pointwise arithmetic beyond Parseval. Size-only and uncontrolled metric-to-atom methods are scoped stops, not route stops. Neither parent is closed and the named-atom endpoint ledger remains at zero.

```text
classification = INTEGRATION_L1
verdict = BOTH_POINTWISE_ROUTES_OPEN_METHODS_SCOPED
selected_route = BOTH_O161_POINTWISE_PARENTS
smallest_missing = LITERAL_FIXED_ATOM_ARITHMETIC_CANCELLATION

fixed_atom_decay_obtained = false
named_atom_endpoint_credit = 0
strict_1/400 = UNPAID
```

The result is L0/L1 only. Any `STOP_SCOPED` declaration applies only to the named method cell and does not stop an O161 pointwise parent or the global architecture. No program-positive L2, prime-pair lower bound, or twin-prime theorem is claimed.

## Reproduce

```powershell
python experiments/tpc191_pointwise_frontier_integration.py
python experiments/tpc191_pointwise_frontier_integration.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
