# Wiki-informed English paper improvement log

Scope: editorial revision only, 12 September 2026. No new numbered paper, research result, proof of TPC, external upload, or Git release.

## Review method

The auto-paper-improvement-loop skill supplies the two-round review–fix–build structure, and paper-compile supplies preservation and presentation checks. Its named GPT-5.4 MCP channel is unavailable. The actual reviewer is an available inherited-model independent read-only agent, reused across rounds. No numerical score is requested or fabricated. This is not a completed ARS approved-claim revision protocol, external peer review, or a novelty/submission-readiness certification.

The primary read every baseline section, all fourteen knowledge cards' summaries/boundaries/relations, relevant full cards, the map guide and current handoff, and targeted original sources for V58, the Kloosterman emitter/one-sided obstruction, constructive boundary proof, weighted cover/composition, moving-target variance and seed criterion. The wiki determines reading connections; original statements determine claim scope. The independent review's own exact scope is retained in its raw report.

## Round 1

Full, unedited independent report: [ROUND1_RAW.md](reviews/ROUND1_RAW.md).

| Finding | Change made |
|---|---|
| R1: analytic output versus TPC endpoint | Rewrote the introduction to distinguish the mixed scalar, imported same-index output, and prime-pair count. Added a notation guide; explicitly named analytic Gate B in the ledger. |
| R2: occurrence summary too strong | Restored conditional attachment/conservation/cover wording in the conclusion; explicitly stated that Section 3 does not construct the production lift consumed upstream. |
| R3: dependency-first orientation | Replaced archive-first opening, defined carrier/H1, marked the opened-D display as source-dependent illustration, and added a fourteen-card primary-source concordance. |
| R4: norm/scalar nonimplication | Added the norm-product inequality and explanation before the theorem, plus a nonalignment caveat before the rank theorem; linked the useful boundary application to the same norm upper bound. |
| R5: one-sided obstruction visibility | Labeled the appendix and linked its exact q-norm obstruction beside the full-array identity; explicitly separated boundary control from the unproved compression residual. |
| R6: clocks and seed criterion | Distinguished integer time from prime-index stage and explained the joint cylinder-cost/oscillation tradeoff. |

Additional presentation improvements: rewritten abstract, compact notation guide, map on a dedicated page without breaking a paragraph, and updated revision-specific provenance. All original formal statements and proof blocks are unchanged.

Round-1 output: [main_round1.pdf](paper/main_round1.pdf), 27 pages, SHA-256 `936865ab77a2c28eafc4746930cfba106cea945c01186bf67f4e9d0b98bbc80d`. Automated checks: 100 protected files unchanged; 25 formal blocks byte-identical; 12 bibliography entries unchanged; 26 embedded font entries; no undefined-reference/citation, missing-glyph, overfull, or underfull warning. These checks do not verify mathematical correctness.

## Round 2

Full, unedited re-review: [ROUND2_RAW.md](reviews/ROUND2_RAW.md). The reviewer found all six R1 recommendations substantively addressed. Two remaining suggestions were applied: the cylinder discussion now explicitly allows other exact routes to seed hitting, and ambiguous “coefficient lengths” is replaced by “coefficient-vector norms.” The former was a scope correction; the latter was a terminology clarification.

The primary also removed an inaccurate count of result roles, shortened display headings to avoid crowded contents entries, compressed repeated closing/provenance text, and restored missing spaces before several citations outside proof blocks. No original formal block or displayed mathematical expression was changed.

Round-2 build tooling initially encountered a stale bibliography lookup because the first round's copied `.bbl` was visible outside the new build directory. The builder now stages only source files in a fresh source directory before compiling to a separate fresh output directory. It checks every required artifact before replacing the delivered PDF. A prose line with loose justification was rephrased; no warnings were suppressed. These were build/presentation fixes, not mathematical changes.

The first clean round-2 candidate had 26 pages, SHA-256 `c660680d090358c9fc84dcbff7510f23702b27f1e3bda4d8730d7b3a85b297b4`. Independent all-page visual review found two presentation defects despite the warning-free compiler log: Table 1 floated above its subsection heading, and Appendix B ended on a six-line spillover page. The unedited findings are preserved in [VISUAL_INITIAL_RAW.md](reviews/VISUAL_INITIAL_RAW.md).

Both were repaired within round 2: Table 1 now has fixed in-place placement, and redundant provenance prose was compressed without dropping its evidence limitations. Final [main_round2.pdf](paper/main_round2.pdf) and [main.pdf](paper/main.pdf) are 25 pages, SHA-256 `6e98a74c09d0a12f8fadd143d9380e71052a6378a65c62670c1cf4f248e17e16`. Checks confirm 100 protected files unchanged, 25 formal blocks identical, all 91 original displayed-math blocks retained exactly, 12 resolved bibliography entries, 26 embedded fonts, and zero final layout/reference/glyph warnings. The References heading and contents entry both point to page 25.

All final pages were rendered at 105 dpi with a hash-bound manifest. The [final independent visual report](reviews/FINAL_VISUAL_RAW.md) records PASS with no blocking defects: six changed pages freshly inspected and nineteen exact-byte matches carried forward from prior individual inspection. The map's small labels and some narrow-column hyphenation remain nonblocking cosmetics. Details are in `QA_REPORT.md`; compilation and hashing alone are not represented as visual or theorem verification.

## Preserved artifacts

- [Original English PDF](paper/main_round0_original.pdf) — unmodified v0.1.
- [Round 1 PDF](paper/main_round1.pdf).
- [Final round 2 PDF](paper/main_round2.pdf), identical to `paper/main.pdf`.
- [Pre-fix visual candidate](paper/visual_candidate_26p.pdf), retained with its initial visual report.
- The original English and Chinese source folders remain untouched; baseline hashes are recorded in `baseline_lock.json`.
