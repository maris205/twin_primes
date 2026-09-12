# AI-assisted TPC research framework — English v0.3

## A Source-Traceable Framework for AI-Assisted Research on the Twin Prime Conjecture

Liang Wang  
School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China  
wangliang.f@gmail.com

This separate author-directed edition reframes the preserved mathematical synthesis as a concrete file-based research resource plus an explicitly specified AI-facing task, review, and handoff protocol. It adds a prospective mathematical, formalization, and AI-evaluation agenda. The framework's empirical effectiveness has not been measured; no experiment or mathematical route is launched by this revision.

- [Revised PDF](paper/main.pdf)
- [Searchable Markdown](paper/main.md) — PDF layout and numbering are authoritative.
- [LaTeX master](paper/main.tex) and [section sources](paper/sections/)
- [Portable source-only ZIP](english_v0.3_source.zip) and [build instructions](BUILD_SOURCE.md)
- [Framework artifact/source map](FRAMEWORK_SOURCE_MAP.md)
- [Next-step experiment plan](refine-logs/EXPERIMENT_PLAN.md) and [NOT_RUN tracker](refine-logs/EXPERIMENT_TRACKER.md)
- [Wiki-to-paper concordance](WIKI_REVISION_CROSSWALK.md)
- [Mathematical source matrix](CORE_SOURCE_MATRIX.md) and [unchanged JSON](CORE_SOURCE_MATRIX.json)
- [Author-directed revision plan](REVISION_PLAN.md), [review and change log](paper/PAPER_IMPROVEMENT_LOG.md), and [QA report](QA_REPORT.md)
- [Full editorial TeX diff](REVISION_DIFF.patch)
- [Preserved v0.2 baseline PDF](paper/main_round0_original.pdf), [first review revision](paper/main_round1.pdf), and [second review revision](paper/main_round2.pdf)

## What changed

The title page and PDF metadata use the author-supplied name, affiliation, and email. The title, abstract, introduction, and conclusion now share a framework contribution. Section 2 describes existing versus proposed capabilities and uses the actual operator, analytic loss ledger, and distinguished-seed criterion as scope-preservation examples. Section 11 separates mathematical open obligations from selective formalization and controlled AI evaluation.

The experiment-plan workflow supplied the claim–evidence–run-order structure, matched-budget baselines, record-deletion ablation, leakage safeguards, and stop/go decision points. These are proposed tests, not measured improvements.

All formal statement/proof blocks and displayed mathematics from English v0.2 are preserved. Old bibliography entries and the supplied route map remain unchanged; two formal-mathematics/AI references and one transparently identified internal framework reference are appended. Prior editions, the wiki, and the primary repository are read-only.

This is not a new numbered TPC paper, a proof of the twin-prime conjecture, an archive-wide semantic audit, or a submission-ready empirical AI paper. Both analytic gates and the distinguished-seed gap remain open. Venue, funding, systematic external positioning, and novelty assessment have not been supplied or completed; the named affiliation does not imply institutional endorsement.

## Rebuild and checks

For PDF compilation from the portable ZIP, use [BUILD_SOURCE.md](BUILD_SOURCE.md). It requires no access to the source archive or wiki.

The additional preservation checks below require this workspace's sibling baseline and primary source files. From this edition directory:

    python -B tools/edition.py build --round 2
    python -B tools/edition.py check
    python -O -B tools/edition.py check
    python -B tools/edition.py render
    python -B tools/edition.py package
    python -B tools/edition.py portable

Requirements: Python 3, latexmk/pdfLaTeX/BibTeX, Pandoc, and Poppler. Builds run without shell escape in a fresh scratch directory. Rebuilding changes the PDF hash and invalidates any earlier hash-specific visual receipt until it is rechecked.

The preservation lock covers 156 selected files, including the complete preceding v0.2 directory, the original language editions, the mathematical core sources, and selected wiki records/cards. This is a precise selected-file guarantee, not a claim that every byte of the full wiki/archive has been freshly audited.

The original [420-directory catalog](../twin_primes/synthesis/seven-island-monograph/SOURCE_CATALOG.md) remains in the preserved repository. Source hashes, compilation, and visual checks address fidelity and presentation, not theorem certification.
