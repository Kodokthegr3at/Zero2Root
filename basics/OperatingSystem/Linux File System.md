# 🗂️ Linux File System

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu Linux File System | What is the Linux File System | Linuxファイルシステムとは |
| 2 | File Tree | Pohon direktori lengkap | Full directory tree | 完全なディレクトリツリー |
| 3 | Root `/` | Direktori akar | Root directory | ルートディレクトリ |
| 4 | `/bin` | Binary perintah esensial | Essential command binaries | 必須コマンドバイナリ |
| 5 | `/sbin` | Binary sistem administrator | System admin binaries | システム管理者バイナリ |
| 6 | `/etc` | File konfigurasi sistem | System configuration files | システム設定ファイル |
| 7 | `/home` | Direktori pengguna | User home directories | ユーザーホームディレクトリ |
| 8 | `/root` | Home untuk root user | Root user's home | rootユーザーのホーム |
| 9 | `/var` | Data variabel & log | Variable data & logs | 可変データとログ |
| 10 | `/tmp` | File sementara | Temporary files | 一時ファイル |
| 11 | `/usr` | Resource Unix bersama | Unix shared resources | Unix共有リソース |
| 12 | `/lib` | Library bersama | Shared libraries | 共有ライブラリ |
| 13 | `/dev` | File perangkat | Device files | デバイスファイル |
| 14 | `/proc` | Info proses & kernel | Process & kernel info | プロセス・カーネル情報 |
| 15 | `/sys` | Info hardware & kernel | Hardware & kernel info | ハードウェア・カーネル情報 |
| 16 | `/mnt` & `/media` | Mount point | Mount points | マウントポイント |
| 17 | `/opt` | Software opsional | Optional software | オプショナルソフトウェア |
| 18 | `/boot` | File booting | Boot files | ブートファイル |
| 19 | `/srv` | Data layanan server | Server service data | サーバーサービスデータ |
| 20 | Security Note | Direktori penting untuk pentest | Key dirs for pentesting | ペンテスト重要ディレクトリ |
| 21 | Workflow | Navigasi praktis | Practical navigation | 実践的なナビゲーション |

---

## 1. 🏢 Overview — What Is the Linux File System

### 🇮🇩 Bahasa Indonesia
**Linux File System** adalah struktur hierarki yang mengorganisir semua file dan direktori di sistem Linux. Berbeda dengan Windows yang menggunakan drive terpisah (C:, D:, dll.), Linux menggunakan **satu pohon direktori tunggal** yang dimulai dari `/` (root).

Semua yang ada di Linux — hardware, proses, konfigurasi, hingga data pengguna — **direpresentasikan sebagai file** dan diorganisir dalam hierarki ini. Prinsip ini dikenal sebagai **"Everything is a file"**.

Standar yang mengatur struktur ini disebut **FHS (Filesystem Hierarchy Standard)**, yang mendefinisikan tujuan dan isi dari setiap direktori utama agar konsisten antar distribusi Linux.

**Mengapa penting untuk cybersecurity:**
- Mengetahui **di mana file konfigurasi disimpan** → target rekognisi
- Memahami **direktori yang dapat ditulis** → potensi privilege escalation
- Mengenal **lokasi log** → forensik dan audit
- Mengetahui **di mana binary tersimpan** → lateral movement & persistence

### 🇬🇧 English
The **Linux File System** is a hierarchical structure that organizes all files and directories on a Linux system. Unlike Windows which uses separate drives (C:, D:, etc.), Linux uses **one single directory tree** starting from `/` (root).

Everything in Linux — hardware, processes, configuration, and user data — is **represented as a file** and organized in this hierarchy. This principle is known as **"Everything is a file"**.

The standard governing this structure is called **FHS (Filesystem Hierarchy Standard)**, which defines the purpose and contents of each major directory for consistency across Linux distributions.

**Why it matters for cybersecurity:**
- Knowing **where config files are stored** → reconnaissance target
- Understanding **writable directories** → potential privilege escalation
- Knowing **log locations** → forensics and auditing
- Knowing **where binaries live** → lateral movement & persistence

### 🇯🇵 日本語
**Linuxファイルシステム**はLinuxシステム上のすべてのファイルとディレクトリを整理する階層構造です。別々のドライブ（C:、D:など）を使うWindowsとは異なり、Linuxは`/`（ルート）から始まる**一つのディレクトリツリー**を使います。

Linux上のすべてのもの — ハードウェア、プロセス、設定、ユーザーデータ — が**ファイルとして表現され**、この階層に整理されます。この原則は**「Everything is a file（すべてはファイル）」**として知られています。

この構造を規定する標準は**FHS（ファイルシステム階層標準）**と呼ばれ、Linuxディストリビューション間の一貫性のために各主要ディレクトリの目的と内容を定義しています。

**サイバーセキュリティにとって重要な理由：**
- **設定ファイルの場所**を知る → 偵察ターゲット
- **書き込み可能なディレクトリ**を理解する → 権限昇格の可能性
- **ログの場所**を知る → フォレンジクスと監査
- **バイナリの場所**を知る → ラテラルムーブメントと永続化

---

## 2. 🌳 File Tree — Full Directory Structure

