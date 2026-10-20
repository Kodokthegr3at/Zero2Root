# Model OSI

> **Zero2Root** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-038` | **Fase 2:** Networking
> **Estimasi belajar:** 6-8 jam | **Level:** Pemula
> **Prasyarat:** LC-005
> **Peta buku:** Kurose & Ross, Computer Networking Ch.1-2; Stallings, Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu model OSI, dan kenapa penting
2. Tujuh layer satu per satu
3. Cara data berjalan: enkapsulasi
4. TCP vs UDP
5. Port yang perlu kamu tahu
6. Perangkat mana bekerja di layer mana
7. Serangan dan pertahanan, per layer
8. Troubleshooting dengan layer
9. OSI vs model TCP/IP
10. Referensi cepat

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Protokol | Seperangkat aturan yang disepakati, diikuti dua komputer supaya bisa saling mengerti |
| Layer (lapisan) | Satu "tugas" di networking. Setiap layer menangani tugasnya, lalu menyerahkan hasilnya ke layer berikutnya |
| PDU | Nama potongan data di sebuah layer (bit, frame, packet, segment, data) |
| Alamat MAC | ID hardware yang tertanam di kartu jaringan, dipakai di dalam satu jaringan lokal |
| Alamat IP | Alamat logis untuk mengarahkan data melintasi jaringan yang berbeda |
| Port | Angka yang menyatakan data itu untuk program yang mana di sebuah komputer (web = 80, SSH = 22) |
| Header | Info tambahan yang ditempelkan sebuah layer di depan data (alamat, port, dsb.) |
| Enkapsulasi | Membungkus data dengan header saat turun melewati layer |
| Frame / packet / segment | Satuan data di layer Data Link / Network / Transport |

---

## 1. Apa Itu Model OSI, dan Kenapa Penting

**Model OSI** (Open Systems Interconnection) adalah cara memecah "bagaimana komputer berkomunikasi lewat jaringan" menjadi **7 layer**, masing-masing dengan satu tugas yang jelas. Model ini diterbitkan lembaga standar ISO pada 1984.

Bayangkan mengirim paket. Satu orang menulis surat, orang lain memasukkannya ke amplop dan menuliskan alamat, kurir menentukan rute, truk membawanya secara fisik. Tiap tahap hanya mengurus tugasnya sendiri dan percaya tahap lain mengerjakan bagiannya. Jaringan bekerja begitu juga: tiap layer mengerjakan bagiannya lalu menyerahkannya ke layer berikut.

Model OSI adalah **peta untuk belajar dan troubleshooting**. Jaringan nyata sebenarnya berjalan di atas model TCP/IP yang lebih sederhana (Bagian 9), tapi OSI adalah kosakata bersama yang dipakai semua orang untuk menjelaskan di mana sesuatu terjadi.

Kenapa penting untuk keamanan:

- Mengetahui *di layer mana* sebuah serangan terjadi memberi tahu di mana harus menaruh pertahanan (firewall web tidak akan menghentikan serangan di kabel).
- Memahami cara data dibungkus layer demi layer adalah dasar analisis paket.
- Mengetahui protokol mana ada di tiap layer memandu aturan firewall dan IDS/IPS.

### Tujuh layer sekilas

```
┌───────┬──────────────────┬────────────────────────────────────────────┐
│ Layer │   Nama           │  Tugasnya                                   │
├───────┼──────────────────┼────────────────────────────────────────────┤
│   7   │  Application     │  Protokol yang dipakai aplikasi (HTTP, DNS, SSH) │
│   6   │  Presentation    │  Format, enkripsi, kompresi                 │
│   5   │  Session         │  Memulai, menjaga, dan mengakhiri percakapan │
│   4   │  Transport       │  TCP/UDP, port, pengiriman andal             │
│   3   │  Network         │  Alamat IP, routing antar jaringan           │
│   2   │  Data Link       │  Alamat MAC, switch, frame                   │
│   1   │  Physical        │  Kabel, radio, bit mentah                    │
└───────┴──────────────────┴────────────────────────────────────────────┘

Trik menghafal, atas ke bawah:
  "All People Seem To Need Data Processing"
