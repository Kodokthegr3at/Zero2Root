# Wireless 802.11 Security & Attacks

> **LearnCybersecurity** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: *802.11 Wireless Networks: The Definitive Guide*; Stallings, *Network Security Essentials*; Kurose & Ross, *Computer Networking*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-043` | **Phase 2:** Networking
> **Est. study:** 5h | **Level:** Advanced
> **Prerequisites:** LC-038
> **Book map:** Gast, 802.11 Wireless Networks (full); Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Table of contents

1. How Wi-Fi is organized
2. How Wi-Fi security grew up
3. WPA2: keys and the 4-way handshake
4. WPA3: a better password exchange
5. Deauthentication and its risk
6. Defenses and monitoring
7. Security notes
8. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| STA (station) | Any Wi-Fi client: a laptop, phone, and so on |
| AP (access point) | The device clients connect to (the Wi-Fi "base") |
| SSID | The network's name, the thing you pick from the Wi-Fi list |
| BSSID | The AP's MAC address, which uniquely identifies it |
| PSK | Pre-shared key: the Wi-Fi password everyone on a home network shares |
| Handshake | The exchange where client and AP prove they know the key and set up encryption |
| CCMP / AES | The encryption used for Wi-Fi data on WPA2/WPA3 |
| Management frame | Control messages (connect, disconnect, beacon) separate from your actual data |
| PMF | Protected Management Frames: protection for those control messages |
| Evil twin | A fake AP that copies a real network's name to lure clients |

---

## 1. How Wi-Fi Is Organized

IEEE 802.11 ("Wi-Fi") connects **stations** (STA, your devices) to **access points** (AP). The network's name is its **SSID**; each AP is uniquely identified by its MAC address, the **BSSID**. Several APs can share one SSID so you roam between them seamlessly.

```
  ┌────────────── Wi-Fi network: SSID "CORP" ──────────────┐
  │   AP1                        AP2                        │
  │    ↑↑↑                        ↑↑↑                       │
  │  phone, laptop              laptop                      │
  └─────────────────────────────────────────────────────────┘
          │
          └── wired connection ──► LAN / Internet
```

Wi-Fi traffic falls into three kinds of frames:

| Frame type | Job | Examples |
|:---|:---|:---|
| Data | Carries your actual traffic | web pages, video |
| Control | Helps share the airwaves | acknowledgements |
| Management | Joining and discovery | beacon, connect, disconnect |

The one thing to internalize: **Wi-Fi is radio, so anyone nearby can hear it.** You can't rely on walls. Confidentiality and integrity come only from the link-layer security the network uses, which is the subject of the rest of this lesson.

---

## 2. How Wi-Fi Security Grew Up

Wi-Fi security improved in clear generations. Where you have a choice, pick the newest your devices support.

| Era | What it uses | Should you use it? |
|:---|:---|:---|
| Open | No encryption | Only with a captive portal + app-level HTTPS |
| WEP | Old, broken cipher | Never; broken decades ago |
| WPA (TKIP) | Transitional | Avoid; legacy |
| WPA2-Personal | A shared password + AES | Still common; only as strong as the password |
| WPA2-Enterprise | Per-user login via 802.1X | The office standard |
| WPA3-Personal | A modern password exchange (SAE) | Preferred; resists offline guessing |
| WPA3-Enterprise | Per-user login, stronger crypto | High assurance |

The practical rule: use WPA3 where you can, WPA2 with a strong password at minimum, and never WEP or TKIP.

---

## 3. WPA2: Keys and the 4-Way Handshake

The goal of the WPA2 handshake is to turn the shared password into a **fresh, unique session key** for each connection, and to confirm both sides know the password, all **without ever sending the password over the air**.

The keys build up in layers:

- **PMK** (the master key): on a home network it comes from the Wi-Fi password mixed with the network name. On enterprise Wi-Fi it comes from the per-user login instead.
- **PTK** (the session key): derived from the PMK plus some fresh random numbers (**nonces**) from both sides and their MAC addresses. Because the nonces are new every time, the session key is different for every connection.
- **GTK** (the group key): shared by the AP with all clients, for broadcast traffic.

### The 4-way handshake

```
  AP                                         STA (client)
   │  1. here's my random number (ANonce)     │
   │─────────────────────────────────────────►│  (client can now compute the PTK)
   │  2. here's mine (SNonce) + proof          │
   │◄─────────────────────────────────────────│  (AP computes the PTK, checks the proof)
   │  3. group key + proof + "install it"      │
   │─────────────────────────────────────────►│
   │  4. acknowledged                          │
   │◄─────────────────────────────────────────│
   │     data now encrypted with the keys      │
