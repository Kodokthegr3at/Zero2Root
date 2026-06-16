# 🪟 Windows File System

> **LearnCybersecurity** | Windows Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu Windows File System | What is the Windows File System | Windowsファイルシステムとは |
| 2 | Drive Letters | Sistem huruf drive | Drive letter system | ドライブレターシステム |
| 3 | File Tree | Pohon direktori lengkap | Full directory tree | 完全なディレクトリツリー |
| 4 | `C:\Windows` | Direktori sistem utama | Main system directory | メインシステムディレクトリ |
| 5 | `C:\Windows\System32` | Jantung sistem Windows | Heart of Windows system | Windowsシステムの中核 |
| 6 | `C:\Users` | Direktori pengguna | User directories | ユーザーディレクトリ |
| 7 | `C:\Program Files` | Software terinstal | Installed software | インストール済みソフト |
| 8 | `C:\ProgramData` | Data aplikasi global | Global application data | グローバルアプリデータ |
| 9 | `C:\Temp` & `%TEMP%` | File sementara | Temporary files | 一時ファイル |
| 10 | Registry | Registri Windows | Windows Registry | Windowsレジストリ |
| 11 | Environment Variables | Variabel lingkungan | Environment variables | 環境変数 |
| 12 | NTFS & Permissions | Filesystem & izin | Filesystem & permissions | ファイルシステムと権限 |
| 13 | Special Files | File & folder tersembunyi | Hidden & special files | 隠しファイルと特殊ファイル |
| 14 | Security Note | Direktori penting untuk pentest | Key dirs for pentesting | ペンテスト重要ディレクトリ |
| 15 | Workflow | Navigasi & rekon praktis | Practical recon navigation | 実践的な偵察ナビゲーション |

---

## 1. 🏢 Overview — What Is the Windows File System

### 🇮🇩 Bahasa Indonesia
**Windows File System** menggunakan struktur berbasis **drive letter** (C:, D:, E:, dll.) — berbeda dari Linux yang menggunakan satu pohon direktori tunggal dari `/`. Setiap drive memiliki hierarki direktorinya sendiri.

Filesystem yang digunakan Windows modern adalah **NTFS (New Technology File System)**, yang mendukung:
- **Permissions granular** per file/folder (ACL)
- **Alternate Data Streams (ADS)** — data tersembunyi di dalam file
- **File & folder encryption (EFS)**
- **Journaling** — pemulihan dari kegagalan sistem
- **Symbolic links & junctions**

**Mengapa penting untuk cybersecurity:**
- Mengetahui **lokasi credential dan konfigurasi** → target rekognisi
- Memahami **NTFS permissions** → privilege escalation
- Mengenal **lokasi log** → forensik dan incident response
- Memahami **Registry** → persistence & malware analysis
- Mengetahui **direktori yang dapat ditulis** → payload staging

### 🇬🇧 English
The **Windows File System** uses a **drive letter-based** structure (C:, D:, E:, etc.) — different from Linux which uses one single directory tree from `/`. Each drive has its own directory hierarchy.

The filesystem used by modern Windows is **NTFS (New Technology File System)**, which supports:
- **Granular per-file/folder permissions** (ACL)
- **Alternate Data Streams (ADS)** — hidden data inside files
- **File & folder encryption (EFS)**
- **Journaling** — recovery from system failures
- **Symbolic links & junctions**

**Why it matters for cybersecurity:**
- Knowing **credential and config locations** → reconnaissance target
- Understanding **NTFS permissions** → privilege escalation
- Knowing **log locations** → forensics and incident response
- Understanding the **Registry** → persistence & malware analysis
- Knowing **writable directories** → payload staging

### 🇯🇵 日本語
**Windowsファイルシステム**は**ドライブレターベース**の構造（C:、D:、E:など）を使います — `/`からの単一ディレクトリツリーを使うLinuxとは異なります。各ドライブには独自のディレクトリ階層があります。

現代のWindowsが使うファイルシステムは**NTFS（New Technology File System）**で、以下をサポートしています：
- **ファイル/フォルダごとの細かい権限**（ACL）
- **代替データストリーム（ADS）** — ファイル内の隠しデータ
- **ファイルとフォルダの暗号化（EFS）**
- **ジャーナリング** — システム障害からの回復
- **シンボリックリンクとジャンクション**

**サイバーセキュリティにとって重要な理由：**
- **認証情報と設定の場所**を知る → 偵察ターゲット
- **NTFS権限**を理解する → 権限昇格
- **ログの場所**を知る → フォレンジクスとインシデントレスポンス
- **レジストリ**を理解する → 永続化とマルウェア分析
- **書き込み可能なディレクトリ**を知る → ペイロードのステージング

---

## 2. 💽 Drive Letters — The Windows Drive System

### 🇮🇩 Bahasa Indonesia
Windows menggunakan **huruf drive** untuk mengidentifikasi partisi dan perangkat penyimpanan. Secara default, drive utama tempat Windows terinstal adalah **`C:\`**. Drive lain (USB, CD, partisi tambahan) mendapat huruf berikutnya secara berurutan.

### 🇬🇧 English
Windows uses **drive letters** to identify partitions and storage devices. By default, the primary drive where Windows is installed is **`C:\`**. Other drives (USB, CD, additional partitions) receive the next available letters sequentially.

### 🇯🇵 日本語
Windowsはパーティションとストレージデバイスを識別するために**ドライブレター**を使います。デフォルトでは、Windowsがインストールされているメインドライブは**`C:\`**です。他のドライブ（USB、CD、追加パーティション）は次の利用可能なレターを順番に取得します。

```cmd
:: List all drives
> wmic logicaldisk get name,description,size,freespace

:: Or in PowerShell
PS> Get-PSDrive -PSProvider FileSystem

Name  Used (GB)  Free (GB)  Provider   Root
----  ---------  ---------  --------   ----
C        85.2       14.8    FileSystem C:\
D         0.0       29.9    FileSystem D:\

