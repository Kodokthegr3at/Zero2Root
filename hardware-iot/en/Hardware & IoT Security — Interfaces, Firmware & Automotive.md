# Hardware & IoT Security, Interfaces, Firmware & Automotive

> **LearnCybersecurity** | Embedded, IoT & Automotive Security Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: *Hardware Hacking Handbook*; *Practical IoT Hacking*; *The Car Hacker's Handbook*, `~/Documents/Books/CyberSec/Hardware/`
> Focus: interface concepts, architecture, and defense. Not vehicle attack recipes or exploit payloads.

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-070` | **Phase 7:** Specialized
> **Est. study:** 6-8h | **Level:** Advanced
> **Prerequisites:** LC-038
> **Book map:** van Woudenberg & O'Flynn, The Hardware Hacking Handbook; Chantzis et al., Practical IoT Hacking; Smith, The Car Hacker's Handbook; Gupta, The IoT Hacker's Handbook
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic |
|---|-------|
| 1 | IoT threat model |
| 2 | Debug interfaces (UART, JTAG, SWD) |
| 3 | Board buses: SPI / I2C / flash |
| 4 | Firmware concepts |
| 5 | Secure boot & signing |
| 6 | IoT network surface |
| 7 | Automotive CAN bus architecture |
| 8 | Automotive security defenses |
| 9 | Device-owner lab practice |
| 10 | Identify & defend cheatsheet |

---

## 1. Embedded / IoT Threat Model

An IoT device is silicon, firmware, radio/network, and cloud, all combined. Threats come from physical access (debug ports), local access (Wi-Fi/BLE), and remote access (cloud APIs).

Risk is highest when a valuable asset is easy to reach and poorly protected. Lower any one of those three and the risk drops.

Typical assets worth protecting: device keys, cloud credentials, sensor data, and safety functions (automotive, medical, or industrial).

For high-assurance designs (a set-top box, a vehicle ECU, an industrial controller), assume the attacker has physical possession of the device. Network controls alone fail if debug interfaces or unsigned firmware update paths still exist.

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  Sensors /  │──▶│  MCU / SoC  │──▶│  Radio/NIC  │──▶ Cloud / Mobile
│  Actuators  │◀──│  + firmware │◀──│  BLE/Wi-Fi  │◀──
└─────────────┘   └──────┬──────┘   └─────────────┘
                         │
                  Debug / flash pads
```

---

## 2. Debug Interfaces, Identification for Device Owners

Device owners and vendor security engineers often need to identify debug ports in order to secure them (disable, blow a fuse, or add authentication), not to attack someone else's device.

### 2.1 UART (Universal Asynchronous Receiver/Transmitter)
| Signal | Function |
|:---|:---|
| TX | Transmit data |
| RX | Receive data |
| GND | Common ground |
| Vcc | Don't wire it blind, check the voltage first |

Physical signs: 2 to 4 adjacent test pads, sometimes with a `TX/RX` silkscreen header. Common baud rates (as a concept): 115200, 57600, 9600.

Defense: disable the console in production, require authenticated login, or remove the shell entirely; limit what sensitive data ends up in logs.

### 2.2 JTAG / SWD

JTAG (IEEE 1149.1) is used for boundary scan and debug. Typical pins: `TCK`, `TMS`, `TDI`, `TDO`, `TRST` (optional).
SWD (ARM) uses two wires: `SWDIO`, `SWCLK`.

A debug port becomes a real danger when all three are true: the pads can be reached, no authentication is required, and the debug fuse is still open.

Defense (vendor side):
- Disable debug in production via a fuse or lifecycle state.
- Use a password or secure debug authentication if debug access must remain available for RMA.
- Epoxy or underfill is not a primary control, it only delays an attacker.

```
PCB edge                 SoC
  ○ TCK  ──────────────▶|
  ○ TMS  ──────────────▶|  Debug TAP
  ○ TDI  ──────────────▶|
  ○ TDO  ◀──────────────|
  ○ GND  ───────────────┘
```

Note: steps for exploiting debug access to bypass a third party's product protections are not included here. The focus is identifying and closing down this attack surface.

---

## 3. Board Buses, SPI, I2C & External Flash

