**Bahasa:** [English](README.md) | [Bahasa Indonesia](README.id.md) | [日本語](README.ja.md)

# Zero2Root

[![GitHub stars](https://img.shields.io/github/stars/Kodokthegr3at/Zero2Root?style=social)](https://github.com/Kodokthegr3at/Zero2Root/stargazers)

![Lessons](https://img.shields.io/badge/lessons-78-blue) ![Languages](https://img.shields.io/badge/languages-ID%20%C2%B7%20EN%20%C2%B7%20JA-success) ![Level](https://img.shields.io/badge/level-pemula%20%E2%86%92%20lanjutan-orange) ![Phases](https://img.shields.io/badge/fase-13-blueviolet) [![Last commit](https://img.shields.io/github/last-commit/Kodokthegr3at/Zero2Root)](https://github.com/Kodokthegr3at/Zero2Root/commits/main) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

> **Dari nol sampai root** — basis pengetahuan cybersecurity trilingual dan roadmap karier untuk sisi serangan dan pertahanan, mencakup internal Linux, jaringan, keamanan aplikasi web, kriptografi, reverse engineering, dan bidang terkait. Halaman ini adalah edisi Bahasa Indonesia dan hanya menautkan ke file pelajaran berbahasa Indonesia; buka edisi English atau 日本語 di atas untuk dua bahasa lainnya.

---

## Mulai di sini

| Dokumen | Kegunaan |
|:---------|:--------|
| [ROADMAP.id.md](ROADMAP.id.md) | Jalur belajar utama: 78 pelajaran (`LC-001` sampai `LC-078`), 13 fase, prasyarat |
| [CAREERS.id.md](CAREERS.id.md) | Jalur karier: 13 peran cyber security, pelajaran untuk tiap peran, jam belajar, dan apa yang belum dibahas |
| [BOOKS.id.md](BOOKS.id.md) | Katalog PDF lokal di `~/Documents/Books/`, dipetakan ke tiap pelajaran |
| [curriculum.json](curriculum.json) | Manifest kurikulum yang bisa dibaca mesin (ID, path, bab buku) |

Cara mulai yang disarankan: pilih dulu peran di [CAREERS.id.md](CAREERS.id.md). Belum yakin? Buka [ROADMAP.id.md](ROADMAP.id.md) dan mulai dari **LC-001**, baca bab buku yang ditautkan dari [BOOKS.id.md](BOOKS.id.md), lalu buka file pelajarannya (tiap file punya blok `Curriculum ID` di bagian atas).

---

## Kategori

Setiap pelajaran masuk ke satu fase, dan setiap fase masuk ke satu kategori. Pilih karier di [CAREERS.id.md](CAREERS.id.md) untuk melihat kategori mana yang penting buatmu.

| Kategori | Fase | Isinya |
|:---|:---|:---|
| Fondasi | 0, 1, 2, 4 | Komputer, Linux, jaringan, kriptografi. Dibutuhkan semua jalur. |
| Offensive (red team) | 3, 5 | Serangan web, metodologi pentest, scanning, eksploitasi, privilege escalation. Hanya untuk lab dan pengujian berizin. |
| Eksploitasi & reverse engineering | 6 | Bug memori, shellcode, assembly, analisis malware statis dan dinamis. |
| Defensive (blue team) | 9 | SOC dan log, monitoring jaringan, threat hunting, incident response dan forensik. |
| Domain spesialisasi | 7, 10, 11, 12 | Active Directory, keamanan cloud, DevSecOps, Android, pembuatan tool keamanan dengan Python dan Go, social engineering, OSINT, hardware dan IoT. |
| Bonus | 8 | Keterampilan editor dan produktivitas. |

---

## Tentang repositori ini

Repositori ini adalah basis pengetahuan belajar mandiri yang mencakup offensive security, internal Linux, analisis protokol jaringan, penetration testing aplikasi web, kriptografi, reverse engineering, analisis malware, binary exploitation, pemrograman keamanan, social engineering, OSINT, keamanan mobile, keamanan hardware/IoT, dan pertahanan blue team (SOC, monitoring jaringan, threat hunting, incident response dan forensik).

Setiap pelajaran ada sebagai tiga file independen, masing-masing dalam Bahasa Indonesia, Inggris, dan Jepang, disimpan di subfolder `id/`, `en/`, dan `ja/` di samping tiap topik. Setiap file berisi tabel perbandingan, contoh perintah, catatan keamanan, cheatsheet, dan referensi ke buku teknis yang tersimpan lokal di `~/Documents/Books/`.

---

## Peta repositori

```
Zero2Root/
  basics/               # Dasar-dasar komputasi, Git, filesystem OS, PowerShell/CMD
  linux/                # Shell, alur kerja, administrasi sistem, jaringan, hardening
  networking/           # Model OSI, TCP/IP, DNS, ARP, subnetting, keamanan wireless
  web/                  # HTTP/HTTPS, SQLi, XSS, CSRF, SSRF, LFI/RFI, upload file, serangan JWT/session
  cryptography/         # Kriptografi simetris/asimetris, hashing, PKI, TLS 1.3
  ethical-hacking/      # Metodologi PTES, Nmap, Metasploit, privilege escalation
  binary-exploitation/  # Stack buffer overflow, shellcoding, mitigasi
  malware-analysis/     # Triase statis/dinamis, sandboxing, assembly x86/x64
  mobile-security/      # Internal Android, sandboxing, Binder IPC, reverse engineering
  programming-security/ # Python dan Go ofensif untuk pembuatan tool
  social-engineering/   # Prinsip pengaruh, vektor, pertahanan organisasi
  osint/                # Siklus intelijen, OPSEC, kerangka investigasi
  hardware-iot/         # UART/JTAG/SPI, ekstraksi firmware, CAN bus
  blue-team/            # SOC, analisis log, monitoring jaringan, threat hunting, IR dan forensik
  active-directory/     # Domain, domain controller, objek, Group Policy, trust
  cloud-security/       # Tanggung jawab bersama, IAM, penyimpanan, jaringan, logging, audit
  devsecops/            # Threat modeling, secret scanning, SAST, SCA, DAST, keamanan pipeline CI
```

Setiap folder topik mengikuti layout yang sama: sebuah direktori dasar berisi subfolder `id/`, `en/`, `ja/`, masing-masing menyimpan set file pelajaran yang sama, diterjemahkan dan ditulis secara independen untuk bahasa tersebut.

---

## 1. Dasar-Dasar & Sistem Operasi (`basics/`)

Dasar-dasar komputasi, Git, filesystem OS, PowerShell/CMD.

| LC-ID | Topik |
|:------|:------|
| `LC-001` | [Expression](basics/id/Expression.md) |
| `LC-002` | [Git — Version Control System](basics/id/Git%20%E2%80%94%20Version%20Control%20System.md) |
| `LC-003` | [PowerShell](basics/id/PowerShell.md) |
| `LC-004` | [Windows Command Prompt (cmd.exe)](basics/id/Windows%20Command%20Prompt%20%28cmd.exe%29.md) |
| `LC-005` | [Linux File System](basics/OperatingSystem/id/Linux%20File%20System.md) |
| `LC-006` | [Windows File System](basics/OperatingSystem/id/Windows%20File%20System.md) |
| `LC-007` | [macOS File System](basics/OperatingSystem/id/macOS%20File%20System.md) |

---

## 2. Dasar-Dasar & Keamanan Linux (`linux/`)

Shell, alur kerja, administrasi sistem, jaringan, hardening.

| LC-ID | Topik |
|:------|:------|
| `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/id/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) |
| `LC-009` | [Linux Distributions (Distros)](linux/id/02.%20Linux%20Distributions%20%28Distros%29.md) |
| `LC-010` | [Introduction to Shell](linux/id/03.%20Introduction%20to%20Shell.md) |
| `LC-011` | [Prompt Description & PS1 Customization](linux/id/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) |
| `LC-012` | [Getting Help — man, --help, apropos](linux/id/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) |
| `LC-013` | [System Information — Kernel, Hardware & Environment](linux/id/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) |
| `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/id/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) |
| `LC-015` | [Working with Files & Directories](linux/id/08.%20Working%20with%20Files%20%26%20Directories.md) |
| `LC-016` | [Editing Files — Nano & Vim](linux/id/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) |
| `LC-017` | [Find Files & Directories](linux/id/10.%20Find%20Files%20%26%20Directories.md) |
| `LC-018` | [File Descriptors & Redirections](linux/id/11.%20File%20Descriptors%20%26%20Redirections.md) |
| `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/id/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) |
| `LC-020` | [Regular Expressions (RegEx)](linux/id/13.%20Regular%20Expressions%20%28RegEx%29.md) |
| `LC-021` | [Permission Management](linux/id/14.%20Permission%20Management.md) |
| `LC-022` | [User Management](linux/id/15.%20User%20Management.md) |
| `LC-023` | [Package Management](linux/id/16.%20Package%20Management.md) |
| `LC-024` | [Service and Process Management](linux/id/17.%20Service%20and%20Process%20Management.md) |
| `LC-025` | [Task Scheduling](linux/id/18.%20Task%20Scheduling.md) |
| `LC-026` | [Network Services](linux/id/19.%20Network%20Services.md) |
| `LC-027` | [Working with Web Services](linux/id/20.%20Working%20with%20Web%20Services.md) |
| `LC-028` | [Backup and Restore](linux/id/21.%20Backup%20and%20Restore.md) |
| `LC-029` | [File System Management](linux/id/22.%20File%20System%20Management.md) |
| `LC-030` | [Containerization](linux/id/23.%20Containerization.md) |
| `LC-031` | [Linux Networking — Interfaces & Routing](linux/id/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) |
| `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/id/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) |
| `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/id/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) |
| `LC-034` | [Firewall Setup](linux/id/27.%20Firewall%20Setup.md) |
| `LC-035` | [System Logs](linux/id/28.%20System%20Logs.md) |
| `LC-036` | [Solaris — Linux Distributions vs Solaris](linux/id/29.%20Solaris%20%E2%80%94%20Linux%20Distributions%20vs%20Solaris.md) |
| `LC-037` | [Shortcuts — Bash Tips & Tricks](linux/id/30.%20Shortcuts%20%E2%80%94%20Bash%20Tips%20%26%20Tricks.md) |
| `LC-071` | [Neovim — Tips & Tricks](linux/Tips%20%26%20Tricks/id/Neovim%20%E2%80%94%20Tips%20%26%20Tricks.md) |

---

## 3. Jaringan Komputer & Protokol (`networking/`)

Model OSI, TCP/IP, DNS, ARP, subnetting, keamanan wireless.

| LC-ID | Topik |
|:------|:------|
| `LC-038` | [OSI Modelling](networking/id/OSI%20Modelling.md) |
| `LC-039` | [TCP-IP Architecture & Socket Programming](networking/id/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) |
| `LC-040` | [IP Addressing & Subnetting](networking/id/IP%20Addressing%20%26%20Subnetting.md) |
| `LC-041` | [DNS & Domain Name System Security](networking/id/DNS%20%26%20Domain%20Name%20System%20Security.md) |
| `LC-042` | [ARP & Local Network Attacks](networking/id/ARP%20%26%20Local%20Network%20Attacks.md) |
| `LC-043` | [Wireless 802.11 Security & Attacks](networking/id/Wireless%20802.11%20Security%20%26%20Attacks.md) |

---

## 4. Keamanan Aplikasi Web (`web/`)

HTTP/HTTPS, SQLi, XSS, CSRF, SSRF, LFI/RFI, upload file, serangan JWT/session.

| LC-ID | Topik |
|:------|:------|
| `LC-044` | [HTTP & cURL](web/HTTP/id/1.%20HTTP%20%26%20cURL.md) |
| `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/id/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) |
| `LC-046` | [HTTP Headers & Security Headers](web/HTTP/id/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) |
| `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/id/1.%20SQL%20Injection%20%28SQLi%29.md) |
| `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/id/2.%20Cross-Site%20Scripting%20%28XSS%29.md) |
| `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/id/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) |
| `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/id/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) |
| `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/id/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) |
| `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/id/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) |
| `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/id/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) |

---

## 5. Kriptografi & PKI (`cryptography/`)

Kriptografi simetris/asimetris, hashing, PKI, TLS 1.3.

| LC-ID | Topik |
|:------|:------|
| `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/id/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) |
| `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/id/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) |
| `LC-056` | [Hash Functions & Message Authentication](cryptography/id/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) |
| `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/id/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) |

