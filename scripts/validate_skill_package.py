#!/usr/bin/env python3
"""Validate the structure of the optical-alignment skill package.

This is a lightweight package validator. It checks the conventions that matter
for this skill: SKILL.md front matter, moderate length, expected reference files,
script presence, and basic progressive-disclosure links.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "references/framework.md",
    "references/typography.md",
    "references/spacing-icons.md",
    "references/implementation.md",
    "references/rubric.md",
    "references/source-map.md",
    "assets/review-template.md",
    "assets/agents-snippet.md",
    "scripts/check_optical_alignment_output.py",
    "evals/trigger-evals.json",
    "evals/task-evals.md",
]

NAME_RE = re.compile(r"^name:\s*([a-z0-9][a-z0-9-]{0,63})\s*$", re.M)
DESC_RE = re.compile(r"^description:\s*(.+)\s*$", re.M)


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    if not root.exists():
        return fail(f"root does not exist: {root}")

    missing = [p for p in REQUIRED if not (root / p).exists()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        return fail("SKILL.md must start with YAML front matter")
    try:
        _, front, body = skill.split("---", 2)
    except ValueError:
        return fail("SKILL.md front matter must be enclosed by --- markers")

    name = NAME_RE.search(front)
    desc = DESC_RE.search(front)
    if not name:
        return fail("front matter must include lowercase hyphenated name")
    if not desc:
        return fail("front matter must include description")
    if len(desc.group(1)) < 80:
        return fail("description is too short to trigger reliably")
    if len(skill.splitlines()) > 500:
        return fail("SKILL.md should stay under 500 lines")

    for ref in REQUIRED:
        if ref.startswith(("references/", "assets/", "scripts/")) and ref not in skill:
            # Source map and some eval files need not be mentioned in SKILL.md.
            if ref not in {"references/source-map.md", "scripts/validate_skill_package.py"}:
                return fail(f"{ref} is not referenced from SKILL.md")

    print("PASS: optical-alignment skill package structure is valid")
    print(f"name: {name.group(1)}")
    print(f"SKILL.md lines: {len(skill.splitlines())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
