**Language:** [English](README.md) | [Bahasa Indonesia](README.id.md) | [日本語](README.ja.md)

# Zero2Root

[![GitHub stars](https://img.shields.io/github/stars/Kodokthegr3at/Zero2Root?style=social)](https://github.com/Kodokthegr3at/Zero2Root/stargazers)

![Lessons](https://img.shields.io/badge/lessons-80-blue) ![Languages](https://img.shields.io/badge/languages-ID%20%C2%B7%20EN%20%C2%B7%20JA-success) ![Level](https://img.shields.io/badge/level-beginner%20%E2%86%92%20advanced-orange) ![Phases](https://img.shields.io/badge/phases-15-blueviolet) [![Last commit](https://img.shields.io/github/last-commit/Kodokthegr3at/Zero2Root)](https://github.com/Kodokthegr3at/Zero2Root/commits/main) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

> **From zero to root** — a trilingual cybersecurity knowledge base and career roadmap for both attack and defense, covering Linux internals, networking, web application security, cryptography, reverse engineering, and related fields. This page is the English edition and links only to the English lesson files; open the Bahasa Indonesia or 日本語 edition above for the other two.

---

## Start here

| Document | Purpose |
|:---------|:--------|
| [ROADMAP.md](ROADMAP.md) | Master learning path: 80 lessons (`LC-001` to `LC-080`), 15 phases, prerequisites |
| [CAREERS.md](CAREERS.md) | Career paths: 13 cyber security roles, the lessons for each, study hours, and what is not covered yet |
| [BOOKS.md](BOOKS.md) | Local PDF catalog at `~/Documents/Books/`, mapped to each lesson |
| [curriculum.json](curriculum.json) | Machine-readable curriculum manifest (IDs, paths, book chapters) |

Recommended entry: pick a role in [CAREERS.md](CAREERS.md) first. Not sure yet? Open [ROADMAP.md](ROADMAP.md) and start at **LC-001**, read the linked book chapters from [BOOKS.md](BOOKS.md), then open the lesson file (each has a `Curriculum ID` block at the top).

---

## Categories

Every lesson belongs to one phase, and every phase belongs to one category. Pick a career in [CAREERS.md](CAREERS.md) to see which categories matter for you.

| Category | Phases | What it covers |
|:---|:---|:---|
| Foundation | 0, 1, 2, 4 | Computers, Linux, networking, cryptography. Needed by every path. |
| Offensive (red team) | 3, 5 | Web attacks, pentest methodology, scanning, exploitation, privilege escalation. Lab and authorized testing only. |
| Exploitation & reverse engineering | 6 | Memory bugs, shellcode, assembly, static and dynamic malware analysis. |
| Defensive (blue team) | 9 | SOC and logs, network monitoring, threat hunting, incident response and forensics. |
| Specialized domains | 7, 10, 11, 12, 13, 14 | Active Directory, cloud security, DevSecOps, GRC, AI security, Android, security tooling in Python and Go, social engineering, OSINT, hardware and IoT. |
| Bonus | 8 | Editor and productivity skills. |

---

## About this repository

This repository is a self-study knowledge base covering offensive security, Linux internals, network protocol analysis, web application penetration testing, cryptography, reverse engineering, malware analysis, binary exploitation, security programming, social engineering, OSINT, mobile security, hardware/IoT security, and blue team defense (SOC, network monitoring, threat hunting, incident response and forensics).

Every lesson exists as three independent files, one each in Bahasa Indonesia, English, and Japanese, kept in `id/`, `en/`, and `ja/` subfolders next to each topic. Each includes comparison tables, command walkthroughs, security notes, cheatsheets, and references to technical books held locally under `~/Documents/Books/`.

---

## Repository map

```
Zero2Root/
  basics/               # Computing fundamentals, Git, OS filesystems, PowerShell/CMD
  linux/                # Shell, workflow, system administration, networking, hardening
  networking/           # OSI model, TCP/IP, DNS, ARP, subnetting, wireless security
  web/                  # HTTP/HTTPS, SQLi, XSS, CSRF, SSRF, LFI/RFI, uploads, JWT/session attacks
  cryptography/         # Symmetric/asymmetric crypto, hashing, PKI, TLS 1.3
  ethical-hacking/      # PTES methodology, Nmap, Metasploit, privilege escalation
  binary-exploitation/  # Stack buffer overflows, shellcoding, mitigations
  malware-analysis/     # Static/dynamic triage, sandboxing, x86/x64 assembly
  mobile-security/      # Android internals, sandboxing, Binder IPC, reverse engineering
  programming-security/ # Offensive Python and Go for tooling
  social-engineering/   # Influence principles, vectors, organizational defense
  osint/                # Intelligence lifecycle, OPSEC, investigation frameworks
  hardware-iot/         # UART/JTAG/SPI, firmware extraction, CAN bus
  blue-team/            # SOC, log analysis, network monitoring, threat hunting, IR and forensics
  active-directory/     # Domains, domain controllers, objects, Group Policy, trusts
  cloud-security/       # Shared responsibility, IAM, storage, network, logging, auditing
  devsecops/            # Threat modeling, secret scanning, SAST, SCA, DAST, CI pipeline security
  grc/                  # Policies, risk management, controls, frameworks, data protection law, audits
  ai-security/          # OWASP Top 10 for LLMs, prompt injection, agents, RAG, model supply chain, AI governance
```

Every topic folder follows the same layout: a base directory containing `id/`, `en/`, `ja/` subfolders, each holding the same set of lesson files translated and written independently for that language.

---

## 1. Basics & Operating Systems (`basics/`)

Computing fundamentals, Git, OS filesystems, PowerShell/CMD.

| LC-ID | Topic |
|:------|:------|
| `LC-001` | [Expression](basics/en/Expression.md) |
| `LC-002` | [Git — Version Control System](basics/en/Git%20%E2%80%94%20Version%20Control%20System.md) |
| `LC-003` | [PowerShell](basics/en/PowerShell.md) |
| `LC-004` | [Windows Command Prompt (cmd.exe)](basics/en/Windows%20Command%20Prompt%20%28cmd.exe%29.md) |
| `LC-005` | [Linux File System](basics/OperatingSystem/en/Linux%20File%20System.md) |
| `LC-006` | [Windows File System](basics/OperatingSystem/en/Windows%20File%20System.md) |
| `LC-007` | [macOS File System](basics/OperatingSystem/en/macOS%20File%20System.md) |

---

## 2. Linux Fundamentals & Security (`linux/`)

Shell, workflow, system administration, networking, hardening.

| LC-ID | Topic |
|:------|:------|
| `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/en/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) |
| `LC-009` | [Linux Distributions (Distros)](linux/en/02.%20Linux%20Distributions%20%28Distros%29.md) |
| `LC-010` | [Introduction to Shell](linux/en/03.%20Introduction%20to%20Shell.md) |
| `LC-011` | [Prompt Description & PS1 Customization](linux/en/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) |
| `LC-012` | [Getting Help — man, --help, apropos](linux/en/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) |
| `LC-013` | [System Information — Kernel, Hardware & Environment](linux/en/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) |
| `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/en/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) |
| `LC-015` | [Working with Files & Directories](linux/en/08.%20Working%20with%20Files%20%26%20Directories.md) |
| `LC-016` | [Editing Files — Nano & Vim](linux/en/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) |
| `LC-017` | [Find Files & Directories](linux/en/10.%20Find%20Files%20%26%20Directories.md) |
| `LC-018` | [File Descriptors & Redirections](linux/en/11.%20File%20Descriptors%20%26%20Redirections.md) |
| `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/en/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) |
| `LC-020` | [Regular Expressions (RegEx)](linux/en/13.%20Regular%20Expressions%20%28RegEx%29.md) |
| `LC-021` | [Permission Management](linux/en/14.%20Permission%20Management.md) |
| `LC-022` | [User Management](linux/en/15.%20User%20Management.md) |
| `LC-023` | [Package Management](linux/en/16.%20Package%20Management.md) |
| `LC-024` | [Service and Process Management](linux/en/17.%20Service%20and%20Process%20Management.md) |
| `LC-025` | [Task Scheduling](linux/en/18.%20Task%20Scheduling.md) |
| `LC-026` | [Network Services](linux/en/19.%20Network%20Services.md) |
| `LC-027` | [Working with Web Services](linux/en/20.%20Working%20with%20Web%20Services.md) |
| `LC-028` | [Backup and Restore](linux/en/21.%20Backup%20and%20Restore.md) |
| `LC-029` | [File System Management](linux/en/22.%20File%20System%20Management.md) |
| `LC-030` | [Containerization](linux/en/23.%20Containerization.md) |
| `LC-031` | [Linux Networking — Interfaces & Routing](linux/en/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) |
| `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/en/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) |
| `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) |
| `LC-034` | [Firewall Setup](linux/en/27.%20Firewall%20Setup.md) |
| `LC-035` | [System Logs](linux/en/28.%20System%20Logs.md) |
| `LC-036` | [Solaris — Linux Distributions vs Solaris](linux/en/29.%20Solaris%20%E2%80%94%20Linux%20Distributions%20vs%20Solaris.md) |
| `LC-037` | [Shortcuts — Bash Tips & Tricks](linux/en/30.%20Shortcuts%20%E2%80%94%20Bash%20Tips%20%26%20Tricks.md) |
| `LC-071` | [Neovim — Tips & Tricks](linux/Tips%20%26%20Tricks/en/Neovim%20%E2%80%94%20Tips%20%26%20Tricks.md) |

---

## 3. Computer Networking & Protocols (`networking/`)

OSI model, TCP/IP, DNS, ARP, subnetting, wireless security.

| LC-ID | Topic |
|:------|:------|
| `LC-038` | [OSI Modelling](networking/en/OSI%20Modelling.md) |
| `LC-039` | [TCP-IP Architecture & Socket Programming](networking/en/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) |
| `LC-040` | [IP Addressing & Subnetting](networking/en/IP%20Addressing%20%26%20Subnetting.md) |
| `LC-041` | [DNS & Domain Name System Security](networking/en/DNS%20%26%20Domain%20Name%20System%20Security.md) |
| `LC-042` | [ARP & Local Network Attacks](networking/en/ARP%20%26%20Local%20Network%20Attacks.md) |
| `LC-043` | [Wireless 802.11 Security & Attacks](networking/en/Wireless%20802.11%20Security%20%26%20Attacks.md) |

---

## 4. Web Application Security (`web/`)

HTTP/HTTPS, SQLi, XSS, CSRF, SSRF, LFI/RFI, uploads, JWT/session attacks.

| LC-ID | Topic |
|:------|:------|
| `LC-044` | [HTTP & cURL](web/HTTP/en/1.%20HTTP%20%26%20cURL.md) |
| `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/en/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) |
| `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) |
| `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) |
| `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) |
| `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) |
| `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) |
| `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) |
| `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) |
| `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) |

