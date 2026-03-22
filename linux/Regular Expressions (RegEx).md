# 🔤 Regular Expressions (RegEx)

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2025 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | What is RegEx? | Apa itu RegEx? | What is RegEx? | RegEx とは？ |
| 2 | Grouping Operators | Operator pengelompokan | Grouping operators | グループ化演算子 |
| 3 | OR Operator | Operator OR | OR operator | OR 演算子 |
| 4 | AND Operator | Operator AND | AND operator | AND 演算子 |
| 5 | Metacharacters | Karakter spesial | Special characters | メタキャラクター |
| 6 | Practice Tasks | Latihan soal | Practice exercises | 練習問題 |

---

## 1. 🎯 What is RegEx?

### 🇮🇩 Bahasa Indonesia
**Regular Expression (RegEx)** adalah urutan karakter dan simbol yang membentuk **pola pencarian**. Bayangkan RegEx sebagai filter yang sangat bisa dikustomisasi — ia menyaring teks untuk menemukan tepat apa yang kita butuhkan.

RegEx bisa digunakan untuk:
- **Mencari** pola teks secara presisi
- **Mengganti** teks secara massal
- **Memvalidasi** input (email, password, nomor telepon)
- **Memfilter** output dari perintah lain

RegEx tersedia di banyak bahasa pemrograman dan tools seperti `grep`, `sed`, `awk`, Python, JavaScript, dll.

### 🇬🇧 English
A **Regular Expression (RegEx)** is a sequence of characters and symbols that form a **search pattern**. Think of RegEx as a highly customizable filter — it sifts through text to find exactly what you need.

RegEx can be used to:
- **Search** for text patterns with precision
- **Replace** text in bulk
- **Validate** input (emails, passwords, phone numbers)
- **Filter** output from other commands

RegEx is available in many programming languages and tools like `grep`, `sed`, `awk`, Python, JavaScript, etc.

### 🇯🇵 日本語
**正規表現（RegEx）** は**検索パターン**を形成する文字とシンボルのシーケンスです。RegEx は非常にカスタマイズ可能なフィルターと考えてください — 必要なものを正確に見つけるためにテキストをふるいにかけます。

RegEx の用途：
- テキストパターンを**精密に検索**する
- テキストを一括**置換**する
- 入力（メール、パスワード、電話番号）を**検証**する
- 他のコマンドの出力を**フィルタリング**する

`grep`、`sed`、`awk`、Python、JavaScript など多くのツールや言語で使えます。

---

## 2. 🔲 Grouping Operators

### 🇮🇩 Bahasa Indonesia
RegEx menggunakan **tiga jenis tanda kurung** yang masing-masing memiliki fungsi berbeda untuk mendefinisikan pola pencarian.

### 🇬🇧 English
RegEx uses **three types of brackets**, each with a different function for defining search patterns.

### 🇯🇵 日本語
RegEx は検索パターンを定義するために、それぞれ異なる機能を持つ**3種類の括弧**を使用します。

---

| Operator | Symbol | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|----------|--------|--------------|----------------|---------|
| **Round brackets** | `(a)` | Mengelompokkan bagian dari regex. Di dalam kurung bisa didefinisikan pola lebih lanjut yang diproses bersama | Group parts of a regex. Inside, you can define further patterns to be processed together | regex の一部をグループ化。括弧内にさらにパターンを定義して一緒に処理できる |
| **Square brackets** | `[a-z]` | Mendefinisikan **kelas karakter**. Di dalam kurung, tentukan daftar karakter yang dicari | Define a **character class**. Inside, specify a list of characters to search for | **文字クラス**を定義。括弧内に検索する文字のリストを指定する |
| **Curly brackets** | `{1,10}` | Mendefinisikan **quantifier**. Menentukan berapa kali pola sebelumnya harus diulang | Define a **quantifier**. Specify how many times the previous pattern should repeat | **量指定子**を定義。前のパターンが何回繰り返されるべきかを指定する |
| **OR operator** | `\|` | Menampilkan hasil jika **salah satu** dari dua ekspresi cocok | Shows results when **one of** the two expressions matches | 2つの式のうち**いずれか一方**が一致した場合に結果を表示 |
| **AND operator** | `.*` | Menampilkan hasil hanya jika **kedua** ekspresi ada dan cocok sesuai urutan | Shows results only when **both** expressions are present and match in the specified order | 両方の式が指定された順序で存在し一致した場合**のみ**結果を表示 |

