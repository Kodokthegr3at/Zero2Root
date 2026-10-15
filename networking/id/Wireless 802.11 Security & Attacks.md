# Keamanan & Serangan Wireless 802.11

> **LearnCybersecurity** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: *802.11 Wireless Networks: The Definitive Guide*; Stallings, *Network Security Essentials*; Kurose & Ross, *Computer Networking*

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-043` | **Fase 2:** Networking
> **Estimasi belajar:** 5 jam | **Level:** Lanjutan
> **Prasyarat:** LC-038
> **Peta buku:** Gast, 802.11 Wireless Networks (lengkap); Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Bagaimana Wi-Fi diatur
2. Bagaimana keamanan Wi-Fi berkembang
3. WPA2: kunci dan handshake 4 langkah
4. WPA3: pertukaran password yang lebih baik
5. Deautentikasi dan risikonya
6. Pertahanan dan pemantauan
7. Catatan keamanan
8. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| STA (station) | Klien Wi-Fi apa pun: laptop, ponsel, dsb. |
| AP (access point) | Perangkat tempat klien menyambung (si "pangkalan" Wi-Fi) |
| SSID | Nama jaringan, yang kamu pilih dari daftar Wi-Fi |
| BSSID | Alamat MAC si AP, yang mengidentifikasinya secara unik |
| PSK | Pre-shared key: password Wi-Fi yang dibagi semua orang di jaringan rumah |
| Handshake | Pertukaran saat klien dan AP membuktikan tahu kuncinya dan menyiapkan enkripsi |
| CCMP / AES | Enkripsi yang dipakai untuk data Wi-Fi di WPA2/WPA3 |
| Management frame | Pesan kontrol (menyambung, memutus, beacon) yang terpisah dari data sebenarnya |
| PMF | Protected Management Frames: proteksi untuk pesan kontrol itu |
| Evil twin | AP palsu yang meniru nama jaringan asli untuk memancing klien |

---

## 1. Bagaimana Wi-Fi Diatur

IEEE 802.11 ("Wi-Fi") menghubungkan **station** (STA, perangkatmu) ke **access point** (AP). Nama jaringannya adalah **SSID**-nya; tiap AP diidentifikasi secara unik oleh alamat MAC-nya, si **BSSID**. Beberapa AP bisa berbagi satu SSID supaya kamu berpindah di antara mereka tanpa putus.

```
  ┌────────────── Jaringan Wi-Fi: SSID "CORP" ──────────────┐
  │   AP1                        AP2                         │
  │    ↑↑↑                        ↑↑↑                        │
  │  ponsel, laptop             laptop                       │
  └──────────────────────────────────────────────────────────┘
          │
          └── koneksi kabel ──► LAN / Internet
