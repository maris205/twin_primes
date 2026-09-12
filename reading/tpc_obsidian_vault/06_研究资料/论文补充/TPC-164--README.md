---
type: "source-reading"
source_path: "papers/tpc-164-minimal-archived-separation-key/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-164"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-164-minimal-archived-separation-key/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-164|TPC-164]] · [[00_开始阅读|首页]]

# TPC-164: minimal archived separation key

Paper title:

> *An Exact Minimal Addressing Key for the Frozen H1 Cut Archive*

## Result

TPC-164 exhausts all `255` nonempty subsets of the frozen field dictionary

```text
ell, k, native_d, jL, jK, D0, reason, type
```

against all `2988` production cut rows. The unique minimum-cardinality separating subset is

```text
(ell, k, native_d, jL, jK)
```

and its cardinality is five. The numbers of injective subsets by cardinality are:

```text
5 fields: 1
6 fields: 3
7 fields: 3
8 fields: 1
```

Selected incomplete-key diagnostics:

```text
(ell,k,native_d)          866 keys, max multiplicity 4
+ reason                 1068 keys, max multiplicity 4
+ jL                     1626 keys, max multiplicity 2
+ jK                     1594 keys, max multiplicity 2
```

The five-field tuple is an exact, lossless address for the frozen archive. It is not an actual-occurrence ID, an active-support certificate, or a canonical/minimal parent representation.

## Reproduce

```powershell
python experiments/tpc164_minimal_key.py
python experiments/tpc164_minimal_key.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Generated artifacts:

```text
experiments/tpc164_minimal_key_certificate.json
experiments/tpc164_minimal_key_audit.json
samples/tpc164_minimal_key_witness.json
```

Stable archival PDF:

```text
tpc-164-minimal-archived-separation-key.pdf
```

## Claim boundary

This is a finite archive-key theorem at L0/L1. It does not construct a production occurrence crosswalk, prove actual active support, select a canonical or minimal actual representation, establish positive fixed-`X` L2, give a prime-pair lower bound, or prove the twin-prime conjecture.
