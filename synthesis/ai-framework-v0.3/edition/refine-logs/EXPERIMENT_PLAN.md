# Experiment Plan

**Problem**: AI assistance across the TPC archive can lose object definitions, hypotheses, source relationships, and conditional status.
**Method thesis**: A source-derived scope-record package and a bounded output/review contract may improve the fidelity of source-grounded answers. The intervention includes explanatory guidance, not merely its format.
**Date**: 12 September 2026.
**Status**: PROSPECTIVE / NOT_RUN. This is a planning artifact, not permission to launch model calls, upload the archive, restart mathematical routes, or purchase compute.

## Context and claim ceiling

The user asked to recast the paper as a framework suitable for AI-assisted TPC research and add a next-step agenda. There is no prior FINAL_PROPOSAL or empirical evaluation to inherit. Existing sources are the preserved English v0.2, the linked wiki, selected knowledge cards, and the current handoff. The new paper specifies the framework; it does not show that AI has solved an open bridge.

Dominant contribution: a concrete file-based resource linked to a scope-preserving task contract. Frontier-model superiority, autonomous discovery, and archive-wide proof verification are not claimed. No model, provider, hardware, timeline, spending limit, or human-evaluation allocation has been selected.

## Claim Map

All claims below are hypotheses to test, not claims established in the manuscript.

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1: A source-derived scope-record package reduces unsupported claim promotion without unacceptable loss of correct-answer coverage. | Tests the complete record intervention: retaining exact objects, quantifiers, and unpaid obligations. | Human-adjudicated held-out tasks, the same underlying source corpus and matched inference allowances, paired estimates with source-family uncertainty, and an unchanged-review ablation. A coverage tolerance must be fixed before test evaluation. | B1, B2 |
| C2, optional: The same contract reduces human correction effort at comparable mathematical fidelity. | Tests practical handoff value without using raw speed as a substitute for correctness. | Blinded review timing and a fixed correction rubric on the same outputs; report uncertainty and disagreements. | B3 |

Anti-claims to rule out: gains are entirely due to larger token allowances, extra inference/review passes, test-specific answer leakage, selective abstention, or duplicate source families counted as independent data. Source-derived explanatory guidance is part of the intervention; the basic record-deletion comparison cannot attribute a gain to formatting alone.

## Paper Storyline

- Main paper empirical extension would need B1 plus B2 before claiming improved AI reliability.
- B3 is optional, supporting workflow usability rather than mathematical progress.
- The present edition contains no result table because no runs have occurred.
- Cut: whole-archive proof-success rates, unadjudicated automated theorem labels, an autonomous-TPC endpoint experiment, broad model leaderboards, or extra agent hierarchies without a specific hypothesis.
- The chosen primitive is a language-model assistant over source documents. No claim that a frontier model is necessary is made; a model-generation comparison is not required to test this information-contract mechanism.

## Shared data and evaluation contract

1. Select bounded tasks from a small set of source families with fully inspected source spans. Candidate families include the physical operator, analytic loss interface, and distinguished-seed criterion, but three families alone would not justify broad statistical generalization.
2. Build human-adjudicated answer rubrics: required object/hypotheses, accepted source spans, permitted conclusion, and explicit disallowed promotions. Do not treat historical review labels as gold proof verdicts.
3. Assign development and test splits at the underlying source-family level and trace shared upstream sources across papers and cards. Construct admissible source-derived records task/rubric-blind, before seeing test questions, planted-error locations, reference answers, or reviewer rationales. Freeze those records before evaluation. Exclude test-specific answer annotations and adjudication materials from every accessible index; log all exclusions and duplicate-family decisions. The disclosed K02/K13/K14 examples are development illustrations, not held-out generalization evidence. Source-derived factual records are the intended intervention; they must not be rewritten after seeing the test.
4. For planted-error tasks, change separate test copies only. Preserve the original archive and wiki. Include strict-inequality changes, dropped residuals, bridge-name confusion, and almost-everywhere versus seed-0 substitution.
5. Freeze the admissible evidence corpus, prompts, budgets, model identifier/version, decoding settings, retrieval configuration, review opportunities, rubric, and abstention policy before evaluating the held-out test set.
6. Use condition-blind human mathematical adjudication. Retain disagreement records and report inter-rater agreement. Human confirmation is needed for source-to-answer correctness; no output is promoted to a mathematical theorem by the scoring pipeline.
7. Primary outcomes: task-level unsupported-promotion rate together with correct-answer coverage and hypothesis retention. Also report unsupported factual claims among attempted claims, so answer length cannot hide the error pattern.
8. Secondary outcomes: source-span precision/recall, calibrated abstention, human correction effort, tokens, tool calls, and latency. Universal abstention is not success.
9. Use paired task comparisons and source-family cluster bootstrap intervals when the number of independently adjudicated families permits it. Report raw counts and limitations for a small pilot. Three repeated decoding seeds, if budget permits, characterize model variance; they do not triple the number of independent mathematical tasks.

