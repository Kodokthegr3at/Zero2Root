**Bahasa:** [English](CAREERS.md) | [Bahasa Indonesia](CAREERS.id.md) | [日本語](CAREERS.ja.md)

# Zero2Root: Jalur Karier

> Cyber security itu bukan satu pekerjaan. Halaman ini memuat peran-peran yang umum, apa yang dikerjakan setiap hari, pelajaran Zero2Root mana yang menyiapkanmu, dan yang tidak kalah penting, apa yang belum dibahas Zero2Root supaya kamu tahu harus belajar dari mana lagi.
> Halaman ini hanya menautkan ke file pelajaran berbahasa Indonesia. Kurikulum lengkap yang berurutan ada di [ROADMAP.id.md](ROADMAP.id.md).

---

## Cara membaca halaman ini

1. Semua jalur dimulai dari **fondasi inti** di bawah. Lewati pelajaran yang sudah kamu kuasai.
2. Lanjutkan dengan pelajaran untuk peranmu, sesuai urutan di daftar.
3. **Cakupan** memberi tahu dengan jujur seberapa banyak isi peran itu yang sudah diajarkan Zero2Root: *baik* artinya sebagian besar yang dibutuhkan junior sudah ada, *sebagian* artinya ada topik penting yang belum ada, *minim* artinya kamu perlu materi dari luar untuk sebagian besarnya.
4. **Cocok untuk kerja pertama** menandai peran yang umum diisi orang tanpa pengalaman security sebelumnya. Peran lain biasanya dicapai setelah satu sampai dua tahun di pekerjaan terkait.
5. Jam belajar adalah estimasi untuk membaca dan praktik langsung, belum termasuk membaca buku.

---

## Ringkasan

