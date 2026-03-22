# ✏️ Editing Files — Nano & Vim

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2025 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | `nano` | Editor teks sederhana | Simple text editor | シンプルなテキストエディタ |
| 2 | Nano Shortcuts | Pintasan keyboard Nano | Nano keyboard shortcuts | Nano キーボードショートカット |
| 3 | `/etc/passwd` | File penting untuk pentester | Important file for pentesters | ペンテスター必見ファイル |
| 4 | `vim` | Editor teks powerful & modal | Powerful modal text editor | 強力なモーダルテキストエディタ |
| 5 | Vim Modes | 6 mode Vim | 6 Vim modes | Vim の6つのモード |
| 6 | `vimtutor` | Latihan Vim interaktif | Interactive Vim practice | インタラクティブ Vim 練習 |

---

## 1. 📝 `nano` — Simple Text Editor

### 🇮🇩 Bahasa Indonesia
`nano` adalah editor teks yang **mudah dipahami** dan cocok untuk pemula. Berbeda dengan Vim, Nano tidak memiliki mode — kamu langsung bisa mengetik setelah membuka file. Untuk membuat atau membuka file, cukup sertakan nama file sebagai argumen pertama.

### 🇬🇧 English
`nano` is a **beginner-friendly** text editor. Unlike Vim, Nano has no modes — you can start typing immediately after opening a file. To create or open a file, simply provide the filename as the first argument.

### 🇯🇵 日本語
`nano` は**初心者に優しい**テキストエディタです。Vim とは異なり、Nano にはモードがなく — ファイルを開いたらすぐに入力できます。ファイルを作成または開くには、最初の引数としてファイル名を指定します。

```bash
# Create and open a new file
$ nano notes.txt

# Open an existing file
$ nano /etc/hosts
```

**Nano Interface:**
```
  GNU nano 2.9.3                    notes.txt

Here we can type everything we want and make our notes.▓


^G Get Help    ^O Write Out   ^W Where Is    ^K Cut Text    ^J Justify
^X Exit        ^R Read File   ^\ Replace     ^U Uncut Text  ^T To Spell
```

> 💡 The caret `^` symbol represents the `[CTRL]` key. So `^X` means `[CTRL + X]`.

---

## 2. ⌨️ Nano Keyboard Shortcuts

### 🇮🇩 Bahasa Indonesia
Nano menampilkan shortcut yang tersedia di bagian bawah layar. Tanda `^` berarti tombol `[CTRL]`, sedangkan `M-` berarti tombol `[Alt]`.

### 🇬🇧 English
Nano displays available shortcuts at the bottom of the screen. The `^` symbol means `[CTRL]`, while `M-` means the `[Alt]` key.

### 🇯🇵 日本語
Nano は画面下部に使用可能なショートカットを表示します。`^` は `[CTRL]` キーを意味し、`M-` は `[Alt]` キーを意味します。

| Shortcut | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|----------|-----------|-------------|---------|
| `CTRL + O` | Simpan file | Save file | ファイルを保存 |
| `CTRL + X` | Keluar dari Nano | Exit Nano | Nano を終了 |
| `CTRL + W` | Cari kata / teks | Search for text | テキストを検索 |
| `CTRL + K` | Potong baris (cut) | Cut current line | 現在の行をカット |
| `CTRL + U` | Tempel (uncut/paste) | Paste cut text | カットしたテキストを貼り付け |
| `CTRL + G` | Tampilkan bantuan | Show help | ヘルプを表示 |
| `CTRL + C` | Tampilkan posisi kursor | Show cursor position | カーソル位置を表示 |
| `CTRL + \` | Ganti teks (replace) | Find and replace | テキストを置換 |
| `M-U` | Undo | Undo last action | 直前の操作を元に戻す |
| `M-E` | Redo | Redo last action | やり直し |

### Search in Nano

```
# Press CTRL+W to open search bar:

GNU nano 2.9.3                    notes.txt

Here ▓we can type everything we want and make our notes.