```
/                          ← Root of the entire file system
│
├── bin/                   ← Essential user binaries (ls, cp, cat, bash...)
├── sbin/                  ← System admin binaries (ifconfig, fdisk, reboot...)
├── etc/                   ← System-wide configuration files
│   ├── passwd             ← User account info
│   ├── shadow             ← Encrypted passwords
│   ├── group              ← Group definitions
│   ├── hosts              ← Static hostname resolution
│   ├── fstab              ← Filesystem mount table
│   ├── crontab            ← System-wide cron jobs
│   ├── sudoers            ← Sudo permissions
│   ├── ssh/               ← SSH daemon config
│   │   └── sshd_config
│   ├── apt/               ← APT package manager config
│   │   └── sources.list
│   ├── nginx/             ← Nginx web server config
│   ├── apache2/           ← Apache web server config
│   ├── systemd/           ← Systemd unit files
│   │   └── system/
│   ├── cron.d/            ← Additional cron jobs
│   ├── cron.daily/
│   ├── cron.weekly/
│   └── cron.monthly/
│
├── home/                  ← Home directories for regular users
│   ├── alice/             ← Alice's personal directory
│   │   ├── Desktop/
│   │   ├── Documents/
│   │   ├── Downloads/
│   │   ├── .bashrc        ← User shell config (hidden)
│   │   ├── .bash_history  ← Command history (hidden)
│   │   └── .ssh/          ← SSH keys (hidden)
│   │       ├── id_rsa     ← Private key
│   │       ├── id_rsa.pub ← Public key
│   │       └── authorized_keys
│   └── bob/
│
├── root/                  ← Home directory for root user
│   ├── .bashrc
│   ├── .bash_history
│   └── .ssh/
│
├── var/                   ← Variable data (changes frequently)
│   ├── log/               ← System & application logs
│   │   ├── syslog         ← General system log
│   │   ├── auth.log       ← Authentication log
│   │   ├── apache2/       ← Apache logs
│   │   │   ├── access.log
│   │   │   └── error.log
│   │   ├── nginx/         ← Nginx logs
│   │   └── mysql/         ← MySQL logs
│   ├── www/               ← Web server document root
│   │   └── html/          ← Default web files
│   ├── mail/              ← Mail spool
│   ├── spool/             ← Print & cron spools
│   │   └── cron/          ← Per-user crontabs
│   └── lib/               ← Persistent application data
│
├── tmp/                   ← Temporary files (cleared on reboot)
│
├── usr/                   ← Unix Shared Resources (read-only)
│   ├── bin/               ← Non-essential user binaries
│   ├── sbin/              ← Non-essential system binaries
│   ├── lib/               ← Libraries for /usr/bin & /usr/sbin
│   ├── local/             ← Locally installed software
│   │   ├── bin/
│   │   ├── lib/
│   │   └── share/
│   ├── share/             ← Architecture-independent data
│   │   ├── man/           ← Manual pages
│   │   └── doc/           ← Documentation
│   └── include/           ← C header files
│
├── lib/                   ← Shared libraries for /bin & /sbin
│   ├── x86_64-linux-gnu/
│   └── modules/           ← Kernel modules
│
├── lib64/                 ← 64-bit shared libraries
│
├── dev/                   ← Device files (virtual)
│   ├── sda                ← First hard disk
│   ├── sda1               ← First partition of sda
│   ├── tty                ← Terminal devices
│   ├── null               ← Null device (discards all input)
│   ├── zero               ← Zero device (outputs null bytes)
│   ├── random             ← Random number generator
│   └── urandom            ← Non-blocking random generator
│
├── proc/                  ← Virtual FS: process & kernel info
│   ├── 1/                 ← Info for PID 1 (systemd)
│   │   ├── cmdline        ← Command line of the process
│   │   ├── status         ← Process status
│   │   └── fd/            ← Open file descriptors
│   ├── cpuinfo            ← CPU information
│   ├── meminfo            ← Memory information
│   ├── net/               ← Network information
│   │   └── tcp            ← Active TCP connections
│   ├── version            ← Kernel version
│   └── mounts             ← Mounted filesystems
│
├── sys/                   ← Virtual FS: hardware & kernel interface
│   ├── class/
│   ├── block/
│   └── bus/
│
├── mnt/                   ← Temporary manual mount point
│
├── media/                 ← Auto-mounted removable media
│   ├── cdrom/
│   └── usb/
│
├── opt/                   ← Optional/third-party software
│   ├── google/
│   └── lampp/
│
├── boot/                  ← Boot loader & kernel files
│   ├── grub/              ← GRUB bootloader config
│   │   └── grub.cfg
│   ├── vmlinuz            ← Compressed Linux kernel
│   └── initrd.img         ← Initial RAM disk image
│
├── srv/                   ← Data served by the system
│   ├── http/              ← Web server data
│   └── ftp/               ← FTP server data
│
├── run/                   ← Runtime data (PID files, sockets)
│
└── snap/                  ← Snap package mount points
```

---

## 3. 🌐 `/` — Root Directory

### 🇮🇩 Bahasa Indonesia
`/` adalah **direktori paling atas** dalam hierarki file system Linux — titik awal dari semua path. Semua direktori lain adalah cabang dari root ini. Hanya **root user** yang memiliki izin penuh untuk menulis ke direktori root secara langsung.

### 🇬🇧 English
`/` is the **topmost directory** in the Linux file system hierarchy — the starting point of all paths. All other directories are branches from this root. Only the **root user** has full write permissions directly to the root directory.

### 🇯🇵 日本語
`/` はLinuxファイルシステム階層の**最上位ディレクトリ** — すべてのパスの出発点です。他のすべてのディレクトリはこのルートの枝です。**rootユーザー**のみがルートディレクトリへの完全な書き込み権限を持ちます。

```bash
# Navigate to root
$ cd /

# List root directory contents
$ ls -la /

drwxr-xr-x  20 root root 4096 Jun  1 00:00 .
drwxr-xr-x  20 root root 4096 Jun  1 00:00 ..
drwxr-xr-x   2 root root 4096 Jun  1 00:00 bin
drwxr-xr-x   3 root root 4096 Jun  1 00:00 boot
drwxr-xr-x  18 root root 3800 Jun  1 00:00 dev
drwxr-xr-x 135 root root 4096 Jun  1 00:00 etc
drwxr-xr-x   3 root root 4096 Jun  1 00:00 home
...
```

