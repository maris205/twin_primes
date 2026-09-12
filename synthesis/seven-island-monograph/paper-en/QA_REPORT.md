# English-edition quality assurance

Date: 12 September 2026. Scope: complete English translation and document presentation, not new research, novelty assessment, or certification of the twin-prime conjecture.

## Artifact and preservation checks

- PDF: 24 A4 pages; SHA-256 `cbe2587a122816583141e68dea7ec352769f237e2519b50d1255b20b9e855867`.
- Complete coverage: abstract, nine main sections, two appendices; each of the twelve section files has the same labels, citation occurrence counts, formal-statement types/counts, and proof counts as its Chinese source.
- Resolved bibliography: 12 entries; cross-reference labels: 30. The bibliography is byte-identical to the Chinese edition.
- Compiler's final log: zero undefined references/citations, missing glyphs, overfull boxes, or underfull boxes. All 25 PDF font entries are embedded. The full build output and final LaTeX log are retained as `compile.log` and `main.log`.
- Chinese baseline: all 30 files unchanged, checked against `chinese_baseline_lock.json`. Chinese PDF SHA-256 remains `687fb29ea34d0f339564b2a1a790135f71cb73303e6f793edf9ec5a9d3db9b55`.
- The 24 core source files and indexed source hashes for 420 directories pass the existing read-only source-integrity check. This is hash verification, not semantic review of all 420 directories.
- User's English map: unchanged; SHA-256 `83c729864e69fc87569ec23ad0b1c7d6251fedd3b61f059881d17fec37ef24fa`.
- Every final PDF page was rendered at 105 dpi. `render_manifest.json` binds the 24 individual page images to the exact final PDF hash.

## Editorial changes during English preparation

The `paper-write` workflow governed full-section translation, preservation of proof and claim scope, and independent cross-review; `paper-compile` governed build and presentation checks. The user's long-form translation request takes precedence over conference-template and nine-page defaults. The skill's named GPT-5.4 reviewer was unavailable; the independent review uses the available inherited-model agent, not a claimed GPT-5.4 run. No numerical review score is invented.

Initial compilation found an overlong English specification tuple, a marginally overlong norm-product sentence, and poorly justified narrow table cells. The tuple and norm product were displayed across suitable lines, the weighted-norm wording was clarified without changing its bound, and the table's narrow columns were made ragged-right. A final provenance note was shortened to prevent a one-line paragraph continuation above the bibliography. No Chinese file was edited.

The English map is reproduced intact. Its caption explicitly qualifies schematic isomorphism/saving/asymptotic labels and distinguishes the two map bridges from repository gate names. Small image labels may require zooming; the full-resolution original is linked in the README. Markdown is a convenience conversion with Pandoc citation keys and cross-reference annotations, not a substitute for the numbered PDF.

## Independent review records

These are bounded reviews of this edition, not a replay of the Chinese edition's two-round research review.

### Translation fidelity

The independent reviewer read all twelve complete Chinese/English section pairs, both masters, macros, and bibliographies. It found no critical or major discrepancies and no dropped mathematical proof step. Its two minor recommendations were both applied: restoring an explicit terminal-equation reference and restoring the introduction's source-navigation sentence. The complete initial report is preserved unchanged in [TRANSLATION_REVIEW_RAW.md](TRANSLATION_REVIEW_RAW.md). After notice of the fixes, the reviewer responded: “Acknowledged. With both minor fixes applied, the translation-fidelity audit is complete with no remaining semantic blockers identified. No further review or changes performed.”

The review compares current working-file editions, not the Chinese synthesis against Git HEAD (the synthesis is not yet committed). Preservation of the Chinese files is separately established by the primary's byte-hash baseline. No fresh external literature verification or historical-theorem review is claimed.

The final pagination check found that the References contents entry pointed to page 23 although the heading began on page 24. An explicit page break before the bibliography anchor corrected the contents entry and link, without changing the 24-page length. The automated English checker now verifies the contents/heading page match.

### Final all-page visual review

The independent reviewer verified all 24 pages of the final hash above, reusing earlier inspections only where page-image hashes matched exactly and freshly inspecting changed images. Verdict: **PASS WITH MINOR COSMETIC ISSUES; no blocking visual defects.** The full unedited report is retained in [VISUAL_REVIEW_RAW.md](VISUAL_REVIEW_RAW.md).

Remaining cosmetic issues are hyphenated long headings, tight spacing before some numerical citations, and the map float intervening in a paragraph across pages 3–5. No text is missing. The map's small labels require enlargement; native image dimensions and embedded RGB pixels were independently checked against the companion. No clipping, formula overlap, blank page, or unreadable table was found. These minor findings are retained rather than represented as a warning-free visual review.

Final automated checks passed in both normal and optimized Python modes with identical results. Work remains local only: no staging, commit, or push was performed. The Chinese edition and historical archive remain unchanged.
