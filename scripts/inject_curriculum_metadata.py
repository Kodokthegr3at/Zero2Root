#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject standardized curriculum metadata block into LearnCybersecurity markdown files."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "curriculum.json"

MARKER_START = "<!-- LC-CURRICULUM-START -->"
MARKER_END = "<!-- LC-CURRICULUM-END -->"


def build_block(entry: dict) -> str:
    books = "; ".join(entry.get("books_short", []))
    prereq = entry.get("prerequisites", "-")
    if prereq == "none":
        prereq = "-"
    return (
        f"{MARKER_START}\n"
        f"> **Curriculum ID:** `{entry['id']}` | **Phase {entry['phase']}:** {entry['phase_name']}  \n"
        f"> **Est. study:** {entry['hours']} | **Level:** {entry['level']}  \n"
        f"> **Prerequisites:** {prereq}  \n"
        f"> **Book map:** {books}\n"
        f"{MARKER_END}\n"
    )


def inject(content: str, block: str) -> str:
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n?",
        re.DOTALL,
    )
    if pattern.search(content):
        return pattern.sub(block, content, count=1)

    lines = content.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            break
    j = insert_at
    while j < len(lines) and (
        lines[j].startswith(">") or lines[j].strip() in ("---", "") or MARKER_START in lines[j]
    ):
        j += 1
    lines.insert(j, "\n" + block)
    return "".join(lines)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    updated = 0
    for entry in manifest["lessons"]:
        path = ROOT / entry["path"]
        if not path.exists():
            print(f"SKIP missing: {entry['path']}")
            continue
        block = build_block(entry)
        text = path.read_text(encoding="utf-8")
        new_text = inject(text, block)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"OK {entry['id']} {entry['path']}")
    print(f"\nDone. Updated {updated} files.")


if __name__ == "__main__":
    main()