```

Traffic Wi-Fi terbagi menjadi tiga jenis frame:

| Jenis frame | Tugas | Contoh |
|:---|:---|:---|
| Data | Membawa traffic sebenarnya | halaman web, video |
| Control | Membantu berbagi gelombang udara | acknowledgement |
| Management | Bergabung dan penemuan | beacon, menyambung, memutus |

Satu hal yang harus dihayati: **Wi-Fi itu radio, jadi siapa pun di dekatnya bisa mendengarnya.** Kamu tidak bisa mengandalkan tembok. Kerahasiaan dan integritas hanya datang dari keamanan layer link yang dipakai jaringan, dan itulah topik sisa materi ini.

---

## 2. Bagaimana Keamanan Wi-Fi Berkembang

Keamanan Wi-Fi membaik dalam generasi yang jelas. Kalau kamu punya pilihan, ambil yang terbaru yang didukung perangkatmu.

| Era | Yang dipakai | Boleh dipakai? |
|:---|:---|:---|
| Open | Tanpa enkripsi | Hanya dengan captive portal + HTTPS di level aplikasi |
| WEP | Cipher lama yang sudah rusak | Jangan pernah; rusak puluhan tahun lalu |
| WPA (TKIP) | Transisi | Hindari; legacy |
| WPA2-Personal | Password bersama + AES | Masih umum; hanya sekuat password-nya |
| WPA2-Enterprise | Login per-user lewat 802.1X | Standar kantor |
| WPA3-Personal | Pertukaran password modern (SAE) | Lebih disukai; tahan tebakan offline |
| WPA3-Enterprise | Login per-user, kripto lebih kuat | Jaminan tinggi |

Aturan praktisnya: pakai WPA3 kalau bisa, minimal WPA2 dengan password kuat, dan jangan pernah WEP atau TKIP.

---

## 3. WPA2: Kunci dan Handshake 4 Langkah

Tujuan handshake WPA2 adalah mengubah password bersama menjadi **kunci sesi yang baru dan unik** untuk tiap koneksi, dan memastikan kedua pihak tahu password-nya, semua itu **tanpa pernah mengirim password lewat udara**.

Kuncinya tersusun berlapis:

- **PMK** (kunci utama): di jaringan rumah berasal dari password Wi-Fi dicampur dengan nama jaringan. Di Wi-Fi enterprise berasal dari login per-user.
- **PTK** (kunci sesi): diturunkan dari PMK plus beberapa angka acak baru (**nonce**) dari kedua pihak dan alamat MAC mereka. Karena nonce-nya baru tiap kali, kunci sesinya berbeda untuk tiap koneksi.
- **GTK** (kunci grup): dibagikan AP ke semua klien, untuk traffic broadcast.

### Handshake 4 langkah

```
  AP                                         STA (klien)
   │  1. ini angka acakku (ANonce)            │
   │─────────────────────────────────────────►│  (klien kini bisa menghitung PTK)
   │  2. ini punyaku (SNonce) + bukti          │
   │◄─────────────────────────────────────────│  (AP menghitung PTK, mengecek buktinya)
   │  3. kunci grup + bukti + "pasang"         │
   │─────────────────────────────────────────►│
   │  4. diakui                                │
   │◄─────────────────────────────────────────│
   │     data kini terenkripsi dengan kunci    │
