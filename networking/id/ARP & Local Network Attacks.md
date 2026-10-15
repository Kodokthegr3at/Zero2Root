# ARP & Serangan Jaringan Lokal

> **LearnCybersecurity** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-042` | **Fase 2:** Networking
> **Estimasi belajar:** 4 jam | **Level:** Lanjutan
> **Prasyarat:** LC-039, LC-040
> **Peta buku:** Kurose & Ross, Computer Networking Ch.4-5; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Kenapa ARP ada
2. Cara request dan reply bekerja
3. ARP cache
4. Mekanisme terkait
5. Masalah MITM di jaringan lokal
6. Pertahanan
7. Deteksi dan pemantauan
8. Catatan keamanan
9. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| ARP | Protokol yang mencari alamat MAC untuk sebuah IP, di dalam satu jaringan lokal |
| Alamat MAC | ID hardware kartu jaringan, dipakai untuk pengiriman di dalam jaringan lokal |
| ARP cache | Tabel jangka pendek yang disimpan perangkat berisi "IP ini = MAC ini" |
| Broadcast | Pesan yang dikirim ke semua orang di segmen lokal |
| Gateway | Router yang dipakai perangkat untuk menjangkau jaringan lain |
| Spoofing / poisoning | Memberi perangkat pemetaan IP-ke-MAC yang palsu |
| MITM | Man-in-the-middle: diam-diam berada di antara dua pihak dan meneruskan traffic-nya |
| DAI | Dynamic ARP Inspection: fitur switch yang membuang pesan ARP yang berbohong |
| Segmentasi | Memecah jaringan jadi zona lebih kecil untuk membatasi sejauh mana penyerang bisa menjangkau |

---

## 1. Kenapa ARP Ada

Di dalam satu jaringan lokal, perangkat mengirim data memakai **alamat MAC** (ID hardware tiap kartu jaringan), bukan alamat IP. Tapi program-programmu dan routing bekerja dalam **alamat IP**. Harus ada yang menghubungkan keduanya. Yang menghubungkannya adalah **ARP** (Address Resolution Protocol):

```text
ARP menjawab satu pertanyaan:  "Alamat MAC mana yang punya IP 10.0.0.9?"
```

Ini hanya bekerja di dalam **segmen lokal** (broadcast domain yang sama). Kamu tidak pernah meng-ARP server yang jauh; sebagai gantinya mesinmu meng-ARP **gateway**-nya lalu menyerahkan frame ke MAC gateway, membiarkan router melanjutkannya.

```
  Host A                    switch                      Host B
  10.0.0.5                                              10.0.0.9
         ──── "Siapa yang punya 10.0.0.9? Beri tahu 10.0.0.5" (broadcast) ────►
         ◄─── "10.0.0.9 ada di bb:bb:bb:bb:bb:bb" (reply) ─────────────────────
  sekarang mengirim frame ke bb:bb:… ────────────────────────────────────────►
