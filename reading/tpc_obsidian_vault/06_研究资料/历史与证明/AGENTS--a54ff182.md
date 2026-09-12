---
type: "source-reading"
source_path: "AGENTS.md"
snapshot_date: "2026-09-12"
owner: "DOC-a54ff182c7e8acf5"
generated: true
semantic_review: "not-certified-by-conversion"
---

<!-- ORIGINAL_BYTES_LINK -->
[原始Markdown文件（逐字节保留）](../../90_%E9%99%84%E4%BB%B6/%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/AGENTS.md.txt)；可用外部编辑器核对。


[[00_开始阅读|首页]] · [[05_综合与进展/历史总结校注|历史与当前状态的区别]]

# Twin-prime research repository protocol

This repository contains only the twin-prime/TPC program and its necessary source-provenance context. User instructions take precedence. The current mathematical endpoint, open obligations and next-paper triggers live in `TPC_HANDOFF.md`, not in this policy.

## Scope and preservation

-   Treat the current repository and source-locked artifacts as the source of truth. Distinguish source statements, inference, finite computations, conditional results and proved uniform statements.
-   Preserve user changes, original manuscripts, data, raw reviews and source hashes. Never auto-stash, reset, clean, delete, overwrite or silently stage unrelated work. Do not edit expected scientific artifacts merely to pass a test, nor rewrite raw reviews to remove formatting warnings.
-   Do not migrate unrelated RH code or agent configurations into this project. Historical shared policy/context inside the path-scoped provenance archive is a frozen source, not active instructions.
-   Keep `papers/tpc-*` and `research/tpc-big-road/` paths stable: source imports, proof links and release manifests rely on their relative layout.
-   The preserved source-inaccessible directory remains inaccessible; directory markers are not manuscripts or mathematical results.

## Entry points and claim boundaries

-   Read the header of `TPC_HANDOFF.md` and its named current entry before selecting a research route. Read `research/tpc-big-road/TPC_ISLAND_MAP_GUIDE.md` before reporting mathematical location or roadmap progress.
-   The image’s Bridge A is the analytic collective-saving bridge; repository Gate A and Gate B both lie inside it. The image’s Bridge B concerns the distinguished arithmetic seed/dynamics route. A file named `Bridge-B` does not prove either mathematical bridge is crossed.
-   Keep islands stable: 1 arithmetic baseline; 2 analytic cancellation; 3 fixed atom; 4 pair-native/H1 structure; 5 nonautonomous dynamics; 6 twin-prime endpoint; 7 Hénon/geometric auxiliary lifting.
-   Every transfer must retain the literal coefficient and signs/masks/weights, fixed physical `h0`, actual summation domain and prefix order, parameter ranges, uniformity and exceptional sets, normalization and full loss ledger.
-   Do not replace signed cancellation by separate absolute bounds, a prescribed arithmetic seed by an almost-everywhere statement, a physical operator by a model, or a growing theorem by a finite certificate.
-   A checker PASS, review score, migration receipt or larger paper count is not arithmetic progress or a proof of the twin-prime conjecture.
-   Keep stopped methods stopped until their exact source-backed reopening condition changes. Do not create a new paper number, PDF or speculative directory merely to continue a pipeline.

## Agent ownership

-   One primary session owns route decisions, shared files, staging, commits, rebases and pushes. Never race another release-owning session.
-   Match parallelism to independent work and the user’s preference. The shared ceiling is 30 open spawned agents, including descendants and completed but unclosed agents; it is not a target. Respect lower runtime limits.
-   Use bounded, source-locked, preferably read-only audit tasks. Provide the exact objective, baseline, read/write allowlists, forbidden paths, claim ceiling, checks and return contract before delegation.
-   Independent proof/source auditors do not write or synchronize the repository. A paper writer owns only its one primary-approved paper directory, after an exact theorem-backed GO. Dependent papers are not written concurrently.
-   Close agents after retaining their complete reports. The primary integrates evidence and reports scoped GO, STOP\_SCOPED or NOT\_TESTABLE accurately.

## Validation and source history

-   Run only the current relevant read-only checks; inspect unfamiliar scripts before execution. Some historical producers rewrite certificates by default. In particular, do not run legacy TPC27–32 writers as regression checks.

-   Use `PYTHONDONTWRITEBYTECODE=1`, `python -B` and cache-disabled tests. Compare normal and optimized modes when explicit-guard validation requires it.

-   For checks needing old commit IDs, use the validated offline runner described in `docs/REPRODUCIBILITY.md`:

    ```sh
    python -B tools/with_legacy_sources.py -- COMMAND ARGUMENTS
    ```

-   This runner exposes authentic, path-scoped original Git objects. It does not mock Git, change source hashes, import unrelated project payloads or add the mixed repository history to the new branch. Missing sources still fail.

-   Do not mistake that deliberately partial object archive for a complete old repository: unrelated subtrees and parent-history traversal may be absent.

-   Before a new numbered publication, follow the current handoff’s provenance and independent QA requirements. A successful LaTeX build is not full PDF QA; source checks, logs, text/fonts, page rendering and independent visual review are separate obligations.

-   Migration verification checks archive fidelity and navigation, not theorem correctness. Never promote source-Markdown coverage to reliable semantic review without independent full-content evidence.

## Git and SSH release discipline

-   The authorized SSH remote is `git@github.com:maris205/twin_primes.git`. Do not change the old mixed repository or its remote as part of normal work in this repository.
-   Inspect tracked and untracked status, fetch, compare upstream changes and synchronize safely before release. Never auto-stash user changes.
-   Stage only the intended files. Do not include secrets, environments or untracked caches. Retain committed compiler logs/PDF aliases when original manifests or archive indexes require them.
-   Stop all writers before release. If upstream changes source locks, handoff or dependencies, review the changes and repeat affected checks.
-   Before a push to an existing branch, run `git pull --rebase origin main` when the worktree is safe. An empty newly created remote has no branch to pull.
-   Push over SSH without force, then verify `HEAD`, `origin/main` and `git ls-remote origin refs/heads/main` agree.
-   Report local-only commits separately from pushed commits. Do not claim a clean worktree when only tracked files were checked.
