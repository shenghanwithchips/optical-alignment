# Implementation and Handoff

Optical alignment only helps if it survives real implementation. Use this reference when editing Figma, CSS, React, SwiftUI, native UI, or design-system components.

## Figma / design tool workflow

Start with auto-layout, constraints, grids, and component metrics. Then use explicit optical offsets only after you can name the visual cause.

Annotate intentional deviations. A useful annotation says: “Optical offset: quote hangs outside text edge so word shapes align,” or “Icon path shifted 1px right to center visual mass inside 40px button.”

Prefer component-level changes for repeated patterns. Use one-off frame nudges for fixed hero copy, posters, banners, covers, and editorial display type.

## CSS / frontend workflow

Render before judging. CSS values, SVG viewBoxes, and font metrics can lie visually.

Prefer visual-only offsets when the layout box should remain stable:

```css
.label {
  transform: translateY(-1px);
}

.headline-line--optical {
  margin-inline-start: -0.03em;
}

.quote-mark {
  position: relative;
  left: -0.25em;
}
```

Use custom properties for design-system patterns:

```css
:root {
  --button-padding-inline: 1.35em;
  --button-padding-block-start: 0.78em;
  --button-padding-block-end: 0.68em;
}
```

Document why a value is asymmetric:

```css
/* Optical: bottom is smaller because vertical rhythm is judged from baseline,
   not descender box. Re-test if font, weight, or label case changes. */
.button {
  padding-block: 12px 10px;
}
```

## Responsive and localization rules

Manual line-specific nudges are fragile when copy wraps. If the copy changes, the optical relationship changes. Treat fixed hero headlines differently from dynamic product copy.

For dynamic text:

- Keep corrections generic and component-based.
- Avoid line-specific transforms unless breakpoints are fixed.
- Re-test translated strings and RTL/writing-mode variants.
- Avoid clipping punctuation or descenders.

For fixed display text:

- Use exact line breaks if approved.
- Add comments tying the optical nudge to the fixed copy.
- Re-test when the copy, typeface, weight, size, or breakpoint changes.

## Accessibility and interaction safety

Never reduce the actual clickable or focusable area just to make the visual center look right. Keep the outer hit target stable and nudge the inner visual element.

Check:

- Focus ring still encloses the interactive object.
- Text is not clipped at 200% zoom or user font scaling.
- SVG or text offsets do not create hidden overflow problems.
- Touch target remains at the project/platform minimum.
- Screen reader order and semantics are unchanged.

## Handoff note template

```markdown
Optical alignment note: [element]
Mechanical baseline: [grid/box/padding/baseline value]
Visual issue: [what looked off]
Correction: [nudge and direction]
Reason: [glyph shape / punctuation / baseline / icon silhouette / visual mass]
Scope: [component-wide / breakpoint-specific / fixed copy only]
Retest if: [font/copy/breakpoint/icon changes]
Accessibility: [hit area/focus/text scaling preserved]
```

## When the agent cannot render

If the environment cannot render the UI or inspect a screenshot, state the limitation. Provide an optical hypothesis, specify what to compare in the final screenshot, and avoid claiming the nudge is correct.
