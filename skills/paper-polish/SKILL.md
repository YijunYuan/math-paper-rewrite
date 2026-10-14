---
name: paper-polish
description: "Polish the readability of an existing mathematical manuscript, harmonize sections, and align abstract and introduction with the body. Use for final editing of AI drafts while preserving claims, proofs, and supporting citations."
---

# Paper polish

Adapted from Pharos; see https://github.com/YijunYuan/math-paper-rewrite/blob/main/NOTICE.md and references/upstream.md. Read ../paper-style/SKILL.md and resolve the style before editing.

## Scope
Preserve mathematical claims, proof obligations, substantive assumptions, quantifier order, constant dependencies, and supporting citations. Do not reorder material in a way that changes what is available to a proof.
Polish can be performed on a draft without a formal verification workflow; state known unresolved issues rather than claiming that the draft passed a verifier. If an issue prevents a truthful abstract or introduction, mark that passage unresolved.

## Consecutive reading
Read adjacent sections together. Remove repeated setup that is genuinely redundant; unify terminology and voice; fix transitions by explaining the logical role of the next section.
Preserve technical precision. If an apparent redundancy is a needed hypothesis, keep it.
For a long proof, clarify its route and what each existing step establishes, without deleting a required inference or inventing a missing proof.
Use descriptive step headings where helpful; avoid adding a heading for every elementary line.

## Abstract and introduction
After reading the actual body, align the abstract with what is established and the mechanism that establishes it.
Write or revise the introduction to the chosen style: precise problem, relevant prior work and its limitation, actual results, concrete contributions, and a short roadmap when useful.
Use ../identify-key-steps/SKILL.md and ../identify-key-ingredients/SKILL.md if the contribution is unclear.
When restating a main theorem, retain exactly the body's assumptions and conclusion, introduce its symbols, and use distinct labels linked to the body theorem.

## Front matter and references
Preserve authorship, funding, acknowledgements, and AI-use disclosures unless explicitly asked to change them. Fill them only from supplied information; do not add Pharos acknowledgements merely because this skill derives from Pharos.
Do not fabricate a computation, reproducibility claim, human review, citation, or verification history. If computation details are essential but missing, report the omission.
Keep mathematical citation support unchanged in a polish-only pass. Flag invalid or insufficient support instead of silently swapping sources.
Check labels and bibliography resolution when source files and a compiler are available. If not, report that limitation accurately. Compilation is a formatting check.

## Finish
Compare the revised statements and key proof passages with their originals; record any unresolved mathematical issue separately from stylistic changes.
Return the requested edited artifact plus a concise change summary. In an integrated rewrite, hand the result back for a final semantic comparison after all abstract/introduction edits.
