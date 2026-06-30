# 🖥️ Windows Command Prompt (cmd.exe)

> **LearnCybersecurity** | Windows Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Category | Bahasa Indonesia | English | 日本語 |
|---|----------|-----------------|---------|--------|
| 1 | Overview | Apa itu Command Prompt | What is Command Prompt | コマンドプロンプトとは |
| 2 | Navigation | Navigasi direktori | Directory navigation | ディレクトリナビゲーション |
| 3 | File & Folder | Manajemen file & folder | File & folder management | ファイル・フォルダ管理 |
| 4 | System Info | Informasi sistem | System information | システム情報 |
| 5 | Network | Perintah jaringan | Network commands | ネットワークコマンド |
| 6 | User & Process | User & proses | Users & processes | ユーザー・プロセス |
| 7 | Pentesting | Perintah enumerasi | Enumeration commands | 列挙コマンド |
| 8 | Cheatsheet | Referensi cepat | Quick reference | クイックリファレンス |

---

## 1. 🏢 Overview — What is Command Prompt

### 🇮🇩 Bahasa Indonesia
**Command Prompt** (`cmd.exe`) adalah command-line interpreter bawaan Windows yang memungkinkan pengguna berinteraksi dengan sistem operasi melalui teks perintah, tanpa perlu antarmuka grafis (GUI). cmd.exe sudah ada sejak era MS-DOS dan masih digunakan hingga sekarang.

Dari perspektif **cybersecurity**, memahami CMD penting untuk:
- **Enumerasi sistem** setelah mendapatkan akses (post-exploitation)
- Menjalankan **scripting** dan otomatisasi (batch files `.bat`)
- **Troubleshooting** jaringan dan sistem

### 🇬🇧 English
**Command Prompt** (`cmd.exe`) is Windows' built-in command-line interpreter that lets users interact with the operating system through text commands, without needing a graphical interface (GUI). cmd.exe has existed since the MS-DOS era and is still widely used today.

From a **cybersecurity** perspective, understanding CMD is important for:
- **System enumeration** after gaining access (post-exploitation)
- Running **scripting** and automation (batch files `.bat`)
- Network and system **troubleshooting**

### 🇯🇵 日本語
**コマンドプロンプト**（`cmd.exe`）はWindows標準のコマンドライン インタープリタで、グラフィカルインターフェース（GUI）を使わずにテキストコマンドでOSと対話できます。cmd.exeはMS-DOS時代から存在し、現在も広く使われています。

**サイバーセキュリティ**の観点から、CMDの理解は以下のために重要です：
- アクセス取得後の**システム列挙**（ポストエクスプロイテーション）
- **スクリプティング**と自動化（バッチファイル `.bat`）の実行
- ネットワークとシステムの**トラブルシューティング**

```cmd
REM Open Command Prompt
Win + R → type "cmd" → Enter

REM Open as Administrator
Win + X → "Command Prompt (Admin)" / "Terminal (Admin)"

REM Check the help menu
C:\> help

REM Get help for a specific command
C:\> help dir
C:\> dir /?
```

---

## 2. 📂 Navigation — Directory Navigation

### 🇮🇩 Bahasa Indonesia
Perintah navigasi digunakan untuk **berpindah antar direktori** dan **melihat isi folder** — setara dengan `cd` dan `ls` di Linux.

### 🇬🇧 English
Navigation commands are used to **move between directories** and **view folder contents** — equivalent to `cd` and `ls` on Linux.

### 🇯🇵 日本語
ナビゲーションコマンドは**ディレクトリ間を移動**し、**フォルダの内容を表示**するために使われます — Linuxの `cd` と `ls` に相当します。

```cmd
REM Show current directory
C:\Users\alex> cd

REM Change directory
C:\> cd Users\alex\Desktop

REM Go up one level
C:\Users\alex\Desktop> cd ..

REM Go to root of current drive
C:\Users\alex> cd \

REM Switch drives (C: to D:)
C:\> D:

REM List contents of current directory
C:\Users\alex> dir

REM List including hidden files
C:\Users\alex> dir /a

REM List recursively (all subfolders)
C:\Users\alex> dir /s

REM Print working directory path
C:\Users\alex> echo %cd%
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `cd` | Tampilkan/pindah direktori | Show/change directory | ディレクトリの表示・変更 |
| `cd ..` | Naik satu level | Go up one level | 一階層上に移動 |
| `cd \` | Ke root drive | Go to drive root | ドライブのルートへ移動 |
| `dir` | Daftar isi folder | List folder contents | フォルダの内容を一覧表示 |
| `dir /a` | Termasuk file tersembunyi | Include hidden files | 隠しファイルを含む |
| `dir /s` | Rekursif (semua subfolder) | Recursive (all subfolders) | 再帰的（全サブフォルダ） |
| `tree` | Tampilkan struktur folder | Display folder structure | フォルダ構造を表示 |

---

## 3. 📁 File & Folder Management

### 🇮🇩 Bahasa Indonesia
Perintah-perintah ini digunakan untuk **membuat, menyalin, memindahkan, dan menghapus** file maupun folder.

### 🇬🇧 English
These commands are used to **create, copy, move, and delete** files and folders.

### 🇯🇵 日本語
これらのコマンドは**ファイルやフォルダの作成、コピー、移動、削除**に使われます。

```cmd
REM Create a new folder
C:\> mkdir newfolder
C:\> md newfolder

