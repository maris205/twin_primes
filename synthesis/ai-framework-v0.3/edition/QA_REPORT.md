# QA report — AI-framework English v0.3

Date: 12 September 2026. Scope: author-directed editorial revision and presentation/preservation checks. This is not theorem certification, empirical AI evaluation, novelty review, or submission approval.

## Artifact identity

- PDF: [paper/main.pdf](paper/main.pdf); identical bytes in [main_round2.pdf](paper/main_round2.pdf).
- Title: A Source-Traceable Framework for AI-Assisted Research on the Twin Prime Conjecture.
- Author: Liang Wang.
- Affiliation: School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China.
- Email: wangliang.f@gmail.com.
- PDF SHA-256: 916693565d81741756af7fcd6151a9e583b1f96a03cd50d2628149be745e0f41.
- 30 pages: through Conclusion, pages 1–27; appendices, page 28; references, pages 29–30.
- No venue-specific template or page limit has been requested. This is an attributed research-framework draft, not an anonymous conference submission.

## Mechanical checks completed

Normal and optimized Python checks produced identical successful results; see [validation.json](validation.json).

| Check | Result and scope |
|---|---|
| Current source–PDF binding | Build manifest records 20 TeX/bibliography/map files and the final PDF hash; current files match. |
| Protected files | 156 selected files unchanged, including every file in the preceding English v0.2 directory, original language editions, mathematical core sources, and selected wiki records/cards. |
| Formal mathematics | All 25 formal statement/proof blocks and all 92 displayed mathematical blocks from v0.2 retained exactly. This is textual preservation, not proof validation. |
| Bibliography | All 12 old entries unchanged; three appended entries cited; 15 entries resolve. The two new external references have a targeted primary-page check, not a systematic survey. |
| References and layout logs | Zero unresolved references/citations, multiply defined labels, missing-character warnings, overfull boxes, or underfull boxes in the final build. |
| Fonts | All 26 reported font entries embedded. |
| Authorship | Full supplied title-page name, school, university, address, and email present; PDF author metadata is Liang Wang. |
| Versions | v0.2 baseline PDF retained; first revision is 32 pages; the 31-page visual candidate is also retained; the corrected final is 30 pages. |
| Map | Original English map image retained unchanged; no map connection is treated as theorem evidence. |
| Portable source package | 21 source/build-instruction members, with verified hashes; independent scratch build passes and gives identical extracted PDF text/layout. |

The [portable build receipt](portable_build.json) records both PDF hashes. Build-time metadata can change the rebuilt PDF's bytes; byte identity across TeX installations or build times is not claimed. The source ZIP hash is a1c73088829d00c7995cfc98e4f172e21e76c56fd988e7409a0225a33392a118.

## Editorial review

Two bounded read-only editorial rounds were performed through the available inherited-model reviewer. The named GPT-5.4 MCP channel was unavailable. No numerical score, full-archive audit, externally verified model identity, or fabricated experimental result is reported.

- [R1 raw report](reviews/ROUND1_RAW.md): six recommendations on framing, concrete source records, bounded protocol, precise agenda, evaluation design, and edition-specific authorship/preservation.
- [R2 raw report](reviews/ROUND2_RAW.md): five residual fixes on task-blind record construction, record-package versus format attribution, aggregate token accounting, scoped intermediate mathematical progress, and the correct name of the weighted pair sum.
- [Complete implementation log](paper/PAPER_IMPROVEMENT_LOG.md): both full raw reports and changes.

The introduction's two-line continuation page in R1 was removed by shortening the reading guide. No proof or earlier display was changed.

## Final visual inspection

The initial [31-page visual report](reviews/VISUAL_INITIAL_RAW.md) found a four-line disclosure spillover page. The disclosure was reflowed onto page 28 by tightening Appendix B, preserving its scope; the agenda heading was also shortened to avoid a broken word. The [31-page candidate](paper/visual_candidate_31p.pdf) and its [render manifest](render_manifest_31p.json) remain available.

The corrected 30-page PDF is rendered and hashed in [render_manifest.json](render_manifest.json). The [final raw visual report](reviews/FINAL_VISUAL_RAW.md) finds no blocking visual defects. The reviewer directly re-inspected pages 2 and 25–30 and independently checked byte-for-byte equality for the other 23 page images against their previously inspected versions. Thus every final page 1–30 has recorded individual visual coverage, with no credit transferred across changed images. See the [image comparison](render_delta.json) and [hash-bound visual receipt](visual_receipt.json).

Nonblocking observations: the smallest map labels require enlargement, as the caption states; the final bibliography page has two complete entries and is sparse. This is not an accidental near-empty prose continuation. Visual checks do not certify source fidelity, mathematical truth, citation accuracy, hyperlinks, or accessibility.

## Remaining scientific and resource limits

The framework is an existing file-based resource plus a specified human-supervised task/review protocol. Fully automatic enforcement, kernel-checked proof dependencies, and improved AI reliability or efficiency are not demonstrated. The prospective [plan](refine-logs/EXPERIMENT_PLAN.md) and [tracker](refine-logs/EXPERIMENT_TRACKER.md) have no executed runs. Model/provider, compute budget, adjudicators, numeric tolerances, and a final test-size rationale remain unselected.

Both analytic gates remain open, with no full-scalar fixed-power credit; the distinguished-seed joint bound remains unverified. A scoped method obstruction is not a universal impossibility theorem. The agenda does not restart stopped norm methods or authorize a new numbered TPC paper.

Wiki coverage and compatibility numbers are attributed to the existing report, not rerun here. The report records 590 formula-display failures involving 188 expressions and no desktop Obsidian test. The source archive and wiki have not been newly reviewed in full for semantic correctness.

Authorship was supplied by the user and applied to this edition. It is not an archive-wide proof attestation, institutional endorsement, or claim of first discovery of every cited result. Funding, external literature positioning, and novelty assessment remain outstanding.
