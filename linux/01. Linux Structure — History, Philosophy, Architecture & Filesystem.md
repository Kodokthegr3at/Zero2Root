# 🐧 Linux Structure — History, Philosophy, Architecture & Filesystem

> **LearnCybersecurity** | Linux Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | What is Linux? | Apa itu Linux? | What is Linux? | Linux とは？ |
| 2 | History | Sejarah Linux | History of Linux | Linux の歴史 |
| 3 | Philosophy | Filosofi Linux | Linux Philosophy | Linux の哲学 |
| 4 | Components | Komponen Linux | Linux Components | Linux のコンポーネント |
| 5 | Architecture | Arsitektur Linux | Linux Architecture | Linux のアーキテクチャ |
| 6 | Filesystem Hierarchy | Hierarki filesystem | Filesystem Hierarchy | ファイルシステム階層 |

---

## 1. 🖥️ What is Linux?

### 🇮🇩 Bahasa Indonesia
Linux adalah **sistem operasi** seperti Windows, macOS, iOS, atau Android. Sistem operasi (OS) adalah perangkat lunak yang mengelola semua sumber daya hardware komputer dan memfasilitasi komunikasi antara aplikasi dan hardware.

Yang membuat Linux unik adalah ia hadir dalam banyak **distribusi (distro)** — versi Linux yang disesuaikan untuk berbagai kebutuhan. Linux sangat penting di dunia cybersecurity karena:
- **Gratis dan open-source** — source code bisa dimodifikasi siapa saja
- **Lebih aman** dari OS lain, jarang terkena malware
- **Sangat stabil** dan berperforma tinggi
- Digunakan di server, mainframe, router, smart TV, konsol game, hingga Android

### 🇬🇧 English
Linux is an **operating system** just like Windows, macOS, iOS, or Android. An OS is software that manages all hardware resources of a computer and facilitates communication between applications and hardware.

What makes Linux unique is it comes in many **distributions (distros)** — versions of Linux tailored to various needs. Linux is critical in cybersecurity because:
- **Free and open-source** — source code can be modified by anyone
- **More secure** than other OSes, rarely affected by malware
- **Very stable** and high-performing
- Used in servers, mainframes, routers, smart TVs, game consoles, and Android

### 🇯🇵 日本語
Linux は Windows、macOS、iOS、Android と同様の**オペレーティングシステム**です。OS はコンピュータのすべてのハードウェアリソースを管理し、アプリケーションとハードウェア間の通信を担うソフトウェアです。

Linux の特徴は多くの**ディストリビューション（ディストロ）**として提供される点です。サイバーセキュリティにおいて重要な理由：
- **無料かつオープンソース** — 誰でもソースコードを修正できる
- 他の OS より**安全**で、マルウェアの影響を受けにくい
- **非常に安定**していて高性能
- サーバー、メインフレーム、ルーター、スマートTV、ゲーム機、Android まで幅広く使われる

---

### 🌍 Popular Linux Distributions

| Distro | Focus | Best For |
|--------|-------|----------|
| **Ubuntu** | User-friendly | Beginners, desktops |
| **Debian** | Stability | Servers, development |
| **Parrot OS** | Security & privacy | Pentesting, CTF |
| **Kali Linux** | Offensive security | Penetration testing |
| **Fedora** | Cutting-edge | Developers |
| **Arch Linux** | Customization | Advanced users |
| **CentOS / RHEL** | Enterprise | Production servers |
| **Manjaro** | Ease of use | Desktop users |

> 💡 **Note:** In HackTheBox Academy, we use **Parrot OS** (Pwnbox) — a Debian-based distro focused on security, privacy, and development.

---

## 2. 📜 History of Linux

### 🇮🇩 Bahasa Indonesia
Linux tidak muncul tiba-tiba — ada serangkaian peristiwa panjang yang mendahuluinya. Pemahaman sejarah ini penting karena banyak konsep Linux berakar dari filosofi Unix yang jauh lebih tua.

