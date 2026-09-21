# Keamanan & Serangan Wireless 802.11

> **LearnCybersecurity** | Seri Networking Fundamentals
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: *802.11 Wireless Networks: The Definitive Guide*; Stallings, *Network Security Essentials*; Kurose & Ross, *Computer Networking*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-043` | **Fase 2:** Networking
> **Estimasi belajar:** 5 jam | **Level:** Advanced
> **Prasyarat:** LC-038
> **Peta buku:** Gast, 802.11 Wireless Networks (full); Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Overview arsitektur & framing 802.11
2. Evolusi keamanan (ringkas)
3. WPA2: PMK, PTK, GTK & 4-way handshake
4. WPA3-Personal: SAE (level tinggi)
5. Management frame & deauthentication (konsep DoS)
6. Pertahanan & monitoring
7. Catatan keamanan: ringkasan pertahanan
8. Cheatsheet

---

## 1. Overview arsitektur & framing 802.11

IEEE 802.11 mendefinisikan WLAN: stasiun (STA), access point (AP), dan BSS (Basic Service Set). Beberapa BSS dengan SSID yang sama dapat membentuk ESS. Medianya half-duplex; akses kanal memakai CSMA/CA (bukan CSMA/CD seperti Ethernet klasik).

Tiga kelas frame:

| Kelas | Peran | Contoh |
|:---|:---|:---|
| Data | Membawa muatan LLC/IP | QoS data |
| Control | Membantu akses medium | RTS/CTS, ACK |
| Management | Keanggotaan & discovery | Beacon, Probe, Auth, Assoc, Deauth, Disassoc |

```
  ┌────────────── ESS / SSID "CORP" ──────────────┐
  │   AP1 (BSS1)              AP2 (BSS2)          │
  │    ↑↑↑                     ↑↑↑                │
  │   STA                      STA                │
  └───────────────────────────────────────────────┘
         │
         └── wired DS (Distribution System) ──► LAN/Internet
```

Beacon mengumumkan SSID (atau hidden), kapabilitas, dan security IE (RSN). Association mengikat STA ke AP sebelum data unicast terenkripsi (pada jaringan modern).

Header 802.11 memakai beberapa field alamat (ToDS/FromDS) untuk membedakan SA/DA/BSSID; detail lengkapnya ada di buku O'Reilly *802.11 Wireless Networks*.

Wireless adalah medium broadcast yang dipakai bersama dalam jangkauan radio. Kerahasiaan dan integritas bergantung pada keamanan link-layer (RSN), bukan pada fakta "berada di dalam gedung". Selalu anggap penerima di sekitar bisa mendengar management frame yang tidak terproteksi dan jaringan yang konfigurasinya lemah.

---

## 2. Evolusi keamanan (ringkas)

| Era | Mekanisme | Status praktis |
|:---|:---|:---|
| Open | Tanpa enkripsi link | Hanya cocok untuk captive portal + TLS di level aplikasi |
| WEP | RC4 + IV lemah | Deprecated / broken, jangan dipakai |
| WPA-PSK (TKIP) | Transisi | Legacy; hindari jika bisa |
| WPA2-Personal | PSK + CCMP (AES) | Masih umum dipakai; PSK lemah jadi risiko |
| WPA2-Enterprise | 802.1X / EAP + RADIUS | Standar di lingkungan kantor |
| WPA3-Personal | SAE | Resistensi terhadap tebakan PSK offline lebih baik |
| WPA3-Enterprise | EAP + opsi suite 192-bit | High assurance |

RSN (Robust Security Network) IE di Beacon menyatakan cipher dan AKM yang ditawarkan. CCMP (AES-CCM) adalah cipher data yang diharapkan pada WPA2; GCMP muncul pada PHY yang lebih baru / konteks WPA3.

---

## 3. WPA2: PMK, PTK, GTK & 4-way handshake

Tujuan handshake: menurunkan kunci sesi yang segar dari rahasia jangka panjang, dan mengonfirmasi kepemilikan bersama tanpa mengirim PSK dalam bentuk cleartext lewat udara.

PMK (Pairwise Master Key):

- Personal (PSK): PMK diturunkan dari passphrase plus SSID (PBKDF2-HMAC-SHA1, 4096 iterasi pada WPA2-PSK klasik):

$$
\mathsf{PMK} = \mathsf{PBKDF2}(\mathsf{passphrase},\; \mathsf{SSID},\; 4096,\; 256\text{ bits})
$$

- Enterprise: PMK dihasilkan dari EAP / MSK setelah 802.1X berhasil (per sesi/user, lebih baik dibanding PSK yang dipakai bersama).

PTK (Pairwise Transient Key) diturunkan dari PMK ditambah nonce dan alamat MAC:

$$
\begin{aligned}
\mathsf{PTK} &= \mathsf{PRF\text{-}X}\big(
  \mathsf{PMK},\;
  \texttt{"Pairwise key expansion"},\\
  &\quad \min(AA,SPA) \,\|\, \max(AA,SPA) \,\|\,
  \min(ANonce,SNonce) \,\|\, \max(ANonce,SNonce)
\big)
\end{aligned}
$$

di mana $AA$ = MAC AP (BSSID), $SPA$ = MAC STA. PTK dipecah menjadi:

| Bagian | Fungsi |
|:---|:---|
| KCK | Key Confirmation Key (MIC pada EAPOL-Key) |
| KEK | Key Encryption Key (membungkus key material) |
| TK | Temporal Key untuk CCMP pada data unicast |

GTK (Group Temporal Key): kunci multicast/broadcast dari AP ke semua STA yang terasosiasi, didistribusikan dalam bentuk terbungkus selama handshake / group key handshake.

### 4-way handshake (EAPOL-Key): alur konsep

```
  AP                                         STA
   │  Msg1: ANonce                            │
   │─────────────────────────────────────────►│
   │          (STA hitung PTK; punya SNonce)  │
   │  Msg2: SNonce + MIC                      │
   │◄─────────────────────────────────────────│
   │  (AP hitung PTK; verifikasi MIC)         │
   │  Msg3: GTK + MIC + install               │
   │─────────────────────────────────────────►│
   │  Msg4: MIC / Ack                         │
   │◄─────────────────────────────────────────│
   │         Data terenkripsi CCMP (TK/GTK)   │
