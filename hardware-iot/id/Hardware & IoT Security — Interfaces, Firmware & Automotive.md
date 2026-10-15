# Hardware & IoT Security, Interfaces, Firmware & Automotive

> **LearnCybersecurity** | Seri Embedded, IoT & Automotive Security
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: *Hardware Hacking Handbook*; *Practical IoT Hacking*; *The Car Hacker's Handbook*, `~/Documents/Books/CyberSec/Hardware/`
> Fokus: konsep antarmuka, arsitektur, dan pertahanan. Bukan resep serangan kendaraan atau payload exploit.

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-070` | **Fase 7:** Spesialisasi
> **Estimasi belajar:** 6-8 jam | **Level:** Lanjutan
> **Prasyarat:** LC-038
> **Peta buku:** van Woudenberg & O'Flynn, The Hardware Hacking Handbook; Chantzis et al., Practical IoT Hacking; Smith, The Car Hacker's Handbook; Gupta, The IoT Hacker's Handbook
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik |
|---|-------|
| 1 | Model ancaman IoT |
| 2 | Antarmuka debug (UART, JTAG, SWD) |
| 3 | Bus papan: SPI / I2C / flash |
| 4 | Konsep firmware |
| 5 | Secure boot & signing |
| 6 | Permukaan jaringan IoT |
| 7 | Arsitektur bus CAN otomotif |
| 8 | Pertahanan keamanan otomotif |
| 9 | Praktik lab pemilik perangkat |
| 10 | Cheatsheet identifikasi & defense |

---

## 1. Model Ancaman Embedded / IoT

Perangkat IoT menggabungkan silikon, firmware, radio/jaringan, dan cloud. Ancaman datang dari jalur fisik (debug port), lokal (Wi-Fi/BLE), dan remote (API cloud).

Risiko paling tinggi kalau aset yang berharga mudah dijangkau dan perlindungannya lemah. Turunkan salah satu dari ketiganya, risikonya ikut turun.

Aset tipikal yang perlu dilindungi: kunci perangkat, kredensial cloud, data sensor, dan fungsi keselamatan (di otomotif, medis, atau industri).

Untuk desain dengan tingkat keyakinan tinggi (set-top box, ECU kendaraan, kontroler industri), anggap saja penyerang punya akses fisik ke perangkat. Kontrol jaringan saja tidak cukup kalau masih ada antarmuka debug terbuka atau jalur update firmware yang tidak ditandatangani.

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  Sensors /  │──▶│  MCU / SoC  │──▶│  Radio/NIC  │──▶ Cloud / Mobile
│  Actuators  │◀──│  + firmware │◀──│  BLE/Wi-Fi  │◀──
└─────────────┘   └──────┬──────┘   └─────────────┘
                         │
                  Debug / flash pads
```

---

## 2. Antarmuka Debug, Identifikasi untuk Pemilik Perangkat

Pemilik perangkat atau security engineer vendor sering perlu mengidentifikasi port debug untuk mengamankannya (menonaktifkan, memutus fuse, atau menambah autentikasi), bukan untuk menyerang perangkat milik orang lain.

### 2.1 UART (Universal Asynchronous Receiver/Transmitter)
| Sinyal | Fungsi |
|:---|:---|
| TX | Transmit data |
| RX | Receive data |
| GND | Ground bersama |
| Vcc | Jangan asal hubung, cek tegangan dulu |

Ciri fisik: 2 sampai 4 test pad berdekatan, kadang ada header dengan silkscreen `TX/RX`. Baud rate yang umum dipakai: 115200, 57600, 9600 (secara konsep).

Pertahanan: nonaktifkan console di production, autentikasi login, atau hapus shell-nya; batasi log yang berisi informasi sensitif.

### 2.2 JTAG / SWD

JTAG (IEEE 1149.1) dipakai untuk boundary scan dan debug. Pin tipikal: `TCK`, `TMS`, `TDI`, `TDO`, `TRST` (opsional).
SWD (ARM) memakai 2 kabel: `SWDIO`, `SWCLK`.