### 🇬🇧 English
Linux didn't appear out of nowhere — there was a long chain of events that preceded it. Understanding this history is important because many Linux concepts are rooted in the much older Unix philosophy.

### 🇯🇵 日本語
Linux は突然現れたわけではなく、長い出来事の連鎖がありました。Linux の多くの概念はより古い Unix の哲学に根ざしているため、この歴史を理解することは重要です。

---

### 🕰️ Timeline

```
1970  ── Unix OS released by Ken Thompson & Dennis Ritchie (AT&T)
  │
1977  ── BSD (Berkeley Software Distribution) released
  │        └── AT&T lawsuit limits BSD development
  │
1983  ── Richard Stallman starts the GNU Project
  │        └── Goal: create a free Unix-like OS
  │        └── GNU General Public License (GPL) created
  │
1991  ── Linus Torvalds (Finnish student) starts Linux kernel
  │        └── Goal: new, free OS kernel
  │        └── Written in C, originally prohibited commercial use
  │
Now   ── Linux kernel: 23+ million lines of code
           Licensed under GNU GPL v2
           600+ distributions available
           Powers most of the internet's servers
           Android (Linux-based) = most installed OS worldwide
```

| Year | Event |
|------|-------|
| **1970** | Unix released by Ken Thompson & Dennis Ritchie at AT&T |
| **1977** | BSD released — limited by AT&T lawsuit |
| **1983** | GNU Project started by Richard Stallman |
| **1989** | GNU General Public License (GPL) created |
| **1991** | Linux kernel created by Linus Torvalds (age 21) |
| **Present** | 23+ million lines of code, 600+ distros, most installed OS globally |

---

## 3. 💡 Linux Philosophy

### 🇮🇩 Bahasa Indonesia
Filosofi Linux berpusat pada **kesederhanaan, modularitas, dan keterbukaan**. Linux mendukung pembuatan program kecil yang melakukan **satu tugas dengan sangat baik**, lalu menggabungkannya untuk menyelesaikan operasi yang kompleks.

### 🇬🇧 English
The Linux philosophy centers on **simplicity, modularity, and openness**. Linux advocates for building small programs that do **one task very well**, then combining them to accomplish complex operations.

### 🇯🇵 日本語
Linux の哲学は**シンプルさ、モジュール性、オープン性**を中心としています。Linux は**一つのことを非常にうまくこなす**小さなプログラムを構築し、それらを組み合わせて複雑な操作を実行することを推奨します。

---

### 5 Core Principles

| # | Principle | 🇮🇩 Penjelasan | 🇬🇧 Description | 🇯🇵 説明 |
|---|-----------|--------------|----------------|---------|
| 1 | **Everything is a file** | Semua resource sistem (hardware, proses, koneksi jaringan) direpresentasikan sebagai file — bisa dibaca & ditulis dengan tools yang sama | All system resources (hardware devices, processes, network connections) are represented as files — readable & writable with the same standard tools | すべてのシステムリソース（ハードウェア、プロセス、ネットワーク接続）がファイルとして表現され、同じ標準ツールで読み書きできる |
| 2 | **Small, single-purpose programs** | Linux menyediakan banyak tools kecil yang masing-masing melakukan satu hal dengan sangat baik | Linux provides many small tools that each do one thing very well | Linux は各自が一つのことを非常にうまく行う多くの小さなツールを提供する |
| 3 | **Ability to chain programs** | Program-program kecil bisa dihubungkan (pipe) untuk menyelesaikan tugas besar dan kompleks | Small programs can be chained together (pipes) to accomplish large and complex tasks | 小さなプログラムをパイプで繋いで大きく複雑なタスクを実行できる |
| 4 | **Avoid captive user interfaces** | Linux dirancang untuk bekerja dengan **shell/terminal**, memberi pengguna kendali penuh atas OS | Linux is designed to work primarily with the **shell/terminal**, giving the user full control over the OS | Linux は主に**シェル/ターミナル**で動作するよう設計されており、ユーザーに OS の完全な制御を与える |
| 5 | **Configuration in text files** | Data konfigurasi disimpan dalam **file teks** (contoh: `/etc/passwd` menyimpan semua user terdaftar) | Configuration data is stored in **text files** (e.g., `/etc/passwd` stores all registered users) | 設定データは**テキストファイル**に保存される（例：`/etc/passwd` はすべての登録ユーザーを保存） |