:: Navigate drives in CMD
> C:         :: switch to C drive
> D:         :: switch to D drive
> cd C:\     :: go to root of C
```

| Drive Letter | 🇮🇩 Penggunaan Umum | 🇬🇧 Common Use | 🇯🇵 一般的な用途 |
|-------------|-------------------|--------------|----------------|
| `A:` / `B:` | Floppy disk (legacy) | Floppy disk (legacy) | フロッピーディスク（レガシー） |
| `C:` | Drive sistem utama | Primary system drive | メインシステムドライブ |
| `D:` | Drive sekunder / DVD | Secondary drive / DVD | セカンダリドライブ/DVD |
| `E:` onward | USB, partisi tambahan | USB, extra partitions | USB、追加パーティション |

---

## 3. 🌳 File Tree — Full Directory Structure

```
C:\                                    ← Primary system drive (root)
│
├── Windows\                           ← Core OS files
│   ├── System32\                      ← 64-bit system binaries & DLLs
│   │   ├── cmd.exe                    ← Command Prompt
│   │   ├── powershell.exe             ← Windows PowerShell
│   │   ├── notepad.exe                ← Notepad
│   │   ├── calc.exe                   ← Calculator
│   │   ├── msiexec.exe                ← Windows Installer
│   │   ├── svchost.exe                ← Service host process
│   │   ├── lsass.exe                  ← Local Security Authority (credentials!)
│   │   ├── winlogon.exe               ← Windows logon process
│   │   ├── taskmgr.exe                ← Task Manager
│   │   ├── reg.exe                    ← Registry editor (CLI)
│   │   ├── net.exe                    ← Network commands
│   │   ├── netstat.exe                ← Network statistics
│   │   ├── ipconfig.exe               ← IP configuration
│   │   ├── whoami.exe                 ← Current user info
│   │   ├── runas.exe                  ← Run as different user
│   │   ├── sc.exe                     ← Service control
│   │   ├── cacls.exe                  ← File ACL editor
│   │   ├── icacls.exe                 ← Improved ACL editor
│   │   ├── drivers\                   ← Kernel drivers (.sys files)
│   │   ├── config\                    ← SAM, SYSTEM, SECURITY hives!
│   │   │   ├── SAM                    ← Security Account Manager (password hashes!)
│   │   │   ├── SYSTEM                 ← System configuration hive
│   │   │   ├── SECURITY               ← Security policy hive
│   │   │   ├── SOFTWARE               ← Installed software hive
│   │   │   └── DEFAULT                ← Default user hive
│   │   ├── winevt\                    ← Windows Event Logs
│   │   │   └── Logs\
│   │   │       ├── System.evtx        ← System events
│   │   │       ├── Security.evtx      ← Security/login events
│   │   │       ├── Application.evtx   ← Application events
│   │   │       └── Microsoft-Windows-PowerShell%4Operational.evtx
│   │   ├── spool\                     ← Print spooler
│   │   └── Tasks\                     ← Scheduled tasks
│   │
│   ├── SysWOW64\                      ← 32-bit system binaries (on 64-bit OS)
│   ├── Temp\                          ← Windows temp files
│   ├── Logs\                          ← Additional OS logs
│   ├── Prefetch\                      ← Program prefetch data (forensics!)
│   ├── ServiceProfiles\               ← Service account profiles
│   │   ├── LocalService\
│   │   ├── NetworkService\
│   │   └── LocalSystem\
│   └── inf\                           ← Driver information files
│
├── Users\                             ← All user profile directories
│   ├── Public\                        ← Shared between all users
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   └── Downloads\
│   │
│   ├── Administrator\                 ← Built-in admin account
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   ├── Downloads\
│   │   ├── AppData\                   ← Application data (hidden)
│   │   │   ├── Local\                 ← Local app data
│   │   │   │   ├── Temp\              ← User temp files
│   │   │   │   ├── Microsoft\         ← MS app data
│   │   │   │   │   ├── Windows\
│   │   │   │   │   │   └── PowerShell\
│   │   │   │   │   │       └── ConsoleHost_history.txt  ← PS history!
│   │   │   │   │   └── Credentials\   ← Stored credentials!
│   │   │   │   └── Google\Chrome\     ← Browser data
│   │   │   ├── LocalLow\              ← Low-integrity app data
│   │   │   └── Roaming\               ← Synced across domain
│   │   │       ├── Microsoft\
│   │   │       │   ├── Windows\
│   │   │       │   │   ├── Recent\    ← Recently opened files
│   │   │       │   │   └── PowerShell\
│   │   │       │   └── Credentials\   ← Cached domain credentials!
│   │   │       └── Mozilla\Firefox\   ← Firefox profile
│   │   ├── NTUSER.DAT                 ← User registry hive!
│   │   └── .ssh\                      ← SSH keys (if installed)
│   │
│   └── alice\                         ← Regular user
│       └── (same structure as above)
│
├── Program Files\                     ← 64-bit installed applications
│   ├── Google\
│   ├── Mozilla Firefox\
│   ├── Microsoft Office\
│   └── Common Files\
│
├── Program Files (x86)\               ← 32-bit installed applications
│   └── (legacy 32-bit software)
│
├── ProgramData\                       ← Global app data (hidden)
│   ├── Microsoft\
│   │   ├── Windows\
│   │   │   └── Start Menu\
│   │   └── Windows Defender\          ← AV definitions & logs
│   └── (other app data)
│
├── Temp\                              ← System-wide temp folder
│
├── inetpub\                           ← IIS web server root
│   ├── wwwroot\                       ← Default web files
│   └── logs\                          ← IIS logs
│
├── $Recycle.Bin\                      ← Recycle Bin (hidden)
│
├── System Volume Information\         ← VSS shadow copies (hidden)
│
├── pagefile.sys                       ← Virtual memory page file
├── hiberfil.sys                       ← Hibernation file (RAM dump!)
├── swapfile.sys                       ← Modern swap file
└── bootmgr                            ← Windows boot manager
```

---

## 4. 🏰 `C:\Windows` — Main System Directory

### 🇮🇩 Bahasa Indonesia
`C:\Windows` adalah **direktori inti sistem operasi Windows** — setara dengan `/` di Linux namun dalam konteks OS. Berisi semua komponen penting OS, driver, file konfigurasi sistem, dan log. Hanya **Administrator/SYSTEM** yang boleh memodifikasi isinya.

### 🇬🇧 English
`C:\Windows` is the **core directory of the Windows operating system** — analogous to `/` in Linux but within the OS context. It contains all critical OS components, drivers, system config files, and logs. Only **Administrator/SYSTEM** accounts should modify its contents.

### 🇯🇵 日本語
`C:\Windows` はWindowsオペレーティングシステムの**コアディレクトリ** — LinuxのOSコンテキストにおける`/`に類似しています。すべての重要なOSコンポーネント、ドライバー、システム設定ファイル、ログが含まれています。**Administrator/SYSTEM**アカウントのみがその内容を変更できます。

```cmd
:: List Windows directory
> dir C:\Windows

