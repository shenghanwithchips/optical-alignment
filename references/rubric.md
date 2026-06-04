# Optical Alignment Rubric

Use this rubric to critique an optical-alignment recommendation, AI-generated UI, or implemented component. Score each dimension from 0 to 3.

## Scoring scale

0 means missing or actively wrong. 1 means generic, weak, or unsupported. 2 means usable but incomplete. 3 means precise, contextual, and implementation-aware.

## Dimensions

### Mechanical baseline

A strong review identifies the measurable reference: grid, margin, bounding box, line box, baseline, centerline, SVG viewBox, component padding, or design token.

Failing signs: “Looks off” with no reference; “just center it”; no current values or layout anchor.

### Optical symptom

A strong review states what appears visually pulled, heavy, loose, low, high, ragged, or imbalanced, and in what direction.

Failing signs: Confuses visual imbalance with preference; does not say where the imbalance is perceived.

### Perceptual cause

A strong review names the cause: curved glyph, diagonal glyph, punctuation, quote mark, baseline, descender, all-caps label, icon silhouette, asymmetric inner whitespace, or misleading bounding box.

Failing signs: Uses “vibe,” “modern,” or “premium” without perceptual diagnosis.

### Context sensitivity

A strong review avoids universal rules. It explains how typeface, font size, font weight, actual copy, line breaks, component scale, and rendering medium affect the decision.

Failing signs: “Always outdent W”; “always use equal padding”; “always center by viewBox.”

### Nudge quality

A strong correction is small, reversible, and axis-specific. It changes only what is needed.

Failing signs: Large unexplained offsets; random magic numbers; redesigns the component when a small nudge would work.

### Implementation safety

A strong recommendation preserves layout stability, hit area, focus ring, text scaling, semantics, and responsive behavior.

Failing signs: Shrinks clickable area; clips text; hides overflow carelessly; breaks localization; treats CSS values as proof without rendering.

### Documentation and handoff

A strong output names the intentional deviation and when it must be retested.

Failing signs: Leaves developers with unexplained asymmetric values; no comments; no scope.

### Validation

A strong output compares before/after at actual size, in context, with real content, at relevant breakpoints.

Failing signs: Only checks with guide lines; no screenshot/render check; no edge cases.

## Anti-slop checks

Be suspicious when an AI-generated review or UI does any of these:

- Says a design is “perfectly aligned” because all values are equal.
- Recommends generic equal padding for every component.
- Uses centered flex/grid alignment as the final answer for icons without checking visual mass.
- Gives exact px values without explaining their dependence on font/copy/rendering.
- Ignores baseline and descender behavior in text containers.
- Ignores hanging punctuation for large quotes or editorial headings.
- Produces polished UI but no mechanical baseline, optical symptom, perceptual cause, or validation method.

## Pass criteria

A recommendation passes when it can answer this sentence clearly:

“Although [mechanical metric] is numerically aligned, [visual cause] makes [element] appear [direction/imbalance], so I would nudge [target] by [small correction] while preserving [layout/accessibility constraint], then validate with [actual rendered comparison].”