> 💡 These principles are why Linux is so powerful for cybersecurity — everything is transparent, scriptable, and composable.

---

## 4. ⚙️ Linux Components

### 🇮🇩 Bahasa Indonesia
Linux terdiri dari beberapa komponen utama yang bekerja bersama untuk mengoperasikan sistem.

### 🇬🇧 English
Linux consists of several key components that work together to operate the system.

### 🇯🇵 日本語
Linux はシステムを動作させるために連携して動く複数の主要コンポーネントで構成されています。

---

| Component | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|-----------|--------------|----------------|---------|
| **Bootloader** | Kode yang memandu proses booting untuk memulai OS. Parrot Linux menggunakan **GRUB Bootloader** | Code that guides the booting process to start the OS. Parrot Linux uses the **GRUB Bootloader** | OSを起動するブートプロセスを導くコード。Parrot Linux は **GRUB Bootloader** を使用 |
| **OS Kernel** | Komponen utama OS yang mengelola resource I/O device di level hardware | The main OS component that manages I/O device resources at the hardware level | I/O デバイスリソースをハードウェアレベルで管理する OS のメインコンポーネント |
| **Daemons** | Layanan background yang memastikan fungsi seperti scheduling, printing, dan multimedia berjalan dengan benar | Background services that ensure functions like scheduling, printing, and multimedia work correctly | スケジューリング、印刷、マルチメディアなどの機能が正常に動作することを保証するバックグラウンドサービス |
| **OS Shell** | Interface antara OS dan user — tempat user memberikan perintah ke OS. Shell populer: **Bash, Zsh, Fish, Ksh** | Interface between OS and user — where users give commands to the OS. Popular shells: **Bash, Zsh, Fish, Ksh** | OS とユーザー間のインターフェース。人気のシェル：**Bash、Zsh、Fish、Ksh** |
| **Graphics Server** | Subsistem grafis **"X" / X-server** yang memungkinkan program grafis berjalan secara lokal atau remote | Graphical subsystem **"X" / X-server** that allows graphical programs to run locally or remotely | グラフィカルプログラムをローカルまたはリモートで実行可能にする **X / X サーバー** |
| **Window Manager** | GUI desktop environment seperti **GNOME, KDE, MATE, Unity, Cinnamon** — termasuk file browser & web browser | GUI desktop environments like **GNOME, KDE, MATE, Unity, Cinnamon** — includes file & web browsers | **GNOME、KDE、MATE、Unity、Cinnamon** などの GUI デスクトップ環境 |
| **Utilities** | Aplikasi yang menjalankan fungsi tertentu untuk user atau program lain | Applications that perform specific functions for the user or other programs | ユーザーや他のプログラムのために特定の機能を実行するアプリケーション |

---

## 5. 🏗️ Linux Architecture

### 🇮🇩 Bahasa Indonesia
Sistem operasi Linux dapat dibagi menjadi **4 lapisan (layer)** yang saling berkomunikasi dari bawah ke atas.

### 🇬🇧 English
The Linux OS can be broken down into **4 layers** that communicate with each other from bottom to top.

### 🇯🇵 日本語
Linux OS は下から上へ互いに通信する**4つのレイヤー**に分けられます。

---

