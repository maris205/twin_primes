## Round 2 re-review

**All six R1 recommendations are substantively addressed in the revised exposition.** One newly added sentence still warrants a small scope correction; one terminology edit is optional. I found no reason within this editorial review to request new mathematics, experiments, or a broader historical audit.

### Remaining actionable findings

**R2-1 — Medium editorial severity: do not make the sufficient cylinder criterion mandatory for every representation.**

**Anchor:** [dynamics.tex:92](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/dynamics.tex:92), immediately after the coarse/fine-cylinder discussion.

The new paragraph ends:

> “This is the precise pointwise issue that an auxiliary representation would also have to resolve.”

Its immediate antecedent is the joint cylinder inequality involving \(\sqrt{q_N}V_N\) and \(\Omega_N\). Consequently, the sentence can suggest that every auxiliary representation must establish that particular criterion. This is stronger than the correctly stated sufficient-only scope at line 90 and the allowance for another exact arithmetic readout in `bridges.tex`.

**Smallest fix:** Replace only the last sentence with:

> Any auxiliary representation must still establish the distinguished-seed conclusion, but need not use this particular cylinder criterion.

**Optional compression:** Since the rest of paragraph 92 repeats the preceding quantitative explanation, the whole paragraph could instead become:

> Within this cylinder criterion, both error terms must be controlled on the same unbounded sequence. Other exact routes to a distinguished-seed hitting theorem remain possible.

Either version preserves the theorem and proof unchanged. The first is the minimal scope correction; the second also reduces repetition.

---

**R2-2 — Low editorial severity, optional: use “coefficient-vector norms” rather than “coefficient lengths.”**

**Anchor:** [barriers.tex:2](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/barriers.tex:2).

The opening asks whether the saving follows from “the operator norm and coefficient lengths alone.” Here “lengths” means Euclidean norms, but the following Kloosterman section uses array lengths to mean support lengths. Those are materially different inputs in this manuscript.

**Minimal replacement:**

> …from the operator norm and coefficient-vector norms alone?

No mathematical change is needed.

### Verification of the six R1 items

| R1 concern | Verification in the revised text |
|---|---|
| Analytic output versus TPC endpoint | **Addressed.** The notation sheet distinguishes the counting objects and auxiliary scalars; the introduction identifies the imported output and separate Gate A premise. The ledger explicitly labels analytic Gate B and retains the imported-interface limitation. |
| Conditional production attachment | **Addressed.** The structural opening, occurrence subsection, new closing transition, and conclusion distinguish identities, supplied lifts, actual support, coverage, and transport cost. The operator section is explicitly not presented as a consequence of a constructed production lift. |
| External-reader orientation | **Addressed.** The introduction is organized by mathematical roles. “Carrier” and the inherited H1 label are explained. The opened-\(D\) display is introduced as an illustration of required source data, not a self-contained estimate. |
| Norm bound versus actual signed scalar | **Addressed.** The norm-product inequality and its nonimplication appear before the theorem. The rank caveat precedes the rank result. The subsequent boundary explanation also shows why the norm upper bound remains useful. |
| One-sided Kloosterman obstruction and boundary scope | **Addressed.** [emitter.tex:36](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/emitter.tex:36) gives the labeled appendix cross-reference and explicit \(q\)-scale obstruction. [boundary.tex:50](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/boundary.tex:50) distinguishes the boundary bound from the unproved compression condition and its residual. |
| Integer-time versus prime-stage dynamics | **Addressed.** [dynamics.tex:95](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/dynamics.tex:95) explicitly changes clocks and disclaims an \(\Omega_N\) estimate or seed-\(0\) hitting theorem. R2-1 concerns the preceding new summary, not this correction. |

The known “four distinct uses” problem is **already resolved in the latest text read**: [introduction.tex:12](/root/autodl-tmp/math_research3/tpc_english_revision/paper/sections/introduction.tex:12) now says “The main results serve distinct roles.”

### Shortened headings and compressed closing material

I have no source-scope objection to the shortened headings observed during this review. The substantive qualifications remain in the local statements and surrounding prose; they need not all be repeated in display titles.

The latest compressed conclusion retains the separate analytic and distinguished-seed obligations, conditional production scope, and explicit non-TPC conclusion. The shortened wiki-provenance paragraph correctly retains the distinction between navigational synthesis and primary proof evidence. Neither needs expansion merely to repeat those cautions.

I would retain the existing local safeguards concerning:

- coefficient-blind bounds versus the actual scalar;
- signed recombination and diagonal removal;
- boundary contribution versus full compression;
- almost-everywhere hitting versus the prescribed seed.

Additional general disclaimer paragraphs are unnecessary.

## Verification scope and limits

**Read completely this round:**

- `twin_primes/AGENTS.md`.
- Revised `paper/main.tex`, `math_commands.tex`, and `notation.tex`.
- All 12 revised section files: abstract, introduction, arithmetic, structure, operator, barriers, emitter, boundary, dynamics, bridges, models, and provenance.
- `reviews/ROUND1_RAW.md`, `REVISION_PLAN.md`, `WIKI_REVISION_CROSSWALK.md`, and the revision-root `README.md`.

I also examined baseline-to-revision textual differences for the abstract, introduction, dynamics, bridges, and provenance sections, and checked the subsequently visible shortened headings and relevant wording. The primary-source checks from R1 remain background evidence; I did not reopen the full card/source corpus this round.

This report concerns the source text read, including late wording changes. I did **not** independently verify the supplied PDF hash, 27-page count, 25-block preservation result, 100 protected-file result, or 12-entry bibliography preservation result. Nor did I establish that the subsequently edited source corresponds byte-for-byte to the intake PDF.

No writes, builds, checkers, experiments, delegation, external uploads, release commands, excluded-repository access, or PDF visual inspection occurred.

**Handoff:** correct R2-1; apply R2-2 if convenient. These are sufficient remaining editorial actions from this review—not a novelty, submission-readiness, or complete mathematical certification.
