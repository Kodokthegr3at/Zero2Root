# DNS & Keamanan Domain Name System

> **LearnCybersecurity** | Seri Networking Fundamentals
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-041` | **Fase 2:** Networking
> **Estimasi belajar:** 4 jam | **Level:** Intermediate
> **Prasyarat:** LC-039
> **Peta buku:** Kurose & Ross, Computer Networking Ch.2; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Hierarki DNS (namespace tree)
2. Algoritma resolusi
3. Jenis resource record
4. DNSSEC (tanda tangan & rantai trust)
5. Privasi DNS (DoT & DoH)
6. Zone transfer (risiko misconfig)
7. Cache poisoning (konsep & pertahanan)
8. Catatan keamanan (deteksi & hardening)
9. Cheatsheet admin

---

## 1. Hierarki DNS: namespace tree

DNS (Domain Name System) memetakan nama hierarkis ke resource, paling sering alamat IP. Namespace-nya berbentuk pohon terbalik, berakar di root (`.`). Setiap label dipisahkan titik, dan nama FQDN dibaca dari kanan ke kiri:

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www
```

Nama penuhnya adalah `www.example.com.` (titik di akhir menandakan root).

| Level | Contoh | Peran |
|:---|:---|:---|
| Root | `.` | Ujung hierarki, root NS |
| TLD | `com`, `id`, `jp` | Dikelola registry |
| SLD / zone | `example.com` | Organisasi / zona otoritatif |
| Host / label | `www`, `mail` | Resource dalam zona |

Delegasi bekerja dengan cara: parent menyimpan record NS (plus glue A/AAAA) untuk child zone. Otoritas zona pada dasarnya adalah kumpulan nameserver yang menjawab dengan flag AA (Authoritative Answer) untuk nama di dalam zona itu.

DNS adalah basis data hierarkis yang terdistribusi. Tidak ada satu server pun yang menyimpan seluruh pohon; otoritas didelegasikan ke bawah secara bertingkat. Klien biasanya berbicara dengan recursive resolver, dan resolver itulah yang menyusuri pohon (atau memakai cache) untuk mendapatkan jawaban.

---

## 2. Algoritma resolusi

Ada tiga peran utama dalam proses resolusi:

| Peran | Perilaku |
|:---|:---|
| Stub resolver | Berjalan di OS/aplikasi, mengirim query ke recursive resolver yang dikonfigurasi |
| Recursive resolver | Melakukan lookup penuh atas nama yang diminta stub, boleh menyimpan cache |
| Authoritative server | Hanya menjawab untuk zona yang dilayaninya |

Algoritma iteratifnya, secara intuitif (mengikuti Kurose):

```text
1. mulai dari root server
2. tanyakan nama itu ke server saat ini
3. dapat jawaban atau NXDOMAIN?   → selesai
4. dapat referral?                → tanya server yang ditunjuk, lalu ulangi langkah 2
```

```
Stub ──Q──► Recursive ──iterative──► Root
                 │                      │
                 │◄──── referral ───────┘
                 ├──► TLD NS
                 │◄── referral
                 └──► Auth NS ──► Answer (AA)
```

Soal caching: TTL pada tiap RR membatasi berapa lama data boleh disimpan di cache. Jawaban negatif juga di-cache (RFC 2308), dengan aturan tersendiri yang terpisah dari jawaban positif.

Rekursi membebaskan klien dari kerja menyusuri pohon DNS sendiri. Idealnya, authoritative server tidak melakukan rekursi untuk publik internet, karena ini memperkecil permukaan untuk amplification/abuse. Memisahkan peran recursive dan authoritative adalah kebersihan operasional standar: jangan mengaktifkan rekursi begitu saja di authoritative server publik.

---

## 3. Jenis resource record

| Type | Fungsi singkat | Contoh data |
|:---|:---|:---|
| A | Host IPv4 | `93.184.216.34` |
| AAAA | Host IPv6 | `2606:2800:...` |
| NS | Delegasi / nameserver zona | `ns1.example.com.` |
| CNAME | Alias ke nama kanonik | `www → origin.cdn.net.` |
| MX | Mail exchanger plus preference | `10 mail.example.com.` |
| TXT | Teks bebas (SPF, verifikasi, dan sejenisnya) | `"v=spf1 ..."` |
| SOA | Start of Authority (serial, timer) | metadata zona |
| PTR | Reverse (in-addr.arpa / ip6.arpa) | nama host |
| SRV | Lokasi service | `_sip._tcp...` |
| DNSKEY | Kunci publik zona (DNSSEC) | key material |
| DS | Hash key child yang disimpan di parent (DNSSEC) | digest |
| RRSIG | Tanda tangan atas RRset | signature |
| NSEC / NSEC3 | Bukti ketidakberadaan (non-existence) | authenticated denial |