```
┌─────────────────────────────────────────────────────┐
│                  SYSTEM UTILITY                      │
│   Makes all OS functionality available to the user   │
│   (commands, programs, libraries, man pages)         │
├─────────────────────────────────────────────────────┤
│                     SHELL                            │
│   Command-line interface (CLI) — user enters         │
│   commands to interact with the kernel               │
│   Bash / Zsh / Fish / Ksh                            │
├─────────────────────────────────────────────────────┤
│                     KERNEL                           │
│   Core of Linux — virtualizes and controls hardware  │
│   CPU, RAM, I/O, process management                  │
│   Gives each process its own virtual resources       │
├─────────────────────────────────────────────────────┤
│                    HARDWARE                          │
│   Physical components: CPU, RAM, HDD/SSD,            │
│   Network card, GPU, peripherals                     │
└─────────────────────────────────────────────────────┘
          ↕ each layer communicates with adjacent layers
```

| Layer | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|-------|--------------|----------------|---------|
| **Hardware** | Perangkat fisik: RAM, hard drive, CPU, dll | Physical devices: RAM, hard drive, CPU, etc. | RAM、HDD、CPU などの物理デバイス |
| **Kernel** | Inti Linux — memvirtualisasi & mengontrol resource hardware, memberi setiap proses resource virtual sendiri | Core of Linux — virtualizes & controls hardware resources, gives each process its own virtual resources | Linux のコア — ハードウェアリソースを仮想化・制御し、各プロセスに独自の仮想リソースを提供 |
| **Shell** | CLI (Command-Line Interface) — user memasukkan perintah untuk menjalankan fungsi kernel | CLI (Command-Line Interface) — users enter commands to execute kernel functions | ユーザーがカーネルの機能を実行するコマンドを入力する CLI |
| **System Utility** | Menyediakan semua fungsionalitas OS kepada user | Makes all OS functionality available to the user | すべての OS 機能をユーザーが利用できるようにする |

---

## 6. 🗂️ Filesystem Hierarchy Standard (FHS)

### 🇮🇩 Bahasa Indonesia
Linux menggunakan struktur direktori berbentuk **pohon (tree)** yang didokumentasikan dalam **Filesystem Hierarchy Standard (FHS)**. Semua direktori dimulai dari root `/` — seperti batang pohon yang bercabang ke bawah.

### 🇬🇧 English
Linux uses a **tree-like directory structure** documented in the **Filesystem Hierarchy Standard (FHS)**. All directories start from the root `/` — like the trunk of a tree branching downward.

### 🇯🇵 日本語
Linux は **Filesystem Hierarchy Standard（FHS）** に記録された**ツリー状のディレクトリ構造**を使用します。すべてのディレクトリはルート `/` から始まります — 木の幹から下に向かって枝分かれするイメージです。

---

### Directory Tree

```
/ (root)
├── bin/      ← essential command binaries
├── boot/     ← bootloader, kernel
├── dev/      ← device files (hardware access)
├── etc/      ← system config files
├── home/     ← user home directories
│   └── cry0l1t3/
├── lib/      ← shared libraries for boot
├── media/    ← removable media (USB, CD)
├── mnt/      ← temporary mount points
├── opt/      ← optional / third-party software
├── proc/     ← virtual filesystem (process info)
├── root/     ← root user's home directory
├── run/      ← runtime data (PIDs, sockets)
├── sbin/     ← system admin binaries
├── sys/      ← virtual filesystem (kernel/device info)
├── tmp/      ← temporary files (cleared on boot)
├── usr/      ← user programs, libraries, man pages
└── var/      ← variable data (logs, mail, web files)
```

---

### 📋 Directory Reference Table

