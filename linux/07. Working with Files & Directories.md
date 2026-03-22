# 📁 Working with Files and Directories

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Command | Bahasa Indonesia | English | 日本語 |
|---|---------|-----------------|---------|--------|
| 1 | `touch` | Buat file kosong | Create empty file | 空ファイルを作成 |
| 2 | `mkdir` | Buat direktori | Create directory | ディレクトリを作成 |
| 3 | `mkdir -p` | Buat nested direktori | Create nested directories | ネストされたディレクトリを作成 |
| 4 | `tree` | Lihat struktur direktori | View directory structure | ディレクトリ構造を表示 |
| 5 | `mv` | Pindah / rename file | Move / rename file | ファイルの移動・名前変更 |
| 6 | `cp` | Salin file | Copy file | ファイルをコピー |
| 7 | `rm` | Hapus file / direktori | Delete file / directory | ファイル・ディレクトリを削除 |

---

## 🐧 Linux vs Windows: File Management

### 🇮🇩 Bahasa Indonesia
Perbedaan utama pengelolaan file di Linux vs Windows terletak pada **cara aksesnya**. Di Windows, kita biasanya menggunakan tools grafis seperti Explorer. Di Linux, terminal menawarkan alternatif yang lebih powerful karena:
- Lebih cepat dengan hanya beberapa perintah
- Bisa memodifikasi file secara selektif menggunakan **regex**
- Bisa menjalankan banyak perintah sekaligus
- Bisa mengotomasi tugas batch editing pada banyak file secara bersamaan

### 🇬🇧 English
The main difference between file management in Linux vs Windows lies in **how files are accessed**. In Windows, we typically use graphical tools like Explorer. In Linux, the terminal offers a more powerful alternative because:
- Faster with just a few commands
- Can modify files selectively using **regex**
- Can run multiple commands simultaneously
- Can automate batch editing tasks on many files at once

### 🇯🇵 日本語
Linux と Windows のファイル管理の主な違いは**アクセス方法**にあります。Windows では通常 Explorer のようなグラフィカルツールを使いますが、Linux ではターミナルがより強力な代替手段を提供します：
- わずかなコマンドで高速処理
- **正規表現（regex）**を使って選択的にファイルを編集できる
- 複数のコマンドを同時に実行できる
- 多くのファイルのバッチ編集タスクを自動化できる

---

## 1. 📄 `touch` — Create an Empty File

### 🇮🇩 Bahasa Indonesia
`touch` digunakan untuk **membuat file kosong baru**. Jika file sudah ada, perintah ini akan memperbarui timestamp-nya tanpa mengubah isinya.

### 🇬🇧 English
`touch` is used to **create a new empty file**. If the file already exists, this command updates its timestamp without changing its contents.

### 🇯🇵 日本語
`touch` は**新しい空のファイルを作成**するために使います。ファイルが既に存在する場合は、内容を変えずにタイムスタンプを更新します。

```bash
# Syntax
touch <filename>

# Create a single file
$ touch info.txt

# Create multiple files at once
$ touch file1.txt file2.txt file3.txt

# Create a file inside a specific directory
$ touch ./Storage/local/user/userinfo.txt
```

> 💡 The `.` (single dot) refers to the **current directory**. Using `./path/file` is a convenient way to work relative to your current location without typing the full absolute path.

---

## 2. 📂 `mkdir` — Create a Directory

### 🇮🇩 Bahasa Indonesia
`mkdir` (make directory) digunakan untuk **membuat direktori baru**. Gunakan flag `-p` untuk membuat direktori bertingkat (nested) secara sekaligus — tanpa `-p`, perintah akan gagal jika direktori parent belum ada.

### 🇬🇧 English
`mkdir` (make directory) is used to **create a new directory**. Use the `-p` flag to create nested directories all at once — without `-p`, the command will fail if the parent directory doesn't yet exist.

### 🇯🇵 日本語
`mkdir`（make directory）は**新しいディレクトリを作成**するために使います。`-p` フラグを使うとネストされたディレクトリを一度に作成できます — `-p` がないと、親ディレクトリが存在しない場合にコマンドが失敗します。

```bash
# Syntax
mkdir <directory_name>

# Create a single directory
$ mkdir Storage

# Create nested directories in one command (-p = parents)
$ mkdir -p Storage/local/user/documents
```

| Flag | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `-p` | Buat direktori parent secara otomatis | Create parent directories automatically | 親ディレクトリを自動作成 |
| `-v` | Tampilkan detail setiap direktori yang dibuat | Show details of each created directory | 作成した各ディレクトリの詳細を表示 |
| `-m` | Set permission saat membuat | Set permissions on creation | 作成時にパーミッションを設定 |

---

## 3. 🌳 `tree` — Visualize Directory Structure

