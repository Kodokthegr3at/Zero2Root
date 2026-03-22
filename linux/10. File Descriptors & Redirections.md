# 📂 File Descriptors & Redirections

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | File Descriptors | Deskriptor file | What are FDs? | ファイルディスクリプタとは |
| 2 | STDIN / STDOUT | Input & Output standar | Standard I/O | 標準入出力 |
| 3 | STDOUT & STDERR | Output & Error | Output & Error streams | 出力とエラー |
| 4 | Redirect STDOUT → File | Simpan output ke file | Save output to file | 出力をファイルへ |
| 5 | Redirect STDOUT & STDERR | Pisahkan output & error | Separate output & error | 出力とエラーを別々に |
| 6 | Redirect STDIN | Input dari file | Input from file | ファイルから入力 |
| 7 | Append `>>` | Tambahkan ke file | Append to file | ファイルに追記 |
| 8 | Here-document `<<` | Stream input ke file | Stream input to file | ストリーム入力 |
| 9 | Pipes `\|` | Sambungkan perintah | Chain commands | コマンドを繋げる |

---

## 1. 📌 File Descriptors (FD)

### 🇮🇩 Bahasa Indonesia
**File Descriptor (FD)** adalah referensi yang dikelola oleh kernel Linux untuk mengidentifikasi dan mengelola operasi Input/Output (I/O). Setiap file, socket, atau resource I/O yang sedang terbuka akan mendapat nomor unik (FD).

Bayangkan FD seperti **nomor tiket penitipan jas**:
- Tiketnya = File Descriptor
- Jasnya = File atau resource
- Petugas = Operating System

Tanpa nomor tiket, OS tidak tahu resource mana yang harus diakses. Di Windows, konsep ini disebut **file handle**.

### 🇬🇧 English
A **File Descriptor (FD)** is a reference maintained by the Linux kernel to identify and manage Input/Output (I/O) operations. Every open file, socket, or I/O resource receives a unique number (FD).

Think of it like a **coat check ticket**:
- The ticket = File Descriptor
- The coat = File or resource
- The attendant = Operating System

Without the ticket number, the OS wouldn't know which resource to interact with. In Windows, this concept is called a **file handle**.

### 🇯🇵 日本語
**ファイルディスクリプタ（FD）** は、Linuxカーネルがジ管理する参照番号で、Input/Output（I/O）操作を識別・管理するために使われます。開かれているファイル、ソケット、またはI/Oリソースはそれぞれ一意の番号（FD）を持ちます。

クロークの**預かり番号票**と考えると分かりやすいです：
- チケット = ファイルディスクリプタ
- コート = ファイルやリソース
- 係員 = オペレーティングシステム

チケットがなければ、OSはどのリソースにアクセスすべきか分かりません。Windowsではこの概念を**ファイルハンドル**と呼びます。

---

### 📊 Default File Descriptors in Linux

| FD | Name | Stream | Description |
|----|------|--------|-------------|
| `0` | **STDIN** | Input | Standard Input — keyboard / file input |
| `1` | **STDOUT** | Output | Standard Output — normal program output |
| `2` | **STDERR** | Output | Standard Error — error messages only |

```
┌─────────────────────────────────────────┐
│              Linux Process              │
│                                         │
│  [FD 0 - STDIN]  ──►  Program Input    │
│  [FD 1 - STDOUT] ◄──  Normal Output    │
│  [FD 2 - STDERR] ◄──  Error Output     │
└─────────────────────────────────────────┘
```

---

## 2. 🔄 STDIN & STDOUT

### 🇮🇩 Bahasa Indonesia
Saat menjalankan `cat`, kita memberikan input standar (STDIN - FD 0) ke program. Setelah menekan `[ENTER]`, teks tersebut dikembalikan ke terminal sebagai output standar (STDOUT - FD 1).

### 🇬🇧 English
When running `cat`, we provide standard input (STDIN - FD 0) to the program. Once we confirm with `[ENTER]`, the text is returned to the terminal as standard output (STDOUT - FD 1).

