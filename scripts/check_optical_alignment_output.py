#!/usr/bin/env python3
"""Check whether an optical-alignment review contains the needed reasoning.

This script is intentionally text-based. It is not a visual validator; it catches
common missing parts in agent-written reviews, implementation plans, and handoff
notes so the agent can revise before final output.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CHECKS = {
    "mechanical baseline": [
        r"mechanical baseline", r"numeric", r"grid", r"bounding box", r"baseline", r"centerline", r"padding", r"margin", r"line box", r"基准", r"数值", r"网格", r"边界框", r"基线",
    ],
    "optical symptom": [
        r"optical symptom", r"looks? off", r"appears", r"perceived", r"visual pull", r"heavier", r"too low", r"too high", r"imbalance", r"视觉", r"看起来", r"偏", r"重心", r"不平衡",
    ],
    "perceptual cause": [
        r"cause", r"glyph", r"letter", r"punctuation", r"quote", r"baseline", r"descender", r"all-caps", r"lowercase", r"icon silhouette", r"visual mass", r"原因", r"字形", r"标点", r"引号", r"图标", r"视觉重量",
    ],
    "specific nudge": [
        r"nudge", r"offset", r"translate", r"margin", r"padding", r"text-indent", r"move", r"shift", r"reduce", r"increase", r"微调", r"偏移", r"移动", r"外悬", r"缩小", r"增加",
    ],
    "context sensitivity": [
        r"depends", r"typeface", r"font", r"weight", r"size", r"copy", r"line break", r"render", r"not universal", r"context", r"取决于", r"字体", r"字号", r"字重", r"文案", r"换行", r"不是通用",
    ],
    "implementation": [
        r"css", r"figma", r"component", r"token", r"wrapper", r"pseudo", r"handoff", r"implementation", r"代码", r"组件", r"设计 token", r"交付",
    ],
    "validation": [
        r"validate", r"before.?after", r"actual size", r"render", r"responsive", r"breakpoint", r"accessibility", r"focus", r"hit area", r"验证", r"前后", r"响应式", r"可访问", r"焦点", r"点击区域",
    ],
}

BAD_PATTERNS = [
    (r"always\s+(outdent|overshoot|align|center)", "universal optical rule"),
    (r"all\s+padding\s+should\s+be\s+equal", "equal padding as final truth"),
    (r"just\s+(center|align)\s+it", "generic alignment advice"),
    (r"mathematically\s+correct\s+is\s+enough", "numbers treated as final visual truth"),
    (r"pixel[- ]perfect" , "pixel-perfect claim without optical reasoning may be suspect"),
    (r"永远", "possible universal rule"),
    (r"总是", "possible universal rule"),
    (r"只要.*居中", "generic center-only advice"),
]


def contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, flags=re.I | re.S) for p in patterns)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_optical_alignment_output.py <review.md|plan.txt>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()

    missing = [name for name, pats in CHECKS.items() if not contains_any(text, pats)]
    bad = [(label, pat) for pat, label in BAD_PATTERNS if re.search(pat, lower, flags=re.I | re.S)]

    score = len(CHECKS) - len(missing)
    print(f"Optical-alignment reasoning score: {score}/{len(CHECKS)}")

    if missing:
        print("Missing reasoning areas:")
        for item in missing:
            print(f"- {item}")

    if bad:
        print("Potential slop / gotcha flags:")
        for label, pat in bad:
            print(f"- {label}: /{pat}/")

    if missing or bad:
        print("Result: REVISE before finalizing")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
