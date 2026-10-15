# Pengalamatan IP, Subnetting & Routing Jaringan

> **LearnCybersecurity** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-040` | **Fase 2:** Networking
> **Estimasi belajar:** 4-5 jam | **Level:** Menengah
> **Prasyarat:** LC-038
> **Peta buku:** Kurose & Ross, Computer Networking Ch.4; Stallings, Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. IPv4 vs IPv6
2. Membaca alamat dalam biner
3. Subnet mask dan CIDR
4. Contoh: memecah sebuah jaringan
5. Rentang alamat privat dan khusus
6. Cara router memilih jalur
7. NAT: berbagi satu alamat publik
8. ICMP, ping, dan traceroute
9. Catatan keamanan
10. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Alamat IP | Alamat logis sebuah perangkat di jaringan, misalnya `192.168.1.10` |
| Oktet | Salah satu dari empat angka di alamat IPv4 (masing-masing 8 bit, 0–255) |
| Subnet | Potongan lebih kecil yang diiris dari jaringan yang lebih besar |
| Subnet mask | Penanda yang menyatakan bagian mana dari alamat itu "network" dan mana "host" |
| CIDR `/n` | Cara singkat menulis mask: `/24` berarti 24 bit pertama adalah bagian network |
| Alamat network | Alamat pertama di sebuah subnet; menamai subnet itu sendiri |
| Alamat broadcast | Alamat terakhir di sebuah subnet; pesan untuk semua yang ada di dalamnya |
| Gateway | Router yang dituju perangkat saat tujuannya ada di jaringan lain |
| NAT | Membuat banyak perangkat privat berbagi satu alamat IP publik |
| Alamat privat | Alamat (seperti `192.168.x.x`) yang hanya bisa dipakai di jaringan lokal, bukan di Internet publik |

---

## 1. IPv4 vs IPv6

**Alamat IP** adalah nama logis yang dipakai perangkat di jaringan (OSI Layer 3). Inilah yang memungkinkan sebuah paket diarahkan dari satu jaringan ke jaringan lain.

| | IPv4 | IPv6 |
|:---|:---|:---|
| Panjang | 32 bit | 128 bit |
| Bentuknya | `192.168.1.1` | `2001:db8::1` |
| Jumlah alamat | sekitar 4,3 miliar | sekitar 3,4 × 10³⁸ (praktis tak terbatas) |
| Pengaturan | manual atau DHCP | otomatis (SLAAC) atau DHCPv6 |
| Broadcast | ada | tidak (pakai multicast) |

IPv4 kehabisan alamat, dan itulah kenapa NAT (Bagian 7) lalu akhirnya IPv6 muncul. Alat keamanan perlu memahami keduanya, karena sebuah perangkat sering punya **keduanya sekaligus** (dual-stack), dan alamat IPv6 yang tak terpantau mudah terlupakan.

---

## 2. Membaca Alamat dalam Biner

Tiap dari keempat angka di alamat IPv4 (tiap **oktet**) sebenarnya adalah 8 bit. Tiap bit mewakili sebuah nilai:

```text
bit:     b7   b6   b5   b4   b3   b2   b1   b0
nilai:  128   64   32   16    8    4    2    1
```

Untuk mengubah bit menjadi angka desimal, jumlahkan nilai di mana bit-nya 1:

```text
11000000  →  128 + 64            = 192
10101000  →  128 +    32 + 8     = 168
```

Jadi `11000000.10101000.00000001.00000001` hanyalah `192.168.1.1`. Subnetting intinya soal di mana kamu menarik garis di 32 bit itu.

---

## 3. Subnet Mask dan CIDR

Sebuah alamat punya dua bagian: bagian **network** (aku ada di jaringan mana?) dan bagian **host** (aku perangkat yang mana?). **Subnet mask** menandai batasnya. Dalam notasi CIDR, `/n` berarti "n bit pertama adalah network, sisanya host."

```text
/24  →  11111111.11111111.11111111.00000000  =  255.255.255.0
        └────── 24 bit network ───────┘└ 8 bit host ┘
```

Dari mask, kamu bisa menghitung tiga alamat kunci sebuah subnet:

```text
alamat network = alamat terendah (semua bit host 0)  → menamai subnet
broadcast      = alamat tertinggi (semua bit host 1) → "semua yang di sini"
host terpakai  = semua yang di antaranya

Contoh, 192.168.1.0/24:
  network   = 192.168.1.0
  broadcast = 192.168.1.255
  terpakai  = 192.168.1.1  …  192.168.1.254   (254 perangkat)