Debug port benar-benar berbahaya kalau ketiga hal ini terjadi bersamaan: pad-nya bisa dijangkau, tidak ada autentikasi, dan fuse debug masih terbuka.

Pertahanan (untuk vendor):
- Nonaktifkan debug di production lewat fuse atau lifecycle state.
- Pakai password atau secure debug authentication kalau debug harus tetap tersedia untuk RMA.
- Epoxy atau underfill bukan kontrol utama, cuma menunda serangan.

```
PCB edge                 SoC
  ○ TCK  ──────────────▶|
  ○ TMS  ──────────────▶|  Debug TAP
  ○ TDI  ──────────────▶|
  ○ TDO  ◀──────────────|
  ○ GND  ───────────────┘
```

Catatan edukasi: langkah eksploitasi debug untuk melewati proteksi produk pihak ketiga tidak disertakan di sini. Fokusnya identifikasi dan penutupan permukaan serangan.

---

## 3. Bus Papan, SPI, I2C & Flash Eksternal

| Bus | Kawat tipikal | Penggunaan | Risiko konsep |
|:---|:---|:---|:---|
| SPI | SCLK, MOSI, MISO, CS | NOR flash firmware | Bisa di-dump kalau CS/flash mudah dijangkau |
| I2C | SDA, SCL | EEPROM, sensor | Data konfigurasi atau kunci yang lemah |
| eMMC / SD | Parallel / SD | Storage OS | Ekstraksi filesystem |

### Layout penyimpanan firmware (konseptual)
```
┌──────────────┬──────────────┬──────────────┬────────────┐
│ Bootloader   │ Kernel / RTOS│ Rootfs / app │ Config/NV  │
│ (+sig?)      │              │              │            │
└──────────────┴──────────────┴──────────────┴────────────┘
```

Pertahanan: enkripsi data non-volatile yang sensitif, ikat secret ke hardware root of trust, dan hindari kredensial plaintext di flash.

---

## 4. Firmware, Konsep Ekstraksi & Analisis

*Practical IoT Hacking* dan *Hardware Hacking Handbook* membahas bagaimana firmware diperoleh untuk analisis keamanan. Di catatan ini fokusnya konsep dan tujuan defensif saja.

### Sumber firmware yang sah
| Sumber | Kapan relevan |
|:---|:---|
| Paket update dari vendor | Analisis supply chain / integritas update |
| Build artifact internal | SDL vendor |
| Perangkat milik sendiri + lab berizin | Research pada unit yang dibeli |
| Rilis open source | Audit komunitas |

### Tujuan analisis (defense)
1. Temukan hardcoded credential atau backdoor service.
2. Verifikasi apakah update sudah ditandatangani.
3. Petakan layanan jaringan yang listening.
4. Periksa konfigurasi TLS dan certificate store.
5. Identifikasi versi komponen untuk mencocokkan dengan CVE yang sudah diketahui.

Update firmware hanya aman kalau sudah ditandatangani, rantai tanda tangannya diverifikasi, dan versi lama yang rentan tidak bisa dipasang lagi (anti-rollback).

Konsep static analysis: unpack image (tool sekelas binwalk di lab), ekstraksi filesystem, triase string, review konfigurasi.
Dynamic: pakai emulator atau test harness pada image milik sendiri, bukan menyasar fleet perangkat orang lain.

---

## 5. Secure Boot, Measured Boot & Firmware Signing

### Rantai secure boot
```
ROM root key
    │ verify
    ▼
Bootloader
    │ verify
    ▼
Kernel / OS image
    │ verify
    ▼
dm-verity / app containers (opsional)
```

| Mekanisme | Fungsi |
|:---|:---|
| Secure boot | Menolak image tanpa tanda tangan valid |
| Measured boot | Mencatat hash ke PCR/TPM untuk attestation |
| Anti-rollback | Menolak versi lama yang sudah diketahui rentan |
| Hardware root of trust | Kunci disimpan di fuse, OTP, atau HSM on-SoC |

### Model signing
```text
σ = Sign(private key vendor, Hash(image))

image hanya diterima jika:
  Verify(pk, image, σ) = OK   dan   versi ≥ versi minimum yang diizinkan
```

