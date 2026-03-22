# 🔐 Permission Management

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Permission Basics | Dasar permission | Permission basics | パーミッションの基礎 |
| 2 | Permission Types | Tipe permission (r, w, x) | Permission types | パーミッションの種類 |
| 3 | Reading Permissions | Membaca output `ls -l` | Reading `ls -l` output | `ls -l` の読み方 |
| 4 | `chmod` | Ubah permission | Change permissions | パーミッションを変更 |
| 5 | Octal Notation | Notasi oktal | Octal notation | 8進数表記 |
| 6 | `chown` | Ubah pemilik file | Change file owner | ファイル所有者を変更 |
| 7 | SUID & SGID | Hak akses khusus | Special access bits | 特殊アクセスビット |
| 8 | Sticky Bit | Bit sticky | Sticky bit | スティッキービット |

---

## 1. 🗝️ Permission Basics

### 🇮🇩 Bahasa Indonesia
Permission di Linux seperti **kunci yang mengontrol akses** ke file dan direktori. Setiap file dan direktori memiliki:
- Seorang **owner** (pemilik/user)
- Sebuah **group** (grup yang terkait)
- Permission yang didefinisikan untuk **owner, group, dan others (orang lain)**

Ketika kamu membuat file baru, file tersebut otomatis menjadi milikmu dan diasosiasikan dengan grupmu.

Untuk **masuk ke dalam direktori**, user membutuhkan **execute permission** pada direktori tersebut — seperti kunci untuk membuka pintu sebelum masuk ke dalam ruangan. Tanpa execute permission, meskipun isi direktori terlihat, user tidak bisa masuk dan akan mendapat error `Permission Denied`.

### 🇬🇧 English
Permissions in Linux act like **keys that control access** to files and directories. Every file and directory has:
- An **owner** (a user)
- A **group** (associated group)
- Permissions defined for **owner, group, and others**

When you create a new file, it automatically belongs to you and is associated with your group.

To **enter a directory**, a user needs **execute permission** on that directory — like a key to unlock a door before stepping inside. Without execute permission, even if directory contents are visible, the user cannot enter and will get a `Permission Denied` error.

### 🇯🇵 日本語
Linux のパーミッションはファイルやディレクトリへのアクセスを制御する**鍵のような存在**です。すべてのファイルとディレクトリには：
- **所有者**（owner/ユーザー）
- **グループ**（関連するグループ）
- **owner、group、others（その他）** に対して定義されたパーミッション

新しいファイルを作成すると、そのファイルは自動的にあなたのものになり、あなたのグループに関連付けられます。

**ディレクトリに入る**には、そのディレクトリに対する **execute パーミッション**が必要です — 部屋に入る前にドアを開ける鍵のようなものです。execute パーミッションなしでは、ディレクトリの内容が見えても中に入れず `Permission Denied` エラーになります。

```bash
# Without execute permission on a directory
$ ls -l
drw-rw-r-- 3 cry0l1t3 cry0l1t3 4096 Jan 12 12:30 scripts

$ ls -al mydirectory/
ls: cannot access 'mydirectory/script.sh': Permission denied
ls: cannot access 'mydirectory/..': Permission denied
ls: cannot access 'mydirectory/.': Permission denied
total 0
d????????? ? ? ? ? ? .
d????????? ? ? ? ? ? ..
-????????? ? ? ? ? ? script.sh
d????????? ? ? ? ? ? subdirectory
```

> ⚠️ Execute permission on a **directory** only allows traversal — it does NOT allow executing files inside. To execute files, you need execute permission on the **file itself**.

---

## 2. 📋 Permission Types

### 🇮🇩 Bahasa Indonesia
Ada **tiga tipe permission** yang bisa diberikan ke file atau direktori, dan ketiganya berlaku berbeda tergantung apakah diterapkan pada file atau direktori.

### 🇬🇧 English
There are **three types of permissions** that can be assigned to files or directories, and they behave differently depending on whether applied to a file or directory.

### 🇯🇵 日本語
ファイルまたはディレクトリに割り当てられる**3種類のパーミッション**があり、ファイルかディレクトリかによって動作が異なります。

---

