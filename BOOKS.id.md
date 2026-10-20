**Bahasa:** [English](BOOKS.md) | [Bahasa Indonesia](BOOKS.id.md) | [日本語](BOOKS.ja.md)

# Perpustakaan Referensi: `~/Documents/Books/`

> **Zero2Root** | Katalog buku lokal yang dipetakan ke ID kurikulum
> 2026 | Semua path relatif terhadap `/home/kodok/Documents/Books/`

Katalog ini memetakan setiap PDF di perpustakaan lokal ke pelajaran Zero2Root. Baca bab yang dirujuk sebelum atau sambil membaca tiap catatan `LC-xxx`.

---

## Linux & Shell

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| Brian Ward, *How Linux Works (3rd Ed.)* | `CyberSec/Linux/203.How Linux Works_ What Every Superuser Should Know.pdf` | LC-005, LC-008-035 | Kernel vs user space, `/proc`/`/sys`, boot, storage, network stack, systemd, security |
| William Shotts, *The Linux Command Line (2nd Ed.)* | `CyberSec/Linux/The Linux Command Line.pdf` | LC-008-020, LC-037, LC-071 | Gramatika shell, navigasi, pipeline, vim, scripting, job control |
| Jeffrey Friedl, *Mastering Regular Expressions (3rd Ed.)* | `CyberSec/Linux/OReilly.Mastering.Regular.Expressions.3rd.Edition.www.EBooksWorld.ir.pdf` | LC-001, LC-020, LC-037 | NFA/DFA, keserakahan, backtracking, ReDoS, pola grep/sed/awk |

---

## Networking

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| Kurose & Ross, *Computer Networking (6th Ed.)* | `CyberSec/Networking/computernetworking.pdf` | LC-038-042, LC-044 | OSI/TCP-IP, delay/loss/throughput, HTTP/DNS, routing, transport layer |
| William Stallings, *Network Security Essentials (4th Ed.)* | `CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf` | LC-033-034, LC-038, LC-041-043, LC-054-057 | Kerahasiaan/integritas/autentikasi, firewall, IDS, TLS, keamanan wireless |
| Christian Benvenuti, *Understanding Linux Network Internals* | `CyberSec/Networking/Understanding Linux Network Internals (2005).pdf` | LC-026, LC-031-032, LC-034 | sk_buff, Netfilter, routing cache, socket layer, interaksi driver |
| W. Richard Stevens, *UNIX Network Programming Vol.1 (3rd Ed.)* | `CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf` | LC-018, LC-026, LC-031, LC-039, LC-067 | Sockets API, state machine TCP, I/O multiplexing, echo server |
| Matthew Gast, *802.11 Wireless Networks (2nd Ed.)* | `CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf` | LC-043 | Tipe frame, handshake 4-way WPA2, PMKID, arsitektur channel |

---

## Keamanan Aplikasi Web

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| Stuttard & Pinto, *The Web Application Hacker's Handbook (2nd Ed.)* | `CyberSec/Web App/The Web Application Hackers Handbook-Honest.pdf` | LC-044-052 | Attack surface HTTP, SQLi, XSS, CSRF, cacat autentikasi, bug logika |
| Michal Zalewski, *The Tangled Web* | `CyberSec/Web App/thetangledweb_ebook.pdf` | LC-044-053 | Model keamanan browser, SOP, CSP, cookie, keunikan web modern |

---

## Kriptografi

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| David Wong, *Real-World Cryptography (2021)* | `CyberSec/Cryptography/Real-World-Cryptography-12.10.2021.-.pdf` | LC-053-057 | Simetris/AEAD, RSA/ECC, hash, tanda tangan digital, TLS 1.3, jebakan praktis |

---