### 🇯🇵 日本語
`cat` を実行すると、プログラムに標準入力（STDIN - FD 0）を与えます。`[ENTER]` で確定すると、そのテキストは標準出力（STDOUT - FD 1）としてターミナルに返されます。

```bash
$ cat
SOME INPUT        # ← STDIN (FD 0) — what you type
SOME INPUT        # ← STDOUT (FD 1) — echoed back
```

---

## 3. ⚠️ STDOUT & STDERR

### 🇮🇩 Bahasa Indonesia
Perintah `find` menghasilkan dua jenis output sekaligus:
- **STDOUT (FD 1)** — hasil yang berhasil ditemukan (hijau)
- **STDERR (FD 2)** — pesan error "Permission denied" (merah)

Untuk menyembunyikan error, kita redirect STDERR ke `/dev/null` — perangkat "lubang hitam" yang membuang semua data yang dikirim ke sana.

### 🇬🇧 English
The `find` command produces two types of output simultaneously:
- **STDOUT (FD 1)** — successfully found results (green)
- **STDERR (FD 2)** — "Permission denied" error messages (red)

To hide errors, we redirect STDERR to `/dev/null` — a "black hole" device that discards all data sent to it.

### 🇯🇵 日本語
`find` コマンドは同時に2種類の出力を生成します：
- **STDOUT (FD 1)** — 正常に見つかった結果（緑）
- **STDERR (FD 2)** — "Permission denied" エラーメッセージ（赤）

エラーを非表示にするには、STDERRを `/dev/null` にリダイレクトします — すべてのデータを破棄する「ブラックホール」デバイスです。

```bash
# Show both STDOUT and STDERR
$ find /etc/ -name shadow
/etc/shadow
find: '/etc/ssl/private': Permission denied

# Redirect STDERR to /dev/null (suppress errors)
$ find /etc/ -name shadow 2>/dev/null
/etc/shadow
```

> 💡 `2>` means "redirect FD 2 (STDERR) to the specified destination"

---

## 4. 💾 Redirect STDOUT to a File

### 🇮🇩 Bahasa Indonesia
Kita bisa menyimpan STDOUT ke dalam file menggunakan tanda `>`. Jika file belum ada, akan **dibuat otomatis**. Jika sudah ada, file akan **ditimpa tanpa konfirmasi**.

### 🇬🇧 English
We can save STDOUT to a file using the `>` operator. If the file doesn't exist, it is **created automatically**. If it already exists, it is **overwritten without confirmation**.

### 🇯🇵 日本語
`>` 演算子を使ってSTDOUTをファイルに保存できます。ファイルが存在しない場合は**自動的に作成**されます。既に存在する場合は**確認なしで上書き**されます。

```bash
$ find /etc/ -name shadow 2>/dev/null > results.txt
$ cat results.txt
/etc/shadow
```

```
find command
    │
    ├──── STDERR (FD 2) ──► /dev/null  (discarded)
    │
    └──── STDOUT (FD 1) ──► results.txt  (saved)
```

---

## 5. 🗂️ Redirect STDOUT and STDERR to Separate Files

### 🇮🇩 Bahasa Indonesia
Kita bisa memisahkan STDOUT dan STDERR ke dua file berbeda secara bersamaan. Ini sangat berguna saat debugging — kita bisa menganalisis error secara terpisah dari output normal.

### 🇬🇧 English
We can redirect STDOUT and STDERR to two different files simultaneously. This is very useful during debugging — we can analyze errors separately from normal output.

### 🇯🇵 日本語
STDOUTとSTDERRを同時に別々のファイルにリダイレクトできます。デバッグ時に非常に便利で、通常の出力とエラーを分けて分析できます。

```bash
$ find /etc/ -name shadow 2> stderr.txt 1> stdout.txt

$ cat stdout.txt
/etc/shadow

$ cat stderr.txt
find: '/etc/ssl/private': Permission denied
find: '/etc/polkit-1/rules.d': Permission denied
```