---

## 4. 📦 `/bin` — Essential User Binaries

### 🇮🇩 Bahasa Indonesia
`/bin` berisi **binary esensial** yang dibutuhkan oleh semua pengguna, bahkan saat sistem dalam mode single-user atau recovery. Perintah-perintah paling dasar yang kamu gunakan sehari-hari tinggal di sini.

### 🇬🇧 English
`/bin` contains **essential binaries** needed by all users, even when the system is in single-user or recovery mode. The most basic commands you use daily live here.

### 🇯🇵 日本語
`/bin` にはシングルユーザーモードやリカバリーモードでも**全ユーザーが必要とする必須バイナリ**が含まれています。日常的に使う最も基本的なコマンドがここにあります。

```bash
# Common binaries found in /bin
ls /bin

bash    cat    chmod   chown   cp     date
echo    grep   gzip    kill    ln     ls
mkdir   mount  mv      nano    ping   ps
pwd     rm     rmdir   sh      sleep  tar
touch   uname  vi      which   ...
```

| Binary | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `bash` | Shell utama | Primary shell | メインシェル |
| `ls` | Daftar isi direktori | List directory contents | ディレクトリ内容を一覧表示 |
| `cp` | Salin file | Copy files | ファイルをコピー |
| `mv` | Pindah/rename file | Move/rename files | ファイルを移動・名前変更 |
| `rm` | Hapus file | Remove files | ファイルを削除 |
| `cat` | Tampilkan isi file | Show file contents | ファイル内容を表示 |
| `grep` | Cari teks dalam file | Search text in files | ファイル内テキストを検索 |
| `chmod` | Ubah permission file | Change file permissions | ファイル権限を変更 |
| `ping` | Cek koneksi jaringan | Check network connection | ネットワーク接続を確認 |

---

## 5. 🔩 `/sbin` — System Administration Binaries

### 🇮🇩 Bahasa Indonesia
`/sbin` berisi binary untuk **administrasi sistem** yang umumnya hanya dijalankan oleh **root user**. Berisi tools untuk manajemen disk, konfigurasi jaringan, dan maintenance sistem.

### 🇬🇧 English
`/sbin` contains binaries for **system administration** that are typically only run by the **root user**. Contains tools for disk management, network configuration, and system maintenance.

### 🇯🇵 日本語
`/sbin` には通常**rootユーザー**のみが実行する**システム管理**用バイナリが含まれています。ディスク管理、ネットワーク設定、システムメンテナンス用のツールが含まれます。

```bash
# Common binaries in /sbin
ls /sbin

fdisk      fsck       ifconfig   init       ip
iptables   mkfs       mount      reboot     route
shutdown   sshd       swapon     umount     useradd
userdel    usermod    ...
```

| Binary | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `ifconfig` | Konfigurasi antarmuka jaringan | Configure network interfaces | ネットワークインターフェース設定 |
| `iptables` | Manajemen firewall | Firewall management | ファイアウォール管理 |
| `fdisk` | Manajemen partisi disk | Disk partition management | ディスクパーティション管理 |
| `useradd` | Tambah user baru | Add new user | 新しいユーザーを追加 |
| `reboot` | Restart sistem | Restart system | システムを再起動 |
| `fsck` | Periksa & perbaiki filesystem | Check & repair filesystem | ファイルシステムの確認・修復 |

---

## 6. ⚙️ `/etc` — System Configuration Files

### 🇮🇩 Bahasa Indonesia
`/etc` adalah **direktori terpenting** dari perspektif keamanan. Berisi **semua file konfigurasi sistem** — mulai dari akun pengguna, password, konfigurasi jaringan, hingga pengaturan service. Seluruh isi `/etc` hanya boleh diubah oleh **root user**.

### 🇬🇧 English
`/etc` is the **most important directory** from a security perspective. It contains **all system configuration files** — from user accounts, passwords, network config, to service settings. All contents of `/etc` should only be modified by the **root user**.

### 🇯🇵 日本語
`/etc` はセキュリティの観点から**最も重要なディレクトリ**です。ユーザーアカウント、パスワード、ネットワーク設定からサービス設定まで、**すべてのシステム設定ファイル**が含まれています。`/etc` の内容はすべて**rootユーザー**のみが変更できます。

```bash
# List /etc contents
$ ls /etc

# ── CRITICAL FILES IN /etc ──────────────────────────────────

# User accounts (readable by all)
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
alice:x:1000:1000:Alice:/home/alice:/bin/bash

# Encrypted passwords (root only!)
$ sudo cat /etc/shadow
root:$6$xyz...:18000:0:99999:7:::

# Group definitions
$ cat /etc/group
sudo:x:27:alice
docker:x:999:alice

# Static hostname resolution
$ cat /etc/hosts
127.0.0.1   localhost
10.10.10.1  target.htb

# Sudo permissions
$ sudo cat /etc/sudoers

# SSH server configuration
$ cat /etc/ssh/sshd_config

# Network interfaces (Debian/Ubuntu)
$ cat /etc/network/interfaces

# DNS resolver config
$ cat /etc/resolv.conf

# System hostname
$ cat /etc/hostname
```

### 🔑 Critical Files in `/etc`

| File | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 | Pentest Value |
|------|--------|-------------|---------|--------------|
| `/etc/passwd` | Info akun user | User account info | ユーザーアカウント情報 | 🔴 High |
| `/etc/shadow` | Password terenkripsi | Encrypted passwords | 暗号化パスワード | 🔴 Critical |
| `/etc/group` | Definisi grup | Group definitions | グループ定義 | 🟡 Medium |
| `/etc/sudoers` | Izin sudo | Sudo permissions | sudo権限 | 🔴 Critical |
| `/etc/hosts` | Resolusi hostname statis | Static hostname resolution | 静的ホスト名解決 | 🟡 Medium |
| `/etc/ssh/sshd_config` | Konfigurasi SSH | SSH configuration | SSH設定 | 🔴 High |
| `/etc/crontab` | Cron jobs sistem | System cron jobs | システムcronジョブ | 🔴 High |
| `/etc/fstab` | Tabel mount filesystem | Filesystem mount table | ファイルシステムマウントテーブル | 🟡 Medium |
| `/etc/resolv.conf` | Konfigurasi DNS | DNS configuration | DNS設定 | 🟡 Medium |

