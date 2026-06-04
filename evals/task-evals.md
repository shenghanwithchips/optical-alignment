# Optical Alignment Task Evals

Use these evaluations after modifying the skill. A good response should follow the skill workflow and pass `scripts/check_optical_alignment_output.py` when saved as text.

## Eval A: all-caps button

Prompt:

> The label in my all-caps button is exactly centered with 20px padding on every side, but visually the text feels too low and the button feels narrow. Review it and suggest a Figma/CSS fix.

Expected qualities:

- States that equal padding is the mechanical baseline, not final proof.
- Diagnoses all-caps label, baseline/cap-height/line-box perception, and horizontal proportion.
- Suggests small bottom/top or label offset plus increased horizontal padding, without claiming universal pixel constants.
- Preserves outer hit area and focus ring.
- Mentions rendered before/after validation.

## Eval B: display headline left edge

Prompt:

> A large bold headline has three lines. The first line begins with “Welcome,” the second with “Everybody,” and the text is left aligned in CSS. The W feels indented compared with the E. Should I push W outside the margin?

Expected qualities:

- Refuses a universal “always outdent W” rule.
- Diagnoses diagonal/curved glyph shapes and neighboring line relationship.
- Recommends comparing the full phrase with and without a small outdent at actual size.
- Notes that copy, typeface, weight, and line break changes require retesting.
- Provides a fixed-copy implementation comment if using CSS.

## Eval C: quote / hanging punctuation

Prompt:

> My blockquote starts with a big curly opening quote. It is left aligned by the browser, but the actual words feel pushed right. How should I fix it for a marketing landing page?

Expected qualities:

- Diagnoses quotation mark breaking the visual text edge.
- Recommends hanging punctuation / optical margin alignment.
- Notes that CSS `hanging-punctuation` can be tried but must be compatibility-checked; fixed-copy alternatives are acceptable.
- Explains that the goal is to align word shapes, not the quote mark.
- Mentions responsive and localization retesting.

## Eval D: icon button

Prompt:

> The Wi-Fi icon SVG is centered by viewBox inside a square button, but it looks too high. The developer says the math is correct.

Expected qualities:

- States that bounding-box center can differ from perceived icon mass.
- Keeps outer button layout centered and stable.
- Suggests moving the inner SVG/path only.
- Mentions focus ring/hit area/accessibility preservation.
- Documents the optical offset so future developers do not recenter it blindly.

## Eval E: bad answer detection

Prompt:

> Review this recommendation: “Everything should use equal padding and exact center alignment. If the numbers are equal, it is visually correct.”

Expected qualities:

- Rejects the recommendation.
- Explains numeric equality versus perceived balance.
- Gives examples from typography, spacing, and icons.
- Replaces it with the measure-perceive-diagnose-nudge-validate workflow.
