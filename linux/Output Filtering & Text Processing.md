# 🔍 Linux Filter Commands — Output Filtering & Text Processing

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Command | Bahasa Indonesia | English | 日本語 |
|---|---------|-----------------|---------|--------|
| 1 | `more` | Tampil dengan batas | Paged viewer | ページ表示 |
| 2 | `less` | Tampil lengkap & scrollable | Scrollable viewer | スクロール表示 |
| 3 | `head` | 10 baris pertama | First 10 lines | 最初の10行 |
| 4 | `tail` | 10 baris terakhir | Last 10 lines | 最後の10行 |
| 5 | `sort` | Urutkan alfabetis | Sort alphabetically | アルファベット順 |
| 6 | `grep` | Filter baris | Search & filter | 検索・絞り込み |
| 7 | `cut` | Buang kolom | Remove columns | 列を削除 |
| 8 | `tr` | Ganti karakter | Replace characters | 文字を置換 |
| 9 | `column` | Format tabel | Table formatter | テーブル形式 |
| 10 | `awk` | Cetak kolom tertentu | Print specific columns | 特定列を表示 |
| 11 | `sed` | Ganti teks (regex) | Substitute text (regex) | テキスト置換 |
| 12 | `wc` | Hitung baris/kata | Count lines/words | 行数・文字数 |

---

## 1. `more`

### 🇮🇩 Bahasa Indonesia
`more` digunakan untuk menampilkan isi file secara halaman per halaman. Namun memiliki beberapa keterbatasan:
- Tidak bisa di-scroll ke atas
- Tampilan yang sudah lewat **akan tertinggal di terminal** setelah keluar dengan `q`
- Cocok untuk melihat file secara cepat tanpa perlu navigasi

### 🇬🇧 English
`more` displays file contents page by page. However, it has limitations:
- Cannot scroll upward
- After exiting with `q`, **the displayed content remains in the terminal**
- Suitable for quick file previews without navigation needs

### 🇯🇵 日本語
`more` はファイルの内容をページ単位で表示します。ただし、いくつかの制限があります：
- 上にスクロールできない
- `q` で終了しても、**表示内容がターミナルに残る**
- ナビゲーション不要の素早いファイル確認に適している

```bash
more /etc/passwd
```

> 💡 **Tip:** Use `SPACE` to go to next page, `q` to quit.

---

## 2. `less`

### 🇮🇩 Bahasa Indonesia
`less` adalah versi yang lebih canggih dari `more`. Perbedaan utamanya:
- Bisa **di-scroll ke atas dan ke bawah**
- Menampilkan seluruh isi file
- Setelah keluar dengan `q`, **terminal akan bersih (stay clear)** — tidak ada sisa tampilan
- Lebih direkomendasikan untuk membaca file panjang

### 🇬🇧 English
`less` is a more advanced version of `more`. Key differences:
- Supports **scrolling both up and down**
- Displays the full file content
- After exiting with `q`, **the terminal clears (stay clear)** — no leftover output
- Recommended for reading long files

### 🇯🇵 日本語
`less` は `more` の高機能版です。主な違い：
- **上下にスクロール可能**
- ファイル全体を表示できる
- `q` で終了すると**ターミナルがクリアされる（stay clear）** — 表示が残らない
- 長いファイルの読み込みに推奨される

```bash
less /etc/passwd
```

> 💡 **Tip:** Use arrow keys or `j`/`k` to scroll, `/keyword` to search inside, `q` to quit.

---

## 3. `head`

### 🇮🇩 Bahasa Indonesia
`head` menampilkan **10 baris pertama** dari sebuah file secara default. Berguna untuk melihat header atau awal dari sebuah file log atau data.

### 🇬🇧 English
`head` displays the **first 10 lines** of a file by default. Useful for previewing headers or the beginning of log/data files.