| Peran | Pekerjaannya | Cocok untuk kerja pertama | Pelajaran setelah fondasi | Jam belajar | Cakupan |
|:---|:---|:---|:---|:---|:---|
| [SOC Analyst](#soc-analyst) | Memantau alert dari banyak sistem, memilah mana yang serangan sungguhan, lalu meneruskannya | ya | 17 | 75-91 | baik |
| [Incident Responder & Analis Forensik (DFIR)](#incident-responder--analis-forensik-dfir) | Mengambil alih saat serangan sudah pasti: membatasi dampaknya, mengumpulkan bukti dari disk dan memori, menyusun ulang timeline, lalu menulis laporan | tidak | 12 | 58-69 | baik |
| [Threat Hunter & Detection Engineer](#threat-hunter--detection-engineer) | Menulis dan menyetel aturan yang memicu alert, lalu secara aktif mencari penyerang yang lolos dari aturan itu | tidak | 9 | 47-57 | baik |
| [Penetration Tester](#penetration-tester) | Menguji jaringan dan aplikasi dengan izin tertulis, menemukan kelemahan sebelum penyerang sungguhan, lalu melaporkan cara memperbaikinya | tidak | 26 | 105-124 | sebagian |
| [Web Application Pentester & Bug Hunter](#web-application-pentester--bug-hunter) | Fokus pada website dan API: mencari bug injection, kontrol akses, dan session, lalu melaporkannya ke pemilik atau program bug bounty | tidak | 15 | 59-72 | baik |
| [Red Team Operator](#red-team-operator) | Berperan sebagai penyerang realistis selama berminggu-minggu untuk menguji apakah blue team menyadarinya | tidak | 24 | 107-131 | sebagian |
| [Malware Analyst & Reverse Engineer](#malware-analyst--reverse-engineer) | Membongkar file mencurigakan untuk tahu apa yang dilakukannya, cara mendeteksinya, dan cara membersihkan dampaknya | tidak | 7 | 40-50 | baik |
| [Vulnerability Researcher & Exploit Developer](#vulnerability-researcher--exploit-developer) | Mencari bug baru di software dan membuktikan apakah bisa dieksploitasi, supaya vendor bisa memperbaikinya | tidak | 4 | 25-32 | minim |
| [Application Security & DevSecOps Engineer](#application-security--devsecops-engineer) | Bekerja bersama developer supaya kode dirilis dengan aman: meninjau desain dan kode, serta menambahkan pengecekan keamanan ke pipeline build | tidak | 19 | 80-98 | baik |
| [Cloud Security Engineer](#cloud-security-engineer) | Mengamankan akun, identitas, jaringan, dan workload di AWS, Azure, atau Google Cloud | tidak | 12 | 56-65 | sebagian |
| [Threat Intelligence & OSINT Analyst](#threat-intelligence--osint-analyst) | Melacak kelompok penyerang dan metodenya dari sumber publik maupun privat, lalu mengubahnya jadi saran yang bisa dipakai tim defender | tidak | 5 | 25-30 | sebagian |
| [Spesialis Keamanan Mobile & IoT](#spesialis-keamanan-mobile--iot) | Menguji aplikasi ponsel, perangkat pintar, dan firmware-nya, mulai dari kode aplikasi sampai papan sirkuit | tidak | 14 | 66-81 | sebagian |
| [GRC & Security Compliance Analyst](#grc--security-compliance-analyst) | Mengelola risiko, kebijakan, dan audit berdasarkan standar seperti ISO 27001 atau NIST CSF | ya | 6 | 30-35 | sebagian |

---

## Fondasi inti (semua jalur)

Pelajaran ini dipakai bersama oleh semua peran: cara kerja komputer, Linux, dan jaringan, ditambah dasar-dasar web. Sekitar 108 sampai 128 jam.

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-001` | [Expression](basics/id/Expression.md) | Pemula | 2-3 jam |
| 2 | `LC-002` | [Git — Version Control System](basics/id/Git%20%E2%80%94%20Version%20Control%20System.md) | Pemula | 3-4 jam |
| 3 | `LC-005` | [Linux File System](basics/OperatingSystem/id/Linux%20File%20System.md) | Pemula | 5-6 jam |
| 4 | `LC-006` | [Windows File System](basics/OperatingSystem/id/Windows%20File%20System.md) | Pemula | 5-6 jam |
| 5 | `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/id/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) | Pemula | 3-4 jam |
| 6 | `LC-009` | [Linux Distributions (Distros)](linux/id/02.%20Linux%20Distributions%20%28Distros%29.md) | Pemula | 2-3 jam |
| 7 | `LC-010` | [Introduction to Shell](linux/id/03.%20Introduction%20to%20Shell.md) | Pemula | 4-5 jam |
| 8 | `LC-011` | [Prompt Description & PS1 Customization](linux/id/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) | Pemula | 2 jam |
| 9 | `LC-012` | [Getting Help — man, --help, apropos](linux/id/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) | Pemula | 2 jam |
| 10 | `LC-013` | [System Information — Kernel, Hardware & Environment](linux/id/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) | Pemula | 3 jam |
| 11 | `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/id/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) | Pemula | 2-3 jam |
| 12 | `LC-015` | [Working with Files & Directories](linux/id/08.%20Working%20with%20Files%20%26%20Directories.md) | Pemula | 3-4 jam |
| 13 | `LC-016` | [Editing Files — Nano & Vim](linux/id/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) | Pemula | 4-5 jam |
| 14 | `LC-017` | [Find Files & Directories](linux/id/10.%20Find%20Files%20%26%20Directories.md) | Pemula | 3 jam |
| 15 | `LC-018` | [File Descriptors & Redirections](linux/id/11.%20File%20Descriptors%20%26%20Redirections.md) | Menengah | 4 jam |
| 16 | `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/id/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) | Menengah | 4-5 jam |
| 17 | `LC-020` | [Regular Expressions (RegEx)](linux/id/13.%20Regular%20Expressions%20%28RegEx%29.md) | Menengah | 5-6 jam |
| 18 | `LC-021` | [Permission Management](linux/id/14.%20Permission%20Management.md) | Menengah | 4-5 jam |
| 19 | `LC-022` | [User Management](linux/id/15.%20User%20Management.md) | Menengah | 4 jam |
| 20 | `LC-024` | [Service and Process Management](linux/id/17.%20Service%20and%20Process%20Management.md) | Menengah | 4-5 jam |
| 21 | `LC-026` | [Network Services](linux/id/19.%20Network%20Services.md) | Menengah | 4 jam |
| 22 | `LC-031` | [Linux Networking — Interfaces & Routing](linux/id/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) | Menengah | 4 jam |
| 23 | `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/id/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) | Menengah | 4-5 jam |
| 24 | `LC-035` | [System Logs](linux/id/28.%20System%20Logs.md) | Menengah | 3-4 jam |
| 25 | `LC-038` | [OSI Modelling](networking/id/OSI%20Modelling.md) | Pemula | 6-8 jam |
| 26 | `LC-039` | [TCP-IP Architecture & Socket Programming](networking/id/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) | Menengah | 5-6 jam |
| 27 | `LC-040` | [IP Addressing & Subnetting](networking/id/IP%20Addressing%20%26%20Subnetting.md) | Menengah | 4-5 jam |
| 28 | `LC-041` | [DNS & Domain Name System Security](networking/id/DNS%20%26%20Domain%20Name%20System%20Security.md) | Menengah | 4 jam |
| 29 | `LC-044` | [HTTP & cURL](web/HTTP/id/1.%20HTTP%20%26%20cURL.md) | Pemula | 3 jam |
| 30 | `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/id/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) | Pemula | 3 jam |

---

## SOC Analyst

**Pekerjaannya:** Memantau alert dari banyak sistem, memilah mana yang serangan sungguhan, lalu meneruskannya. Pekerjaan pertama yang paling umum di cyber security.

**Cocok untuk kerja pertama:** ya  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/id/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Pemula | 3-4 jam |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 4 | `LC-034` | [Firewall Setup](linux/id/27.%20Firewall%20Setup.md) | Lanjutan | 4 jam |
| 5 | `LC-042` | [ARP & Local Network Attacks](networking/id/ARP%20%26%20Local%20Network%20Attacks.md) | Lanjutan | 4 jam |
| 6 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Menengah | 3-4 jam |
| 7 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 8 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 9 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/id/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Menengah | 3-4 jam |
| 12 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/id/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Menengah | 4-5 jam |
| 13 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 14 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/id/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Menengah | 6-7 jam |
| 15 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |
| 16 | `LC-075` | [Incident Response & Digital Forensics](blue-team/id/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Lanjutan | 7-9 jam |
| 17 | `LC-076` | [Active Directory Fundamentals](active-directory/id/1.%20Active%20Directory%20Fundamentals.md) | Menengah | 5-6 jam |

Waktu belajar jalur ini: sekitar 75 sampai 91 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Active Directory dan log event Windows secara mendalam
- Lab SIEM langsung dengan produk tertentu
- Analisis email phishing sebagai pelajaran tersendiri
- Log Microsoft 365 dan sign-in Entra ID

---

## Incident Responder & Analis Forensik (DFIR)

**Pekerjaannya:** Mengambil alih saat serangan sudah pasti: membatasi dampaknya, mengumpulkan bukti dari disk dan memori, menyusun ulang timeline, lalu menulis laporan.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-007` | [macOS File System](basics/OperatingSystem/id/macOS%20File%20System.md) | Pemula | 4-5 jam |
| 3 | `LC-028` | [Backup and Restore](linux/id/21.%20Backup%20and%20Restore.md) | Menengah | 3 jam |
| 4 | `LC-029` | [File System Management](linux/id/22.%20File%20System%20Management.md) | Menengah | 4-5 jam |
| 5 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 6 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Lanjutan | 5-6 jam |
| 7 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/id/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Lanjutan | 5 jam |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 9 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/id/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Menengah | 6-7 jam |
| 10 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |
| 11 | `LC-075` | [Incident Response & Digital Forensics](blue-team/id/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Lanjutan | 7-9 jam |
| 12 | `LC-076` | [Active Directory Fundamentals](active-directory/id/1.%20Active%20Directory%20Fundamentals.md) | Menengah | 5-6 jam |

Waktu belajar jalur ini: sekitar 58 sampai 69 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Forensik registry dan artefak Windows secara mendalam
- Forensik perangkat mobile
- Incident response di cloud

---

## Threat Hunter & Detection Engineer

**Pekerjaannya:** Menulis dan menyetel aturan yang memicu alert, lalu secara aktif mencari penyerang yang lolos dari aturan itu.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/id/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Lanjutan | 5-6 jam |
| 3 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/id/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Lanjutan | 5-6 jam |
| 4 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Lanjutan | 5-6 jam |
| 5 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/id/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Lanjutan | 5 jam |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 7 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 8 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/id/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Menengah | 6-7 jam |
| 9 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |

Waktu belajar jalur ini: sekitar 47 sampai 57 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Detection-as-code dan pipeline CI untuk aturan deteksi
- Data engineering untuk pipeline log

---

## Penetration Tester

**Pekerjaannya:** Menguji jaringan dan aplikasi dengan izin tertulis, menemukan kelemahan sebelum penyerang sungguhan, lalu melaporkan cara memperbaikinya.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/id/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Pemula | 3-4 jam |
| 3 | `LC-025` | [Task Scheduling](linux/id/18.%20Task%20Scheduling.md) | Menengah | 3-4 jam |
| 4 | `LC-027` | [Working with Web Services](linux/id/20.%20Working%20with%20Web%20Services.md) | Menengah | 3-4 jam |
| 5 | `LC-030` | [Containerization](linux/id/23.%20Containerization.md) | Lanjutan | 4-5 jam |
| 6 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 7 | `LC-034` | [Firewall Setup](linux/id/27.%20Firewall%20Setup.md) | Lanjutan | 4 jam |
| 8 | `LC-042` | [ARP & Local Network Attacks](networking/id/ARP%20%26%20Local%20Network%20Attacks.md) | Lanjutan | 4 jam |
| 9 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/id/Wireless%20802.11%20Security%20%26%20Attacks.md) | Lanjutan | 5 jam |
| 10 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Menengah | 3-4 jam |
| 11 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 12 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 13 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Menengah | 3 jam |
| 14 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 15 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 16 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Lanjutan | 3-4 jam |
| 17 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 18 | `LC-056` | [Hash Functions & Message Authentication](cryptography/id/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Menengah | 3-4 jam |
| 19 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 20 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/id/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Menengah | 4-5 jam |
| 21 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/id/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | Menengah | 4 jam |
| 22 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/id/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Lanjutan | 5-6 jam |
| 23 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/id/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Lanjutan | 5-6 jam |
| 24 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 25 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/id/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Menengah | 5 jam |
| 26 | `LC-076` | [Active Directory Fundamentals](active-directory/id/1.%20Active%20Directory%20Fundamentals.md) | Menengah | 5-6 jam |

Waktu belajar jalur ini: sekitar 105 sampai 124 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Serangan dan pertahanan Active Directory (sebagian besar tes internal melibatkan AD)
- Menulis laporan pentest
- Penetration testing di cloud

---

## Web Application Pentester & Bug Hunter

**Pekerjaannya:** Fokus pada website dan API: mencari bug injection, kontrol akses, dan session, lalu melaporkannya ke pemilik atau program bug bounty.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/id/20.%20Working%20with%20Web%20Services.md) | Menengah | 3-4 jam |
| 2 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Menengah | 3-4 jam |
| 3 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 4 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 5 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Menengah | 3 jam |
| 6 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 7 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 8 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Lanjutan | 3-4 jam |
| 9 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 10 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/id/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | Menengah | 4-5 jam |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/id/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Menengah | 3-4 jam |
| 12 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/id/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Menengah | 4-5 jam |
| 14 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 15 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/id/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Menengah | 5 jam |

Waktu belajar jalur ini: sekitar 59 sampai 72 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Keamanan API (REST dan GraphQL) sebagai pelajaran tersendiri
- Celah OAuth dan SSO secara mendalam
- Insecure deserialization

---

## Red Team Operator

**Pekerjaannya:** Berperan sebagai penyerang realistis selama berminggu-minggu untuk menguji apakah blue team menyadarinya. Biasanya dicapai setelah beberapa tahun jadi pentester.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/id/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Pemula | 3-4 jam |
| 3 | `LC-030` | [Containerization](linux/id/23.%20Containerization.md) | Lanjutan | 4-5 jam |
| 4 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 5 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Menengah | 3-4 jam |
| 6 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 7 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 8 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Menengah | 3 jam |
| 9 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 10 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 11 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Lanjutan | 3-4 jam |
| 12 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/id/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Menengah | 4-5 jam |
| 14 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/id/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | Menengah | 4 jam |
| 15 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/id/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Lanjutan | 5-6 jam |
| 16 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/id/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Lanjutan | 5-6 jam |
| 17 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/id/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Lanjutan | 6-8 jam |
| 18 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/id/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Lanjutan | 8-10 jam |
| 19 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 20 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/id/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Menengah | 4-5 jam |
| 21 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/id/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Menengah | 5 jam |
| 22 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 23 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |
| 24 | `LC-076` | [Active Directory Fundamentals](active-directory/id/1.%20Active%20Directory%20Fundamentals.md) | Menengah | 5-6 jam |

Waktu belajar jalur ini: sekitar 107 sampai 131 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Jalur serangan Active Directory
- Infrastruktur command-and-control (C2) dan OPSEC
- Cara kerja deteksi endpoint dan kenapa penyerang berusaha menghindarinya

---

## Malware Analyst & Reverse Engineer

**Pekerjaannya:** Membongkar file mencurigakan untuk tahu apa yang dilakukannya, cara mendeteksinya, dan cara membersihkan dampaknya.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/id/PowerShell.md) | Pemula | 4-5 jam |
| 2 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/id/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Lanjutan | 6-8 jam |
| 3 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Lanjutan | 5-6 jam |
| 4 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/id/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Lanjutan | 5 jam |
| 5 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/id/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Lanjutan | 8-10 jam |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 7 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |

Waktu belajar jalur ini: sekitar 40 sampai 50 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Internal Windows secara mendalam
- Unpacking dan trik anti-analisis
- Malware .NET dan Android

---

## Vulnerability Researcher & Exploit Developer

**Pekerjaannya:** Mencari bug baru di software dan membuktikan apakah bisa dieksploitasi, supaya vendor bisa memperbaikinya.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** minim

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/id/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Lanjutan | 6-8 jam |
| 2 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Lanjutan | 5-6 jam |
| 3 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/id/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Lanjutan | 8-10 jam |
| 4 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |

Waktu belajar jalur ini: sekitar 25 sampai 32 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Eksploitasi heap
- Fuzzing
- Eksploitasi kernel dan browser
- Mitigasi modern secara mendalam (CFG, CET, sandboxing)

---

## Application Security & DevSecOps Engineer

**Pekerjaannya:** Bekerja bersama developer supaya kode dirilis dengan aman: meninjau desain dan kode, serta menambahkan pengecekan keamanan ke pipeline build.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** baik

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/id/20.%20Working%20with%20Web%20Services.md) | Menengah | 3-4 jam |
| 2 | `LC-030` | [Containerization](linux/id/23.%20Containerization.md) | Lanjutan | 4-5 jam |
| 3 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Menengah | 3-4 jam |
| 4 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 5 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 6 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Menengah | 3 jam |
| 7 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 8 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 9 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Lanjutan | 3-4 jam |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 11 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/id/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | Menengah | 4-5 jam |
| 12 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/id/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | Menengah | 4-5 jam |
| 13 | `LC-056` | [Hash Functions & Message Authentication](cryptography/id/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Menengah | 3-4 jam |
| 14 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 15 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Lanjutan | 6-8 jam |
| 16 | `LC-077` | [Cloud Security Fundamentals](cloud-security/id/1.%20Cloud%20Security%20Fundamentals.md) | Menengah | 5-6 jam |
| 17 | `LC-078` | [DevSecOps Fundamentals](devsecops/id/1.%20DevSecOps%20Fundamentals.md) | Menengah | 6-7 jam |
| 18 | `LC-080` | [AI & LLM Security Fundamentals](ai-security/id/1.%20AI%20%26%20LLM%20Security%20Fundamentals.md) | Menengah | 5-6 jam |
| 19 | `LC-081` | [Cloud IAM in Depth](cloud-security/id/2.%20Cloud%20IAM%20in%20Depth.md) | Lanjutan | 6-7 jam |

Waktu belajar jalur ini: sekitar 80 sampai 98 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Threat modeling secara mendalam (diagram alur data, attack tree)
- Secure code review untuk bahasa tertentu
- Penandatanganan artefak dan provenance build SLSA
- Platform manajemen secret seperti HashiCorp Vault

---

## Cloud Security Engineer

**Pekerjaannya:** Mengamankan akun, identitas, jaringan, dan workload di AWS, Azure, atau Google Cloud.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/id/20.%20Working%20with%20Web%20Services.md) | Menengah | 3-4 jam |
| 2 | `LC-030` | [Containerization](linux/id/23.%20Containerization.md) | Lanjutan | 4-5 jam |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 4 | `LC-034` | [Firewall Setup](linux/id/27.%20Firewall%20Setup.md) | Lanjutan | 4 jam |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 6 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 7 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 9 | `LC-077` | [Cloud Security Fundamentals](cloud-security/id/1.%20Cloud%20Security%20Fundamentals.md) | Menengah | 5-6 jam |
| 10 | `LC-078` | [DevSecOps Fundamentals](devsecops/id/1.%20DevSecOps%20Fundamentals.md) | Menengah | 6-7 jam |
| 11 | `LC-081` | [Cloud IAM in Depth](cloud-security/id/2.%20Cloud%20IAM%20in%20Depth.md) | Lanjutan | 6-7 jam |
| 12 | `LC-082` | [Kubernetes Security](cloud-security/id/3.%20Kubernetes%20Security.md) | Lanjutan | 7-8 jam |

Waktu belajar jalur ini: sekitar 56 sampai 65 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Keamanan infrastructure as code secara mendalam (modul Terraform, policy as code)
- Incident response dan deteksi di cloud secara mendalam
- Keamanan jaringan cloud secara mendalam (private endpoint, kontrol lalu lintas keluar)
- Keamanan serverless

---

## Threat Intelligence & OSINT Analyst

**Pekerjaannya:** Melacak kelompok penyerang dan metodenya dari sumber publik maupun privat, lalu mengubahnya jadi saran yang bisa dipakai tim defender.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Lanjutan | 5-6 jam |
| 2 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/id/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Menengah | 4-5 jam |
| 3 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/id/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Menengah | 5 jam |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 5 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Lanjutan | 6-8 jam |

Waktu belajar jalur ini: sekitar 25 sampai 30 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Kerangka intelijen (Diamond Model, kill chain) secara mendalam
- Format berbagi (STIX/TAXII, MISP)
- Menulis laporan intelijen

---

## Spesialis Keamanan Mobile & IoT

**Pekerjaannya:** Menguji aplikasi ponsel, perangkat pintar, dan firmware-nya, mulai dari kode aplikasi sampai papan sirkuit.

**Cocok untuk kerja pertama:** tidak, biasanya setelah 1-2 tahun di peran terkait  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/id/Wireless%20802.11%20Security%20%26%20Attacks.md) | Lanjutan | 5 jam |
| 2 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) | Menengah | 5-6 jam |
| 3 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Menengah | 4-5 jam |
| 4 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Menengah | 3 jam |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Lanjutan | 3-4 jam |
| 6 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Lanjutan | 4-5 jam |
| 7 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Lanjutan | 3-4 jam |
| 8 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Lanjutan | 4-5 jam |
| 9 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/id/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | Menengah | 4-5 jam |
| 10 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 11 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/id/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Lanjutan | 6-8 jam |
| 12 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/id/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Lanjutan | 8-10 jam |
| 13 | `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/id/Android%20Security%20Internals%20%26%20Vulnerabilities.md) | Lanjutan | 6-8 jam |
| 14 | `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/id/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) | Lanjutan | 6-8 jam |

Waktu belajar jalur ini: sekitar 66 sampai 81 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Keamanan iOS
- Bluetooth Low Energy
- Intersepsi trafik aplikasi mobile secara mendalam

---

## GRC & Security Compliance Analyst

**Pekerjaannya:** Mengelola risiko, kebijakan, dan audit berdasarkan standar seperti ISO 27001 atau NIST CSF. Lebih sedikit bekerja dengan tool, lebih banyak dengan orang dan dokumen.

**Cocok untuk kerja pertama:** ya  
**Cakupan di Zero2Root:** sebagian

**Pelajaran, berurutan (setelah fondasi inti):**

| # | ID | Pelajaran | Level | Jam |
|:---|:---|:---|:---|:---|
| 1 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Lanjutan | 4 jam |
| 2 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Lanjutan | 5 jam |
| 3 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/id/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Menengah | 4-5 jam |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) | Pemula | 5-6 jam |
| 5 | `LC-075` | [Incident Response & Digital Forensics](blue-team/id/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Lanjutan | 7-9 jam |
| 6 | `LC-079` | [GRC Fundamentals](grc/id/1.%20GRC%20Fundamentals.md) | Pemula | 5-6 jam |

Waktu belajar jalur ini: sekitar 30 sampai 35 jam di luar fondasi inti.

**Belum dibahas di Zero2Root** (pelajari dari sumber lain):

- Menerapkan ISO 27001 langkah demi langkah (dokumen ISMS, audit internal)
- Analisis risiko kuantitatif (FAIR) secara mendalam
- Regulasi sektor (keuangan, kesehatan, pembayaran)
- Privacy engineering dan penilaian dampak pelindungan data (DPIA)