```

Each side proves it derived the **same** session key, which is only possible if both really know the password. Nobody ever transmits the password.

The catch for home Wi-Fi: all of this security rests on the **password's strength**. A short or common password can be guessed offline by someone who captured the handshake. (This lesson does not cover how that cracking is done.) The fix is a long random password, or better, WPA3 or Enterprise.

---

## 4. WPA3: A Better Password Exchange

WPA3-Personal replaces the handshake with **SAE** (Simultaneous Authentication of Equals, built on a method called Dragonfly). The important difference: both sides prove they know the password through a live back-and-forth, in a way that **doesn't hand an eavesdropper anything they can test offline**.

| Property | What it means for you |
|:---|:---|
| No cheap offline guessing | Capturing the exchange no longer lets an attacker grind through password guesses on their own machine |
| Online guessing only | An attacker must guess against the live AP, which can rate-limit them |

SAE still needs a non-trivial password (so online guessing stays hopeless), and running a mixed WPA2+WPA3 "transition mode" can weaken things if old devices force the network down to WPA2. For organizations, Enterprise with EAP-TLS (per-user certificates) remains the gold standard. SAE is a real improvement, not an excuse to use `password123`.

---

## 5. Deauthentication and Its Risk

Historically, the management frames that tell a device to disconnect ("deauth") were sent **without any protection**. That means someone within radio range could forge a disconnect and knock a device off its network. By itself that's a denial of service: the device drops and has to reconnect.

The bigger danger is what can come next. A disconnected device may automatically reconnect to a lookalike network, an **evil twin**: a fake AP broadcasting the same SSID to lure clients and harvest credentials.

The defense is **Protected Management Frames (PMF / 802.11w)**, which authenticates those control messages so forged disconnects are rejected. PMF is **mandatory in WPA3**. Also helpful: user awareness, and validating the server certificate on Enterprise Wi-Fi.

> This lesson explains the concept and defenses, not how to inject frames or run a jamming attack.

Treat a sudden wave of mass disconnects as an availability incident: check the AP logs, look for nearby RF changes, and confirm PMF is being enforced.

---

## 6. Defenses and Monitoring

| Control | Purpose |
|:---|:---|
| WPA3 / PMF required | Blocks classic deauth attacks and strengthens password-based Wi-Fi |
| 802.1X + EAP-TLS | Per-device/user identity, a fresh key per session |
| Disable WEP / TKIP | Removes the broken ciphers |
| Strong, unique password (if using PSK) | High entropy; rotate it periodically |
| Client isolation | Stops Wi-Fi clients from reaching each other |
| Separate guest and staff SSIDs | Firewall the guest network off from the internal one |
| Rogue AP detection | Spots foreign or lookalike networks on your channels |
| Disable WPS PIN | Removes a weak way to recover the password |

Detection ideas: a second beacon advertising your SSID from an unexpected BSSID (a possible evil twin), a sudden spike of disconnects in a capture on your own network, or a jump in authentication failures.

---

## 7. Security Notes

| Issue | Risk | Defense |
|:---|:---|:---|
| Weak password | The whole link's confidentiality falls | Long random password, or WPA3 / Enterprise |
| Legacy WEP / TKIP | Trivially broken | Force AES (CCMP/GCMP) only |
| Unprotected management frames | Deauth denial of service | PMF / WPA3 |
| Flat Wi-Fi + LAN | Lateral movement after joining | Client isolation + network access control |
| Evil twin | Credential phishing | User awareness; validate EAP server certificates |
| Weak IoT Wi-Fi | A soft entry point into the network | A separate SSID / VLAN for IoT |

Lab hygiene: only audit the AP and the airspace you have permission for. Capture for troubleshooting on your own network, never a neighbor's.

---

## 8. Cheatsheet

```bash
# ── Your own link state (Linux) ──────────────────────────────
iw dev                         # your wireless interfaces
iw dev wlan0 link              # current BSSID, frequency, signal
iw dev wlan0 info

# ── Survey nearby networks (observability on your radio) ─────
sudo iw dev wlan0 scan | egrep 'BSS|SSID|RSN|signal'

# ── NetworkManager ───────────────────────────────────────────
nmcli device wifi list
nmcli connection show

# ── Regulatory / channel info ────────────────────────────────
iw reg get

# ── On an AP you operate, prefer these settings ──────────────
# WPA3 (SAE) where clients allow it, otherwise WPA2 + a strong password
# PMF required (ieee80211w=2), AES/CCMP only, WPS PIN disabled
```

| Command | Use |
|:---|:---|
| `iw … link` | Shows your BSSID, frequency, and signal |
| `iw … scan` | Surveys nearby networks (follow local law) |
| `nmcli device wifi` | Manages Wi-Fi profiles on the desktop |

---

> **References & book sources**
> - Matthew Gast, *802.11 Wireless Networks: The Definitive Guide*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - IEEE 802.11i / WPA2 RSN, IEEE 802.11w (PMF), the WPA3 (Wi-Fi Alliance) specification
> - `man iw`, `man nmcli`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and administration for WLANs you own, no cracking procedures or attack injection.