---

## 6. Ethical Hacking & Penetration Testing (`ethical-hacking/`)

Metodologi PTES, Nmap, Metasploit, privilege escalation.

| LC-ID | Topik |
|:------|:------|
| `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/id/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) |
| `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/id/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) |
| `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/id/3.%20Metasploit%20Framework%20%26%20Exploitation.md) |
| `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/id/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) |

---

## 7. Binary Exploitation (`binary-exploitation/`)

Stack buffer overflow, shellcoding, mitigasi.

| LC-ID | Topik |
|:------|:------|
| `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/id/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) |

---

## 8. Reverse Engineering & Analisis Malware (`malware-analysis/`)

Triase statis/dinamis, sandboxing, assembly x86/x64.

| LC-ID | Topik |
|:------|:------|
| `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/id/1.%20Static%20Malware%20Analysis%20Fundamentals.md) |
| `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/id/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) |
| `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/id/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) |

---

## 9. Keamanan Aplikasi Mobile (`mobile-security/`)

Internal Android, sandboxing, Binder IPC, reverse engineering.

| LC-ID | Topik |
|:------|:------|
| `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/id/Android%20Security%20Internals%20%26%20Vulnerabilities.md) |

---

## 10. Pemrograman Keamanan & Pengembangan Tool (`programming-security/`)

Python dan Go ofensif untuk pembuatan tool.

| LC-ID | Topik |
|:------|:------|
| `LC-067` | [Offensive Python & Go for Pentesters](programming-security/id/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) |

---

## 11. Social Engineering & Faktor Manusia (`social-engineering/`)

Prinsip pengaruh, vektor, pertahanan organisasi.

| LC-ID | Topik |
|:------|:------|
| `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/id/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) |