---

## 3. ➕ OR Operator (`|`)

### 🇮🇩 Bahasa Indonesia
Operator `|` (OR) mencari baris yang mengandung **salah satu** dari pola yang diberikan. Untuk menggunakan operator ini dengan `grep`, diperlukan flag `-E` (extended regex).

### 🇬🇧 English
The `|` (OR) operator searches for lines containing **at least one** of the given patterns. To use this operator with `grep`, the `-E` (extended regex) flag is required.

### 🇯🇵 日本語
`|`（OR）演算子は、指定されたパターンの**少なくとも一つ**を含む行を検索します。`grep` でこの演算子を使うには `-E`（拡張正規表現）フラグが必要です。

```bash
# Search for lines containing "my" OR "false"
$ grep -E "(my|false)" /etc/passwd

lxd:x:105:65534::/var/lib/lxd/:/bin/false
pollinate:x:109:1::/var/cache/pollinate:/bin/false
mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```

```
Pattern:  (my|false)
              │
     ┌────────┴────────┐
     ▼                 ▼
   "my"             "false"
  matches?          matches?
     │                 │
     └────────┬─────────┘
              ▼
     Either one = SHOW LINE
```

> All 3 lines are shown because each line contains either `my` (mysql) or `false` (/bin/false), or both.

---

## 4. ✖️ AND Operator (`.*`)

### 🇮🇩 Bahasa Indonesia
Operator `.*` (AND) hanya menampilkan baris yang mengandung **kedua** pola secara berurutan. `.*` berarti "karakter apa pun, berapa pun banyaknya" di antara dua pola — sehingga kedua kata harus ada dalam satu baris.

### 🇬🇧 English
The `.*` (AND) operator only shows lines that contain **both** patterns in order. `.*` means "any character, any number of times" between two patterns — so both words must exist in the same line.

### 🇯🇵 日本語
`.*`（AND）演算子は、**両方の**パターンを順番に含む行のみを表示します。`.*` は2つのパターンの間に「任意の文字が何文字でも」という意味で — 両方の単語が同じ行に存在する必要があります。

```bash
# Search for lines containing BOTH "my" AND "false" (in that order)
$ grep -E "(my.*false)" /etc/passwd

mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```

```
Pattern:  (my.*false)
            │  │   │
            │  │   └── "false" must appear AFTER "my"
            │  └────── any characters in between (.*)
            └────────── "my" must appear first

mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
  ↑ "my" found here              ↑ "false" found here → MATCH ✓

lxd:x:105:65534::/var/lib/lxd/:/bin/false
  ↑ no "my" found → NO MATCH ✗
```

### Alternative: Chained grep

```bash
# Same result using two grep pipes (AND logic)
$ grep -E "my" /etc/passwd | grep -E "false"

mysql:x:116:120:MySQL Server,,:/nonexistent:/bin/false
```

> Both approaches produce the same result — chained `grep` is more readable; `.*` is more compact.

---

## 5. 🔣 RegEx Metacharacters — Quick Reference

### 🇮🇩 Bahasa Indonesia
**Metacharacter** adalah simbol spesial dalam regex yang mendefinisikan **struktur** pencarian, bukan karakter literal.

### 🇬🇧 English
**Metacharacters** are special symbols in regex that define the **structure** of the search, not literal characters.

### 🇯🇵 日本語
**メタキャラクター**は、文字そのものではなく検索の**構造**を定義する正規表現の特殊シンボルです。

---