| Permission | Symbol | On File | On Directory |
|------------|--------|---------|--------------|
| **Read** | `r` | 🇮🇩 Baca isi file / 🇬🇧 Read file contents / 🇯🇵 ファイルを読む | 🇮🇩 Lihat daftar isi direktori / 🇬🇧 List directory contents / 🇯🇵 ディレクトリの内容を一覧 |
| **Write** | `w` | 🇮🇩 Ubah / tulis ke file / 🇬🇧 Modify / write to file / 🇯🇵 ファイルを変更・書き込む | 🇮🇩 Buat, hapus, rename file di dalamnya / 🇬🇧 Create, delete, rename files inside / 🇯🇵 内部のファイルを作成・削除・名前変更 |
| **Execute** | `x` | 🇮🇩 Jalankan file sebagai program / 🇬🇧 Run file as a program / 🇯🇵 ファイルをプログラムとして実行 | 🇮🇩 Masuk / traversal direktori / 🇬🇧 Enter / traverse directory / 🇯🇵 ディレクトリに入る・移動する |

---

## 3. 👁️ Reading `ls -l` Output

### 🇮🇩 Bahasa Indonesia
Output dari `ls -l` menampilkan permission dalam format terstruktur. Memahami setiap kolom sangat penting untuk menganalisis keamanan sistem.

### 🇬🇧 English
The `ls -l` output displays permissions in a structured format. Understanding each column is essential for analyzing system security.

### 🇯🇵 日本語
`ls -l` の出力はパーミッションを構造化された形式で表示します。各列を理解することはシステムセキュリティの分析に不可欠です。

```bash
$ ls -l /etc/passwd
- rwx rw- r--   1 root root 1641 May 4 23:42 /etc/passwd
```

### Permission String Anatomy

```
- rwx rw- r--   1  root  root  1641  May 4 23:42  /etc/passwd
│  │   │   │    │   │     │      │       │              │
│  │   │   │    │   │     │      │       │              └─ Filename
│  │   │   │    │   │     │      │       └─ Date & Time
│  │   │   │    │   │     │      └─ File Size (bytes)
│  │   │   │    │   │     └─ Group owner
│  │   │   │    │   └─ User owner
│  │   │   │    └─ Number of hard links
│  │   │   └─ Others permissions  → r-- (read only)
│  │   └─ Group permissions       → rw- (read + write)
│  └─ Owner permissions           → rwx (read + write + execute)
└─ File type: - = file, d = directory, l = symlink
```

### Permission Groups

```
  - │ rwx │ rw- │ r--
  │    │      │     │
  │    │      │     └── Others  (everyone else)
  │    │      └──────── Group   (group members)
  │    └─────────────── Owner   (file owner/user)
  └──────────────────── File type
```

### File Type Characters

| Symbol | 🇮🇩 Tipe | 🇬🇧 Type | 🇯🇵 タイプ |
|--------|---------|---------|----------|
| `-` | File biasa | Regular file | 通常ファイル |
| `d` | Direktori | Directory | ディレクトリ |
| `l` | Symbolic link | Symbolic link | シンボリックリンク |
| `c` | Character device | Character device | キャラクターデバイス |
| `b` | Block device | Block device | ブロックデバイス |
| `p` | Named pipe | Named pipe | 名前付きパイプ |
| `s` | Socket | Socket | ソケット |

---

## 4. 🔧 `chmod` — Change Permissions

### 🇮🇩 Bahasa Indonesia
`chmod` (change mode) digunakan untuk **mengubah permission** file atau direktori. Ada dua cara penggunaan: **symbolic notation** (menggunakan huruf) dan **octal notation** (menggunakan angka).

### 🇬🇧 English
`chmod` (change mode) is used to **change permissions** of files or directories. There are two ways to use it: **symbolic notation** (using letters) and **octal notation** (using numbers).

### 🇯🇵 日本語
`chmod`（change mode）はファイルやディレクトリの**パーミッションを変更**するために使います。**シンボリック表記**（文字を使用）と**8進数表記**（数字を使用）の2つの使い方があります。

---

### Symbolic Notation

```bash
# Syntax
chmod <who><+/-><permission> <file>
```

| Symbol | 🇮🇩 Target | 🇬🇧 Target | 🇯🇵 対象 |
|--------|-----------|----------|---------|
| `u` | Owner (pemilik) | Owner (user) | 所有者 |
| `g` | Group | Group | グループ |
| `o` | Others (orang lain) | Others | その他 |
| `a` | All (semua) | All users | すべてのユーザー |
| `+` | Tambahkan permission | Add permission | パーミッションを追加 |
| `-` | Hapus permission | Remove permission | パーミッションを削除 |
| `=` | Set permission secara eksplisit | Set permission explicitly | パーミッションを明示的に設定 |