---

## 12. OSINT (`osint/`)

Siklus intelijen, OPSEC, kerangka investigasi.

| LC-ID | Topik |
|:------|:------|
| `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/id/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) |

---

## 13. Keamanan Hardware & IoT (`hardware-iot/`)

UART/JTAG/SPI, ekstraksi firmware, CAN bus.

| LC-ID | Topik |
|:------|:------|
| `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/id/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) |

---

## 14. Blue Team & Keamanan Defensif (`blue-team/`)

SOC dan analisis log, monitoring jaringan, threat hunting, incident response dan forensik.

| LC-ID | Topik |
|:------|:------|
| `LC-072` | [SOC & Log Analysis](blue-team/id/1.%20SOC%20%26%20Log%20Analysis.md) |
| `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/id/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) |
| `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/id/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) |
| `LC-075` | [Incident Response & Digital Forensics](blue-team/id/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) |

---

## 15. Keamanan Active Directory (`active-directory/`)

Domain, domain controller, objek, Group Policy, trust.

| LC-ID | Topik |
|:------|:------|
| `LC-076` | [Active Directory Fundamentals](active-directory/id/1.%20Active%20Directory%20Fundamentals.md) |

---

## 16. Keamanan Cloud (`cloud-security/`)

Tanggung jawab bersama, IAM, penyimpanan, jaringan, logging, audit.

