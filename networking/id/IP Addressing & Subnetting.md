# Pengalamatan IP, Subnetting & Routing Jaringan

> **LearnCybersecurity** | Seri Networking Fundamentals
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-040` | **Fase 2:** Networking
> **Estimasi belajar:** 4-5 jam | **Level:** Intermediate
> **Prasyarat:** LC-038
> **Peta buku:** Kurose & Ross, Computer Networking Ch.4; Stallings, Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. IPv4 vs IPv6
2. Representasi biner & aljabar mask
3. Rumus inti CIDR
4. Contoh perhitungan: `192.168.1.0/26`
5. RFC 1918 & rentang khusus
6. Routing: longest prefix match
7. NAT & PAT
8. ICMP & diagnostik
9. Catatan keamanan
10. Cheatsheet

---

## 1. IPv4 vs IPv6

Alamat IP adalah identifier logis pada lapisan jaringan (OSI L3 / TCP/IP Internet layer) yang memungkinkan paket di-route antar jaringan.

| Karakteristik | IPv4 | IPv6 |
|:---|:---|:---|
| Panjang | 32-bit (4 oktet) | 128-bit |
| Notasi | Dotted decimal `192.168.1.1` | Hex `2001:db8::1` |
| Ruang alamat | 2³² ≈ 4.29 × 10⁹ | 2¹²⁸ ≈ 3.4 × 10³⁸ |
| Header | 20–60 B (dengan opsi) | 40 B tetap + extension headers |
| Konfigurasi | Manual / DHCP | SLAAC / DHCPv6 |
| Broadcast | Ada | Tidak ada (memakai multicast/anycast) |

Keterbatasan ruang alamat IPv4 mendorong adopsi CIDR, NAT, dan akhirnya IPv6. Tooling keamanan perlu memahami kedua stack ini, termasuk host dual-stack dan eksposur IPv6 yang kadang tidak disadari administratornya.

---

## 2. Representasi biner & aljabar mask

### 2.1 Oktet

Satu oktet = 8 bit, dengan nilai 0..255:

```text
bit:     b7   b6   b5   b4   b3   b2   b1   b0
nilai:  128   64   32   16    8    4    2    1
```

Untuk mendapat nilai desimalnya, jumlahkan nilai setiap bit yang bernilai 1. Untuk `11000000` hasilnya 128 + 64 = 192.

Contoh: `192` = `11000000`, `168` = `10101000`.

### 2.2 Network mask

Prefix length p (CIDR `/p`) berarti p bit di sebelah kiri adalah bagian **network**, sisanya h=32-p adalah bagian **host** (untuk IPv4):

```text
mask = p angka 1 diikuti (32 - p) angka 0

/24  →  11111111.11111111.11111111.00000000  =  255.255.255.0
```

Operasi inti:

```text
alamat network = alamat AND mask         (semua bit host jadi 0)
broadcast      = alamat OR (NOT mask)    (semua bit host jadi 1)
bagian host    = alamat AND (NOT mask)

Contoh 192.168.1.77/26:  network = 192.168.1.64,  broadcast = 192.168.1.127
```

Dua alamat A,B berada di subnet yang sama jika dan hanya jika:

```text
(A AND mask) = (B AND mask)
```

Dengan kata lain, kedua alamat menghasilkan alamat network yang sama.

---

## 3. Rumus inti CIDR

Misalkan prefix `/p` pada IPv4 (0 ≤ p ≤ 32), dengan h = 32 - p.

| Kuantitas | Rumus |
|:---|:---|
| Ukuran blok (total alamat) | N = 2ʰ = 2³²⁻ᵖ |
| Usable host (subnet klasik) | N_usable = 2ʰ - 2 (kecuali `/31` point-to-point menurut RFC 3021, dan `/32` sebagai host route) |
| Jumlah subnet jika meminjam n bit dari blok induk | 2ⁿ |
| Subnet mask desimal | konversi mask(p) ke 4 oktet |
| Increment / stride antar subnet | 2ʰ pada oktet yang relevan |

**Tabel mask cepat:**

| Prefix | Mask | h | Total | Usable |
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

VLSM mengalokasikan blok yang tidak seragam ukurannya: subnet besar untuk jaringan akses, `/30` atau `/31` untuk link router. Syaratnya, blok tidak boleh overlap dan harus selaras pada boundary 2ʰ (aligned prefix).

Prosedur:

1. Urutkan kebutuhan host dari yang terbesar ke terkecil.
2. Untuk kebutuhan H host, pilih h minimum dengan 2ʰ-2 ≥ H (atau 2ʰ ≥ H untuk kasus khusus seperti link point-to-point).
3. Ambil prefix berikutnya yang masih bebas dan aligned.

---

## 4. Contoh perhitungan: `192.168.1.0/26`

```text
prefix p = 26   →   bit host h = 32 - 26 = 6
total alamat    = 2⁶ = 64
host terpakai   = 64 - 2 = 62   (dikurangi alamat network dan broadcast)
```

Mask: `255.255.255.192` (`11111111.11111111.11111111.11000000`).

Jika `192.168.1.0/24` dipecah menjadi blok `/26`, berarti n=2 bit dipinjam sehingga menghasilkan 2²=4 subnet:

| # | Network | Rentang usable | Broadcast |
|:---:|:---|:---|:---|
| 0 | 192.168.1.0/26 | .1 – .62 | .63 |
| 1 | 192.168.1.64/26 | .65 – .126 | .127 |
| 2 | 192.168.1.128/26 | .129 – .190 | .191 |
| 3 | 192.168.1.192/26 | .193 – .254 | .255 |

Cek alignment: network address harus habis dibagi 64 pada oktet terakhir.

Aturan verifikasi yang selalu berlaku: `broadcast = network + size - 1`, dan subnet berikutnya dimulai dari `network + size`.

---

## 5. RFC 1918 & rentang khusus

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
│  0.0.0.0/8         "this network" / unspecified            │
│  100.64.0.0/10     CGNAT (RFC 6598)                        │
└────────────────────────────────────────────────────────────┘
```

