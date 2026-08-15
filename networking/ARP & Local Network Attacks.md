# 🌐 ARP Protocol & Local Network Attacks

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | ARP Protocol | Protokol resolusi IP ke MAC | ARP Protocol & Cache Architecture | ARPプロトコルの仕組みとキャッシュ |
| 2 | ARP Request/Reply | Alur request & reply frame | Frame Exchange & Resolution Flow | ARPリクエストとリプライのフロー |
| 3 | ARP Spoofing / Poisoning | Serangan manipulasi cache ARP | ARP Poisoning & MITM Mechanics | ARPスプーフィングとMITM攻撃 |
| 4 | MITM Attack Scenarios | Intersepsi traffic, SSL Stripping | Traffic Interception & Credential Sniffing | トラフィック傍受とSSLストリッピング |
| 5 | Detection & Defense | Deteksi arping, DAI & static ARP | ARP Detection, DAI & Hardening | ARP攻撃の検知と対策（DAI） |
| 6 | Cheatsheet | Perintah `arp`, `bettercap`, `dsniff` | Attack & Defensive Cheatsheet | ARPコマンドと攻撃ツールチートシート |

---

## 1. 🔍 ARP Protocol & Resolution Architecture

### 🇮🇩 Bahasa Indonesia
**ARP (Address Resolution Protocol - RFC 826)** beroperasi di perbatasan antara Layer 2 (Data Link) dan Layer 3 (Network). Tugas utamanya adalah memetakan **IP Address logis** (Layer 3) ke **MAC Address fisik perangkat keras** (Layer 2) di dalam satu subnet *broadcast domain* lokal.

ARP tidak memiliki mekanisme autentikasi — setiap host akan memercayai balasan (*reply*) ARP yang diterimanya, bahkan jika host tersebut tidak pernah meminta request sebelumnya (*gratuitous ARP*). Kelemahan desain mendasar inilah yang menjadi celah bagi **ARP Spoofing**.

---

## 2. 🔄 ARP Frame Exchange Flow

```
Host A (192.168.1.10) wants to send packet to Host B (192.168.1.20)
  │
  ├── 1. Check local ARP Cache (`arp -a`). If entry missing:
  │
  ├── 2. [BROADCAST] "Who has 192.168.1.20? Tell 192.168.1.10" ───> FF:FF:FF:FF:FF:FF (All hosts)
  │                                                                       │
  │<── 3. [UNICAST]  "192.168.1.20 is at 00:11:22:33:44:55" ─────────── Host B replies
  │
  └── 4. Host A updates local ARP cache and transmits Ethernet Frame.
```

---

## 3. 🏴‍☠️ ARP Spoofing / Poisoning (Man-in-the-Middle)

### 🇮🇩 Bahasa Indonesia
Dalam serangan **ARP Cache Poisoning**:
1. Penyerang mengirimkan paket balasan ARP palsu (*Gratuitous ARP Reply*) secara terus-menerus ke **Target Host** dan **Default Gateway (Router)**.
2. Penyerang memberi tahu Target: *"Saya adalah Gateway (IP 192.168.1.1 ada di MAC Penyerang)"*.
3. Penyerang memberi tahu Gateway: *"Saya adalah Target (IP 192.168.1.10 ada di MAC Penyerang)"*.
4. Akibatnya, seluruh lalu lintas internet dari Target dialihkan melewati mesin Penyerang sebelum diteruskan ke Router asli.

```
                  ┌────────────────────────┐
                  │   Attacker (Kali)      │
                  │ MAC: AA:AA:AA:AA:AA:AA │
                  └───────────┬────────────┘
                              │
            ┌─────────────────┴─────────────────┐
            │                                   │
            ▼ (Forwarded Traffic)               ▼ (Forwarded Traffic)
 ┌──────────────────────┐             ┌──────────────────────┐
 │     Victim PC        │             │   Default Gateway    │
 │ IP: 192.168.1.50     │             │ IP: 192.168.1.1      │
 │ MAC: BB:BB:BB:BB:BB  │             │ MAC: CC:CC:CC:CC:CC  │
 └──────────────────────┘             └──────────────────────┘
```

---

## 4. 🔐 Security Notes — MITM Exploitation & Defense

### 1. Enabling IP Forwarding (Attacker Machine)
Agar koneksi internet korban tidak putus saat serangan berlangsung, penyerang wajib mengaktifkan packet forwarding di kernel Linux:
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

### 2. Tools & Attack Execution
- **`arpspoof` (dsniff suite)**:
  ```bash
  # Poison victim -> gateway
  sudo arpspoof -i eth0 -t 192.168.1.50 192.168.1.1
  # Poison gateway -> victim
  sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.50
  ```
- **`bettercap`**:
  ```bash
  sudo bettercap -iface eth0
  set arp.spoof.targets 192.168.1.50
  arp.spoof on
  net.sniff on
  ```

### 3. Defensive Countermeasures
- **Dynamic ARP Inspection (DAI)**: Fitur switch enterprise (Cisco) yang memvalidasi setiap frame ARP terhadap database *DHCP Snooping binding table*.
- **Static ARP Tables**: Mengunci MAC gateway secara permanen pada endpoint kritis:
  ```bash
  sudo arp -s 192.168.1.1 00:11:22:33:44:55
  ```

---

## 5. 🧠 Quick Reference Cheatsheet

```bash
# ── VIEW & MANAGE ARP TABLE ──────────────────────────────────
ip neighbor show               # Modern Linux ARP table inspection
arp -a                         # Legacy ARP table view
sudo ip neigh flush all        # Clear local ARP cache

# ── DETECTION & SCANNING ─────────────────────────────────────
sudo arp-scan -l               # Scan local subnet via ARP
sudo arpwatch -i eth0          # Monitor and log ARP MAC changes
```

---

> 📚 **References & Book Sources:**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach (6th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Christian Benvenuti — *Understanding Linux Network Internals* (`~/Documents/Books/CyberSec/Networking/`)
> - Georgia Weidman — *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Peter Kim — *The Hacker Playbook 3: Practical Guide To Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - `man 7 arp`, `man arpspoof`, `man arp-scan`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
