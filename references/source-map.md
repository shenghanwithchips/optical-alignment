# Source Map

This skill was synthesized from the uploaded `optically-perfect-design.pdf` and the uploaded `how-to-write-the-skills.md`, then supplemented with stable implementation references.

## Domain source: optically-perfect-design.pdf

Page 1 establishes the premise: mathematical alignment from design software or CSS can disagree with human perception, so designers should treat grids and metrics as starting points and trust visual judgment for final decisions.

Pages 1-4 focus on typography edge alignment. The article shows that large bold headlines reveal “overshooting” problems; round glyphs such as G, C, O, Q, and S can need to extend slightly past a margin, while sharp/diagonal letters such as T, V, W, X, Y, and Z may also need contextual adjustment. It emphasizes that letter-specific rules are not universal.

Pages 5-7 focus on center alignment, quotation marks, and hanging punctuation. The article shows how punctuation and quotes can distort perceived center or edge alignment, and recommends leaving quotation marks outside the edge for better visual flow in certain contexts.

Pages 7-9 focus on internal spacing. Equal padding around all-caps button labels can look vertically wrong; the example reduces bottom padding and increases horizontal padding. Lowercase labels behave differently because the eye is drawn toward the baseline. Text boxes can also need asymmetric vertical padding, with bottom spacing judged from the baseline rather than the descender. Icons can need optical centering because bounding boxes differ from perceived visual mass.

## Skill-writing source: how-to-write-the-skills.md

The skill follows the uploaded guidance to ground the skill in real expertise rather than generic advice, keep `SKILL.md` concise, use progressive disclosure for larger references, include gotchas, provide output templates, add validation loops, bundle scripts for repeatable checks, and include evals before sharing.

## Supplemental implementation references

CSS `hanging-punctuation` exists and specifies whether punctuation can hang at the start or end of a line, but browser support can be limited. This skill therefore treats it as one implementation option, not a guaranteed production fix.

Agent skill packages commonly use a `SKILL.md` file with `name` and `description`, plus optional scripts, references, and assets. This package follows that shape for portability across agent runtimes that support Agent Skills.
