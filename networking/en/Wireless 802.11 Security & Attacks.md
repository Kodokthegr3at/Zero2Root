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

1. 802.11 architecture & framing overview
2. Security evolution (brief)
3. WPA2: PMK, PTK, GTK & 4-way handshake
4. WPA3-Personal: SAE (high level)
5. Management frames & deauthentication (DoS concept)
6. Defenses & monitoring
7. Security notes: defense summary
8. Cheatsheet

---

## 1. 802.11 architecture & framing overview

IEEE 802.11 defines the WLAN: stations (STA), access points (AP), and the BSS (Basic Service Set). Several BSSs sharing the same SSID can form an ESS. The medium is half-duplex; channel access uses CSMA/CA (not the classic Ethernet CSMA/CD).

Three frame classes:

| Class | Role | Examples |
|:---|:---|:---|
| Data | Carries the LLC/IP payload | QoS data |
| Control | Assists medium access | RTS/CTS, ACK |
| Management | Membership & discovery | Beacon, Probe, Auth, Assoc, Deauth, Disassoc |

```
  ┌────────────── ESS / SSID "CORP" ──────────────┐
  │   AP1 (BSS1)              AP2 (BSS2)          │
  │    ↑↑↑                     ↑↑↑                │
  │   STA                      STA                │
  └───────────────────────────────────────────────┘
         │
         └── wired DS (Distribution System) ──► LAN/Internet
```

The Beacon announces the SSID (or a hidden one), capabilities, and the security IE (RSN). Association binds a STA to an AP before unicast data is encrypted (on modern networks).

The 802.11 header uses several address fields (ToDS/FromDS) to distinguish SA/DA/BSSID; the full detail is in the O'Reilly book *802.11 Wireless Networks*.

Wireless is a shared broadcast medium within radio range. Confidentiality and integrity depend on link-layer security (RSN), not on "being indoors." Always assume nearby receivers can hear unprotected management traffic and poorly configured networks.

---

## 2. Security evolution (brief)

| Era | Mechanism | Practical status |
|:---|:---|:---|
| Open | No link encryption | Only suited to a captive portal plus application-level TLS |
| WEP | RC4 + weak IV | Deprecated / broken, do not use |
| WPA-PSK (TKIP) | Transitional | Legacy; avoid where possible |
| WPA2-Personal | PSK + CCMP (AES) | Still common; a weak PSK is a real risk |
| WPA2-Enterprise | 802.1X / EAP + RADIUS | The office standard |
| WPA3-Personal | SAE | Better resistance to offline PSK guessing |
| WPA3-Enterprise | EAP + an optional 192-bit suite | High assurance |

The RSN (Robust Security Network) IE in the Beacon states the ciphers and AKMs on offer. CCMP (AES-CCM) is the expected data cipher on WPA2; GCMP shows up on newer PHYs / WPA3 contexts.

---

## 3. WPA2: PMK, PTK, GTK & 4-way handshake

The handshake's goal: derive a fresh session key from a long-term secret, and confirm mutual possession without ever sending the PSK in cleartext over the air.

PMK (Pairwise Master Key):

- Personal (PSK): the PMK is derived from the passphrase plus the SSID (PBKDF2-HMAC-SHA1, 4096 iterations on classic WPA2-PSK):

$$
\mathsf{PMK} = \mathsf{PBKDF2}(\mathsf{passphrase},\; \mathsf{SSID},\; 4096,\; 256\text{ bits})
$$

- Enterprise: the PMK comes from EAP / the MSK after a successful 802.1X exchange (per session/user, an improvement over a shared PSK).

PTK (Pairwise Transient Key) is derived from the PMK plus nonces and MAC addresses:

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

where $AA$ = the AP's MAC (BSSID), $SPA$ = the STA's MAC. The PTK splits into:

| Part | Function |
|:---|:---|
| KCK | Key Confirmation Key (MIC on EAPOL-Key) |
| KEK | Key Encryption Key (wraps key material) |
| TK | Temporal Key for CCMP on unicast data |

GTK (Group Temporal Key): the multicast/broadcast key from the AP to all associated STAs, distributed wrapped during the handshake / a group key handshake.

### 4-way handshake (EAPOL-Key): conceptual flow

```
  AP                                         STA
   │  Msg1: ANonce                            │
   │─────────────────────────────────────────►│
   │          (STA computes PTK; has SNonce)  │
   │  Msg2: SNonce + MIC                      │
   │◄─────────────────────────────────────────│
   │  (AP computes PTK; verifies MIC)         │
   │  Msg3: GTK + MIC + install               │
   │─────────────────────────────────────────►│
   │  Msg4: MIC / Ack                         │
   │◄─────────────────────────────────────────│
   │         Data encrypted with CCMP (TK/GTK) │
```

