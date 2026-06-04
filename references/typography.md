# Typography Optical Alignment

Typography is where optical alignment becomes most visible because glyph metrics rarely match perceived edges. Use this reference for headlines, display copy, centered type, quotes, and fixed marketing/editorial text.

## Start with actual rendered text

Do not judge from font names or CSS alone. Browser rendering, antialiasing, font fallback, weight, line-height, letter-spacing, and line breaks affect the perceived result. Always inspect the final rendered copy when possible.

## Left-aligned display type

The visible left edge of a block is not always the same as the glyph bounding boxes. In large bold headlines, the first glyph of each line can create a ragged perceived margin even when each line is mechanically aligned.

Round glyphs such as G, C, O, Q, and S often need to extend slightly past the alignment edge because curves visually recede. Sharp or diagonal glyphs such as T, V, W, X, Y, and Z can also create optical edge issues, but they must be judged by their relationship to the neighboring lines. There is no “always outdent this letter” rule.

Useful review questions:

- Which letterform appears to define the visual edge of each line?
- Are curves visually receding compared with vertical stems?
- Does a diagonal or crossbar create empty space that makes the line feel indented?
- Does the correction still work when comparing the entire phrase, not just one letter?

## Center-aligned display type

Metric centering is based on line length. Optical centering is based on visual mass. A line ending in punctuation or quotation marks can appear longer or heavier even if the software centers it correctly.

For centered text, compare the visual center of each line, not just the bounding width. If one line feels pulled by punctuation or asymmetric glyphs, a very small horizontal nudge can make the block feel more centered.

## Hanging punctuation and optical margins

For quotes, pull-quotes, editorial headings, landing page hero copy, posters, book covers, and banners, punctuation may need to hang outside the text edge. The goal is to align the actual word shapes, not the quote mark or period.

On the web, CSS provides `hanging-punctuation`, but browser support may be limited. For production UI, verify compatibility before relying on it. For fixed copy, alternatives include negative `text-indent`, wrapper spans, pseudo-elements, or one-off Figma/CSS offsets.

Use hanging punctuation when:

- A large quote mark breaks the left edge of a block.
- Periods or quotation marks make centered lines feel off.
- The copy is fixed enough to justify manual tuning.
- The layout is editorial, marketing, print, poster, cover, or hero-level.

Avoid heavy manual punctuation tuning when:

- The copy is highly dynamic or localized.
- The text wraps unpredictably across responsive breakpoints.
- The implementation would become fragile or inaccessible.

## Baseline-aware vertical judgment

When evaluating vertical spacing around text, remember that the visual bottom of a line is usually perceived from the baseline, not from the deepest descender. Descenders matter, but if padding is measured only from the descender box, the text can look vertically low.

For buttons and cards with text, inspect cap height, x-height, baseline, descenders, and line-height. A label can be mathematically centered in the line box while still appearing too low or too high.

## Kerning, tracking, and CSS limits

Do not promise a single CSS trick for every typographic optical problem. Kerning and text alignment are driven by font metrics; dynamic web text makes exact baseline and margin control difficult. If the user needs perfect type, prioritize stable, high-value copy and document the exceptions.

## Implementation patterns

For a fixed hero headline, use annotated spans or custom classes:

```css
.hero-title .line--optical-left {
  margin-inline-start: -0.04em; /* tune after rendering */
}

.hero-title .quote-mark {
  margin-inline-start: -0.28em; /* hangs punctuation; verify per typeface */
}
```

For first-line punctuation experiments, consider `hanging-punctuation` only after compatibility review:

```css
blockquote {
  hanging-punctuation: first allow-end;
}
```

For line-specific nudges, document the fixed copy dependency:

```css
/* Optical correction for fixed homepage headline at >= 768px.
   Keeps word shapes aligned; remove/retest if copy changes. */
.hero-title__line:nth-child(1) {
  transform: translateX(-2px);
}
```