Alamat private tidak unik secara global, boleh overlap antar organisasi. Konektivitas ke Internet publik membutuhkan NAT atau dual-stack publik.

---

## 6. Routing: longest prefix match

Router memilih rute dengan prefix terpanjang yang mencocokkan alamat tujuan.

Contoh: untuk D= `192.168.1.10`, jika tabel routing punya `192.168.0.0/16` via A dan `192.168.1.0/24` via B, router memilih rute `/24` karena lebih spesifik.

Default route: `0.0.0.0/0` untuk IPv4, `::/0` untuk IPv6.

---

## 7. NAT & PAT

NAT (Network Address Translation) memetakan alamat di boundary jaringan, biasanya antara ruang private dan public.

| Tipe | Mapping | Penggunaan |
|:---|:---|:---|
| Static NAT | 1 ke 1 tetap | Server yang perlu IP publik stabil |
| Dynamic NAT | Dari pool publik | Jarang dipakai murni di SOHO |
| PAT / overload | Many ke 1 via port | Setup rumah/kantor tipikal |

Model PAT secara intuitif:

```text
(IP privat, port privat, IP tujuan, port tujuan, proto)  ⇄  (IP publik, port baru SPORT', IP tujuan, port tujuan, proto)
```

State table di perangkat NAT menyimpan SPORT' supaya paket balasan dapat dikembalikan ke host privat yang benar.

Implikasi keamanan: NAT bukan firewall. Jaringan tetap membutuhkan filter stateful, reverse proxy, dan hardening tambahan. NAT juga mempersulit komunikasi end-to-end (VoIP, IPsec); IPv6 mengembalikan addressability langsung antar host, sehingga desain keamanan perlu menyesuaikan.

NAT berguna untuk troubleshooting dan pertimbangan arsitektur, tetapi jangan diperlakukan sebagai mekanisme access-control tersendiri.

---

## 8. ICMP & diagnostik

### Ping

- IPv4: Echo Request Type 8, Echo Reply Type 0.
- Ping mengukur reachability dan sampel RTT, bukan throughput.

**Heuristik TTL / Hop Limit** (kasar, bisa diubah admin):

| Initial TTL yang teramati | Perkiraan OS |
|:---:|:---|
| ~64 | Kebanyakan Linux/Unix |
| ~128 | Kebanyakan Windows |
| ~255 | Kebanyakan perangkat jaringan |

### Traceroute

Traceroute mengirim paket dengan TTL=1,2,3,... secara berurutan. Setiap hop yang men-decrement TTL menjadi 0 membalas dengan ICMP Time Exceeded (Type 11). Dari balasan berurutan ini, path hop-by-hop dapat dibangun, meskipun path tersebut bisa asimetris atau sebagian difilter.

---

## 9. Catatan keamanan

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| IP spoofing | Menyamarkan sumber paket, sering dipakai untuk reflection attack | uRPF, ACL ingress/egress, BCP38 |
| L3 yang terlalu flat | Lateral movement mudah dilakukan jika satu host di-compromise | Segmentasi VLAN/subnet plus firewall east-west |
| Management exposed | SSH/RDP berada di segmen user biasa | VRF/VLAN manajemen terpisah |
| Shadow IPv6 | Host dual-stack yang tidak terpantau | Inventory IPv6, RA Guard |
| Kebijakan ICMP yang terlalu terbuka | Recon dan penyalahgunaan | Rate-limit; jangan blokir semua ICMP secara membabi buta (PMTUD butuh Type 3 Code 4) |

Kebersihan lab: petakan interface dan rute pada mesin milik Anda sendiri (`ip addr`, `ip route`) sebelum bereksperimen dengan routing atau firewall. Kesalahan konfigurasi prefix sering menjadi root cause outage.

---

## 10. Cheatsheet

### Mental math CIDR

- `/24` → 256 alamat, stride 1 di oktet terakhir
- `/25` → 128 alamat, stride 128
- `/26` → 64 alamat, stride 64
- `/27` → 32 alamat, stride 32
- `/28` → 16 alamat, stride 16
- `/30` → 4 alamat, stride 4 (tipikal untuk link point-to-point)

```bash
# ── Inspeksi (host Anda) ──────────────────────────────────────
ip -c addr show
ip route show
ip -4 route get 1.1.1.1
ip neighbor show

# ── Diagnostik ─────────────────────────────────────────────────
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
mtr -n 1.1.1.1

# ── Helper kalkulator subnet ────────────────────────────────────
ipcalc 192.168.1.0/26          # jika terpasang
python3 -c "import ipaddress as i; n=i.ip_network('192.168.1.0/26');
print(n.network_address, n.broadcast_address, n.num_addresses)"
```

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1918, RFC 4632 (CIDR), RFC 3021 (/31), RFC 6598 (CGNAT)
> - `man ip`, `man ping`, `man traceroute`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Edukasi dan lab pada jaringan milik sendiri atau yang sudah berizin.
