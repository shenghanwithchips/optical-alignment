---
name: optical-alignment
description: Use when reviewing, refining, or implementing visual UI alignment, optical alignment, typography, hanging punctuation, button padding, card spacing, icon centering, visual balance, or pixel-perfect layouts that still look visually off. Guides the agent to start from numeric alignment, diagnose perceived imbalance from glyph shape, visual mass, baseline, punctuation, spacing, and bounding boxes, then make small context-specific optical nudges with validation and implementation notes.
---

# Optical Alignment

Use this skill when a user asks why an interface, headline, button, card, icon, poster, landing page, hero section, Figma frame, CSS layout, or coded prototype is mathematically aligned but visually wrong. The goal is not decorative polish. The goal is to make the perceived alignment match the human eye while preserving implementation quality.

## Core principle

Numeric alignment is the starting measurement, not the final design decision. Humans perceive shape, visual weight, empty space, baseline, punctuation, and neighboring forms; software aligns bounding boxes and metrics. Prefer the design that looks balanced in context, and document why it intentionally deviates from equal numbers.

## Default workflow

1. Establish the mechanical baseline: identify the grid, margin, bounding box, baseline, centerline, component padding, and current numeric values.
2. Inspect the perceived imbalance: hide or soften guides, view at actual size, zoom out, and compare whether the visual weight feels pulled left/right/up/down.
3. Diagnose the visual cause: glyph shape, punctuation, line break, baseline, descender, all-caps label, icon silhouette, asymmetric whitespace, or a misleading bounding box.
4. Make the smallest useful optical nudge: adjust margin, padding, transform, text-indent, component offset, line position, or icon wrapper only on the axis causing the imbalance.
5. Compare before/after in context: check the component beside adjacent text, cards, icons, controls, and surrounding whitespace, not as an isolated crop.
6. Encode the decision: use design tokens or named exceptions when the pattern repeats; use a documented one-off only for fixed hero copy, posters, covers, banners, or editorial layouts.
7. Validate implementation: render the actual browser/app output, check responsive states, localization, focus rings, hit area, text scaling, clipping, and screenshots at target sizes.

## Progressive disclosure

Read `references/framework.md` when you need the full thinking model or must explain optical alignment conceptually.

Read `references/typography.md` for headlines, large display type, left/center alignment, glyph overshoot, quotes, optical margins, and hanging punctuation.

Read `references/spacing-icons.md` for buttons, cards, text containers, baseline-aware padding, icon centering, and optical centroid issues.

Read `references/implementation.md` when editing Figma/CSS/code or when handing off intentional optical offsets to developers.

Read `references/rubric.md` before critiquing visual craft or deciding whether a generated design is optical alignment or AI slop.

Use `assets/review-template.md` when the user asks for a structured optical review. Use `assets/agents-snippet.md` when adding this skill as mandatory guidance for coding/design agents.

Run `python scripts/check_optical_alignment_output.py <file>` to check whether a written review or implementation plan contains the required optical-alignment reasoning.

Run `python scripts/validate_skill_package.py .` before sharing or modifying this skill package.

## Gotchas

Do not answer with “align everything equally” or “use the grid” as the final recommendation. Equal numbers can still look off.

Do not invent universal pixel constants. A 2px or 5px nudge can be plausible, but the correct offset depends on typeface, font size, font weight, letterforms, copy, line break, icon shape, screen density, and rendering engine.

Do not say every W, T, V, round letter, quote, or period should always overshoot. The relationship between neighboring lines and glyphs decides the correction.

Do not judge optical alignment from CSS values alone. Render the design and inspect the actual output.

Do not shrink touch targets, focus rings, or accessible hit areas to make visuals look centered. Use wrappers, pseudo-elements, inner spans, transforms, or visual-only offsets when needed.

Do not over-tune dynamic body copy. Prioritize fixed hero headlines, marketing sections, logos, editorial layouts, button components, icon buttons, and reusable UI primitives where the copy/shape is stable.

Do not let auto-layout, grid snapping, browser defaults, or component libraries override the eye. They are useful mechanical baselines, not visual truth.

## Output contract

When producing an optical-alignment review, include these sections in prose or a compact table if the user wants a checklist:

- Mechanical baseline: what is currently aligned numerically.
- Optical symptom: what looks visually off and in which direction.
- Cause: glyph, baseline, punctuation, visual mass, padding, icon silhouette, or bounding-box mismatch.
- Nudge: the specific visual correction, with tentative values only when useful.
- Implementation: Figma/CSS/component change and how to avoid breaking layout/accessibility.
- Validation: before/after comparison, responsive states, real copy, and edge cases.

## Short response pattern

When the user asks “why does this look off?” answer with this shape:

```markdown
The numbers are aligned, but the perceived mass is not. The visual pull comes from [shape / punctuation / baseline / icon silhouette / padding]. I would keep [mechanical anchor] as the reference, then nudge [element] [direction] by roughly [small amount or qualitative amount], compare at actual size, and encode it as [token / one-off annotation / CSS wrapper] if it repeats. Check [responsive/accessibility/real-copy edge case] before shipping.
```

## When creating or editing code

Render or inspect the real output before finalizing. If no renderer is available, state that the recommendation is a design hypothesis and give the user a concrete before/after check to perform.

Prefer reversible implementation patterns: wrapper offsets, custom properties, tokenized component padding, `transform`, `margin-inline-start`, `text-indent`, or pseudo-elements. Avoid fragile DOM changes when a visual-only nudge is enough.

## Validation loop

After the first correction, critique the result against `references/rubric.md`. If the nudge fixed numeric symmetry but introduced visual imbalance, clipping, inaccessible hit areas, or undocumented magic numbers, revise and re-check.
