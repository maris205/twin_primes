## R2 editorial audit

R1 is substantially implemented in the selected text. The author block and PDF author metadata match the supplied identity; the affiliation, postal address, and email are correct, with conventional spacing. The framework now has concrete K02/K13/K14 examples, explicitly separates existing resources from proposed automation, and makes no measured AI-benefit claim. The new prose retains the separate analytic gates, strict loss thresholds, and sufficient-only distinguished-seed criterion.

Five residual wording/design-contract issues remain. None requires changing the preserved formal mathematics or executing experiments.

### Residual findings

1. **Make the record-construction rule consistent with the answer-leakage rule.**

   The plan excludes summaries that directly reveal held-out answers, while S2 receives scope records containing precisely the conclusions tested by conditional-status and hypothesis-retention questions. As written, that rule could either remove the intended intervention or permit test-specific answer annotations under the name “scope record.” [Experiment plan]( /root/autodl-tmp/math_research3/tpc_ai_framework/refine-logs/EXPERIMENT_PLAN.md:35), [Agenda]( /root/autodl-tmp/math_research3/tpc_ai_framework/paper/sections/agenda.tex:19)

   **Fix:** distinguish admissible source-derived records from test-specific answers and adjudication rubrics. Require record construction to be task/rubric-blind, freeze the records before held-out evaluation, and keep test questions, planted-error locations, reference answers, and reviewer rationales out of every accessible index. The K02/K13/K14 examples already disclosed in the paper should be development illustrations, not evidence of undisclosed-task generalization.

2. **Clarify what the fixed-review ablation can attribute to the records.**

   S2-minus-records retains underlying source text, but that is not necessarily information-equivalent to human-curated conclusions and scope explanations. The comparison can test the value of **supplying the curated record package**; it cannot by itself distinguish organization/format from the additional explicit guidance supplied by that package. This matters because the plan promises matched information and rejects extra context as an alternative explanation. [Claim map]( /root/autodl-tmp/math_research3/tpc_ai_framework/refine-logs/EXPERIMENT_PLAN.md:20), [B2]( /root/autodl-tmp/math_research3/tpc_ai_framework/refine-logs/EXPERIMENT_PLAN.md:60)

   **Fix:** either limit the mechanism claim to the complete source-derived record intervention, or specify an information-matched control containing the same record facts and wording in unstructured form. The first option is sufficient for this prospective edition and requires no additional baseline family. Keep the stronger “structure itself helps” interpretation conditional on the second design.

3. **Correct the token-budget upper-bound definition.**

   B1 correctly says retrieved context and review inference are charged to the budget, but the budget section defines \(t\) as a “per-output token cap.” An output-only cap does not bound input/context tokens or the repeated inputs to review calls, so \(n\times s\times k\times t\) is not the stated total inference upper bound under that reading. [B1 setup]( /root/autodl-tmp/math_research3/tpc_ai_framework/refine-logs/EXPERIMENT_PLAN.md:54), [Budget]( /root/autodl-tmp/math_research3/tpc_ai_framework/refine-logs/EXPERIMENT_PLAN.md:96)

   **Fix:** define \(t\) as the aggregate input-plus-output token cap across **all model calls for one task–condition–repeat**, including retrieval context and review; account for separately metered reasoning tokens where applicable. Describe equal caps as matched allowances and report actual usage separately. No provider selection or numerical budget is needed now.

4. **Do not make a full Gate B saving a prerequisite for every useful mathematical continuation.**

   The agenda currently says “a useful continuation must…” and then “It must yield a full-scalar saving.” That is too broad for Islands 2–4: a genuinely useful scoped attachment lemma or coefficient-sensitive intermediate result need not itself close Gate B. The existing boundary result illustrates that distinction. [Mathematical agenda]( /root/autodl-tmp/math_research3/tpc_ai_framework/paper/sections/agenda.tex:5)

   **Fix:** use wording such as:

   > A continuation intended to satisfy Gate B must ultimately yield a full-scalar saving … Intermediate results should state precisely which attachment or loss obligation they resolve.

   Retain the existing restrictions on reopening stopped generic-norm methods. This corrects the scope of the agenda without weakening the gate’s mathematical requirements.

5. **Correct the description of \(S_2(x)\).**

   The agenda calls \(S_2(x)\) “the prime-pair counting function.” In the preserved baseline it is the **von Mangoldt-weighted pair sum**; \(\pi_2(x)\) is the prime-pair count. The distinction is particularly important in a framework whose examples emphasize object identity. [Agenda]( /root/autodl-tmp/math_research3/tpc_ai_framework/paper/sections/agenda.tex:7)

   **Fix:** replace that phrase with “the von Mangoldt-weighted pair sum \(S_2(x)\).” The surrounding warning that the complete upstream implication is not reconstructed is already correct.

### Actual read scope and limits

I read all thirteen selected files completely, as encountered during this audit:

- `paper/main.tex`.
- `paper/sections/{abstract,introduction,framework,agenda,conclusion,bridges,provenance}.tex`.
- The complete `paper/references.bib`, including all three appended entries.
- `REVISION_PLAN.md` and `FRAMEWORK_SOURCE_MAP.md`.
- `refine-logs/EXPERIMENT_PLAN.md` and `refine-logs/EXPERIMENT_TRACKER.md`.

I also reread `twin_primes/AGENTS.md` and reused the previously read mathematical baseline, wiki evidence, handoff entry, and island-map guide. The appended bibliography entries were inspected as text; their external primary sources were not independently reverified in R2.

I did not inspect the PDF, reproduce the reported validation, or independently establish preservation. The known introduction widow page is excluded from these findings as requested. No writes, builds, checkers, agents, Git operations, uploads, or old-tree access occurred.

Within this scope, the remaining issues concern precise wording and the prospective evaluation contract—not an asserted TPC proof, completed automation, or empirical validation.