```
find command
    │
    ├──── STDERR (FD 2) ──► stderr.txt
    │
    └──── STDOUT (FD 1) ──► stdout.txt
```

---

## 6. ⬅️ Redirect STDIN

### 🇮🇩 Bahasa Indonesia
Tanda `<` digunakan untuk **memberikan isi file sebagai STDIN** ke sebuah perintah. Arahnya berlawanan dengan `>` — data mengalir dari file ke program.

Bayangkan `>` dan `<` sebagai **panah arah** yang menunjukkan ke mana data mengalir.

### 🇬🇧 English
The `<` operator is used to **feed a file's contents as STDIN** to a command. The direction is opposite to `>` — data flows from the file into the program.

Think of `>` and `<` as **directional arrows** showing where data flows.

### 🇯🇵 日本語
`<` 演算子はファイルの内容をコマンドの**STDINとして渡す**ために使います。方向は `>` と逆で、データはファイルからプログラムへと流れます。

`>` と `<` はデータの流れる方向を示す**方向矢印**と考えてください。

```bash
$ cat < stdout.txt
/etc/shadow
```

```
stdout.txt ──► (FD 0 - STDIN) ──► cat ──► terminal output
```

---

## 7. ➕ Redirect STDOUT and Append to a File (`>>`)

### 🇮🇩 Bahasa Indonesia
Tanda `>>` (double greater-than) digunakan untuk **menambahkan output ke akhir file** yang sudah ada, tanpa menimpa isinya. Berbeda dengan `>` yang akan menghapus isi file lama.

| Operator | Aksi |
|----------|------|
| `>` | Timpa file (overwrite) |
| `>>` | Tambahkan ke akhir (append) |

### 🇬🇧 English
The `>>` (double greater-than) operator **appends output to the end of an existing file** without overwriting it. This is different from `>`, which erases the old file content.

| Operator | Action |
|----------|--------|
| `>` | Overwrite file |
| `>>` | Append to end of file |

### 🇯🇵 日本語
`>>`（二重大なり記号）は既存ファイルの末尾に**出力を追記**します。古い内容を消去する `>` とは異なります。

| 演算子 | 動作 |
|--------|------|
| `>` | ファイルを上書き |
| `>>` | ファイルの末尾に追記 |

```bash
$ find /etc/ -name passwd >> stdout.txt 2>/dev/null
$ cat stdout.txt
/etc/shadow          # ← existing content
/etc/pam.d/passwd    # ← appended
/etc/cron.daily/passwd
/etc/passwd
```

---

## 8. 📥 Redirect STDIN Stream to a File (`<<` / Here-Document)

### 🇮🇩 Bahasa Indonesia
`<<` (double lower-than) digunakan untuk **streaming input langsung dari terminal ke file**. Ini disebut **Here-Document**. Kita mendefinisikan penanda akhir input (biasanya `EOF` = End Of File). Semua teks yang diketik sebelum `EOF` akan dianggap sebagai input.

### 🇬🇧 English
`<<` (double lower-than) is used to **stream input directly from the terminal into a file**. This is called a **Here-Document**. We define an end marker (usually `EOF` = End Of File). All text typed before `EOF` is treated as input.

### 🇯🇵 日本語
`<<`（二重小なり記号）はターミナルから直接**ストリーム入力をファイルへ書き込む**ために使います。これを**ヒアドキュメント**と呼びます。終端マーカー（通常は `EOF` = End Of File）を定義し、`EOF` より前に入力されたすべてのテキストが入力として扱われます。

```bash
$ cat << EOF > stream.txt
> Hack The Box
> EOF

$ cat stream.txt
Hack The Box
```

> 💡 `EOF` is just a convention — you can use any word as the end marker (e.g., `END`, `STOP`, `DONE`).

---

## 9. 🔗 Pipes (`|`)