Kegagalan klasik yang sering terjadi: debug boot masih diaktifkan, kunci privat vendor bocor, atau verifikasi diimplementasikan di software yang mudah di-patch tanpa perlindungan fuse.

---

## 6. Permukaan Jaringan & Cloud IoT

| Lapisan | Contoh | Hardening |
|:---|:---|:---|
| Radio lokal | BLE, Zigbee, Wi-Fi AP | Pairing PIN kuat, disable WPS, rotasi key |
| Layanan LAN | Telnet/HTTP legacy | Hapus, hanya pakai HTTPS/SSH, patch rutin |
| Cloud API | Device ke broker MQTT/HTTP | Mutual TLS, token dengan hak akses minimal |
| Mobile companion | App pengawasan | Secure storage, cert pinning yang matang |
| Kanal update | OTA | Signed OTA + anti-rollback |

Identitas device dengan least privilege: setiap device punya identitas unik, jangan pakai satu global key untuk seluruh fleet.

Dengan begitu, membobol satu device tidak otomatis memberi penyerang akses ke semua device lain di fleet, asalkan kuncinya unik dan dirotasi.

---

## 7. Arsitektur Bus CAN (Otomotif)

*The Car Hacker's Handbook* menjelaskan bahwa kendaraan modern pada dasarnya adalah jaringan ECU. CAN (Controller Area Network) adalah bus serial differential yang paling banyak dipakai.

### Properti arsitektur
| Properti | Arti |
|:---|:---|
| Multimaster | Banyak ECU bisa transmit |
| Priority by ID | ID lebih rendah berarti prioritas lebih tinggi |
| Broadcast | Frame terlihat oleh semua node di bus yang sama |
| Tanpa auth bawaan (versi klasik) | Frame tidak "login", kepercayaan = akses ke bus |

```
ECU_A ----+------ ECU_B ------+------ ECU_C
          |                   |
         CAN_H / CAN_L differential pair
```

### Frame (konsep)
```text
CAN frame = ID (isi pesannya tentang apa) | DLC (panjang data) | Data (0-8 byte) | CRC (cek error)
```

ISO-TP / UDS memakai CAN sebagai transport untuk diagnostik, ini permukaan yang harus dikontrol ketat.

### Domain tipikal di kendaraan
| Domain | Contoh fungsi | Sensitivitas |
|:---|:---|:---|
| Powertrain | Engine / transmission | Safety-critical |
| Chassis | ABS / steering assist | Safety-critical |
| Body | Jendela / kunci pintu | Kenyamanan + keamanan |
| Infotainment | Media / aplikasi | Titik masuk serangan yang tinggi |
| OBD-II | Port diagnostik | Titik masuk fisik |
| Telematics | Modem seluler | Titik masuk remote |

---

## 8. Pertahanan Keamanan Otomotif

Fokus untuk pembaca security engineer di sini adalah segmentasi dan kontrol, bukan skrip serangan.

| Pertahanan | Deskripsi |
|:---|:---|
| Gateway ECU | Filter/policy antar domain CAN/Ethernet |
| Segmentasi bus | Mengisolasi infotainment dari domain safety |
| Secure diagnostics | Autentikasi sebelum sesi UDS yang sensitif |
| Signed firmware per ECU | Secure boot untuk tiap ECU |
| IDS/IPS kendaraan | Deteksi anomali ID/frekuensi frame (dari vendor) |
| Kebijakan akses OBD | Membatasi dongle aftermarket, edukasi pengguna |
| Hardening telematics | Patch modem, mutual auth ke cloud |
| Supply chain | Code review untuk ECU dari supplier |

```
Infotainment ──X──▶ Safety CAN
       │              ▲
       ▼              │ policy
   Gateway ECU ───────┘
       │
       ▼
   Telematics (auth'd)
```

Makin ketat aturan filter di gateway dan makin rapi pemisahan domainnya, makin sulit penyerang melompat dari satu bagian mobil (misalnya infotainment) ke bagian lain (misalnya rem).

Aturan tegas: catatan ini tidak menyediakan skrip injeksi CAN, resep replay attack, atau cara bypass immobilizer. Memahami arsitektur berguna untuk desain defensif dan assessment yang berizin.

