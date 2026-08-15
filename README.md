# 🛡️ LearnCybersecurity

> **Comprehensive Trilingual Cybersecurity Knowledge Base & Offensive Security Roadmap**  
> 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語  
> 👤 Author: [kodoktheGr3at](https://github.com/Kodokthegr3at) | 📅 Last Updated: 2026  

---

## 📖 About This Repository / Tentang Repositori / このリポジトリについて

### 🇮🇩 Bahasa Indonesia
Repositori ini adalah pusat dokumentasi teknis dan catatan belajar mandiri komprehensif di bidang **Cybersecurity**, mencakup **Offensive Security, Linux Internals, Network Protocol Analysis, Web Application Penetration Testing, Cryptography, Reverse Engineering, Malware Analysis, Binary Exploitation, Security Programming, Social Engineering, OSINT, Mobile Security (Android), dan Hardware/IoT Security**. 

Setiap catatan ditulis dengan standar **tiga bahasa (Trilingual: ID, EN, JP)**, dilengkapi tabel perbandingan mendalam, diagram alur, perintah praktis CLI, catatan keamanan (*Security Notes*, *Threat Vectors* & *PrivEsc*), cheatsheet siap pakai, serta referensi buku teknis standar industri dari direktori lokal `~/Documents/Books/`.

### 🇬🇧 English
This repository is an open, comprehensive technical knowledge base documenting a structured journey into **Cybersecurity**, spanning **Offensive Security, Linux Internals, Network Protocol Analysis, Web Application Penetration Testing, Cryptography, Reverse Engineering, Malware Analysis, Binary Exploitation, Security Programming, Social Engineering, OSINT, Mobile Security (Android), and Hardware/IoT Security**.

Every document follows a strict **trilingual format (Bahasa Indonesia, English, and 日本語)**, featuring structured comparison tables, command workflows, dedicated 🔐 **Security Notes**, actionable cheatsheets, and direct citations to definitive cybersecurity literature located in `~/Documents/Books/`.

### 🇯🇵 日本語
このリポジトリは、**サイバーセキュリティ（オフェンシブセキュリティ、Linux内部構造、ネットワーク分析、Webペネトレーションテスト、暗号技術、リバースエンジニアリング、マルウェア解析、バイナリ解析/脆弱性攻撃、セキュリティプログラミング、ソーシャルエンジニアリング、OSINT、モバイルセキュリティ、およびハードウェア/IoTセキュリティ）** の網羅的な技術ナレッジベースです。

すべてのドキュメントは **3言語対応（インドネシア語・英語・日本語）** で記述され、詳細な比較表、実践的なコマンド例、セキュリティノート（権限昇格・攻撃手法）、チートシート、および専門書籍（`~/Documents/Books/`）の参考文献を含んでいます。

---

## 🗺️ Repository Map & Curriculum / Daftar Modul / モジュール一覧

```
LearnCybersecurity/
├── 📁 basics/                    # Computing fundamentals, Git, OS filesystems & PowerShell
├── 🐧 linux/                     # In-depth Linux administration, shell, security & tools (HTB Mod 18)
├── 🌐 networking/                # OSI model, TCP/IP, DNS, ARP, Subnetting & Wireless 802.11
├── 🕸️ web/                       # HTTP/HTTPS, cURL, SQLi, XSS, CSRF, SSRF, LFI, Uploads & JWT
├── 🔐 cryptography/              # AES, RSA, ECC, Hash Functions, MACs, PKI & TLS 1.3
├── 🎯 ethical-hacking/           # PTES methodology, Nmap scanning, Metasploit & PrivEsc
├── 💥 binary-exploitation/       # Stack buffer overflows, shellcode, ret2win, ROP & mitigations
├── 🦠 malware-analysis/          # Static/Dynamic triage, Sandboxing, Procmon & x86/x64 Assembly
├── 📱 mobile-security/           # Android internals, UID sandbox, Binder IPC, Frida & APK RE
├── 🐍 programming-security/      # Offensive Python sockets/proxies & high-concurrency Go tools
├── 🎭 social-engineering/        # Psychology, Pretexting, Phishing (AiTM) & Physical Infiltration
├── 🔍 osint/                     # Intelligence lifecycle, OPSEC, Sock Puppets & Frameworks
└── 🔌 hardware-iot/              # UART/JTAG/SPI debugging, Binwalk extraction & CAN Bus hacking
```

---

### 1. 📂 Basics & Operating Systems (`basics/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Expression.md](file:///home/kodok/Documents/LearnCybersecurity/basics/Expression.md) | Expression & Syntax | Operasi aritmatika, boolean, regex, dan injeksi ekspresi | Expressions, operators, precedence & injection exploits | 式、演算子、正規表現と式インジェクション脆弱性 |
| [Git — Version Control System.md](file:///home/kodok/Documents/LearnCybersecurity/basics/Git%20%E2%80%94%20Version%20Control%20System.md) | Git & Version Control | Git workflow, branching, commit, dan pencarian credential | Git workflow, branching, commit & Git secret hunting | Gitの基本操作、ブランチ管理、機密情報の漏洩対策 |
| [PowerShell.md](file:///home/kodok/Documents/LearnCybersecurity/basics/PowerShell.md) | Windows PowerShell | Cmdlet, pipeline objek, dan post-exploitation Windows | PowerShell cmdlets, object pipelines & Windows recon | PowerShellコマンドレット、オブジェクトパイプライン |
| [Windows Command Prompt (cmd.exe).md](file:///home/kodok/Documents/LearnCybersecurity/basics/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Windows CMD | Perintah CMD, batch script, dan enumerasi sistem | Legacy CMD utilities, batch scripting & host recon | CMDコマンド、バッチ処理、システム列挙 |
| [Linux File System.md](file:///home/kodok/Documents/LearnCybersecurity/basics/OperatingSystem/Linux%20File%20System.md) | Linux OS Architecture | Hirarki FHS Linux (`/etc`, `/var`, `/proc`, `/sys`) | Linux Filesystem Hierarchy Standard & device nodes | Linuxファイルシステム階層標準と主要ディレクトリ |
| [macOS File System.md](file:///home/kodok/Documents/LearnCybersecurity/basics/OperatingSystem/macOS%20File%20System.md) | macOS OS Architecture | Struktur direktori Darwin/APFS (`/System`, `/Library`) | macOS APFS architecture, domain folders & bundle layout | macOS APFSアーキテクチャとディレクトリ構造 |
| [Windows File System.md](file:///home/kodok/Documents/LearnCybersecurity/basics/OperatingSystem/Windows%20File%20System.md) | Windows OS Architecture | Struktur NTFS, drive letters, System32 & Registry | Windows NTFS structure, system folders & alternate data streams | Windows NTFS構造、システムフォルダとADS |

---

### 2. 🐧 Linux Fundamentals & Security (`linux/`) — HTB Academy Module 18 Standard

| # | File | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|---|:-----|:-------------------|:------------|:----------|
| **01** | [01. Linux Structure...](file:///home/kodok/Documents/LearnCybersecurity/linux/01.%20Linux%20Structure%20%E2%80%94%20History,%20Philosophy,%20Architecture%20&%20Filesystem.md) | Sejarah, filosofi Unix, kernel vs user space | History, Unix philosophy, kernel space & FHS | Linuxの歴史、Unix哲学、カーネル空間とFHS |
| **02** | [02. Linux Distributions...](file:///home/kodok/Documents/LearnCybersecurity/linux/02.%20Linux%20Distributions%20%28Distros%29.md) | Keluarga distro (Debian, RHEL, Arch) & pentest distro | Distro families (Debian, RedHat, Arch) & security distros | ディストリビューション系統とペンテスト用OS |
| **03** | [03. Introduction to Shell.md](file:///home/kodok/Documents/LearnCybersecurity/linux/03.%20Introduction%20to%20Shell.md) | Shell basics, built-ins, dan rbash breakout | Shell fundamentals, built-ins & rbash breakouts | シェルの基本、ビルトインと制限シェル脱出 |
| **04** | [04. Prompt Description...](file:///home/kodok/Documents/LearnCybersecurity/linux/04.%20Prompt%20Description%20&%20PS1%20Customization.md) | Kustomisasi prompt Bash `$PS1` dan format escape | PS1 customization, color codes & terminal security | PS1プロンプトのカスタマイズとエスケープシーケンス |
| **05** | [05. Getting Help...](file:///home/kodok/Documents/LearnCybersecurity/linux/05.%20Getting%20Help%20%E2%80%94%20man,%20--help,%20apropos.md) | Sistem bantuan, `man`, section nomor & GTFOBins pager | Linux documentation, `man` sections & pager escapes | マニュアル参照、manセクションとページャー脱出 |
| **06** | [06. System Information...](file:///home/kodok/Documents/LearnCybersecurity/linux/06.%20System%20Information%20%E2%80%94%20Kernel,%20Hardware%20&%20Environment.md) | Identifikasi kernel, CPU, RAM, disk, IP & rekon lokal | OS & kernel telemetry, hardware, sockets & local recon | システム情報、ハードウェア、ソケットとローカル偵察 |
| **07** | [07. Navigation...](file:///home/kodok/Documents/LearnCybersecurity/linux/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) | Navigasi direktori (`pwd`, `cd`, `ls -la`) | Directory traversal, relative vs absolute paths | ディレクトリ移動と相対パス・絶対パスの概念 |
| **08** | [08. Working with Files...](file:///home/kodok/Documents/LearnCybersecurity/linux/08.%20Working%20with%20Files%20&%20Directories.md) | Manajemen file, wildcard injection & secure shred | File manipulation, wildcard exploits & secure wipe | ファイル操作、ワイルドカード悪用と完全消去 |
| **09** | [09. Editing Files...](file:///home/kodok/Documents/LearnCybersecurity/linux/09.%20Editing%20Files%20%E2%80%94%20Nano%20&%20Vim.md) | Editor terminal (Nano & Vim) dan shell escape | Terminal editors (Nano, Vim modes) & shell breakouts | ターミナルエディタ（Nano / Vim）とシェル起動 |
| **10** | [10. Find Files & Directories.md](file:///home/kodok/Documents/LearnCybersecurity/linux/10.%20Find%20Files%20&%20Directories.md) | Pencarian file, filter & pencarian SUID/SGID PrivEsc | File search, filtering & SUID/PrivEsc hunting | 高度なファイル探索とSUID権限昇格ベクトルの特定 |
| **11** | [11. File Descriptors...](file:///home/kodok/Documents/LearnCybersecurity/linux/11.%20File%20Descriptors%20&%20Redirections.md) | Redireksi I/O, pipe, dan reverse shell `/dev/tcp` | I/O redirection, pipes & reverse shell mechanics | I/Oリダイレクト、パイプとリバースシェル構造 |
| **12** | [12. Filter Contents...](file:///home/kodok/Documents/LearnCybersecurity/linux/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20&%20Text%20Processing.md) | Filter teks (`grep`, `awk`, `sed`) & log forensics | Text processing pipelines, forensic log queries & GTFOBins | テキスト処理、ログフォレンジクスとGTFOBins |
| **13** | [13. Regular Expressions (RegEx).md](file:///home/kodok/Documents/LearnCybersecurity/linux/13.%20Regular%20Expressions%20%28RegEx%29.md) | Regex patterns, ReDoS vulnerability & threat patterns | RegEx syntax, ReDoS backtracking & IOC signatures | 正規表現の文法、ReDoS脆弱性と脅威検知パターン |
| **14** | [14. User Management.md](file:///home/kodok/Documents/LearnCybersecurity/linux/14.%20User%20Management.md) | Manajemen user/grup, `/etc/shadow`, sudo audit | User accounts, shadow hashes & sudo privilege checks | ユーザー管理、パスワードハッシュとsudo権限監査 |
| **15** | [15. Permission Management.md](file:///home/kodok/Documents/LearnCybersecurity/linux/15.%20Permission%20Management.md) | Izin file (rwx, oktal), SUID/SGID, dan Sticky Bit | File permissions, octal modes, SUID/SGID & Sticky Bit | パーミッション管理、8進数表記、SUID/SGID |
| **16** | [16. Package Management.md](file:///home/kodok/Documents/LearnCybersecurity/linux/16.%20Package%20Management.md) | Paket manajer (`apt`, `dpkg`, `pip`, `gem`, `snap`) | Package management workflows & third-party repos | パッケージ管理システムと外部リポジトリ設定 |
| **17** | [17. Service and Process...](file:///home/kodok/Documents/LearnCybersecurity/linux/17.%20Service%20and%20Process%20Management.md) | Manajemen `systemd`, `systemctl`, `journalctl`, sinyal kill | Systemd services, background jobs & process monitoring | Systemdサービス管理、プロセス監視とシグナル制御 |
| **18** | [18. Task Scheduling.md](file:///home/kodok/Documents/LearnCybersecurity/linux/18.%20Task%20Scheduling.md) | Penjadwalan Cron & Systemd Timer, persistensi malware | Crontab syntax, systemd timers & persistence auditing | Cronタスク設定、Systemdタイマーと常駐メカニズム |
| **19** | [19. Working with Web Services.md](file:///home/kodok/Documents/LearnCybersecurity/linux/19.%20Working%20with%20Web%20Services.md) | Apache2, Nginx, Python/PHP server, vHosts & payload staging | Apache, Nginx, Python web servers, vHosts & payload hosting | Webサーバー設定、軽量HTTPサーバーとペイロード配信 |
| **20** | [20. Backup and Restore.md](file:///home/kodok/Documents/LearnCybersecurity/linux/20.%20Backup%20and%20Restore.md) | `tar`, `rsync`, `scp`, `gpg`, tar wildcard injection privesc | `tar`, `rsync`, `scp`, `gpg` & tar wildcard privilege escalation | バックアップ管理、rsync/scpとtar悪用権限昇格 |
| **21** | [21. System Logs.md](file:///home/kodok/Documents/LearnCybersecurity/linux/21.%20System%20Logs.md) | `/var/log`, `journalctl`, `dmesg`, log poisoning & anti-forensics | System logs, auth telemetry, log poisoning & evasion | ログ調査、Syslog/journalctlとログポイズニング |
| **22** | [22. Linux Hardening & Security.md](file:///home/kodok/Documents/LearnCybersecurity/linux/22.%20Linux%20Hardening%20&%20Security.md) | Hardening Linux, SSH hardening, UFW firewall, fail2ban & sysctl | Linux OS hardening, SSH securing, UFW, fail2ban & kernel sysctl | Linuxセキュリティ堅牢化、SSH設定、UFW、fail2banとカーネル設定 |
| 💡 | [Bash Tips & Tricks...](file:///home/kodok/Documents/LearnCybersecurity/linux/Tips%20&%20Tricks/Bash%20Tips%20&%20Tricks%20%E2%80%94%20Shortcuts%20&%20Productivity.md) | Pintasan keyboard bash, riwayat perintah & produktivitas | Bash shortcuts, history expansion & terminal productivity | Bashショートカットキーと生産性向上テクニック |
| 💡 | [Neovim — Tips & Tricks.md](file:///home/kodok/Documents/LearnCybersecurity/linux/Tips%20&%20Tricks/Neovim%20%E2%80%94%20Tips%20&%20Tricks.md) | Navigasi cepat Neovim, modal editing & konfigurasi | Neovim productivity, keymaps & modal editing workflow | Neovimの基本操作、キーマップと設定テクニック |

---

### 3. 🌐 Computer Networking & Protocols (`networking/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [OSI Modelling.md](file:///home/kodok/Documents/LearnCybersecurity/networking/OSI%20Modelling.md) | OSI 7-Layer Model | Analisis mendalam 7 layer OSI, enkapsulasi data, dan vektor serangan tiap layer | Comprehensive 7-layer OSI model, packet dissection & layer attacks | OSI参照モデル7階層の詳細解説、パケット分析と各層攻撃 |
| [TCP-IP Architecture & Socket Programming.md](file:///home/kodok/Documents/LearnCybersecurity/networking/TCP-IP%20Architecture%20&%20Socket%20Programming.md) | TCP/IP & Sockets | Model 4 layer TCP/IP, 3-way handshake, TCP flags, socket programming C/Python & SYN Flood | TCP/IP 4-layer model, handshakes, TCP flags, socket APIs & SYN Flood | TCP/IP 4層構造、ハンドシェイク、ソケットプログラミング |
| [IP Addressing & Subnetting.md](file:///home/kodok/Documents/LearnCybersecurity/networking/IP%20Addressing%20&%20Subnetting.md) | IP & Subnetting | IPv4/IPv6, CIDR, VLSM, private RFC 1918, NAT/PAT, ICMP traceroute & pivoting | IPv4/IPv6, CIDR calculations, RFC 1918 scopes, NAT/PAT & pivoting | IPアドレス体系、CIDRサブネット計算、NAT/PATとルーティング |
| [DNS & Domain Name System Security.md](file:///home/kodok/Documents/LearnCybersecurity/networking/DNS%20&%20Domain%20Name%20System%20Security.md) | DNS Security | Hierarki DNS, record types, DNS zone transfer (AXFR), cache poisoning & DoH/DoT | DNS hierarchy, records, AXFR transfers, cache poisoning & DoH | DNS階層構造、ゾーン転送攻撃、キャッシュ汚染とDNSSEC |
| [ARP & Local Network Attacks.md](file:///home/kodok/Documents/LearnCybersecurity/networking/ARP%20&%20Local%20Network%20Attacks.md) | ARP & MITM Attacks | Protokol ARP, cache poisoning, Man-in-the-Middle (MITM), bettercap & mitigasi DAI | ARP resolution, cache poisoning, MITM sniffing & DAI defense | ARPプロトコル、中間者攻撃（MITM）、DAI対策 |
| [Wireless 802.11 Security & Attacks.md](file:///home/kodok/Documents/LearnCybersecurity/networking/Wireless%20802.11%20Security%20&%20Attacks.md) | Wireless Security | Standar 802.11, WEP/WPA2/WPA3, 4-way handshake, deauth attack, PMKID & aircrack-ng | 802.11 Wi-Fi standards, WPA2/3, 4-way handshake, deauth & aircrack | 無線LAN規格、WPA2ハンドシェイク奪取、Deauth攻撃 |

---

### 4. 🕸️ Web Application Security & OWASP (`web/`)

| # | File | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|---|:-----|:-------------------|:------------|:----------|
| **HTTP.1** | [1. HTTP & cURL.md](file:///home/kodok/Documents/LearnCybersecurity/web/HTTP/1.%20HTTP%20&%20cURL.md) | Protokol HTTP, anatomi URL, dan pengujian cURL melalui Burp Suite | HTTP fundamentals, URL anatomy, cURL switches & Burp proxying | HTTPの基礎、URLの構造、cURLとBurpプロキシ連携 |
| **HTTP.2** | [2. HTTP Requests, Responses & Status Codes.md](file:///home/kodok/Documents/LearnCybersecurity/web/HTTP/2.%20HTTP%20Requests,%20Responses%20&%20Status%20Codes.md) | Struktur pesan HTTP, metode aman/idempotent, klasifikasi status & verb tampering | HTTP message syntax, idempotent verbs, status codes & verb tampering | HTTPメッセージ構造、冪等性、ステータスコードと改ざん |
| **HTTP.3** | [3. HTTP Headers & Security Headers.md](file:///home/kodok/Documents/LearnCybersecurity/web/HTTP/3.%20HTTP%20Headers%20&%20Security%20Headers.md) | Header HTTP esensial, CSP, HSTS, SameSite cookie, SOP & CORS misconfiguration | Request/Response headers, CSP, HSTS, Cookie flags, SOP & CORS | 主要HTTPヘッダー、セキュリティヘッダー、CORS設定ミス |
| **VULN.1** | [1. SQL Injection (SQLi).md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/1.%20SQL%20Injection%20%28SQLi%29.md) | In-Band (UNION/Error), Blind (Boolean/Time), OOB, SQLMap & Prepared Statements | UNION/Error, Boolean/Time Blind, OOB, SQLMap & Prepared Statements | SQLインジェクション（UNION、ブラインド、SQLMap、防御） |
| **VULN.2** | [2. Cross-Site Scripting (XSS).md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Reflected XSS, Stored XSS, DOM XSS, pencurian cookie, CSP bypass & encoding | Reflected, Stored, DOM XSS, session hijacking, CSP bypasses & encoding | XSS（反射型、格納型、DOMベース、Cookie奪取、CSP） |
| **VULN.3** | [3. Cross-Site Request Forgery (CSRF).md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Eksploitasi CSRF form otomatis, SameSite cookie (Lax/Strict) & Anti-CSRF Token | CSRF exploit generation, SameSite cookies & Anti-CSRF tokens | CSRF攻撃、SameSite属性、トークン検証パターン |
| **VULN.4** | [4. Server-Side Request Forgery (SSRF).md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Rekon jaringan internal, eksploitasi metadata cloud (AWS/GCP), gopher & bypass | Internal pivoting, AWS/GCP cloud metadata theft, gopher & bypasses | SSRF攻撃、クラウドメタデータ（AWS/GCP）奪取、Gopher |
| **VULN.5** | [5. Command Injection & File Inclusion.md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/5.%20Command%20Injection%20&%20File%20Inclusion%20%28LFI%20&%20RFI%29.md) | OS Command Injection, PHP Wrappers (`php://filter`), LFI to RCE & log poisoning | OS Command Injection, PHP filter wrappers, LFI to RCE & poisoning | OSコマンドインジェクション、LFI/RFI、ログポイズニング |
| **VULN.6** | [6. File Upload Vulnerabilities & Web Shells.md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/6.%20File%20Upload%20Vulnerabilities%20&%20Web%20Shells.md) | Bypass validasi file, polyglot PHP-GIF, SVG XSS, override `.htaccess` & web shell | Upload validation bypasses, polyglots, SVG XSS & web shells | ファイルアップロード脆弱性、ポリグロット、Webシェル |
| **VULN.7** | [7. Authentication, Session & JWT Attacks.md](file:///home/kodok/Documents/LearnCybersecurity/web/Vulnerabilities/7.%20Authentication,%20Session%20&%20JWT%20Attacks.md) | Kerentanan sesi, JWT `alg: none`, HMAC secret brute-force & Key Confusion RS256 | Session flaws, JWT `alg: none`, HMAC brute force & RS256 confusion | 認証・セッション欠陥、JWT脆弱性（alg: none、鍵混同） |

---

### 5. 🔐 Cryptography & PKI (`cryptography/`)

| # | File | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|---|:-----|:-------------------|:------------|:----------|
| **01** | [1. Symmetric Cryptography & Block Ciphers.md](file:///home/kodok/Documents/LearnCybersecurity/cryptography/1.%20Symmetric%20Cryptography%20&%20Block%20Ciphers.md) | Kriptografi simetris, AES, mode operasi (ECB, CBC, GCM-AEAD) & Padding Oracle | Symmetric encryption, AES, cipher modes (ECB, CBC, GCM) & Padding Oracle | 共通鍵暗号、AES、暗号利用モード（ECB, CBC, GCM） |
| **02** | [2. Asymmetric Cryptography & Key Exchange.md](file:///home/kodok/Documents/LearnCybersecurity/cryptography/2.%20Asymmetric%20Cryptography%20&%20Key%20Exchange.md) | Kunci publik, matematika RSA, Diffie-Hellman (DH/ECDH), ECC kurva eliptik & tanda tangan digital | Public-key math, RSA, Diffie-Hellman, Elliptic Curve (ECC) & signatures | 公開鍵暗号、RSA、ディフィー・ヘルマン鍵交換、ECC |
| **03** | [3. Hash Functions & Message Authentication.md](file:///home/kodok/Documents/LearnCybersecurity/cryptography/3.%20Hash%20Functions%20&%20Message%20Authentication.md) | Sifat fungsi hash, collision attacks, HMAC, password hashing (Argon2, bcrypt) | Hash properties, collision attacks, HMAC & password hashing (Argon2id) | 暗号学的ハッシュ関数、衝突耐性、HMAC、Argon2 |
| **04** | [4. Public Key Infrastructure (PKI) & TLS 1.3.md](file:///home/kodok/Documents/LearnCybersecurity/cryptography/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20&%20TLS%201.3.md) | Arsitektur CA, sertifikat digital X.509, TLS 1.3 1-RTT handshake & Forward Secrecy (PFS) | PKI trust hierarchy, X.509 certificates, TLS 1.3 handshake & PFS | PKI信頼の連鎖、X.509証明書、TLS 1.3ハンドシェイク |

---

### 6. 🎯 Ethical Hacking & Penetration Testing (`ethical-hacking/`)

| # | File | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|---|:-----|:-------------------|:------------|:----------|
| **01** | [1. Penetration Testing Methodology & Recon.md](file:///home/kodok/Documents/LearnCybersecurity/ethical-hacking/1.%20Penetration%20Testing%20Methodology%20&%20Reconnaissance.md) | Metodologi PTES, rekon pasif (Google Dorking, Shodan, crt.sh), rekon aktif & vHost fuzzing | PTES framework, passive OSINT (Shodan, crt.sh), active footpriting & vHosts | PTES手法、パッシブ偵察（Shodan）、アクティブ調査 |
| **02** | [2. Port Scanning & Network Enumeration (Nmap).md](file:///home/kodok/Documents/LearnCybersecurity/ethical-hacking/2.%20Port%20Scanning%20&%20Network%20Enumeration%20%28Nmap%29.md) | Teknik scan Nmap (SYN, Connect, UDP), NSE vulnerability scripts & firewall evasion | Nmap scan types (SYN, UDP), NSE vulnerability engine & IDS evasion | Nmapポートスキャン手法、NSEスクリプト、IDS回避 |
| **03** | [3. Metasploit Framework & Exploitation.md](file:///home/kodok/Documents/LearnCybersecurity/ethical-hacking/3.%20Metasploit%20Framework%20&%20Exploitation.md) | Arsitektur MSF, payload staged vs inline, kontrol memori Meterpreter & pembuatan MSFVenom | MSF architecture, staged vs inline payloads, Meterpreter & MSFVenom | Metasploitフレームワーク、Meterpreter、MSFVenom |
| **04** | [4. Privilege Escalation & Post-Exploitation.md](file:///home/kodok/Documents/LearnCybersecurity/ethical-hacking/4.%20Privilege%20Escalation%20&%20Post-Exploitation.md) | Eskalasi Linux (SUID, Sudo, Capabilities), Windows (`SeImpersonate`), Mimikatz & Chisel | Linux/Windows elevation vectors, token abuse, Mimikatz & Chisel pivoting | 権限昇格手法（SUID, Token悪用）、Mimikatz、Chisel |

---

### 7. 💥 Binary Exploitation & Vulnerability Research (`binary-exploitation/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Stack Buffer Overflow & Shellcoding.md](file:///home/kodok/Documents/LearnCybersecurity/binary-exploitation/Stack%20Buffer%20Overflow%20&%20Shellcoding.md) | Stack Buffer Overflow | Layout memori virtual, kontrol EIP/RIP, shellcode biner, mitigasi ASLR/DEP/Canary, dan Ret2win | Memory anatomy, EIP control, bad characters, shellcode, mitigations & Ret2win | スタックオーバーフロー、EIP奪取、シェルコード、ASLR/DEP回避 |

---

### 8. 🦠 Reverse Engineering & Malware Analysis (`malware-analysis/`)

| # | File | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|---|:-----|:-------------------|:------------|:----------|
| **01** | [1. Static Malware Analysis Fundamentals.md](file:///home/kodok/Documents/LearnCybersecurity/malware-analysis/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Isolasi lab, hashing, string triage, anatomi PE header, Import Address Table (IAT) & UPX | Safe lab fencing, PE header anatomy, IAT suspicious APIs & UPX unpacking | 静的解析の基礎、PEヘッダー構造、IAT危険関数、UPX |
| **02** | [2. Dynamic Malware Analysis & Sandboxing.md](file:///home/kodok/Documents/LearnCybersecurity/malware-analysis/2.%20Dynamic%20Malware%20Analysis%20&%20Sandboxing.md) | Monitoring perilaku Procmon, snapshot Regshot, simulasi jaringan INetSim & anti-VM | Behavioral telemetry (Procmon), Regshot diffs, INetSim & VM evasion | 動的振る舞い解析、Procmon、Regshot、INetSim偽装 |
| **03** | [3. x86 & x64 Assembly for Reverse Engineering.md](file:///home/kodok/Documents/LearnCybersecurity/malware-analysis/3.%20x86%20&%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Register x86/x64, stack frame (prologue/epilogue), instruksi mesin, percabangan & Ghidra/GDB | x86/x64 registers, stack lifecycle, calling conventions & Ghidra/GDB triage | アセンブリ言語基礎、スタックフレーム構造、Ghidra/GDB |

---

### 9. 📱 Mobile Application Security (`mobile-security/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Android Security Internals & Vulnerabilities.md](file:///home/kodok/Documents/LearnCybersecurity/mobile-security/Android%20Security%20Internals%20&%20Vulnerabilities.md) | Android Security | Sandbox Android (UID), IPC Binder, dekompilasi JADX/APKTool, bypass SSL Pinning Frida | Android UID sandbox, Binder IPC, JADX/Smali decompile & Frida SSL pinning | Androidサンドボックス構造、Binder通信、JADX逆コンパイル、Fridaフック |

---

### 10. 🐍 Security Programming & Tool Development (`programming-security/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Offensive Python & Go for Pentesters.md](file:///home/kodok/Documents/LearnCybersecurity/programming-security/Offensive%20Python%20&%20Go%20for%20Pentesters.md) | Python & Go Security | TCP Proxy Python, port scanner multithreaded Go, fuzzer web, dan injeksi shellcode Windows | Raw sockets, TCP proxy, concurrent Go scanner & Windows shellcode injection | Pythonソケットプロキシ、Go言語並行ポートスキャナ、メモリ注入 |

---

### 11. 🎭 Social Engineering & Intelligence (`social-engineering/` & `osint/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Social Engineering — Principles, Vectors & Defense.md](file:///home/kodok/Documents/LearnCybersecurity/social-engineering/Social%20Engineering%20%E2%80%94%20Principles,%20Vectors%20&%20Defense.md) | Social Engineering | 6 Prinsip persuasi Cialdini, pretexting, phishing AiTM (Evilginx2 bypass MFA), BadUSB & FIDO2 | Cialdini persuasion laws, pretexting, AiTM phishing, BadUSB & FIDO2 | ソーシャルエンジニアリング、心理誘導、Evilginx2、FIDO2 |
| [OSINT — Open Source Intelligence Framework.md](file:///home/kodok/Documents/LearnCybersecurity/osint/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20&%20Techniques.md) | OSINT Intelligence | 6 Siklus intelijen, investigator OPSEC, sock puppets, geolokasi foto & SpiderFoot/Recon-ng | 6-Phase intelligence lifecycle, researcher OPSEC, geolocation & OSINT tools | OSINTインテリジェンスサイクル、OPSEC、画像位置特定 |

---

### 12. 🔌 Hardware & IoT Security (`hardware-iot/`)

| File | Topic | 🇮🇩 Bahasa Indonesia | 🇬🇧 English | 🇯🇵 日本語 |
|:-----|:------|:-------------------|:------------|:----------|
| [Hardware & IoT Security — Interfaces, Firmware & Automotive.md](file:///home/kodok/Documents/LearnCybersecurity/hardware-iot/Hardware%20&%20IoT%20Security%20%E2%80%94%20Interfaces,%20Firmware%20&%20Automotive.md) | Hardware & IoT Security | Debug interfaces (UART, JTAG, SPI), ekstraksi firmware Binwalk & serangan CAN Bus mobil | Hardware interfaces (UART/JTAG), Binwalk firmware unpacking & CAN Bus hacking | ハードウェアデバッグ（UART/JTAG）、ファームウェア解析、CANバス |

---

## 📚 Reference Library / Perpustakaan Referensi / 参考文献ライブラリ

Semua materi di repositori ini dirakit dan diverifikasi secara langsung berdasarkan literatur teknis standar industri di direktori lokal `~/Documents/Books/`:

### 🐧 Linux & Operating Systems (`~/Documents/Books/Linux/`)
- **Brian Ward** — *How Linux Works: What Every Superuser Should Know (3rd Edition)*
- **William Shotts** — *The Linux Command Line: A Complete Introduction (2nd Edition)*
- **Jeffrey E.F. Friedl** — *Mastering Regular Expressions (3rd Edition)*
- **Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau** — *Operating Systems: Three Easy Pieces*

### 🌐 Computer Networking & Communications (`~/Documents/Books/CyberSec/Networking/`)
- **James Kurose & Keith Ross** — *Computer Networking: A Top-Down Approach (6th Edition)*
- **William Stallings** — *Network Security Essentials: Applications and Standards (4th Edition)*
- **Matthew Gast** — *802.11 Wireless Networks: The Definitive Guide (2nd Edition)*
- **Christian Benvenuti** — *Understanding Linux Network Internals*
- **W. Richard Stevens** — *UNIX Network Programming (Volume 1, 3rd Edition)*

### 🕸️ Web Application Security (`~/Documents/Books/CyberSec/Web App/`)
- **Dafydd Stuttard & Marcus Pinto** — *The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws (2nd Edition)*
- **Michal Zalewski** — *The Tangled Web: A Guide to Securing Modern Web Applications*

### 🔐 Cryptography & Data Protection (`~/Documents/Books/CyberSec/Cryptography/`)
- **David Wong** — *Real-World Cryptography (2021 Edition)*

### 🎯 Offensive Security & Penetration Testing (`~/Documents/Books/CyberSec/Ethical Hacking/` & `Handbook/`)
- **Peter Kim** — *The Hacker Playbook 3: Practical Guide To Penetration Testing*
- **Georgia Weidman** — *Penetration Testing: A Hands-On Introduction to Hacking*
- **Jon Erickson** — *Hacking: The Art of Exploitation (2nd Edition)*
- **David Kennedy et al.** — *Metasploit: The Penetration Tester's Guide*
- **Allen Harper et al.** — *Gray Hat Hacking: The Ethical Hacker's Handbook*

### 🦠 Malware Analysis, Binary Exploitation & Reverse Engineering (`~/Documents/Books/CyberSec/Malware/` & `Reverse Engineeering/`)
- **Michael Sikorski & Andrew Honig** — *Practical Malware Analysis: The Hands-On Guide to Dissecting Malicious Software*
- **Dennis Andriesse** — *Practical Binary Analysis (1st Edition)*
- **Alex Matrosov et al.** — *Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats*
- **Bruce Dang et al.** — *Practical Reverse Engineering*
- **Chris Anley et al.** — *The Shellcoder's Handbook: Discovering and Exploiting Security Holes (2nd Edition)*

### 📱 Mobile Security & Android (`~/Documents/Books/CyberSec/Android/`)
- **Nikolay Elenkov** — *Android Security Internals: An In-Depth Guide to Android's Security Architecture*

### 💻 Programming & Scripting for Security (`~/Documents/Books/Programming/` & `CyberSec/Programming/`)
- **Justin Seitz & Tim Arnold** — *Black Hat Python (2nd Edition)*
- **Tom Steele, Chris Patten & Dan Kottmann** — *Black Hat Go: Go Programming For Hackers and Pentesters*
- **K. N. King** — *C Programming: A Modern Approach (2nd Edition)*
- **Al Sweigart** — *Automate the Boring Stuff with Python (2nd Edition)*

### 🎭 Social Engineering & Psychology (`~/Documents/Books/CyberSec/Social Engineering/`)
- **Christopher Hadnagy** — *Social Engineering: The Science of Human Hacking (2nd Edition)*
- **Kevin Mitnick** — *The Art of Deception: Controlling the Human Element of Security*
- **Joe Gray** — *Practical Social Engineering: A Primer for the Ethical Hacker*

### 🔍 OSINT & Open Source Intelligence (`~/Documents/Books/CyberSec/OSINT/`)
- **Babak Akhgar et al.** — *Open Source Intelligence Methods and Tools*

### 🔌 Hardware, IoT & Automotive Security (`~/Documents/Books/CyberSec/Hardware/` & `Handbook/`)
- **Jasper van Woudenberg & Colin O'Flynn** — *The Hardware Hacking Handbook*
- **Fotios Chantzis et al.** — *Practical IoT Hacking: The Definitive Guide to Attacking the Internet of Things*
- **Craig Smith** — *The Car Hacker's Handbook: A Guide for the Penetration Tester*
- **Aditya Gupta** — *The IoT Hacker's Handbook*

---

## ⚖️ Legal Disclaimer / Penafian Hukum / 免責事項

- **🇮🇩 Bahasa Indonesia**: Seluruh konten, perintah, dan teknik yang didokumentasikan di repositori ini ditujukan semata-mata untuk **tujuan edukasi, riset keamanan, dan penetration testing berizin**. Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan atau kerusakan yang diakibatkan oleh penggunaan informasi ini.
- **🇬🇧 English**: All documentation, scripts, and attack vectors in this repository are strictly for **educational purposes, defensive auditing, and authorized penetration testing**. The author assumes no liability for any unauthorized activities, misconfigurations, or damages resulting from the application of this knowledge.
- **🇯🇵 日本語**: 本リポジトリに記載されているすべての技術情報、コマンド、検証手順は、**教育、正当なセキュリティ監査、および明示的な許可を得たペネトレーションテスト**のみを目的としています。許可のない不正アクセスや違法行為への利用を固く禁じます。

---

## 👤 Author & Contributions

- **Maintainer**: `kodoktheGr3at`
- **GitHub**: [github.com/Kodokthegr3at](https://github.com/Kodokthegr3at)
- **Repository**: [github.com/Kodokthegr3at/LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
- 💬 *Feedback, improvements, and PRs are welcome!*
