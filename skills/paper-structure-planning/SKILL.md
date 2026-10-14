---
name: paper-structure-planning
description: "Plan or restructure a mathematical paper around its key results, concepts, and proof dependencies. Use for fragmented AI drafts, excessive lemmas, unclear narrative, or chapter organization."
---

# Paper structure planning

Adapted from Pharos; see https://github.com/YijunYuan/math-paper-rewrite/blob/main/NOTICE.md and references/upstream.md for provenance and the unmodified original. Use the standalone procedure below; the original's project services are not required.

## Inputs
Read the manuscript or proof notes, intended main result, and supplied literature or author guidance. Use theorem labels, section/paragraph anchors, and file names as evidence locators. A draft assertion is not a verified fact; record gaps and uncertain statements explicitly.

## Procedure
1. Recover the argument's thread: problem → obstacle → central idea → supporting results → main theorem.
2. Identify key results by reading their proofs. Include the final target and results that carry a non-obvious construction, an essential use of a hypothesis, a difficult passage from a special case to the general case, or a genuinely nontrivial estimate.
3. Do not organize chapters around definition unfolding, substitutions, routine specializations, or bookkeeping alone. Computations can be essential mathematical evidence; assess their actual logical contribution rather than excluding them categorically.
4. Merge redundant concepts and resolve notation collisions. Name a recurring bundle of assumptions when it functions as a coherent concept; do not manufacture terminology for a one-off expression.
5. Define objects before first use. Put global notation and standing assumptions in a setup section when useful; put a new construction next to its mathematical role.
6. Make each body section establish one central result or several tightly connected ones. Order proof dependencies so readers encounter prerequisites first. Introductory previews are allowed; circular proof dependencies are not.
7. Use ../statement-writing/SKILL.md for decisions about merging facts and phrasing theorem statements. Use ../outline-file-writing/SKILL.md when a concrete skeleton is requested.
8. Resolve style through ../paper-style/SKILL.md. Preserve the author's required section structure unless a proposed reorganization is part of the task.

## Output
Provide an ordered outline with, for each section: purpose, principal result, prerequisites, source anchors, and material to merge/move/remove. Separate established claims from proposed repairs. Record an old-to-new section map when reorganizing an existing manuscript.

A needed change to a theorem's hypotheses or conclusion is a mathematical issue, not editorial permission. Propose it explicitly and propagate the dependency impact only when mathematical revision is authorized.
