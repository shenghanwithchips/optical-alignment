# optical-alignment skill

This skill packages an optical-alignment thinking workflow for UI, typography, spacing, icons, and coded visual polish. 

Use it when a design is technically aligned but visually off: headline edges, centered text, hanging punctuation, all-caps buttons, card padding, icon centering, and implementation handoff.

## Structure

- `SKILL.md` contains the core trigger, workflow, gotchas, output contract, and validation loop.
- `references/` contains detailed frameworks for typography, spacing/icons, implementation, rubrics, and source mapping.
- `assets/` contains reusable review and agent-instruction templates.
- `scripts/` contains a package validator and a text checker for optical-alignment reasoning.
- `evals/` contains trigger and task evaluations for future refinement.

## Validate

From this directory:

```bash
python scripts/validate_skill_package.py .
```

To check a generated optical-alignment review:

```bash
python scripts/check_optical_alignment_output.py path/to/review.md
```

## Adapter idea for coding agents

Add the content of `assets/agents-snippet.md` to your project-level `AGENTS.md`, Cursor Rule, or equivalent agent instruction file. Keep the detailed framework in this skill package rather than pasting everything into a global rule.

## Licence
MIT
