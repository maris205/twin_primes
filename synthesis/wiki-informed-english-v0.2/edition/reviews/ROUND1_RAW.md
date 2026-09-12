Source scan is complete. Here is the bounded round-1 handoff for the separate revision copy. **No further research or historical audit is needed to implement these recommendations.**

The baseline generally preserves the correct mathematical boundaries. The priority is to make its dependency structure clearer to external readers; one concluding sentence also needs its conditional scope restored. All anchors below refer to the reviewed `paper-en` baseline; apply changes only to the corresponding files in the preserved revision copy.

## Findings

### R1 — High editorial severity: distinguish the analytic output from the TPC endpoint earlier

**Anchors:** [introduction.tex:13](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/introduction.tex:13); [arithmetic.tex:3](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/arithmetic.tex:3); [bridges.tex:21](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/bridges.tex:21), through `eq:terminal`.

The introduction gives \(\delta>1/400\) before explaining the output it serves. Readers first meet the genuine weighted prime-pair count \(S_2\), then study the operator scalar \(\mathfrak C_x\), but only near the end encounter the imported interface’s different output \(S_x^{\rm phys}\).

**Minimal fix:** Add an early paragraph distinguishing these three quantities and explicitly identifying the stopping point:

> The conditional deduction reproduced here yields a bound for \(S_x^{\rm phys}\), not directly for the weighted prime-pair count \(S_2(x)\). The manuscript does not reconstruct the further upstream implication from this analytic output to TPC.

In the ledger, rename “Full scalar target” to **“Analytic Gate B: full scalar target.”** Keep Gate A as a separate unproved premise, and retain all strict exponent margins.

**Basis:** K02 → K13 → K11; checked V58’s imported identity and conditional endpoint compiler. This is a visibility issue, not a request to prove the missing implication.

### R2 — High editorial severity: restore conditional scope in the conclusion’s occurrence-layer summary

**Anchors:** [structure.tex:53](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/structure.tex:53), especially lines 64 and 83–85; [bridges.tex:62](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/bridges.tex:62).

The structural section carefully distinguishes conditional attachment, a supplied lift, actual active support, and transport costs. The conclusion compresses this into:

> “The fixed atom and occurrence layer fix the coefficients, support, and prefixes.”

That can be read as an accomplished production-level attachment.

**Minimal replacement:**

> The fixed-atom results preserve coefficients, masks, and prefixes on their stated source support. The occurrence results specify conditional attachment, conservation, and weighted-cover interfaces; they do not construct the production lift or pay its coefficient-transport cost.

Also announce at the start of the occurrence subsection that these are distinct interfaces, not successive completed constructions.

**Basis:** K07–K09; checked TPC205’s explicitly uninstantiated production pair-to-\(\omega\) premise, TPC143’s conservation contract, and TPC117’s transport-cost passage.

### R3 — Medium editorial severity: orient readers by mathematical dependencies before archive terminology

**Anchors:** [introduction.tex:4](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/introduction.tex:4), reading guide at line 35; [arithmetic.tex:30](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/arithmetic.tex:30); [structure.tex:38](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/structure.tex:38).

The introduction gives archive history and island tasks, but not a compact explanation of the connections between them. “H1,” “opened-\(D\),” “carrier,” and “packet” then demand repository knowledge. The displayed opened-\(D\) coefficient deliberately leaves \(r_R\) and \(B_\alpha\) as source aliases.

**Minimal fix:**

- Put a short dependency paragraph before the archive-history paragraph: structural identities and attachment requirements; the common analytic scalar and its estimates; the separate distinguished-seed route.
- Define “carrier” as an indexing set of terms or occurrences; identify “H1” as an inherited source label.
- Give the opened-\(D\) display a role-only introduction, or move that illustrative source-dependent display to the provenance appendix.

Use the wiki’s relation types—definition, exact transformation, conditional attachment, method obstruction, estimate—without copying wiki navigation machinery into the article. Keep the supplied map unchanged.

### R4 — Medium editorial severity: place the norm/scalar nonimplication before the long proofs

**Anchors:** [operator.tex:49](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/operator.tex:49), `eq:readout`; [barriers.tex:61](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/barriers.tex:61), `thm:normbarrier`, `cor:normalized`, and line 138; abstract.

The clearest explanation—“a lower bound on an upper-bound expression”—comes after substantial proof development. The statement is correct; its placement makes readers work unnecessarily to interpret the negative results.

**Minimal insertion before `thm:normbarrier`:**