| Path | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|------|--------------|----------------|---------|
| `/` | Direktori root — berisi semua file yang dibutuhkan untuk booting | Top-level root directory — contains all files needed to boot the OS | ルートディレクトリ — OS の起動に必要なすべてのファイルを含む |
| `/bin` | Binary perintah esensial (ls, cp, mv, cat, dll) | Essential command binaries (ls, cp, mv, cat, etc.) | 基本コマンドのバイナリ（ls、cp、mv、cat など） |
| `/boot` | Bootloader, kernel executable, file booting | Static bootloader, kernel executable, boot files | 静的ブートローダー、カーネル実行ファイル、起動ファイル |
| `/dev` | File device untuk akses hardware (disk, USB, dll) | Device files for hardware access (disk, USB, etc.) | ハードウェアアクセス用デバイスファイル |
| `/etc` | File konfigurasi sistem lokal & aplikasi | Local system & application configuration files | ローカルシステムとアプリの設定ファイル |
| `/home` | Direktori home untuk setiap user | Home directory for each user on the system | システムの各ユーザーのホームディレクトリ |
| `/lib` | Shared library untuk sistem boot | Shared library files required for system boot | システム起動に必要な共有ライブラリ |
| `/media` | Media removable eksternal (USB, CD/DVD) | External removable media (USB drives, CDs) | 外部リムーバブルメディア（USB、CD/DVD） |
| `/mnt` | Mount point sementara untuk filesystem | Temporary mount point for regular filesystems | 通常のファイルシステムの一時マウントポイント |
| `/opt` | Software opsional / third-party tools | Optional / third-party software | オプションのサードパーティソフトウェア |
| `/root` | Direktori home untuk user root | Home directory for the root user | root ユーザーのホームディレクトリ |
| `/sbin` | Binary untuk administrasi sistem | System administration executables | システム管理用実行ファイル |
| `/tmp` | File sementara — **dihapus saat reboot** | Temporary files — **cleared on reboot** | 一時ファイル — **再起動時に消去される** |
| `/usr` | Program user, library, man pages | User programs, libraries, man pages | ユーザープログラム、ライブラリ、マニュアルページ |
| `/var` | Data variabel: log, email, web files, cron | Variable data: logs, emails, web files, cron | ログ、メール、Webファイル、cronなどの可変データ |

---

### 🔐 Pentesting-Relevant Directories

| Path | 🇮🇩 Relevansi Pentesting | 🇬🇧 Pentesting Relevance | 🇯🇵 ペンテスト関連性 |
|------|-------------------------|-------------------------|-------------------|
| `/etc/passwd` | Daftar semua user di sistem | List of all users on the system | システムの全ユーザーリスト |
| `/etc/shadow` | Hash password user (butuh root) | User password hashes (requires root) | ユーザーパスワードハッシュ（root必要） |
| `/etc/crontab` | Scheduled jobs — bisa ada privilege escalation | Scheduled jobs — potential privilege escalation | スケジュールジョブ — 権限昇格の可能性 |
| `/tmp` | Writable oleh semua user — sering digunakan untuk staging exploit | Writable by all users — often used for exploit staging | 全ユーザーが書き込み可能 — エクスプロイトのステージングに使われる |
| `/var/log` | Log sistem — jejak aktivitas user & serangan | System logs — traces of user activity & attacks | システムログ — ユーザー活動と攻撃の痕跡 |
| `/home` | Kemungkinan berisi SSH keys, credential, config | May contain SSH keys, credentials, config files | SSH キー、認証情報、設定ファイルが含まれる可能性 |
| `/root` | Home directory root — target privilege escalation | Root user's home — target for privilege escalation | root のホームディレクトリ — 権限昇格のターゲット |
| `/dev` | Device files — `/dev/null`, `/dev/shm` (RAM-based temp storage) | Device files — `/dev/null`, `/dev/shm` (RAM temp storage) | デバイスファイル — `/dev/null`、`/dev/shm`（RAM一時ストレージ） |

---

## 🧠 Quick Reference Cheatsheet

```bash
# Check Linux version and distro
uname -a                    # kernel version
cat /etc/os-release         # distro information
lsb_release -a              # distro details

# Explore filesystem hierarchy
ls /                        # list root directory
ls /etc/                    # system config files
ls /home/                   # user home directories
ls /var/log/                # system log files
cat /etc/passwd             # list all users
cat /etc/os-release         # current distro info

# Check shell in use
echo $SHELL                 # current shell path
cat /etc/shells             # all available shells
```

---

> 📚 **References:**
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - [Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
> - [The Linux Kernel Archives](https://www.kernel.org)
> - `man hier` — filesystem hierarchy manual page

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/kodoktheGr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.