---

## 5. Cryptography & PKI (`cryptography/`)

Symmetric/asymmetric crypto, hashing, PKI, TLS 1.3.

| LC-ID | Topic |
|:------|:------|
| `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/en/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) |
| `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/en/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) |
| `LC-056` | [Hash Functions & Message Authentication](cryptography/en/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) |
| `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) |

---

## 6. Ethical Hacking & Penetration Testing (`ethical-hacking/`)

PTES methodology, Nmap, Metasploit, privilege escalation.

| LC-ID | Topic |
|:------|:------|
| `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/en/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) |
| `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/en/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) |
| `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/en/3.%20Metasploit%20Framework%20%26%20Exploitation.md) |
| `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/en/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) |

---

## 7. Binary Exploitation (`binary-exploitation/`)

Stack buffer overflows, shellcoding, mitigations.

| LC-ID | Topic |
|:------|:------|
| `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/en/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) |

---

## 8. Reverse Engineering & Malware Analysis (`malware-analysis/`)

Static/dynamic triage, sandboxing, x86/x64 assembly.

| LC-ID | Topic |
|:------|:------|
| `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) |
| `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/en/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) |
| `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/en/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) |

---

## 9. Mobile Application Security (`mobile-security/`)

Android internals, sandboxing, Binder IPC, reverse engineering.

| LC-ID | Topic |
|:------|:------|
| `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/en/Android%20Security%20Internals%20%26%20Vulnerabilities.md) |

