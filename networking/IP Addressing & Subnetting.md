# 🌐 IP Addressing, Subnetting & Network Routing

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | IPv4 vs IPv6 | Struktur alamat IP | IPv4 vs IPv6 Architecture | IPv4とIPv6の構造比較 |
| 2 | IP Classes & RFC 1918 | Private IP vs Public IP | IP Classes & RFC 1918 Private Scopes | IPクラスとRFC 1918プライベートIP |
| 3 | Subnetting & CIDR | Subnet mask & perhitungan VLSM | Subnetting, CIDR & VLSM Mathematics | サブネット化とCIDR計算 |
| 4 | NAT & PAT | Mekanisme translasi alamat | NAT & PAT Network Address Translation | NATとPATのアドレス変換機構 |
| 5 | ICMP & Diagnostics | Diagnostik ping & traceroute | ICMP Diagnostics, Ping & Traceroute | ICMPとネットワーク診断ツール |
| 6 | Security Note | IP spoofing & pivot routing | IP Spoofing, Subnet Pivoting & Evasion | IPスプーフィングとピボッティング |
| 7 | Cheatsheet | Referensi subnetting & IP | Subnetting Quick Reference & CIDR Table | サブネット計算チートシート |

---

## 1. 🔢 IPv4 vs IPv6 Architecture

### 🇮🇩 Bahasa Indonesia
**IP Address (Internet Protocol Address)** adalah identifier numerik logis yang diberikan kepada setiap perangkat yang terhubung ke jaringan komputer berbasis IP.

| Karakteristik | IPv4 (Internet Protocol v4) | IPv6 (Internet Protocol v6) |
|:---|:---|:---|
| **Panjang Alamat** | 32-bit (4 Oktet) | 128-bit (8 Hexadectet) |
| **Format Penulisan**| Desimal bertitik (`192.168.1.1`) | Heksadesimal bertitik-dua (`2001:0db8:85a3::8a2e:0370:7334`) |
| **Total Ruang Alamat**| ~4,29 Miliar ($2^{32}$) | $3.4 \times 10^{38}$ ($2^{128}$) |
| **Konfigurasi** | Manual / DHCP | SLAAC (Stateless) / DHCPv6 |
| **Header Size** | 20 – 60 Bytes (Variable) | 40 Bytes (Fixed, efisien) |
| **Keamanan** | Opsional (IPsec) | Terintegrasi natively dalam standar |

---

## 2. 🏢 IP Classes & RFC 1918 Private IP Ranges

```
┌────────────────────────────────────────────────────────────────────────┐
│                   RFC 1918 PRIVATE IP ADDRESS BLOCKS                   │
├─────────┬───────────────────────────────┬──────────────┬───────────────┤
│ Class   │ IP Range                      │ CIDR Prefix  │ Total Hosts   │
├─────────┼───────────────────────────────┼──────────────┼───────────────┤
│ Class A │ 10.0.0.0 – 10.255.255.255     │ 10.0.0.0/8   │ 16,777,216    │
│ Class B │ 172.16.0.0 – 172.31.255.255   │ 172.16.0.0/12│ 1,048,576     │
│ Class C │ 192.168.0.0 – 192.168.255.255 │ 192.168.0.0/16│ 65,536       │
├─────────┴───────────────────────────────┴──────────────┴───────────────┤
│ Special: 127.0.0.0/8 (Loopback / Localhost)                            │
│ Special: 169.254.0.0/16 (APIPA / Link-Local)                           │
│ Special: 224.0.0.0/4 (Class D Multicast)                               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. 🧮 Subnetting, CIDR & Subnet Calculation

### 🇮🇩 Bahasa Indonesia
**Subnetting** adalah proses membagi satu blok jaringan besar menjadi beberapa sub-jaringan yang lebih kecil (*subnets*).
**CIDR (Classless Inter-Domain Routing)** menggunakan notasi `/prefix` (contoh: `/24`) untuk menentukan berapa bit yang digunakan sebagai **Network ID** dan sisanya sebagai **Host ID**.

- **Rumus Jumlah Subnet**: $2^n$ (di mana $n$ = jumlah bit yang dipinjam dari host)
- **Rumus Jumlah Usable Host**: $2^h - 2$ (di mana $h$ = sisa bit host; dikurangi 2 untuk *Network Address* dan *Broadcast Address*).

```
Contoh Subnetting 192.168.1.0/26:
Prefix: /26 -> Subnet Mask: 255.255.255.192
Sisa Bit Host (h) = 32 - 26 = 6 bit
Total Usable Host = 2^6 - 2 = 64 - 2 = 62 host per subnet