> ⚠️ **Pentesting note:** `/etc/passwd` dan `/etc/shadow` adalah target utama dalam privilege escalation. Jika bisa membaca `/etc/shadow`, gunakan tools seperti `john` atau `hashcat` untuk crack password.

---

## 7. 🏠 `/home` — User Home Directories

### 🇮🇩 Bahasa Indonesia
`/home` berisi **direktori pribadi untuk setiap pengguna biasa**. Setiap user memiliki subdirektori sendiri (`/home/username`) yang menjadi tempat penyimpanan file personal, konfigurasi aplikasi, dan file tersembunyi (dotfiles).

### 🇬🇧 English
`/home` contains **personal directories for each regular user**. Each user has their own subdirectory (`/home/username`) which stores personal files, application configurations, and hidden files (dotfiles).

### 🇯🇵 日本語
`/home` には**各一般ユーザーの個人ディレクトリ**が含まれています。各ユーザーは自分のサブディレクトリ（`/home/username`）を持ち、個人ファイル、アプリケーション設定、隠しファイル（ドットファイル）を保存します。

```bash
# List all user home directories
$ ls /home
alice  bob  charlie

# Explore a user's home directory
$ ls -la /home/alice

drwxr-xr-x  alice alice  .
drwxr-xr-x  root  root   ..
-rw-------  alice alice  .bash_history   ← command history!
-rw-r--r--  alice alice  .bashrc
-rw-r--r--  alice alice  .profile
drwx------  alice alice  .ssh/           ← SSH keys!
drwxr-xr-x  alice alice  Desktop/
drwxr-xr-x  alice alice  Documents/
drwxr-xr-x  alice alice  Downloads/

# High-value files in /home for pentesting
$ cat /home/alice/.bash_history     # command history
$ cat /home/alice/.ssh/id_rsa       # private SSH key
$ ls /home/alice/.ssh/authorized_keys
```

### 🔑 Key Hidden Files (Dotfiles) in `/home`

| File | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|------|--------|-------------|---------|
| `.bashrc` | Konfigurasi shell bash | Bash shell configuration | bashシェル設定 |
| `.bash_history` | Riwayat perintah | Command history | コマンド履歴 |
| `.bash_profile` | Login shell config | Login shell config | ログインシェル設定 |
| `.ssh/id_rsa` | Private key SSH | SSH private key | SSH秘密鍵 |
| `.ssh/authorized_keys` | Kunci yang diizinkan login | Authorized SSH keys | 許可されたSSHキー |
| `.profile` | Environment variables | Environment variables | 環境変数 |
| `.gitconfig` | Konfigurasi Git | Git configuration | Git設定 |

---

## 8. 👑 `/root` — Root User's Home

### 🇮🇩 Bahasa Indonesia
`/root` adalah **direktori home untuk superuser (root)**. Berbeda dari user biasa yang home-nya ada di `/home/username`, root memiliki direktori tersendiri di `/root`. Direktori ini **hanya bisa diakses oleh root**.

### 🇬🇧 English
`/root` is the **home directory for the superuser (root)**. Unlike regular users whose home is in `/home/username`, root has its own dedicated directory at `/root`. This directory is **only accessible by root**.

### 🇯🇵 日本語
`/root` は**スーパーユーザー（root）のホームディレクトリ**です。ホームが`/home/username`にある一般ユーザーとは異なり、rootは`/root`に専用ディレクトリを持ちます。このディレクトリは**rootのみがアクセスできます**。

```bash
# Access root's home (requires root)
$ sudo ls -la /root

drwx------  root root  .
drwxr-xr-x  root root  ..
-rw-------  root root  .bash_history   ← root's command history!
-rw-r--r--  root root  .bashrc
drwx------  root root  .ssh/
-rw-------  root root  .ssh/id_rsa

# Check root's command history (privilege escalation gold!)
$ sudo cat /root/.bash_history
```

> 🔴 **Pentesting note:** Mendapatkan akses ke `/root` berarti **fully compromised**. File `.bash_history` di sini bisa mengungkap password, perintah sensitif, atau lateral movement yang dilakukan admin.

---

## 9. 📊 `/var` — Variable Data & Logs

### 🇮🇩 Bahasa Indonesia
`/var` berisi **data yang sering berubah** selama operasi sistem normal — terutama log, spool, database runtime, dan file web server. Nama "var" berasal dari "variable". Direktori paling penting di sini untuk keamanan adalah **`/var/log`**.

### 🇬🇧 English
`/var` contains **data that frequently changes** during normal system operation — especially logs, spools, runtime databases, and web server files. The name "var" comes from "variable". The most security-important directory here is **`/var/log`**.

### 🇯🇵 日本語
`/var` には通常のシステム操作中に**頻繁に変化するデータ**が含まれています — 特にログ、スプール、ランタイムデータベース、Webサーバーファイルなど。「var」という名前は「variable（変数）」に由来します。ここでセキュリティ上最も重要なディレクトリは**`/var/log`**です。