```

Verifikasi MIC dengan KCK membuktikan bahwa kedua pihak menurunkan PTK yang sama, yang berarti keduanya memiliki PMK yang sama.

Keamanan WPA2-Personal pada akhirnya bergantung pada entropi PSK. Passphrase dengan entropi rendah membuka celah untuk tebakan offline terhadap handshake yang berhasil ditangkap; catatan ini sengaja tidak mendokumentasikan prosedur cracking-nya. Mitigasinya: pakai PSK acak yang panjang, atau lebih baik prioritaskan WPA3-SAE atau Enterprise (802.1X).

---

## 4. WPA3-Personal: SAE (level tinggi)

SAE (Simultaneous Authentication of Equals) berbasis protokol Dragonfly (password-authenticated key exchange). Kedua pihak membuktikan pengetahuan atas password lewat interaksi online di grup eliptik / finite field, lalu menghasilkan PMK.

Sifat yang diinginkan (intuisi):

| Properti | Makna operasional |
|:---|:---|
| PAKE | Password tidak dipakai sebagai PSK "hashable" dengan cara yang sama seperti WPA2 |
| Resistensi offline | Menangkap handshake saja tidak memberi jalur verifikasi offline murah seperti pada PSK klasik |
| Forward-looking | Dipasangkan dengan kriptografi yang lebih modern di RSN |

SAE tetap membutuhkan password yang tidak sepele (sebagai proteksi terhadap tebakan online / rate-limited). Transition mode (WPA2+WPA3) dapat melemahkan postur keamanan jika STA legacy tetap dipaksa dipakai; pahami trade-off ini terhadap inventaris perangkat yang ada.

SAE mengubah model ancaman untuk jaringan berbasis passphrase; ini bukan izin untuk memakai password seperti `password123`. Enterprise dengan EAP-TLS tetap menjadi standar emas untuk organisasi.

---

## 5. Management frame & deauthentication (konsep DoS)

Banyak management frame klasik (deauth, disassoc) secara historis dikirim tanpa proteksi setara data frame. Akibatnya, pengirim yang berada dalam jangkauan radio bisa memaksa STA terputus dari AP, yang secara konsep merupakan DoS atau gangguan ketersediaan.

$$
\mathsf{Deauth}:\ \mathsf{STA} \leftrightarrow \mathsf{AP}\ \text{session torn down (state cleared)}
$$

Dampak sekunder: pengguna mungkin tersambung ulang ke SSID jahat yang mirip (evil twin) jika kebijakan di perangkat lemah. Mitigasi lewat edukasi pengguna, WPA3, validasi sertifikat Enterprise, dan PMF.

Protected Management Frames (PMF / 802.11w): melindungi sebagian management frame penting, dan wajib dipakai pada WPA3. Aktifkan mode PMF capable/required sesuai inventaris klien yang ada.

Catatan: tidak ada daftar perintah injeksi frame, tool cracking, atau playbook DoS di dokumen ini.

Perlakukan gelombang disconnect massal yang tidak jelas penyebabnya sebagai insiden ketersediaan: korelasikan log AP, perubahan RF di sekitar, dan apakah PMF sedang ditegakkan.

---

## 6. Pertahanan & monitoring

| Kontrol | Tujuan |
|:---|:---|
| WPA3 / PMF required | Mengurangi deauth klasik & memperkuat WPA2-Personal |
| 802.1X + EAP-TLS | Identitas per perangkat/user, PMK per sesi |
| Nonaktifkan WEP/TKIP | Menghilangkan cipher lemah |
| PSK unik dan kuat per SSID (jika pakai PSK) | Entropi tinggi; rotasi berkala |
| Client isolation / AP isolation | Mengurangi pergerakan lateral antar klien Wi-Fi |
| SSID guest terpisah dari corp | Segmentasi firewall |
| Deteksi rogue AP | Mendeteksi BSSID/SSID asing di kanal yang sama |
| Survei RF berkelanjutan | Baseline noise / utilisasi kanal |
| Nonaktifkan WPS PIN | Menghilangkan vektor recovery PSK yang lemah |

Ide deteksi: beacon SSID kembar dengan BSSID berbeda, lonjakan deauth pada air capture di lab Anda sendiri, klien yang sering berpindah BSSID tanpa kebijakan roaming, dan lonjakan kegagalan EAP.

---

## 7. Catatan keamanan: ringkasan pertahanan

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| PSK lemah | Kerahasiaan link ter-compromise | PSK acak yang panjang, atau WPA3/Enterprise |
| WEP/TKIP legacy | Crypto yang mudah dipatahkan | Paksa hanya CCMP/GCMP |
| Management frame terbuka | Deauth DoS | PMF / WPA3 |
| Wi-Fi dan LAN tidak terpisah | Pergerakan lateral setelah associate | Isolation + NAC |
| Evil twin | Phishing kredensial | Edukasi pengguna; validasi sertifikat server EAP |
| Wi-Fi IoT yang lemah | Titik lemah dalam jaringan | SSID/VLAN terpisah |

Kebersihan lab: audit hanya AP dan spektrum yang Anda punya izin atasnya. Lakukan capture untuk troubleshooting di jaringan sendiri, bukan untuk menyerang tetangga.

---

## 8. Cheatsheet: admin / lab yang sah

```bash
# ── Link state (Linux, interface Anda) ───────────────────────
iw dev
iw dev wlan0 link
iw dev wlan0 info
iwlist wlan0 scanning 2>/dev/null | head   # legacy; prefer iw scan

