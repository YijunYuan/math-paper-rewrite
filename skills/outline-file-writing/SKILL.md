---
name: outline-file-writing
description: "Write a mathematical paper's explicit outline or LaTeX skeleton with shared statements, notation, labels, dependencies, and citation evidence. Use after structural planning or to coordinate a long manuscript rewrite."
---

# Outline file writing

Adapted from Pharos; see https://github.com/YijunYuan/math-paper-rewrite/blob/main/NOTICE.md and references/upstream.md. Use ../paper-structure-planning/SKILL.md to decide the structure and ../statement-writing/SKILL.md for formal assertions.

## Inputs and format
Read the manuscript, agreed section plan, available source references, and existing preamble/template.
Preserve the requested format. For LaTeX, create a body fragment usable with the existing manuscript preamble; for prose-only planning, use a structured outline without imposing a TeX project.
Use an outline as a stable contract between sections, not as a fabricated record of verification.

## Include
1. A global notation map: symbol, meaning, scope, and existing macro when applicable. Reuse existing commands and avoid introducing macros unnecessarily.
2. An introduction scaffold reflecting the chosen style. Draft its substantive prose only when the actual results are understood.
3. Standing assumptions and ambiguous terminology, defined before first use.
4. Body sections containing every key result, every cross-section statement/definition, and each essential external result in the scope in which it is used.
5. A reference collation recording the source and what claim it supports. Preserve existing bibliography keys and BibTeX/BibLaTeX conventions.

Keep the planning skeleton short. Omit proofs and section-internal routine lemmas unless the user requests a proof outline. Such a proof outline is a distinct deliverable and must not be described as a complete proof.

## Traceability
For each shared statement, record in comments or a companion map:
- source: original manuscript label/paragraph or supplied proof-note anchor;
- owner: section that proves/defines it, or external source;
- depends: earlier statements needed;
- status: supported by inspected material, unresolved, or proposed.
For an external theorem, record exact source locator, required hypotheses, conclusion, and whether the primary source was actually checked. Record unknown status honestly.

Do not convert “the manuscript asserts” into “verified.” Do not invent Pharos fact IDs, project services, or verification metadata.
If a shared statement must change, enumerate all affected sections and update their contracts consistently; do not silently patch just one occurrence.

## Labels and checks
Preserve existing stable labels, resolve duplicates, and ensure one global symbol has one meaning. New labels can use thm:, prop:, lem:, def:, sec:, eq: followed by meaningful slugs.
If generating LaTeX, use environments defined by the supplied template. Compile with an available engine when the deliverable needs it, and report unresolved dependencies or unavailable tooling. Do not require a Pharos template or command.
Deliver the outline and its remaining mathematical/source questions; reserve research logs and internal identifiers for the companion map, not publication prose.