```bash
# ── LOGS — /var/log ─────────────────────────────────────────

# General system log
$ tail -f /var/log/syslog

# Authentication log (login attempts, sudo usage)
$ tail -f /var/log/auth.log
$ grep "Failed password" /var/log/auth.log
$ grep "Accepted password" /var/log/auth.log

# Apache web server logs
$ tail -f /var/log/apache2/access.log
$ tail -f /var/log/apache2/error.log

# Nginx logs
$ tail -f /var/log/nginx/access.log

# Kernel messages
$ tail -f /var/log/kern.log

# ── WEB FILES — /var/www ────────────────────────────────────

# Default Apache web root
$ ls /var/www/html/
$ cat /var/www/html/index.html

# ── CRON SPOOLS — /var/spool/cron ───────────────────────────
$ sudo ls /var/spool/cron/crontabs/
```

### 📁 Key Subdirectories in `/var`

| Directory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|-----------|--------|-------------|---------|
| `/var/log` | Log sistem dan aplikasi | System and app logs | システムとアプリのログ |
| `/var/www` | File web server | Web server files | Webサーバーファイル |
| `/var/spool` | Print & cron queues | Print & cron queues | プリントとcronキュー |
| `/var/lib` | Data aplikasi persisten | Persistent app data | 永続的なアプリデータ |
| `/var/mail` | Mailbox pengguna | User mailboxes | ユーザーメールボックス |
| `/var/tmp` | File temp persisten | Persistent temp files | 永続的な一時ファイル |

---

## 10. 🗑️ `/tmp` — Temporary Files

### 🇮🇩 Bahasa Indonesia
`/tmp` adalah direktori untuk **file sementara** yang dibuat oleh proses dan pengguna. Isi direktori ini **dihapus otomatis saat sistem reboot**. Semua pengguna bisa membaca dan menulis ke `/tmp` — ini menjadikannya lokasi favorit untuk aktivitas berbahaya.

### 🇬🇧 English
`/tmp` is the directory for **temporary files** created by processes and users. Its contents are **automatically cleared on reboot**. All users can read and write to `/tmp` — making it a favorite location for malicious activity.

### 🇯🇵 日本語
`/tmp` はプロセスとユーザーが作成する**一時ファイル**のディレクトリです。その内容は**システム再起動時に自動的に消去されます**。すべてのユーザーが`/tmp`に読み書きできます — これが悪意のある活動の定番場所になる理由です。

```bash
# /tmp is world-writable
$ ls -la / | grep tmp
drwxrwxrwt  root root  tmp     ← "t" = sticky bit

# Common pentesting uses of /tmp
$ ls -la /tmp/                  # check for suspicious files

# Common attacker patterns in /tmp
# - Dropped payloads: /tmp/shell.elf
# - Compiled exploits: /tmp/exploit
# - Exfiltration staging: /tmp/loot.tar.gz
```

> ⚠️ **Pentesting note:** `/tmp` adalah lokasi standar untuk **drop payload** karena world-writable. Saat melakukan post-exploitation, selalu periksa `/tmp` untuk menemukan artefak dari attacker lain atau aktivitas mencurigakan.

---

## 11. 📚 `/usr` — Unix Shared Resources

### 🇮🇩 Bahasa Indonesia
`/usr` berisi **mayoritas program dan data yang digunakan pengguna** — ini adalah direktori terbesar di sebagian besar sistem Linux. Berbeda dengan `/bin` yang hanya berisi binary paling esensial, `/usr/bin` berisi semua binary non-esensial untuk pengguna biasa.

### 🇬🇧 English
`/usr` contains the **majority of programs and data used by users** — it is the largest directory on most Linux systems. Unlike `/bin` which holds only the most essential binaries, `/usr/bin` contains all non-essential binaries for regular users.

### 🇯🇵 日本語
`/usr` には**ユーザーが使用するプログラムとデータの大部分**が含まれています — ほとんどのLinuxシステムで最大のディレクトリです。最も必須のバイナリのみを持つ`/bin`とは異なり、`/usr/bin`には一般ユーザー向けの非必須バイナリがすべて含まれています。

```bash
$ ls /usr
bin  include  lib  lib64  local  sbin  share  src

# Most installed programs go here
$ ls /usr/bin | head -20
nmap  python3  gcc  vim  curl  wget  ssh  ...

# Locally compiled/installed software
$ ls /usr/local/bin

# Man pages
$ ls /usr/share/man/

# Documentation
$ ls /usr/share/doc/
```

| Directory | 🇮🇩 Isi | 🇬🇧 Contents | 🇯🇵 内容 |
|-----------|--------|-------------|---------|
| `/usr/bin` | Binary pengguna non-esensial | Non-essential user binaries | 非必須ユーザーバイナリ |
| `/usr/sbin` | Binary sistem non-esensial | Non-essential system binaries | 非必須システムバイナリ |
| `/usr/lib` | Library untuk /usr/bin | Libraries for /usr/bin | /usr/bin用ライブラリ |
| `/usr/local` | Software yang dikompilasi lokal | Locally compiled software | ローカルコンパイルソフト |
| `/usr/share` | Data arsitektur-independen | Architecture-independent data | アーキテクチャ非依存データ |
| `/usr/include` | C header files | C header files | Cヘッダーファイル |

---

## 12. 🔗 `/lib` — Shared Libraries

### 🇮🇩 Bahasa Indonesia
`/lib` berisi **shared libraries** (setara dengan .dll di Windows) yang dibutuhkan oleh binary di `/bin` dan `/sbin`. Juga berisi **kernel modules** di `/lib/modules/`.

### 🇬🇧 English
`/lib` contains **shared libraries** (equivalent to .dll in Windows) needed by binaries in `/bin` and `/sbin`. It also contains **kernel modules** in `/lib/modules/`.

### 🇯🇵 日本語
`/lib` には`/bin`と`/sbin`のバイナリが必要とする**共有ライブラリ**（Windowsの.dllに相当）が含まれています。また`/lib/modules/`に**カーネルモジュール**も含まれています。