---

## 10. Security Programming & Tool Development (`programming-security/`)

Offensive Python and Go for tooling.

| LC-ID | Topic |
|:------|:------|
| `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) |

---

## 11. Social Engineering & Human Factors (`social-engineering/`)

Influence principles, vectors, organizational defense.

| LC-ID | Topic |
|:------|:------|
| `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/en/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) |

---

## 12. OSINT (`osint/`)

Intelligence lifecycle, OPSEC, investigation frameworks.

| LC-ID | Topic |
|:------|:------|
| `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/en/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) |

---

## 13. Hardware & IoT Security (`hardware-iot/`)

UART/JTAG/SPI, firmware extraction, CAN bus.

| LC-ID | Topic |
|:------|:------|
| `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/en/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) |

---

## 14. Blue Team & Defensive Security (`blue-team/`)

SOC and log analysis, network monitoring, threat hunting, incident response and forensics.

| LC-ID | Topic |
|:------|:------|
| `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) |
| `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/en/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) |
| `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) |
| `LC-075` | [Incident Response & Digital Forensics](blue-team/en/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) |

---

## 15. Active Directory Security (`active-directory/`)

Domains, domain controllers, objects, Group Policy, trusts.

| LC-ID | Topic |
|:------|:------|
| `LC-076` | [Active Directory Fundamentals](active-directory/en/1.%20Active%20Directory%20Fundamentals.md) |

---

## 16. Cloud Security (`cloud-security/`)

Shared responsibility, IAM, storage, network, logging, auditing.

| LC-ID | Topic |
|:------|:------|
| `LC-077` | [Cloud Security Fundamentals](cloud-security/en/1.%20Cloud%20Security%20Fundamentals.md) |

---

## 17. DevSecOps (`devsecops/`)

Threat modeling, secret scanning, SAST, SCA, DAST, CI pipeline security.

| LC-ID | Topic |
|:------|:------|
| `LC-078` | [DevSecOps Fundamentals](devsecops/en/1.%20DevSecOps%20Fundamentals.md) |

---

## 18. Governance, Risk & Compliance (`grc/`)

Policies, risk management, controls, frameworks, data protection law, audits.

| LC-ID | Topic |
|:------|:------|
| `LC-079` | [GRC Fundamentals](grc/en/1.%20GRC%20Fundamentals.md) |

---

## 19. AI Security (`ai-security/`)

OWASP Top 10 for LLMs, prompt injection, agents, RAG, model supply chain, AI governance.

| LC-ID | Topic |
|:------|:------|
| `LC-080` | [AI & LLM Security Fundamentals](ai-security/en/1.%20AI%20%26%20LLM%20Security%20Fundamentals.md) |

---

## Coverage status

Zero2Root does not cover everything yet. These topics are missing today, so study them from other sources if your career needs them. Each career in [CAREERS.md](CAREERS.md) lists its own gaps.

| Topic | Status | Most affected careers |
|:---|:---|:---|
| Active Directory: attacks, defense, Windows event logs (fundamentals are in LC-076) | partly available | Pentester, Red Team, SOC Analyst |
| Cloud security: IAM in depth, Kubernetes, infrastructure as code (fundamentals are in LC-077) | partly available | Cloud Security Engineer |
| DevSecOps: artifact signing, SLSA, secrets platforms (fundamentals are in LC-078) | partly available | AppSec & DevSecOps Engineer |
| AI and LLM security: model training and poisoning in depth, agent frameworks (fundamentals are in LC-080) | partly available | AppSec, Red Team |
| GRC: implementing ISO 27001, quantitative risk, sector regulations (fundamentals are in LC-079) | partly available | GRC Analyst |
| API security, heap exploitation, fuzzing, iOS | not planned yet | Web pentester, Vulnerability Researcher, Mobile |

---

## Reference library

All material in this repository is written against technical reference books held locally under `~/Documents/Books/`. See [BOOKS.md](BOOKS.md) for the full catalog mapped to each lesson.

---

## Legal disclaimer

All documentation, commands, and attack vectors in this repository are for educational purposes, defensive auditing, and authorized penetration testing only. The author assumes no liability for unauthorized activity, misconfiguration, or damage resulting from the use of this material.

---

## Author and contributions

- Maintainer: `kodoktheGr3at`
- GitHub: [github.com/Kodokthegr3at](https://github.com/Kodokthegr3at)
- Repository: [github.com/Kodokthegr3at/Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
- Feedback, improvements, and pull requests are welcome.