| Bus | Typical wiring | Usage | Conceptual risk |
|:---|:---|:---|:---|
| SPI | SCLK, MOSI, MISO, CS | NOR flash firmware | Dumpable if CS/flash is exposed |
| I2C | SDA, SCL | EEPROM, sensors | Config data or weak keys |
| eMMC / SD | Parallel / SD | OS storage | Filesystem extraction |

### Firmware storage layout (conceptual)
```
┌──────────────┬──────────────┬──────────────┬────────────┐
│ Bootloader   │ Kernel / RTOS│ Rootfs / app │ Config/NV  │
│ (+sig?)      │              │              │            │
└──────────────┴──────────────┴──────────────┴────────────┘
```

Defense: encrypt sensitive non-volatile storage, bind secrets to a hardware root of trust, and avoid plaintext credentials in flash.

---

## 4. Firmware, Extraction & Analysis Concepts

*Practical IoT Hacking* and the *Hardware Hacking Handbook* cover how firmware gets obtained for security analysis. Here the focus stays on the concepts and the defensive goal.

### Legitimate firmware sources
| Source | When it's relevant |
|:---|:---|
| Vendor update package | Supply chain / update integrity analysis |
| Internal build artifact | Vendor SDL |
| A device you own + authorized lab | Research on a purchased unit |
| Open source release | Community audit |

### Analysis goals (defense)
1. Find hardcoded credentials or a backdoor service.
2. Verify whether updates are signed.
3. Map out which network services are listening.
4. Review TLS configuration and the certificate store.
5. Identify component versions to match against known CVEs.

A firmware update is only safe if it is signed, the signature chain is verified, and older vulnerable versions cannot be installed again (anti-rollback).

Static analysis concepts: unpack the image (binwalk-class tools in a lab setting), extract the filesystem, triage strings, review configuration.
Dynamic: run an emulator or test harness against an image you own, not against someone else's deployed fleet.

---

## 5. Secure Boot, Measured Boot & Firmware Signing

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
dm-verity / app containers (optional)
```

| Mechanism | Function |
|:---|:---|
| Secure boot | Rejects an image without a valid signature |
| Measured boot | Records a hash into a PCR/TPM for attestation |
| Anti-rollback | Rejects older versions with known vulnerabilities |
| Hardware root of trust | Keys stored in fuse, OTP, or an on-SoC HSM |

### Signing model
```text
σ = Sign(vendor private key, Hash(image))

accept the image only if:
  Verify(pk, image, σ) = OK   and   version ≥ minimum allowed version
```

Classic failure modes: debug boot left enabled, a leaked vendor private key, or verification implemented in software that can be patched without fuse protection.

---

## 6. IoT Network & Cloud Surface

| Layer | Examples | Hardening |
|:---|:---|:---|
| Local radio | BLE, Zigbee, Wi-Fi AP | Strong pairing PIN, disable WPS, rotate keys |
| LAN services | Legacy Telnet/HTTP | Remove them, use HTTPS/SSH only, patch regularly |
| Cloud API | Device to MQTT/HTTP broker | Mutual TLS, least-privilege scoped tokens |
| Mobile companion | Oversight app | Secure storage, mature certificate pinning |
| Update channel | OTA | Signed OTA + anti-rollback |

Least-privilege device identity: every device should have a unique identity, not one global key shared across the whole fleet.

That way, hacking one device does not hand the attacker every other device in the fleet, as long as keys are unique and rotated.

---

## 7. CAN Bus Architecture (Automotive)

*The Car Hacker's Handbook* points out that a modern vehicle is really a network of ECUs. CAN (Controller Area Network) is the differential serial bus used most widely.

### Architectural properties
| Property | Meaning |
|:---|:---|
| Multimaster | Many ECUs can transmit |
| Priority by ID | A lower ID means higher priority |
| Broadcast | A frame is visible to every node on the same bus |
| No built-in auth (classic) | A frame doesn't "log in", trust equals bus access |

```
ECU_A ----+------ ECU_B ------+------ ECU_C
          |                   |
         CAN_H / CAN_L differential pair