```bash
# Starting permissions
$ ls -l shell
-rwxr-x--x   1 cry0l1t3 htbteam 0 May 4 22:12 shell

# Add read permission for ALL users
$ chmod a+r shell && ls -l shell
-rwxr-xr-x   1 cry0l1t3 htbteam 0 May 4 22:12 shell

# Remove write from group
$ chmod g-w shell

# Add execute for owner only
$ chmod u+x shell

# Set exact permissions for others (read only)
$ chmod o=r shell
```

---

## 5. 🔢 Octal Notation

### 🇮🇩 Bahasa Indonesia
Sistem permission Linux berbasis **sistem bilangan oktal**. Setiap permission (r, w, x) memiliki nilai biner yang dijumlahkan menjadi angka oktal 0–7.

### 🇬🇧 English
The Linux permission system is based on the **octal number system**. Each permission (r, w, x) has a binary value that sums to an octal number 0–7.

### 🇯🇵 日本語
Linux のパーミッションシステムは**8進数システム**に基づいています。各パーミッション（r、w、x）はバイナリ値を持ち、0〜7の8進数に合計されます。

---

### Octal Calculation Table

```
Binary Notation:       4  2  1  |  4  2  1  |  4  2  1
                      ──────────────────────────────────
Binary Representation: 1  1  1  |  1  0  1  |  1  0  0
                      ──────────────────────────────────
Octal Value:              7     |     5     |     4
                      ──────────────────────────────────
Permission:            r  w  x  |  r  -  x  |  r  -  -
```

| Octal | Binary | Permissions | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 |
|-------|--------|-------------|---------|------------|---------|
| `0` | `000` | `---` | Tidak ada permission | No permissions | 権限なし |
| `1` | `001` | `--x` | Execute saja | Execute only | 実行のみ |
| `2` | `010` | `-w-` | Write saja | Write only | 書き込みのみ |
| `3` | `011` | `-wx` | Write + Execute | Write + Execute | 書き込み＋実行 |
| `4` | `100` | `r--` | Read saja | Read only | 読み取りのみ |
| `5` | `101` | `r-x` | Read + Execute | Read + Execute | 読み取り＋実行 |
| `6` | `110` | `rw-` | Read + Write | Read + Write | 読み取り＋書き込み |
| `7` | `111` | `rwx` | Full permission | Full permissions | フル権限 |

```bash
# Set permissions using octal: 754 = rwxr-xr--
$ chmod 754 shell && ls -l shell
-rwxr-xr--   1 cry0l1t3 htbteam 0 May 4 22:12 shell
#  7   5   4
# rwx r-x r--
# owner=7(rwx), group=5(r-x), others=4(r--)
```

### Common Octal Combinations

| Octal | Permissions | 🇮🇩 Use Case | 🇬🇧 Use Case | 🇯🇵 用途 |
|-------|-------------|------------|------------|---------|
| `777` | `rwxrwxrwx` | Semua bisa baca/tulis/eksekusi | Everyone can read/write/execute | 全員が読み書き実行可能 |
| `755` | `rwxr-xr-x` | Owner penuh, group & others bisa baca & eksekusi | Owner full, group & others read & execute | 所有者フル、他は読み取り＋実行 |
| `644` | `rw-r--r--` | Owner baca & tulis, others baca saja | Owner read & write, others read only | 所有者読み書き、他は読み取りのみ |
| `600` | `rw-------` | Hanya owner yang bisa akses | Only owner can access | 所有者のみアクセス可能 |
| `700` | `rwx------` | Hanya owner yang bisa baca/tulis/eksekusi | Only owner can read/write/execute | 所有者のみ全権限 |
| `400` | `r--------` | Read-only untuk owner (proteksi file penting) | Read-only for owner (protect important files) | 所有者のみ読み取り（重要ファイルの保護） |

---

## 6. 👤 `chown` — Change Owner

### 🇮🇩 Bahasa Indonesia
`chown` (change owner) digunakan untuk **mengubah pemilik dan/atau grup** dari sebuah file atau direktori. Hanya root atau user dengan hak sudo yang bisa menjalankan perintah ini.

### 🇬🇧 English
`chown` (change owner) is used to **change the owner and/or group** of a file or directory. Only root or users with sudo privileges can run this command.

### 🇯🇵 日本語
`chown`（change owner）はファイルやディレクトリの**所有者やグループを変更**するために使います。このコマンドを実行できるのは root または sudo 権限を持つユーザーのみです。

```bash
# Syntax
chown <user>:<group> <file/directory>

# Change owner to root, group to root
$ chown root:root shell && ls -l shell
-rwxr-xr--   1 root root 0 May 4 22:12 shell

# Change only the owner (keep current group)
$ chown cry0l1t3 shell

# Change only the group (keep current owner)
$ chown :htbteam shell

# Change owner recursively (entire directory)
$ chown -R root:root /var/www/html/
```

