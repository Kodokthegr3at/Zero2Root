# ARP & Local Network Attacks

> **LearnCybersecurity** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Kurose & Ross, *Computer Networking*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-042` | **Phase 2:** Networking
> **Est. study:** 4h | **Level:** Advanced
> **Prerequisites:** LC-039, LC-040
> **Book map:** Kurose & Ross, Computer Networking Ch.4-5; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Table of contents

1. Why ARP exists
2. How request and reply work
3. The ARP cache
4. Related mechanisms
5. The on-link MITM problem
6. Defenses
7. Detection and monitoring
8. Security notes
9. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| ARP | The protocol that finds the MAC address for a given IP, inside one local network |
| MAC address | A network card's hardware ID, used for delivery within a local network |
| ARP cache | The short-term table a device keeps of "this IP = this MAC" |
| Broadcast | A message sent to everyone on the local segment |
| Gateway | The router a device uses to reach other networks |
| Spoofing / poisoning | Feeding a device a false IP-to-MAC mapping |
| MITM | Man-in-the-middle: quietly sitting between two parties and relaying their traffic |
| DAI | Dynamic ARP Inspection: a switch feature that drops lying ARP messages |
| Segmentation | Splitting the network into smaller zones to limit how far an attacker can reach |

---

## 1. Why ARP Exists

Inside one local network, a device delivers data using **MAC addresses** (the hardware ID of each network card), not IP addresses. But your programs and routing work in **IP addresses**. Something has to connect the two. That something is **ARP** (Address Resolution Protocol):

```text
ARP answers one question:  "What MAC address has IP 10.0.0.9?"
```

It only works within the **local segment** (the same broadcast domain). You never ARP for a far-away server; instead your machine ARPs for its **gateway** and hands the frame to the gateway's MAC, letting the router take it from there.

```
  Host A                    switch                      Host B
  10.0.0.5                                              10.0.0.9
         ──── "Who has 10.0.0.9? Tell 10.0.0.5" (broadcast) ────►
         ◄─── "10.0.0.9 is at bb:bb:bb:bb:bb:bb" (reply) ────────
  now sends frames to bb:bb:… ──────────────────────────────────►
