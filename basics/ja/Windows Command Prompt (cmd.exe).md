# Windows コマンドプロンプト（cmd.exe）

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-004` | **フェーズ0:** 基礎
> **学習目安:** 3-4時間 | **レベル:** 初級
> **前提知識:** LC-001
> **書籍対応:** Gray Hat Hacking、Windows列挙の章
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック | 説明 |
|---|---------|------|
| 1 | 概要 | コマンドプロンプトとは |
| 2 | ナビゲーション | ディレクトリナビゲーション |
| 3 | ファイル・フォルダ管理 | ファイル・フォルダ管理 |
| 4 | システム情報 | システム情報 |
| 5 | ネットワーク | ネットワークコマンド |
| 6 | ユーザー・プロセス | ユーザーとプロセス |
| 7 | ホスト列挙 | 許可下のホスト列挙 |
| 8 | セキュリティノート | 監査ログとLOLBin防御 |
| 9 | チートシート | クイックリファレンス |

---

## 1. 概要: コマンドプロンプトとは

コマンドプロンプト（`cmd.exe`）はWindows標準のコマンドラインインタープリタで、グラフィカルインターフェース（GUI）を使わずにテキストコマンドでOSと対話できます。cmd.exeはMS-DOS時代から存在し、現在も広く使われています。

サイバーセキュリティの観点から、CMDの理解は以下のために重要です。
- アクセス取得後のシステム列挙（ポストエクスプロイテーション）
- バッチファイル（`.bat`）を使ったスクリプティングと自動化
- ネットワークとシステムのトラブルシューティング

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

## 2. ディレクトリナビゲーション

ナビゲーションコマンドは、ディレクトリ間を移動し、フォルダの内容を表示するために使われます。Linuxの `cd` と `ls` に相当します。

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

| コマンド | 機能 |
|---------|------|
| `cd` | ディレクトリの表示・変更 |
| `cd ..` | 一階層上に移動 |
| `cd \` | ドライブのルートへ移動 |
| `dir` | フォルダの内容を一覧表示 |
| `dir /a` | 隠しファイルを含む |
| `dir /s` | 再帰的（全サブフォルダ） |
| `tree` | フォルダ構造を表示 |

---

## 3. ファイル・フォルダ管理

これらのコマンドは、ファイルやフォルダの作成、コピー、移動、削除に使われます。

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

| コマンド | 機能 |
|---------|------|
| `mkdir` / `md` | 新しいフォルダを作成 |
| `rmdir` / `rd` | フォルダを削除 |
| `copy` | ファイルをコピー |
| `xcopy` | フォルダ・ファイルの高度なコピー |
| `move` | ファイル・フォルダを移動 |
| `ren` | 名前を変更 |
| `del` | ファイルを削除 |
| `type` | テキストファイルの内容を表示 |
| `findstr` | ファイル内のテキストを検索 |

---

## 4. システム情報

これらのコマンドは、OSのバージョン、ハードウェア、設定などのシステム情報を取得するために使われます。

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

| コマンド | 機能 |
|---------|------|
| `systeminfo` | 完全なシステム情報 |
| `ver` | OSバージョン |
| `set` | 環境変数を表示 |
| `wmic qfe list` | インストール済みホットフィックス一覧 |
| `wmic product get name,version` | インストール済みソフトウェア一覧 |
| `cls` | 画面をクリア |

ペンテスト時のメモ: `systeminfo` と `wmic qfe list` は、脆弱で悪用可能な可能性を示す未適用パッチを確認するためによく使われます。

---

## 5. ネットワークコマンド

ネットワークコマンドは、接続診断、IP設定の確認、ネットワークのトラブルシューティングに使われます。

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

| コマンド | 機能 |
|---------|------|
| `ipconfig` | IP設定を表示 |
| `ipconfig /all` | 詳細なIP設定 |
| `ping` | 接続テスト |
| `tracert` | ホストへの経路を追跡 |
| `netstat -ano` | アクティブな接続とPID |
| `arp -a` | ARPテーブルを表示 |
| `nslookup` | DNSルックアップ |
| `net view` | ネットワーク上のコンピュータ一覧 |

ペンテスト時のメモ: `netstat -ano` を `tasklist` と組み合わせることで、不審な開いているポートを所有しているプロセスを特定できます。

---

## 6. ユーザーとプロセス

これらのコマンドは、ユーザーアカウントの管理と、システム上で実行中のプロセスの監視に使われます。

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

| コマンド | 機能 |
|---------|------|
| `whoami` | 現在のユーザーを表示 |
| `whoami /priv` | ユーザー権限を表示 |
| `net user` | すべてのローカルユーザー一覧 |
| `net user /add` | 新規ユーザー作成 |
| `net localgroup administrators` | 管理者グループの管理 |
| `tasklist` | 実行中のプロセス一覧 |
| `taskkill` | プロセスを終了 |

重要: `net user /add` や `net localgroup` を使う際は、必ず管理者としてCMDを実行してください。これらは昇格した権限を必要とします。

---

## 7. 許可されたホスト列挙

許可された検証や自分のラボでは、以下のコマンドでWindowsホストの棚卸しと設定監査ができます。攻撃用のPrivEsc手順ではありません。

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

注記: これらのコマンドは、許可されたペネトレーションテスト、防御側の監査、CTF/ラボ環境のみを対象としています。

---

## 8. セキュリティノート: CMDのハードニング、監査、LOLBinへの意識

`cmd.exe` と組み込みユーティリティ（Living-off-the-Land）は、攻撃者と管理者の双方が使います。防御の基本は、権限の縮小、監査の有効化、そして正規バイナリの悪用を監視することです。

```cmd
:: ── Privilege & session hygiene ─────────────────────────────
whoami /groups
:: Prefer standard user for daily work; elevate only when required
:: Disable local admin where possible; use LAPS for workstation admins

