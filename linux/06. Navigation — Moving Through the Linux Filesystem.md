# 🧭 Navigation — Moving Through the Linux Filesystem

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Command | Bahasa Indonesia | English | 日本語 |
|---|---------|-----------------|---------|--------|
| 1 | `pwd` | Tampilkan direktori saat ini | Show current directory | 現在のディレクトリを表示 |
| 2 | `ls` | Daftar isi direktori | List directory contents | ディレクトリの内容を一覧表示 |
| 3 | `ls -l` | Detail isi direktori | Detailed directory listing | 詳細な一覧表示 |
| 4 | `ls -la` | Tampilkan file tersembunyi | Show hidden files | 隠しファイルを表示 |
| 5 | `cd` | Pindah direktori | Change directory | ディレクトリを移動 |
| 6 | `cd -` | Kembali ke direktori sebelumnya | Go back to previous directory | 直前のディレクトリに戻る |
| 7 | `cd ..` | Naik ke parent direktori | Go up to parent directory | 親ディレクトリへ移動 |
| 8 | `clear` | Bersihkan terminal | Clear terminal screen | ターミナルをクリア |
| 9 | Shortcuts | Pintasan keyboard shell | Shell keyboard shortcuts | シェルキーボードショートカット |

---

## 1. 📍 `pwd` — Print Working Directory

### 🇮🇩 Bahasa Indonesia
`pwd` (Print Working Directory) digunakan untuk **mengetahui posisi direktori kita saat ini** di dalam filesystem. Ini adalah perintah pertama yang harus dijalankan saat baru masuk ke sistem, agar kita tahu sedang berada di mana.

### 🇬🇧 English
`pwd` (Print Working Directory) is used to **find out our current position** in the filesystem. This is the first command to run when accessing a system, so we know exactly where we are.

### 🇯🇵 日本語
`pwd`（Print Working Directory）は、ファイルシステム内での**現在の位置を確認**するために使用します。システムにアクセスした際に最初に実行するコマンドで、自分がどこにいるかを正確に把握できます。

```bash
$ pwd
/home/cry0l1t3
```

---

## 2. 📋 `ls` — List Directory Contents

### 🇮🇩 Bahasa Indonesia
`ls` digunakan untuk **menampilkan daftar file dan direktori** di dalam suatu lokasi. Tanpa opsi tambahan, hanya nama file dan folder yang ditampilkan. Kita juga bisa menentukan path tertentu tanpa perlu berpindah ke sana terlebih dahulu.

### 🇬🇧 English
`ls` is used to **display a list of files and directories** at a location. Without extra options, only the names of files and folders are shown. We can also specify a path without needing to navigate there first.

### 🇯🇵 日本語
`ls` は指定した場所の**ファイルとディレクトリの一覧を表示**するために使います。オプションなしでは、ファイルとフォルダの名前のみが表示されます。先にそこに移動しなくても、特定のパスを指定できます。

```bash
# List current directory
$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

# List specific path without navigating there
$ ls /var/
backups  cache  crash  lib  local  log  lock  mail  opt  run  spool  tmp
```

---

## 3. 🔍 `ls -l` — Detailed Listing

### 🇮🇩 Bahasa Indonesia
Flag `-l` menampilkan **informasi lengkap** tentang setiap file dan direktori, termasuk permission, pemilik, ukuran, dan waktu modifikasi. Baris pertama `total 32` menunjukkan total blok disk yang digunakan (32 blok × 1024 byte = **32 KB**).

### 🇬🇧 English
The `-l` flag shows **detailed information** about each file and directory, including permissions, owner, size, and modification time. The first line `total 32` indicates total disk blocks used (32 blocks × 1024 bytes = **32 KB**).

### 🇯🇵 日本語
`-l` フラグはパーミッション、所有者、サイズ、更新日時など各ファイル・ディレクトリの**詳細情報を表示**します。最初の行 `total 32` は使用ディスクブロック数を示します（32ブロック × 1024バイト = **32 KB**）。

```bash
$ ls -l

total 32
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
drwxr-xr-x 3 cry0l1t3 htbacademy 4096 Nov 15 03:26 Downloads
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Music
```

### Output Column Breakdown

