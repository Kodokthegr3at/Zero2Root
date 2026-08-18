# 📡 Wireless 802.11 Security & Attacks

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: *802.11 Wireless Networks: The Definitive Guide*; Stallings — *Network Security Essentials*; Kurose & Ross — *Computer Networking*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-043` | **Phase 2:** Networking  
> **Est. study:** 5h | **Level:** Advanced  
> **Prerequisites:** LC-038  
> **Book map:** Gast Â 802.11 Wireless Networks (full); Stallings Â Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | 802.11 Overview | Framing & arsitektur | Frames & BSS model | フレームとBSS |
| 2 | Security Evolution | WEP→WPA2→WPA3 | Protocol history | セキュリティ進化 |
| 3 | WPA2 Handshake | PMK / PTK / GTK | 4-way handshake math | 4ウェイハンドシェイク |
| 4 | WPA3 SAE | Konsep SAE | Dragonfly high-level | SAEの概要 |
| 5 | Management Frames | Deauth sebagai DoS | Deauth DoS concept | デオーズの概念 |
| 6 | Defenses | Monitoring & harden | Detection & controls | 防御と監視 |
| 7 | Security Notes | Checklist | Defense summary | 防御まとめ |
| 8 | Cheatsheet | iw / NetworkManager | Admin CLI | 管理CLI |

---

## 1. 📶 802.11 Architecture & Framing Overview

### 🇮🇩 Bahasa Indonesia
**IEEE 802.11** mendefinisikan WLAN: stasiun (**STA**), access point (**AP**), dan **BSS** (Basic Service Set). Beberapa BSS dengan SSID sama dapat membentuk **ESS**. Media half-duplex; akses kanal memakai **CSMA/CA** (bukan CSMA/CD Ethernet klasik).

Tiga kelas frame:

| Kelas | Peran | Contoh |
|:---|:---|:---|
| **Data** | Muatan LLC/IP | QoS data |
| **Control** | Bantu akses medium | RTS/CTS, ACK |
| **Management** | Keanggotaan & discovery | Beacon, Probe, Auth, Assoc, Deauth, Disassoc |

```
  ┌────────────── ESS / SSID "CORP" ──────────────┐
  │   AP1 (BSS1)              AP2 (BSS2)          │
  │    ↑↑↑                     ↑↑↑                │
  │   STA                      STA                │
  └───────────────────────────────────────────────┘
         │
         └── wired DS (Distribution System) ──► LAN/Internet