```

Tiap pihak membuktikan ia menurunkan kunci sesi yang **sama**, yang hanya mungkin kalau keduanya benar-benar tahu password-nya. Tidak ada yang pernah mengirim password-nya.

Jebakan untuk Wi-Fi rumah: seluruh keamanan ini bertumpu pada **kekuatan password**. Password yang pendek atau umum bisa ditebak offline oleh orang yang menangkap handshake-nya. (Materi ini tidak membahas cara cracking itu dilakukan.) Solusinya adalah password acak yang panjang, atau lebih baik, WPA3 atau Enterprise.

---

## 4. WPA3: Pertukaran Password yang Lebih Baik

WPA3-Personal mengganti handshake dengan **SAE** (Simultaneous Authentication of Equals, dibangun di atas metode bernama Dragonfly). Perbedaan pentingnya: kedua pihak membuktikan tahu password lewat bolak-balik langsung, dengan cara yang **tidak memberi penyadap apa pun yang bisa diuji secara offline**.

| Sifat | Artinya buatmu |
|:---|:---|
| Tidak ada tebakan offline murah | Menangkap pertukarannya tidak lagi membuat penyerang bisa menggilir tebakan password di mesinnya sendiri |
| Hanya tebakan online | Penyerang harus menebak langsung ke AP, yang bisa membatasi lajunya |

SAE tetap butuh password yang tidak sepele (supaya tebakan online tetap sia-sia), dan menjalankan "mode transisi" campuran WPA2+WPA3 bisa melemahkan kalau perangkat lama memaksa jaringan turun ke WPA2. Untuk organisasi, Enterprise dengan EAP-TLS (sertifikat per-user) tetap standar emas. SAE adalah peningkatan nyata, bukan alasan untuk memakai `password123`.

---

## 5. Deautentikasi dan Risikonya

Secara historis, management frame yang menyuruh perangkat memutus ("deauth") dikirim **tanpa proteksi apa pun**. Artinya orang dalam jangkauan radio bisa memalsukan sebuah pemutusan dan melempar perangkat keluar dari jaringannya. Itu sendiri sudah denial of service: perangkatnya terputus dan harus menyambung lagi.

Bahaya yang lebih besar adalah apa yang bisa menyusul. Perangkat yang terputus bisa otomatis menyambung ke jaringan mirip, sebuah **evil twin**: AP palsu yang menyiarkan SSID yang sama untuk memancing klien dan memanen kredensial.

Pertahanannya adalah **Protected Management Frames (PMF / 802.11w)**, yang mengautentikasi pesan-pesan kontrol itu sehingga pemutusan palsu ditolak. PMF **wajib di WPA3**. Juga membantu: kesadaran pengguna, dan memvalidasi sertifikat server di Wi-Fi Enterprise.

> Materi ini menjelaskan konsep dan pertahanannya, bukan cara menyuntikkan frame atau menjalankan serangan jamming.

Anggap gelombang pemutusan massal yang mendadak sebagai insiden ketersediaan: cek log AP, cari perubahan RF di sekitar, dan pastikan PMF ditegakkan.

---

## 6. Pertahanan dan Pemantauan

| Kontrol | Tujuan |
|:---|:---|
| WPA3 / PMF wajib | Memblokir serangan deauth klasik dan memperkuat Wi-Fi berbasis password |
| 802.1X + EAP-TLS | Identitas per-perangkat/user, kunci baru tiap sesi |
| Matikan WEP / TKIP | Menghapus cipher yang rusak |
| Password kuat dan unik (kalau pakai PSK) | Entropi tinggi; rotasi berkala |
| Client isolation | Mencegah klien Wi-Fi saling menjangkau |
| Pisahkan SSID tamu dan staf | Firewall jaringan tamu dari yang internal |
| Deteksi AP nakal | Menemukan jaringan asing atau mirip di channel-mu |
| Matikan WPS PIN | Menghapus cara lemah untuk memulihkan password |

Ide deteksi: beacon kedua yang menyiarkan SSID-mu dari BSSID tak terduga (kemungkinan evil twin), lonjakan pemutusan mendadak di capture jaringanmu sendiri, atau lonjakan kegagalan autentikasi.

---

## 7. Catatan Keamanan

| Masalah | Risiko | Pertahanan |
|:---|:---|:---|
| Password lemah | Kerahasiaan seluruh link jatuh | Password acak panjang, atau WPA3 / Enterprise |
| WEP / TKIP lawas | Rusak dengan mudah | Paksa hanya AES (CCMP/GCMP) |
| Management frame tak terlindungi | Denial of service deauth | PMF / WPA3 |
| Wi-Fi + LAN datar | Pergerakan lateral setelah bergabung | Client isolation + network access control |
| Evil twin | Phishing kredensial | Kesadaran pengguna; validasi sertifikat server EAP |
| Wi-Fi IoT lemah | Titik masuk lunak ke jaringan | SSID / VLAN terpisah untuk IoT |

Kebersihan lab: hanya audit AP dan ruang udara yang kamu punya izinnya. Capture untuk troubleshooting di jaringanmu sendiri, bukan milik tetangga.

---

## 8. Cheatsheet

```bash
# ── State link milikmu (Linux) ───────────────────────────────
iw dev                         # interface wireless-mu
iw dev wlan0 link              # BSSID, frekuensi, sinyal saat ini
iw dev wlan0 info

# ── Survei jaringan sekitar (observabilitas di radiomu) ─────
sudo iw dev wlan0 scan | egrep 'BSS|SSID|RSN|signal'

# ── NetworkManager ───────────────────────────────────────────
nmcli device wifi list
nmcli connection show

# ── Info regulasi / channel ──────────────────────────────────
iw reg get

# ── Di AP yang kamu operasikan, utamakan setting ini ────────
# WPA3 (SAE) kalau klien mendukung, selain itu WPA2 + password kuat
# PMF wajib (ieee80211w=2), hanya AES/CCMP, WPS PIN dimatikan
```

| Perintah | Kegunaan |
|:---|:---|
| `iw … link` | Menampilkan BSSID, frekuensi, dan sinyalmu |
| `iw … scan` | Mensurvei jaringan sekitar (ikuti hukum setempat) |
| `nmcli device wifi` | Mengelola profil Wi-Fi di desktop |

---

> **Referensi & sumber buku**
> - Matthew Gast, *802.11 Wireless Networks: The Definitive Guide*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - IEEE 802.11i / WPA2 RSN, IEEE 802.11w (PMF), spesifikasi WPA3 (Wi-Fi Alliance)
> - `man iw`, `man nmcli`

> **Repositori:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan administrasi untuk WLAN milik sendiri, tanpa prosedur cracking atau injeksi serangan.