REM Remove an empty folder
C:\> rmdir newfolder
C:\> rd newfolder

REM Remove a folder AND all its contents
C:\> rmdir /s /q newfolder

REM Create an empty file
C:\> type nul > file.txt

REM Copy a file
C:\> copy file.txt D:\backup\file.txt

REM Copy a folder (with subfolders)
C:\> xcopy C:\source D:\dest /s /e

REM Move a file or folder
C:\> move file.txt D:\backup\

REM Rename a file or folder
C:\> ren oldname.txt newname.txt

REM Delete a file
C:\> del file.txt

REM Delete a file silently (no confirmation)
C:\> del /q file.txt

REM View contents of a text file
C:\> type file.txt

REM Search for text inside files
C:\> findstr "password" file.txt

REM Find files by name
C:\> dir /s /b *.txt
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `mkdir` / `md` | Buat folder baru | Create new folder | 新しいフォルダを作成 |
| `rmdir` / `rd` | Hapus folder | Remove folder | フォルダを削除 |
| `copy` | Salin file | Copy file | ファイルをコピー |
| `xcopy` | Salin folder/file lanjutan | Advanced copy for folders/files | フォルダ・ファイルの高度なコピー |
| `move` | Pindah file/folder | Move file/folder | ファイル・フォルダを移動 |
| `ren` | Ganti nama | Rename | 名前を変更 |
| `del` | Hapus file | Delete file | ファイルを削除 |
| `type` | Tampilkan isi file teks | Display text file contents | テキストファイルの内容を表示 |
| `findstr` | Cari teks dalam file | Search text within files | ファイル内のテキストを検索 |

---

## 4. 💻 System Information

### 🇮🇩 Bahasa Indonesia
Perintah-perintah ini digunakan untuk **mendapatkan informasi tentang sistem** seperti versi OS, hardware, dan konfigurasi.

### 🇬🇧 English
These commands are used to **retrieve system information** such as OS version, hardware, and configuration.

### 🇯🇵 日本語
これらのコマンドは、OSのバージョン、ハードウェア、設定などの**システム情報を取得**するために使われます。

```cmd
REM Show detailed system info (OS, version, hotfixes, etc.)
C:\> systeminfo

REM Show OS version only
C:\> ver

REM Show environment variables
C:\> set

REM Show a specific environment variable
C:\> echo %USERNAME%
C:\> echo %COMPUTERNAME%
C:\> echo %PATH%

REM List installed hotfixes/patches
C:\> wmic qfe list

REM List installed software
C:\> wmic product get name,version

REM Show disk drive info
C:\> wmic logicaldisk get caption,description

REM Clear the screen
C:\> cls
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `systeminfo` | Info sistem lengkap | Full system information | 完全なシステム情報 |
| `ver` | Versi OS | OS version | OSバージョン |
| `set` | Tampilkan env variables | Show environment variables | 環境変数を表示 |
| `wmic qfe list` | Daftar hotfix terinstal | List installed hotfixes | インストール済みホットフィックス一覧 |
| `wmic product get name,version` | Daftar software terinstal | List installed software | インストール済みソフトウェア一覧 |
| `cls` | Bersihkan layar | Clear screen | 画面をクリア |

> 💡 **Pentesting note:** `systeminfo` and `wmic qfe list` are commonly used to check for missing patches that may indicate vulnerable, exploitable systems.

---

## 5. 🌐 Network Commands

### 🇮🇩 Bahasa Indonesia
Perintah jaringan digunakan untuk **diagnosa konektivitas**, melihat konfigurasi IP, dan troubleshooting jaringan.

### 🇬🇧 English
Network commands are used for **connectivity diagnostics**, viewing IP configuration, and network troubleshooting.

### 🇯🇵 日本語
ネットワークコマンドは**接続診断**、IP設定の確認、ネットワークのトラブルシューティングに使われます。

```cmd
REM Show IP configuration
C:\> ipconfig

REM Show detailed IP configuration (DNS, MAC, etc.)
C:\> ipconfig /all

REM Release and renew DHCP lease
C:\> ipconfig /release
C:\> ipconfig /renew

REM Flush DNS cache
C:\> ipconfig /flushdns