```

---

## 2. Tujuh Layer Satu per Satu

### Layer 1 — Physical: memindahkan bit mentah

Layer paling bawah. Membawa 1 dan 0 polos sebagai pulsa listrik, cahaya, atau gelombang radio. Layer ini tidak mengerti arti datanya; cuma memindahkan sinyal dari A ke B. Ini soal kabel, fiber, konektor, radio, dan perangkat yang hanya mengulang sinyal (hub, repeater).

Perintah aman untuk memeriksanya:

```bash
ip link show            # apakah interface-nya up? (Linux)
ethtool eth0            # kecepatan, duplex, "Link detected: yes"
ip -s link show eth0    # penghitung error (kabel jelek, interferensi)
```

| Media | Kecepatan umum | Jarak maks |
|-------|-------|---------------|
| Kabel Cat5e | 1 Gbps | 100 m |
| Kabel Cat6 | 10 Gbps | 55 m |
| Fiber (single-mode) | 100 Gbps+ | 40–80 km |
| Wi-Fi 6 | hingga ~9,6 Gbps | ~100 m |

### Layer 2 — Data Link: bicara dengan perangkat sebelah

Layer ini memindahkan data antar perangkat di **jaringan lokal yang sama**, memakai **alamat MAC** (ID hardware tiap kartu jaringan). Satuan datanya adalah **frame**. Perangkat utamanya adalah **switch**, yang belajar MAC mana ada di port mana lalu meneruskan frame sesuai itu.

```bash
ip link show      # alamat MAC-mu sendiri
ip neigh show     # tabel ARP: IP mana memetakan ke MAC mana
```

Protokol yang perlu diketahui: **Ethernet** (frame LAN kabel), **ARP** (mencari MAC untuk sebuah IP, dibahas di LC-042), **802.1Q** (tag VLAN), **STP** (mencegah loop antar switch).

### Layer 3 — Network: mencari jalur antar jaringan

Layer ini membawa data dari satu jaringan ke jaringan lain memakai **alamat IP**, dan memilih rutenya. Satuan datanya adalah **packet**, dan perangkat utamanya adalah **router**.

```bash
ip addr show          # alamat IP-mu
ip route show         # tabel routing / default gateway
ping -c 4 8.8.8.8     # apakah host itu bisa dijangkau sama sekali? (ICMP)
traceroute 8.8.8.8    # lewat jalur mana paketnya?
```

Protokol: **IPv4/IPv6** (pengalamatan), **ICMP** (ping dan pesan error), **OSPF/BGP** (router saling berbagi rute).

### Layer 4 — Transport: menyampaikan data ke program yang tepat, dengan andal

Layer ini menghubungkan **program**, bukan sekadar mesin, memakai **nomor port**. Ada dua pilihan utama:

- **TCP:** membangun koneksi dulu, menjamin semua tiba berurutan, mengirim ulang yang hilang. Dipakai untuk web, SSH, email.
- **UDP:** langsung menembakkan data tanpa persiapan dan tanpa jaminan. Lebih cepat, dipakai untuk DNS, panggilan video, game.

```bash
ss -tulnp             # port mana yang terbuka dan listening (Linux)
nc -zv host 22        # apakah sebuah port TCP bisa dijangkau?
```

### Layer 5 — Session: mengelola percakapan

Memulai, menjaga, dan mengakhiri sebuah "session" antar aplikasi dengan rapi. Kalau transfer putus, layer session adalah ide yang memungkinkannya lanjut dari titik yang tepat. Contoh: session NetBIOS dan SMB (berbagi file Windows), RPC, iSCSI.

### Layer 6 — Presentation: menerjemahkan dan mengamankan data

Si "penerjemah". Memastikan data dari satu sistem bisa dibaca sistem lain: encoding karakter (ASCII, Unicode), kompresi (gzip), dan **enkripsi (TLS ada di sini)**. Base64 dan format gambar seperti JPEG/PNG juga urusan layer presentation.

```bash
echo "Hello" | base64          # encode
echo "SGVsbG8K" | base64 -d    # decode
openssl s_client -connect example.com:443 </dev/null   # memeriksa koneksi TLS
```

### Layer 7 — Application: yang sebenarnya "dibicarakan" program

Layer teratas, paling dekat dengan pengguna. Ini soal **protokol jaringan** yang dipakai aplikasi, bukan aplikasinya sendiri. HTTP, DNS, FTP, SSH, SMTP, SNMP, LDAP, RDP, SMB semuanya ada di sini.

> Catatan: "Application layer" **bukan** berarti Chrome atau Firefox. Maksudnya protokol (HTTP) yang dibicarakan program-program itu.

```bash
curl -I https://example.com    # melihat header respons HTTP
dig example.com                # lookup DNS
```

| Protokol | Port | Kegunaan |
|----------|------|----------|
| HTTP / HTTPS | 80 / 443 | Web |
| DNS | 53 | Lookup nama |
| SSH | 22 | Shell jarak jauh yang aman |
| FTP | 21 | Transfer file (cleartext) |
| SMTP | 25 | Mengirim email |
| SMB | 445 | Berbagi file Windows |
| RDP | 3389 | Remote desktop |

---

## 3. Cara Data Berjalan: Enkapsulasi

Saat kamu mengirim sesuatu, data turun melewati layer di mesinmu. Tiap layer membungkus data dengan **header**-nya sendiri, seperti memasukkan surat ke dalam amplop di dalam amplop yang lebih besar. Di sisi lain, tiap layer membuka amplopnya saat naik.

```
KOMPUTERMU (turun)                     KOMPUTER LAIN (naik)