| Metacharacter | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 | Example |
|--------------|---------|------------|---------|---------|
| `.` | Karakter apa pun (kecuali newline) | Any character (except newline) | 任意の1文字（改行除く） | `a.c` → `abc`, `a1c` |
| `*` | 0 atau lebih dari karakter sebelumnya | 0 or more of the previous character | 直前の文字が0回以上 | `ab*` → `a`, `ab`, `abb` |
| `+` | 1 atau lebih dari karakter sebelumnya | 1 or more of the previous character | 直前の文字が1回以上 | `ab+` → `ab`, `abb` |
| `?` | 0 atau 1 dari karakter sebelumnya | 0 or 1 of the previous character | 直前の文字が0回か1回 | `ab?` → `a`, `ab` |
| `^` | Awal dari baris | Beginning of line | 行の先頭 | `^root` |
| `$` | Akhir dari baris | End of line | 行の末尾 | `bash$` |
| `[abc]` | Salah satu karakter dalam list | One of the listed characters | リスト内のいずれか1文字 | `[abc]` → `a`, `b`, or `c` |
| `[^abc]` | Karakter yang **tidak** ada dalam list | Character **not** in the list | リストにない文字 | `[^abc]` → anything except a, b, c |
| `[a-z]` | Semua huruf kecil a sampai z | All lowercase letters a to z | 小文字 a から z | `[a-z]+` |
| `[0-9]` | Semua digit 0 sampai 9 | All digits 0 to 9 | 数字 0 から 9 | `[0-9]+` |
| `\d` | Digit (sama dengan `[0-9]`) | Digit (same as `[0-9]`) | 数字（`[0-9]` と同じ） | `\d+` → `123` |
| `\w` | Word character (`[a-zA-Z0-9_]`) | Word character (`[a-zA-Z0-9_]`) | 単語文字 | `\w+` → `hello_123` |
| `\s` | Whitespace (spasi, tab) | Whitespace (space, tab) | 空白文字（スペース、タブ） | `\s+` |
| `{n}` | Tepat n kali pengulangan | Exactly n repetitions | ちょうど n 回繰り返し | `a{3}` → `aaa` |
| `{n,m}` | Antara n dan m kali pengulangan | Between n and m repetitions | n 回以上 m 回以下の繰り返し | `a{2,4}` → `aa`, `aaa`, `aaaa` |
| `\` | Escape — karakter berikutnya literal | Escape — next character is literal | エスケープ — 次の文字をリテラルとして扱う | `\.` → literal dot |

---

## 6. 🏋️ Practice Tasks — `/etc/ssh/sshd_config`

### 🇮🇩 Bahasa Indonesia
Latihan berikut menggunakan file `/etc/ssh/sshd_config` — file konfigurasi SSH yang nyata di sistem Linux. Ini adalah latihan penting karena file ini sering dianalisis saat melakukan audit keamanan sistem.

### 🇬🇧 English
The following exercises use the `/etc/ssh/sshd_config` file — a real SSH configuration file on Linux systems. This is important practice because this file is often analyzed during system security audits.

### 🇯🇵 日本語
以下の練習は `/etc/ssh/sshd_config` ファイル — Linux システム上の実際の SSH 設定ファイルを使用します。このファイルはシステムセキュリティ監査時によく分析されるため、重要な練習です。

---

| # | 🇮🇩 Tugas | 🇬🇧 Task | 🇯🇵 タスク | Answer |
|---|----------|---------|----------|--------|
| 1 | Tampilkan semua baris yang **tidak mengandung** karakter `#` | Show all lines that **do not contain** the `#` character | `#` 文字を**含まない**すべての行を表示 | 👇 |
| 2 | Cari semua baris yang mengandung kata yang **dimulai dengan** `Permit` | Search for all lines containing a word that **starts with** `Permit` | `Permit` で**始まる**単語を含むすべての行を検索 | 👇 |
| 3 | Cari semua baris yang mengandung kata yang **diakhiri dengan** `Authentication` | Search for all lines containing a word **ending with** `Authentication` | `Authentication` で**終わる**単語を含むすべての行を検索 | 👇 |
| 4 | Cari semua baris yang mengandung kata `Key` | Search for all lines containing the word `Key` | `Key` という単語を含むすべての行を検索 | 👇 |
| 5 | Cari semua baris yang **dimulai dengan** `Password` dan mengandung `yes` | Search for all lines **beginning with** `Password` and containing `yes` | `Password` で**始まり** `yes` を含むすべての行を検索 | 👇 |
| 6 | Cari semua baris yang **diakhiri dengan** `yes` | Search for all lines that **end with** `yes` | `yes` で**終わる**すべての行を検索 | 👇 |