```

Kelemahan utamanya terpasang di desain ARP sendiri: **tidak ada cara untuk mengecek apakah sebuah reply itu jujur.** Siapa pun yang menjawab lebih dulu, dan paling meyakinkan, menang. Fakta tunggal itulah akar dari setiap serangan di materi ini, dan alasan pertahanan di Bagian 6 ada. (IPv6 memakai protokol serupa bernama NDP, bukan ARP.)

---

## 2. Cara Request dan Reply Bekerja

ARP hanya punya dua pesan utama:

| Operasi | Artinya |
|:---|:---|
| Request | "Siapa yang punya IP ini? Beri tahu aku." (dikirim sebagai broadcast ke semua) |
| Reply | "IP itu ada di MAC ini." (dikirim balik ke si penanya) |

```text
A → semua:  "Siapa yang punya IP_B? Beri tahu A"
B → A:      "IP_B ada di MAC_B"
```

Setelah pertukaran ini, A bisa mengirim frame langsung ke B. Banyak sistem juga diam-diam belajar pemetaan hanya dari traffic ARP yang didengarnya, yang praktis tapi justru itulah kenapa reply yang **tak diminta** atau tak terduga adalah tanda bahaya.

---

## 3. ARP Cache

Supaya tidak bertanya tiap kali, tiap perangkat menyimpan tabel jangka pendek:

```text
alamat IP  →  (alamat MAC, state, interface, waktu kedaluwarsa)
```

```bash
ip neigh show      # lihat cache ARP/NDP di Linux
```

Entri-entrinya kedaluwarsa dan diperbarui. Yang penting dipahami adalah ini: **cache hanya sepercaya siapa pun yang boleh bicara di segmen itu.** Kalau sebuah perangkat menerima reply tanpa pengecekan tambahan, reply palsu bisa diam-diam menimpa entri yang benar.

Tips praktis: setelah mengganti kartu jaringan atau renumbering, entri cache yang basi bisa menyebabkan masalah ketersambungan "hantu" sampai ia kedaluwarsa. Flush entri hanya di mesin yang kamu administrasi.

---

## 4. Mekanisme Terkait

| Mekanisme | Apa itu | Catatan keamanan |
|:---|:---|:---|
| Proxy ARP | Router menjawab ARP atas nama perangkat yang bukan lokal | Memperluas kepercayaan lokal; audit kalau tak disengaja |
| Gratuitous ARP | Pengumuman "ini aku" yang tak diminta | Sah untuk failover, tapi juga jalur spoofing kalau tak difilter |
| ARP probe (RFC 5227) | Cek konflik alamat sebelum memakai sebuah IP | Berguna untuk deteksi alamat ganda |

```
  Normal:      "Siapa yang punya B?"   →  "B ada di MAC_B"
  Gratuitous:  "A ada di MAC_A"        →  (pengumuman, memperbarui cache semua orang)
```

---

## 5. Masalah MITM di Jaringan Lokal

Karena reply ARP tidak diverifikasi, perangkat jahat di segmen yang sama bisa meyakinkan korban bahwa **IP gateway ada di MAC penyerang**. Korban lalu mengirim traffic "ke Internet"-nya ke penyerang, bukan ke router sungguhan.

Kalau penyerang diam-diam meneruskan traffic itu, korban tidak menyadari apa-apa, sementara penyerang duduk di tengah dan bisa membaca atau mengubah apa pun yang tidak terenkripsi. Itulah **man-in-the-middle di layer jaringan lokal**.

```
  Sebelum:  Korban ───────────────► Gateway ──► Internet

  Sesudah:  Korban ──► Penyerang ──► Gateway ──► Internet
                     (membaca/mengubah traffic sambil lewat)
```

> Materi ini menjelaskan **kenapa** serangan ini mungkin dan cara menghentikannya. Instruksi poisoning langkah demi langkah dan tool spoofing sengaja tidak dimasukkan.

Arti defensifnya: jangan menganggap "frame yang dialamatkan ke MAC gateway benar-benar sampai ke gateway." Mengenkripsi layer atas (TLS di mana-mana) membatasi apa yang bisa dibaca penyerang, tapi tidak mengembalikan kepercayaan di layer lokal, terutama untuk ketersediaan dan untuk apa pun yang tidak terenkripsi ujung-ke-ujung. Kamu tetap butuh kontrol di bawah.

---

## 6. Pertahanan

| Kontrol | Cara kerja | Cocok di mana |
|:---|:---|:---|
| DHCP Snooping | Switch mencatat (MAC, IP, port) yang sah dari lease DHCP sungguhan | Fondasi untuk DAI |
| Dynamic ARP Inspection (DAI) | Switch mengecek tiap pesan ARP terhadap catatan itu dan membuang yang berbohong | Jaringan akses enterprise |
| Entri ARP statis | Pemetaan tetap yang diatur manual di host atau router kritis | Gateway, server kecil |
| Port security | Membatasi berapa alamat MAC yang diterima sebuah port switch | Tepi akses |
| Segmentasi / private VLAN | Mencegah perangkat saling menjangkau bebas di layer lokal | Di mana-mana; kontrol arsitektur terkuat |

Ide terkuat di sini adalah **segmentasi**: makin kecil segmen lokal, makin sedikit perangkat yang bisa dijangkau penyerang dengan trik ARP sejak awal. Entri statis tidak skalabel untuk jaringan besar, jadi kombinasi praktisnya adalah DHCP Snooping plus DAI di switch akses, dengan pemantauan di atasnya.

```
  [ VLAN User ] ──DAI + DHCP Snooping──► [ gateway ] ──filter──► [ VLAN Server ]