REM Test connectivity to a host
C:\> ping google.com

REM Trace the route to a host
C:\> tracert google.com

REM Show active network connections
C:\> netstat -ano

REM Show ARP table
C:\> arp -a

REM DNS lookup
C:\> nslookup google.com

REM Show all network shares
C:\> net share

REM List computers on the domain/workgroup
C:\> net view

REM Show routing table
C:\> route print
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `ipconfig` | Tampilkan konfigurasi IP | Show IP configuration | IP設定を表示 |
| `ipconfig /all` | Konfigurasi IP detail | Detailed IP configuration | 詳細なIP設定 |
| `ping` | Tes konektivitas | Test connectivity | 接続テスト |
| `tracert` | Lacak rute ke host | Trace route to host | ホストへの経路を追跡 |
| `netstat -ano` | Koneksi jaringan aktif + PID | Active connections + PID | アクティブな接続とPID |
| `arp -a` | Tampilkan tabel ARP | Show ARP table | ARPテーブルを表示 |
| `nslookup` | Lookup DNS | DNS lookup | DNSルックアップ |
| `net view` | Daftar komputer di network | List computers on network | ネットワーク上のコンピュータ一覧 |

> 💡 **Pentesting note:** `netstat -ano` combined with `tasklist` helps identify which process owns a suspicious open port.

---

## 6. 👤 Users & Processes

### 🇮🇩 Bahasa Indonesia
Perintah-perintah ini digunakan untuk **mengelola user account** dan **memonitor proses** yang sedang berjalan di sistem.

### 🇬🇧 English
These commands are used to **manage user accounts** and **monitor running processes** on the system.

### 🇯🇵 日本語
これらのコマンドは**ユーザーアカウントの管理**とシステム上で実行中の**プロセスの監視**に使われます。

```cmd
REM Show current logged-in user
C:\> whoami

REM Show current user's privileges
C:\> whoami /priv

REM Show current user's group memberships
C:\> whoami /groups

REM List all local user accounts
C:\> net user

REM Show details of a specific user
C:\> net user alex

REM Create a new local user
C:\> net user alex P@ssw0rd123 /add

REM Add user to local Administrators group
C:\> net localgroup administrators alex /add

REM Change a user's password
C:\> net user alex NewP@ssw0rd /add

REM Delete a user
C:\> net user alex /delete

REM List running processes
C:\> tasklist

REM Find a specific process
C:\> tasklist | findstr "chrome"

REM Kill a process by PID
C:\> taskkill /PID 1234 /F

REM Kill a process by name
C:\> taskkill /IM notepad.exe /F
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `whoami` | Tampilkan user saat ini | Show current user | 現在のユーザーを表示 |
| `whoami /priv` | Tampilkan privilege user | Show user privileges | ユーザー権限を表示 |
| `net user` | Daftar semua user lokal | List all local users | すべてのローカルユーザー一覧 |
| `net user /add` | Buat user baru | Create new user | 新規ユーザー作成 |
| `net localgroup administrators` | Kelola grup admin | Manage administrators group | 管理者グループの管理 |
| `tasklist` | Daftar proses berjalan | List running processes | 実行中のプロセス一覧 |
| `taskkill` | Hentikan proses | Terminate a process | プロセスを終了 |

> 🔴 **Critical:** Always run CMD **as Administrator** when using `net user /add` or `net localgroup` — these require elevated privileges.

---

## 7. 🛡️ Pentesting — Enumeration Commands

### 🇮🇩 Bahasa Indonesia
Setelah mendapatkan akses ke sistem Windows, perintah-perintah berikut sering digunakan untuk **enumerasi cepat** guna memahami sistem dan mencari peluang **privilege escalation**.

### 🇬🇧 English
After gaining access to a Windows system, the following commands are commonly used for **quick enumeration** to understand the system and look for **privilege escalation** opportunities.

### 🇯🇵 日本語
Windowsシステムへのアクセスを取得した後、以下のコマンドはシステムを理解し**権限昇格**の機会を探すための**迅速な列挙**によく使われます。

```cmd
REM ── Basic Recon ─────────────────────────────────────
whoami /all                        REM full identity, groups, privileges
hostname                           REM computer name
systeminfo                         REM OS, patches, architecture
echo %username% %computername%     REM quick context

REM ── User & Group Enumeration ────────────────────────
net user                           REM list local users
net localgroup administrators      REM who's in admin group
net accounts                       REM password policy

REM ── Network Enumeration ─────────────────────────────
ipconfig /all                      REM network interfaces
netstat -ano                       REM active connections
arp -a                             REM known hosts on LAN

REM ── Files & Credentials Hunting ─────────────────────
dir /s /b *password*               REM find files with "password" in name
findstr /si password *.txt *.ini *.cfg   REM search content for "password"
type C:\Users\*\Desktop\*.txt      REM check desktop notes

