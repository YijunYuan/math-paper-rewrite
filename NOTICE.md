# Provenance and modification notice

This package contains seven adapted writing skills and one new coordinating skill.
The seven skills and default style are derived from [FrenzyMath/Pharos](https://github.com/frenzymath/Pharos), commit `aa0b72e4a7211311a3156ef7d993cd3be9f57445`, retrieved 2026-10-14.
Pharos acknowledges development by Bin Dong, Guoxiong Gao, Jiedong Jiang, Shurui Liu, Zeming Sun, and Bin Wu.
Upstream licensing: Apache License 2.0; see LICENSE. No upstream NOTICE file was present in the inspected source tree.

The seven original skill texts are retained unchanged as `skills/<name>/references/upstream.md`.
The original default style is retained as `skills/paper-style/references/upstream-style.md`.
These are historical source references, not executable instructions for the standalone workflow.
The corresponding active SKILL.md files and default STYLE.md are modified derivatives; the math-paper-rewrite controller is new.

## Changes made on 2026-10-14
- Replace required fact-graph IDs, project checkpoints, route boards, MCP services, and Pharos CLI jobs with ordinary manuscript anchors, proof notes, and source references.
- Preserve the selected skills' functions while condensing workflow-specific instructions.
- Add narrow-task routing, explicit editorial/mathematical boundaries, and a final semantic comparison after introduction and abstract edits.
- Make templates and bibliography conventions configurable; do not insert Pharos system-use disclosure or acknowledgements into a manuscript merely because these skills are used.
- Replace journal/author-prestige filters and fixed publication-age cutoffs with relevance and evidence criteria.
- Distinguish exact computational proof from numerical evidence instead of categorically excluding computations from key steps.
- Add English display names and package usage documentation.

## Source mapping

| Retained source | Original repository path |
| --- | --- |
| skills/paper-structure-planning/references/upstream.md | [agents/skills/main/paper/paper-structure-planning/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/main/paper/paper-structure-planning/SKILL.md) |
| skills/statement-writing/references/upstream.md | [agents/skills/main/paper/statement-writing/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/main/paper/statement-writing/SKILL.md) |
| skills/identify-key-steps/references/upstream.md | [agents/skills/reporter/identify-key-steps/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/reporter/identify-key-steps/SKILL.md) |
| skills/identify-key-ingredients/references/upstream.md | [agents/skills/reporter/identify-key-ingredients/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/reporter/identify-key-ingredients/SKILL.md) |
| skills/paper-style/references/upstream.md | [agents/skills/main/paper/paper-style/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/main/paper/paper-style/SKILL.md) |
| skills/paper-polish/references/upstream.md | [agents/skills/main/paper/paper-polish/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/main/paper/paper-polish/SKILL.md) |
| skills/outline-file-writing/references/upstream.md | [agents/skills/main/paper/outline-file-writing/SKILL.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/skills/main/paper/outline-file-writing/SKILL.md) |
| skills/paper-style/references/upstream-style.md | [agents/resources/default-style/STYLE.md](https://github.com/frenzymath/Pharos/blob/aa0b72e4a7211311a3156ef7d993cd3be9f57445/agents/resources/default-style/STYLE.md) |

The package is an independent adaptation, not an official Pharos release. No endorsement by the upstream authors is implied.