:: Key subdirectories
> dir C:\Windows\System32
> dir C:\Windows\SysWOW64
> dir C:\Windows\Temp
> dir C:\Windows\Prefetch

:: Check Windows version
> winver
> ver

:: PowerShell
PS> [System.Environment]::OSVersion
PS> Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion
```

| Subdirectory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|-------------|--------|-------------|---------|
| `System32\` | Binary sistem 64-bit & DLL | 64-bit system binaries & DLLs | 64ビットシステムバイナリとDLL |
| `SysWOW64\` | Binary sistem 32-bit | 32-bit system binaries | 32ビットシステムバイナリ |
| `Temp\` | File sementara sistem | System temp files | システム一時ファイル |
| `Prefetch\` | Data prefetch program | Program prefetch data | プログラムプリフェッチデータ |
| `Logs\` | Log sistem tambahan | Additional system logs | 追加システムログ |
| `inf\` | File informasi driver | Driver information files | ドライバー情報ファイル |
| `Fonts\` | File font sistem | System font files | システムフォントファイル |

---

## 5. ⚙️ `C:\Windows\System32` — Heart of Windows

### 🇮🇩 Bahasa Indonesia
`System32` adalah **direktori terpenting di Windows** — berisi semua binary sistem inti, DLL (Dynamic Link Library), driver, file konfigurasi registry, dan log event. Ini adalah target utama dalam pentesting karena berisi **SAM database** (password hashes) dan **Event Logs**.

> ⚠️ Meskipun namanya "System32", pada Windows 64-bit direktori ini berisi binary **64-bit**. Binary 32-bit ada di `SysWOW64`.

### 🇬🇧 English
`System32` is the **most important directory in Windows** — containing all core system binaries, DLLs (Dynamic Link Libraries), drivers, registry config files, and event logs. It is a primary target in pentesting because it contains the **SAM database** (password hashes) and **Event Logs**.

> ⚠️ Despite being named "System32", on 64-bit Windows this directory contains **64-bit** binaries. 32-bit binaries live in `SysWOW64`.

### 🇯🇵 日本語
`System32` はWindowsの**最も重要なディレクトリ** — すべてのコアシステムバイナリ、DLL（ダイナミックリンクライブラリ）、ドライバー、レジストリ設定ファイル、イベントログが含まれています。**SAMデータベース**（パスワードハッシュ）と**イベントログ**が含まれているため、ペンテストの主要ターゲットです。

> ⚠️ 「System32」という名前にもかかわらず、64ビットWindowsではこのディレクトリに**64ビット**バイナリが含まれています。32ビットバイナリは`SysWOW64`にあります。

```cmd
:: Navigate to System32
> cd C:\Windows\System32

:: Key executables
> cmd.exe              :: Command Prompt
> powershell.exe       :: PowerShell
> lsass.exe            :: Credential storage process
> svchost.exe          :: Service host
> taskmgr.exe          :: Task Manager
> msiexec.exe          :: Windows Installer
> reg.exe              :: Registry CLI tool
> sc.exe               :: Service Control
> net.exe              :: Network commands
> whoami.exe           :: Current user
> icacls.exe           :: File permissions
> runas.exe            :: Run as another user

:: Registry hives (locked while OS runs)
> dir C:\Windows\System32\config\
SAM       SYSTEM    SECURITY    SOFTWARE    DEFAULT
```

### 🔑 Critical Files in `System32\config\`

| File | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `SAM` | Hash password akun lokal | Local account password hashes | ローカルアカウントのパスワードハッシュ | 🔴 Critical |
| `SYSTEM` | Konfigurasi sistem, boot key | System config, boot key | システム設定、ブートキー | 🔴 Critical |
| `SECURITY` | Kebijakan keamanan lokal | Local security policies | ローカルセキュリティポリシー | 🔴 High |
| `SOFTWARE` | Software terinstal & config | Installed software & config | インストール済みソフトとその設定 | 🟡 Medium |
| `DEFAULT` | Profil user default | Default user profile | デフォルトユーザープロファイル | 🟢 Low |

```cmd
:: SAM is locked while Windows runs — dump via shadow copy
:: Or use tools like: secretsdump.py, mimikatz

:: From attacker machine (via impacket):
$ python3 secretsdump.py -sam SAM -system SYSTEM LOCAL

:: Copy hives via shadow copy (requires admin):
> vssadmin create shadow /for=C:
> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM C:\temp\SAM
```

---

## 6. 👥 `C:\Users` — User Directories

### 🇮🇩 Bahasa Indonesia
`C:\Users` berisi **direktori profil untuk setiap pengguna** yang pernah login ke sistem. Setiap user memiliki direktori dengan struktur yang sama, termasuk folder `AppData` yang tersembunyi yang menyimpan data aplikasi, kredensial tersimpan, dan history.

### 🇬🇧 English
`C:\Users` contains **profile directories for every user** who has ever logged into the system. Each user has a directory with the same structure, including the hidden `AppData` folder which stores application data, saved credentials, and history.

### 🇯🇵 日本語
`C:\Users` にはシステムにログインしたことのある**すべてのユーザーのプロファイルディレクトリ**が含まれています。各ユーザーは同じ構造のディレクトリを持ち、アプリケーションデータ、保存された認証情報、履歴を保存する隠し`AppData`フォルダが含まれています。

```cmd
:: List all user profiles
> dir C:\Users
> net user

:: Navigate to a user profile
> cd C:\Users\alice

:: Show hidden AppData folder
> dir /a C:\Users\alice

