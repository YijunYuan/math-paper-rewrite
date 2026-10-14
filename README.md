# math-paper-rewrite

A standalone skill bundle for improving mathematical papers, especially AI-generated and AI-assisted drafts. Includes **seven writing skills adapted from Pharos and one new orchestrator**.

No Pharos runtime, fact graph, checkpoint system, MCP service, or multi-agent framework is required. Inputs may include LaTeX, Markdown, extracted PDF text, proof notes, and source references. File editing, PDF extraction, and LaTeX compilation use the capabilities available in the host environment.

## Included skills

| Skill | Purpose |
| --- | --- |
| [math-paper-rewrite](skills/math-paper-rewrite/SKILL.md) | New orchestrator: scope the task, route work, preserve mathematical meaning, and consolidate revisions |
| [paper-structure-planning](skills/paper-structure-planning/SKILL.md) | Identify key results and organize sections and concepts |
| [statement-writing](skills/statement-writing/SKILL.md) | Consolidate fragmented facts and clarify hypotheses, quantifiers, and conclusions |
| [identify-key-steps](skills/identify-key-steps/SKILL.md) | Locate the genuinely nontrivial steps in a proof |
| [identify-key-ingredients](skills/identify-key-ingredients/SKILL.md) | Trace essential observations, citations, methods, and contributions |
| [paper-style](skills/paper-style/SKILL.md) | Apply a consistent voice using author guidance, exemplars, or the bundled style |
| [paper-polish](skills/paper-polish/SKILL.md) | Harmonize sections and align the introduction and abstract with the body |
| [outline-file-writing](skills/outline-file-writing/SKILL.md) | Create a traceable skeleton of sections, notation, statements, and citations |

Separate proof-audit and reference-audit skills are outside this bundle. Semantic comparisons during editing are not a complete correctness certification.

## Installation

Clone this repository:

```bash
git clone https://github.com/YijunYuan/math-paper-rewrite.git
```

Copy **all eight complete directories** from `skills/` into your project's `.agents/skills/` directory, or into your Codex user skills directory, normally `~/.codex/skills/`. Keep each skill's `references/`, `agents/`, and `LICENSE` files.

The orchestrator calls companion skills through sibling-relative paths. Install the bundle together rather than installing only the orchestrator.

If the destination already contains a skill with the same name, compare and back up that version before replacing it. Restart or reopen the session so the host can discover the installed skills.

The bundle uses the standard `SKILL.md` directory format. No Python package or background service is required to use the writing instructions.

## Usage

### Rewrite a complete paper

> Use $math-paper-rewrite to revise this mathematical manuscript. Preserve its mathematical meaning and existing citation support. Improve the narrative, theorem organization, introduction, and transitions. Keep the paper in English, save a separate revised version, and list substantive changes and unresolved mathematical issues.

### Polish only

> Use $paper-polish to polish this LaTeX draft. Do not change theorem hypotheses, conclusions, or proof dependencies. Report any mathematical issue separately.

### Refine statements

> Use $statement-writing to reorganize the propositions in Section 3. Consolidate fragments used only within one proof, clarify quantifier scopes and constant dependencies, and retain every necessary assumption.

### Identify contributions

> Use $identify-key-steps followed by $identify-key-ingredients to identify the proof's main mechanism and the essential inputs behind it. Ground each finding in a manuscript passage and distinguish established contributions from unresolved claims.

The orchestrator loads only the skills needed for the task. A full rewrite usually follows: key steps → key ingredients → structure and statements → body revision → polish → final semantic comparison. Narrow requests go directly to the corresponding skill.

## Custom style

Provide `style/STYLE.md` in the manuscript project to specify venue requirements, language, sentence style, proof detail, and accessible exemplars. Otherwise, use the bundled [default style](skills/paper-style/references/STYLE.md).

Exemplars guide expression and organization, not the copying of claims, references, or author information. Using these skills does not justify adding a claim that Pharos generated or verified the paper.

## Provenance and license

Source revision: Pharos `aa0b72e4a7211311a3156ef7d993cd3be9f57445`. Each extracted skill's original text is preserved in `references/upstream.md`; the active `SKILL.md` is a standalone adaptation. Original and adapted default style files are also retained separately.

See [NOTICE.md](NOTICE.md) for source paths and modification details, and [provenance.json](provenance.json) for source hashes. Distributed under [Apache-2.0](LICENSE). This is an independent adaptation, not an official Pharos release.

## Validation

Run:

```bash
python scripts/validate_package.py
```

The standard-library validator checks the eight-skill inventory, metadata, sibling dependencies, local references, license copies, and original-source hashes. It does not verify mathematical correctness.