### 🇮🇩 Bahasa Indonesia
`tree` menampilkan **struktur direktori secara visual** dalam bentuk pohon (tree). Sangat berguna untuk memverifikasi hasil pembuatan direktori bertingkat.

### 🇬🇧 English
`tree` displays the **directory structure visually** in a tree format. Very useful for verifying the result of nested directory creation.

### 🇯🇵 日本語
`tree` はディレクトリ構造をツリー形式で**視覚的に表示**します。ネストされたディレクトリ作成の結果を確認するのに非常に便利です。

```bash
# View current directory structure
$ tree .

.
├── info.txt
└── Storage
    └── local
        └── user
            └── documents

4 directories, 1 file

# After creating more files
$ touch ./Storage/local/user/userinfo.txt
$ tree .

.
├── info.txt
└── Storage
    └── local
        └── user
            ├── documents
            └── userinfo.txt

4 directories, 2 files
```

---

## 4. 🚚 `mv` — Move and Rename Files

### 🇮🇩 Bahasa Indonesia
`mv` (move) memiliki **dua fungsi sekaligus**: memindahkan file/direktori ke lokasi lain, dan mengganti nama (rename) file/direktori. Perintah yang sama digunakan untuk keduanya — bedanya hanya pada argumen yang diberikan.

### 🇬🇧 English
`mv` (move) serves **two purposes at once**: moving a file/directory to another location, and renaming a file/directory. The same command is used for both — the difference is only in the arguments provided.

### 🇯🇵 日本語
`mv`（move）は**2つの目的を同時に持ちます**：ファイル・ディレクトリを別の場所に移動することと、名前を変更することです。どちらも同じコマンドを使います — 違いは指定する引数だけです。

```bash
# Syntax
mv <source> <destination>

# ── RENAME a file ──────────────────────────────────
$ mv info.txt information.txt

# ── MOVE a single file to a directory ──────────────
$ mv information.txt Storage/

# ── MOVE multiple files to a directory ─────────────
$ mv information.txt readme.txt Storage/

$ tree .
.
└── Storage
    ├── information.txt
    ├── local
    │   └── user
    │       ├── documents
    │       └── userinfo.txt
    └── readme.txt

4 directories, 3 files

# ── MOVE and RENAME at the same time ───────────────
$ mv Storage/readme.txt Storage/local/READ_ME.txt
```

> ⚠️ **Warning:** `mv` will **overwrite** the destination file without warning if a file with the same name already exists. Use `mv -i` (interactive) to get a confirmation prompt before overwriting.

```bash
# Safe move with confirmation
$ mv -i info.txt Storage/
mv: overwrite 'Storage/info.txt'? y
```

---

## 5. 📋 `cp` — Copy Files and Directories

### 🇮🇩 Bahasa Indonesia
`cp` (copy) digunakan untuk **menyalin file atau direktori** ke lokasi baru. File asli tetap ada di lokasi semula. Untuk menyalin direktori beserta seluruh isinya, gunakan flag `-r` (recursive).

### 🇬🇧 English
`cp` (copy) is used to **copy files or directories** to a new location. The original file remains in its original location. To copy a directory along with all its contents, use the `-r` (recursive) flag.

### 🇯🇵 日本語
`cp`（copy）はファイルやディレクトリを新しい場所に**コピー**するために使います。元のファイルは元の場所に残ります。ディレクトリとその内容をすべてコピーするには `-r`（recursive）フラグを使います。

```bash
# Syntax
cp <source> <destination>

# Copy a file to another directory
$ cp Storage/readme.txt Storage/local/

$ tree .
.
└── Storage
    ├── information.txt
    ├── local
    │   ├── readme.txt           ← copied here
    │   └── user
    │       ├── documents
    │       └── userinfo.txt
    └── readme.txt               ← original still here

4 directories, 4 files

# Copy entire directory (recursive)
$ cp -r Storage/ Storage_backup/

# Copy and preserve permissions/timestamps
$ cp -rp Storage/ Storage_backup/
```

| Flag | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `-r` | Salin direktori secara rekursif | Copy directory recursively | ディレクトリを再帰的にコピー |
| `-p` | Pertahankan permission & timestamp | Preserve permissions & timestamps | パーミッションとタイムスタンプを保持 |
| `-i` | Konfirmasi sebelum menimpa | Confirm before overwriting | 上書き前に確認 |
| `-v` | Tampilkan file yang disalin | Show files being copied | コピーされるファイルを表示 |

---

## 6. 🗑️ `rm` — Delete Files and Directories

### 🇮🇩 Bahasa Indonesia
`rm` (remove) digunakan untuk **menghapus file atau direktori**. Hati-hati: di Linux tidak ada **Recycle Bin** — file yang dihapus dengan `rm` **tidak bisa dikembalikan** secara normal. Selalu gunakan dengan hati-hati, terutama dengan flag `-rf`.