:: PowerShell history (gold mine!)
> type C:\Users\alice\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

:: Stored Windows credentials
> cmdkey /list

:: Recent files
> dir C:\Users\alice\AppData\Roaming\Microsoft\Windows\Recent\

:: Check all users' PowerShell history
> foreach ($user in (Get-ChildItem C:\Users)) {
    $hist = "$($user.FullName)\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
    if (Test-Path $hist) { echo "=== $($user.Name) ==="; Get-Content $hist }
  }
```

### 🔑 High-Value Files in `C:\Users\<username>\`

| Path | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `NTUSER.DAT` | Registry hive pengguna | User registry hive | ユーザーレジストリハイブ | 🔴 High |
| `AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt` | Riwayat PowerShell | PowerShell history | PowerShell履歴 | 🔴 Critical |
| `AppData\Roaming\Microsoft\Credentials\` | Kredensial domain tersimpan | Cached domain credentials | キャッシュされたドメイン認証情報 | 🔴 Critical |
| `AppData\Local\Microsoft\Credentials\` | Kredensial lokal tersimpan | Cached local credentials | キャッシュされたローカル認証情報 | 🔴 High |
| `AppData\Local\Google\Chrome\User Data\Default\Login Data` | Password browser Chrome | Chrome browser passwords | Chromeブラウザパスワード | 🔴 High |
| `AppData\Roaming\Mozilla\Firefox\Profiles\` | Profil Firefox | Firefox profile | Firefoxプロファイル | 🔴 High |
| `.ssh\id_rsa` | SSH private key | SSH private key | SSH秘密鍵 | 🔴 High |
| `Desktop\` | File di desktop | Files on desktop | デスクトップのファイル | 🟡 Medium |
| `Documents\` | Dokumen pengguna | User documents | ユーザードキュメント | 🟡 Medium |

---

## 7. 📦 `C:\Program Files` — Installed Applications

### 🇮🇩 Bahasa Indonesia
`C:\Program Files` adalah lokasi default untuk **instalasi aplikasi 64-bit**. `C:\Program Files (x86)` digunakan untuk **aplikasi 32-bit** pada sistem 64-bit. Direktori ini memerlukan **hak Administrator** untuk menulis.

### 🇬🇧 English
`C:\Program Files` is the default location for **64-bit application installations**. `C:\Program Files (x86)` is used for **32-bit applications** on 64-bit systems. Writing to these directories requires **Administrator rights**.

### 🇯🇵 日本語
`C:\Program Files` は**64ビットアプリケーションのインストール**のデフォルト場所です。`C:\Program Files (x86)` は64ビットシステムの**32ビットアプリケーション**に使われます。これらのディレクトリへの書き込みには**管理者権限**が必要です。

```cmd
:: List installed 64-bit programs
> dir "C:\Program Files"

:: List installed 32-bit programs
> dir "C:\Program Files (x86)"

:: PowerShell - list all installed programs
PS> Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Sort-Object DisplayName

:: Common pentesting-relevant software locations
> dir "C:\Program Files\OpenSSH-Win64\"         :: SSH client/server
> dir "C:\Program Files\Git\"                   :: Git
> dir "C:\Program Files\Python*\"               :: Python
> dir "C:\Program Files\Microsoft SQL Server\"  :: SQL Server
> dir "C:\Program Files\FileZilla Server\"      :: FTP server
```

> 💡 **Pentesting note:** Aplikasi yang salah dikonfigurasi di `Program Files` dengan **permission yang terlalu longgar** bisa menjadi vektor privilege escalation melalui DLL hijacking atau binary planting.

---

## 8. 🗄️ `C:\ProgramData` — Global Application Data

### 🇮🇩 Bahasa Indonesia
`C:\ProgramData` adalah direktori **tersembunyi** yang menyimpan data aplikasi yang **dibagikan antar semua pengguna**. Berbeda dengan `AppData` yang per-user, `ProgramData` bersifat global. Sering berisi file konfigurasi, database, dan log aplikasi.

### 🇬🇧 English
`C:\ProgramData` is a **hidden** directory that stores application data **shared across all users**. Unlike `AppData` which is per-user, `ProgramData` is global. Often contains config files, databases, and application logs.

### 🇯🇵 日本語
`C:\ProgramData` は**すべてのユーザー間で共有される**アプリケーションデータを保存する**隠し**ディレクトリです。ユーザーごとの`AppData`とは異なり、`ProgramData`はグローバルです。設定ファイル、データベース、アプリケーションログが含まれることが多いです。

```cmd
:: Show hidden ProgramData (requires /a flag or Show Hidden Files)
> dir /a C:\ProgramData

:: Common contents
> dir C:\ProgramData\Microsoft\Windows Defender\   :: AV logs & exclusions
> dir C:\ProgramData\Microsoft\Windows\Start Menu\ :: All-users start menu
> dir C:\ProgramData\ssh\                          :: SSH server config (if installed)
> type C:\ProgramData\ssh\sshd_config

:: Search for config files with credentials
PS> Get-ChildItem -Path "C:\ProgramData" -Recurse -Include "*.conf","*.config","*.ini","*.xml" -ErrorAction SilentlyContinue |
    Select-String -Pattern "password|passwd|pwd" -CaseSensitive:$false
```

---

## 9. 🗑️ `C:\Temp` & `%TEMP%` — Temporary Files

### 🇮🇩 Bahasa Indonesia
Windows memiliki **dua lokasi temp**: `C:\Windows\Temp` (sistem) dan `%TEMP%` (per user, biasanya `C:\Users\<user>\AppData\Local\Temp`). Keduanya bisa digunakan untuk staging payload dan sering menjadi tempat artifact sementara yang berguna untuk forensik.

### 🇬🇧 English
Windows has **two temp locations**: `C:\Windows\Temp` (system-wide) and `%TEMP%` (per user, typically `C:\Users\<user>\AppData\Local\Temp`). Both can be used for payload staging and often contain temporary artifacts useful for forensics.

### 🇯🇵 日本語
Windowsには**2つのtempの場所**があります：`C:\Windows\Temp`（システム全体）と`%TEMP%`（ユーザーごと、通常`C:\Users\<user>\AppData\Local\Temp`）。どちらもペイロードのステージングに使えますが、フォレンジクスに有用な一時的なアーティファクトが含まれることが多いです。

```cmd
:: View system temp
> dir C:\Windows\Temp

