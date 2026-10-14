---
name: identify-key-steps
description: "Identify the genuine nontrivial steps in a mathematical manuscript or proof notes. Use to explain the proof idea, focus a paper's narrative, or replace an AI-generated list of facts with a supported contribution map."
---

# Identify key steps

Adapted from Pharos; see https://github.com/YijunYuan/math-paper-rewrite/blob/main/NOTICE.md and references/upstream.md.

## Read the evidence
Read the main claim and its proof, follow cited internal lemmas to their dependencies, and consult supplied literature when judging what is standard. Use manuscript anchors instead of fact IDs. Do not classify a proof you have not read. Use research-history records only when supplied; their absence does not block analysis of the manuscript.

## Find the work
1. State what the manuscript actually establishes, with its hypotheses; distinguish this from the intended target.
2. Extract a compact proof skeleton: reductions, constructions, essential estimates, and supporting results.
3. For each skeleton result, separate the depth of its statement from the difficulty of its proof given its prerequisites.
4. Locate the precise step where something nonroutine happens: an auxiliary choice not prescribed by the claim, essential use of a hypothesis, difficult generalization, nontrivial bound, delicate exhaustive classification, or essential imported theorem.
5. Explain why a naive or routine alternative does not suffice only when the text or a checked argument supports that comparison. Do not invent a history of failed attempts.
6. Treat length, lemma count, citation count, and verifier rejections as weak signals. A short step may carry the entire idea.
7. Name the dependencies of each nontrivial step for ../identify-key-ingredients/SKILL.md.

Judge mathematical content, not author prestige or journal rank. A computation may carry a genuine result; distinguish exact exhaustive computation from numerical evidence and from the conceptual choice that makes the computation useful.

## Output
Give the main achieved claim; a short skeleton; and for each key step its location, what it establishes, why it is nonroutine, what it depends on, and confidence/limitations.
Separate “supported by the inspected argument,” “asserted but not established,” and “proposed.” If no nontrivial input can be identified, say so without inventing novelty. This is a contribution analysis, not a full correctness certificate.