L7  Data                               L7  Data
L6  Data                               L6  Data
L5  Data                               L5  Data
L4  [header TCP | Data]  = Segment     L4  [header TCP | Data]
L3  [header IP | Segment] = Packet     L3  [header IP | ...]
L2  [header MAC | Packet | FCS] = Frame L2 [header MAC | ... | FCS]
L1  101000110101...  = Bit             L1  101000110101...

            ─────── media fisik ───────>
```

Tiap layer hanya membaca header *miliknya sendiri*. Satuan datanya berganti nama di tiap level: **bit** (L1), **frame** (L2), **packet** (L3), **segment** (L4), dan sekadar **data** di atasnya.

---

## 4. TCP vs UDP

Keduanya ada di Layer 4, tapi perilakunya sangat berbeda.

| Aspek | TCP | UDP |
|--------|-----|-----|
| Satuan data | Segment | Datagram |
| Koneksi | Ya (handshake 3 langkah) | Tidak |
| Andal? | Ya, mengirim ulang data yang hilang | Tidak ada jaminan |
| Berurutan? | Ya | Tidak dijamin |
| Kecepatan | Lebih lambat (overhead lebih banyak) | Lebih cepat |
| Cocok untuk | Web, SSH, transfer file, email | DNS, panggilan video, game |

### Handshake 3 langkah TCP

Sebelum TCP mengirim data sungguhan, kedua pihak saling menyapa dalam tiga langkah. Seperti telepon: "Kamu dengar aku?" — "Ya, kamu dengar aku?" — "Ya."

```
Client                          Server
  │──── SYN ─────────────────────>│   1. "Aku mau bicara"
  │<─── SYN + ACK ────────────────│   2. "Oke, aku juga mau bicara"
  │──── ACK ─────────────────────>│   3. "Bagus, ayo mulai"
  │<════ data mengalir dua arah ═>│