## Ethical Hacking & Exploitation

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| Peter Kim, *The Hacker Playbook 3* | `CyberSec/Ethical Hacking/The Hacker Playbook 3 - Practical Guide To Penetration Testing by Peter Kim.pdf` | LC-058-061 | Recon, scanning, pengiriman exploit, playbook privesc |
| Georgia Weidman, *Penetration Testing* | `CyberSec/Ethical Hacking/Penetration Testing - A hands-on introduction to Hacking.pdf` | LC-058-061 | Setup lab, metodologi, dasar Metasploit, pelaporan |
| *Gray Hat Hacking* | `CyberSec/Handbook/gray-hat-hacking.pdf` | LC-003-004, LC-006, LC-061-062 | Internal OS untuk exploit dev, privesc Windows/Linux |
| Kennedy et al., *Metasploit: The Penetration Tester's Guide* | `CyberSec/Android/Metasploit - The Penetration Tester's Guide.pdf` | LC-060 | Arsitektur MSF, Meterpreter, pengembangan modul |
| *The Shellcoder's Handbook (2nd Ed.)* | `CyberSec/Handbook/Wiley.The.Shellcoders.Handbook.2nd.Edition.Aug.2007.pdf` | LC-062 | Stack overflow, heap, shellcode, bypass proteksi |
| Erickson, *Hacking: The Art of Exploitation* | `CyberSec/Ethical Hacking/Hacking - The Next Generation.pdf` | LC-062 | Memori C, assembly, pola pikir eksploitasi |

---

## Malware & Reverse Engineering

| Buku | Path | ID Kurikulum | Topik teknis utama |
|:-----|:-----|:---------------|:---------------------|
| Sikorski & Honig, *Practical Malware Analysis* | `CyberSec/Malware/practicalmalwareanalysis.pdf` | LC-063-065 | Triase statis/dinamis, format PE, debugging, packer |
| Andriesse, *Practical Binary Analysis* | `CyberSec/Malware/Practical Binary Analysis 1st Edition (2019).pdf` | LC-063-064 | Parsing ELF/PE, pengantar symbolic execution, binary lifting |
| Dang et al., *Practical Reverse Engineering* | `CyberSec/Reverse Engineeering/Practical Reverse Engineering.pdf` | LC-065 | Disassembly x86/x64/ARM, calling convention, obfuskasi |
| *Rootkits and Bootkits* | `CyberSec/Malware/Rootkits and Bootkits - Reversing Modern Malware And Next Generation Threats (2019).pdf` | LC-063+ | Persistence mode-kernel, rantai boot |

---

## Mobile, Pemrograman, OSINT, Hardware

| Buku | Path | ID Kurikulum |
|:-----|:-----|:---------------|
| Elenkov, *Android Security Internals* | `CyberSec/Android/Android_Security_Internals-An_In-Depth_Guide_to_Android_s_Security_Architecture.pdf` | LC-066 |
| Seitz & Arnold, *Black Hat Python (2nd Ed.)* | `CyberSec/Programming/Black Hat Python, 2nd Edition (Justin Seitz Tim Arnold) (Z-Library).pdf` | LC-067 |
| Steele et al., *Black Hat Go* | `CyberSec/Programming/Black Hat Go [Tom Steele, Chris Patten & Dan Kottmann].pdf` | LC-067 |
| Hadnagy, *Social Engineering (2nd Ed.)* | `CyberSec/Social Engineering/socialengineering_thescienceofhumanhacking_2ndedition.pdf` | LC-068 |
| Mitnick, *The Art of Deception* | `CyberSec/Social Engineering/The Art of Deception.pdf` | LC-068 |
| Gray, *Practical Social Engineering* | `CyberSec/Social Engineering/practical_social_engineering_a_primer_for_the_ethical_hacker_171850098x.pdf` | LC-068 |
| Akhgar et al., *OSINT Methods and Tools* | `CyberSec/OSINT/Open Source Intelligence Methods and Tools.pdf` | LC-069 |
| *Hardware Hacking Handbook* | `CyberSec/Hardware/The Hardware Hacking Handbook.pdf` | LC-070 |
| *Practical IoT Hacking* | `CyberSec/Hardware/Practical IoT Hacking_ The Definitive Guide to Attacking the Internet of Things.pdf` | LC-070 |
| *The Car Hacker's Handbook* | `CyberSec/Hardware/thecarhackershandbook.pdf` | LC-070 |
| *IoT Hacker's Handbook (Gupta)* | `CyberSec/Handbook/The IoT Hackers Handbook A Practical Guide to Hacking the Internet of Things by Aditya Gupta (z-lib.org).pdf` | LC-070 |

---

## Dasar-Dasar Pemrograman

| Buku | Path | ID Kurikulum |
|:-----|:-----|:---------------|
| K. N. King, *C Programming: A Modern Approach (2nd Ed.)* | `Programming/C /K. N. King - C Programming_ A Modern Approach Second Edition (2008, W. W. Norton & Company) - libgen.li.pdf` | LC-001, LC-062, LC-065 |
| Al Sweigart, *Automate the Boring Stuff with Python* | `Programming/Python/Automate the Boring Stuff with Python.pdf` | LC-001, LC-067 |
| Scott Meyers, *Effective Modern C++* | `Programming/ C++/Effective-Modern-C++.pdf` | LC-001 |

---

> Lihat [ROADMAP.id.md](ROADMAP.id.md) untuk jalur belajar berurutan dari `LC-001` sampai `LC-075`.