```
drwxr-xr-x   2   cry0l1t3   htbacademy   4096   Nov 13 17:37   Desktop
     │        │       │           │         │          │           │
     │        │       │           │         │          │           └─ Name
     │        │       │           │         │          └─ Date & Time
     │        │       │           │         └─ Size (bytes) / blocks
     │        │       │           └─ Group owner
     │        │       └─ Owner (user)
     │        └─ Number of hard links
     └─ Type + Permissions
```

| Column | 🇮🇩 Keterangan | 🇬🇧 Description | 🇯🇵 説明 |
|--------|---------------|----------------|---------|
| `drwxr-xr-x` | Tipe & permission file | File type & permissions | ファイルの種類とパーミッション |
| `2` | Jumlah hard link | Number of hard links | ハードリンク数 |
| `cry0l1t3` | Pemilik file | File owner (user) | ファイルの所有者 |
| `htbacademy` | Grup pemilik | Group owner | グループ所有者 |
| `4096` | Ukuran file (byte) | File size in bytes | ファイルサイズ（バイト） |
| `Nov 13 17:37` | Tanggal & waktu modifikasi | Last modification date & time | 最終更新日時 |
| `Desktop` | Nama file / direktori | File / directory name | ファイル・ディレクトリ名 |

### Understanding Permissions: `drwxr-xr-x`

```
d  rwx  r-x  r-x
│   │    │    │
│   │    │    └─ Others  : read + execute only
│   │    └─ Group    : read + execute only
│   └─ Owner    : read + write + execute
└─ Type: d=directory, -=file, l=symlink
```

| Symbol | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 |
|--------|---------|------------|---------|
| `d` | Direktori | Directory | ディレクトリ |
| `-` | File biasa | Regular file | 通常ファイル |
| `l` | Symbolic link | Symbolic link | シンボリックリンク |
| `r` | Read (baca) | Read permission | 読み取り権限 |
| `w` | Write (tulis) | Write permission | 書き込み権限 |
| `x` | Execute (eksekusi) | Execute permission | 実行権限 |
| `-` | Tidak ada permission | No permission | 権限なし |

---

## 4. 👁️ `ls -la` — Show Hidden Files

### 🇮🇩 Bahasa Indonesia
Flag `-a` menampilkan **semua file termasuk file tersembunyi**. Di Linux, file tersembunyi diawali dengan tanda titik (`.`), seperti `.bashrc` atau `.bash_history`. File-file ini biasanya berisi konfigurasi penting dan sering terlewat oleh `ls` biasa.

### 🇬🇧 English
The `-a` flag shows **all files including hidden ones**. In Linux, hidden files start with a dot (`.`), like `.bashrc` or `.bash_history`. These files usually contain important configurations and are often missed by plain `ls`.

### 🇯🇵 日本語
`-a` フラグは**隠しファイルを含むすべてのファイルを表示**します。Linuxでは、`.bashrc` や `.bash_history` のようにドット（`.`）で始まるファイルが隠しファイルです。これらは重要な設定ファイルであることが多く、通常の `ls` では見えません。

```bash
$ ls -la

total 403188
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bash_history
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bashrc
...
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
```

> 💡 **Pentesting note:** Hidden files like `.bash_history` can contain previously executed commands, credentials, or sensitive paths left behind by other users — always check with `ls -la` when enumerating a system.

### Common Hidden Files

| File | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `.bashrc` | Konfigurasi shell Bash | Bash shell configuration | Bash シェルの設定 |
| `.bash_history` | Riwayat perintah yang dijalankan | History of executed commands | 実行コマンドの履歴 |
| `.bash_profile` | Konfigurasi login shell | Login shell configuration | ログインシェルの設定 |
| `.ssh/` | Kunci & konfigurasi SSH | SSH keys & configuration | SSH キーと設定 |
| `.env` | Variabel environment | Environment variables | 環境変数 |

---

## 5. 📂 `cd` — Change Directory

### 🇮🇩 Bahasa Indonesia
`cd` (Change Directory) digunakan untuk **berpindah antar direktori**. Kita bisa menggunakan **absolute path** (dimulai dari `/`) atau **relative path** (relatif terhadap direktori saat ini). Tidak perlu berpindah bertahap — bisa langsung melompat ke path tujuan secara penuh.