MIC verification with the KCK proves both sides derived the same PTK, which means they hold the same PMK.

WPA2-Personal's security ultimately comes down to PSK entropy. A low-entropy passphrase opens the door to offline guessing against captured handshake material; this note deliberately does not document cracking procedures. Mitigation: a long random PSK, or preferably WPA3-SAE or Enterprise (802.1X).

---

## 4. WPA3-Personal: SAE (high level)

SAE (Simultaneous Authentication of Equals) is built on the Dragonfly protocol (a password-authenticated key exchange). Both sides prove knowledge of the password through an online interaction over an elliptic curve / finite field group, then derive a PMK.

Desired properties (intuition):

| Property | Operational meaning |
|:---|:---|
| PAKE | The password is not used as a "hashable" PSK the same way WPA2 uses it |
| Offline resistance | Capturing the handshake alone does not give a cheap offline verification path like classic PSK does |
| Forward-looking | Paired with more modern cryptography in the RSN |

SAE still requires a non-trivial password (as protection against online, rate-limited guessing). Transition mode (WPA2+WPA3) can weaken the security posture if legacy STAs are still forced onto it; understand that trade-off against your device inventory.

SAE changes the threat model for passphrase-based networks; it is not a license to use `password123`. Enterprise with EAP-TLS remains the gold standard for organizations.

---

## 5. Management frames & deauthentication (DoS concept)

Many classic management frames (deauth, disassoc) were historically sent without the same protection as data frames. As a result, a sender within radio range could force a STA to disconnect from its AP, which conceptually is a DoS or availability disruption.

$$
\mathsf{Deauth}:\ \mathsf{STA} \leftrightarrow \mathsf{AP}\ \text{session torn down (state cleared)}
$$

A secondary effect: users may reconnect to a similar-looking rogue SSID (an evil twin) if device policy is weak. Mitigation comes through user education, WPA3, Enterprise certificate validation, and PMF.

Protected Management Frames (PMF / 802.11w): protects some important management frames, and is mandatory under WPA3. Enable PMF capable/required mode according to your client inventory.

Note: no frame injection command list, cracking tool, or DoS playbook is included in this document.

Treat an unexplained wave of mass disconnects as an availability incident: correlate AP logs, nearby RF changes, and whether PMF is being enforced.

---

## 6. Defenses & monitoring

| Control | Purpose |
|:---|:---|
| WPA3 / PMF required | Reduces classic deauth attacks and strengthens WPA2-Personal |
| 802.1X + EAP-TLS | Per-device/user identity, PMK per session |
| Disable WEP/TKIP | Removes weak ciphers |
| Strong, unique PSK per SSID (if using PSK) | High entropy; periodic rotation |
| Client isolation / AP isolation | Reduces lateral movement between Wi-Fi clients |
| Separate guest and corp SSID | Firewall segmentation |
| Rogue AP detection | Detects foreign BSSIDs/SSIDs on the same channel |
| Continuous RF survey | Baselines noise / channel utilization |
| Disable WPS PIN | Removes a weak PSK recovery vector |

Detection ideas: a twin SSID beacon with a different BSSID, a spike in deauths on an air capture in your own lab, clients that roam between BSSIDs frequently without a roaming policy, and a spike in EAP failures.

---

## 7. Security notes: defense summary

| Issue | Risk | Defense |
|:---|:---|:---|
| Weak PSK | Compromises link confidentiality | Long random PSK, or WPA3/Enterprise |
| Legacy WEP/TKIP | Trivially broken cryptography | Force CCMP/GCMP only |
| Open management frames | Deauth DoS | PMF / WPA3 |
| Flat Wi-Fi and LAN | Lateral movement after association | Isolation + NAC |
| Evil twin | Credential phishing | User education; validate EAP server certs |
| Weak IoT Wi-Fi | A soft spot in the network | Separate SSID/VLAN |

Lab hygiene: audit only the AP and spectrum you have permission for. Capture for troubleshooting on your own network, not to attack a neighbor's.

---

## 8. Cheatsheet: legitimate admin / lab

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

| Command | Use |
|:---|:---|
| `iw … link` | Shows BSSID, frequency, and signal for your STA |
| `iw … scan` | Surveys the surrounding environment (follow local law) |
| `nmcli device wifi` | Manages Wi-Fi profiles on the desktop |

---

> **References & book sources**
> - Matthew Gast, *802.11 Wireless Networks: The Definitive Guide*, `~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - IEEE 802.11i / WPA2 RSN, IEEE 802.11w (PMF), a WPA3 (Wi-Fi Alliance) specification overview
> - `man iw`, `man nmcli`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and administration for WLANs you own, no cracking procedures or attack injection.