### 🇬🇧 English
`rm` (remove) is used to **delete files or directories**. Be careful: in Linux there is no **Recycle Bin** — files deleted with `rm` **cannot be recovered** normally. Always use with caution, especially with the `-rf` flag.

### 🇯🇵 日本語
`rm`（remove）はファイルやディレクトリを**削除**するために使います。注意：Linuxには**ゴミ箱がない** — `rm` で削除されたファイルは通常**復元できません**。特に `-rf` フラグを使う際は十分注意してください。

```bash
# Delete a single file
$ rm info.txt

# Delete with confirmation prompt (-i = interactive)
$ rm -i info.txt
rm: remove regular file 'info.txt'? y

# Delete an empty directory
$ rmdir Storage/local/user/documents

# Delete a directory and ALL its contents (DANGEROUS!)
$ rm -r Storage/

# Force delete without any prompts (USE WITH EXTREME CAUTION)
$ rm -rf Storage/
```

| Flag | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `-r` | Hapus direktori secara rekursif | Delete directory recursively | ディレクトリを再帰的に削除 |
| `-f` | Paksa hapus tanpa konfirmasi | Force delete without prompt | 確認なしで強制削除 |
| `-i` | Konfirmasi sebelum hapus | Confirm before each deletion | 削除前に確認 |
| `-v` | Tampilkan file yang dihapus | Show files being deleted | 削除されるファイルを表示 |

> 🔴 **DANGER:** `rm -rf /` or `rm -rf /*` will delete **everything on the system**. Never run these commands — they are irreversible and will destroy the entire filesystem.

---

## 🔗 Full Workflow Example

```bash
# 1. Create directory structure
$ mkdir -p Storage/local/user/documents

# 2. Create files
$ touch info.txt
$ touch ./Storage/local/user/userinfo.txt

# 3. Verify structure
$ tree .
.
├── info.txt
└── Storage
    └── local
        └── user
            ├── documents
            └── userinfo.txt

# 4. Rename a file
$ mv info.txt information.txt

# 5. Move files into Storage
$ touch readme.txt
$ mv information.txt readme.txt Storage/

# 6. Copy readme.txt to local/
$ cp Storage/readme.txt Storage/local/

# 7. Verify final structure
$ tree .
.
└── Storage
    ├── information.txt
    ├── local
    │   ├── readme.txt
    │   └── user
    │       ├── documents
    │       └── userinfo.txt
    └── readme.txt

# 8. Clean up: delete the entire Storage directory
$ rm -r Storage/
```

---

## 📊 Command Summary Table

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Example |
|---------|-----------|-------------|---------|---------|
| `touch` | Buat file kosong | Create empty file | 空ファイル作成 | `touch file.txt` |
| `mkdir` | Buat direktori | Create directory | ディレクトリ作成 | `mkdir Storage` |
| `mkdir -p` | Buat nested direktori | Create nested dirs | ネスト作成 | `mkdir -p a/b/c` |
| `tree` | Tampilkan struktur | Show structure | 構造を表示 | `tree .` |
| `mv` | Pindah / rename | Move / rename | 移動・名前変更 | `mv a.txt b.txt` |
| `cp` | Salin file | Copy file | コピー | `cp a.txt dir/` |
| `cp -r` | Salin direktori | Copy directory | ディレクトリコピー | `cp -r dir1/ dir2/` |
| `rm` | Hapus file | Delete file | ファイル削除 | `rm file.txt` |
| `rm -r` | Hapus direktori | Delete directory | ディレクトリ削除 | `rm -r Storage/` |
| `rmdir` | Hapus dir kosong | Remove empty dir | 空ディレクトリ削除 | `rmdir emptydir/` |

---

## 🧠 Quick Reference Cheatsheet

```bash
# Create
touch filename.txt                    # empty file
mkdir dirname                         # directory
mkdir -p parent/child/grandchild      # nested directories
touch ./parent/child/file.txt         # file in specific path

# View structure
tree .                                # current directory tree
tree /path/to/dir                     # specific directory tree

# Move / Rename
mv old.txt new.txt                    # rename
mv file.txt dir/                      # move to directory
mv file1 file2 dir/                   # move multiple files
mv -i file.txt dir/                   # safe move (confirm overwrite)

# Copy
cp file.txt dir/                      # copy file to directory
cp -r dir1/ dir2/                     # copy entire directory
cp -rp dir1/ dir2/                    # copy + preserve permissions

# Delete
rm file.txt                           # delete file
rm -i file.txt                        # delete with confirmation
rm -r dirname/                        # delete directory
rmdir emptydir/                       # delete empty directory only
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man touch`, `man mkdir`, `man mv`, `man cp`, `man rm`, `man tree`
> - GNU Coreutils Documentation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.