:: View current user temp (expand variable)
> echo %TEMP%
C:\Users\alice\AppData\Local\Temp
> dir %TEMP%

:: PowerShell
PS> $env:TEMP
PS> Get-ChildItem $env:TEMP

:: Clear temp files
> del /q /f /s %TEMP%\*

:: Common attacker artifacts in temp:
:: - Downloaded payloads
:: - Extracted archives
:: - Compiled exploit binaries
:: - Credential dumps
```

---

## 10. 🗂️ Registry — Windows Registry

### 🇮🇩 Bahasa Indonesia
**Windows Registry** adalah **database hierarki terpusat** yang menyimpan konfigurasi sistem, pengaturan aplikasi, dan informasi pengguna. Registry adalah komponen terpenting untuk dipahami dalam Windows pentesting — ini adalah lokasi utama untuk **persistence**, **credential storage**, dan **system configuration**.

Registry terdiri dari **hive utama (root keys)**:

### 🇬🇧 English
The **Windows Registry** is a **centralized hierarchical database** that stores system configuration, application settings, and user information. The Registry is the most important component to understand in Windows pentesting — it is the primary location for **persistence**, **credential storage**, and **system configuration**.

The Registry consists of **main hives (root keys)**:

### 🇯🇵 日本語
**Windowsレジストリ**はシステム設定、アプリケーション設定、ユーザー情報を保存する**集中型階層データベース**です。レジストリはWindowsペンテストで理解すべき最も重要なコンポーネントです — **永続化**、**認証情報の保存**、**システム設定**の主要な場所です。

レジストリは**主要なハイブ（ルートキー）**で構成されています：

| Hive | Abbreviation | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|------|-------------|--------|-------------|---------|
| `HKEY_LOCAL_MACHINE` | `HKLM` | Konfigurasi mesin lokal | Local machine configuration | ローカルマシン設定 |
| `HKEY_CURRENT_USER` | `HKCU` | Konfigurasi user saat ini | Current user configuration | 現在のユーザー設定 |
| `HKEY_USERS` | `HKU` | Semua profil user | All user profiles | 全ユーザープロファイル |
| `HKEY_CLASSES_ROOT` | `HKCR` | Asosiasi file & COM objects | File associations & COM objects | ファイル関連付けとCOMオブジェクト |
| `HKEY_CURRENT_CONFIG` | `HKCC` | Hardware profile saat ini | Current hardware profile | 現在のハードウェアプロファイル |

```cmd
:: Open Registry Editor (GUI)
> regedit

:: Registry CLI — reg.exe
> reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run   :: startup programs
> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run   :: user startup

:: ── PERSISTENCE LOCATIONS IN REGISTRY ─────────────────────
:: Auto-run on startup (all users)
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

:: Auto-run on startup (current user)
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

:: ── CREDENTIAL-RELATED REGISTRY KEYS ───────────────────────
:: Windows autologon (may contain cleartext password!)
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

:: Stored VNC passwords
> reg query HKCU\Software\ORL\WinVNC3\Password
> reg query HKCU\Software\TightVNC\Server

:: PuTTY stored sessions
> reg query HKCU\Software\SimonTatham\PuTTY\Sessions

:: ── SYSTEM INFO VIA REGISTRY ────────────────────────────────
:: OS version
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName

:: Installed software
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

:: PowerShell
PS> Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" |
    Select-Object DefaultUserName, DefaultPassword, AutoAdminLogon
```

### 🔑 Critical Registry Keys for Pentesting

| Registry Key | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|-------------|--------|-------------|---------|--------------|
| `HKLM\SAM` | Hash password lokal | Local password hashes | ローカルパスワードハッシュ | 🔴 Critical |
| `HKLM\SYSTEM\CurrentControlSet\Services` | Daftar service | Service list | サービス一覧 | 🔴 High |
| `HKLM\SOFTWARE\...\Winlogon` | Auto-logon credentials | Auto-logon credentials | 自動ログイン認証情報 | 🔴 Critical |
| `HKCU\...\Run` | Program startup user | User startup programs | ユーザースタートアッププログラム | 🔴 High |
| `HKLM\...\Run` | Program startup sistem | System startup programs | システムスタートアッププログラム | 🔴 High |
| `HKCU\Software\SimonTatham\PuTTY` | PuTTY sessions/passwords | PuTTY sessions/passwords | PuTTYセッション/パスワード | 🟠 High |

---

## 11. 🌍 Environment Variables — Windows Env Vars

### 🇮🇩 Bahasa Indonesia
**Environment variables** adalah variabel yang menyimpan informasi tentang lingkungan sistem. Di Windows, bisa diakses dengan tanda `%` (CMD) atau `$env:` (PowerShell). Sangat berguna untuk navigasi karena menunjuk ke direktori penting tanpa harus tahu path lengkapnya.

### 🇬🇧 English
**Environment variables** store information about the system environment. In Windows, they are accessed with `%` signs (CMD) or `$env:` (PowerShell). Very useful for navigation because they point to important directories without needing the full path.

### 🇯🇵 日本語
**環境変数**はシステム環境に関する情報を保存します。Windowsでは`%`記号（CMD）または`$env:`（PowerShell）でアクセスします。完全なパスを知らなくても重要なディレクトリを指すため、ナビゲーションに非常に便利です。

```cmd
:: List all environment variables
> set
> set | findstr /i "path"

:: PowerShell
PS> Get-ChildItem Env:
PS> $env:PATH

:: ── KEY ENVIRONMENT VARIABLES ────────────────────────────────
%SYSTEMROOT%        :: C:\Windows
%SYSTEMDRIVE%       :: C:
%WINDIR%            :: C:\Windows
%PROGRAMFILES%      :: C:\Program Files
%PROGRAMFILES(X86)% :: C:\Program Files (x86)
%PROGRAMDATA%       :: C:\ProgramData
%USERPROFILE%       :: C:\Users\alice
%APPDATA%           :: C:\Users\alice\AppData\Roaming
%LOCALAPPDATA%      :: C:\Users\alice\AppData\Local
%TEMP%              :: C:\Users\alice\AppData\Local\Temp
%TMP%               :: Same as %TEMP%
%USERNAME%          :: alice
%USERDOMAIN%        :: WORKGROUP or DOMAIN_NAME
%COMPUTERNAME%      :: PC hostname
%PATH%              :: Directories searched for executables
%PATHEXT%           :: Executable file extensions