# ── Scan SSIDs (observability on your radio) ─────────────────
sudo iw dev wlan0 scan | egrep 'BSS|SSID|RSN|capability'

# ── NetworkManager ───────────────────────────────────────────
nmcli general status
nmcli device wifi list
nmcli connection show
nmcli device wifi show-password   # only for profiles you own

# ── Regulatory / channel info ────────────────────────────────
iw reg get
iw phy phy0 info | less

# ── Hostapd / AP you operate: check config ideas ─────────────
# wpa=2, rsn_pairwise=CCMP, ieee80211w=2 (PMF required) on YOUR AP
# Prefer SAE (WPA3) when client inventory allows
```

| Perintah | Kegunaan |
|:---|:---|
| `iw … link` | Menampilkan BSSID, freq, dan signal STA Anda |
| `iw … scan` | Survei lingkungan sekitar (patuhi hukum lokal) |
| `nmcli device wifi` | Mengelola profil Wi-Fi di desktop |

---

> **Referensi & sumber buku**
> - Matthew Gast, *802.11 Wireless Networks: The Definitive Guide*, `~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - IEEE 802.11i / WPA2 RSN, IEEE 802.11w (PMF), tinjauan spesifikasi WPA3 (Wi-Fi Alliance)
> - `man iw`, `man nmcli`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Edukasi dan administrasi WLAN milik sendiri, tanpa prosedur cracking atau injeksi serangan.
