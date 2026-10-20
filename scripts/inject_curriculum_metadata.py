#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject the curriculum metadata block into every Zero2Root lesson (id/en/ja).

Lessons that already have a block are left alone, since many were hand-tuned
after translation. Pass --force to regenerate every block from curriculum.json.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "curriculum.json"
LANGS = ("en", "id", "ja")

MARKER_START = "<!-- LC-CURRICULUM-START -->"
MARKER_END = "<!-- LC-CURRICULUM-END -->"

LABELS = {
    "en": ("Curriculum ID", "Phase {}", "Est. study", "Level", "Prerequisites", "Book map"),
    "id": ("ID Kurikulum", "Fase {}", "Estimasi belajar", "Level", "Prasyarat", "Peta buku"),
    "ja": ("カリキュラムID", "フェーズ{}", "想定学習時間", "レベル", "前提科目", "書籍対応"),
}
LEVELS = {
    "id": {"Beginner": "Pemula", "Intermediate": "Menengah", "Advanced": "Lanjutan"},
    "ja": {"Beginner": "初級", "Intermediate": "中級", "Advanced": "上級"},
}
HOURS = {"en": "{}h", "id": "{} jam", "ja": "{}時間"}


def build_block(entry: dict, lang: str) -> str:
    cid, phase, study, level, prereq_l, books_l = LABELS[lang]
    hours = HOURS[lang].format(entry["hours"].rstrip("h"))
    lvl = LEVELS.get(lang, {}).get(entry["level"], entry["level"])
    prereq = entry.get("prerequisites", "-")
    if prereq == "none":
        prereq = "-"
    books = "; ".join(entry.get("books_short", []))
    return (
        f"{MARKER_START}\n"
        f"> **{cid}:** `{entry['id']}` | **{phase.format(entry['phase'])}:** {entry['phase_name']}\n"
        f"> **{study}:** {hours} | **{level}:** {lvl}\n"
        f"> **{prereq_l}:** {prereq}\n"
        f"> **{books_l}:** {books}\n"
        f"{MARKER_END}\n"
    )


def inject(content: str, block: str, force: bool) -> str:
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n?",
        re.DOTALL,
    )
    if pattern.search(content):
        return pattern.sub(lambda _: block, content, count=1) if force else content

    lines = content.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            break
    j = insert_at
    while j < len(lines) and (lines[j].startswith(">") or lines[j].strip() in ("---", "")):
        j += 1
    lines.insert(j, block + "\n")
    return "".join(lines)


def main() -> None:
    force = "--force" in sys.argv[1:]
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    updated = missing = 0
    for entry in manifest["lessons"]:
        for lang in LANGS:
            path = ROOT / entry["dir"] / lang / entry["file"]
            rel = path.relative_to(ROOT)
            if not path.exists():
                print(f"SKIP missing: {rel}")
                missing += 1
                continue
            text = path.read_text(encoding="utf-8")
            new_text = inject(text, build_block(entry, lang), force)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                updated += 1
                print(f"OK {entry['id']} {rel}")
    print(f"\nDone. Updated {updated} files, {missing} missing.")


if __name__ == "__main__":
    main()
