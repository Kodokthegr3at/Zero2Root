# DNS & Keamanan Domain Name System

> **LearnCybersecurity** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-041` | **Fase 2:** Networking
> **Estimasi belajar:** 4 jam | **Level:** Menengah
> **Prasyarat:** LC-039
> **Peta buku:** Kurose & Ross, Computer Networking Ch.2; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu DNS, dan pohon nama
2. Bagaimana sebuah lookup sebenarnya terjadi
3. Jenis record yang akan kamu temui
4. DNSSEC: membuktikan jawaban itu asli
5. Privasi DNS: DoT dan DoH
6. Zone transfer: risiko salah konfigurasi
7. Cache poisoning, dan cara mencegahnya
8. Catatan keamanan
9. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| DNS | "Buku telepon" Internet: mengubah nama seperti `example.com` menjadi alamat IP |
| Resolver | Layanan yang melakukan lookup untukmu (biasanya milik ISP atau yang publik) |
| Authoritative server | Server yang menyimpan jawaban sebenarnya untuk sebuah domain |
| Record (RR) | Satu entri di DNS: sebuah nama plus nilainya (alamat, mail server, dsb.) |
| Zone | Kumpulan record satu domain, dikelola sebagai satu kesatuan |
| TTL | Berapa lama sebuah jawaban boleh disimpan di cache sebelum harus dicari lagi |
| Cache | Salinan jawaban terbaru yang disimpan, supaya lookup yang sama langsung instan |
| DNSSEC | Tanda tangan digital pada jawaban DNS, supaya kamu bisa membedakan yang palsu |
| DoT / DoH | DNS yang dikirim lewat koneksi terenkripsi (lewat TLS, atau lewat HTTPS) |

---

## 1. Apa Itu DNS, dan Pohon Nama

Komputer bicara dalam alamat IP, tapi manusia mengingat nama. **DNS** (Domain Name System) adalah layanan yang menerjemahkan satu ke yang lain: kamu mengetik `example.com`, DNS mengembalikan `93.184.216.34`. Ini buku teleponnya Internet.

Nama diatur sebagai pohon terbalik, dibaca dari **kanan ke kiri**, mulai dari root:

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www            →  nama lengkap: www.example.com.
```

| Level | Contoh | Siapa yang mengelola |
|:---|:---|:---|
| Root | `.` | Server root |
| TLD (top-level domain) | `com`, `id`, `jp` | Sebuah registry |
| Domain / zone | `example.com` | Sebuah organisasi |
| Host | `www`, `mail` | Sebuah mesin di dalam domain |

Tidak ada satu server pun yang tahu seluruh pohon. Tiap level **mendelegasikan** level berikutnya ke bawah ("tanya server `.com`, mereka akan mengarahkanmu ke server `example.com`"). Delegasi itulah yang membuat DNS bisa melayani seluruh Internet.

---

## 2. Bagaimana Sebuah Lookup Sebenarnya Terjadi

Ada tiga pemain yang terlibat:

| Pemain | Peran |
|:---|:---|
| Stub resolver | Klien kecil di dalam OS-mu; ia tinggal bertanya ke resolver |
| Recursive resolver | Mengerjakan pekerjaan beratnya, dan mengingat (cache) jawaban |
| Authoritative server | Menyimpan record sebenarnya untuk sebuah domain |

Kalau resolver belum punya jawabannya di cache, ia menelusuri pohon dari atas:

```text
1. tanya server root         → "aku tidak tahu, tapi tanya server .com"
2. tanya server .com         → "tanya server example.com"
3. tanya server example.com  → "www.example.com adalah 93.184.216.34"  ✓
```

```
Kamu ──► Recursive resolver ──► Root
                │                 │  "tanya .com"
                ├──► .com ────────┘
                │     │  "tanya example.com"
                └──► example.com ──► Jawaban
                │
        meng-cache jawabannya selama TTL, jadi lain kali instan
```

Tiap record punya **TTL** yang menyatakan berapa lama boleh di-cache. Caching itulah yang membuat DNS cepat; tanpanya, tiap klik akan menelusuri seluruh pohon lagi.

Catatan kebersihan: resolver **recursive** (menelusuri pohon untuk klien) dan server **authoritative** (menjawab untuk sebuah domain) adalah dua pekerjaan berbeda. Server authoritative publik sebaiknya tidak sekaligus melakukan recursion terbuka, karena itu jadi magnet penyalahgunaan dan amplifikasi.