### 🇮🇩 Bahasa Indonesia
**Pipe (`|`)** digunakan untuk **menghubungkan output satu perintah sebagai input ke perintah berikutnya**. Ini memungkinkan kita membangun rantai perintah yang powerful tanpa perlu menyimpan data ke file sementara.

Pipe bisa dirantai berkali-kali — output dari perintah pertama menjadi input perintah kedua, lalu outputnya menjadi input perintah ketiga, dan seterusnya.

### 🇬🇧 English
**Pipes (`|`)** are used to **connect the output of one command as the input to the next command**. This allows building powerful command chains without saving data to temporary files.

Pipes can be chained multiple times — the output of the first command becomes the input of the second, whose output becomes the input of the third, and so on.

### 🇯🇵 日本語
**パイプ（`|`）** は**あるコマンドの出力を次のコマンドの入力として繋げる**ために使用します。一時ファイルを使わずに強力なコマンドチェーンを構築できます。

パイプは何度でも連結できます — 最初のコマンドの出力が2番目の入力になり、その出力が3番目の入力になります。

```bash
# Single pipe: find .conf files and filter for "systemd"
$ find /etc/ -name *.conf 2>/dev/null | grep systemd
/etc/systemd/system.conf
/etc/systemd/timesyncd.conf
/etc/systemd/journald.conf
/etc/systemd/user.conf
/etc/systemd/logind.conf
/etc/systemd/resolved.conf

# Chained pipes: add wc to count results
$ find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l
6
```

**Pipeline flow:**
```
[find /etc/ -name *.conf]
          │  STDOUT
          ▼
    [grep systemd]          ← filters only "systemd" lines
          │  STDOUT
          ▼
        [wc -l]             ← counts the remaining lines
          │
          ▼
          6
```

---

## 🔗 Redirection Operators — Quick Reference

| Operator | Name | Description |
|----------|------|-------------|
| `>` | Redirect STDOUT | Write output to file (overwrite) |
| `>>` | Append STDOUT | Append output to file |
| `<` | Redirect STDIN | Read input from file |
| `<<` | Here-Document | Stream multi-line input |
| `2>` | Redirect STDERR | Write errors to file |
| `2>/dev/null` | Suppress STDERR | Discard all error messages |
| `1>` | Explicit STDOUT | Write STDOUT to file (same as `>`) |
| `2>&1` | Merge STDERR→STDOUT | Combine error stream into output stream |
| `\|` | Pipe | Pass STDOUT to next command's STDIN |

---

## 🔀 Full Pipeline Example

```bash
# Find all .conf files, filter for "systemd", count results
$ find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l
6
```

```
find /etc/ -name *.conf
    │
    ├── STDERR ──► /dev/null      (errors suppressed)
    │
    └── STDOUT ──► grep systemd   (filter results)
                        │
                        └── STDOUT ──► wc -l   (count lines)
                                          │
                                          └──► 6
```

---

## 📊 File Descriptor Flow Summary

```
                  ┌──────────────────┐
  Keyboard ──────►│  FD 0 (STDIN)    │
                  │                  │
                  │     PROCESS      │
                  │                  │
  Terminal ◄──────│  FD 1 (STDOUT)   │
                  │                  │
  Terminal ◄──────│  FD 2 (STDERR)   │
                  └──────────────────┘

Redirection changes where these streams go:
  STDIN  (0) : keyboard → file (<) or here-doc (<<)
  STDOUT (1) : terminal → file (>) or append (>>)
  STDERR (2) : terminal → file (2>) or /dev/null (suppress)
```

---

## 🧠 Quick Reference Cheatsheet

```bash
# Suppress errors
command 2>/dev/null

# Save output to file (overwrite)
command > output.txt

# Save output to file (append)
command >> output.txt

# Save STDOUT and STDERR separately
command 1> stdout.txt 2> stderr.txt

# Read file as STDIN
command < input.txt

# Here-document (multi-line stdin)
command << EOF
line one
line two
EOF

# Pipe output to next command
command1 | command2 | command3

# Practical example
find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man bash` — section on Redirection
> - GNU Bash Manual: Redirections

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.