Search:  notes
^G Get Help   M-C Case Sens   M-B Backwards   ^C Cancel
```

```bash
# Workflow: edit → save → exit
1. nano notes.txt           # open/create file
2. Type your content        # write directly
3. CTRL + O  → ENTER        # save file
4. CTRL + X                 # exit editor
5. cat notes.txt            # verify content
```

---

## 3. 🔐 `/etc/passwd` — Important File for Pentesters

### 🇮🇩 Bahasa Indonesia
File `/etc/passwd` menyimpan **informasi penting tentang semua user** di sistem Linux, termasuk username, UID, GID, dan direktori home. Secara historis, file ini juga menyimpan hash password, namun sekarang hash tersebut dipindahkan ke `/etc/shadow` yang memiliki permission lebih ketat.

Bagi penetration tester, file ini penting karena:
- Misconfigured permissions bisa mengekspos informasi sensitif
- Bisa menjadi titik awal untuk **privilege escalation**
- Membantu mengidentifikasi user accounts yang lemah

### 🇬🇧 English
The `/etc/passwd` file stores **essential information about all users** on the Linux system, including usernames, UIDs, GIDs, and home directories. Historically, it also stored password hashes, but those are now moved to `/etc/shadow` which has stricter permissions.

For penetration testers, this file is important because:
- Misconfigured permissions can expose sensitive information
- It can be a starting point for **privilege escalation**
- Helps identify weak user accounts

### 🇯🇵 日本語
`/etc/passwd` ファイルはLinuxシステムの**全ユーザーに関する重要な情報**（ユーザー名、UID、GID、ホームディレクトリなど）を保存しています。歴史的にはパスワードハッシュも保存されていましたが、現在はより厳格なパーミッションを持つ `/etc/shadow` に移動されています。

ペネトレーションテスターにとってこのファイルが重要な理由：
- 誤ったパーミッション設定により機密情報が露出する可能性がある
- **権限昇格（Privilege Escalation）**の起点になり得る
- 脆弱なユーザーアカウントの特定に役立つ

```bash
# View the passwd file
$ cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
htb-student:x:1001:1001::/home/htb-student:/bin/bash
```

```
username : password : UID : GID : comment : home_dir : shell
   root  :    x    :  0  :  0  :  root   :  /root   : /bin/bash
```

| Field | Description |
|-------|-------------|
| `root` | Username |
| `x` | Password placeholder (hash in `/etc/shadow`) |
| `0` | User ID (UID) — 0 = root |
| `0` | Group ID (GID) |
| `root` | Comment / GECOS field |
| `/root` | Home directory |
| `/bin/bash` | Default shell |

> ⚠️ **Pentesting note:** If `/etc/passwd` is world-writable, an attacker can add a new root user directly. Always check: `ls -la /etc/passwd`

---

## 4. ⚡ `vim` — Powerful Modal Editor

### 🇮🇩 Bahasa Indonesia
`vim` (Vi IMproved) adalah editor teks open-source yang sangat powerful. Berbeda dengan Nano, Vim adalah **modal editor** — artinya Vim memiliki beberapa mode berbeda untuk mengetik teks dan menjalankan perintah. Vim mengikuti prinsip Unix: kecil, cepat, dan bisa diintegrasikan dengan tools lain seperti `grep`, `awk`, `sed`.

Vim memang memiliki kurva belajar yang lebih curam dibanding Nano, namun **efisiensinya luar biasa** setelah terbiasa.

### 🇬🇧 English
`vim` (Vi IMproved) is an extremely powerful open-source text editor. Unlike Nano, Vim is a **modal editor** — meaning it has different modes for typing text and executing commands. Vim follows the Unix principle: small, fast, and integrable with other tools like `grep`, `awk`, `sed`.

Vim has a steeper learning curve than Nano, but its **efficiency is extraordinary** once mastered.

### 🇯🇵 日本語
`vim`（Vi IMproved）は非常に強力なオープンソーステキストエディタです。Nano とは異なり、Vim は**モーダルエディタ** — テキスト入力とコマンド実行に異なるモードを持ちます。Vim は Unix の原則（小さく、速く、`grep`・`awk`・`sed` などの他ツールと統合可能）に従っています。

Nano よりも学習曲線は急ですが、慣れると**驚異的な効率性**を発揮します。

```bash
# Open Vim
$ vim

