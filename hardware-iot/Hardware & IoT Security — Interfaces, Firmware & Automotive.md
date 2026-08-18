# 🔌 Hardware & IoT Security — Interfaces, Firmware & Automotive

> **LearnCybersecurity** | Embedded, IoT & Automotive Security Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: *Hardware Hacking Handbook*; *Practical IoT Hacking*; *The Car Hacker’s Handbook* — `~/Documents/Books/CyberSec/Hardware/`  
> ⚠️ Fokus: konsep antarmuka, arsitektur, dan **pertahanan**. Bukan resep serangan kendaraan atau payload exploit.

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-070` | **Phase 7:** Specialized  
> **Est. study:** 6-8h | **Level:** Advanced  
> **Prerequisites:** LC-038  
> **Book map:** van Woudenberg & O'Flynn Â The Hardware Hacking Handbook; Chantzis et al. Â Practical IoT Hacking; Smith Â The Car Hacker's Handbook; Gupta Â The IoT Hacker's Handbook
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Embedded Threat Model | Model ancaman IoT | IoT threat model | IoT脅威モデル |
| 2 | Debug Interfaces | UART, JTAG, SWD | Debug ports | デバッグインタフェース |
| 3 | SPI / I²C / Flash | Bus & penyimpanan | Board buses | 基板バス |
| 4 | Firmware Concepts | Ekstraksi & analisis konsep | Firmware concepts | ファームウェア概念 |
| 5 | Secure Boot & Signing | Boot aman | Secure boot | セキュアブート |
| 6 | IoT Network Surface | Permukaan jaringan | Network surface | ネットワーク面 |
| 7 | CAN Architecture | Bus CAN otomotif | CAN bus architecture | CANアーキテクチャ |
| 8 | Automotive Defenses | Segmentasi & hardening | Auto defenses | 自動車の防御 |
| 9 | Owner Lab Practice | Praktik pemilik perangkat | Device-owner lab | 所有者ラボ |
| 10 | Cheatsheet | Identifikasi & defense | Cheatsheet | チートシート |

---

## 1. 🎯 Embedded / IoT Threat Model

### 🇮🇩 Bahasa Indonesia
Perangkat IoT menggabungkan **silikon + firmware + radio/jaringan + cloud**. Ancaman datang dari fisik (debug port), lokal (Wi-Fi/BLE), dan remote (API cloud).

$$
\mathsf{Risk} = \mathsf{AssetValue} \times \mathsf{Exposure} \times \mathsf{WeakControl}
$$

Aset tipikal: kunci perangkat, kredensial cloud, data sensor, safety functions (otomotif/medis/industri).

### 🇬🇧 English
Assume physical possession for high-assurance designs (set-top, vehicle ECU, industrial controller). Network controls alone fail if debug interfaces or unsigned firmware update paths exist.

### 日本語
高保証設計では物理アクセスを前提にします。デバッグポートと未署名アップデートが弱点になりやすいです。

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  Sensors /  │──▶│  MCU / SoC  │──▶│  Radio/NIC  │──▶ Cloud / Mobile
│  Actuators  │◀──│  + firmware │◀──│  BLE/Wi-Fi  │◀──
└─────────────┘   └──────┬──────┘   └─────────────┘
                         │
                  Debug / flash pads
```

---

## 2. 🧪 Debug Interfaces — Identification for Device Owners

Pemilik perangkat / vendor security engineer sering perlu **mengidentifikasi** port debug untuk mengamankan (disable, fuse, authenticate) — bukan untuk menyerang milik orang lain.

### 2.1 UART (Universal Asynchronous Receiver/Transmitter)
| Sinyal | Fungsi |
|:---|:---|
| TX | Transmit data |
| RX | Receive data |
| GND | Ground bersama |
| Vcc | Jangan asal hubung — cek tegangan! |

Ciri fisik: 2–4 test pad berdekatan; kadang header silkscreen `TX/RX`. Baud rate umum: 115200, 57600, 9600 (konsep).

**Defense:** nonaktifkan console di production, autentikasi login, atau hapus shell; batasi log sensitif.

### 2.2 JTAG / SWD
**JTAG** (IEEE 1149.1) — boundary scan + debug. Pin tipikal: `TCK`, `TMS`, `TDI`, `TDO`, `TRST` (opsional).  
**SWD** (ARM) — 2-wire: `SWDIO`, `SWCLK`.

$$
\mathsf{DebugExposure} = [\mathsf{PadsAccessible}] \land [\mathsf{AuthAbsent}] \land [\mathsf{FuseOpen}]
$$

**Defense (vendor):**
- Disable debug di production fuse / lifecycle state.
- Password / secure debug authentication bila debug harus tetap ada untuk RMA.
- Epoxy / underfill **bukan** kontrol utama — hanya delay.

```
PCB edge                 SoC
  ○ TCK  ──────────────▶|
  ○ TMS  ──────────────▶|  Debug TAP
  ○ TDI  ──────────────▶|
  ○ TDO  ◀──────────────|
  ○ GND  ───────────────┘
```

