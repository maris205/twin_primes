# English v0.2 quality assurance

Date: 12 September 2026. Scope: wiki-informed editorial revision and document presentation. No research route was resumed; no new numbered TPC paper or proof of the conjecture is claimed.

## Final artifact and preservation

- Final PDF: 25 A4 pages, 3,639,363 bytes. SHA-256 `6e98a74c09d0a12f8fadd143d9380e71052a6378a65c62670c1cf4f248e17e16`.
- `paper/main.pdf` and `paper/main_round2.pdf` are identical. The original 24-page English v0.1 and 27-page round 1 are preserved separately.
- All 100 protected files are unchanged: the original English and Chinese editions, selected primary sources, selected source catalogs, and fourteen wiki cards. Each of the 24 core primary-source hashes also matches the inherited source matrix.
- All 25 original formal statement/proof blocks are byte-identical. All 91 original displayed-math blocks remain unchanged. Added prose, notation, cross-references, and the explicit norm-product inequality do not introduce a new theorem.
- Bibliography, macros, and the user-supplied map are unchanged. Twelve bibliography entries are resolved; all 26 PDF font entries are embedded.
- Final compiler log: zero undefined references/citations, missing-character warnings, duplicate labels, overfull boxes, or underfull boxes. The References contents entry and heading both point to page 25.
- Normal and optimized Python validation produce identical results; explicit guards do not depend on Python assertions.

These checks establish preservation and presentation properties, not theorem correctness. In particular, retaining proof text does not constitute independent verification of that proof.

## Editorial review

Two bounded independent read-only reviews were conducted using the available inherited-model agent. The skill's named GPT-5.4 MCP channel was unavailable; no such review or score is claimed. The full reports are preserved in [round 1](reviews/ROUND1_RAW.md) and [round 2](reviews/ROUND2_RAW.md).

All six round-1 recommendations were addressed. Round 2 identified a sufficient-only scope issue in the new cylinder summary and an ambiguous use of “lengths”; both were corrected using the reviewer's suggested wording. The final headings/provenance were additionally shortened for presentation. See [the revision log](PAPER_IMPROVEMENT_LOG.md) for the exact changes and limitations of each review.

## Independent visual inspection

The first 26-page round-2 candidate was inspected individually on every page. Despite clean compiler diagnostics, the reviewer found a detached Table 1 subsection heading and a six-line Appendix B spillover page. Both findings are retained in [the initial visual report](reviews/VISUAL_INITIAL_RAW.md). Fixed table placement and a shorter provenance section produced the 25-page candidate above.

The final PDF is rendered at 105 dpi; `render_manifest.json` records its exact hash and the image hash for every page. The independent [final visual report](reviews/FINAL_VISUAL_RAW.md) gives **PASS, no blocking visual defects**. Every final page is covered: pages 2, 7, 8, 9, 24, and 25 were freshly inspected individually; the other 19 pages reused prior individual inspection only after exact-byte and hash matches. The reviewer rechecked the final PDF hash after inspection.

Both initial findings are resolved. Remaining nonblocking cosmetics: small labels in the unchanged map require enlargement, and the narrow island-table column hyphenates some words. These are retained honestly rather than represented as a perfect visual layout. Visual QA does not independently certify theorem correctness, source fidelity, citation accuracy, hyperlink operation, or accessibility; font embedding and local companion-link existence were checked separately by the primary.

## Portability and limitations

The source-only ZIP includes all 18 required source/instruction files plus a member-hash manifest. Every ZIP member has been checked against the current source bytes. It was extracted to a fresh directory and independently rebuilt using only those packaged files; the rebuilt PDF's complete layout-preserving text extraction is byte-identical to the delivered PDF's extraction. The historical archive and wiki are intentionally not bundled; they remain available in the workspace through the source concordance.

Authorship, venue selection, systematic external literature positioning, novelty assessment, and a complete independent mathematical audit are not supplied by this editorial task. The wiki was used to organize dependencies, not as independent proof evidence. The analytic signed estimates and distinguished-seed bridge remain unproved.

All changes are local to the separate revision directory. No staging, commit, push, external manuscript upload, notification, or original-source rewrite was performed.