REM ── Scheduled Tasks & Services (priv-esc vectors) ───
schtasks /query /fo LIST /v        REM list scheduled tasks
sc query                           REM list services
sc qc <servicename>                REM service config (check binary path)

REM ── Installed Software & Patches ────────────────────
wmic product get name,version
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

> ⚠️ **Note:** These commands are intended for **authorized** penetration testing and CTF environments only.

---

## 📊 Command Summary Table

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Admin needed? |
|---------|-----------|-------------|---------|----------------|
| `dir` | Daftar isi folder | List folder contents | フォルダ内容を一覧表示 | ❌ |
| `cd` | Pindah direktori | Change directory | ディレクトリを変更 | ❌ |
| `mkdir` / `rmdir` | Buat/hapus folder | Create/remove folder | フォルダの作成・削除 | ❌ (system folders: ✅) |
| `copy` / `move` | Salin/pindah file | Copy/move file | ファイルのコピー・移動 | ❌ |
| `del` | Hapus file | Delete file | ファイルを削除 | ❌ |
| `systeminfo` | Info sistem | System info | システム情報 | ❌ |
| `ipconfig` | Konfigurasi jaringan | Network configuration | ネットワーク設定 | ❌ |
| `ping` / `tracert` | Tes jaringan | Network testing | ネットワークテスト | ❌ |
| `netstat -ano` | Koneksi aktif | Active connections | アクティブな接続 | ❌ |
| `whoami` | User saat ini | Current user | 現在のユーザー | ❌ |
| `net user /add` | Buat user | Create user | ユーザー作成 | ✅ |
| `net localgroup` | Kelola grup | Manage groups | グループ管理 | ✅ |
| `tasklist` / `taskkill` | Kelola proses | Manage processes | プロセス管理 | ❌ (some processes: ✅) |
| `sc query` | Daftar service | List services | サービス一覧 | ❌ |
| `schtasks` | Scheduled tasks | Scheduled tasks | スケジュールタスク | ❌ (some actions: ✅) |

---

## 🔗 Practical Workflow Example

```cmd
REM ── SCENARIO: Quick Windows host enumeration ─────────

REM 1. Identify who and where you are
whoami /all
hostname
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

REM 2. Check network setup
ipconfig /all
netstat -ano

REM 3. Enumerate users and groups
net user
net localgroup administrators

REM 4. Look for interesting files
dir /s /b C:\Users\*password*
findstr /si password *.txt *.ini *.xml *.config

REM 5. Check scheduled tasks and services for priv-esc
schtasks /query /fo LIST /v
sc query

REM 6. Check running processes
tasklist /v
```

---

## 🧠 Quick Reference Cheatsheet

```cmd
:: ── NAVIGATION ──────────────────────────────────────────────
cd <path>                      :: change directory
cd ..                          :: go up one level
dir                            :: list contents
dir /s /b *.txt                :: find files recursively

:: ── FILE / FOLDER ───────────────────────────────────────────
mkdir <name>                   :: create folder
rmdir /s /q <name>             :: delete folder + contents
copy <src> <dest>              :: copy file
xcopy <src> <dest> /s /e       :: copy folder recursively
move <src> <dest>              :: move file/folder
del <file>                     :: delete file
type <file>                    :: view file contents
findstr "<text>" <file>        :: search inside file

:: ── SYSTEM INFO ─────────────────────────────────────────────
systeminfo                     :: full system info
ver                             :: OS version
set                             :: environment variables
wmic qfe list                  :: installed hotfixes
cls                             :: clear screen

:: ── NETWORK ──────────────────────────────────────────────────
ipconfig /all                  :: network config
ping <host>                    :: connectivity test
tracert <host>                 :: trace route
netstat -ano                   :: active connections + PID
nslookup <domain>              :: DNS lookup
arp -a                         :: ARP table

:: ── USERS / PROCESSES ───────────────────────────────────────
whoami /all                    :: current user, groups, privileges
net user                       :: list local users
net user <name> <pw> /add      :: create user
net localgroup administrators <name> /add  :: add to admin group
tasklist                       :: list running processes
taskkill /PID <pid> /F         :: kill process by PID
taskkill /IM <name>.exe /F     :: kill process by name

:: ── ENUMERATION (PENTESTING) ────────────────────────────────
whoami /priv                   :: check current privileges
net accounts                   :: password policy
schtasks /query /fo LIST /v    :: scheduled tasks
sc query                       :: list services
wmic product get name,version  :: installed software
dir /s /b *password*           :: hunt for files
```

---

> 📚 **References:**
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - `help`, `<command> /?`, Microsoft Docs — [Windows Commands Reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
> - Living Off The Land Binaries (LOLBAS) project — for advanced post-exploitation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.