RRset adalah semua RR dengan nama, type, dan class yang sama. Operasi DNSSEC menandatangani seluruh RRset, bukan satu RR tunggal yang dipisahkan dari siblings-nya.

Format wire klasiknya lewat UDP/53 (jawaban besar beralih ke TCP/53 atau EDNS0). EDNS0 memperluas ukuran UDP yang diizinkan dan membawa opsi tambahan, seperti DO bit untuk menandai "DNSSEC OK" dan cookies.

---

## 4. DNSSEC: tanda tangan & rantai trust

DNSSEC menambahkan otentikasi dan integritas pada data DNS, bukan kerahasiaan. Resolver yang melakukan validasi memastikan jawaban benar berasal dari zona yang tepat dan tidak diubah di jalur transit maupun di cache.

Komponen intinya:

| RR | Peran |
|:---|:---|
| DNSKEY | Kunci publik zona (ZSK / KSK) |
| RRSIG | Tanda tangan atas RRset |
| DS | Digest DNSKEY milik child, disimpan di parent |
| NSEC/NSEC3 | Bukti bahwa nama/type tidak ada |

Verifikasi RRSIG secara konsep: untuk RRset R dan kunci publik K:

```text
Verify(public key, RRset, RRSIG) → accept / reject
```

Secara abstrak, dengan skema tanda tangan Sign/Verify:

```text
RRSIG = Sign(private key, Hash(RRset) + meta)
```

di mana meta mencakup algorithm, labels, original TTL, inception/expiration, key tag, dan signer name.

Rantai trust-nya:

```
Trust Anchor (root KSK, hardcoded/managed)
        │  validates
        ▼
   root DNSKEY ──RRSIG──► root zone data
        │  DS for .com
        ▼
   com DNSKEY ──► … ──DS──► example.com DNSKEY
                                │
                                ▼
                         RRSIG on example.com RRsets
```

Resolver membutuhkan trust anchor, biasanya di level root. Kalau DS di parent cocok dengan DNSKEY milik child, dan RRSIG valid serta berada dalam jendela waktu yang benar, RRset dianggap Secure. Kegagalan validasi menghasilkan status Bogus, artinya jawaban itu tidak boleh dipakai. Zona yang tidak memakai DNSSEC berstatus Insecure, bukan Bogus.

DNSSEC menghentikan substitusi jawaban palsu yang tidak terdeteksi di sepanjang jalur maupun di cache, dengan syarat validator diaktifkan secara end-to-end. Ia tidak mengenkripsi query; untuk kerahasiaan pertanyaan itu sendiri, gunakan DoT/DoH.

---

## 5. Privasi DNS: DoT & DoH

| Mekanisme | Port / framing | Sifat |
|:---|:---|:---|
| DNS klasik | UDP/TCP 53 | Pertanyaan & jawaban cleartext |
| DoT (DNS over TLS) | TCP 853 | DNS dibungkus di dalam TLS |
| DoH (DNS over HTTPS) | TCP 443 | DNS lewat API HTTP(S) |

Manfaatnya: mencegah pengintaian pasif dan manipulasi on-path terhadap query/response di jalur yang sebelumnya cleartext.

Trade-off operasionalnya perlu dipahami. Resolver terpusat, misalnya vendor DoH tertentu, tetap bisa melihat metadata resolusi, jadi pilih kebijakan privasi secara sadar. Di lingkungan enterprise, resolver internal sering dipaksakan sambil memblokir DoH liar agar logging dan DLP tetap berjalan; ini perlu didokumentasikan dan dikomunikasikan ke pengguna. Kombinasi ideal untuk lab atau produk adalah DoT/DoH menuju resolver yang juga melakukan validasi DNSSEC.

---

## 6. Zone transfer: risiko misconfiguration

AXFR (full zone transfer) dan IXFR (incremental) dipakai agar secondary bisa meniru isi zona primary. Ini fitur operasional yang sah, bukan "serangan". Tapi kalau diizinkan ke semua sumber tanpa batas, seluruh isi zona, termasuk host internal dan naming scheme, bisa diunduh oleh pihak luar.

Risiko dari misconfig semacam ini:

- Exposure inventori nama internal
- Membantu recon sebelum serangan lain dilakukan
- Kemunculan secondary palsu kalau tidak ada kontrol akses, idealnya ditambah TSIG

Langkah hardening untuk admin zona Anda sendiri:

- Batasi AXFR/IXFR hanya ke IP secondary yang sudah dikenal
- Pakai TSIG (shared secret berbasis HMAC) antara primary dan secondary
- Jangan mengandalkan "security through obscurity" pada nama host; tetap terapkan segmentasi dan least privilege

