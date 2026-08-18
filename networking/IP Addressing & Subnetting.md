# 🌐 IP Addressing, Subnetting & Network Routing

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Kurose & Ross — *Computer Networking*; Stallings — *Network Security Essentials*; Benvenuti — *Understanding Linux Network Internals*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-040` | **Phase 2:** Networking  
> **Est. study:** 4-5h | **Level:** Intermediate  
> **Prerequisites:** LC-038  
> **Book map:** Kurose & Ross Â Computer Networking Ch.4; Stallings Â Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | IPv4 vs IPv6 | Struktur & ruang alamat | Address architecture | アドレス体系 |
| 2 | Binary & Masks | Representasi bit & mask | Bit math & masks | ビットとマスク |
| 3 | CIDR Formulas | Rumus prefix/host/subnet | CIDR mathematics | CIDRの数式 |
| 4 | Worked Examples | Latihan /26, VLSM | Step-by-step examples | 計算例 |
| 5 | RFC 1918 & Special | Private & khusus | Private & special ranges | 特殊アドレス |
| 6 | Routing Lookup | Longest prefix match | LPM routing | 最長一致 |
| 7 | NAT & PAT | Translasi alamat | Address translation | アドレス変換 |
| 8 | ICMP Diagnostics | Ping & traceroute | Reachability tools | 疎通確認 |
| 9 | Security Notes | Spoofing & segmentasi | Threats & defense | 脅威と防御 |
| 10 | Cheatsheet | Tabel CIDR & perintah | CIDR table & CLI | チートシート |

---

## 1. 🔢 IPv4 vs IPv6 Architecture

### 🇮🇩 Bahasa Indonesia
**Alamat IP** adalah identifier logis pada lapisan jaringan (OSI L3 / TCP/IP Internet layer) agar paket dapat di-*route* antar jaringan.

| Karakteristik | IPv4 | IPv6 |
|:---|:---|:---|
| Panjang | 32-bit (4 oktet) | 128-bit |
| Notasi | Dotted decimal `192.168.1.1` | Hex `2001:db8::1` |
| Ruang | $2^{32} \approx 4.29\times 10^9$ | $2^{128} \approx 3.4\times 10^{38}$ |
| Header | 20–60 B (opsi) | 40 B fixed + extension headers |
| Konfigurasi | Manual / DHCP | SLAAC / DHCPv6 |
| Broadcast | Ada | Tidak (multicast/anycast) |

### 🇬🇧 English
IPv4 exhaustion drove **CIDR**, **NAT**, and ultimately **IPv6**. Security tooling must understand both stacks (dual-stack hosts, IPv6 leftover exposure).

### 日本語
IPv4枯渇がCIDR・NAT・IPv6導入を加速しました。デュアルスタック環境では両スタックの可視化が重要です。

---

## 2. 🧮 Binary Representation & Mask Algebra

### 2.1 Oktet
Satu oktet $= 8$ bit, nilai $0..255$:

$$
v = b_7\cdot 2^7 + b_6\cdot 2^6 + \cdots + b_0\cdot 2^0
$$

Contoh: `192` = `11000000`, `168` = `10101000`.

### 2.2 Network mask
Prefix length $p$ (CIDR `/p`) berarti $p$ bit kiri = **network**, sisanya $h=32-p$ = **host** (IPv4):

$$
\mathsf{mask} = \underbrace{1\ldots 1}_{p}\,\underbrace{0\ldots 0}_{32-p}
$$

Operasi inti:

$$
\begin{aligned}
\mathsf{NetworkAddress}(A,p) &= A \land \mathsf{mask}(p) \\
\mathsf{Broadcast}(A,p) &= A \lor \neg\mathsf{mask}(p) \\
\mathsf{HostBits}(A,p) &= A \land \neg\mathsf{mask}(p)
\end{aligned}
$$

Dua alamat $A,B$ berada di subnet sama iff:

$$
A \land \mathsf{mask}(p) = B \land \mathsf{mask}(p)
$$

---

## 3. 📐 CIDR Core Formulas

Misalkan prefix `/p` pada IPv4 ($0 \le p \le 32$), $h = 32 - p$.

| Kuantitas | Rumus |
|:---|:---|
| Ukuran blok (alamat total) | $N = 2^{h} = 2^{32-p}$ |
| Usable host (subnet klasik) | $N_{\text{usable}} = 2^{h} - 2$ (kecuali `/31` point-to-point RFC 3021, `/32` host route) |
| Jumlah subnet jika meminjam $n$ bit dari blok induk | $2^{n}$ |
| Subnet mask desimal | konversi $\mathsf{mask}(p)$ ke 4 oktet |
| Increment / stride antar subnet | $2^{h}$ pada oktet yang relevan |

**Contoh mask cepat:**

| Prefix | Mask | $h$ | Total | Usable |
|:---:|:---|:---:|:---:|:---:|
| /8 | 255.0.0.0 | 24 | 16,777,216 | 16,777,214 |
| /16 | 255.255.0.0 | 16 | 65,536 | 65,534 |
| /24 | 255.255.255.0 | 8 | 256 | 254 |
| /25 | 255.255.255.128 | 7 | 128 | 126 |
| /26 | 255.255.255.192 | 6 | 64 | 62 |
| /27 | 255.255.255.224 | 5 | 32 | 30 |
| /28 | 255.255.255.240 | 4 | 16 | 14 |
| /30 | 255.255.255.252 | 2 | 4 | 2 |
| /32 | 255.255.255.255 | 0 | 1 | 1 (host) |

### VLSM (Variable Length Subnet Mask)
Alokasikan blok **tidak seragam**: subnet besar untuk akses, `/30` atau `/31` untuk link router. Syarat: blok **tidak overlap** dan selaras pada boundary $2^{h}$ (aligned prefix).

Prosedur:
1. Urutkan kebutuhan host menurun.
2. Untuk kebutuhan $H$ host, pilih $h$ minimum dengan $2^{h}-2 \ge H$ (atau $2^{h}\ge H$ untuk kasus khusus).
3. Ambil prefix berikutnya yang masih free & aligned.

---

## 4. ✅ Worked Example — `192.168.1.0/26`

### 🇮🇩 Bahasa Indonesia
$$
p=26,\quad h=6,\quad N=2^6=64,\quad N_{\text{usable}}=62
$$

Mask: `255.255.255.192` (`11111111.11111111.11111111.11000000`).

Jika memecah `192.168.1.0/24` menjadi `/26`, $n=2$ bit dipinjam ⇒ $2^2=4$ subnet:

| # | Network | Usable range | Broadcast |
|:---:|:---|:---|:---|
| 0 | 192.168.1.0/26 | .1 – .62 | .63 |
| 1 | 192.168.1.64/26 | .65 – .126 | .127 |
| 2 | 192.168.1.128/26 | .129 – .190 | .191 |
| 3 | 192.168.1.192/26 | .193 – .254 | .255 |

**Cek alignment:** network address harus habis dibagi 64 pada oktet terakhir.

### 🇬🇧 English
Always verify: `broadcast = network + size - 1`, and the next subnet starts at `network + size`.

### 日本語
`broadcast = network + size - 1`、次のサブネットは `network + size` から始まります。

---

## 5. 🏢 RFC 1918 Private & Special-Use Ranges

```
┌────────────────────────────────────────────────────────────┐
│ RFC 1918 PRIVATE BLOCKS                                    │
│  10.0.0.0/8        (10.0.0.0 – 10.255.255.255)             │
│  172.16.0.0/12     (172.16.0.0 – 172.31.255.255)           │
│  192.168.0.0/16    (192.168.0.0 – 192.168.255.255)         │
├────────────────────────────────────────────────────────────┤
│ SPECIAL                                                    │
│  127.0.0.0/8       loopback                                │
│  169.254.0.0/16    link-local (APIPA)                      │
│  224.0.0.0/4       IPv4 multicast                          │
│  0.0.0.0/8         “this network” / unspecified            │
│  100.64.0.0/10     CGNAT (RFC 6598)                        │
└────────────────────────────────────────────────────────────┘
```

Private addresses **tidak** unik global — boleh overlap antar organisasi; konektivitas Internet membutuhkan NAT atau dual-stack publik.

---

## 6. 🗺️ Routing — Longest Prefix Match (LPM)

Router memilih rute dengan **prefix terpanjang** yang mencocokkan destinasi:

$$
\mathsf{route}(D) = \arg\max_{r:\; D\in r.\mathsf{prefix}} |r.p|
$$

Contoh: untuk $D=$ `192.168.1.10`, jika tabel punya `192.168.0.0/16` via A dan `192.168.1.0/24` via B ⇒ pilih **/24** (lebih spesifik).

Default route: `0.0.0.0/0` (IPv4) / `::/0` (IPv6).

---

## 7. 🔄 NAT & PAT

### 🇮🇩 Bahasa Indonesia
**NAT** memetakan alamat di boundary (biasanya private ↔ public).

| Tipe | Mapping | Penggunaan |
|:---|:---|:---|
| Static NAT | 1↔1 tetap | Server yang perlu IP publik stabil |
| Dynamic NAT | pool publik | Jarang murni di SOHO |
| PAT / overload | many↔1 via **port** | Rumah/kantor tipikal |

Model PAT (intuisi):

$$
(sip, sport, dip, dport, proto) \;\leftrightarrow\; (SIP_{pub}, SPORT', dip, dport, proto)
$$

State table di NAT device mengingat $SPORT'$ agar reply kembali ke host privat benar.

**Implikasi keamanan:** NAT **bukan** firewall. Tetap butuh filter stateful, reverse proxy, dan hardening. NAT juga mempersulit end-to-end (VoIP, IPsec) — IPv6 mengembalikan addressability.

### 🇬🇧 English
Understand NAT for troubleshooting and architecture; do not treat it as an access-control mechanism by itself.

### 日本語
NATは到達性の都合であり、単体ではアクセス制御になりません。ファイアウォールは別途必要です。

---

## 8. 📡 ICMP & Diagnostics

### Ping
- IPv4: Echo Request **Type 8** / Reply **Type 0**
- Mengukur reachability & RTT sampel (bukan throughput).

**TTL / Hop Limit heuristics** (kasar, bisa diubah admin):
| Initial TTL seen | Hint OS |
|:---:|:---|
| ~64 | Many Linux/Unix |
| ~128 | Many Windows |
| ~255 | Many network devices |

### Traceroute
Kirim paket dengan $TTL=1,2,3,\ldots$; setiap hop yang men-decrement ke 0 membalas **ICMP Time Exceeded (Type 11)**. Membangun path hop-by-hop (bisa asymmetris / difilter).

---

## 9. 🔐 Security Notes — Defense-Oriented

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| IP spoofing | Menyamarkan sumber (sering dengan reflection) | uRPF, ingress/egress ACL, BCP38 |
| Overly flat L3 | Lateral movement mudah jika host compromised | Segmentasi VLAN/subnet + firewall east-west |
| Exposed management | SSH/RDP di segmen user | Mgmt VRF/VLAN terpisah |
| Shadow IPv6 | Host dual-stack tak terawasi | Inventory IPv6, RA Guard |
| Open ICMP policy | Recon & abuse | Rate-limit; jangan buta-blok semua ICMP (PMTUD butuh Type 3 Code 4) |

**Lab hygiene:** petakan interface & rute pada mesin **milik Anda** (`ip addr`, `ip route`) sebelum eksperimen routing/firewall — salah konfigurasi prefix sering jadi root cause outage.

---

## 10. 🧠 Cheatsheet

### CIDR mental math
- `/24` → 256 alamat, stride `1` di oktet terakhir  
- `/25` → 128, stride 128  
- `/26` → 64, stride 64  
- `/27` → 32, stride 32  
- `/28` → 16, stride 16  
- `/30` → 4, stride 4 (link tipikal)

```bash
# ── Inspection (host Anda) ───────────────────────────────────
ip -c addr show
ip route show
ip -4 route get 1.1.1.1
ip neighbor show

# ── Diagnostics ──────────────────────────────────────────────
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
mtr -n 1.1.1.1

# ── Subnet calculator helpers ────────────────────────────────
ipcalc 192.168.1.0/26          # jika terpasang
python3 -c "import ipaddress as i; n=i.ip_network('192.168.1.0/26');
print(n.network_address, n.broadcast_address, n.num_addresses)"
```

---

> 📚 **References & Book Sources**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach* — `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti — *Understanding Linux Network Internals* — `~/Documents/Books/CyberSec/Networking/`
> - William Stallings — *Network Security Essentials (4th Edition)* — `~/Documents/Books/CyberSec/Networking/`
> - RFC 1918, RFC 4632 (CIDR), RFC 3021 (/31), RFC 6598 (CGNAT)
> - `man ip`, `man ping`, `man traceroute`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & lab pada jaringan milik sendiri / berizin.