```bash
# List shared libraries
$ ls /lib/x86_64-linux-gnu/ | head -10

# List loaded kernel modules
$ lsmod

# List kernel modules directory
$ ls /lib/modules/$(uname -r)/
```

---

## 13. 💾 `/dev` — Device Files

### 🇮🇩 Bahasa Indonesia
`/dev` berisi **file perangkat (device files)** — representasi virtual dari semua hardware yang terhubung ke sistem. Di Linux, semua hardware diperlakukan sebagai file, termasuk disk, terminal, dan perangkat khusus seperti `/dev/null`.

### 🇬🇧 English
`/dev` contains **device files** — virtual representations of all hardware connected to the system. In Linux, all hardware is treated as a file, including disks, terminals, and special devices like `/dev/null`.

### 🇯🇵 日本語
`/dev` にはシステムに接続されたすべてのハードウェアの仮想表現である**デバイスファイル**が含まれています。Linuxでは、ディスク、端末、`/dev/null`などの特殊デバイスを含むすべてのハードウェアがファイルとして扱われます。

```bash
# List block devices (hard drives, partitions)
$ lsblk
$ ls /dev/sd*
/dev/sda   /dev/sda1   /dev/sda2

# Special devices
$ ls /dev/null       # discards everything written to it
$ ls /dev/zero       # produces infinite null bytes
$ ls /dev/random     # generates random bytes (blocking)
$ ls /dev/urandom    # generates random bytes (non-blocking)
$ ls /dev/tty        # current terminal

# Useful pentesting tricks
$ cat /dev/null        # empty output
$ dd if=/dev/zero of=file.bin bs=1M count=10  # create 10MB zero file
$ cat /dev/urandom | base64 | head -c 32      # generate random string
```

### 🔑 Important Device Files

| Device | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `/dev/sda` | Hard disk pertama | First hard disk | 最初のハードディスク |
| `/dev/sda1` | Partisi pertama sda | First partition of sda | sdaの最初のパーティション |
| `/dev/null` | Buang semua output | Discard all output | すべての出力を破棄 |
| `/dev/zero` | Output null bytes tak terbatas | Infinite null bytes output | 無限のヌルバイト出力 |
| `/dev/random` | Generator angka acak | Random number generator | 乱数生成器 |
| `/dev/tty` | Terminal saat ini | Current terminal | 現在の端末 |

---

## 14. 🔬 `/proc` — Process & Kernel Information

### 🇮🇩 Bahasa Indonesia
`/proc` adalah **virtual filesystem** — bukan direktori nyata di disk, melainkan interface ke **informasi kernel dan proses yang sedang berjalan**. Setiap proses memiliki subdirektori bernama PID-nya. Sangat berguna untuk forensik dan debugging.

### 🇬🇧 English
`/proc` is a **virtual filesystem** — not a real directory on disk, but an interface to **kernel and running process information**. Each process has a subdirectory named after its PID. Extremely useful for forensics and debugging.

### 🇯🇵 日本語
`/proc` は**仮想ファイルシステム** — ディスク上の実際のディレクトリではなく、**カーネルと実行中のプロセス情報**へのインターフェースです。各プロセスにはPIDにちなんだサブディレクトリがあります。フォレンジクスとデバッグに非常に役立ちます。

```bash
# View CPU information
$ cat /proc/cpuinfo

# View memory information
$ cat /proc/meminfo

# View kernel version
$ cat /proc/version
Linux version 5.15.0-91-generic

# View all running processes
$ ls /proc/ | grep -E '^[0-9]+'

# Inspect a specific process (PID 1 = systemd)
$ cat /proc/1/cmdline
$ cat /proc/1/status
$ ls /proc/1/fd/             # open file descriptors

# View active network connections
$ cat /proc/net/tcp

# View mounted filesystems
$ cat /proc/mounts

# System uptime
$ cat /proc/uptime
```

---

## 15. 🖥️ `/sys` — Hardware & Kernel Interface

### 🇮🇩 Bahasa Indonesia
`/sys` adalah **virtual filesystem** lain yang menyediakan interface ke **struktur kernel dan hardware**. Lebih terstruktur dari `/proc` dan digunakan untuk melihat dan mengubah pengaturan hardware secara real-time.

### 🇬🇧 English
`/sys` is another **virtual filesystem** providing an interface to **kernel structure and hardware**. More structured than `/proc` and used to view and modify hardware settings in real-time.

### 🇯🇵 日本語
`/sys` は**カーネル構造とハードウェア**へのインターフェースを提供するもう一つの**仮想ファイルシステム**です。`/proc`よりも構造化されており、ハードウェア設定をリアルタイムで表示・変更するために使います。

```bash
# View block devices
$ ls /sys/block/

# View network interfaces
$ ls /sys/class/net/
eth0  lo  wlan0

# View CPU details
$ ls /sys/devices/system/cpu/
```

---

## 16. 💿 `/mnt` & `/media` — Mount Points

### 🇮🇩 Bahasa Indonesia
- **`/mnt`** — digunakan untuk **mount sementara secara manual** oleh administrator (misalnya: USB drive, NFS share, ISO image)
- **`/media`** — digunakan untuk **auto-mount** media yang dapat dilepas (USB, CD-ROM) oleh sistem secara otomatis

### 🇬🇧 English
- **`/mnt`** — used for **temporary manual mounts** by administrators (e.g. USB drives, NFS shares, ISO images)
- **`/media`** — used for **auto-mounting** removable media (USB, CD-ROM) automatically by the system

### 🇯🇵 日本語
- **`/mnt`** — 管理者による**手動での一時マウント**に使用（例：USBドライブ、NFSシェア、ISOイメージ）
- **`/media`** — システムによるリムーバブルメディア（USB、CD-ROM）の**自動マウント**に使用