```

---

## 7. Deteksi dan Pemantauan

Sinyal yang layak diselidiki di jaringan yang kamu kelola:

| Sinyal | Kemungkinan artinya |
|:---|:---|
| MAC gateway tiba-tiba berubah di banyak host sekaligus | Percobaan spoofing atau binding yang tidak stabil |
| Dua MAC berbeda sama-sama mengklaim satu IP | Konflik alamat atau spoofing |
| Badai request ARP | Loop, salah konfigurasi, atau scanning agresif |
| Penghitung "drop" DAI naik di switch | Pesan ARP yang melanggar binding yang tercatat |

```bash
# Pengamatan yang sah di host milikmu
ip neigh show
sudo tcpdump -ni eth0 arp     # amati traffic ARP di NIC-mu sendiri
```

Korelasikan yang kamu lihat dengan log DAI milik switch dan daftar lease DHCP.

---

## 8. Catatan Keamanan

| Masalah | Risiko | Pertahanan |
|:---|:---|:---|
| ARP tidak bisa diautentikasi | Binding IP-ke-MAC palsu | DHCP Snooping + DAI |
| Satu segmen datar besar | MITM lokal dan recon jadi mudah | VLAN / segmentasi |
| Gratuitous ARP tak difilter | Menimpa cache massal | Rate limiting / inspeksi |
| Entri statis basi | Gangguan setelah ganti NIC | Runbook untuk memperbaruinya |
| IPv6 diabaikan | Celah kalau kamu cuma memikirkan ARP | RA Guard, inspeksi ND |
| Protokol cleartext | Bisa dibaca kalau MITM berhasil | TLS di mana-mana, plus HSTS |

Prinsipnya: percayai jaringan lokal hanya sejauh kebijakan switch benar-benar menegakkannya. Enkripsi ujung-ke-ujung melengkapi kontrol di layer link, bukan menggantikannya.

---

## 9. Cheatsheet

```bash
# ── Periksa tabel neighbor (host milikmu) ────────────────────
ip neigh show
ip -4 neigh show dev eth0
ip -6 neigh show               # padanan IPv6 (NDP)

# ── Kelola entri di host MILIKMU (hati-hati di produksi) ─────
sudo ip neigh add 10.0.0.1 lladdr aa:bb:cc:dd:ee:ff dev eth0 nud permanent
sudo ip neigh del 10.0.0.1 dev eth0
sudo ip neigh flush dev eth0

# ── Picu lookup normal ───────────────────────────────────────
ping -c 1 10.0.0.9
ip neigh get 10.0.0.9 dev eth0

# ── Amati ARP secara pasif di NIC-mu sendiri ─────────────────
sudo tcpdump -ni eth0 arp -vv

# ── MAC learning di Linux bridge ─────────────────────────────
bridge fdb show
```

| Perintah | Kegunaan |
|:---|:---|
| `ip neigh` | Melihat atau mengedit cache ARP/NDP |
| `tcpdump arp` | Mengaudit traffic ARP di NIC-mu sendiri |
| `bridge fdb` | Melihat MAC learning di Linux bridge |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - W. Richard Stevens, *UNIX Network Programming, Vol. 1*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 826 (ARP), RFC 5227 (IPv4 Address Conflict Detection), RFC 4861 (NDP)

> **Repositori:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab untuk jaringan milik sendiri atau yang kamu berizin menguji. Tidak ada playbook poisoning.