```

The key weakness is built into ARP's design: **it has no way to check whether a reply is telling the truth.** Whoever answers first, and most convincingly, wins. That single fact is the root of every attack in this lesson, and the reason the defenses in Section 6 exist. (IPv6 uses a similar protocol called NDP instead of ARP.)

---

## 2. How Request and Reply Work

ARP has just two main messages:

| Operation | Meaning |
|:---|:---|
| Request | "Who has this IP? Tell me." (sent as a broadcast to everyone) |
| Reply | "That IP is at this MAC." (sent back to the asker) |

```text
A → everyone:  "Who has IP_B? Tell A"
B → A:         "IP_B is at MAC_B"
```

After this exchange, A can send frames straight to B. Many systems also quietly learn mappings just from ARP traffic they overhear, which is convenient but is exactly why an **unsolicited** or unexpected reply is a red flag.

---

## 3. The ARP Cache

To avoid asking every time, each device keeps a short-term table:

```text
IP address  →  (MAC address, state, interface, expiry time)
```

```bash
ip neigh show      # view the ARP/NDP cache on Linux
```

Entries time out and get refreshed. The important thing to understand is this: **the cache is only as trustworthy as whoever is allowed to speak on the segment.** If a device accepts a reply without any extra checking, a false reply can quietly overwrite a correct entry.

Practical tip: after swapping a network card or renumbering, stale cache entries can cause "ghost" connectivity problems until they expire. Flush entries only on machines you administer.

---

## 4. Related Mechanisms

| Mechanism | What it is | Security note |
|:---|:---|:---|
| Proxy ARP | A router answers ARP on behalf of a device that isn't local | Extends local trust; audit it if it's unintentional |
| Gratuitous ARP | An unsolicited "here I am" announcement | Legitimate for failover, but also a spoofing vector if unfiltered |
| ARP probe (RFC 5227) | A check for address conflicts before using an IP | Useful for duplicate-address detection |

```
  Normal:      "Who has B?"        →  "B is at MAC_B"
  Gratuitous:  "A is at MAC_A"     →  (announcement, updates everyone's cache)
```

---

## 5. The On-Link MITM Problem

Because ARP replies aren't verified, a malicious device on the same segment can convince a victim that **the gateway's IP is at the attacker's MAC**. The victim then sends its "to the Internet" traffic to the attacker instead of the real router.

If the attacker quietly forwards that traffic onward, the victim notices nothing, while the attacker sits in the middle and can read or alter anything that isn't encrypted. That's a **man-in-the-middle at the local-network layer**.

```
  Before:  Victim ───────────────► Gateway ──► Internet

  After:   Victim ──► Attacker ──► Gateway ──► Internet
                    (reads/alters traffic in passing)
```

> This lesson explains **why** the attack is possible and how to stop it. Step-by-step poisoning instructions and spoofing tools are deliberately left out.

What this means defensively: don't assume "a frame addressed to the gateway's MAC actually reaches the gateway." Encrypting higher layers (TLS everywhere) limits what an attacker can read, but it doesn't restore trust at the local layer, especially for availability and for anything not end-to-end encrypted. You still need the controls below.

---

## 6. Defenses

| Control | How it works | Where it fits |
|:---|:---|:---|
| DHCP Snooping | The switch records the legitimate (MAC, IP, port) from real DHCP leases | The foundation for DAI |
| Dynamic ARP Inspection (DAI) | The switch checks each ARP message against those records and drops the liars | Enterprise access networks |
| Static ARP entries | A fixed, manually set mapping on a critical host or router | Gateways, small servers |
| Port security | Limits how many MAC addresses a switch port will accept | The access edge |
| Segmentation / private VLANs | Keeps devices from freely reaching each other at the local layer | Everywhere; the strongest architectural control |

The most powerful idea here is **segmentation**: the smaller the local segment, the fewer devices an attacker can even reach with ARP tricks in the first place. Static entries don't scale to a big network, so the practical combination is DHCP Snooping plus DAI at the access switches, with monitoring on top.

```
  [ User VLAN ] ──DAI + DHCP Snooping──► [ gateway ] ──filtering──► [ Server VLAN ]
```

---

## 7. Detection and Monitoring

Signals worth investigating on a network you run:

| Signal | Possible meaning |
|:---|:---|
| The gateway's MAC suddenly changes on many hosts at once | A spoofing attempt or an unstable binding |
| Two different MACs both claim the same IP | An address conflict or spoofing |
| A storm of ARP requests | A loop, a misconfiguration, or aggressive scanning |
| Rising DAI "drop" counters on a switch | ARP messages that violate the recorded bindings |

```bash
# Legitimate observation on a host you own
ip neigh show
sudo tcpdump -ni eth0 arp     # watch ARP traffic on your own NIC
```

Correlate what you see with the switch's own DAI logs and the DHCP lease list.

---

## 8. Security Notes

| Issue | Risk | Defense |
|:---|:---|:---|
| ARP can't be authenticated | A forged IP-to-MAC binding | DHCP Snooping + DAI |
| One big flat segment | Easy local MITM and recon | VLANs / segmentation |
| Unfiltered gratuitous ARP | Mass cache overwrite | Rate limiting / inspection |
| Stale static entries | An outage after a NIC swap | A runbook for updating them |
| IPv6 ignored | A gap if you only think about ARP | RA Guard, ND inspection |
| Cleartext protocols | Readable if a MITM succeeds | TLS everywhere, plus HSTS |

The principle: trust the local network only as far as the switch policy actually enforces. End-to-end encryption complements link-layer controls, it doesn't replace them.

---

## 9. Cheatsheet

```bash
# ── Inspect the neighbor table (your own host) ───────────────
ip neigh show
ip -4 neigh show dev eth0
ip -6 neigh show               # the IPv6 (NDP) equivalent

# ── Manage entries on YOUR host (be careful in production) ───
sudo ip neigh add 10.0.0.1 lladdr aa:bb:cc:dd:ee:ff dev eth0 nud permanent
sudo ip neigh del 10.0.0.1 dev eth0
sudo ip neigh flush dev eth0

# ── Trigger a normal lookup ──────────────────────────────────
ping -c 1 10.0.0.9
ip neigh get 10.0.0.9 dev eth0

# ── Observe ARP passively on your own NIC ────────────────────
sudo tcpdump -ni eth0 arp -vv

# ── MAC learning on a Linux bridge ───────────────────────────
bridge fdb show
```

| Command | Use |
|:---|:---|
| `ip neigh` | View or edit the ARP/NDP cache |
| `tcpdump arp` | Audit ARP traffic on your own NIC |
| `bridge fdb` | See MAC learning on a Linux bridge |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - W. Richard Stevens, *UNIX Network Programming, Vol. 1*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 826 (ARP), RFC 5227 (IPv4 Address Conflict Detection), RFC 4861 (NDP)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on. No poisoning playbook included.