:: Use variables for navigation
> cd %USERPROFILE%
> cd %APPDATA%\Microsoft\Windows\PowerShell
> dir %SYSTEMROOT%\System32\config
```

| Variable | 🇮🇩 Menunjuk ke | 🇬🇧 Points to | 🇯🇵 指す先 |
|----------|---------------|-------------|----------|
| `%SYSTEMROOT%` | Direktori Windows | Windows directory | Windowsディレクトリ |
| `%USERPROFILE%` | Home direktori user | User home directory | ユーザーホームディレクトリ |
| `%APPDATA%` | AppData Roaming | AppData Roaming | AppData Roaming |
| `%TEMP%` | Folder temp user | User temp folder | ユーザー一時フォルダ |
| `%PROGRAMFILES%` | Program Files 64-bit | Program Files 64-bit | Program Files 64ビット |
| `%COMPUTERNAME%` | Nama komputer | Computer name | コンピューター名 |
| `%USERNAME%` | Nama user saat ini | Current username | 現在のユーザー名 |

---

## 12. 🔒 NTFS & Permissions — File System Security

### 🇮🇩 Bahasa Indonesia
**NTFS** menggunakan sistem **ACL (Access Control List)** untuk mengatur izin akses. Setiap file dan folder memiliki **DACL (Discretionary ACL)** yang menentukan siapa yang bisa melakukan apa. Memahami NTFS permissions sangat penting untuk privilege escalation dan forensik.

### 🇬🇧 English
**NTFS** uses an **ACL (Access Control List)** system to control access permissions. Each file and folder has a **DACL (Discretionary ACL)** that determines who can do what. Understanding NTFS permissions is critical for privilege escalation and forensics.

### 🇯🇵 日本語
**NTFS**はアクセス権限を制御するために**ACL（アクセス制御リスト）**システムを使います。各ファイルとフォルダには、誰が何をできるかを決定する**DACL（随意ACL）**があります。NTFS権限の理解は権限昇格とフォレンジクスにとって重要です。

```cmd
:: View file/folder permissions
> icacls C:\Windows\System32
> icacls C:\Users\alice\Desktop

:: Example output:
C:\Users\alice\Desktop
  BUILTIN\Administrators:(I)(F)     :: Full control
  NT AUTHORITY\SYSTEM:(I)(F)        :: Full control
  alice:(I)(OI)(CI)(F)              :: Full control (owner)
  BUILTIN\Users:(I)(RX)             :: Read & Execute

:: Check permissions on a specific file
> icacls C:\Windows\System32\config\SAM

:: Find writable directories (privilege escalation!)
PS> Get-ChildItem "C:\Program Files\" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.PSIsContainer } |
    ForEach-Object {
        $acl = Get-Acl $_.FullName
        if ($acl.Access | Where-Object { $_.IdentityReference -match "Everyone|Users" -and $_.FileSystemRights -match "Write|FullControl" }) {
            $_.FullName
        }
    }

:: Alternate Data Streams (ADS) — hide data in files
:: Create ADS
> echo "hidden data" > normal.txt:hidden_stream
:: Read ADS
> more < normal.txt:hidden_stream
:: List ADS
> dir /r normal.txt
> Get-Item normal.txt -Stream *
```

### 🔑 NTFS Permission Types

| Permission | Symbol | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 |
|-----------|--------|---------|-----------|---------|
| Full Control | `F` | Semua hak penuh | All rights | すべての権限 |
| Modify | `M` | Baca, tulis, hapus | Read, write, delete | 読み取り・書き込み・削除 |
| Read & Execute | `RX` | Baca & jalankan | Read & run | 読み取り・実行 |
| Read | `R` | Hanya baca | Read only | 読み取りのみ |
| Write | `W` | Hanya tulis | Write only | 書き込みのみ |

---

## 13. 👻 Special & Hidden Files

### 🇮🇩 Bahasa Indonesia
Windows menyembunyikan berbagai file dan direktori dari tampilan normal. Ada beberapa cara file bisa "tersembunyi": atribut hidden, atribut sistem, atau berada di lokasi yang tidak terindeks. Beberapa file ini sangat penting untuk forensik dan pentesting.

### 🇬🇧 English
Windows hides various files and directories from normal view. Files can be "hidden" in several ways: the hidden attribute, system attribute, or by being in non-indexed locations. Some of these files are critical for forensics and pentesting.

### 🇯🇵 日本語
Windowsは通常のビューから様々なファイルとディレクトリを隠しています。ファイルが「隠される」方法はいくつかあります：隠し属性、システム属性、またはインデックスされていない場所にあること。これらのファイルの一部はフォレンジクスとペンテストにとって非常に重要です。

```cmd
:: Show hidden files in CMD
> dir /a C:\
> dir /a /s C:\Users\alice

:: Show hidden files in PowerShell
PS> Get-ChildItem -Force C:\Users\alice
PS> Get-ChildItem -Force -Hidden C:\

:: ── IMPORTANT HIDDEN FILES ───────────────────────────────────

:: Page file (virtual memory — may contain sensitive data!)
> dir /a C:\pagefile.sys

:: Hibernation file (complete RAM dump at hibernate time!)
> dir /a C:\hiberfil.sys
:: Extract from hiberfil.sys (Volatility/Hibernation tools)
$ python3 volatility3 -f hiberfil.sys windows.info

:: Recycle Bin
> dir /a C:\$Recycle.Bin\

:: System Volume Information (VSS shadow copies)
> dir /a "C:\System Volume Information\"

:: NTUSER.DAT (user registry hive — hidden in user profile)
> dir /a C:\Users\alice\NTUSER.DAT

