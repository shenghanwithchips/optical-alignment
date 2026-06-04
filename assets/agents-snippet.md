# Agent instruction snippet for optical alignment

When a task involves UI visual polish, typography, spacing, icon centering, button padding, optical alignment, hanging punctuation, or “pixel-perfect but looks off” issues, use the optical-alignment skill before making final design or code changes.

Do not treat equal CSS/Figma values as proof that the design is visually correct. First identify the mechanical baseline, then the perceived optical symptom, then the perceptual cause, then the smallest reversible nudge.

Every visual correction must document why it intentionally deviates from numeric equality and how to validate it in the rendered result.

Before finalizing, check for optical-alignment slop: universal glyph rules, unexplained magic px values, clipped text, reduced hit targets, broken focus rings, untested responsive text, and component-library defaults that look mathematically centered but visually off.
