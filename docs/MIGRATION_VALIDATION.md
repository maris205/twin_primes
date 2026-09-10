# Migration validation · 2026-09-10

Source snapshot: `02d51d372e9c95ffc2ed36727829363a32cec030`.
Destination: `git@github.com:maris205/twin_primes.git`, independent `main` history.

| Read-only check | Observed result |
|---|---|
| Main source inventory | 7,670 selected source files; 7,659 unchanged; 11 explicit non-paper adaptations. |
| Main paper coverage | All 420 original TPC directories retained; all 7,032 files under `papers/` unchanged. |
| Early branches | Four TPC-only snapshots, 116 files; hashes recorded. |
| Legacy source archive | 98 snapshots, 10,562 authentic Git objects; every pack/index digest and exact object inventory verified. |
| TPC418 current checker | PASS in normal and optimized wrapper modes, including their child checkers. |
| Source-Markdown unit suite | 126 tests PASS after pinning one inherited historical-PDF assertion to its original source commit. |
| Provenance guard tests | Five tests PASS: duplicate JSON keys, nonfinite constants, path traversal, symlink and boolean-size rejection. |
| Conversion batch TPC140–418 | 279 source locks and 279 text roundtrips PASS; 17,398 math nodes covered. |
| Conversion/index link check | 608 documents and 12,183 local links checked; zero link issues and zero current-coverage issues. |
| Current inventory refresh | PASS: 279 full-source, 140 partial/notes, one inaccessible, zero independently reliable full reviews. |
| Independent local clone | Separate `--no-hardlinks` clone passed archive verification and resolved the original TPC418 TeX by old commit ID using its own packaged source objects. |
| Source repository preservation | Original HEAD and SSH remote unchanged; no tracked changes; its 350 pre-existing untracked files were left in place. |

The initial pre-commit unit run could not resolve a new repository's unborn
HEAD. After the first commit, one inherited test remained stale because the
source repository's final commit had restored `main.pdf`: the historical
fallback assertion now explicitly uses `ed725e6537012bd17a32d061d9d8e6dd3b253613`,
matching that test's existing conversion source. No PDF, manuscript,
certificate or expected scientific result was rewritten.

The original TPC171 manifest's worktree used CRLF while its committed Git blob
uses LF. The migrated file uses the committed blob bytes, as the source
manifest requires. This representation difference is not a mathematical edit.

Limits: these checks do not establish the twin-prime conjecture, full PDF/TeX
synchronization, semantic correctness of every manuscript, all cross-document
anchors, or complete replay of every historical experiment. Existing unmapped
PDF section headings remain reported by the batch checker. Whole-original-repo
audits requiring unrelated objects or complete parent history still require
the original repository. See [scope and commands](REPRODUCIBILITY.md).