---

## 3. Jenis Record yang Akan Kamu Temui

| Tipe | Yang disimpan | Contoh |
|:---|:---|:---|
| A | Alamat IPv4 | `93.184.216.34` |
| AAAA | Alamat IPv6 | `2606:2800:...` |
| CNAME | Alias ("nama ini sebenarnya nama itu") | `www → origin.cdn.net.` |
| MX | Ke mana email untuk domain ini pergi | `10 mail.example.com.` |
| NS | Server mana yang authoritative untuk zone | `ns1.example.com.` |
| TXT | Teks bebas (dipakai untuk SPF, verifikasi domain) | `"v=spf1 ..."` |
| PTR | Kebalikannya: dari IP kembali ke nama | dipakai di reverse lookup |
| DNSKEY / RRSIG / DS | Kunci dan tanda tangan DNSSEC (Bagian 4) | data kunci / tanda tangan |

DNS biasanya berjalan lewat UDP port 53 (kecil dan cepat); jawaban besar jatuh ke TCP port 53.

---

## 4. DNSSEC: Membuktikan Jawaban Itu Asli

DNS biasa punya kelemahan: saat sebuah jawaban tiba, tidak ada cara bawaan untuk tahu bahwa jawaban itu benar-benar datang dari tempat yang tepat dan tidak ditukar di tengah jalan. **DNSSEC** memperbaikinya dengan menambahkan **tanda tangan digital** (ide tanda tangan berasal dari LC-055).

Tiap zone menandatangani record-nya. Resolver yang memvalidasi bisa mengecek tanda tangannya dan yakin jawabannya asli dan tidak diubah:

```text
cek:  Verify(public key zone, record-nya, tanda tangannya) → asli / palsu
```

Kepercayaannya dirantai dari root ke bawah, seperti rantai sertifikat di PKI (LC-057): root menjamin `.com`, `.com` menjamin `example.com`, dan seterusnya. Resolver cukup mempercayai root untuk mempercayai seluruh rantai.

```
root (titik awal yang dipercaya)
  │ menjamin
  ▼
.com
  │ menjamin
  ▼
example.com  ──menandatangani──►  record-nya sendiri
```

Penting: DNSSEC membuktikan jawaban itu **asli**, tapi **tidak** menyembunyikannya. Pertanyaan dan jawabannya tetap berjalan terbuka. Untuk privasi, kamu butuh DoT atau DoH (bagian berikutnya).

---

## 5. Privasi DNS: DoT dan DoH

DNS klasik dikirim dalam teks polos, jadi siapa pun di jalur bisa melihat tiap nama yang kamu cari, dan berpotensi mengubahnya. Dua mekanisme mengenkripsinya:

| Mekanisme | Caranya | Port |
|:---|:---|:---|
| DNS klasik | Teks polos | UDP/TCP 53 |
| DoT (DNS over TLS) | DNS dibungkus koneksi TLS | TCP 853 |
| DoH (DNS over HTTPS) | DNS dibawa lewat HTTPS, jadi menyatu dengan traffic web | TCP 443 |

Manfaatnya adalah menghentikan penyadapan pasif dan perubahan di jalur atas lookup-mu. Tapi ada trade-off: resolver mana pun yang kamu pakai (termasuk penyedia DoH besar) tetap melihat query-mu, jadi pilih yang kebijakan privasinya kamu percaya. Banyak organisasi sengaja memaksa resolver internal dan memblokir DoH dadakan supaya logging keamanan mereka tetap bekerja. Kombinasi terbaik adalah transport terenkripsi (DoT/DoH) **plus** resolver yang memvalidasi DNSSEC.

---

## 6. Zone Transfer: Risiko Salah Konfigurasi

**Zone transfer** (AXFR) adalah fitur yang sah: ia membuat server DNS cadangan bisa menyalin seluruh daftar record dari server utama. Masalahnya muncul kalau dibiarkan terbuka untuk siapa saja.

Kalau orang asing bisa meminta zone transfer, mereka bisa mengunduh **seluruh** daftar hostname internalmu sekaligus: server, skema penamaan, semuanya. Itu tambang emas untuk reconnaissance, diserahkan tanpa serangan sungguhan.

Cara menjaga zone milikmu:

- Izinkan zone transfer hanya ke server cadanganmu yang dikenal, berdasarkan IP.
- Lindungi transfernya dengan **TSIG** (sebuah rahasia bersama yang dicek kedua server).
- Jangan mengandalkan hostname rahasia untuk keamanan; tetap terapkan segmentasi dan least privilege.