# Open or create a file
$ vim notes.txt

# Exit Vim (from Normal mode)
:q          # quit (if no changes)
:q!         # force quit (discard changes)
:wq         # save and quit
:x          # save and quit (shorthand)
```

---

## 5. 🎭 Vim Modes

### 🇮🇩 Bahasa Indonesia
Vim memiliki **6 mode fundamental** yang membuatnya berbeda dari editor biasa. Memahami mode-mode ini adalah kunci untuk menguasai Vim.

### 🇬🇧 English
Vim has **6 fundamental modes** that make it different from ordinary editors. Understanding these modes is the key to mastering Vim.

### 🇯🇵 日本語
Vim には**6つの基本モード**があり、これが通常のエディタとの違いです。これらのモードを理解することが Vim 習得の鍵です。

---

| Mode | Enter With | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|------|-----------|--------------|----------------|---------|
| **Normal** | `ESC` | Mode default saat membuka Vim. Semua input dianggap perintah editor, bukan teks. | Default mode when opening Vim. All inputs are treated as editor commands, not text. | Vim 起動時のデフォルトモード。すべての入力がエディタコマンドとして扱われる。 |
| **Insert** | `i`, `a`, `o` | Mode untuk mengetik dan memasukkan teks ke dalam buffer. | Mode for typing and inserting text into the buffer. | テキストをバッファに入力・挿入するモード。 |
| **Visual** | `v`, `V`, `CTRL+V` | Mode untuk **menandai (select) teks** secara visual. Teks yang dipilih bisa dihapus, disalin, atau diganti. | Mode for **visually selecting text**. Selected text can be deleted, copied, or replaced. | テキストを**視覚的に選択**するモード。選択したテキストを削除・コピー・置換できる。 |
| **Command** | `:` | Mode untuk memasukkan **perintah satu baris** di bagian bawah editor (misalnya sort, replace, delete). | Mode for entering **single-line commands** at the bottom of the editor (e.g. sort, replace, delete). | エディタ下部で**一行コマンドを入力**するモード（ソート、置換、削除など）。 |
| **Replace** | `R` | Teks yang diketik akan **menimpa karakter yang ada**. Jika sudah habis, teks baru ditambahkan. | Newly typed text **overwrites existing characters**. If no more old characters, new text is appended. | 入力したテキストが**既存の文字を上書き**。古い文字がなくなると追加される。 |
| **Ex** | `Q` | Mengemulasi perilaku editor teks **Ex** (pendahulu Vim). Memungkinkan beberapa perintah dieksekusi berurutan tanpa kembali ke Normal mode. | Emulates the behavior of the **Ex** text editor (Vim's predecessor). Allows executing multiple commands sequentially without returning to Normal mode. | **Ex** テキストエディタ（Vim の前身）の動作をエミュレート。Normal モードに戻らず複数コマンドを順次実行できる。 |

---

### Mode Flow Diagram

```
               ┌─────────────────────┐
               │    NORMAL MODE      │  ← default on start / press ESC
               └──────────┬──────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
   ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
   │ INSERT MODE │ │ VISUAL MODE │ │ COMMAND MODE │
   │  (i, a, o) │ │  (v, V)     │ │     (:)      │
   └─────────────┘ └─────────────┘ └──────────────┘
   Type text here   Select text     :w  :q  :wq
   Press ESC        Press ESC       :s/old/new/g
   to go back       to go back
```

---

### Essential Vim Commands

```bash
# --- Mode switching ---
i           # Enter Insert mode (before cursor)
a           # Enter Insert mode (after cursor)
o           # New line below + Insert mode
ESC         # Return to Normal mode

# --- Navigation (Normal mode) ---
h j k l     # Move left / down / up / right
gg          # Go to first line
G           # Go to last line
:20         # Go to line 20

# --- Editing (Normal mode) ---
dd          # Delete (cut) current line
yy          # Yank (copy) current line
p           # Paste below
u           # Undo
CTRL + r    # Redo
x           # Delete character under cursor

