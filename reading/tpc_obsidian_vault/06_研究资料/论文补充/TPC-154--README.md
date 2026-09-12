---
type: "source-reading"
source_path: "papers/tpc-154-conservative-completion-fiber-obstruction/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-154"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-154-conservative-completion-fiber-obstruction/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-154|TPC-154]] · [[00_开始阅读|首页]]

# TPC-154: Conservative completion-fiber obstruction

TPC-154 asks whether the actual one-to-many occurrence lift can be recovered from the TPC-153 cut shadow alone. It cannot be identified from the current schema.

For every partial source row the audit constructs two exact formal completions:

```text
A: one child with weight 1
B: two row-separated children with weights 1/2 and 1/2
```

Both forget to the same unit shadow column. Their row-separated branch counts differ. Consequently branch multiplicity and the populated formal parent, zero-mode, physical-group, stage and target-shift labels do not descend to the current schema.

The scope is essential:

```text
H1.formal_completion_fiber_nonuniqueness
    = PROVED_L0_SCHEMA
H1.current_artifacts_only_canonical_actual_lift
    = STOP_DECLARED_ROUTE
H1.augmented_actual_occurrence_lift
    = NOT_TESTABLE
selected_augmented_route_stopped
    = false
```

The generated children are `FORMAL_ONLY`. They are not asserted to be actual arithmetic occurrences. Thus the paper does not prove that the actual carrier has two completions, or that a theorem-backed augmented route is impossible.

Run:

```bash
python experiments/tpc154_completion_fiber_obstruction.py
python experiments/tpc154_completion_fiber_obstruction.py --check
```

The deterministic artifacts are:

-   `samples/tpc154_formal_completions.jsonl`;
-   `experiments/tpc154_completion_fiber_obstruction_certificate.json`;
-   `schemas/tpc154-conservative-completion-v1.schema.json`.

All 2,988 current production fibers are FUM. One ETO fiber is included only as a separately tagged `SYNTHETIC_L0_ONLY` schema regression. TPC-153 is rerun and locked with `CANONICAL_UTF8_LF_V2`; hashes have integrity semantics only.
