# 🔌 Hardware & IoT Security — Interfaces, Firmware & Automotive

> **LearnCybersecurity** | Hardware & Embedded Security Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Hardware Architecture | Arsitektur embedded & PCB triage | Embedded Systems & PCB Reconnaissance | 組み込みシステムと基板解析 |
| 2 | Hardware Interfaces | Serial UART, JTAG, SPI & I2C | Hardware Debug Protocols (UART/JTAG/SPI) | デバッグインターフェース（UART, JTAG） |
| 3 | Firmware Extraction | Dump flash memory & Binwalk | Firmware Extraction & Binary Unpacking | ファームウェア抽出とBinwalk解析 |
| 4 | Firmware Emulation | Emulasi arsitektur MIPS/ARM (QEMU) | MIPS/ARM Firmware Emulation with QEMU | QEMUによるファームウェアエミュレーション |
| 5 | Automotive / CAN Bus | Protokol Controller Area Network | Automotive Hacking & CAN Bus Exploitation | 車載ネットワーク（CANバス）のセキュリティ |
| 6 | Common IoT Flaws | Hardcoded creds & MQTT flaws | Common IoT Vulnerabilities & Threat Models | IoTデバイスの代表的な脆弱性 |
| 7 | Cheatsheet | Perintah `binwalk`, `minicom`, `can-utils` | Hardware & CAN Bus CLI Cheatsheet | ハードウェア・CANバスチートシート |

---

## 1. 🔍 Embedded Systems & PCB Reconnaissance

### 🇮🇩 Bahasa Indonesia
Hardware hacking berfokus pada analisis fisik perangkat keras (*Printed Circuit Board / PCB*) untuk menemukan titik akses pengujian debug (*test points*), membuang memori chip flash, atau mendapatkan shell root interaktif langsung melalui sirkuit elektronik.

**Langkah-langkah Triage Fisik PCB**:
1. **Identifikasi Komponen Utama**: Catat nomor seri SoC/CPU (misal: MediaTek, Realtek, Broadcom, ESP32, Allwinner) dan chip Flash Memory (SPI Flash 8-pin SOIC).
2. **Cari Test Points & Header Pin**: Cari barisan 4-pin atau 5-pin lubang (*through-hole headers*) yang sering kali merupakan port **UART** atau **JTAG**.
3. **Gunakan Multimeter**:
   - Tentukan **GND (Ground)** dengan mode kontinuitas (*continuity test*) ke pelindung RF atau ground plane.
   - Tentukan **VCC (3.3V atau 5V)** dengan mode voltmeter DC saat perangkat dinyalakan.
   - Tentukan **TX (Transmit)** dengan melihat fluktuasi voltase (3.3V turun ke 2.8V-3.0V) saat proses boot awal (data log ditransmisikan).
   - Tentukan **RX (Receive)** dengan nilai voltase konstan (biasanya 3.3V) yang siap menerima input.

---

## 2. 🔌 Hardware Debug Protocols (UART, JTAG, SPI, I2C)

```
┌─────────────────────────────────────────────────────────────┐
│                 HARDWARE INTERFACE MATRIX                   │
├──────────┬──────────┬───────────────────────────────────────┤
│ Protocol │ Pins     │ Cybersecurity Attack Vector           │
├──────────┼──────────┼───────────────────────────────────────┤
│ **UART** │ TX, RX,  │ Root Interactive Serial Terminal Shell│
│          │ GND, VCC │ (Baud rates: 9600, 115200, 57600)     │
├──────────┼──────────┼───────────────────────────────────────┤
│ **JTAG** │ TDI, TDO,│ Hardware Debugger / Full Memory Dump  │
│          │ TCK, TMS │ & CPU Register Control / Breakpoints  │
├──────────┼──────────┼───────────────────────────────────────┤
│ **SPI**  │ MOSI,MISO│ Direct Flash Memory Chip Read/Dump    │
│          │ SCK, CS  │ (Using Flashrom / CH341A / Bus Pirate)│
├──────────┼──────────┼───────────────────────────────────────┤
│ **I2C**  │ SDA, SCL │ Intercepting sensor / EEPROM bus data │
└──────────┴──────────┴───────────────────────────────────────┘
```

---

## 3. 🧬 Firmware Extraction & Reverse Engineering (Binwalk)