### 🇬🇧 English
`cd` (Change Directory) is used to **navigate between directories**. We can use an **absolute path** (starting from `/`) or a **relative path** (relative to the current directory). No need to navigate step by step — we can jump directly to the full destination path.

### 🇯🇵 日本語
`cd`（Change Directory）は**ディレクトリ間を移動**するために使います。**絶対パス**（`/` から始まる）または**相対パス**（現在のディレクトリからの相対）が使えます。段階的に移動する必要はなく、目的地の完全パスに直接ジャンプできます。

```bash
# Navigate using absolute path (jump directly)
$ cd /dev/shm
cry0l1t3@htb[/dev/shm]$

# Navigate using relative path
$ cd Documents

# Jump to home directory
$ cd ~
$ cd          # also goes to home

# Navigate using dot notation
$ cd ./Storage/local/user
```

### Absolute vs Relative Path

```
Filesystem root: /
        │
        ├── home/
        │     └── cry0l1t3/        ← you are here (~)
        │           ├── Desktop/
        │           └── Documents/
        │
        └── dev/
              └── shm/             ← target

Absolute: cd /dev/shm              (always starts from /)
Relative: cd ../../dev/shm         (from current location)
```

---

## 6. ↩️ `cd -` — Return to Previous Directory

### 🇮🇩 Bahasa Indonesia
`cd -` adalah pintasan cepat untuk **kembali ke direktori yang sebelumnya dikunjungi**. Sangat berguna saat berpindah bolak-balik antara dua direktori yang berbeda.

### 🇬🇧 English
`cd -` is a quick shortcut to **return to the previously visited directory**. Very useful when switching back and forth between two different directories.

### 🇯🇵 日本語
`cd -` は**直前に訪れたディレクトリに戻る**クイックショートカットです。2つの異なるディレクトリを行き来するときに非常に便利です。

```bash
$ pwd
/home/cry0l1t3

$ cd /dev/shm
cry0l1t3@htb[/dev/shm]$

$ cd -
cry0l1t3@htb[~]$         # back to /home/cry0l1t3

$ cd -
cry0l1t3@htb[/dev/shm]$  # and back again
```

---

## 7. ⬆️ `cd ..` — Go Up to Parent Directory

### 🇮🇩 Bahasa Indonesia
`..` (dua titik) selalu merujuk ke **direktori parent** (satu level di atas direktori saat ini). Sedangkan `.` (satu titik) merujuk ke **direktori saat ini**. Kedua simbol ini selalu tampil dalam output `ls -la` sebagai dua entri pertama.

### 🇬🇧 English
`..` (two dots) always refers to the **parent directory** (one level above the current directory). While `.` (one dot) refers to the **current directory**. Both symbols always appear in `ls -la` output as the first two entries.

### 🇯🇵 日本語
`..`（二つのドット）は常に**親ディレクトリ**（現在のディレクトリの一つ上）を指します。一方 `.`（一つのドット）は**現在のディレクトリ**を指します。どちらも `ls -la` の出力で最初の2つのエントリとして常に表示されます。

```bash
$ pwd
/dev/shm

$ ls -la /dev/shm
total 0
drwxrwxrwt  2 root root   40 Mai 15 18:31 .    ← current dir (/dev/shm)
drwxr-xr-x 17 root root 4000 Mai 14 20:45 ..   ← parent dir (/dev)

# Go up one level
$ cd ..
cry0l1t3@htb[/dev]$

# Go up two levels at once
$ cd ../..

# Combine with path
$ cd ../../home/cry0l1t3
```

---

## 8. 🧹 `clear` — Clear the Terminal

### 🇮🇩 Bahasa Indonesia
`clear` digunakan untuk **membersihkan layar terminal** dari semua output sebelumnya. Bisa juga dikombinasikan dengan perintah lain menggunakan `&&`. Alternatif lebih cepat: gunakan shortcut keyboard `[CTRL + L]`.

### 🇬🇧 English
`clear` is used to **clean the terminal screen** from all previous output. It can also be combined with other commands using `&&`. A faster alternative: use the keyboard shortcut `[CTRL + L]`.