## Experiment Blocks

### B1: Main fidelity comparison

- Claim tested: C1.
- Why: establish whether the full contract helps the intended bounded tasks.
- Dataset/split/task: frozen source-family split; source localization, hypothesis-preserving reconstruction, conditional-status classification, and planted scope-error detection.
- Compared systems: three baseline families only: S0 unstructured source access; S1 ordinary retrieval; S2 retrieval plus structured scope records and bounded output contract.
- Metrics: unsupported promotion, correct-answer coverage, hypothesis retention; then source accuracy and abstention.
- Setup: identical fixed model/version and admissible underlying evidence; no training. Match token/tool limits and review opportunities. Record retrieval settings and charge both retrieved context and review inference to the budget. Three decoding seeds if affordable; deterministic settings documented otherwise.
- Success criterion: lower unsupported promotion with uncertainty and no coverage loss beyond a predeclared tolerance. A numeric tolerance and minimum test size must be set using development data and human requirements before test access.
- Failure interpretation: no demonstrated reliability benefit; investigate task sensitivity, leakage, weak record quality, or a true null effect. Do not relabel documentation coverage as experimental success.
- Table target: paired fidelity/coverage table with task and source-family counts.
- Priority: MUST-RUN before empirical reliability claims.

### B2: Mechanism and simplicity ablation

- Claim tested: C1 and the extra-compute anti-claim.
- Why: separate scope records from ordinary retrieval and additional review effort.
- Dataset/split/task: the same frozen tasks as B1.
- Compared systems: S2 and S2-minus-records, with identical output fields, underlying source access, inference limits, and review passes; also S2-minus-review, at a separately declared budget condition. These are ablations within S2, not new baseline families. The deletion comparison tests supplying the complete source-derived record package, including curated explanations. A claim about structure/format itself would require an additional information-matched control containing the same record facts and wording as unstructured text; that stronger claim is not required here.
- Metrics: the B1 primary metrics plus record-maintenance and inference cost.
- Setup: no new training or model; no test-driven prompt tuning; preserve run IDs for paired outputs. Removed information remains accessible as underlying source text.
- Success criterion: evidence that supplying the record package matters at fixed review opportunity; do not attribute the result to format alone. If review can be deleted without harmful loss, prefer the simpler contract.
- Failure interpretation: adopt the simpler system or attribute any difference to review/compute instead of the record mechanism. Do not claim novelty from the ablation alone.
- Table target: compact deletion-study table, with error categories in the appendix.
- Priority: MUST-RUN for the mechanism claim.

### B3: Failure analysis and handoff effort

- Claim tested: optional C2.
- Why: test whether preserved scope translates into usable handoff, and identify remaining failure modes.
- Dataset/split/task: condition-blind review of a preselected subset of B1/B2 outputs; retain errors and abstentions, not just successes.
- Compared systems: outputs from S0, S1, S2; no new model family.
- Metrics: human minutes to an accepted scoped answer, required corrections, unresolved cases, and the B1 fidelity rubric.
- Setup: fixed instructions and timing protocol; randomized output order; separate answer adjudication from the identity of the producing condition.
- Success criterion: reduced correction effort at comparable fidelity, with uncertainty; no numeric effect is presumed.
- Failure interpretation: useful organization may not save reviewer time; report the tradeoff.
- Table/figure target: optional correction-effort table and sourced qualitative error cases.
- Priority: NICE-TO-HAVE.

## Run Order and Milestones