```bash
# ── STEP 1: DUMP RAW SPI FLASH MEMORY DIRECTLY FROM CHIP ────
# Gunakan clip SOIC-8 dengan programmer CH341A USB
flashrom -p ch341a_spi -r firmware_dump.bin

# ── STEP 2: SCAN FOR EMBEDDED COMPRESSED FILESYSTEMS ─────────
binwalk firmware_dump.bin

# ── STEP 3: RECURSIVE EXTRACTION (SQUASHFS / CRAMFS / UBIFS) ─
binwalk -Me firmware_dump.bin

# ── STEP 4: AUDIT EXTRACTED ROOT FILESYSTEM ──────────────────
cd _firmware_dump.bin.extracted/squashfs-root/
grep -rn "password" etc/
cat etc/shadow
find . -name "*.cgi" -o -name "*.sh"
```

---

## 4. 🖥️ Dynamic Firmware Emulation with QEMU

Jika perangkat fisik tidak dapat dinyalakan kembali, analis dapat mengemulasikan binary server web (seperti `httpd` atau `goahead`) pada PC analis x86_64:

```bash
# Salin QEMU user-mode emulator ke direktori root firmware yang diekstrak
sudo cp /usr/bin/qemu-mips-static _firmware.bin.extracted/squashfs-root/
sudo chroot _firmware.bin.extracted/squashfs-root/ ./qemu-mips-static /usr/sbin/httpd
```

---

## 5. 🚗 Automotive Security & CAN Bus (Controller Area Network)

### 🇮🇩 Bahasa Indonesia
**CAN Bus (Controller Area Network)** adalah standar bus komunikasi serial broadcast tanpa master yang menghubungkan seluruh komputer mikro mobil (*Electronic Control Units / ECU*).

- **Karakteristik Kritis CAN Bus**:
  - **Broadcast**: Seluruh node menerima setiap frame di bus.
  - **Tanpa Autentikasi**: ECU mempercayai frame apa pun yang ID-nya valid.
  - **Tanpa Enkripsi**: Payload berupa byte heksadesimal mentah.

```bash
# ── 1. SETUP VIRTUAL / PHYSICAL CAN INTERFACE (SOCKETCAN) ────
# Setup virtual CAN interface untuk latihan lokal
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# ── 2. SNIFF REAL-TIME TRAFFIC (CANDUMP) ─────────────────────
candump vcan0
# Output: vcan0  188   [8]  01 22 00 00 00 00 00 00

# ── 3. VISUAL DELTA ANALYSIS (CANSNIFFER) ────────────────────
# Menyoroti byte yang berubah saat pedal gas diinjak atau pintu dibuka
cansniffer -c vcan0

# ── 4. RECORD TRAFFIC TO FILE ────────────────────────────────
candump -l vcan0 # Menghasilkan candump-2026-08-16.log

# ── 5. REPLAY ATTACK (CANPLAYER) ─────────────────────────────
# Mengulang aksi buka pintu atau menaikkan jarum speedometer
canplayer -I candump-2026-08-16.log

# ── 6. INJECT ARBITRARY FRAME (CANSEND) ──────────────────────
# Mengirim frame dengan CAN ID 0x188 dan 8 byte payload
cansend vcan0 188#0102030405060708
```

---

## 6. 🧠 Quick Reference Cheatsheet

```bash
# ── SERIAL TERMINAL ACCESS VIA UART ──────────────────────────
sudo minicom -D /dev/ttyUSB0 -b 115200
sudo screen /dev/ttyUSB0 115200

# ── IDENTIFY UNKNOWN UART PINOUT (BAUDRATE DETECT) ───────────
python3 -m serial.tools.miniterm /dev/ttyUSB0
```

---

> 📚 **References & Book Sources:**
> - Jasper van Woudenberg & Colin O'Flynn — *The Hardware Hacking Handbook* (`~/Documents/Books/CyberSec/Hardware/`)
> - Fotios Chantzis et al. — *Practical IoT Hacking: The Definitive Guide to Attacking the Internet of Things* (`~/Documents/Books/CyberSec/Hardware/`)
> - Craig Smith — *The Car Hacker's Handbook: A Guide for the Penetration Tester* (`~/Documents/Books/CyberSec/Hardware/`)
> - Aditya Gupta — *The IoT Hacker's Handbook* (`~/Documents/Books/CyberSec/Handbook/`)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