```

### Frame (concept)
```text
CAN frame = ID (what the message is about) | DLC (data length) | Data (0-8 bytes) | CRC (error check)
```

ISO-TP / UDS use CAN as a transport for diagnostics, a surface that needs tight control.

### Typical vehicle domains
| Domain | Example functions | Sensitivity |
|:---|:---|:---|
| Powertrain | Engine / transmission | Safety-critical |
| Chassis | ABS / steering assist | Safety-critical |
| Body | Windows / locks | Convenience + security |
| Infotainment | Media / apps | High attack entry point |
| OBD-II | Diagnostics port | Physical entry point |
| Telematics | Cellular modem | Remote entry point |

---

## 8. Automotive Security Defenses

The focus for a security engineer here is segmentation and control, not attack scripts.

| Defense | Description |
|:---|:---|
| Gateway ECU | Filters / policies traffic between CAN/Ethernet domains |
| Bus segmentation | Isolates infotainment from safety domains |
| Secure diagnostics | Authentication before sensitive UDS sessions |
| Signed firmware per ECU | Secure boot for each ECU |
| Vehicle IDS/IPS | Detects anomalies in frame ID/frequency (vendor-supplied) |
| OBD access policy | Restricts aftermarket dongles, user awareness |
| Telematics hardening | Patching the modem, mutual auth to the cloud |
| Supply chain | Code review for supplier ECUs |

```
Infotainment ──X──▶ Safety CAN
       │              ▲
       ▼              │ policy
   Gateway ECU ───────┘
       │
       ▼
   Telematics (auth'd)
```

The stronger the gateway's filtering rules and the better the domains are separated, the harder it is for an attacker to jump from one part of the car (for example infotainment) to another (for example braking).

Hard rule: this material does not provide CAN injection scripts, replay attack recipes, or immobilizer bypass steps. Understanding the architecture is useful for defensive design and authorized assessment.

---

## 9. Device-Owner / Vendor Lab Practice

Safe practice on devices you own, or in an authorized lab:

1. Photograph the board and document the silkscreen and test pads.
2. Measure voltage before connecting any adapter (3.3V vs 5V).
3. Inventory the debug ports, then plan how to close them before production.
4. Pull firmware through the official update channel and verify its signature.
5. Scan network services on an isolated lab Wi-Fi network.
6. Record findings as a SAST/hardening backlog item, not as a public exploit chain released without coordination.

| Don't | Do |
|:---|:---|
| Probe someone else's vehicle ECU | Practice on a training ECU or a legal lab |
| Publish a safety bypass | Coordinate disclosure with the vendor |
| Ignore pin voltage | Check with a multimeter first |
| Use a global shared cloud key | Use per-device credentials |

---

## 10. Identify & Defend Cheatsheet

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
| UART | 3-4 pads, TX/RX labels | Disable shell; no secrets in log |
| JTAG | 5+ pads or 10/20-pin footprint | Lifecycle disable / auth |
| SWD | 2-wire near MCU | Same as JTAG |
| SPI flash | 8-pin NOR near SoC | Secure boot + encrypt NV |
| OBD-II | Cabin connector | Policy + authenticated diag |
| CAN | Twisted pair to ECUs | Gateway & segmentation |

---

## Security Notes, Threats & Defenses

| Threat | Mechanism | Defense |
|:---|:---|:---|
| Debug abuse | Open UART/JTAG | Disable/fuse/auth debug |
| Firmware clone / implant | Unsigned update | Secure boot + anti-rollback |
| Fleet key leak | Shared symmetric key | Per-device keys + rotation |
| Cloud account takeover | Weak pairing | Strong provisioning; MFA on owner account |
| IVI to safety crossover | Flat network | Gateway filtering / domain isolation |
| Malicious OBD dongle | Bus access | User education; restricted diag |
| Supply-chain backdoor | Third-party ECU code | Audit, SBOM, signing |

Not covered here: CAN attack scripts, immobilizer defeat, airbag/safety misuse, or an RCE playbook for an ECU.

---

> **References & Book Sources**
> - *The Hardware Hacking Handbook*, `~/Documents/Books/CyberSec/Hardware/`
> - *Practical IoT Hacking: The Definitive Guide to Attacking the Internet of Things*, `~/Documents/Books/CyberSec/Hardware/` (adapted here for defense & owner assessment)
> - *The Car Hacker's Handbook*, `~/Documents/Books/CyberSec/Hardware/` (adapted here for CAN architecture + defenses)
> - Industry: UNECE WP.29 / ISO/SAE 21434 (automotive cybersecurity process, overview)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> For education and securing devices you own or work with in an authorized lab. Not for interfering with someone else's vehicle or device.
