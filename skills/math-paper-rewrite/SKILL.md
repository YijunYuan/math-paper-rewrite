---
name: math-paper-rewrite
description: "Coordinate a standalone mathematical-paper rewrite using seven Pharos-derived writing skills. Use for improving AI-generated or AI-assisted manuscripts, full-paper rewriting, narrative reconstruction, or a combined structure-and-style revision; route narrow tasks to the appropriate companion skill."
---

# Math paper rewrite

Coordinate exactly seven companion writing skills. Work with ordinary LaTeX, Markdown, extracted PDF text, and supplied proof notes; no Pharos service, fact graph, or agent framework is required.

## Establish the task
Read the supplied manuscript and explicit constraints. Determine the requested output and scope from the conversation:
- Full rewrite: improve exposition and organization while preserving mathematical meaning.
- Structure only: analyze and propose/revise an outline, as requested.
- Statements only: refine formal assertions and their granularity.
- Polish only: improve expression and seams without structural or mathematical intervention.
- Contribution analysis: identify key steps and inputs.
Do not turn a narrow edit into a full audit. Ask only for inputs genuinely needed, such as a missing manuscript.
Preserve original language unless translation is requested. Make a separate revised artifact by default; follow explicit in-place edit instructions.

## Route by actual need
Read only the companion skills required for the current operation, via these package-relative paths:

| Job | Skill |
| --- | --- |
| Identify where the proof's work happens | ../identify-key-steps/SKILL.md |
| Trace essential ideas, methods, and sources | ../identify-key-ingredients/SKILL.md |
| Plan sections and concept placement | ../paper-structure-planning/SKILL.md |
| Merge/split and phrase formal statements | ../statement-writing/SKILL.md |
| Fix shared notation, statements, and dependencies in a skeleton | ../outline-file-writing/SKILL.md |
| Resolve and apply voice/exemplars | ../paper-style/SKILL.md |
| Harmonize finished text and front matter | ../paper-polish/SKILL.md |

These are sibling directories installed as one package. If a required file is unavailable, report that packaging problem and use available instructions without claiming the missing skill ran.

## Full rewrite workflow
1. Read the manuscript as a whole. Build a lightweight evidence map: main claim, supporting results, definitions, essential citations, dependency links, and known unresolved issues. Use existing labels and paragraph anchors.
2. Resolve the style once. Locate key steps, then key ingredients, to find the narrative and calibrate contribution claims.
3. Plan structure. Consolidate one-use proof fragments where appropriate; preserve independent and cross-section results. Write a skeleton only when the task's scale or requested deliverable benefits from one.
4. Rewrite the body in dependency order using the agreed statements and notation. Explain what each section contributes. For long proofs, give a route and the role of each step. Keep a needed inference even if it makes the prose less smooth.
5. Check old-to-new correspondence for every changed theorem and mathematically consequential proof passage: hypotheses, quantifier scopes, parameter ranges, constant dependence, conclusion, and logical dependencies. If a dependency changes, inspect the affected uses.
6. Polish the complete body, then align the introduction and abstract with it. Resolve duplicated setup, inconsistent terminology, unsupported promotional language, and misleading novelty claims.
7. Perform a final semantic comparison after polishing, including abstract claims and introductory theorem restatements. Validate references/labels and compile when relevant and available. Record what was actually checked.

## Mathematical boundary
Editing does not establish truth. Do not silently repair a false claim, strengthen a result, weaken a hypothesis, change an imported theorem, or conceal a proof gap.
For a suspected substantive issue, preserve the original claim in a style-only task, locate the issue, explain the consequence, and propose a repair separately. Continue unaffected writing work.
When mathematical repair is explicitly authorized, show the change and check its affected dependencies before adopting it. Mark unresolved problems; do not certify a proof based on fluent prose or successful compilation.
Do not add the separate verification skills to this package or invoke a full proof audit by default. A user-requested audit is a separately scoped task.

## Evidence and attribution
Attribute ideas and citations from inspected sources. Do not infer authorship, funding, human verification, or research history. Preserve existing AI disclosure unless the user requests an alteration; do not insert Pharos system-use claims because these skills were used.
Use primary sources when a specific citation needs checking and access is available; mark unavailable checks. Do not invent references or declare a source nonexistent merely because search failed.
Judge novelty and mathematical importance by content and evidence, not journal prestige or author affiliation.

## Deliver and stop
Deliver the revised artifact in the requested format, a concise change summary, and anchored unresolved issues. Include old-to-new labels/sections when reorganization makes that useful.
For a review-only request, deliver the requested analysis rather than editing.
Finish when the requested scope is revised, semantic changes are accounted for, available format checks are complete, and limitations are stated. Avoid endless polish loops or unsolicited full-scale research.
Preserve source materials and the revision record needed to review changes; do not publish the user's manuscript externally unless requested.