> Catatan edukasi: langkah eksploitasi debug untuk melewati proteksi produk pihak ketiga **tidak** disertakan. Fokus identifikasi & penutupan permukaan.

---

## 3. 📶 Board Buses — SPI, I²C & External Flash

| Bus | Kawat tipikal | Penggunaan | Risiko konsep |
|:---|:---|:---|:---|
| **SPI** | SCLK, MOSI, MISO, CS | NOR flash firmware | Dump jika CS/flash exposed |
| **I²C** | SDA, SCL | EEPROM, sensor | Data konfigurasi / kunci lemah |
| **eMMC / SD** | Parallel / SD | Storage OS | Ekstraksi filesystem |

### Firmware storage layout (konseptual)
```
┌──────────────┬──────────────┬──────────────┬────────────┐
│ Bootloader   │ Kernel / RTOS│ Rootfs / app │ Config/NV  │
│ (+sig?)      │              │              │            │
└──────────────┴──────────────┴──────────────┴────────────┘
```

**Defense:** encrypt sensitive NV; bind secrets to hardware root of trust; avoid plaintext credentials in flash.

---

## 4. 📦 Firmware — Extraction & Analysis Concepts

*Practical IoT Hacking* / *Hardware Hacking Handbook* membahas bagaimana firmware didapat untuk **analisis keamanan**. Di catatan ini: **konsep & tujuan defensif**.

### Sumber firmware (sah)
| Sumber | Kapan relevan |
|:---|:---|
| Vendor update package | Analisis supply chain / update integrity |
| Build artifact internal | SDL vendor |
| Device you own + authorized lab | Research on purchased unit |
| Open source release | Audit komunitas |

### Tujuan analisis (defense)
1. Temukan hardcoded credential / backdoor service.
2. Verifikasi apakah update ditandatangani.
3. Petakan layanan jaringan yang listening.
4. Periksa konfigurasi TLS / certificate store.
5. Identifikasi versi komponen → CVE known.

$$
\mathsf{UpdateSafe} \iff \mathsf{Signed} \land \mathsf{VerifiedChain} \land \mathsf{AntiRollback}
$$

**Static analysis concepts:** unpack (binwalk-class tools in lab), filesystem extract, string triage, configuration review.  
**Dynamic:** emulator / test harness pada image yang Anda miliki — bukan targeting fleet orang lain.

---

## 5. 🔐 Secure Boot, Measured Boot & Firmware Signing

### Secure boot chain
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
| **Secure boot** | Tolak image tanpa tanda tangan valid |
| **Measured boot** | Catat hash ke PCR/TPM untuk attestation |
| **Anti-rollback** | Tolak versi lebih lama yang rentan |
| **Hardware root of trust** | Kunci di fuse/OTP/HSM on-SoC |

### Signing model
$$
\begin{aligned}
\sigma &= \mathsf{Sign}_{sk_{vendor}}(\mathsf{Hash}(image)) \\
\mathsf{Accept} &\iff \mathsf{Verify}_{pk}(image,\sigma)=1 \land \mathsf{version} \ge v_{\min}
\end{aligned}
$$

**Kegagalan klasik:** debug boot enabled; kunci privat vendor bocor; verifikasi diimplementasikan di software yang mudah di-patch tanpa fuse.

---

## 6. 🌐 IoT Network & Cloud Surface

| Lapisan | Contoh | Hardening |
|:---|:---|:---|
| Local radio | BLE, Zigbee, Wi-Fi AP | Pairing PIN kuat; disable WPS; rotate keys |
| LAN services | Telnet/HTTP legacy | Hapus; HTTPS/SSH saja; patch |
| Cloud API | Device ↔ broker MQTT/HTTP | Mutual TLS; least privilege tokens |
| Mobile companion | Oversight app | Secure storage; cert pinning maturity |
| Update channel | OTA | Signed OTA + anti-rollback |

**Least privilege device identity:** setiap device = identitas unik; jangan satu global key untuk seluruh fleet.

$$
\mathsf{CompromiseOne} \not\Rightarrow \mathsf{CompromiseFleet}
\quad \text{(jika key unik + rotate)}
$$

---

## 7. 🚗 CAN Bus Architecture (Automotive)

*The Car Hacker’s Handbook* menjelaskan bahwa kendaraan modern adalah jaringan ECU. **CAN (Controller Area Network)** adalah bus serial differential yang banyak dipakai.

### Properti arsitektur
| Properti | Arti |
|:---|:---|
| Multimaster | Banyak ECU bisa transmit |
| Priority by ID | ID lebih rendah = prioritas lebih tinggi |
| Broadcast | Frame terlihat oleh node di bus yang sama |
| No built-in auth (klasik) | Frame tidak “login” — kepercayaan = akses bus |

```
ECU_A ----+------ ECU_B ------+------ ECU_C
          |                   |
         CAN_H / CAN_L differential pair
```

### Frame (konsep)
$$
\mathsf{CANFrame} \approx \langle \mathsf{ID},\; \mathsf{DLC},\; \mathsf{Data}_{0..8},\; \mathsf{CRC} \rangle
$$