---

## 7. ⚡ SUID & SGID — Special Permission Bits

### 🇮🇩 Bahasa Indonesia
**SUID (Set User ID)** dan **SGID (Set Group ID)** adalah permission khusus yang memungkinkan user menjalankan program dengan **hak akses pemilik file** (bukan hak akses user yang menjalankan).

- **SUID** — program berjalan dengan hak akses **owner file**
- **SGID** — program berjalan dengan hak akses **group file**
- Ditandai dengan huruf **`s`** menggantikan `x` pada permission string

⚠️ **Risiko keamanan:** Jika program dengan SUID memiliki fitur untuk membuka shell (seperti `journalctl`), user biasa bisa mendapatkan akses **root shell** — ini adalah vektor privilege escalation yang umum!

### 🇬🇧 English
**SUID (Set User ID)** and **SGID (Set Group ID)** are special permissions that allow users to run programs with the **file owner's privileges** (not the executing user's privileges).

- **SUID** — program runs with **file owner's** privileges
- **SGID** — program runs with **file group's** privileges
- Indicated by the letter **`s`** replacing `x` in the permission string

⚠️ **Security risk:** If a SUID program has a feature to launch a shell (like `journalctl`), regular users could get a **root shell** — this is a common privilege escalation vector!

### 🇯🇵 日本語
**SUID（Set User ID）** と **SGID（Set Group ID）** は、ユーザーが**ファイル所有者の権限**でプログラムを実行できる特殊パーミッションです（実行ユーザーの権限ではなく）。

- **SUID** — プログラムは**ファイル所有者の**権限で実行される
- **SGID** — プログラムは**ファイルグループの**権限で実行される
- パーミッション文字列の `x` が **`s`** に置き換わる

⚠️ **セキュリティリスク：** SUID プログラムにシェルを起動する機能がある場合（`journalctl` など）、一般ユーザーが **root シェル**を取得できる可能性があります — これは一般的な権限昇格の手口です！

```bash
# SUID bit set (lowercase s = execute permission also set)
-rwsr-xr-x   1 root root 68208 Nov 24 16:11 /usr/bin/passwd
  │
  └── "s" here = SUID (runs as root regardless of who executes it)

# Set SUID bit
$ chmod u+s filename
$ chmod 4755 filename   # 4 = SUID bit

# Set SGID bit
$ chmod g+s filename
$ chmod 2755 filename   # 2 = SGID bit

# Find all SUID files on the system (pentesting!)
$ find / -type f -perm -4000 2>/dev/null

# Find all SGID files
$ find / -type f -perm -2000 2>/dev/null
```

