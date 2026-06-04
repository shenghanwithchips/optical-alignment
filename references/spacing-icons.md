# Spacing, Buttons, Cards, and Icons

Use this reference when equal padding, centered icons, or symmetric boxes look visually wrong.

## Uneven spacing can be visually correct

Equal numbers often look logical in code and wrong in perception. The eye judges the relationship between shape and empty space, not only the rectangle around them.

A good spacing correction states which visual mass is being balanced. It should not merely say “make it uneven.”

## Buttons

Buttons often need horizontal padding that is larger than vertical padding. All-caps labels can make vertical centering look off because the glyph mass, cap height, baseline, and line box do not feel centered the same way the numbers do.

For all-caps labels, inspect whether the bottom appears too spacious. A small bottom reduction or upward text offset can create better vertical balance. The source example uses a 2px bottom reduction and 5px extra horizontal padding, but those values are examples, not constants.

For lowercase labels, the baseline and x-height often create a more natural vertical balance. Horizontal padding may still need to expand to make the button feel composed.

Implementation guidance:

- Preserve the outer hit area even if inner text is optically offset.
- Prefer tokenized component padding if the pattern repeats.
- Use a child span or pseudo-element if only the label needs a visual offset.
- Retest with the shortest and longest expected labels.

Example:

```css
.button {
  min-height: 44px; /* keep accessible target; tune to project standard */
  padding: var(--button-padding-block) var(--button-padding-inline);
}

.button__label--all-caps {
  transform: translateY(-1px); /* optical only; verify in rendered output */
}
```

## Text containers and cards

For text blocks inside cards, equal top and bottom padding may make the bottom feel too loose. Bottom padding should often be judged from the text baseline rather than from the descender box. This can make the bottom padding slightly smaller than the top padding while still looking balanced.

Review questions:

- Is the card measured from the line-height box, the glyph ink, or the baseline?
- Does the text feel vertically centered when viewed without guides?
- Does the bottom whitespace look larger because descenders are rare or visually light?
- Does the card still work with multi-line text, real content, and responsive wrapping?

## Icons

Icon bounding boxes are rarely the same as visual centers. A Wi-Fi icon, play triangle, chevron, search icon, star, location pin, or arrow can feel off-center even when the SVG viewBox is mathematically centered.

Diagnose the silhouette first. Ask where the icon's perceived mass sits. Then offset the inner SVG or icon path while preserving the outer button/container alignment.

Implementation guidance:

- Keep the outer icon button box aligned to the layout grid.
- Offset the inner SVG or path visually.
- Preserve focus ring, hit target, and layout dimensions.
- Add an implementation note such as “SVG path optically centered; do not recenter by viewBox.”

Example:

```css
.icon-button {
  inline-size: 40px;
  block-size: 40px;
  display: grid;
  place-items: center;
}

.icon-button svg[data-icon="play"] {
  transform: translateX(1px); /* balances triangular visual mass */
}
```

## Spacing quality checks

The correction is good when the component feels calm without visible guides, the grid remains understandable, repeated components still align as a system, and the nudge does not create fragile one-off CSS for ordinary dynamic content.
