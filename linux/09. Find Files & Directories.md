# 🔎 Find Files and Directories

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Command | Bahasa Indonesia | English | 日本語 |
|---|---------|-----------------|---------|--------|
| 1 | `which` | Cari lokasi program | Find program path | プログラムのパスを検索 |
| 2 | `find` | Cari file & folder dengan filter | Search files & folders with filters | フィルター付きファイル検索 |
| 3 | `locate` | Cari cepat via database | Fast search via database | データベースから高速検索 |

---

## 1. 🧭 `which`

### 🇮🇩 Bahasa Indonesia
`which` digunakan untuk **mencari lokasi (path) dari sebuah program** yang dapat dieksekusi. Sangat berguna saat kita ingin tahu apakah sebuah tool seperti `curl`, `netcat`, `wget`, `python`, atau `gcc` tersedia di sistem. Jika program tidak ditemukan, tidak ada output yang ditampilkan.

### 🇬🇧 English
`which` is used to **find the path of an executable program**. It is very useful when we want to know whether a tool like `curl`, `netcat`, `wget`, `python`, or `gcc` is available on the system. If the program is not found, no output is displayed.

### 🇯🇵 日本語
`which` は**実行可能なプログラムのパスを検索**するために使用します。`curl`、`netcat`、`wget`、`python`、`gcc` などのツールがシステムに存在するか確認するのに非常に便利です。プログラムが見つからない場合は何も表示されません。

```bash
# Check if Python is installed and where
$ which python
/usr/bin/python

# Check multiple tools at once
$ which curl wget netcat gcc
/usr/bin/curl
/usr/bin/wget
/usr/bin/netcat
/usr/bin/gcc

# Program not found = no output
$ which nonexistent
$
```

> 💡 **Use case in pentesting:** After gaining access to a system, run `which python python3 perl ruby nc wget curl` to quickly inventory available tools for post-exploitation.

---

## 2. 🔍 `find`

### 🇮🇩 Bahasa Indonesia
`find` adalah tool pencarian yang sangat powerful. Selain menemukan file dan folder, ia juga memiliki berbagai **opsi filter** seperti ukuran file, tanggal modifikasi, pemilik file, tipe objek, dan bahkan bisa **menjalankan perintah** pada setiap hasil yang ditemukan dengan flag `-exec`.

### 🇬🇧 English
`find` is an extremely powerful search tool. Beyond finding files and folders, it also provides various **filter options** like file size, modification date, file owner, object type, and can even **execute commands** on each result found using the `-exec` flag.

### 🇯🇵 日本語
`find` は非常に強力な検索ツールです。ファイルやフォルダを見つけるだけでなく、ファイルサイズ、更新日時、所有者、オブジェクトの種類などの**フィルターオプション**を持ち、`-exec` フラグで各検索結果に対して**コマンドを実行**することもできます。

### Syntax

```bash
find <location> <options>
```

### Example — Full Command

```bash
$ find / -type f -name *.conf -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
```

**Output:**
```
-rw-r--r-- 1 root root 136392 Apr 25 20:29 /usr/src/linux-headers-5.5.0/include/config/auto.conf
-rw-r--r-- 1 root root  82290 Apr 25 20:29 /usr/src/linux-headers-5.5.0/include/config/tristate.conf
-rw-r--r-- 1 root root  95813 May  7 14:33 /usr/share/metasploit-framework/data/jtr/repeats32.conf
-rw-r--r-- 1 root root  60346 May  7 14:33 /usr/share/metasploit-framework/data/jtr/dynamic.conf
-rw-r--r-- 1 root root  21254 May  2 11:59 /usr/share/doc/sqlmap/examples/sqlmap.conf
-rw-r--r-- 1 root root  25086 Mar  4 22:04 /etc/dnsmasq.conf
```

---

### 📋 `find` Options Breakdown

| Option | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|--------|----------------------|-------------|------------|
| `-type f` | Cari hanya **file** (`f`=file, `d`=direktori) | Search only **files** (`f`=file, `d`=directory) | **ファイル**のみ検索（`f`=ファイル、`d`=ディレクトリ） |
| `-name *.conf` | Cari file berekstensi `.conf` (wildcard `*`) | Search files with `.conf` extension (wildcard `*`) | `.conf` 拡張子のファイルを検索（ワイルドカード `*`） |
| `-user root` | Filter file milik user `root` | Filter files owned by user `root` | `root` ユーザーが所有するファイルを絞り込む |
| `-size +20k` | Hanya file **lebih besar dari 20 KiB** | Only files **larger than 20 KiB** | **20 KiB より大きい**ファイルのみ |
| `-newermt 2020-03-03` | Hanya file yang **dimodifikasi setelah** tanggal tersebut | Only files **modified after** the specified date | 指定した日付**以降に更新された**ファイルのみ |
| `-exec ls -al {} \;` | **Jalankan perintah** pada setiap hasil (`{}` = placeholder hasil) | **Execute a command** on each result (`{}` = result placeholder) | 各結果に対して**コマンドを実行**（`{}` = 結果のプレースホルダー） |
| `2>/dev/null` | Sembunyikan pesan **error** (redirect ke null device) | Suppress **error** messages (redirect to null device) | **エラーメッセージ**を非表示（null デバイスへリダイレクト） |

---

### 📐 Size Filter Reference