```

Menutup koneksi adalah pertukaran sopan serupa (FIN / ACK) di kedua arah.

---

## 5. Port yang Perlu Kamu Tahu

**Port** adalah angka 0 sampai 65535 yang menyatakan traffic itu untuk layanan yang mana di sebuah mesin. Ada tiga rentang:

- **0–1023:** port terkenal (HTTP 80, SSH 22). Di kebanyakan sistem, hanya administrator yang bisa membukanya.
- **1024–49151:** port terdaftar untuk aplikasi tertentu.
- **49152–65535:** port sementara, dipilih otomatis untuk tiap koneksi keluar.

```bash
# Discovery sederhana dan sah atas apa yang terbuka di host milikmu
nmap host              # port-port umum
nmap -p- host          # semua port
nc -zv host 443        # cek satu port tertentu
```

| Port | Layanan | Kenapa sensitif |
|------|---------|--------------------|
| 21 | FTP | Mengirim password dalam cleartext |
| 22 | SSH | Target login yang umum; pakai key, bukan password |
| 23 | Telnet | Cleartext; sebaiknya dipensiunkan |
| 25 | SMTP | Email; bisa disalahgunakan untuk enumerasi user atau relay spam |
| 53 | DNS | Bisa membocorkan nama internal (zone transfer) |
| 80 / 443 | HTTP / HTTPS | Seluruh permukaan serangan web |
| 139 / 445 | NetBIOS / SMB | Berbagi file Windows; secara historis sangat sering dieksploitasi |
| 3389 | RDP | Remote desktop; target brute-force yang sering |
| 3306 / 5432 | MySQL / PostgreSQL | Database yang terekspos dengan login lemah atau default |
| 6379 | Redis | Sering dibiarkan tanpa autentikasi sama sekali |

---

## 6. Perangkat Mana Bekerja di Layer Mana

| Layer | Perangkat | Tugas |
|-------|-----------|-------|
| 7 Application | Firewall web (WAF), proxy, load balancer | Memfilter dan memeriksa HTTP/TLS |
| 4 Transport | Firewall stateful | Mengizinkan/memblokir berdasarkan port dan koneksi |
| 3 Network | Router, switch Layer-3 | Routing antar jaringan |
| 2 Data Link | Switch, bridge, access point | Meneruskan frame berdasarkan MAC |
| 1 Physical | Hub, repeater, kabel, kartu jaringan | Membawa sinyal |

Cara cepat melihat router Layer-3 yang dipakai mesinmu sendiri:

```bash
ip route | grep default    # default gateway = router-mu
```

---

## 7. Serangan dan Pertahanan, per Layer

Setiap layer bisa diserang dengan caranya sendiri. Tujuan di sini adalah mengenali **jenis serangan itu masuk layer mana, dan bagaimana dipertahankan**, supaya kamu bisa menaruh kontrol yang tepat. Ini peta untuk defender, bukan panduan menyerang: perintah eksploitasi yang spesifik sengaja tidak dimasukkan, dan materi lain (LC-042 ARP, LC-039 Wireless, modul web) membahas konsepnya lebih dalam.

| Layer | Contoh serangan (apa itu) | Cara bertahan |
|-------|---------------------------|---------------|
| 7 Application | SQL injection, XSS, request forgery, phishing: menyalahgunakan logika aplikasi | Validasi input, patching, firewall aplikasi web |
| 6 Presentation | TLS downgrade / SSL stripping: memaksa koneksi lebih lemah atau polos | Paksa HTTPS (HSTS), TLS 1.3 modern, tolak cipher lama |
| 5 Session | Session hijacking, serangan replay kredensial: memakai ulang session atau hash curian | Rotasi token session, wajibkan MFA, perketat autentikasi |
| 4 Transport | SYN flood, port scanning, UDP flood: menguras atau memeriksa layanan | SYN cookie, rate limiting, firewall stateful |
| 3 Network | IP spoofing, ICMP flood, route poisoning: memalsukan alamat atau rute | Ingress filtering (uRPF), ACL, batas laju ICMP |
| 2 Data Link | ARP spoofing, MAC flooding, VLAN hopping: menipu switch lokal | Dynamic ARP Inspection, port security di switch |
| 1 Physical | Penyadapan kabel, Wi-Fi "evil twin" palsu, jamming | Kontrol akses fisik, selalu enkripsi (VPN, HTTPS) |

Poin paling berguna: sebuah kontrol hanya melindungi layer-nya sendiri. Enkripsi di Layer 6 tidak berguna melawan orang yang mencabut kabel di Layer 1, dan firewall web Layer-7 tidak berguna melawan ARP spoof di Layer 2. Keamanan nyata menumpuk pertahanan di beberapa layer sekaligus (defense in depth).

---

## 8. Troubleshooting dengan Layer

Layer memberimu checklist saat "kok tidak jalan". Mulai dari bawah lalu naik: kalau layer bawah rusak, tidak ada yang di atasnya bisa bekerja.

```
Tidak bisa menjangkau sebuah server?

L1 Physical:   Kabel terpasang / Wi-Fi tersambung? Link up?
               ip link show eth0   → cari "state UP"

L2 Data Link:  Bisa melihat MAC gateway?
               ip neigh show

L3 Network:    Bisa ping gateway, lalu sebuah IP publik?
               ping 192.168.1.1  lalu  ping 8.8.8.8
               ip route show     → ada default route?

L4 Transport:  Apakah port-nya benar-benar terbuka?
               nc -zv target 443

L5/6 Session/Presentation:  Sertifikat TLS valid / belum kedaluwarsa?
               openssl s_client -connect target:443

L7 Application: Layanan itu bilang apa?
               curl -v https://target   → cek status code dan log
```

---

## 9. OSI vs Model TCP/IP

Jaringan nyata berjalan di atas model TCP/IP 4 layer. Tujuh layer OSI memetakan ke sana begini:

```
Model OSI                    Model TCP/IP          Contoh
Layer 7 Application  ┐
Layer 6 Presentation ├──────  Application          HTTP, DNS, SSH, TLS
Layer 5 Session      ┘
Layer 4 Transport    ───────  Transport            TCP, UDP
Layer 3 Network      ───────  Internet             IP, ICMP
Layer 2 Data Link    ┐
Layer 1 Physical     ┴──────  Network Access       Ethernet, Wi-Fi, ARP
```

Pakai OSI untuk *bernalar dan berbicara* soal di mana sesuatu terjadi; traffic di kabel adalah TCP/IP.

---

## 10. Referensi Cepat

```text
CHEAT SHEET LAYER (atas → bawah)
  L7 Application   HTTP, DNS, SSH, SMB          (yang dibicarakan aplikasi)
  L6 Presentation  TLS, Base64, JPEG            (format & enkripsi)
  L5 Session       NetBIOS, RPC, session SMB    (mengelola percakapan)
  L4 Transport     TCP (andal), UDP (cepat)     [PORT]
  L3 Network       IP, ICMP, routing            [ALAMAT IP]
  L2 Data Link     Ethernet, ARP, VLAN          [ALAMAT MAC]
  L1 Physical      kabel, radio, bit            [HARDWARE]