:: Prefetch files (program execution evidence)
> dir C:\Windows\Prefetch\
> dir C:\Windows\Prefetch\ | findstr .pf

:: Windows Event Logs
> dir C:\Windows\System32\winevt\Logs\

:: View Windows Event Log
PS> Get-WinEvent -LogName Security -MaxEvents 50 |
    Where-Object { $_.Id -in 4624,4625,4648 } |
    Select-Object TimeCreated, Id, Message

:: Event IDs for pentesting
:: 4624 = Successful logon
:: 4625 = Failed logon
:: 4648 = Logon with explicit credentials
:: 4672 = Special privileges assigned (admin logon)
:: 4688 = Process creation
:: 4698 = Scheduled task created
```

### 🔑 Important Hidden Files

| File/Directory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|---------------|--------|-------------|---------|--------------|
| `C:\pagefile.sys` | Memory virtual | Virtual memory | 仮想メモリ | 🟠 High |
| `C:\hiberfil.sys` | Dump RAM saat hibernate | RAM dump at hibernate | ハイバネート時のRAMダンプ | 🔴 Critical |
| `C:\$Recycle.Bin` | File yang dihapus | Deleted files | 削除済みファイル | 🟡 Medium |
| `C:\System Volume Information` | Shadow copies | Shadow copies | シャドウコピー | 🔴 High |
| `NTUSER.DAT` | Registry hive user | User registry hive | ユーザーレジストリハイブ | 🔴 High |
| `C:\Windows\Prefetch\*.pf` | Bukti eksekusi program | Program execution evidence | プログラム実行証拠 | 🟠 High |
| `winevt\Logs\Security.evtx` | Log keamanan/login | Security/login logs | セキュリティ/ログインログ | 🔴 High |

---

## 14. 🔐 Security Note — Key Locations for Pentesting

### 🇮🇩 Bahasa Indonesia
Berikut adalah lokasi-lokasi **paling penting dari perspektif Windows pentesting**, baik untuk rekognisi, privilege escalation, credential dumping, maupun forensik:

### 🇬🇧 English
Here are the **most important locations from a Windows pentesting perspective**, whether for reconnaissance, privilege escalation, credential dumping, or forensics:

### 🇯🇵 日本語
偵察、権限昇格、認証情報ダンプ、フォレンジクスのいずれの観点からも、**Windowsペンテストの観点から最も重要な場所**を以下に示します：

```cmd
:: ── CREDENTIAL HUNTING ───────────────────────────────────────

:: Password hashes (requires admin + shadow copy or offline)
C:\Windows\System32\config\SAM
C:\Windows\System32\config\SYSTEM

:: Cleartext AutoLogon credentials in registry
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

:: PowerShell command history
%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

:: Stored credentials manager
> cmdkey /list

:: Browser saved passwords (Chrome)
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data

:: Unattended install files (may contain admin password!)
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep\sysprep.xml
C:\Windows\system32\sysprep.inf

:: web.config files (IIS credentials)
C:\inetpub\wwwroot\web.config
C:\Windows\Microsoft.NET\Framework*\*\web.config

:: ── PRIVILEGE ESCALATION ────────────────────────────────────

:: Writable Program Files directories
C:\Program Files\
C:\Program Files (x86)\

:: Always Install Elevated (if enabled = escalation!)
> reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
> reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

:: Services with weak permissions
> sc query
> accesschk.exe -uwcqv "Everyone" *
> accesschk.exe -uwcqv "Users" *

:: Unquoted service paths
> wmic service get name,displayname,pathname,startmode |
  findstr /i "auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """

:: ── PERSISTENCE LOCATIONS ────────────────────────────────────

:: Registry run keys
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

:: Scheduled tasks
C:\Windows\System32\Tasks\
C:\Windows\SysWOW64\Tasks\
> schtasks /query /fo LIST /v

:: Startup folders
C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\

:: Services
HKLM\SYSTEM\CurrentControlSet\Services\
> sc query type= all state= all

:: ── LOG ANALYSIS ─────────────────────────────────────────────
C:\Windows\System32\winevt\Logs\Security.evtx    :: login events
C:\Windows\System32\winevt\Logs\System.evtx      :: system events
C:\Windows\System32\winevt\Logs\Application.evtx :: app events
C:\inetpub\logs\LogFiles\                         :: IIS logs

:: ── FORENSIC ARTIFACTS ──────────────────────────────────────
C:\Windows\Prefetch\          :: program execution history
C:\hiberfil.sys               :: hibernation RAM dump
C:\$Recycle.Bin\              :: deleted files
C:\Users\*\AppData\Roaming\Microsoft\Windows\Recent\  :: recent files
```

### 📊 Windows Security Priority Table

| Location | 🔴 Risk Level | 🇮🇩 Alasan | 🇬🇧 Reason | 🇯🇵 理由 |
|----------|--------------|-----------|-----------|---------|
| `System32\config\SAM` | 🔴 Critical | Password hashes | Password hashes | パスワードハッシュ |
| `Winlogon registry key` | 🔴 Critical | Cleartext password | Cleartext password | クリアテキストパスワード |
| `PSReadline history` | 🔴 Critical | Command history + passwords | Command history + passwords | コマンド履歴+パスワード |
| `hiberfil.sys` | 🔴 Critical | Full RAM dump | Full RAM dump | 完全なRAMダンプ |
| `AppData\Credentials` | 🔴 High | Cached credentials | Cached credentials | キャッシュされた認証情報 |
| `NTUSER.DAT` | 🔴 High | User registry hive | User registry hive | ユーザーレジストリハイブ |
| `Security.evtx` | 🟠 High | Login events | Login events | ログインイベント |
| `Unattend.xml` | 🔴 Critical | Admin password in plaintext | Admin password in plaintext | プレーンテキストの管理者パスワード |
| `Prefetch files` | 🟡 Medium | Execution history | Execution history | 実行履歴 |
| `$Recycle.Bin` | 🟡 Medium | Deleted files | Deleted files | 削除済みファイル |

---

## 📊 Complete Directory Reference Table

| Directory | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|-----------|-----------|-------------|---------|
| `C:\` | Drive sistem utama | Primary system drive | メインシステムドライブ |
| `C:\Windows` | File inti OS | Core OS files | コアOSファイル |
| `C:\Windows\System32` | Binary sistem 64-bit | 64-bit system binaries | 64ビットシステムバイナリ |
| `C:\Windows\SysWOW64` | Binary sistem 32-bit | 32-bit system binaries | 32ビットシステムバイナリ |
| `C:\Windows\System32\config` | Registry hives + SAM | Registry hives + SAM | レジストリハイブ+SAM |
| `C:\Windows\System32\winevt` | Windows Event Logs | Windows Event Logs | Windowsイベントログ |
| `C:\Windows\Temp` | Temp sistem | System temp | システム一時 |
| `C:\Windows\Prefetch` | Data prefetch | Prefetch data | プリフェッチデータ |
| `C:\Users` | Profil semua user | All user profiles | 全ユーザープロファイル |
| `C:\Users\<user>\AppData` | Data aplikasi user | User app data | ユーザーアプリデータ |
| `C:\Program Files` | Aplikasi 64-bit | 64-bit applications | 64ビットアプリケーション |
| `C:\Program Files (x86)` | Aplikasi 32-bit | 32-bit applications | 32ビットアプリケーション |
| `C:\ProgramData` | Data aplikasi global | Global app data | グローバルアプリデータ |
| `C:\Temp` | Temp sistem alternatif | Alternate system temp | 代替システム一時 |
| `C:\inetpub` | Root web server IIS | IIS web server root | IIS Webサーバールート |
| `C:\$Recycle.Bin` | File terhapus | Deleted files | 削除済みファイル |

---

## 🔗 Practical Workflow Example

```cmd
:: ── SCENARIO: Windows post-exploitation filesystem recon ────