---

## 9. Praktik Lab Pemilik Perangkat / Vendor

Praktik aman pada perangkat yang Anda miliki atau di laboratorium berizin:

1. Foto board, dokumentasikan silkscreen dan test pad.
2. Ukur tegangan sebelum menghubungkan adapter apapun (3.3V vs 5V).
3. Buat inventaris port debug, lalu rencanakan penutupannya sebelum production.
4. Ambil firmware dari saluran update resmi, verifikasi tanda tangannya.
5. Scan layanan jaringan di Wi-Fi lab yang terisolasi.
6. Catat temuan sebagai backlog SAST/hardening, bukan exploit chain publik tanpa koordinasi.

| Jangan | Lakukan |
|:---|:---|
| Probe ECU kendaraan orang lain | Belajar di training ECU atau lab yang legal |
| Publikasikan bypass safety | Koordinasikan disclosure dengan vendor |
| Abaikan tegangan pin | Ukur dengan multimeter dulu |
| Pakai global shared cloud key | Pakai kredensial per-device |

---

## 10. Cheatsheet, Identifikasi & Pertahanan

```text
HARDWARE SURFACE CHECK (owner/vendor)
[ ] UART pads present? → disable console / auth in prod
[ ] JTAG/SWD exposed? → fuse/disable/secure debug
[ ] External flash readable? → encrypt secrets; signed images
[ ] OTA signed + anti-rollback?
[ ] Unique device identity (no fleet-wide key)?
[ ] Cloud API: mTLS / scoped tokens?
[ ] Automotive: gateway between IVI and safety domains?
[ ] Diagnostics: authenticated UDS sessions?
```

| Antarmuka | Petunjuk identifikasi | Pertahanan utama |
|:---|:---|:---|
| UART | 3-4 pad, label TX/RX | Nonaktifkan shell, jangan log secret |
| JTAG | 5+ pad atau footprint 10/20-pin | Nonaktifkan di lifecycle / auth |
| SWD | 2 kabel dekat MCU | Sama seperti JTAG |
| SPI flash | NOR 8-pin dekat SoC | Secure boot + enkripsi NV |
| OBD-II | Konektor di kabin | Kebijakan akses + diagnostik berautentikasi |
| CAN | Twisted pair ke ECU | Gateway dan segmentasi |

---

## Catatan Keamanan, Ancaman & Pertahanan

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Penyalahgunaan debug | UART/JTAG terbuka | Nonaktifkan/fuse/auth debug |
| Firmware clone / implant | Update tanpa tanda tangan | Secure boot + anti-rollback |
| Bocornya key fleet | Symmetric key yang dibagi bersama | Key per-device + rotasi |
| Pengambilalihan akun cloud | Pairing yang lemah | Provisioning kuat, MFA di akun pemilik |
| Infotainment tembus ke safety | Jaringan flat | Filtering gateway / isolasi domain |
| Dongle OBD berbahaya | Akses ke bus | Edukasi pengguna, diagnostik dibatasi |
| Backdoor di supply chain | Kode ECU pihak ketiga | Audit, SBOM, signing |

Tidak dibahas di sini: skrip serangan CAN, cara mengalahkan immobilizer, penyalahgunaan airbag/safety, atau playbook RCE untuk ECU.

---

> **Referensi dan Sumber Buku**
> - *The Hardware Hacking Handbook*, `~/Documents/Books/CyberSec/Hardware/`
> - *Practical IoT Hacking: The Definitive Guide to Attacking the Internet of Things*, `~/Documents/Books/CyberSec/Hardware/` (diadaptasi untuk defense & assessment oleh pemilik)
> - *The Car Hacker's Handbook*, `~/Documents/Books/CyberSec/Hardware/` (diadaptasi untuk arsitektur CAN + pertahanan)
> - Industri: UNECE WP.29 / ISO/SAE 21434 (gambaran umum proses cybersecurity otomotif)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi ini untuk edukasi dan pengamanan perangkat milik sendiri atau lab berizin. Bukan untuk mengganggu kendaraan atau perangkat orang lain.