```bash
# Manually mount a USB drive
$ sudo mount /dev/sdb1 /mnt/usb

# Unmount
$ sudo umount /mnt/usb

# Check mounted filesystems
$ mount | grep /mnt
$ df -h

# Auto-mounted USB usually appears here
$ ls /media/username/
```

---

## 17. 📦 `/opt` — Optional Software

### 🇮🇩 Bahasa Indonesia
`/opt` digunakan untuk **software pihak ketiga atau opsional** yang tidak dikelola oleh package manager distro. Software yang diinstal di sini biasanya self-contained dalam subdirektorinya sendiri.

### 🇬🇧 English
`/opt` is used for **third-party or optional software** not managed by the distro's package manager. Software installed here is usually self-contained in its own subdirectory.

### 🇯🇵 日本語
`/opt` はディストリビューションのパッケージマネージャーで管理されない**サードパーティまたはオプションのソフトウェア**に使われます。ここにインストールされたソフトウェアは通常、自身のサブディレクトリ内で自己完結しています。

```bash
# Common contents of /opt
$ ls /opt
google/   lampp/   BurpSuite/   vmware/

# Example: Burp Suite installed in /opt
$ ls /opt/BurpSuite/
BurpSuitePro  jre/  burpsuite_pro.jar
```

---

## 18. 🚀 `/boot` — Boot Files

### 🇮🇩 Bahasa Indonesia
`/boot` berisi **semua file yang diperlukan untuk booting sistem** — termasuk kernel Linux, initial RAM disk (initrd), dan konfigurasi bootloader GRUB. Jangan mengubah isi direktori ini kecuali kamu tahu apa yang kamu lakukan.

### 🇬🇧 English
`/boot` contains **all files required to boot the system** — including the Linux kernel, initial RAM disk (initrd), and GRUB bootloader configuration. Do not modify the contents of this directory unless you know what you are doing.

### 🇯🇵 日本語
`/boot` には**システムの起動に必要なすべてのファイル** — Linuxカーネル、初期RAMディスク（initrd）、GRUBブートローダー設定が含まれています。何をしているかわかる場合以外、このディレクトリの内容を変更しないでください。

```bash
$ ls /boot

grub/           # GRUB bootloader config directory
vmlinuz-5.15.0  # Compressed Linux kernel
initrd.img      # Initial RAM disk image
config-5.15.0   # Kernel build configuration
System.map      # Kernel symbol table

# View GRUB configuration
$ cat /boot/grub/grub.cfg

# View current kernel version
$ uname -r
5.15.0-91-generic
```

---

## 19. 🌐 `/srv` — Server Service Data

### 🇮🇩 Bahasa Indonesia
`/srv` berisi **data yang disajikan oleh layanan server** yang berjalan di sistem, seperti file web, FTP, atau data repositori. Penggunaannya bervariasi antar distribusi.

### 🇬🇧 English
`/srv` contains **data served by server services** running on the system, such as web files, FTP, or repository data. Its usage varies across distributions.

### 🇯🇵 日本語
`/srv` にはシステムで実行されているサーバーサービスが提供するデータ（Webファイル、FTP、リポジトリデータなど）が含まれています。使用方法はディストリビューションによって異なります。

```bash
$ ls /srv
http/   ftp/   git/

# Example: web files served from /srv
$ ls /srv/http/
index.html  assets/  uploads/
```

---

## 20. 🔐 Security Note — Key Directories for Pentesting

### 🇮🇩 Bahasa Indonesia
Berikut adalah direktori-direktori **paling penting dari perspektif penetration testing**, baik untuk rekognisi, privilege escalation, maupun forensik:

### 🇬🇧 English
Here are the **most important directories from a penetration testing perspective**, whether for reconnaissance, privilege escalation, or forensics:

### 🇯🇵 日本語
偵察、権限昇格、フォレンジクスのいずれの観点からも、**ペンテストの観点から最も重要なディレクトリ**を以下に示します：

```bash
# ── CREDENTIAL HUNTING ───────────────────────────────────────
/etc/passwd             # usernames & shells
/etc/shadow             # password hashes (root only)
/etc/sudoers            # sudo privileges
/home/*/.bash_history   # command history (may contain passwords)
/home/*/.ssh/id_rsa     # SSH private keys
/root/.bash_history     # root's command history
/root/.ssh/id_rsa       # root's SSH private key

# ── CONFIG FILES WITH CREDENTIALS ───────────────────────────
/var/www/html/          # web app source code (DB passwords!)
/etc/mysql/             # MySQL config
/etc/php*/              # PHP config (db connections)
/home/*/.gitconfig      # Git credentials

# ── LOG ANALYSIS ─────────────────────────────────────────────
/var/log/auth.log       # login attempts & sudo usage
/var/log/syslog         # general system events
/var/log/apache2/       # web server access/error logs
/var/log/nginx/         # nginx logs

# ── WRITABLE DIRECTORIES (privilege escalation) ──────────────
/tmp/                   # world-writable
/var/tmp/               # world-writable, persists across reboots
/dev/shm/               # shared memory, world-writable

# ── PERSISTENCE LOCATIONS ────────────────────────────────────
/etc/cron*/             # cron jobs
/var/spool/cron/        # per-user cron jobs
/etc/systemd/system/    # systemd services
/etc/rc.local           # startup script
/home/*/.bashrc         # user shell startup
```

### 📊 Directory Security Priority Table