:: 1. Who am I and what privileges do I have?
> whoami
> whoami /priv
> whoami /groups
> net user %USERNAME%

:: 2. System information
> systeminfo
> hostname
> echo %COMPUTERNAME%
> echo %USERDOMAIN%

:: 3. List all local users
> net user
> net localgroup administrators

:: 4. Hunt for AutoLogon credentials (cleartext!)
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

:: 5. Check PowerShell history
> type "%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"

:: 6. List stored credentials
> cmdkey /list

:: 7. Find unattended install files
> dir /s /b C:\*.xml | findstr /i "unattend sysprep"
> type C:\Windows\Panther\Unattend.xml

:: 8. Check scheduled tasks for persistence
> schtasks /query /fo LIST /v | findstr /i "task\|run\|status"

:: 9. Check startup programs (persistence)
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> dir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
> dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\"

:: 10. Find services with unquoted paths (privesc)
> wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """"

:: 11. Check AlwaysInstallElevated (privesc if both = 1)
> reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
> reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

:: 12. Find recent security events
PS> Get-WinEvent -LogName Security -MaxEvents 100 |
    Where-Object { $_.Id -in 4624,4625,4648,4672 } |
    Select-Object TimeCreated,Id,@{n='Message';e={$_.Message.Substring(0,100)}}

:: 13. Search for config files with passwords
PS> Get-ChildItem -Path C:\ -Recurse -Include "*.config","*.xml","*.ini","*.txt" -ErrorAction SilentlyContinue |
    Select-String -Pattern "password|passwd|pwd|secret|credential" -CaseSensitive:$false |
    Select-Object Path, LineNumber, Line | Select-Object -First 20
```

---

## 🧠 Quick Reference Cheatsheet

```cmd
:: ── NAVIGATION ───────────────────────────────────────────────
cd C:\                              :: go to C drive root
dir /a                              :: list all including hidden
dir /s /b *.txt                     :: recursive search
tree C:\ /f /a                      :: show full file tree

:: ── KEY ENVIRONMENT VARIABLES ────────────────────────────────
%SYSTEMROOT%    → C:\Windows
%USERPROFILE%   → C:\Users\alice
%APPDATA%       → C:\Users\alice\AppData\Roaming
%LOCALAPPDATA%  → C:\Users\alice\AppData\Local
%TEMP%          → C:\Users\alice\AppData\Local\Temp
%PROGRAMFILES%  → C:\Program Files
%PROGRAMDATA%   → C:\ProgramData

:: ── CREDENTIAL HUNTING ───────────────────────────────────────
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
cmdkey /list
type "%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
dir /s /b C:\*pass* C:\*cred* C:\*vnc* C:\*.config 2>nul

:: ── REGISTRY (PERSISTENCE & PRIVESC) ─────────────────────────
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

:: ── SERVICES & TASKS ─────────────────────────────────────────
sc query type= all state= all
schtasks /query /fo LIST /v
wmic service get name,pathname,startmode | findstr /i "auto" | findstr /i /v "C:\Windows"

:: ── NETWORK INFO ─────────────────────────────────────────────
ipconfig /all
netstat -ano
arp -a
route print
net share
net use

:: ── USER & GROUPS ────────────────────────────────────────────
net user
net localgroup
net localgroup administrators
whoami /all
whoami /priv

:: ── SYSTEM INFO ──────────────────────────────────────────────
systeminfo
wmic os get Caption,Version,BuildNumber
wmic computersystem get Name,Domain,Manufacturer
ver

:: ── POWERSHELL EQUIVALENTS ───────────────────────────────────
PS> Get-ChildItem -Force -Recurse          :: dir /a /s
PS> Get-ItemProperty HKLM:\...\Run         :: reg query
PS> Get-WinEvent -LogName Security         :: Event logs
PS> Get-Service                            :: sc query
PS> Get-ScheduledTask                      :: schtasks
PS> Get-NetIPAddress                       :: ipconfig
PS> Get-NetTCPConnection                   :: netstat
PS> Get-LocalUser                          :: net user
PS> Get-LocalGroupMember Administrators    :: net localgroup administrators
```

---

> 📚 **References:**
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - [Microsoft Docs — Windows File System](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)
> - [PayloadsAllTheThings — Windows Privilege Escalation](https://github.com/swisskyrepo/PayloadsAllTheThings)
> - [GTFOBins Windows — LOLBAS](https://lolbas-project.github.io)
> - [Mimikatz Documentation](https://github.com/gentilkiwi/mimikatz)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.