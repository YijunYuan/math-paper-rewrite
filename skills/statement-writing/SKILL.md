---
name: statement-writing
description: "Write or revise theorem, proposition, lemma, corollary, and conjecture statements. Use to consolidate fragmented AI-generated facts, clarify quantifiers and hypotheses, or separate statements from proofs."
---

# Statement writing

Adapted from Pharos; see https://github.com/YijunYuan/math-paper-rewrite/blob/main/NOTICE.md and references/upstream.md. Treat a statement as a unit of reading, not a one-to-one copy of an internal proof record.

## Select the unit
Fold a fact into the proof of its sole consumer when it is a one-use estimate, auxiliary construction, definition unfolding, or routine specialization. Combine tightly linked facts when they yield one clean conclusion; combine cases handled by the same argument.
Keep separate the main target, results with multiple unrelated consumers, cross-section dependencies, and arguments using substantially different tools. State an imported theorem separately from conclusions derived from it. Define a named concept separately from proving its properties.

Before a merge, make a correspondence between source statements and the proposed statement. Preserve the assumptions and conclusions actually supported. If one claim needs an additional hypothesis, give it a separate statement or explicitly scoped conditional item.

## Phrase the result
- Write hypotheses, then a connective, then the conclusion.
- State all substantive hypotheses needed to read the result on its own. Reuse unambiguous global notation without redefining it.
- Introduce symbols before first use or bind them at their first occurrence. State ranges, quantifier order, uniqueness/existence distinctions, and constant dependencies.
- Separate claims with different quantifier scopes into enumerated complete sentences. Do not let “some,” “every,” “uniformly,” or “sufficiently large” drift during editing.
- Keep reductions, calculations, motivation, and “we show” inside the proof or surrounding prose, not inside the formal assertion.
- Move proof-only constants and auxiliary objects out of the statement. Name a lengthy construction first if the conclusion needs it.
- Use theorem for a principal result, proposition for a substantial supporting result, lemma for a supporting step, corollary for an immediate consequence, and conjecture for an unproved claim.
- Preserve existing stable labels where possible. Keep internal execution identifiers out of the published text.

## Check and deliver
Compare old and new hypotheses, quantified variables, ranges, dependencies, and conclusions. Show the revised statement plus a short explanation of merges or splits when useful.
If a missing assumption is necessary for truth, flag it as a proposed mathematical correction; do not silently add it under a style-only instruction. Never present a cleaner statement as proved solely because its source draft said so.