```

Dua alamat ada di **subnet yang sama** hanya kalau bagian network-nya sama. Itulah yang menentukan apakah komputermu bicara langsung ke perangkat lain, atau harus mengirim lewat gateway.

### Referensi mask cepat

| CIDR | Mask | Bit host | Total alamat | Perangkat terpakai |
|:---:|:---|:---:|:---:|:---:|
| /24 | 255.255.255.0 | 8 | 256 | 254 |
| /25 | 255.255.255.128 | 7 | 128 | 126 |
| /26 | 255.255.255.192 | 6 | 64 | 62 |
| /27 | 255.255.255.224 | 5 | 32 | 30 |
| /28 | 255.255.255.240 | 4 | 16 | 14 |
| /30 | 255.255.255.252 | 2 | 4 | 2 |

Polanya: tiap tambahan satu bit ruang host **menggandakan** jumlah alamat. "Terpakai" selalu dua lebih sedikit, karena alamat network dan broadcast tidak bisa diberikan ke perangkat. (`/30` dengan 2 host terpakai adalah pilihan klasik untuk link antara dua router.)

---

## 4. Contoh: Memecah Sebuah Jaringan

Misalkan kamu punya `192.168.1.0/24` (256 alamat) dan ingin memecahnya menjadi **empat subnet yang sama besar**.

Empat potong berarti meminjam 2 bit lagi dari bagian host (karena 2² = 4), yang mengubah `/24` menjadi `/26`. Tiap `/26` punya 64 alamat:

| # | Network | Rentang terpakai | Broadcast |
|:---:|:---|:---|:---|
| 1 | 192.168.1.0/26 | .1 – .62 | .63 |
| 2 | 192.168.1.64/26 | .65 – .126 | .127 |
| 3 | 192.168.1.128/26 | .129 – .190 | .191 |
| 4 | 192.168.1.192/26 | .193 – .254 | .255 |

Dua aturan membuat ini mudah dihitung di kepala:

- Tiap subnet lebarnya 64, jadi network-nya melangkah tiap 64: `.0, .64, .128, .192`.
- Broadcast selalu `network berikutnya − 1`.

Kalau subnet yang berbeda butuh ukuran yang berbeda (LAN kantor besar, link router kecil berisi 2 alamat), beri masing-masing subnet terkecil yang muat, mulai dari yang terbesar, tanpa tumpang tindih. Ini disebut **VLSM** (Variable Length Subnet Mask).

---

## 5. Rentang Alamat Privat dan Khusus

Beberapa rentang dicadangkan untuk dipakai di dalam jaringan lokal. Alamat ini tidak unik di seluruh dunia, jadi tidak bisa muncul langsung di Internet publik; ia menjangkau Internet lewat NAT (Bagian 7).

```
┌────────────────────────────────────────────────────────────┐
│ PRIVAT (RFC 1918) — bebas dipakai di jaringanmu sendiri    │
│  10.0.0.0/8        10.0.0.0     – 10.255.255.255           │
│  172.16.0.0/12     172.16.0.0   – 172.31.255.255           │
│  192.168.0.0/16    192.168.0.0  – 192.168.255.255          │
├────────────────────────────────────────────────────────────┤
│ KHUSUS                                                     │
│  127.0.0.0/8       loopback ("mesin ini")                  │
│  169.254.0.0/16    link-local (muncul saat DHCP gagal)     │
│  224.0.0.0/4       multicast                               │
└────────────────────────────────────────────────────────────┘
```

Melihat alamat `169.254.x.x` di sebuah mesin adalah petunjuk yang berguna: biasanya artinya DHCP tidak menjawab, jadi perangkat memilih alamat sendiri.

---

## 6. Cara Router Memilih Jalur

Sebuah router mungkin tahu beberapa rute yang cocok untuk sebuah tujuan. Aturannya sederhana: **yang paling spesifik menang** (longest prefix match).

```text
Tujuan: 192.168.1.10

Rute A: 192.168.0.0/16  via router X   (luas: seluruh /16)
Rute B: 192.168.1.0/24  via router Y   (spesifik: cuma /24 ini)

→ router memilih B, karena /24 lebih spesifik dari /16
```

Kalau tidak ada yang cocok, traffic jatuh ke **default route** `0.0.0.0/0` (`::/0` untuk IPv6), dan begitulah mesinmu menjangkau Internet luas lewat gateway-nya.

---

## 7. NAT: Berbagi Satu Alamat Publik

Rumahmu punya satu IP publik tapi banyak perangkat. **NAT** (Network Address Translation) membuat semuanya berbagi IP itu. Router menulis ulang alamat sumber privat dari traffic keluar menjadi alamat publiknya sendiri, dan mengingat percakapan mana milik perangkat internal mana (dengan melacak nomor port) supaya balasannya kembali ke yang benar.

```text
laptop 192.168.1.10:51000  →  router  →  publik 203.0.113.5:62000  →  Internet
                                 (mengingat pemetaannya)
