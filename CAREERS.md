**Language:** [English](CAREERS.md) | [Bahasa Indonesia](CAREERS.id.md) | [日本語](CAREERS.ja.md)

# Zero2Root: Career Paths

> Cyber security is not one job. This page lists the common roles, what each one does day to day, which Zero2Root lessons prepare you for it, and, just as important, what Zero2Root does not cover yet so you know where to look elsewhere.
> This page links only to the English lesson files. The full ordered curriculum is in [ROADMAP.md](ROADMAP.md).

---

## How to read this page

1. Every path starts with the **core foundation** below. Skip lessons you already know.
2. Then follow the lessons for your role, in the order listed.
3. **Coverage** tells you honestly how much of the role Zero2Root teaches today: *good* means most of what a junior needs is here, *partial* means important topics are missing, *minimal* means you will need outside material for most of it.
4. **Good first job** marks roles people commonly get hired into without prior security experience. The others usually come after one or two years in a related job.
5. Hours are study estimates for reading plus hands-on practice, not including the books.

---

## Overview

| Role | What the job is | Good first job | Lessons after the core | Study hours | Coverage |
|:---|:---|:---|:---|:---|:---|
| [SOC Analyst](#soc-analyst) | Watches alerts from many systems, decides which ones are real attacks, and escalates them | yes | 17 | 75-91 | good |
| [Incident Responder & Forensic Analyst (DFIR)](#incident-responder--forensic-analyst-dfir) | Takes over when an attack is confirmed: contains it, collects evidence from disks and memory, rebuilds the timeline, and writes the report | no | 12 | 58-69 | good |
| [Threat Hunter & Detection Engineer](#threat-hunter--detection-engineer) | Writes and tunes the rules that raise alerts, and searches proactively for attackers that slipped past them | no | 9 | 47-57 | good |
| [Penetration Tester](#penetration-tester) | Tests networks and applications with written permission, finds weaknesses before real attackers do, and reports how to fix them | no | 26 | 105-124 | partial |
| [Web Application Pentester & Bug Hunter](#web-application-pentester--bug-hunter) | Focuses on websites and APIs: finds injection, access-control, and session bugs, and reports them to the owner or a bug bounty program | no | 15 | 59-72 | good |
| [Red Team Operator](#red-team-operator) | Plays a realistic attacker over weeks to test whether the blue team notices | no | 24 | 107-131 | partial |
| [Malware Analyst & Reverse Engineer](#malware-analyst--reverse-engineer) | Takes a suspicious file apart to learn what it does, how to detect it, and how to clean up after it | no | 7 | 40-50 | good |
| [Vulnerability Researcher & Exploit Developer](#vulnerability-researcher--exploit-developer) | Finds new bugs in software and proves whether they can be exploited, so vendors can fix them | no | 4 | 25-32 | minimal |
| [Application Security & DevSecOps Engineer](#application-security--devsecops-engineer) | Works with developers so code ships safely: reviews designs and code, and adds security checks to the build pipeline | no | 17 | 69-85 | good |
| [Cloud Security Engineer](#cloud-security-engineer) | Secures accounts, identities, networks, and workloads on AWS, Azure, or Google Cloud | no | 10 | 43-50 | partial |
| [Threat Intelligence & OSINT Analyst](#threat-intelligence--osint-analyst) | Tracks attacker groups and their methods from public and private sources, and turns that into advice the defenders can use | no | 5 | 25-30 | partial |
| [Mobile & IoT Security Specialist](#mobile--iot-security-specialist) | Tests phone apps, smart devices, and their firmware, from the app code down to the circuit board | no | 14 | 66-81 | partial |
| [GRC & Security Compliance Analyst](#grc--security-compliance-analyst) | Manages risk, policies, and audits against standards like ISO 27001 or NIST CSF | yes | 5 | 25-29 | minimal |

---

## Core foundation (all paths)

These lessons are shared by every role: how computers, Linux, and networks work, plus the basics of the web. About 108 to 128 hours.

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-001` | [Expression](basics/en/Expression.md) | Beginner | 2-3h |
| 2 | `LC-002` | [Git — Version Control System](basics/en/Git%20%E2%80%94%20Version%20Control%20System.md) | Beginner | 3-4h |
| 3 | `LC-005` | [Linux File System](basics/OperatingSystem/en/Linux%20File%20System.md) | Beginner | 5-6h |
| 4 | `LC-006` | [Windows File System](basics/OperatingSystem/en/Windows%20File%20System.md) | Beginner | 5-6h |
| 5 | `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/en/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) | Beginner | 3-4h |
| 6 | `LC-009` | [Linux Distributions (Distros)](linux/en/02.%20Linux%20Distributions%20%28Distros%29.md) | Beginner | 2-3h |
| 7 | `LC-010` | [Introduction to Shell](linux/en/03.%20Introduction%20to%20Shell.md) | Beginner | 4-5h |
| 8 | `LC-011` | [Prompt Description & PS1 Customization](linux/en/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) | Beginner | 2h |
| 9 | `LC-012` | [Getting Help — man, --help, apropos](linux/en/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) | Beginner | 2h |
| 10 | `LC-013` | [System Information — Kernel, Hardware & Environment](linux/en/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) | Beginner | 3h |
| 11 | `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/en/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) | Beginner | 2-3h |
| 12 | `LC-015` | [Working with Files & Directories](linux/en/08.%20Working%20with%20Files%20%26%20Directories.md) | Beginner | 3-4h |
| 13 | `LC-016` | [Editing Files — Nano & Vim](linux/en/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) | Beginner | 4-5h |
| 14 | `LC-017` | [Find Files & Directories](linux/en/10.%20Find%20Files%20%26%20Directories.md) | Beginner | 3h |
| 15 | `LC-018` | [File Descriptors & Redirections](linux/en/11.%20File%20Descriptors%20%26%20Redirections.md) | Intermediate | 4h |
| 16 | `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/en/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) | Intermediate | 4-5h |
| 17 | `LC-020` | [Regular Expressions (RegEx)](linux/en/13.%20Regular%20Expressions%20%28RegEx%29.md) | Intermediate | 5-6h |
| 18 | `LC-021` | [Permission Management](linux/en/14.%20Permission%20Management.md) | Intermediate | 4-5h |
| 19 | `LC-022` | [User Management](linux/en/15.%20User%20Management.md) | Intermediate | 4h |
| 20 | `LC-024` | [Service and Process Management](linux/en/17.%20Service%20and%20Process%20Management.md) | Intermediate | 4-5h |
| 21 | `LC-026` | [Network Services](linux/en/19.%20Network%20Services.md) | Intermediate | 4h |
| 22 | `LC-031` | [Linux Networking — Interfaces & Routing](linux/en/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) | Intermediate | 4h |
| 23 | `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/en/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) | Intermediate | 4-5h |
| 24 | `LC-035` | [System Logs](linux/en/28.%20System%20Logs.md) | Intermediate | 3-4h |
| 25 | `LC-038` | [OSI Modelling](networking/en/OSI%20Modelling.md) | Beginner | 6-8h |
| 26 | `LC-039` | [TCP-IP Architecture & Socket Programming](networking/en/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) | Intermediate | 5-6h |
| 27 | `LC-040` | [IP Addressing & Subnetting](networking/en/IP%20Addressing%20%26%20Subnetting.md) | Intermediate | 4-5h |
| 28 | `LC-041` | [DNS & Domain Name System Security](networking/en/DNS%20%26%20Domain%20Name%20System%20Security.md) | Intermediate | 4h |
| 29 | `LC-044` | [HTTP & cURL](web/HTTP/en/1.%20HTTP%20%26%20cURL.md) | Beginner | 3h |
| 30 | `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/en/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) | Beginner | 3h |

---

## SOC Analyst

**What the job is:** Watches alerts from many systems, decides which ones are real attacks, and escalates them. The most common first job in cyber security.

**Good first job:** yes  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/en/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Beginner | 3-4h |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 4 | `LC-034` | [Firewall Setup](linux/en/27.%20Firewall%20Setup.md) | Advanced | 4h |
| 5 | `LC-042` | [ARP & Local Network Attacks](networking/en/ARP%20%26%20Local%20Network%20Attacks.md) | Advanced | 4h |
| 6 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Intermediate | 3-4h |
| 7 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 8 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 9 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/en/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Intermediate | 3-4h |
| 12 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/en/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Intermediate | 4-5h |
| 13 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 14 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/en/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Intermediate | 6-7h |
| 15 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |
| 16 | `LC-075` | [Incident Response & Digital Forensics](blue-team/en/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Advanced | 7-9h |
| 17 | `LC-076` | [Active Directory Fundamentals](active-directory/en/1.%20Active%20Directory%20Fundamentals.md) | Intermediate | 5-6h |

Study time for this path: about 75 to 91 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Active Directory and Windows event logs in depth
- Hands-on SIEM labs with a specific product
- Phishing email analysis as its own lesson
- Cloud logs (AWS CloudTrail, Microsoft 365)

---

## Incident Responder & Forensic Analyst (DFIR)

**What the job is:** Takes over when an attack is confirmed: contains it, collects evidence from disks and memory, rebuilds the timeline, and writes the report.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-007` | [macOS File System](basics/OperatingSystem/en/macOS%20File%20System.md) | Beginner | 4-5h |
| 3 | `LC-028` | [Backup and Restore](linux/en/21.%20Backup%20and%20Restore.md) | Intermediate | 3h |
| 4 | `LC-029` | [File System Management](linux/en/22.%20File%20System%20Management.md) | Intermediate | 4-5h |
| 5 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 6 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Advanced | 5-6h |
| 7 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/en/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Advanced | 5h |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 9 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/en/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Intermediate | 6-7h |
| 10 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |
| 11 | `LC-075` | [Incident Response & Digital Forensics](blue-team/en/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Advanced | 7-9h |
| 12 | `LC-076` | [Active Directory Fundamentals](active-directory/en/1.%20Active%20Directory%20Fundamentals.md) | Intermediate | 5-6h |

Study time for this path: about 58 to 69 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Windows registry and artifact forensics in depth
- Mobile device forensics
- Cloud incident response

---

## Threat Hunter & Detection Engineer

**What the job is:** Writes and tunes the rules that raise alerts, and searches proactively for attackers that slipped past them.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/en/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Advanced | 5-6h |
| 3 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/en/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Advanced | 5-6h |
| 4 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Advanced | 5-6h |
| 5 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/en/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Advanced | 5h |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 7 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 8 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/en/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | Intermediate | 6-7h |
| 9 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |

Study time for this path: about 47 to 57 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Detection-as-code and CI pipelines for rules
- Data engineering for log pipelines

---

## Penetration Tester

**What the job is:** Tests networks and applications with written permission, finds weaknesses before real attackers do, and reports how to fix them.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** partial

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/en/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Beginner | 3-4h |
| 3 | `LC-025` | [Task Scheduling](linux/en/18.%20Task%20Scheduling.md) | Intermediate | 3-4h |
| 4 | `LC-027` | [Working with Web Services](linux/en/20.%20Working%20with%20Web%20Services.md) | Intermediate | 3-4h |
| 5 | `LC-030` | [Containerization](linux/en/23.%20Containerization.md) | Advanced | 4-5h |
| 6 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 7 | `LC-034` | [Firewall Setup](linux/en/27.%20Firewall%20Setup.md) | Advanced | 4h |
| 8 | `LC-042` | [ARP & Local Network Attacks](networking/en/ARP%20%26%20Local%20Network%20Attacks.md) | Advanced | 4h |
| 9 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/en/Wireless%20802.11%20Security%20%26%20Attacks.md) | Advanced | 5h |
| 10 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Intermediate | 3-4h |
| 11 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 12 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 13 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Intermediate | 3h |
| 14 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 15 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 16 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Advanced | 3-4h |
| 17 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 18 | `LC-056` | [Hash Functions & Message Authentication](cryptography/en/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Intermediate | 3-4h |
| 19 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 20 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/en/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Intermediate | 4-5h |
| 21 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/en/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | Intermediate | 4h |
| 22 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/en/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Advanced | 5-6h |
| 23 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/en/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Advanced | 5-6h |
| 24 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 25 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/en/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Intermediate | 5h |
| 26 | `LC-076` | [Active Directory Fundamentals](active-directory/en/1.%20Active%20Directory%20Fundamentals.md) | Intermediate | 5-6h |

Study time for this path: about 105 to 124 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Active Directory attacks and defenses (most internal tests involve AD)
- Writing a pentest report
- Cloud penetration testing

---

## Web Application Pentester & Bug Hunter

**What the job is:** Focuses on websites and APIs: finds injection, access-control, and session bugs, and reports them to the owner or a bug bounty program.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/en/20.%20Working%20with%20Web%20Services.md) | Intermediate | 3-4h |
| 2 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Intermediate | 3-4h |
| 3 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 4 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 5 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Intermediate | 3h |
| 6 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 7 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 8 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Advanced | 3-4h |
| 9 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 10 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/en/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | Intermediate | 4-5h |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/en/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Intermediate | 3-4h |
| 12 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/en/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Intermediate | 4-5h |
| 14 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 15 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/en/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Intermediate | 5h |

Study time for this path: about 59 to 72 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- API security (REST and GraphQL) as its own lesson
- OAuth and SSO flaws in depth
- Insecure deserialization

---

## Red Team Operator

**What the job is:** Plays a realistic attacker over weeks to test whether the blue team notices. Usually reached after a few years of pentesting.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** partial

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/en/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | Beginner | 3-4h |
| 3 | `LC-030` | [Containerization](linux/en/23.%20Containerization.md) | Advanced | 4-5h |
| 4 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 5 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Intermediate | 3-4h |
| 6 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 7 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 8 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Intermediate | 3h |
| 9 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 10 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 11 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Advanced | 3-4h |
| 12 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/en/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | Intermediate | 4-5h |
| 14 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/en/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | Intermediate | 4h |
| 15 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/en/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | Advanced | 5-6h |
| 16 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/en/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | Advanced | 5-6h |
| 17 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/en/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Advanced | 6-8h |
| 18 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/en/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Advanced | 8-10h |
| 19 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 20 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/en/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Intermediate | 4-5h |
| 21 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/en/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Intermediate | 5h |
| 22 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 23 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |
| 24 | `LC-076` | [Active Directory Fundamentals](active-directory/en/1.%20Active%20Directory%20Fundamentals.md) | Intermediate | 5-6h |

Study time for this path: about 107 to 131 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Active Directory attack paths
- Command-and-control (C2) infrastructure and OPSEC
- How endpoint detection works and why attackers try to avoid it

---

## Malware Analyst & Reverse Engineer

**What the job is:** Takes a suspicious file apart to learn what it does, how to detect it, and how to clean up after it.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/en/PowerShell.md) | Beginner | 4-5h |
| 2 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/en/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Advanced | 6-8h |
| 3 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Advanced | 5-6h |
| 4 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/en/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | Advanced | 5h |
| 5 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/en/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Advanced | 8-10h |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 7 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |

Study time for this path: about 40 to 50 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Windows internals in depth
- Unpacking and anti-analysis tricks
- .NET and Android malware

---

## Vulnerability Researcher & Exploit Developer

**What the job is:** Finds new bugs in software and proves whether they can be exploited, so vendors can fix them.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** minimal

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/en/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Advanced | 6-8h |
| 2 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Advanced | 5-6h |
| 3 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/en/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Advanced | 8-10h |
| 4 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |

Study time for this path: about 25 to 32 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Heap exploitation
- Fuzzing
- Kernel and browser exploitation
- Modern mitigations in depth (CFG, CET, sandboxing)

---

## Application Security & DevSecOps Engineer

**What the job is:** Works with developers so code ships safely: reviews designs and code, and adds security checks to the build pipeline.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** good

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/en/20.%20Working%20with%20Web%20Services.md) | Intermediate | 3-4h |
| 2 | `LC-030` | [Containerization](linux/en/23.%20Containerization.md) | Advanced | 4-5h |
| 3 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/en/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | Intermediate | 3-4h |
| 4 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 5 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 6 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Intermediate | 3h |
| 7 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 8 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 9 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Advanced | 3-4h |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 11 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/en/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | Intermediate | 4-5h |
| 12 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/en/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | Intermediate | 4-5h |
| 13 | `LC-056` | [Hash Functions & Message Authentication](cryptography/en/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | Intermediate | 3-4h |
| 14 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 15 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/en/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | Advanced | 6-8h |
| 16 | `LC-077` | [Cloud Security Fundamentals](cloud-security/en/1.%20Cloud%20Security%20Fundamentals.md) | Intermediate | 5-6h |
| 17 | `LC-078` | [DevSecOps Fundamentals](devsecops/en/1.%20DevSecOps%20Fundamentals.md) | Intermediate | 6-7h |

Study time for this path: about 69 to 85 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Threat modeling in depth (data-flow diagrams, attack trees)
- Secure code review for specific languages
- Artifact signing and SLSA build provenance
- Secrets management platforms such as HashiCorp Vault

---

## Cloud Security Engineer

**What the job is:** Secures accounts, identities, networks, and workloads on AWS, Azure, or Google Cloud.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** partial

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/en/20.%20Working%20with%20Web%20Services.md) | Intermediate | 3-4h |
| 2 | `LC-030` | [Containerization](linux/en/23.%20Containerization.md) | Advanced | 4-5h |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 4 | `LC-034` | [Firewall Setup](linux/en/27.%20Firewall%20Setup.md) | Advanced | 4h |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 6 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 7 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 9 | `LC-077` | [Cloud Security Fundamentals](cloud-security/en/1.%20Cloud%20Security%20Fundamentals.md) | Intermediate | 5-6h |
| 10 | `LC-078` | [DevSecOps Fundamentals](devsecops/en/1.%20DevSecOps%20Fundamentals.md) | Intermediate | 6-7h |

Study time for this path: about 43 to 50 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Cloud IAM in depth (policy evaluation, cross-account access, Azure and GCP specifics)
- Kubernetes security
- Infrastructure as code and its misconfigurations
- Cloud incident response and detection in depth

---

## Threat Intelligence & OSINT Analyst

**What the job is:** Tracks attacker groups and their methods from public and private sources, and turns that into advice the defenders can use.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** partial

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/en/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | Advanced | 5-6h |
| 2 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/en/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Intermediate | 4-5h |
| 3 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/en/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | Intermediate | 5h |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 5 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/en/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | Advanced | 6-8h |

Study time for this path: about 25 to 30 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Intelligence frameworks (Diamond Model, kill chain) in depth
- Sharing formats (STIX/TAXII, MISP)
- Writing intelligence reports

---

## Mobile & IoT Security Specialist

**What the job is:** Tests phone apps, smart devices, and their firmware, from the app code down to the circuit board.

**Good first job:** no, usually after 1-2 years in a related role  
**Coverage in Zero2Root:** partial

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/en/Wireless%20802.11%20Security%20%26%20Attacks.md) | Advanced | 5h |
| 2 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/en/1.%20SQL%20Injection%20%28SQLi%29.md) | Intermediate | 5-6h |
| 3 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/en/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | Intermediate | 4-5h |
| 4 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/en/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | Intermediate | 3h |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/en/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | Advanced | 3-4h |
| 6 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/en/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | Advanced | 4-5h |
| 7 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/en/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | Advanced | 3-4h |
| 8 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/en/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | Advanced | 4-5h |
| 9 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/en/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | Intermediate | 4-5h |
| 10 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 11 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/en/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | Advanced | 6-8h |
| 12 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/en/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | Advanced | 8-10h |
| 13 | `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/en/Android%20Security%20Internals%20%26%20Vulnerabilities.md) | Advanced | 6-8h |
| 14 | `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/en/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) | Advanced | 6-8h |

Study time for this path: about 66 to 81 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- iOS security
- Bluetooth Low Energy
- Mobile app traffic interception in depth

---

## GRC & Security Compliance Analyst

**What the job is:** Manages risk, policies, and audits against standards like ISO 27001 or NIST CSF. Less hands-on with tools, more with people and documents.

**Good first job:** yes  
**Coverage in Zero2Root:** minimal

**Lessons, in order (after the core foundation):**

| # | ID | Lesson | Level | Hours |
|:---|:---|:---|:---|:---|
| 1 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/en/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | Advanced | 4h |
| 2 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/en/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | Advanced | 5h |
| 3 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/en/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | Intermediate | 4-5h |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/en/1.%20SOC%20%26%20Log%20Analysis.md) | Beginner | 5-6h |
| 5 | `LC-075` | [Incident Response & Digital Forensics](blue-team/en/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | Advanced | 7-9h |

Study time for this path: about 25 to 29 hours on top of the core foundation.

**Not covered in Zero2Root yet** (study these from other sources):

- Risk assessment methods
- ISO 27001, NIST CSF, and other frameworks
- Indonesian and Japanese data protection law (UU PDP, APPI)
- Audit and evidence collection