SATUAN DATA PER LAYER
  L7–L5 Data → L4 Segment/Datagram → L3 Packet → L2 Frame → L1 Bit

TRIK MENGHAFAL
  atas → bawah:  All People Seem To Need Data Processing
  bawah → atas:  Please Do Not Throw Sausage Pizza Away
```

### Tabel referensi OSI lengkap

| Layer | Nama | PDU | Alamat | Perangkat | Protokol utama |
|-------|------|-----|--------|-----------|----------------|
| 7 | Application | Data | — | WAF, proxy | HTTP, DNS, SSH |
| 6 | Presentation | Data | — | — | TLS, MIME |
| 5 | Session | Data | — | — | NetBIOS, RPC |
| 4 | Transport | Segment / Datagram | Port | Firewall | TCP, UDP |
| 3 | Network | Packet | Alamat IP | Router | IPv4, IPv6, ICMP |
| 2 | Data Link | Frame | Alamat MAC | Switch | Ethernet, ARP |
| 1 | Physical | Bit | — | Hub, NIC | Ethernet, DSL |

---

## Latihan

Coba jawab dulu tanpa membuka kunci. Kalau salah, baca lagi bagian yang disebut di soal.

### Task 1: kenali layernya

1. Alamat MAC dipakai di layer berapa? (Bagian 2)
2. Router bekerja di layer apa, dan memakai alamat jenis apa?
3. Menurut OSI, TLS (gembok di browser) masuk layer mana?
4. Satuan data (PDU) TCP di layer 4 disebut apa?

<details><summary>Kunci jawaban</summary>

1. Layer 2 (Data Link)
2. Layer 3 (Network), dengan alamat IP
3. Layer 6 (Presentation)
4. Segment

</details>

### Task 2: port yang wajib hafal

| Soal | Jawaban kamu |
|:---|:---|
| Port default SSH? | |
| Port default HTTPS? | |
| Port berbagi file Windows (SMB)? | |
| Port DNS? | |
| Port Remote Desktop (RDP)? | |

<details><summary>Kunci jawaban</summary>

22 · 443 · 445 · 53 · 3389

</details>

### Task 3: praktik di komputermu sendiri

Jalankan perintah berikut di Linux-mu, lalu jawab pertanyaan di komentarnya.

```bash
ip addr show       # Soal: berapa alamat IP kamu? (Layer 3)
ip link show       # Soal: berapa alamat MAC kamu? (Layer 2)
ss -tulnp          # Soal: port apa saja yang listening di mesinmu? (Layer 4)
curl -I https://example.com   # Soal: status code apa yang dibalas? (Layer 7)
```

### Task 4: troubleshooting

`ping 8.8.8.8` berhasil, tapi `ping google.com` gagal. Kemungkinan masalahnya ada di protokol apa?

<details><summary>Kunci jawaban</summary>

DNS (layer 7). Ping ke IP berhasil, berarti jaringan dan routing di layer 3 sudah jalan. Yang gagal adalah proses menerjemahkan nama domain ke IP.

</details>

### Lab gratis

| Tool | Yang bisa dilatih | Biaya |
|:---|:---|:---|
| Wireshark | Rekam traffic-mu sendiri, lalu lihat layer 2 sampai 7 di panel detail paket | Gratis |
| Cisco Packet Tracer | Simulasi switch dan router (daftar lewat Cisco NetAcad) | Gratis |

Kamu dianggap lulus pelajaran ini kalau bisa menjelaskan ke teman di layer mana alamat MAC, alamat IP, dan port bekerja, tanpa melihat catatan.

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 793 (TCP), RFC 768 (UDP)
> - Dokumentasi resmi Nmap dan Wireshark, registri nomor port IANA

> **Repositori:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Materi edukasi dan lab untuk jaringan milik sendiri atau yang kamu berizin mengujinya.