Catatan penting: catatan ini tidak berisi prosedur serangan, hanya kesadaran konfigurasi dan checklist defensif.

Perlakukan zone transfer yang terbuka sebagai cacat konfigurasi. Pantau upaya AXFR yang tidak terduga di log authoritative server.

---

## 7. Cache poisoning: konsep & pertahanan

Cache poisoning, secara konsep, terjadi ketika recursive resolver menyimpan binding nama ke data yang salah karena menerima jawaban palsu yang tampak sah (cocok ID/question) sebelum jawaban asli tiba, atau karena kelemahan dalam prediksi transaksi.

Model ancaman level tinggi (intuisi dari era Kaminsky): ruang tebakan transaksi historis terlalu kecil kalau

```text
ruang tebakan = 2¹⁶ kemungkinan TXID × jumlah kemungkinan port sumber
```

bernilai kecil, dan penyerang bisa membanjiri jawaban spoof untuk query yang ia picu sendiri.

Pertahanan modernnya (bukan cookbook serangan):

| Kontrol | Efek |
|:---|:---|
| Source port randomization | Memperbesar ruang tebakan transaksi |
| TXID random | Sudah lama wajib, dikombinasikan dengan randomisasi port |
| DNS cookies (RFC 7873) | Token klien-server yang mengurangi spoof murah |
| DNSSEC validation | Jawaban palsu gagal verifikasi, jadi berstatus Bogus |
| 0x20 encoding / QNAME case | Entropi tambahan di wire, di tempat yang mendukungnya |
| Network path security | Membatasi siapa yang bisa inject paket di jalur resolver |

Sinyal untuk deteksi: lonjakan SERVFAIL pada zona yang biasanya aman, RRset yang tiba-tiba berubah tanpa ada perubahan zona yang sah, atau ketidakcocokan dengan pandangan resolver validasi lain.

Pertahanan yang benar itu defense-in-depth: entropi pada transaksi query digabung dengan otentikasi kriptografis lewat DNSSEC. Tak satupun dari keduanya cukup sendirian sebagai cerita operasional yang lengkap.

---

## 8. Catatan keamanan: pertahanan & deteksi

| Isu | Risiko | Pertahanan / deteksi |
|:---|:---|:---|
| DNS cleartext | Sniff / tamper on-path | DoT/DoH, jalur tepercaya |
| Resolver tanpa validasi | Forgery tidak terdeteksi | Aktifkan validasi DNSSEC |
| Open recursive | Abuse / amplification | ACL klien, pisahkan auth dari recursive |
| Open AXFR | Zone dump | ACL + TSIG, alert di log |
| Rogue resolver (via DHCP/RA) | Redirect resolusi | DHCP snooping, RA Guard, policy DoH |
| Trust anchor basi | False Bogus / outage | Otomasi RFC 5011, plus monitoring |

Kebersihan lab: uji hanya resolver dan zona milik Anda sendiri. Saat mendiagnosis status Bogus, bandingkan jawaban `dig +dnssec` dengan resolver publik lain yang juga melakukan validasi.

---

## 9. Cheatsheet: admin / lab yang sah

```bash
# ── Basic lookup (sistem Anda) ───────────────────────────────
dig example.com A +noall +answer
dig example.com AAAA
dig MX example.com
dig NS example.com

# ── Trace iterative path (observability) ─────────────────────
dig +trace example.com

# ── DNSSEC inspection ────────────────────────────────────────
dig example.com A +dnssec +multi
dig DNSKEY example.com +multi
dig DS example.com +short
delv example.com A          # validating lookup jika dikonfigurasi

# ── Reverse / SOA ────────────────────────────────────────────
dig -x 93.184.216.34
dig SOA example.com +noall +answer

# ── Check if YOUR authoritative allows transfer to YOU only ──
# (jalankan dari secondary yang diizinkan; expect REFUSED dari host lain)
dig AXFR example.com @ns1.example.com

# ── Local stub / systemd-resolved ────────────────────────────
resolvectl status
resolvectl query example.com
```

| Perintah | Kegunaan |
|:---|:---|
| `dig +short` | Jawaban ringkas |
| `dig +dnssec` | Tampilkan RRSIG / DO |
| `dig +trace` | Simulasikan jalan dari root |
| `delv` | Validasi DNSSEC di sisi klien lewat BIND tools |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - RFC 1034/1035 (DNS), RFC 4033-4035 (DNSSEC), RFC 7858 (DoT), RFC 8484 (DoH), RFC 7873 (Cookies)
> - `man dig`, `man resolvectl`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab pada sistem atau zona milik sendiri atau yang berizin. Tidak ada prosedur serangan di sini.