| LC-ID | Topik |
|:------|:------|
| `LC-077` | [Cloud Security Fundamentals](cloud-security/id/1.%20Cloud%20Security%20Fundamentals.md) |

---

## 17. DevSecOps (`devsecops/`)

Threat modeling, secret scanning, SAST, SCA, DAST, keamanan pipeline CI.

| LC-ID | Topik |
|:------|:------|
| `LC-078` | [DevSecOps Fundamentals](devsecops/id/1.%20DevSecOps%20Fundamentals.md) |

---

## Status cakupan

Zero2Root belum membahas semuanya. Topik-topik ini belum ada sekarang, jadi pelajari dari sumber lain kalau kariermu membutuhkannya. Setiap karier di [CAREERS.id.md](CAREERS.id.md) juga mencantumkan bagian yang masih kurang.

| Topik | Status | Karier yang paling terdampak |
|:---|:---|:---|
| Active Directory: serangan, pertahanan, log event Windows (dasar-dasarnya ada di LC-076) | sebagian tersedia | Pentester, Red Team, SOC Analyst |
| Keamanan cloud: IAM mendalam, Kubernetes, infrastructure as code (dasar-dasarnya ada di LC-077) | sebagian tersedia | Cloud Security Engineer |
| DevSecOps: penandatanganan artefak, SLSA, platform secret (dasar-dasarnya ada di LC-078) | sebagian tersedia | AppSec & DevSecOps Engineer |
| Keamanan AI dan LLM | direncanakan | AppSec, Red Team |
| GRC (risiko, ISO 27001, NIST CSF, hukum perlindungan data) | direncanakan | GRC Analyst |
| Keamanan API, eksploitasi heap, fuzzing, iOS | belum direncanakan | Web pentester, Vulnerability Researcher, Mobile |

---

## Perpustakaan referensi

Semua materi di repositori ini ditulis berdasarkan buku referensi teknis yang tersimpan lokal di `~/Documents/Books/`. Lihat [BOOKS.id.md](BOOKS.id.md) untuk katalog lengkap yang dipetakan ke tiap pelajaran.

---

## Penafian hukum

Seluruh dokumentasi, perintah, dan vektor serangan di repositori ini hanya untuk tujuan edukasi, audit defensif, dan penetration testing berizin. Penulis tidak bertanggung jawab atas aktivitas tidak sah, kesalahan konfigurasi, atau kerusakan yang timbul dari penggunaan materi ini.

---

## Penulis dan kontribusi

- Pengelola: `kodoktheGr3at`
- GitHub: [github.com/Kodokthegr3at](https://github.com/Kodokthegr3at)
- Repositori: [github.com/Kodokthegr3at/Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
- Masukan, perbaikan, dan pull request diterima dengan senang hati.