| Milestone | Goal and runs | Decision gate | Cost and turnaround | Risk / mitigation |
|---|---|---|---|---|
| M0 sanity | Freeze selected source families, task rubrics, planted-error copies, leakage audit, and scoring tests; no scientific inference. | Stop if source support is missing, gold answers disputed, or family leakage persists. | Human preparation dominates; not yet estimated. | Small-source selection and documented disagreements. |
| M1 baseline | Pilot S0 and S1 on development tasks. | Continue only if both can access required evidence and metric logic is correct. | Two access conditions times development tasks and permitted repeats; provider/runtime unknown. | Inspect failures before freezing final configuration. |
| M2 main | Freeze test protocol and run matched S0/S1/S2 on held-out tasks. | No empirical C1 claim without fidelity plus coverage evidence. | Three conditions times test tasks and repeats; estimate after M1. | No tuning on test outcomes. |
| M3 decision | Fixed-review record ablation; optional review deletion. | Simplify if records or review add no demonstrated value. | One or two additional variants times the same task/repeat budget. | Separate mechanism from extra effort. |
| M4 polish | Optional B3, uncertainty analysis, failure documentation; separate formalization feasibility assessment. | Stop at descriptive pilot if families/resources are insufficient. | Human-review dependent; no committed completion date. | Do not inflate repeated seeds into task diversity. |

## Compute and Data Budget

- Total GPU-hours: UNESTIMATED; hardware/model not selected. No GPU use is authorized here.
- For n tasks, s repeats, k conditions/variants, and an aggregate model-token cap t for one task–condition–repeat, the inference upper bound is n × s × k × t. Here t includes input plus output tokens across every model call, repeated retrieval context, review calls, and any separately metered reasoning tokens. Equal caps are matched allowances, not equal actual usage; actual consumption is reported separately. Add the declared tool budget and human adjudication separately.
- Default stochastic repeats: s = 3 only if later budget approval permits; record any alternative.
- No API cost estimate is fabricated without a selected model/provider and measured development-run usage.
- Data preparation: source-family assignment, span-level rubrics, duplicate and summary-leakage exclusions, independent test-copy errors, fixed retrieval index.
- Human evaluation: mathematical adjudicators, a disagreement procedure, and sufficient time for condition-blind inspection. None is currently allocated.
- Biggest bottleneck: producing defensible held-out tasks and reference answers without leaking repeated source content.

## Separate mathematical and formalization agenda

These are research obligations, not experiment runs in this tracker.

- Island 2 / map Bridge A / analytic Gate B: source-exact signed interior bound or paid two-sided attachment/residual theorem, full saving δ > 1/400; the critical-array route needs ℓ < 19/2400. Gate A remains separate; boundary saving alone does not pay the interior.
- Islands 3–4: preserve production coverage and coefficient transport; existing structural interfaces are not automatically a constructed attachment.
- Island 5 / Bridge B: the sufficient cylinder criterion needs both errors on the same unbounded sequence with fixed margin. No necessity or verified joint bound is claimed.
- Island 7: exact event/time/seed attachment before any pointwise consequence.
- Selective formalization: first assess a small finite identity or cylinder averaging statement, library support, and source-to-formal correspondence; only a kernel-checked proof would count as formal evidence.
- A documented agenda does not reopen stopped norm methods or change the current handoff.

## Risks and Mitigations

- Answer leakage: construct source-derived records task/rubric-blind, freeze them, exclude test-specific answer materials, partition by shared upstream sources, and audit the complete accessible index.
- Abstention gaming: pair promotion rate with correct-answer coverage and retained hypotheses.
- Unequal compute/information: freeze and report total allowances, actual consumption, underlying source access, and review opportunities. The fixed-review record ablation tests the whole curated record intervention; do not claim a pure formatting effect without an information-matched control.
- Rubric circularity: human-source adjudication, unresolved-answer tracking, and no automatic theorem labels.
- Overgeneralization: distinguish a selected-source pilot from a benchmark of all 419 manuscripts.
- Security/privacy: no upload or external model call is authorized by this document; provider and corpus permissions require a separate execution decision.

## Final Checklist

- [x] Proposed main comparison and deletion table are specified; neither is populated.
- [x] The whole record intervention is tested in a proposed fixed-review ablation; a pure structure effect is not claimed.
- [x] Simplicity is tested by deletion; unnecessary components may be removed.
- [x] Frontier-model superiority is explicitly not claimed.
- [x] Optional runs are separated from must-run evidence.
- [ ] Human rubrics, leakage checks, and final split adjudicated.
- [ ] Model, resources, numeric tolerances, and test-size rationale selected.
- [ ] Any experiment executed.