:: ── Command-line process auditing (defender-side) ───────────
:: Enable via GPO: Audit Process Creation + Include command line
:: Event ID 4688 (Security) — review suspicious cmd.exe /c chains
wevtutil qe Security /q:"*[System[(EventID=4688)]]" /c:5 /f:text

:: ── Soften attack surface ───────────────────────────────────
:: AppLocker/WDAC: restrict who can launch cmd.exe / scripting hosts
:: Remove unnecessary local admin; block interactive logon for service accounts
:: Prefer PowerShell with Script Block Logging for admin automation (auditable)
```

| コントロール | 内容 |
|-------------|------|
| Least privilege | 日常の管理者シェル禁止 |
| Process creation audit | 4688とコマンドライン |
| WDAC / AppLocker | `cmd` 等を制限 |
| LOLBAS monitoring | 異常なLOLBinを警告 |
| Credential hygiene | パスワードを`echo`しない |

防御優先の原則: 予期しない `cmd.exe /c` の連鎖、`sc`/`schtasks` の変更、ユーザープロファイル全体への大量の `findstr` は、単なるノイズではなく捜索すべきシグナルとして扱ってください。

---

## コマンド概要表

| コマンド | 機能 | 管理者権限が必要か |
|---------|------|------------------|
| `dir` | フォルダ内容を一覧表示 | いいえ |
| `cd` | ディレクトリを変更 | いいえ |
| `mkdir` / `rmdir` | フォルダの作成・削除 | いいえ（システムフォルダ: はい） |
| `copy` / `move` | ファイルのコピー・移動 | いいえ |
| `del` | ファイルを削除 | いいえ |
| `systeminfo` | システム情報 | いいえ |
| `ipconfig` | ネットワーク設定 | いいえ |
| `ping` / `tracert` | ネットワークテスト | いいえ |
| `netstat -ano` | アクティブな接続 | いいえ |
| `whoami` | 現在のユーザー | いいえ |
| `net user /add` | ユーザー作成 | はい |
| `net localgroup` | グループ管理 | はい |
| `tasklist` / `taskkill` | プロセス管理 | いいえ（一部のプロセス: はい） |
| `sc query` | サービス一覧 | いいえ |
| `schtasks` | スケジュールタスク | いいえ（一部の操作: はい） |

---

## 実践的なワークフロー例

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

## クイックリファレンスチートシート

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

:: ── DEFENSE / AUDIT CHECKS ──────────────────────────────────
whoami /priv                   :: review privileges (expect minimal daily)
net accounts                   :: password policy inventory
wevtutil qe Security /c:3 /f:text   :: sample recent Security events
:: Prefer AppLocker/WDAC + 4688 command-line auditing in production
```

---

> **参考文献・書籍情報:**
> - Peter Kim、*The Hacker Playbook 3*（`~/Documents/Books/CyberSec/Ethical Hacking/`）、許可された手法の文脈
> - Georgia Weidman、*Penetration Testing: A Hands-On Introduction to Hacking*（`~/Documents/Books/CyberSec/Ethical Hacking/`）
> - Allen Harper 他、*Gray Hat Hacking*（`~/Documents/Books/CyberSec/Handbook/`）
> - Microsoft Docs、[Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)、Audit Process Creation
> - [LOLBAS Project](https://lolbas-project.github.io)、living-off-the-landバイナリに対する防御側の意識向上
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - `help`, `<command> /?`

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> **フィードバックや貢献を歓迎します。** 誤りを見つけた場合はissueまたはPRを開いてください。