# --- Search (Normal mode) ---
/pattern    # Search forward
n           # Next match
N           # Previous match

# --- Command mode ---
:w          # Save (write)
:q          # Quit
:wq         # Save and quit
:q!         # Force quit (no save)
:s/old/new/g        # Replace on current line
:%s/old/new/g       # Replace in entire file
:set number         # Show line numbers
```

---

## 6. 🎓 `vimtutor` — Learn Vim Interactively

### 🇮🇩 Bahasa Indonesia
`vimtutor` adalah **tutorial interaktif bawaan Vim** yang dirancang untuk membantu pemula menguasai editor ini. Waktu yang dibutuhkan sekitar 25–30 menit. Sangat direkomendasikan untuk memulai sebelum menggunakan Vim secara aktif.

Bisa diakses dengan dua cara:
1. Ketik `vimtutor` di terminal (membuka copy file latihan)
2. Dari dalam Vim: masuk ke Command mode lalu ketik `:Tutor`

### 🇬🇧 English
`vimtutor` is Vim's **built-in interactive tutorial** designed to help beginners master the editor. It takes approximately 25–30 minutes to complete. Highly recommended before using Vim actively.

It can be accessed in two ways:
1. Type `vimtutor` in the terminal (opens a practice copy)
2. From inside Vim: enter Command mode and type `:Tutor`

### 🇯🇵 日本語
`vimtutor` はVim に組み込まれた**インタラクティブチュートリアル**で、初心者がエディタを習得するために設計されています。完了に約25〜30分かかります。Vim を積極的に使う前に強く推奨します。

2つのアクセス方法：
1. ターミナルで `vimtutor` と入力（練習用コピーが開く）
2. Vim 内から：Command モードで `:Tutor` と入力

```bash
# Start the interactive tutorial
$ vimtutor
```

```
===============================================================================
=    W e l c o m e   t o   t h e   V I M   T u t o r    -    Version 1.7      =
===============================================================================

     Vim is a very powerful editor that has many commands, too many to
     explain in a tutor such as this.  This tutor is designed to describe
     enough of the commands that you will be able to easily use Vim as
     an all-purpose editor.

     The approximate time required to complete the tutor is 25-30 minutes...
```

> 💡 `vimtutor` opens a **copy** of the practice file — feel free to experiment without fear of breaking anything. All commands in the lessons must be executed to properly learn them!

---

## 📊 Nano vs Vim — Comparison

| Feature | `nano` | `vim` |
|---------|--------|-------|
| **Learning curve** | 🟢 Easy | 🔴 Steep |
| **Modal editing** | ❌ No | ✅ Yes (6 modes) |
| **Shortcuts shown** | ✅ Bottom bar | ❌ Must memorize |
| **Speed (when mastered)** | 🟡 Medium | 🟢 Very fast |
| **Scripting / macros** | ❌ No | ✅ Yes |
| **Plugin support** | ❌ No | ✅ Extensive |
| **Best for** | Quick edits, beginners | Power users, developers |
| **Exit command** | `CTRL + X` | `:q!` or `:wq` |

---

## 🧠 Quick Reference Cheatsheet

```bash
# ── NANO ──────────────────────────────────────────
nano filename.txt       # open / create file
CTRL + O  → ENTER       # save file
CTRL + X                # exit
CTRL + W                # search
CTRL + K                # cut line
CTRL + U                # paste
M-U                     # undo

# ── VIM ───────────────────────────────────────────
vim filename.txt        # open / create file

# Mode switching
i                       # insert mode
ESC                     # back to normal mode
v                       # visual mode
:                       # command mode

# Save / Exit
:w                      # save
:q                      # quit
:wq                     # save and quit
:q!                     # force quit

# Essential commands (Normal mode)
dd                      # delete line
yy                      # copy line
p                       # paste
u                       # undo
/pattern                # search

# Start interactive tutorial
vimtutor
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man nano`, `man vim`
> - [Vim official documentation](https://www.vim.org/docs.php)
> - `vimtutor` — built-in interactive tutorial

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.