### 🇯🇵 日本語
`head` はデフォルトでファイルの**最初の10行**を表示します。ログファイルやデータファイルの先頭を確認するのに便利です。

```bash
head /etc/passwd

# Custom: show first 20 lines
head -n 20 /etc/passwd
```

---

## 4. `tail`

### 🇮🇩 Bahasa Indonesia
`tail` adalah kebalikan dari `head` — menampilkan **10 baris terakhir** dari sebuah file. Sangat berguna untuk memantau file log secara real-time dengan flag `-f`.

### 🇬🇧 English
`tail` is the opposite of `head` — it displays the **last 10 lines** of a file. Extremely useful for monitoring log files in real-time using the `-f` flag.

### 🇯🇵 日本語
`tail` は `head` の反対で、ファイルの**最後の10行**を表示します。`-f` フラグを使うとログファイルをリアルタイム監視できます。

```bash
tail /etc/passwd

# Real-time log monitoring
tail -f /var/log/syslog

# Custom: show last 20 lines
tail -n 20 /etc/passwd
```

---

## 5. `sort`

### 🇮🇩 Bahasa Indonesia
`sort` mengurutkan isi file atau output berdasarkan **urutan alfabet (A–Z)** secara default. Bisa dikombinasikan dengan pipe (`|`) untuk mengurutkan output dari perintah lain.

### 🇬🇧 English
`sort` arranges file contents or output in **alphabetical order (A–Z)** by default. Can be combined with pipes (`|`) to sort output from other commands.

### 🇯🇵 日本語
`sort` はファイルの内容や出力を**アルファベット順（A–Z）**に並べ替えます。パイプ（`|`）と組み合わせて他コマンドの出力を並べ替えることができます。

```bash
sort /etc/passwd

# Reverse order (Z-A)
sort -r /etc/passwd

# Sort numerically
sort -n file.txt
```

---

## 6. `grep`

### 🇮🇩 Bahasa Indonesia
`grep` singkatan dari **Global Regular Expression Print**. Fungsinya untuk **mencari dan memfilter** baris dari file atau output yang sesuai dengan pola tertentu. Sangat powerful jika dikombinasikan dengan regex.

### 🇬🇧 English
`grep` stands for **Global Regular Expression Print**. It is used to **search and filter** lines from files or output that match a specific pattern. Extremely powerful when combined with regex.

### 🇯🇵 日本語
`grep` は **Global Regular Expression Print** の略です。特定のパターンに一致する行を**検索・フィルタリング**するために使用します。正規表現と組み合わせると非常に強力です。

```bash
# Show lines containing "root"
grep "root" /etc/passwd

# Exclude lines with "false" or "nologin"
grep -v "false\|nologin" /etc/passwd

# Case insensitive search
grep -i "ROOT" /etc/passwd
```

| Flag | Function |
|------|----------|
| `-v` | Invert match (exclude pattern) |
| `-i` | Case insensitive |
| `-n` | Show line numbers |
| `-r` | Recursive search in directory |
| `-E` | Extended regex |

---

## 7. `cut`

### 🇮🇩 Bahasa Indonesia
`cut` digunakan untuk **membuang atau mengekstrak bagian tertentu** dari setiap baris dalam file. Biasanya digunakan untuk memilih kolom berdasarkan delimiter tertentu (seperti `:` pada `/etc/passwd`).

### 🇬🇧 English
`cut` is used to **remove or extract specific parts** from each line of a file. Commonly used to select columns based on a specific delimiter (like `:` in `/etc/passwd`).

### 🇯🇵 日本語
`cut` はファイルの各行から**特定の部分を削除または抽出**するために使用します。`/etc/passwd` の `:` のような区切り文字を基準に列を選択するのによく使われます。

```bash
# Extract field 1 (username) using ":" as delimiter
cut -d":" -f1 /etc/passwd

# Extract multiple fields
cut -d":" -f1,7 /etc/passwd
```

---

## 8. `tr`