### 🇯🇵 日本語
`clear` はターミナル画面から以前のすべての出力を**クリア**するために使います。`&&` を使って他のコマンドと組み合わせることもできます。より速い代替手段：キーボードショートカット `[CTRL + L]` を使用します。

```bash
# Clear the terminal
$ clear

# Combine: navigate and clear in one line
$ cd /dev/shm && clear

# Keyboard shortcut alternative
[CTRL + L]
```

---

## 9. ⌨️ Shell Navigation Shortcuts

### 🇮🇩 Bahasa Indonesia
Shell menyediakan berbagai **pintasan keyboard** yang mempercepat navigasi dan penggunaan terminal secara signifikan.

### 🇬🇧 English
The shell provides various **keyboard shortcuts** that significantly speed up terminal navigation and usage.

### 🇯🇵 日本語
シェルはターミナルの操作をクイックに行うための様々な**キーボードショートカット**を提供します。

| Shortcut | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|----------|-----------|-------------|---------|
| `[TAB]` | Auto-complete nama file/path | Auto-complete file/path names | ファイル名・パスを自動補完 |
| `[TAB TAB]` | Tampilkan semua kemungkinan | Show all possible completions | すべての候補を表示 |
| `↑ / ↓` | Scroll riwayat perintah | Scroll through command history | コマンド履歴をスクロール |
| `[CTRL + R]` | Cari di riwayat perintah | Search command history | コマンド履歴を検索 |
| `[CTRL + L]` | Bersihkan terminal | Clear terminal | ターミナルをクリア |
| `[CTRL + C]` | Batalkan perintah yang berjalan | Cancel running command | 実行中のコマンドをキャンセル |
| `[CTRL + A]` | Pindah ke awal baris | Move to start of line | 行の先頭に移動 |
| `[CTRL + E]` | Pindah ke akhir baris | Move to end of line | 行の末尾に移動 |

### TAB Auto-complete Demo

```bash
# Type partial path and press TAB twice to see options
$ cd /dev/s[TAB TAB]
shm/  snd/

# Add "h" to narrow it down — shell completes automatically
$ cd /dev/sh[TAB]
$ cd /dev/shm/    ← completed!
```

---

## 🔗 `ls` Flags Quick Reference

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `ls` | Daftar nama saja | Names only | 名前のみ |
| `ls -l` | Detail (permission, size, date) | Detailed listing | 詳細表示 |
| `ls -a` | Tampilkan file tersembunyi | Show hidden files | 隠しファイルを表示 |
| `ls -la` | Detail + hidden files | Detailed + hidden | 詳細＋隠しファイル |
| `ls -lh` | Detail + ukuran human-readable | Detail + human-readable size | 人間が読みやすいサイズ |
| `ls -lt` | Sort berdasarkan waktu | Sort by time | 時間順にソート |
| `ls -lr` | Urutan terbalik | Reverse order | 逆順表示 |
| `ls /path` | Daftar path tertentu | List specific path | 特定パスを一覧表示 |

---

## 🧠 Quick Reference Cheatsheet

```bash
# ── WHERE AM I ──────────────────────────────────────
pwd                         # show current directory

# ── LIST CONTENTS ───────────────────────────────────
ls                          # basic list
ls -l                       # detailed list
ls -la                      # detailed + hidden files
ls -lh                      # human-readable sizes
ls /var/                    # list specific path

# ── NAVIGATE ────────────────────────────────────────
cd /dev/shm                 # absolute path
cd Documents                # relative path
cd ~                        # home directory
cd -                        # previous directory
cd ..                       # parent directory
cd ../..                    # two levels up

# ── CLEAN TERMINAL ──────────────────────────────────
clear                       # clear screen
cd /dev/shm && clear        # navigate + clear
[CTRL + L]                  # shortcut to clear

# ── SHORTCUTS ───────────────────────────────────────
[TAB]                       # auto-complete
[TAB TAB]                   # show all completions
[↑] / [↓]                  # command history
[CTRL + R]                  # search history
[CTRL + C]                  # cancel command
[CTRL + A]                  # beginning of line
[CTRL + E]                  # end of line
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man ls`, `man cd`, `man pwd`
> - GNU Coreutils Documentation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.