ISO-TP / UDS memakai CAN sebagai transport untuk diagnostik — permukaan yang harus dikontrol ketat.

### Domain tipikal di kendaraan
| Domain | Contoh fungsi | Sensitivitas |
|:---|:---|:---|
| Powertrain | Engine / transmission | Safety-critical |
| Chassis | ABS / steering assists | Safety-critical |
| Body | Windows / locks | Convenience + security |
| Infotainment | Media / apps | High attack entry |
| OBD-II | Diagnostics port | Physical entry point |
| Telematics | Cellular modem | Remote entry point |

---

## 8. 🛡️ Automotive Security Defenses

Fokus handbook untuk pembaca security engineer: **segmentasi & kontrol**, bukan skrip serangan.

| Defense | Deskripsi |
|:---|:---|
| **Gateway ECU** | Filter / policy antar domain CAN/Ethernet |
| **Segmentasi bus** | Isolasi infotainment dari safety domains |
| **Secure diagnostics** | Auth sebelum UDS sesi sensitif |
| **Signed firmware ECU** | Secure boot per ECU |
| **IDS/IPS kendaraan** | Deteksi anomali ID/frekuensi frame (vendor) |
| **OBD access policy** | Batasi aftermarket dongle; user awareness |
| **Telematics hardening** | Patch modem; mutual auth ke cloud |
| **Supply chain** | Code review supplier ECUs |

```
Infotainment ──X──▶ Safety CAN
       │              ▲
       ▼              │ policy
   Gateway ECU ───────┘
       │
       ▼
   Telematics (auth'd)
```

$$
\mathsf{LateralMoveHard} \propto \mathsf{GatewayPolicyStrength} \times \mathsf{DomainIsolation}
$$

> **Hard rule:** catatan ini tidak menyediakan skrip injeksi CAN, replay attack recipes, atau bypass immobilizer. Memahami arsitektur berguna untuk **defensive design & assessment berizin**.

---

## 9. 🧰 Device-Owner / Vendor Lab Practice

Praktik aman pada perangkat yang Anda miliki atau laboratorium berizin:

1. Foto board; dokumentasikan silkscreen & test pads.
2. Ukur tegangan **sebelum** menghubungkan adapter (3.3V vs 5V).
3. Inventaris port debug → rencana penutupan produksi.
4. Ambil firmware dari saluran update resmi; verifikasi tanda tangan.
5. Scan layanan jaringan pada Wi-Fi lab terisolasi.
6. Catat temuan sebagai SAST/hardening backlog — bukan exploit chain publik tanpa koordinasi.

| Jangan | Lakukan |
|:---|:---|
| Probe ECU kendaraan orang lain | Pelajari pada training ECU / legal lab |
| Publikasikan bypass safety | Vendor disclosure berkoordinasi |
| Abaikan tegangan pin | Multimeter dulu |
| Global shared cloud key | Per-device credentials |

---

## 10. 🛠️ Cheatsheet — Identify & Defend

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

| Interface | Identify hint | Primary defense |
|:---|:---|:---|
| UART | 3–4 pads, TX/RX labels | Disable shell; no secrets in log |
| JTAG | 5+ pads or 10/20-pin footprint | Lifecycle disable / auth |
| SWD | 2-wire near MCU | Same as JTAG |
| SPI flash | 8-pin NOR near SoC | Secure boot + encrypt NV |
| OBD-II | Cabin connector | Policy + authenticated diag |
| CAN | Twisted pair to ECUs | Gateway & segmentation |

---

## 🔐 Security Notes — Threats & Defenses

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Debug abuse | Open UART/JTAG | Disable/fuse/auth debug |
| Firmware clone / implant | Unsigned update | Secure boot + anti-rollback |
| Fleet key leak | Shared symmetric key | Per-device keys + rotation |
| Cloud account takeover | Weak pairing | Strong provisioning; MFA on owner account |
| IVI → safety crossover | Flat network | Gateway filtering / domain isolation |
| Malicious OBD dongle | Bus access | User education; restricted diag |
| Supply-chain backdoor | Third-party ECU code | Audit, SBOM, signing |

> **Tidak dibahas:** CAN attack scripts, immobilizer defeat, airbag/safety misuse, atau RCE playbook ECU.

---

> 📚 **References & Book Sources**
> - *The Hardware Hacking Handbook* — `~/Documents/Books/CyberSec/Hardware/`
> - *Practical IoT Hacking: The Definitive Guide to Attacking the Internet of Things* — `~/Documents/Books/CyberSec/Hardware/` (adaptasi: defense & owner assessment)
> - *The Car Hacker’s Handbook* — `~/Documents/Books/CyberSec/Hardware/` (adaptasi: arsitektur CAN + defenses)
> - Industry: UNECE WP.29 / ISO/SAE 21434 (automotive cybersecurity process — overview)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & pengamanan perangkat milik sendiri / lab berizin. Tidak untuk mengganggu kendaraan atau perangkat orang lain.