Subnet 1:
- Network Address  : 192.168.1.0
- Usable Host Range: 192.168.1.1 - 192.168.1.62
- Broadcast Address: 192.168.1.63
```

---

## 4. 🔄 NAT (Network Address Translation) & PAT

### 🇮🇩 Bahasa Indonesia
**NAT** memungkinkan beberapa host dengan alamat IP private RFC 1918 untuk berbagi satu (atau beberapa) alamat IP publik untuk mengakses Internet:
1. **Static NAT**: Pemetaan 1-ke-1 tetap antara satu IP private dan satu IP publik.
2. **Dynamic NAT**: Pemetaan dari kolam (*pool*) IP publik yang tersedia.
3. **PAT (Port Address Translation / NAT Overload)**: Ribuan IP private berbagi **satu IP publik tunggal**, dibedakan berdasarkan **nomor Source Port unik**.

---

## 5. 📡 ICMP & Network Diagnostics (`ping`, `traceroute`)

### 🛠️ ICMP Telemetry & Reconnaissance
- **`ping` (Echo Request Type 8 / Echo Reply Type 0)**: Menguji konektivitas end-to-end dan latensi (RTT).
  - *TTL Inspection (OS Fingerprinting)*:
    - `TTL = 64` → Linux / Unix host
    - `TTL = 128` → Windows host
    - `TTL = 255` → Cisco / Network Switch
- **`traceroute` / `tracepath`**: Memetakan rute hop-by-hop dengan mengirim paket UDP/ICMP dengan nilai TTL yang bertambah secara inkremental ($TTL = 1, 2, 3...$). Setiap router yang mengurangi TTL menjadi 0 akan mengembalikan paket `ICMP Time Exceeded (Type 11)`.

---

## 6. 🔐 Security Notes — Pivoting & Network Recon

### 1. Subnet Discovery & Local Pivoting
Ketika pentester mendapatkan shell awal (*foothold*) pada target Linux/Windows:
- Cek semua network interfaces: `ip addr` atau `ifconfig`
- Cek routing table lokal: `ip route` atau `netstat -rn`
- Jika ditemukan interface internal kedua (misal `10.10.10.5/24` selain `192.168.1.50`), mesin target dapat dijadikan **Pivot Jump Host** menggunakan SSH Dynamic Port Forwarding (`ssh -D 1080`) atau `chisel` untuk menyerang subnet internal yang tersembunyi.

---

## 7. 🧠 Quick Reference Cheatsheet

```bash
# ── IP ADDRESS & ROUTE INSPECTION ────────────────────────────
ip -c addr show               # Show IP addresses with color highlights
ip route show                 # Display kernel routing table
ip neighbor show              # Display ARP cache neighbors

# ── NETWORK DIAGNOSTICS ──────────────────────────────────────
ping -c 4 8.8.8.8             # Send 4 ICMP echo requests
traceroute -n 8.8.8.8         # Trace path without DNS resolution
mtr 8.8.8.8                   # Interactive real-time traceroute

# ── SUBNET SCANNING (NMAP) ───────────────────────────────────
nmap -sn 192.168.1.0/24       # Ping sweep entire /24 subnet
nmap -PR -sn 192.168.1.0/24   # ARP ping sweep (Local subnet only)
```

---

> 📚 **References & Book Sources:**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach (6th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Christian Benvenuti — *Understanding Linux Network Internals* (`~/Documents/Books/CyberSec/Networking/`)
> - William Stallings — *Network Security Essentials: Applications and Standards (4th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Peter Kim — *The Hacker Playbook 3: Practical Guide To Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - `man ip`, `man ping`, `man traceroute`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