```

**Beacon** mengumumkan SSID (atau hidden), kapabilitas, security IE (RSN). **Association** mengikat STA ke AP sebelum data unicast terenkripsi (pada jaringan modern).

Header 802.11 memakai beberapa alamat (ToDS/FromDS) untuk membedakan SA/DA/BSSID — detail lengkap di buku O'Reilly *802.11 Wireless Networks*.

### 🇬🇧 English
Wireless is a **shared broadcast medium** within radio range: confidentiality and integrity depend on link-layer security (RSN), not on “being indoors.” Always assume nearby receivers can hear unprotected management and poorly configured networks.

### 🇯🇵 日本語
無線は電波の届く範囲で共有媒体です。機密性はRSN等のリンク層保護に依存します。

---

## 2. 🔐 Security Evolution (Brief)

| Era | Mekanisme | Status praktis |
|:---|:---|:---|
| Open | Tanpa enkripsi link | Hanya untuk captive portal + TLS app |
| **WEP** | RC4 + IV lemah | **Deprecated / broken** — jangan dipakai |
| WPA-PSK (TKIP) | Transisi | Legacy; hindari jika bisa |
| **WPA2-Personal** | PSK + CCMP (AES) | Masih umum; PSK lemah = risiko |
| **WPA2-Enterprise** | 802.1X / EAP + RADIUS | Standar kantor |
| **WPA3-Personal** | **SAE** | Resistensi offline PSK-guess lebih baik |
| **WPA3-Enterprise** | EAP + opsi 192-bit suite | High assurance |

**RSN (Robust Security Network)** IE di Beacon menyatakan cipher & AKM yang ditawarkan. **CCMP** (AES-CCM) adalah cipher data WPA2 yang diharapkan; **GCMP** muncul di PHY lebih baru / WPA3 contexts.

---

## 3. 🔑 WPA2 — PMK, PTK, GTK & 4-Way Handshake

### 🇮🇩 Bahasa Indonesia
Tujuan handshake: dari rahasia jangka panjang, turunkan kunci sesi **segar** dan konfirmasi kepemilikan bersama tanpa mengirim PSK cleartext di udara.

**PMK (Pairwise Master Key):**

- **Personal (PSK):** PMK diturunkan dari passphrase + SSID (PBKDF2-HMAC-SHA1, 4096 iterasi pada WPA2-PSK klasik):

$$
\mathsf{PMK} = \mathsf{PBKDF2}(\mathsf{passphrase},\; \mathsf{SSID},\; 4096,\; 256\text{ bits})
$$

- **Enterprise:** PMK hasil dari EAP / MSK setelah 802.1X sukses (per sesi/user, lebih baik dari PSK bersama).

**PTK (Pairwise Transient Key)** diturunkan dari PMK + nonces + MAC:

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

di mana $AA$ = AP MAC (BSSID), $SPA$ = STA MAC. PTK dipecah menjadi:

| Bagian | Fungsi |
|:---|:---|
| KCK | Key Confirmation Key (MIC pada EAPOL-Key) |
| KEK | Key Encryption Key (bungkus key material) |
| TK | Temporal Key untuk CCMP data unicast |

**GTK (Group Temporal Key):** kunci multicast/broadcast dari AP ke semua STA terasosiasi; didistribusikan terbungkus selama handshake / group key handshake.

### 4-Way Handshake (EAPOL-Key) — alur konsep

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

Verifikasi MIC dengan KCK membuktikan kedua pihak menurunkan PTK sama ⇒ memiliki PMK yang sama.

### 🇬🇧 English
Security of WPA2-Personal collapses to **PSK entropy**. A low-entropy passphrase enables **offline** guessing against captured handshake material — this note does **not** document cracking procedures. Mitigation: long random PSK, prefer **WPA3-SAE** or **Enterprise (802.1X)**.

### 🇯🇵 日本語
WPA2-Personalの強度はパスフレーズのエントロピーに依存します。推測しやすいPSKは避け、WPA3またはEnterpriseを優先します。

---

## 4. 🐉 WPA3-Personal — SAE (High-Level)

### 🇮🇩 Bahasa Indonesia
**SAE (Simultaneous Authentication of Equals)** berbasis protokol **Dragonfly** (password-authenticated key exchange). Kedua pihak membuktikan pengetahuan password lewat interaksi **online** di grup eliptik / finite field, lalu menghasilkan PMK.

Sifat yang diinginkan (intuisi):

| Properti | Makna operasional |
|:---|:---|
| PAKE | Password tidak dipakai sebagai PSK “hashable” gaya WPA2 yang sama |
| Resistensi offline | Menangkap handshake saja tidak memberi verifikasi offline murah seperti PSK klasik |
| Forward-looking | Dipasangkan dengan kriptografi modern di RSN |

Masih butuh password yang tidak sepele (proteksi terhadap guessing **online** / rate). **Transition mode** (WPA2+WPA3) dapat melemahkan postur jika STA legacy dipaksa — pahami trade-off inventory perangkat.

### 🇬🇧 English
SAE changes the **threat model** for passphrase networks; it is not a license to use `password123`. Enterprise with EAP-TLS remains the gold standard for organizations.

### 日本語
SAEはオフライン推測を難しくしますが、弱いパスワードや移行モードの残存WPA2には注意が必要です。

---

## 5. 📵 Management Frames & Deauthentication (DoS Concept)

### 🇮🇩 Bahasa Indonesia
Banyak **management frame** klasik (deauth, disassoc) historis dikirim **tanpa proteksi** setara data frame. Akibatnya, pengirim di jangkauan radio dapat memaksa STA putus dari AP ⇒ **DoS / gangguan ketersediaan** (konsep).

$$
\mathsf{Deauth}:\ \mathsf{STA} \leftrightarrow \mathsf{AP}\ \text{session torn down (state cleared)}
$$

Dampak sekunder: pengguna mungkin tersambung ulang ke SSID jahat yang mirip (evil twin) jika kebijakan perangkat lemah — mitigasi lewat edukasi, WPA3, validasi sertifikat Enterprise, dan **PMF**.

**Protected Management Frames (PMF / 802.11w):** melindungi (sebagian) management frames penting; **wajib** pada WPA3. Aktifkan PMF capable/required sesuai inventori klien.

> Catatan: tidak ada daftar perintah injeksi frame, tool cracking, atau playbook DoS di dokumen ini.

### 🇬🇧 English
Treat unexplained mass disconnects as a **availability incident**: correlate AP logs, nearby RF changes, and whether PMF is enforced.

### 🇯🇵 日本語
大量切断は可用性インシデントとして扱い、PMFの有無とAPログを相関させます。

---

## 6. 🛡️ Defenses & Monitoring

| Kontrol | Tujuan |
|:---|:---|
| WPA3 / PMF required | Kurangi deauth klasik & perkuat Personal |
| 802.1X + EAP-TLS | Identitas perangkat/user, PMK per sesi |
| Disable WEP/TKIP | Hilangkan cipher lemah |
| Strong unique PSK per SSID (jika PSK) | Entropy tinggi; rotasi |
| Client isolation / AP isolation | Kurangi lateral Wi-Fi |
| Guest vs corp SSID | Segmentasi firewall |
| Rogue AP detection | Deteksi BSSID/SSID asing di kanal |
| Continuous RF survey | Baseline noise / channel util |
| Disable WPS PIN | Hilangkan vektor PSK recovery lemah |

**Deteksi (ide):** beacon SSID kembar dengan BSSID beda, lonjakan deauth di air capture lab Anda, klien yang sering ganti BSSID tanpa roaming policy, EAP failure spike.

---

## 7. 🔐 Security Notes — Defense Summary

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| Weak PSK | Compromise link privacy | Long random PSK or WPA3/Enterprise |
| Legacy WEP/TKIP | Trivial crypto breaks | Force CCMP/GCMP only |
| Open mgmt frames | Deauth DoS | PMF / WPA3 |
| Flat Wi-Fi + LAN | Lateral setelah associate | Isolation + NAC |
| Evil twin UX | Credential phishing | Educate; validate EAP server certs |
| IoT weak Wi-Fi | Soft underbelly | Separate SSID/VLAN |

**Lab hygiene:** audit hanya AP & spektrum yang Anda miliki izinnya. Capture untuk troubleshooting di jaringan sendiri, bukan untuk menyerang tetangga.

---

## 8. 🧠 Cheatsheet — Legitimate Admin / Lab

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
| `iw … link` | BSSID, freq, signal STA Anda |
| `iw … scan` | Survey lingkungan (patuh hukum lokal) |
| `nmcli device wifi` | Kelola profil Wi-Fi desktop |

---

> 📚 **References & Book Sources**
> - Matthew Gast — *802.11 Wireless Networks: The Definitive Guide* — `~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - William Stallings — *Network Security Essentials (4th Edition)* — `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach* — `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - IEEE 802.11i / WPA2 RSN, IEEE 802.11w (PMF), WPA3 (Wi-Fi Alliance) specifications overview
> - `man iw`, `man nmcli`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & administrasi WLAN milik sendiri — tanpa prosedur cracking atau injeksi serangan.