> Materi ini soal mengenali dan memperbaiki salah konfigurasinya, bukan melakukannya. Pantau log server authoritative-mu untuk percobaan transfer yang tak terduga.

---

## 7. Cache Poisoning, dan Cara Mencegahnya

**Idenya:** resolver meng-cache jawaban apa pun yang diterimanya. Kalau penyerang bisa menyelipkan jawaban **palsu** sebelum yang asli tiba, dan membuatnya tampak valid, resolver meng-cache alamat yang salah dan menyerahkannya ke semua orang selama TTL berlaku. Itu mengirim korban ke server penyerang padahal address bar masih menampilkan nama asli.

Supaya palsunya diterima, ia harus cocok dengan pertanyaan resolver dan beberapa nilai acak. Dulu nilai acak itu terlalu kecil untuk aman. Pertahanan modern semuanya bekerja dengan membuat jawaban palsu jauh lebih sulit dipalsukan atau lebih mudah dideteksi:

| Pertahanan | Yang dilakukan |
|:---|:---|
| Port sumber acak + ID query acak | Sangat memperbesar yang harus ditebak penyerang |
| DNS cookie | Token bersama yang menolak spoofing murah dari luar jalur |
| Validasi DNSSEC | Jawaban palsu gagal pengecekan tanda tangan lalu dibuang |
| Transport terenkripsi (DoT/DoH) | Mencegah penyerang di jalur membaca atau menyuntikkan |

Tanda bahaya yang perlu diperhatikan: alamat yang tiba-tiba berubah tanpa update yang sah, lonjakan kegagalan resolusi, atau jawaban sebuah resolver yang berbeda dari resolver tepercaya lain. Perlindungan sebenarnya adalah defense in depth: keacakan untuk mempersulit tebakan, **plus** DNSSEC untuk membuat pemalsuan bisa terdeteksi.

---

## 8. Catatan Keamanan

| Masalah | Risiko | Pertahanan / deteksi |
|:---|:---|:---|
| DNS teks polos | Penyadapan dan perubahan di jalur | DoT/DoH, resolver tepercaya |
| Resolver tanpa validasi | Jawaban palsu lolos tanpa disadari | Aktifkan validasi DNSSEC |
| Recursive resolver terbuka | Penyalahgunaan dan amplifikasi | Batasi klien; pisahkan recursive dari authoritative |
| Zone transfer terbuka | Seluruh zone-mu tersedot | Batasi per IP + TSIG; beri alert di log |
| Resolver nakal lewat DHCP | Lookup-mu diarahkan ulang | DHCP snooping, RA Guard, kebijakan DoH |

Kebersihan lab: hanya uji resolver dan zone milikmu. Saat sebuah jawaban terlihat salah, bandingkan hasil `dig +dnssec` dengan resolver publik tepercaya kedua.

---

## 9. Cheatsheet

```bash
# ── Lookup dasar ─────────────────────────────────────────────
dig example.com A +short       # cuma alamat IPv4-nya
dig example.com AAAA           # IPv6
dig MX example.com             # mail server
dig NS example.com             # name server authoritative

# ── Lihat seluruh penelusuran dari root ──────────────────────
dig +trace example.com

# ── Inspeksi DNSSEC ──────────────────────────────────────────
dig example.com A +dnssec      # tampilkan tanda tangan (RRSIG)
delv example.com A             # lookup dengan validasi, kalau dikonfigurasi

# ── Reverse lookup ───────────────────────────────────────────
dig -x 93.184.216.34

# ── Resolver sistemmu sendiri ────────────────────────────────
resolvectl status
resolvectl query example.com
```

| Perintah | Kegunaan |
|:---|:---|
| `dig +short` | Jawaban ringkas |
| `dig +dnssec` | Tampilkan tanda tangan DNSSEC |
| `dig +trace` | Mengamati lookup menelusuri dari root |
| `resolvectl` | Memeriksa resolver sistem sendiri |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1034/1035 (DNS), RFC 4033-4035 (DNSSEC), RFC 7858 (DoT), RFC 8484 (DoH), RFC 7873 (Cookies)
> - `man dig`, `man resolvectl`

> **Repositori:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab di sistem atau zone milik sendiri atau yang kamu berizin menguji. Tidak ada prosedur serangan.
