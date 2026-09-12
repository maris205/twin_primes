---
type: "source-reading"
source_path: "papers/tpc-165-source-backed-local-global-crosswalk-gluing/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-165"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-165-source-backed-local-global-crosswalk-gluing/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-165|TPC-165]] · [[00_开始阅读|首页]]

# TPC-165: source-backed local-to-global crosswalk gluing

Paper title:

> *Source-Backed Local-to-Global Gluing for Formal H1 Occurrence Crosswalks*

## Formal theorem

For a finite cover of archived cuts, suppose each patch supplies a finite nonempty local row family and every overlap supplies an exact, typed, weight-preserving bijection. If the overlap maps satisfy the identity, inverse, and triple-overlap cocycle laws, then quotienting the disjoint union of local rows gives:

```text
a global formal row family
unique descent of every preserved typed payload
uniqueness up to the unique isomorphism commuting with local maps
exact global column conservation when all local column sums are one
```

This is a formal L0 theorem. In production it becomes useful only after source-backed local occurrence edges and their overlaps exist.

## Production status

TPC-163 finds zero theorem-backed production actual-occurrence edges in the frozen declared corpus. Therefore:

```text
production local patch family       NOT_TESTABLE
production overlap cocycle          NOT_TESTABLE
production formal totality          NOT_TESTABLE
production actual active support    NOT_TESTABLE
production canonical minimality     NOT_TESTABLE
```

The last three are separate gates. Even a format-verifier pass for a formal occurrence witness would not automatically prove active support or canonical/minimal representation.

## Synthetic nonvacuity

A two-patch fixture with

```text
U1 = {c1,c2}
U2 = {c2,c3}
```

glues four local row copies to three global formal rows. Every local and global rational column sum is exactly one. The fixture is marked `SYNTHETIC_REACHABILITY` and carries no theorem or production semantics.

## Reproduce

```powershell
python experiments/tpc165_gluing_audit.py
python experiments/tpc165_gluing_audit.py --check
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Generated artifacts:

```text
experiments/tpc165_gluing_certificate.json
experiments/tpc165_gluing_audit.json
samples/tpc165_synthetic_local_patches.json
```

Stable archival PDF:

```text
tpc-165-source-backed-local-global-crosswalk-gluing.pdf
```

## Claim boundary

No production local occurrence patch, actual active-support certificate, canonical/minimal parent representation, production H1 crosswalk, positive fixed-`X` L2 result, prime-pair lower bound, or twin-prime theorem is proved.