### 🇮🇩 Bahasa Indonesia
`tr` (translate) digunakan untuk **mengganti atau menghapus karakter** dari input. Misalnya, mengganti karakter `:` menjadi spasi ` ` agar output lebih mudah dibaca.

### 🇬🇧 English
`tr` (translate) is used to **replace or delete characters** from input. For example, replacing `:` with a space ` ` to make the output more readable.

### 🇯🇵 日本語
`tr`（translate）は入力から**文字を置換または削除**するために使用します。例えば、`:` をスペース ` ` に置き換えて出力を読みやすくします。

```bash
# Replace ":" with space
cat /etc/passwd | tr ":" " "

# Convert lowercase to uppercase
cat file.txt | tr 'a-z' 'A-Z'

# Delete specific characters
cat file.txt | tr -d ':'
```

---

## 9. `column`

### 🇮🇩 Bahasa Indonesia
`column` digunakan untuk **memformat output menjadi tampilan tabel** yang lebih rapi dan mudah dibaca. Biasanya dikombinasikan dengan `tr` untuk menghasilkan tabel yang terstruktur.

### 🇬🇧 English
`column` is used to **format output into a neat table layout** for easier reading. Usually combined with `tr` to produce structured, readable tables.

### 🇯🇵 日本語
`column` は出力を**きれいなテーブル形式にフォーマット**して読みやすくするために使用します。通常 `tr` と組み合わせて整理されたテーブルを生成します。

```bash
# Format passwd file as a table
cat /etc/passwd | tr ":" " " | column -t
```

---

## 10. `awk`

### 🇮🇩 Bahasa Indonesia
`awk` adalah bahasa pemrograman pemrosesan teks yang sangat powerful. Fungsi utamanya adalah untuk **mencetak kolom tertentu** dari setiap baris output. Misalnya, `$1` merujuk ke kolom pertama, `$NF` merujuk ke kolom terakhir.

### 🇬🇧 English
`awk` is a powerful text processing programming language. Its primary use is to **print specific columns** from each line of output. For example, `$1` refers to the first column, `$NF` refers to the last column.

### 🇯🇵 日本語
`awk` は強力なテキスト処理プログラミング言語です。主な用途は出力の各行から**特定の列を表示**することです。例えば、`$1` は最初の列、`$NF` は最後の列を指します。

```bash
cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'
```

**Output:**
```
root /bin/bash
sync /bin/sync
postgres /bin/bash
mrb3n /bin/bash
cry0l1t3 /bin/bash
htb-student /bin/bash
```

| Variable | Meaning |
|----------|---------|
| `$1` | First column |
| `$2` | Second column |
| `$NF` | Last column (N = total fields) |
| `$0` | Entire line |
| `NR` | Current line number |

---

## 11. `sed`

### 🇮🇩 Bahasa Indonesia
`sed` (Stream Editor) adalah alat untuk **mengganti teks menggunakan pola regex** pada input. Format umumnya adalah `s/pola_lama/pola_baru/g`:
- `s` = substitute (ganti)
- `/g` = global (ganti semua kemunculan, bukan hanya yang pertama)

### 🇬🇧 English
`sed` (Stream Editor) is a tool for **substituting text using regex patterns** on input. The general format is `s/old_pattern/new_pattern/g`:
- `s` = substitute command
- `/g` = global flag (replace all occurrences, not just the first)

### 🇯🇵 日本語
`sed`（Stream Editor）は入力に対して**正規表現パターンを使ってテキストを置換**するツールです。一般的な形式は `s/古いパターン/新しいパターン/g`：
- `s` = substitute（置換）コマンド
- `/g` = global フラグ（最初だけでなくすべての出現箇所を置換）

```bash
cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'
```

**Output:**
```
root /HTB/bash
sync /HTB/sync
postgres /HTB/bash
mrb3n /HTB/bash
cry0l1t3 /HTB/bash
htb-student /HTB/bash
```

