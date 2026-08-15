# 🌐 DNS & Domain Name System Security

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | DNS Hierarchy | Hierarki & arsitektur DNS | DNS Architecture & Tree Hierarchy | DNSの階層構造とアーキテクチャ |
| 2 | Record Types | Jenis-jenis DNS record | DNS Record Types (A, AAAA, MX, TXT...) | 主要なDNSレコードの種類 |
| 3 | Query Resolution | Resolusi recursive vs iterative | Recursive vs Iterative Resolution | 再帰的問い合わせと反復問い合わせ |
| 4 | DNS Reconnaissance | Teknik rekon DNS & zone transfer | DNS Recon & AXFR Zone Transfers | DNS偵察とゾーン転送攻撃 |
| 5 | Attacks & Exploits | Serangan DNS poisoning & DoH/DoT | DNS Poisoning, Amplification & DoH/DoT | DNSキャッシュポイズニングと増幅攻撃 |
| 6 | Cheatsheet | Cheatsheet perintah `dig` & `nslookup` | DNS Query Commands Cheatsheet | digおよびnslookupチートシート |

---

## 1. 🌲 DNS Architecture & Tree Hierarchy

### 🇮🇩 Bahasa Indonesia
**DNS (Domain Name System)** adalah buku telepon internet yang menerjemahkan nama domain yang mudah diingat manusia (seperti `example.com`) menjadi alamat IP numerik (seperti `93.184.216.34`) yang dimengerti mesin. Berjalan pada port **53 UDP/TCP**.

```
                           [ . ] Root Domain (Root Nameservers: a.root-servers.net - m.root-servers.net)
                                 │
         ┌───────────────────────┴───────────────────────┐
      [ .com ]                                        [ .org ]     Top-Level Domain (TLD)
         │                                               │
   [ example.com ]                                [ wikipedia.org ] Second-Level Domain (SLD)
         │                                               │
   [ api.example.com ]                             [ en.wikipedia.org ] Subdomain
```

---

## 2. 📋 Core DNS Record Types

| Record Type | Description / Fungsi | Contoh Penggunaan | Cybersecurity Significance |
|:---|:---|:---|:---|
| **A** | Address: Memetakan hostname ke IPv4 | `example.com -> 93.184.216.34` | Target pemetaan IP target dan vHost |
| **AAAA** | IPv6 Address: Memetakan hostname ke IPv6 | `example.com -> 2606:2800:220:1:...` | Mengungkap interface IPv6 yang sering lupa difirewall |
| **CNAME** | Canonical Name: Alias ke domain lain | `www.example.com -> example.com` | **Subdomain Takeover** jika CNAME mengarah ke cloud bucket mati |
| **MX** | Mail Exchanger: Server email domain | `example.com -> mail.example.com` | Mengungkap penyedia email & mail server vulnerability |
| **TXT** | Text: Metadata arbitrer, SPF, DKIM, DMARC | `v=spf1 include:_spf.google.com ~all` | Verifikasi kepemilikan, email spoofing protection, DNS tunneling |
| **NS** | Nameserver: Server otoritatif domain | `example.com -> ns1.example.com` | Mengidentifikasi DNS provider & target AXFR |
| **SOA** | Start of Authority: Info administratif zona | `ns1.example.com admin.example.com 20260101` | Serial number, refresh timer, zone administrator |
| **PTR** | Pointer: Reverse DNS (IP ke Hostname) | `34.216.184.93.in-addr.arpa -> example.com`| Reverse lookup untuk menemukan hidden hosts |

---

## 3. 🔍 DNS Query Resolution Workflow

```
Client (Stub Resolver)
  │
  ├── 1. Query: "What is IP of target.com?" ─────────────> Local Recursive Resolver (8.8.8.8 / 1.1.1.1)
  │                                                               │
  │                                                               ├── 2. Query Root: [ . ] ────> Root DNS Server
  │                                                               │<── 3. Refer to .com TLD ────┘
  │                                                               │
  │                                                               ├── 4. Query TLD: [ .com ] ──> TLD Server
  │                                                               │<── 5. Refer to ns1.target.com
  │                                                               │
  │                                                               ├── 6. Query Authoritative ──> Authoritative Nameserver
  │                                                               │<── 7. Answer: 203.0.113.10 ─┘
  │<── 8. Return IP: 203.0.113.10 (Cached) ───────────────────────┘
```

---

## 4. 🎯 DNS Reconnaissance & Zone Transfer (AXFR)

### 🇮🇩 Bahasa Indonesia
**DNS Zone Transfer (AXFR)** adalah mekanisme replikasi seluruh database DNS dari master server ke slave server via TCP port 53. Jika server salah dikonfigurasi (*misconfiguration*) dan mengizinkan query AXFR dari sembarang IP publik, penyerang bisa mengunduh **seluruh daftar subdomain internal dan IP private** perusahaan dalam 1 detik!

```bash
# ── ATTEMPTING DNS ZONE TRANSFER (AXFR) ──────────────────────
# 1. Find authoritative nameservers
dig ns target.com +short

# 2. Query AXFR against each nameserver
dig axfr @ns1.target.com target.com

# Using host utility
host -l target.com ns1.target.com
```

---

## 5. 🔐 Security Notes — DNS Attack Vectors

### 1. DNS Cache Poisoning (Kaminsky Attack)
Penyerang menyuntikkan respons DNS palsu ke dalam cache *recursive resolver* lokal. Ketika pengguna mencoba membuka `bank.com`, resolver yang telah teracuni akan mengarahkan korban ke IP website phishing milik penyerang.
- **Mitigasi**: Implementasi **DNSSEC (DNS Security Extensions)** dengan tanda tangan digital kriptografi.

### 2. DNS Amplification DDoS
Penyerang mengirimkan query `ANY` atau `TXT` berukuran besar ke *Open DNS Resolvers* dengan memalsukan IP sumber (*IP spoofing*) menjadi IP korban. Respons DNS berukuran 50–100x lebih besar akan membanjiri bandwidth korban.

### 3. DNS Tunneling (C2 Data Exfiltration)
Penyerang menggunakan subdomain terenkripsi (misal: `base64data.c2.attacker.com`) dalam query TXT/A untuk menyelundupkan data rahasia keluar jaringan atau membangun saluran komunikasi *Command & Control* (C2) melewati firewall.

---

## 6. 🧠 Quick Reference Cheatsheet

```bash
# ── DIG COMMAND WORKFLOWS ────────────────────────────────────
dig target.com A +short        # Fast IPv4 lookup
dig target.com MX +noall +answer # Query Mail servers
dig target.com TXT             # Query SPF, DKIM & TXT records
dig @1.1.1.1 target.com ANY    # Query all records from Cloudflare DNS
dig -x 192.168.1.1             # Reverse DNS lookup (PTR)

# ── SUBDOMAIN ENUMERATION ────────────────────────────────────
dnsrecon -d target.com -t brt -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
fierce --domain target.com
```

---

> 📚 **References & Book Sources:**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach (6th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - William Stallings — *Network Security Essentials: Applications and Standards (4th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Peter Kim — *The Hacker Playbook 3: Practical Guide To Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Babak Akhgar et al. — *Open Source Intelligence Methods and Tools* (`~/Documents/Books/CyberSec/OSINT/`)
> - `man dig`, `man nslookup`, `man 5 resolv.conf`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