---

### ✅ Solutions

```bash
# Task 1 — Lines NOT containing "#"
grep -v "#" /etc/ssh/sshd_config

# Task 2 — Lines with a word STARTING with "Permit"
grep -E "Permit\w+" /etc/ssh/sshd_config

# Task 3 — Lines with a word ENDING with "Authentication"
grep -E "\w+Authentication" /etc/ssh/sshd_config

# Task 4 — Lines containing the word "Key"
grep "Key" /etc/ssh/sshd_config

# Task 5 — Lines BEGINNING with "Password" AND containing "yes"
grep -E "^Password.*yes" /etc/ssh/sshd_config

# Task 6 — Lines ENDING with "yes"
grep -E "yes$" /etc/ssh/sshd_config
```

### Solution Breakdown

```
Task 1:  grep -v "#"
               │
               └── -v = invert match (exclude lines WITH #)

Task 2:  Permit\w+
         │      │
         │      └── \w+ = one or more word characters after "Permit"
         └── literal "Permit"

Task 3:  \w+Authentication
         │   │
         │   └── literal "Authentication" at the end
         └── \w+ = one or more word characters before it

Task 5:  ^Password.*yes
         │         │  │
         │         │  └── "yes" anywhere after
         │         └── .* = any characters in between
         └── ^ = must be at the START of line

Task 6:  yes$
         │  │
         │  └── $ = must be at the END of line
         └── literal "yes"
```

---

## 🔗 grep + RegEx Flags Reference

| Flag | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `-E` | Aktifkan extended regex | Enable extended regex | 拡張正規表現を有効化 |
| `-i` | Case insensitive | Case insensitive search | 大文字小文字を区別しない |
| `-v` | Invert match (exclude) | Invert match (exclude pattern) | マッチを反転（除外） |
| `-n` | Tampilkan nomor baris | Show line numbers | 行番号を表示 |
| `-r` | Rekursif (cari di seluruh direktori) | Recursive search in directory | ディレクトリを再帰的に検索 |
| `-c` | Hitung jumlah baris yang cocok | Count matching lines | 一致する行数を数える |
| `-o` | Tampilkan hanya bagian yang cocok | Show only the matching part | 一致した部分のみ表示 |

---

## 🧠 Quick Reference Cheatsheet

```bash
# Basic grep with regex
grep "pattern" file.txt               # literal search
grep -E "pattern" file.txt            # extended regex
grep -v "pattern" file.txt            # exclude pattern
grep -i "pattern" file.txt            # case insensitive

# OR / AND logic
grep -E "(one|two)" file.txt          # OR: contains "one" or "two"
grep -E "(one.*two)" file.txt         # AND: contains both in order
grep "one" file.txt | grep "two"      # AND: chained pipes

# Anchors
grep -E "^word" file.txt              # lines STARTING with "word"
grep -E "word$" file.txt              # lines ENDING with "word"

# Character classes
grep -E "[0-9]+" file.txt             # lines with digits
grep -E "[a-z]+" file.txt             # lines with lowercase letters
grep -E "\w+" file.txt                # lines with word characters

# Quantifiers
grep -E "a{3}" file.txt               # exactly 3 "a"s
grep -E "a{2,4}" file.txt             # 2 to 4 "a"s

# Practical sshd_config examples
grep -v "#" /etc/ssh/sshd_config              # no comments
grep -E "^Password.*yes" /etc/ssh/sshd_config # password + yes
grep -E "yes$" /etc/ssh/sshd_config           # ends with yes
grep -E "Permit\w+" /etc/ssh/sshd_config      # starts with Permit
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man grep`, `man regex`
> - [regex101.com](https://regex101.com) — interactive RegEx tester
> - GNU grep documentation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.