---

## 12. `wc`

### 🇮🇩 Bahasa Indonesia
`wc` (Word Count) digunakan untuk **menghitung jumlah baris, kata, atau karakter** dalam file atau output. Flag yang paling umum digunakan dalam filtering adalah `-l` untuk menghitung jumlah baris hasil match.

### 🇬🇧 English
`wc` (Word Count) is used to **count the number of lines, words, or characters** in a file or output. The most commonly used flag in filtering is `-l` to count the number of matched lines.

### 🇯🇵 日本語
`wc`（Word Count）はファイルや出力の**行数・単語数・文字数を数える**ために使用します。フィルタリングで最もよく使われるフラグは、マッチした行数を数える `-l` です。

```bash
cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | wc -l
```

**Output:**
```
6
```

| Flag | Function |
|------|----------|
| `-l` | Count lines |
| `-w` | Count words |
| `-c` | Count bytes/characters |

---

## 🔗 Putting It All Together / Menggabungkan Semuanya / すべてを組み合わせる

One-liner pipeline combining all tools:

```bash
cat /etc/passwd \
  | grep -v "false\|nologin" \   # Remove service accounts
  | tr ":" " " \                 # Replace ":" with space
  | awk '{print $1, $NF}' \      # Print username and shell
  | sed 's/bin/HTB/g' \          # Replace "bin" with "HTB"
  | sort \                       # Sort alphabetically
  | wc -l                        # Count total results
```

### Pipeline Diagram

```
[cat /etc/passwd]
       │
       ▼
[grep -v "false\|nologin"]  ── filter out service accounts
       │
       ▼
[tr ":" " "]  ── make columns readable
       │
       ▼
[awk '{print $1, $NF}']  ── extract username & shell
       │
       ▼
[sed 's/bin/HTB/g']  ── substitute text
       │
       ▼
[sort]  ── alphabetical order
       │
       ▼
[wc -l]  ── count output
```

---

## 📊 Command Comparison Table

| Command | Input | Output | Scrollable | Terminal Clean After Exit |
|---------|-------|--------|-----------|--------------------------|
| `more` | File | Paged | ❌ | ❌ Stays |
| `less` | File | Paged | ✅ | ✅ Clears |
| `head` | File | First N lines | — | ✅ |
| `tail` | File | Last N lines | — | ✅ |
| `sort` | File/pipe | Sorted lines | — | ✅ |
| `grep` | File/pipe | Matched lines | — | ✅ |
| `cut` | File/pipe | Extracted columns | — | ✅ |
| `tr` | Pipe | Translated chars | — | ✅ |
| `column` | Pipe | Table formatted | — | ✅ |
| `awk` | Pipe | Selected fields | — | ✅ |
| `sed` | Pipe | Substituted text | — | ✅ |
| `wc` | File/pipe | Count | — | ✅ |

---

## 🧠 Quick Reference Cheatsheet

```bash
# View files
more file.txt          # paged, stays in terminal
less file.txt          # paged, scrollable, clean exit
head -n 10 file.txt    # first 10 lines
tail -n 10 file.txt    # last 10 lines
tail -f file.txt       # real-time follow

# Filter & search
grep "pattern" file.txt          # search for pattern
grep -v "pattern" file.txt       # exclude pattern
grep -i "pattern" file.txt       # case-insensitive

# Transform
sort file.txt                    # sort A-Z
sort -r file.txt                 # sort Z-A
cut -d":" -f1 file.txt           # extract column 1
tr ":" " " < file.txt            # replace char
column -t file.txt               # table format

# Advanced
awk '{print $1, $NF}' file.txt   # print first & last column
sed 's/old/new/g' file.txt       # substitute text globally
wc -l file.txt                   # count lines
```

---

> 📚 **References:**  
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)  
> - `man` pages: `man grep`, `man awk`, `man sed`  
> - GNU Coreutils Documentation  

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.