> The following lower bounds concern the norm-product upper bound  
> \[
> |\mathfrak C_x|\le \|A\|\,\|w\|_2\,\|\beta\|_2.
> \]
> They do not give a lower bound for \(|\mathfrak C_x|\).

Before the growing-rank theorem, state that its negative subspaces are not identified with the actual coefficient vectors. Qualify the abstract’s negative-direction result as an obstruction to the specified low-rank norm repairs.

**Basis:** K02–K04; checked `LANE_NORM_PROOF.md`. Preserve the separate real/complex rank conventions and the mixed-scalar warning.

### R5 — Medium editorial severity: keep the one-sided Kloosterman obstruction with the analytic argument

**Anchors:** [emitter.tex:33](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/emitter.tex:33), `cond:compression`; [models.tex:1](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/models.tex:1); [boundary.tex:46](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/boundary.tex:46).

The exact one-short/one-complete obstruction is central to the two-sided attachment problem, but its proof sits beside historical model evidence in the appendix. Readers may miss its role or mistake it for a numerical observation.

**Minimal fix:** Move `models.tex` lines 1–14 beside the full-array discussion in `emitter.tex`, or add a labeled cross-reference there explicitly stating the exact \(q\)-norm conclusion. Leave historical finite/model-evidence discussion in the appendix.

Add one transition explaining that the boundary theorem pays a contribution of the original scalar; it does **not** establish `cond:compression` or construct its residual \(R_{bcq}\).

**Basis:** K05 → K13 and K06 → K13; checked `NEXT_ARITHMETIC_OBLIGATION.md`. Preserve signed recombination, diagonal removal, integration, and the nonidentification of actual arithmetic coefficients with extremizers.

### R6 — Medium editorial severity: mark the change of clock in the dynamics section

**Anchors:** [dynamics.tex:17](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/dynamics.tex:17), `thm:haar`; `prop:seed` at line 69; [dynamics.tex:91](/root/autodl-tmp/math_research3/twin_primes/synthesis/seven-island-monograph/paper-en/sections/dynamics.tex:91).

The metric/seed distinction is already well stated. The less explicit transition is from integer time \(n\) in the moving events to prime-index stage \(k\) in replication–deletion evolution. Consecutive presentation can suggest that the latter supplies progress on the missing cylinder oscillation bound.

**Minimal insertion before the stage-evolution subsection:**

> We now change from integer time \(n\) to prime-index stage \(k\). The following exact evolution and scoped carrier obstruction do not provide a bound for \(\Omega_N\) or a hitting theorem at seed \(0\).

Prefer “transfer to the distinguished seed” where “return” might suggest orbit recurrence. Keep \(\sqrt{q_N}V_N\) and \(\Omega_N\) together whenever summarizing the sufficient criterion.

**Basis:** K10 → K14 and K12 → K14; checked the source cylinder criterion and its attainability qualification.

## Read scope and limits

Read completely:

- `twin_primes/AGENTS.md`.
- `main.tex`, `math_commands.tex`, and all 12 section files: abstract, introduction, arithmetic, structure, operator, barriers, emitter, boundary, dynamics, bridges, models, provenance.
- All K01–K14 cards, including typed links and claim boundaries.
- `CORE_SOURCE_MATRIX.json` and the standalone island-map guide.
- `TPC_HANDOFF.md` lines 1–110, including its complete leading physical-return entry.

Targeted primary-source checks, using the matrix’s source identities:

| Source | Scope read |
|---|---|
| V58 | Lines 34–104, 293–330 |
| TPC18 opened-\(D\) dispersion | Lines 4–57 |
| TPC205 conditional composition | Lines 119–155 |
| TPC143 occurrence lift | Lines 83–202 |
| TPC117 weighted cover | Lines 263–303 |
| Distinguished-seed reconnaissance report | Lines 78–105 |
| `LANE_NORM_PROOF.md` | Complete, lines 1–156 |
| `NEXT_ARITHMETIC_OBLIGATION.md` | Complete, lines 1–141 |

Cards were treated as navigational synthesis, not independent proof validation. Recorded hashes were not recomputed. The supplied 24-page baseline was not visually inspected. The newly frozen 100-file package, revision copy, build tooling, and crosswalk were not separately audited.

No writes, delegation, external uploads, old-repository access, experiments, builds, checkers, or release commands occurred. This report makes no novelty, submission-readiness, or complete-proof certification.

**Recommended implementation order: R1 and R2 first, then R3–R6. All six can be addressed with local exposition and organization changes while preserving the mathematics.**