| Directory | 🔴 Risk Level | 🇮🇩 Alasan | 🇬🇧 Reason | 🇯🇵 理由 |
|-----------|--------------|-----------|-----------|---------|
| `/etc/shadow` | 🔴 Critical | Hash password | Password hashes | パスワードハッシュ |
| `/etc/sudoers` | 🔴 Critical | Izin root | Root permissions | root権限 |
| `/root/` | 🔴 Critical | Data root user | Root user data | rootユーザーデータ |
| `/home/*/.ssh/` | 🔴 High | SSH private keys | SSH private keys | SSH秘密鍵 |
| `/var/log/` | 🟠 High | Rekam aktivitas | Activity records | 活動記録 |
| `/tmp/` | 🟠 High | World-writable | World-writable | 全ユーザー書き込み可 |
| `/etc/passwd` | 🟡 Medium | Username info | Username info | ユーザー名情報 |
| `/var/www/` | 🟡 Medium | Kode web app | Web app code | Webアプリコード |
| `/etc/cron*` | 🟡 Medium | Task terjadwal | Scheduled tasks | スケジュールタスク |

---

## 📊 Complete Directory Reference Table

| Directory | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Type |
|-----------|-----------|-------------|---------|------|
| `/` | Direktori akar | Root directory | ルートディレクトリ | Real |
| `/bin` | Binary esensial pengguna | Essential user binaries | 必須ユーザーバイナリ | Real |
| `/sbin` | Binary sistem admin | System admin binaries | システム管理バイナリ | Real |
| `/etc` | Konfigurasi sistem | System configuration | システム設定 | Real |
| `/home` | Home direktori user | User home directories | ユーザーホーム | Real |
| `/root` | Home untuk root | Root user's home | rootのホーム | Real |
| `/var` | Data variabel & log | Variable data & logs | 可変データとログ | Real |
| `/tmp` | File sementara | Temporary files | 一時ファイル | Real |
| `/usr` | Resource Unix bersama | Unix shared resources | Unix共有リソース | Real |
| `/lib` | Shared libraries | Shared libraries | 共有ライブラリ | Real |
| `/dev` | File perangkat | Device files | デバイスファイル | Virtual |
| `/proc` | Info proses & kernel | Process & kernel info | プロセス・カーネル情報 | Virtual |
| `/sys` | Info hardware & kernel | Hardware & kernel info | ハードウェア・カーネル情報 | Virtual |
| `/mnt` | Mount point manual | Manual mount point | 手動マウントポイント | Real |
| `/media` | Mount point auto | Auto mount point | 自動マウントポイント | Real |
| `/opt` | Software opsional | Optional software | オプションソフト | Real |
| `/boot` | File booting | Boot files | ブートファイル | Real |
| `/srv` | Data layanan server | Server service data | サービスデータ | Real |
| `/run` | Data runtime | Runtime data | ランタイムデータ | Virtual |

---

## 🔗 Practical Workflow Example

```bash
# ── SCENARIO: Post-exploitation filesystem reconnaissance ────

# 1. Identify the OS and kernel
$ uname -a
$ cat /etc/os-release

# 2. List all users on the system
$ cat /etc/passwd | grep "/bin/bash"

# 3. Hunt for password hashes
$ sudo cat /etc/shadow

# 4. Check sudo privileges
$ sudo -l
$ cat /etc/sudoers

# 5. Find SSH keys
$ find /home -name "id_rsa" 2>/dev/null
$ find /root -name "id_rsa" 2>/dev/null

# 6. Read command histories
$ cat /home/*/.bash_history 2>/dev/null
$ cat /root/.bash_history 2>/dev/null

# 7. Check web files for credentials
$ find /var/www -name "*.php" -exec grep -l "password" {} \;
$ find /var/www -name "config.php" 2>/dev/null

# 8. Check for writable directories
$ find / -writable -type d 2>/dev/null | grep -v proc

# 9. Look for scheduled tasks (persistence)
$ crontab -l
$ cat /etc/crontab
$ ls /etc/cron.d/
$ systemctl list-timers

# 10. Check running services
$ ps -aux
$ netstat -tulpn 2>/dev/null || ss -tulpn

# 11. Look for SUID binaries (privilege escalation)
$ find / -perm -4000 -type f 2>/dev/null

# 12. Check kernel version for exploits
$ uname -r
$ cat /proc/version
```

---

## 🧠 Quick Reference Cheatsheet

```bash
# ── NAVIGATION ───────────────────────────────────────────────
cd /                             # go to root
ls -la /                         # list root contents
tree / -L 2                      # show 2-level tree (install: apt install tree)

# ── KEY FILES ────────────────────────────────────────────────
cat /etc/passwd                  # user accounts
sudo cat /etc/shadow             # password hashes
cat /etc/group                   # groups
cat /etc/hosts                   # hostname resolution
cat /etc/sudoers                 # sudo rules
cat /etc/ssh/sshd_config         # SSH config
cat /etc/crontab                 # system cron jobs
cat /proc/version                # kernel version
cat /proc/cpuinfo                # CPU info
cat /proc/meminfo                # memory info

# ── LOG FILES ────────────────────────────────────────────────
tail -f /var/log/syslog          # live system log
tail -f /var/log/auth.log        # live auth log
grep "Failed" /var/log/auth.log  # failed logins
grep "Accept" /var/log/auth.log  # successful logins

# ── FIND COMMANDS ────────────────────────────────────────────
find / -name "*.conf" 2>/dev/null           # find config files
find / -perm -4000 2>/dev/null              # find SUID files
find / -writable -type d 2>/dev/null        # find writable dirs
find /home -name "id_rsa" 2>/dev/null       # find SSH keys
find / -name "*.log" 2>/dev/null            # find log files
find / -name "config.php" 2>/dev/null       # find web configs

# ── DISK & MOUNT ─────────────────────────────────────────────
df -h                            # disk usage (human readable)
lsblk                            # list block devices
mount                            # show mounted filesystems
sudo mount /dev/sdb1 /mnt/usb   # mount a device
sudo umount /mnt/usb             # unmount a device
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - [Linux Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
> - `man hier` — Manual page for the Linux filesystem hierarchy
> - [GTFOBins](https://gtfobins.github.io) — SUID/SUDO binary exploitation

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.