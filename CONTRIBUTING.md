# Contributing to Zero2Root

> **Language:** English · [Bahasa Indonesia](#berkontribusi-bahasa-indonesia) · [日本語](#貢献する-日本語)

Thanks for helping make Zero2Root better! Fixes, clearer explanations, and new translations are all welcome — however small.

## What you can help with

- **Fix typos and errors** in any lesson.
- **Improve an explanation** so it's easier to understand.
- **Keep the three languages in sync** — if you change a lesson in one language, try to mirror it in `id/`, `en/`, and `ja/`.
- **Add examples, diagrams, or analogies** that make a concept click.

## How the repo is organized

- Each topic folder (e.g. `networking/`) has `id/`, `en/`, `ja/` subfolders with the same lessons in each language.
- Every lesson has a `Curriculum ID` block at the top (`LC-001` … `LC-078`) and a **Key Terms** table right before section 1.
- Career paths live in [CAREERS.md](CAREERS.md) (the same data is in the `careers` section of `curriculum.json`; keep both in sync).
- The learning path lives in [ROADMAP.md](ROADMAP.md); book references in [BOOKS.md](BOOKS.md).

## Style guide

- **Plain language first.** Write for a beginner. Lead each section with a one- or two-sentence intro before the details.
- **Keep the Key Terms table** at the top of each lesson (2 columns: term, plain meaning).
- **Defense-focused.** Explain how attacks work *conceptually*, and how to detect and defend against them. Do **not** add ready-to-run exploit code, attack scripts, or step-by-step instructions for attacking systems you don't own.
- **Educational and authorized use only.** Examples assume a lab or a system you own or are permitted to test.
- **Keep tables tidy** — every row the same number of columns, with a proper `|:---|` separator.

## How to submit a change

1. Fork the repo and create a branch (`fix/typo-in-sqli`).
2. Make your change in the relevant language file(s).
3. Open a Pull Request describing what you changed and why.

Small PRs are easier to review and merge quickly. Thank you! ⭐

---

## Berkontribusi (Bahasa Indonesia)

Terima kasih sudah membantu! Perbaikan typo, penjelasan yang lebih jelas, dan terjemahan baru semuanya diterima.

- **Struktur:** tiap folder topik punya subfolder `id/`, `en/`, `ja/` berisi pelajaran yang sama. Tiap pelajaran punya blok `Curriculum ID` dan tabel **Istilah penting** sebelum bagian 1.
- **Gaya:** bahasa sederhana dan ramah pemula; pertahankan tabel Istilah penting; fokus ke deteksi & pertahanan, **bukan** skrip serangan siap pakai; hanya untuk edukasi dan pengujian berizin; jaga tabel tetap rapi.
- **Cara kirim:** fork → buat branch → ubah file bahasa terkait → buka Pull Request yang menjelaskan perubahanmu. PR kecil lebih cepat ditinjau.

## 貢献する (日本語)

改善にご協力ありがとうございます。誤字修正、より分かりやすい説明、新しい翻訳など、どんな小さな貢献も歓迎します。

- **構成:** 各トピックのフォルダに `id/`、`en/`、`ja/` のサブフォルダがあり、同じレッスンが各言語で入っている。各レッスンには `Curriculum ID` ブロックと、1節の前に **重要な用語** の表がある。
- **スタイル:** まず平易な言葉で、初心者向けに。重要な用語の表は残す。攻撃は*概念的に*説明し、検知と防御に重点を置く。すぐ使えるエクスプロイトや攻撃スクリプトは**加えない**。教育および許可された検証目的のみ。表は整えて保つ。
- **提出方法:** フォーク → ブランチ作成 → 該当言語のファイルを編集 → 変更内容を説明する Pull Request を開く。小さな PR ほど早くレビューできる。
