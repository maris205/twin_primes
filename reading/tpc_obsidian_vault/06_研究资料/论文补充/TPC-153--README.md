---
type: "source-reading"
source_path: "papers/tpc-153-canonical-cut-occurrence-shadow/README.md"
snapshot_date: "2026-09-12"
owner: "TPC-153"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/papers/tpc-153-canonical-cut-occurrence-shadow/README.md.txt)；可用外部编辑器核对。


论文入口：[[02_论文/TPC-153|TPC-153]] · [[00_开始阅读|首页]]

# TPC-153: Canonical cut-occurrence shadow

TPC-153 constructs the strongest occurrence-like object determined by the current cut archive:

```text
H1.cut_occurrence_shadow = PROVED_L1_STRUCTURAL
H1.frontier_occurrence_lift = NOT_TESTABLE
```

There is exactly one partial shadow row of exact weight `1` for every nonsoft source path in `ETO union FUM`. Hence the shadow matrix is an injective, row-separated and conservative identity injection. It preserves only sourced cut data. It does not contain an actual occurrence ID, actual branch count, canonical parent, later stage, downstream selector, physical group, or active-support certificate.

The current production census is:

```text
ELIGIBLE_TAIL_OPEN = 0
FRONTIER_UNMAPPED  = 2988
```

The separate ETO record is explicitly `SYNTHETIC_L0_ONLY`. It tests the domain contract and is not included in the production census or treated as an asymptotic existence theorem.

Run the deterministic audit from this paper directory:

```bash
python experiments/tpc153_cut_occurrence_shadow.py
python experiments/tpc153_cut_occurrence_shadow.py --check
```

It writes and checks:

-   `samples/tpc153_cut_occurrence_shadow.jsonl`;
-   `samples/tpc153_synthetic_eto_regression.json`;
-   `experiments/tpc153_cut_occurrence_shadow_certificate.json`.

The script reruns TPC-143 and binds the source chain under `CANONICAL_UTF8_LF_V2`. Hashes are integrity locks only. The conditional identity `q_pushforward(L_X) = S_X` states what every future actual completion must satisfy; it does not construct `L_X`.
