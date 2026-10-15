# Windowsファイルシステム

> **LearnCybersecurity** | 基礎シリーズ | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-006` | **フェーズ0:** 基礎
> **推定学習時間:** 5-6時間 | **レベル:** 初級
> **前提:** LC-001
> **書籍対応:** Gray Hat Hacking（NTFS、Registry、ADS）
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック |
|---|---------|
| 1 | Windowsファイルシステムとは |
| 2 | ドライブレターシステム |
| 3 | 完全なディレクトリツリー |
| 4 | `C:\Windows` |
| 5 | `C:\Windows\System32` |
| 6 | `C:\Users` |
| 7 | `C:\Program Files` |
| 8 | `C:\ProgramData` |
| 9 | `C:\Temp`と`%TEMP%` |
| 10 | レジストリ |
| 11 | 環境変数 |
| 12 | NTFSと権限 |
| 13 | 隠しファイルと特殊ファイル |
| 14 | 機微なロケーションとハードニング |
| 15 | 実践的な偵察ナビゲーション |

---

## 重要な用語

この教材でよく出てくる言葉である。

| 用語 | 意味 |
|:---|:---|
| ドライブレター | Windowsは1つのルートではなく、各ボリュームに文字(`C:`、`D:`)を割り当てる |
| NTFS | 現代のWindowsファイルシステム(権限、ジャーナリング、暗号化) |
| パス | ファイルの場所。Windowsはバックスラッシュを使う(`C:\Users\alex`) |
| 環境変数 | パスへの名前付きの近道。`%APPDATA%` や `%SystemRoot%` など |
| レジストリ | ファイルツリーとは別の、Windowsの中心的な設定データベース |
| ACL | アクセス制御リスト。誰がread/write/executeできるかのファイルごとの規則 |
| ADS | 代替データストリーム。NTFSがファイルに付けられる隠しデータ |
| 隠し / システムファイル | 既定で表示されないよう印が付いたファイル |

---

## 1. 概要: Windowsファイルシステムとは

Windowsファイルシステムは、`/`を根とする単一のディレクトリツリーを使うLinuxとは違い、ドライブレター構造（C:、D:、E:など）を使う。各ドライブは独自のディレクトリ階層を持つ。

現代のWindowsはNTFS（New Technology File System）上で動作し、以下をサポートする。
- ACLによるファイル・フォルダ単位の細かい権限
- Alternate Data Streams（ADS）: ファイルに付随する隠しデータ
- ファイル・フォルダ暗号化（EFS）
- システム障害後の復旧のためのジャーナリング
- シンボリックリンクとジャンクション

これはセキュリティの仕事にとっていくつかの具体的な点で重要だ。
- 認証情報や設定ファイルの場所を知ることは偵察のターゲットを与える
- NTFS権限を理解することは権限昇格の前提知識になる
- ログの場所を知ることはフォレンジックとインシデントレスポンスを支える
- レジストリを理解することは永続化とマルウェア分析にとって重要
- どのディレクトリが書き込み可能かを知ることはペイロード配置にとって重要

---

## 2. ドライブレター: Windowsのドライブシステム

Windowsはパーティションとストレージデバイスを識別するためにドライブレターを使う。デフォルトでは、Windowsがインストールされている主ドライブは`C:\`だ。他のドライブ（USB、CD、追加パーティション）は次に使えるレターを順に割り当てられる。

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

| ドライブレター | 一般的な用途 |
|-----------------|---------------|
| `A:` / `B:` | フロッピーディスク（レガシー） |
| `C:` | 主システムドライブ |
| `D:` | セカンダリドライブ / DVD |
| `E:`以降 | USB、追加パーティション |

---

## 3. ファイルツリー: ディレクトリ構造全体

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

## 4. `C:\Windows`: 主要システムディレクトリ

`C:\Windows`はWindowsオペレーティングシステムの中核ディレクトリで、Linuxの`/`におおむね相当するが、対象範囲はファイルシステム全体ではなくOS自体に限られる。すべての重要なOSコンポーネント、ドライバ、システム設定ファイル、ログを保持している。この中身を変更してよいのはAdministratorとSYSTEMアカウントだけだ。

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

| サブディレクトリ | 内容 |
|-------------------|------|
| `System32\` | 64ビットシステムバイナリとDLL |
| `SysWOW64\` | 32ビットシステムバイナリ |
| `Temp\` | システム一時ファイル |
| `Prefetch\` | プログラムのプリフェッチデータ |
| `Logs\` | 追加のシステムログ |
| `inf\` | ドライバ情報ファイル |
| `Fonts\` | システムフォントファイル |

---

## 5. `C:\Windows\System32`: Windowsの心臓部

`System32`はWindowsで最も重要なディレクトリだ。コアシステムバイナリ、DLL（Dynamic Link Library）、ドライバ、レジストリ設定ファイル、イベントログを保持している。SAMデータベース（パスワードハッシュ）とイベントログを含むため、ペンテストの主要なターゲットになる。

「System32」という名前にもかかわらず、64ビットWindowsではこのディレクトリには64ビットバイナリが入っている。32ビットバイナリは`SysWOW64`にある。

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

### `System32\config\`内の重要ファイル

| ファイル | 内容 | ペンテストでの価値 |
|---------|------|---------------------|
| `SAM` | ローカルアカウントのパスワードハッシュ | 最重要 |
| `SYSTEM` | システム設定、ブートキー | 最重要 |
| `SECURITY` | ローカルセキュリティポリシー | 高 |
| `SOFTWARE` | インストール済みソフトウェアと設定 | 中 |
| `DEFAULT` | デフォルトユーザープロファイル | 低 |

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

## 6. `C:\Users`: ユーザーディレクトリ

`C:\Users`は、システムにログインしたことのあるすべてのユーザーのプロファイルディレクトリを保持している。各ユーザーは同じレイアウトのディレクトリを持ち、アプリケーションデータ、保存された認証情報、履歴を保存する隠しフォルダ`AppData`も含む。

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

### `C:\Users\<username>\`内の高価値ファイル

| パス | 内容 | ペンテストでの価値 |
|------|------|---------------------|
| `NTUSER.DAT` | ユーザーレジストリハイブ | 高 |
| `AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt` | PowerShell履歴 | 最重要 |
| `AppData\Roaming\Microsoft\Credentials\` | キャッシュされたドメイン認証情報 | 最重要 |
| `AppData\Local\Microsoft\Credentials\` | キャッシュされたローカル認証情報 | 高 |
| `AppData\Local\Google\Chrome\User Data\Default\Login Data` | Chromeブラウザのパスワード | 高 |
| `AppData\Roaming\Mozilla\Firefox\Profiles\` | Firefoxプロファイル | 高 |
| `.ssh\id_rsa` | SSH秘密鍵 | 高 |
| `Desktop\` | デスクトップ上のファイル | 中 |
| `Documents\` | ユーザーのドキュメント | 中 |

---

## 7. `C:\Program Files`: インストール済みアプリケーション

`C:\Program Files`は64ビットアプリケーションのデフォルトインストール先だ。`C:\Program Files (x86)`は64ビットシステム上の32ビットアプリケーションを保持する。どちらのディレクトリへの書き込みにもAdministrator権限が必要だ。

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

ペンテストのメモ: `Program Files`内のアプリケーションが緩すぎるフォルダやバイナリの権限を持って配布されていると、DLLハイジャックやバイナリの差し替えを通じた権限昇格のベクターになりうる。

---

## 8. `C:\ProgramData`: グローバルアプリケーションデータ

`C:\ProgramData`は、全ユーザー間で共有されるアプリケーションデータを保存する隠しディレクトリだ。ユーザーごとの`AppData`とは違い、`ProgramData`はグローバルだ。通常は設定ファイル、データベース、アプリケーションログを保持する。

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

## 9. `C:\Temp`と`%TEMP%`: 一時ファイル

Windowsは2つの一時ロケーションを持つ。`C:\Windows\Temp`（システム全体用）と`%TEMP%`（ユーザーごと、通常は`C:\Users\<user>\AppData\Local\Temp`）だ。どちらもペイロード配置に使われ得るし、どちらもフォレンジックに役立つ一時的な痕跡を残していることが多い。

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

## 10. レジストリ: Windows Registry

Windows Registryは、システム設定、アプリケーション設定、ユーザー情報を保存する中央集権的な階層データベースだ。Windowsのペンテストで理解すべき最も重要な要素であり、永続化、認証情報の保存、システム設定の主要な場所である。

レジストリはいくつかの主要なハイブ（ルートキー）に整理されている。

| ハイブ | 略称 | 内容 |
|--------|------|------|
| `HKEY_LOCAL_MACHINE` | `HKLM` | ローカルマシンの設定 |
| `HKEY_CURRENT_USER` | `HKCU` | 現在のユーザーの設定 |
| `HKEY_USERS` | `HKU` | すべてのユーザープロファイル |
| `HKEY_CLASSES_ROOT` | `HKCR` | ファイル関連付けとCOMオブジェクト |
| `HKEY_CURRENT_CONFIG` | `HKCC` | 現在のハードウェアプロファイル |

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

### ペンテストで重要なレジストリキー

| レジストリキー | 内容 | ペンテストでの価値 |
|-----------------|------|---------------------|
| `HKLM\SAM` | ローカルパスワードハッシュ | 最重要 |
| `HKLM\SYSTEM\CurrentControlSet\Services` | サービス一覧 | 高 |
| `HKLM\SOFTWARE\...\Winlogon` | 自動ログオン認証情報 | 最重要 |
| `HKCU\...\Run` | ユーザーの起動プログラム | 高 |
| `HKLM\...\Run` | システムの起動プログラム | 高 |
| `HKCU\Software\SimonTatham\PuTTY` | PuTTYのセッション/パスワード | 高 |

---

## 11. 環境変数: Windowsの環境変数

環境変数はシステム環境に関する情報を保存する。Windowsでは、CMDでは`%`記号、PowerShellでは`$env:`でアクセスする。フルパスなしで重要なディレクトリを指し示すため、ナビゲーションに便利だ。

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

| 変数 | 指す先 |
|------|--------|
| `%SYSTEMROOT%` | Windowsディレクトリ |
| `%USERPROFILE%` | ユーザーのホームディレクトリ |
| `%APPDATA%` | AppData Roaming |
| `%TEMP%` | ユーザーの一時フォルダ |
| `%PROGRAMFILES%` | Program Files（64ビット） |
| `%COMPUTERNAME%` | コンピュータ名 |
| `%USERNAME%` | 現在のユーザー名 |

---

## 12. NTFSと権限: ファイルシステムのセキュリティ

NTFSはACL（Access Control List）システムでアクセス権限を制御する。すべてのファイルとフォルダはDACL（Discretionary ACL）を持ち、誰が何をできるかを決めている。NTFS権限を理解することは、権限昇格とフォレンジックの両方にとって重要だ。

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

### NTFS権限の種類

| 権限 | 記号 | 意味 |
|------|------|------|
| Full Control | `F` | すべての権利 |
| Modify | `M` | 読み取り、書き込み、削除 |
| Read & Execute | `RX` | 読み取りと実行 |
| Read | `R` | 読み取りのみ |
| Write | `W` | 書き込みのみ |

---

## 13. 特殊ファイルと隠しファイル

Windowsは通常の表示からさまざまなファイルやディレクトリを隠している。ファイルが「隠される」方法はいくつかある。hidden属性、system属性、あるいは単にインデックスされないロケーションに置かれている場合だ。これらの一部は、フォレンジックとペンテストにとって非常に重要だ。

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

### 重要な隠しファイル

| ファイル/ディレクトリ | 内容 | ペンテストでの価値 |
|-------------------------|------|---------------------|
| `C:\pagefile.sys` | 仮想メモリ | 高 |
| `C:\hiberfil.sys` | ハイバネート時のRAMダンプ | 最重要 |
| `C:\$Recycle.Bin` | 削除されたファイル | 中 |
| `C:\System Volume Information` | シャドウコピー | 高 |
| `NTUSER.DAT` | ユーザーレジストリハイブ | 高 |
| `C:\Windows\Prefetch\*.pf` | プログラム実行の痕跡 | 高 |
| `winevt\Logs\Security.evtx` | セキュリティ/ログインログ | 高 |

---

## 14. セキュリティノート: 機微なロケーションと防御的ハードニング

以下のロケーションは攻撃者と防御者の双方にとって高価値だ。管理下にあるホストでの権限監査、監視、ハードニングに使い、攻撃的な認証情報抽出のレシピとしては使わないこと。

```cmd
:: ── HIGH-VALUE PATHS (defender inventory) ────────────────────
C:\Windows\System32\config\SAM
C:\Windows\System32\config\SYSTEM
:: Protect with disk encryption, ACL lockdown, backup hygiene

HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
:: Disable AutoLogon cleartext; audit DefaultPassword presence

%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
:: Avoid secrets on CLI; enable PS logging instead of relying on history

C:\Windows\Panther\Unattend.xml
C:\Windows\system32\sysprep\sysprep.xml
:: Remove leftover unattend files from images

C:\inetpub\wwwroot\web.config
:: Secrets → vault / DPAPI / KeyVault, not plaintext in web.config

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
C:\Windows\System32\Tasks\
:: Inventory autoruns; alert on unexpected changes

C:\Windows\System32\winevt\Logs\Security.evtx
:: Forward to SIEM; protect local log tampering
```

### 防御的ハードニングの重点

| コントロール | メモ |
|-------------|------|
| BitLocker / 暗号化 | オフラインでのSAM窃取から保護 |
| AutoLogonシークレットなし | 平文のAutoLogonを削除 |
| AlwaysInstallElevated | 無効化されていることを確認 |
| サービスACL | ユーザーが書き込めるバイナリパスがないこと |
| Autorunの棚卸し | Runキーとスケジュールタスクをベースライン化 |
| Unattendのクリーンアップ | ゴールデンイメージから除去 |
| イベント転送 | WEF / SIEM |

平文のWinlogonパスワード、残存したUnattend.xmlファイル、ユーザーが書き込めるサービスバイナリは、いずれも重大なハードニングの所見として扱う。レッドチームのシナリオを検討する前に、まずこれらを是正すること。

### Windowsセキュリティ優先度表

| ロケーション | リスクレベル | 理由 |
|--------------|---------------|------|
| `System32\config\SAM` | 最重要 | パスワードハッシュ |
| `Winlogon registry key` | 最重要 | 平文パスワード |
| `PSReadline history` | 最重要 | コマンド履歴とパスワード |
| `hiberfil.sys` | 最重要 | RAMの完全ダンプ |
| `AppData\Credentials` | 高 | キャッシュされた認証情報 |
| `NTUSER.DAT` | 高 | ユーザーレジストリハイブ |
| `Security.evtx` | 高 | ログインイベント |
| `Unattend.xml` | 最重要 | 平文の管理者パスワード |
| `Prefetch files` | 中 | 実行履歴 |
| `$Recycle.Bin` | 中 | 削除されたファイル |

---

## ディレクトリ一覧リファレンス表

| ディレクトリ | 機能 |
|-------------|------|
| `C:\` | 主システムドライブ |
| `C:\Windows` | OSのコアファイル |
| `C:\Windows\System32` | 64ビットシステムバイナリ |
| `C:\Windows\SysWOW64` | 32ビットシステムバイナリ |
| `C:\Windows\System32\config` | レジストリハイブとSAM |
| `C:\Windows\System32\winevt` | Windows Event Logs |
| `C:\Windows\Temp` | システム一時領域 |
| `C:\Windows\Prefetch` | プリフェッチデータ |
| `C:\Users` | すべてのユーザープロファイル |
| `C:\Users\<user>\AppData` | ユーザーのアプリデータ |
| `C:\Program Files` | 64ビットアプリケーション |
| `C:\Program Files (x86)` | 32ビットアプリケーション |
| `C:\ProgramData` | グローバルアプリデータ |
| `C:\Temp` | 代替のシステム一時領域 |
| `C:\inetpub` | IISのWebサーバールート |
| `C:\$Recycle.Bin` | 削除されたファイル |

---

## 実践ワークフロー例

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

## クイックリファレンス早見表

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

> 参考文献:
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`)、許可された手法の文脈で参照
> - Georgia Weidman, *Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - [Microsoft Docs — Windows File Systems](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - [LOLBAS Project](https://lolbas-project.github.io)、防御側の認識向上のために参照

> **LearnCybersecurity** | 基礎シリーズ | kodoktheGr3at | 2026