balasan ←───────────────────── router  ←────────────────────────────  balasan
```

| Tipe | Yang dilakukan |
|:---|:---|
| Static NAT | Pemetaan 1-ke-1 tetap, untuk server yang butuh IP publik tetap |
| PAT / "overload" | Banyak perangkat di balik satu IP publik (setup rumah/kantor biasa) |

Poin keamanan penting: **NAT bukan firewall.** NAT menyembunyikan alamat internal sebagai efek samping, tapi tidak menentukan apa yang diizinkan. Kamu tetap butuh filter sungguhan. IPv6 sering melewati NAT sama sekali (alamatnya cukup banyak), jadi jangan menganggap "kita punya NAT" berarti "kita terlindungi."

---

## 8. ICMP, Ping, dan Traceroute

**ICMP** adalah protokol pembawa pesan di network layer: ia membawa pengecekan ketersambungan dan laporan error.

**Ping** mengirim ICMP "kamu di sana?" dan menunggu balasan. Ia memberi tahu apakah sebuah host bisa dijangkau dan kira-kira berapa lama satu perjalanan bolak-balik, tidak lebih.

**TTL** di balasan memberi petunjuk kasar tentang sistem lawan (ini cuma default dan bisa diubah):

| TTL terlihat | Kemungkinan sistem |
|:---:|:---|
| ~64 | Linux / Unix / macOS |
| ~128 | Windows |
| ~255 | Perangkat jaringan (router, switch) |

**Traceroute** adalah pemanfaatan TTL yang cerdik. Ia mengirim paket dengan TTL = 1, lalu 2, lalu 3, dan seterusnya. Tiap router yang membuang paket saat TTL mencapai 0 akan melapor balik, jadi kamu tahu jalurnya lompatan demi lompatan.

```bash
ping -c 4 1.1.1.1      # terjangkau? berapa waktu bolak-baliknya?
traceroute -n 1.1.1.1  # lewat jalur mana?
```

---

## 9. Catatan Keamanan

| Masalah | Risiko | Pertahanan |
|:---|:---|:---|
| IP spoofing | Memalsukan sumber untuk bersembunyi atau memantulkan serangan ke orang lain | Filter sumber di tepi (BCP38 / uRPF) |
| Satu jaringan datar besar | Kalau satu host dibobol, penyerang mudah menjangkau semuanya | Pecah jadi subnet/VLAN dengan filter di antaranya |
| Manajemen terekspos | SSH/RDP berada di jaringan user biasa | Subnet manajemen terpisah |
| IPv6 terlupakan | Host dual-stack yang tak dipantau di v6 | Inventarisasi IPv6 juga; RA Guard |
| Memblokir semua ICMP | Merusak diagnostik berguna dan path-MTU discovery | Rate-limit, bukan blokir total |

Kebersihan lab: lihat interface dan rute milikmu (`ip addr`, `ip route`) sebelum mengubah apa pun. Subnet mask atau rute yang salah adalah salah satu penyebab gangguan yang paling umum.

---

## 10. Cheatsheet

### Hitung cepat di kepala

- `/24` → 256 alamat, network melangkah tiap 1 di oktet terakhir
- `/25` → 128 alamat, langkah 128
- `/26` → 64 alamat, langkah 64
- `/27` → 32 alamat, langkah 32
- `/28` → 16 alamat, langkah 16
- `/30` → 4 alamat (2 terpakai), link router-ke-router klasik

```bash
# ── Periksa mesinmu sendiri ──────────────────────────────────
ip -c addr show
ip route show
ip -4 route get 1.1.1.1    # rute/gateway mana yang akan dipakai?
ip neighbor show

# ── Diagnostik ───────────────────────────────────────────────
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
mtr -n 1.1.1.1             # traceroute langsung dan terus-menerus

# ── Kalkulator subnet ────────────────────────────────────────
ipcalc 192.168.1.0/26       # kalau terpasang
python3 -c "import ipaddress as i; n=i.ip_network('192.168.1.0/26'); \
print(n.network_address, n.broadcast_address, n.num_addresses)"
```

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1918, RFC 4632 (CIDR), RFC 3021 (/31), RFC 6598 (CGNAT)
> - `man ip`, `man ping`, `man traceroute`

> **Repositori:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab untuk jaringan milik sendiri atau yang kamu berizin mengujinya.