| Suffix | Unit | Example |
|--------|------|---------|
| `c` | Bytes | `-size +100c` |
| `k` | Kilobytes (KiB) | `-size +20k` |
| `M` | Megabytes (MiB) | `-size +5M` |
| `G` | Gigabytes (GiB) | `-size +1G` |
| `+` prefix | Larger than | `-size +20k` |
| `-` prefix | Smaller than | `-size -5k` |

---

### 🛠️ Practical `find` Examples

```bash
# Find all .conf files owned by root, larger than 20KB, modified after 2020-03-03
find / -type f -name *.conf -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null

# Find all directories named "backup"
find / -type d -name backup 2>/dev/null

# Find SUID files (critical for privilege escalation)
find / -type f -perm -4000 2>/dev/null

# Find writable files owned by current user
find / -type f -writable 2>/dev/null

# Find files modified in the last 7 days
find /home -type f -mtime -7

# Find files by exact size (exactly 1337 bytes)
find / -type f -size 1337c 2>/dev/null
```

> ⚠️ **Pentesting note:** `find / -perm -4000 2>/dev/null` searches for **SUID binaries** — files that run with the owner's privileges. These are prime targets for privilege escalation.

---

## 3. ⚡ `locate`

### 🇮🇩 Bahasa Indonesia
`locate` menawarkan cara pencarian yang **jauh lebih cepat** dibanding `find`. Alasannya: `locate` tidak menelusuri filesystem secara langsung, melainkan mencari dari **database lokal** yang berisi informasi semua file dan folder di sistem.

**Kelemahan:** Database perlu diperbarui secara manual dengan `sudo updatedb` — file yang baru dibuat mungkin belum masuk database.

**Kapan pakai `locate` vs `find`?**
- Gunakan `locate` untuk pencarian **cepat** tanpa filter kompleks
- Gunakan `find` ketika butuh filter spesifik (ukuran, tanggal, pemilik, dll.)

### 🇬🇧 English
`locate` offers a **much faster** search compared to `find`. The reason: `locate` does not traverse the filesystem directly — instead, it searches a **local database** containing information about all files and folders on the system.

**Limitation:** The database needs to be manually updated with `sudo updatedb` — newly created files may not yet be in the database.

**When to use `locate` vs `find`?**
- Use `locate` for **quick searches** without complex filters
- Use `find` when you need specific filters (size, date, owner, etc.)

### 🇯🇵 日本語
`locate` は `find` と比べて**はるかに高速**な検索を提供します。理由は、ファイルシステムを直接走査せず、システム上の全ファイルとフォルダの情報を持つ**ローカルデータベース**から検索するためです。

**制限：** `sudo updatedb` でデータベースを手動更新する必要があります — 新しく作成されたファイルはまだデータベースに入っていない場合があります。

**`locate` と `find` の使い分け：**
- 複雑なフィルターが不要な**高速検索**には `locate`
- サイズ、日時、所有者などの特定フィルターが必要な場合は `find`

```bash
# Update the locate database (run before first use or after new files added)
$ sudo updatedb

# Search for all .conf files
$ locate *.conf
/etc/GeoIP.conf
/etc/NetworkManager/NetworkManager.conf
/etc/UPower/UPower.conf
/etc/adduser.conf
...

# Search for a specific filename
$ locate shadow
/etc/shadow
/etc/shadow-
```

> 💡 `locate` is significantly faster than `find` for broad searches, but lacks fine-grained filtering. Always run `sudo updatedb` first to ensure the database is current.

---

## 📊 Command Comparison: `which` vs `find` vs `locate`

| Feature | `which` | `find` | `locate` |
|---------|---------|--------|----------|
| **Purpose** | Find executable path | Search files/dirs | Fast file search |
| **Speed** | ⚡ Instant | 🐢 Slow (live scan) | ⚡ Fast (database) |
| **Filter options** | ❌ None | ✅ Many (size, date, user…) | ❌ Minimal |
| **Real-time results** | ✅ Yes | ✅ Yes | ⚠️ Depends on `updatedb` |
| **Needs root** | ❌ No | ⚠️ For some paths | ❌ No (update needs sudo) |
| **Use case** | Check if tool exists | Complex targeted search | Quick broad search |

---

## 🔗 Combining Tools in a Workflow

```bash
# Step 1: Check if python3 is available
which python3

# Step 2: Find all Python scripts owned by root
find / -type f -name "*.py" -user root 2>/dev/null

# Step 3: Quick search for config files
sudo updatedb && locate *.conf

# Step 4: Find SUID files and list them in detail
find / -type f -perm -4000 -exec ls -la {} \; 2>/dev/null
```

---

## 🧠 Quick Reference Cheatsheet

```bash
# which — find executable location
which python
which curl wget netcat

# find — powerful search with filters
find / -type f -name "*.conf"              # all .conf files
find / -type d -name "backup"              # directories named backup
find / -type f -user root -size +20k       # root's files > 20KB
find / -type f -newermt 2020-01-01         # files modified after date
find / -type f -perm -4000 2>/dev/null     # SUID files
find / -type f -name "*.conf" -exec ls -al {} \; 2>/dev/null

# locate — fast database search
sudo updatedb                              # update database first
locate *.conf                              # find all .conf files
locate shadow                              # find files named shadow
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man find`, `man locate`, `man which`
> - GNU Findutils Documentation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.