> 🔴 **Pentesting note:** Finding SUID binaries is a critical step in privilege escalation. Check [GTFOBins](https://gtfobins.github.io) to see if a found SUID binary can be exploited to gain root access.

---

## 8. 📌 Sticky Bit

### 🇮🇩 Bahasa Indonesia
**Sticky bit** adalah permission khusus pada **direktori** yang memastikan hanya **pemilik file, pemilik direktori, atau root** yang bisa menghapus atau mengubah nama file di dalamnya — meskipun user lain memiliki write permission pada direktori tersebut.

Bayangkan sticky bit seperti **gembok pada laci pribadi** di ruang kerja bersama — semua orang bisa masuk ke ruangan, tapi tidak bisa membuka laci orang lain.

Ada dua varian sticky bit:
- **`t` (lowercase)** — Sticky bit aktif + execute permission juga ada
- **`T` (uppercase)** — Sticky bit aktif tapi **tidak ada execute permission** (others tidak bisa masuk)

### 🇬🇧 English
The **sticky bit** is a special permission on **directories** that ensures only the **file owner, directory owner, or root** can delete or rename files inside — even if other users have write permission on the directory.

Think of the sticky bit as a **lock on personal drawers** in a shared workspace — everyone can enter the room, but can't open each other's drawers.

Two variants of the sticky bit:
- **`t` (lowercase)** — Sticky bit active + execute permission also set
- **`T` (uppercase)** — Sticky bit active but **no execute permission** (others cannot enter)

### 🇯🇵 日本語
**スティッキービット**は**ディレクトリ**への特殊パーミッションで、**ファイルの所有者、ディレクトリの所有者、またはroot**のみがファイルを削除または名前変更できるようにします — 他のユーザーがそのディレクトリへの書き込み権限を持っていても同様です。

スティッキービットは共有ワークスペースの**個人ロッカーの鍵**のようなものです — 誰でも部屋に入れますが、他の人のロッカーは開けられません。

スティッキービットの2つのバリアント：
- **`t`（小文字）** — スティッキービット有効 + execute パーミッションも設定済み
- **`T`（大文字）** — スティッキービット有効だが **execute パーミッションなし**（他のユーザーはディレクトリに入れない）

```bash
$ ls -l
drw-rw-r-t 3 cry0l1t3 cry0l1t3 4096 Jan 12 12:30 scripts
drw-rw-r-T 3 cry0l1t3 cry0l1t3 4096 Jan 12 12:32 reports
#        │                                          │
#        └── lowercase t = sticky + execute set     └── uppercase T = sticky, NO execute
```

```
Sticky bit variants:
┌────────────────────────────────────────────────────────────┐
│  lowercase t  │  Sticky bit ON + Others have execute (x)   │
│               │  → Others CAN enter directory              │
│               │  → Others CANNOT delete other's files      │
├────────────────────────────────────────────────────────────┤
│  uppercase T  │  Sticky bit ON + Others have NO execute    │
│               │  → Others CANNOT enter directory           │
│               │  → Others CANNOT see contents              │
└────────────────────────────────────────────────────────────┘
```

```bash
# Set sticky bit
$ chmod +t /shared/directory
$ chmod 1777 /tmp           # 1 = sticky bit, 777 = full permissions

# Common example: /tmp always has sticky bit
$ ls -ld /tmp
drwxrwxrwt 18 root root 4096 Jan 12 12:00 /tmp
#        ↑ lowercase t = sticky + execute
```

> 💡 `/tmp` always has the sticky bit set (`1777`) so any user can create files there, but only the file owner can delete their own files.

---

## 📊 Special Permission Bits Summary

| Bit | Symbol | Octal | Set With | 🇮🇩 Efek | 🇬🇧 Effect | 🇯🇵 効果 |
|-----|--------|-------|----------|---------|----------|---------|
| **SUID** | `s` on owner `x` | `4xxx` | `chmod u+s` | Program berjalan sebagai owner file | Program runs as file owner | ファイル所有者として実行 |
| **SGID** | `s` on group `x` | `2xxx` | `chmod g+s` | Program berjalan sebagai group file | Program runs as file group | ファイルグループとして実行 |
| **Sticky** | `t`/`T` on others `x` | `1xxx` | `chmod +t` | Hanya owner yang bisa hapus filenya | Only owner can delete their files | 所有者のみファイルを削除可能 |

---

## 🔐 Permission Management Cheatsheet

```bash
# ── VIEW PERMISSIONS ────────────────────────────────────
ls -l file.txt              # view file permissions
ls -la                      # view all including hidden
stat file.txt               # detailed permission info

# ── CHMOD SYMBOLIC ──────────────────────────────────────
chmod u+x file.txt          # add execute for owner
chmod g-w file.txt          # remove write from group
chmod o=r file.txt          # set others to read only
chmod a+r file.txt          # add read for ALL users
chmod u+x,g-w file.txt      # multiple changes at once

# ── CHMOD OCTAL ─────────────────────────────────────────
chmod 777 file.txt          # rwxrwxrwx (everyone full)
chmod 755 file.txt          # rwxr-xr-x (standard binary)
chmod 644 file.txt          # rw-r--r-- (standard file)
chmod 600 file.txt          # rw------- (private file)
chmod 400 file.txt          # r-------- (read-only protected)

# ── CHOWN ───────────────────────────────────────────────
chown user file.txt         # change owner
chown user:group file.txt   # change owner and group
chown :group file.txt       # change group only
chown -R user:group dir/    # recursive change

# ── SPECIAL BITS ────────────────────────────────────────
chmod u+s file.txt          # set SUID
chmod g+s dir/              # set SGID
chmod +t dir/               # set sticky bit
chmod 4755 file.txt         # SUID + rwxr-xr-x
chmod 2755 dir/             # SGID + rwxr-xr-x
chmod 1777 dir/             # sticky + rwxrwxrwx

# ── FIND SPECIAL PERMISSION FILES (pentesting) ──────────
find / -perm -4000 2>/dev/null   # find all SUID files
find / -perm -2000 2>/dev/null   # find all SGID files
find / -perm -1000 2>/dev/null   # find all sticky bit dirs
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - [GTFOBins — SUID Exploitation](https://gtfobins.github.io)
> - `man chmod`, `man chown`, `man stat`
> - Linux Filesystem Hierarchy Standard

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.