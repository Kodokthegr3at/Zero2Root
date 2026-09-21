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
2. ARP request & reply
3. ARP cache (neighbor table)
4. Related mechanisms (Proxy ARP, GARP)
5. On-link MITM concept
6. Defenses (DAI, static ARP, segmentation)
7. Detection & monitoring
8. Security notes (defense summary)
9. Admin cheatsheet

---

## 1. Why ARP exists

On Ethernet/IPv4, delivering a frame requires the destination MAC address at L2, while applications and routing work with the IP address at L3. ARP (Address Resolution Protocol) bridges the two:

$$
\mathsf{ARP}:\ \mathsf{IPv4} \;\longrightarrow\; \mathsf{MAC}
$$

This resolution only works on the local link, meaning the same broadcast domain. A router is never ARP'd across subnets for a remote host. Instead, the host ARPs its gateway and sends the frame to the gateway's MAC.

```
  Host A                    L2 switch                   Host B
  IP 10.0.0.5               (broadcast domain)          IP 10.0.0.9
  MAC aa:aa:…  ──────── ARP who-has 10.0.0.9 ────────►
               ◄─────── ARP is-at bb:bb:… ────────────
  Frame dst=bb:bb ───────────────────────────────────►
```

IPv6 uses NDP (Neighbor Discovery) instead of ARP, a similar concept (L3 to L2 resolution) carried over ICMPv6 messages.

ARP is a trust-on-first-use, soft-state mapping protocol with no built-in cryptographic authenticity. That design choice is exactly why local-link integrity controls matter.

---

## 2. ARP request & reply

ARP is wrapped in an Ethernet frame with EtherType `0x0806`. There are two main operations:

| `op` | Name | Meaning |
|:---:|:---|:---|
| 1 | Request | "Who has $IP_t$? Tell $IP_s$" |
| 2 | Reply | "$IP_t$ is at $MAC_t$" |

Key fields (IPv4 over Ethernet):

| Field | Typical content |
|:---|:---|
| HTYPE / PTYPE | Ethernet / IPv4 |
| HLEN / PLEN | 6 / 4 |
| SHA / SPA | Sender MAC / Sender IP |
| THA / TPA | Target MAC / Target IP |

A request is usually sent as an Ethernet broadcast (`ff:ff:ff:ff:ff:ff`), with THA often zeroed. A reply is usually unicast back to the requester's SHA, except in special cases.

Canonical flow:

$$
\begin{aligned}
A &\xrightarrow{\mathsf{ARP\,Req}(TPA=B)} \mathsf{Broadcast} \\
B &\xrightarrow{\mathsf{ARP\,Rep}(SPA=B,\,SHA=MAC_B)} A
\end{aligned}
$$

After this exchange, $A$ can send IP frames with `dst MAC = MAC_B`.

Hosts also learn mappings from packets they observe passively, depending on the kernel or stack implementation. Unsolicited or unexpected replies are a classic integrity concern, which is why some switch features validate ARP against DHCP bindings.

---

## 3. ARP cache (neighbor table)

The kernel keeps a temporary mapping:

$$
\mathsf{Cache}:\ (IP) \mapsto (MAC,\; \mathsf{state},\; \mathsf{iface},\; \mathsf{expiry})
$$

| Aspect | Typical behavior |
|:---|:---|
| Incomplete | Request sent, no reply yet |
| Reachable / stale | Mapping exists, may be re-probed |
| TTL / gc | Stale entries get dropped or refreshed |
| Failures | Limited retries, then a neighbor error |

On modern Linux, `ip neigh` shows neighbor state (ARP for IPv4, NDISC for IPv6). Understanding these states helps when troubleshooting a "host unreachable on-link" case.

Update rules, intuitively: a reply that looks valid can create or overwrite an entry. Without extra L2 validation, the correctness of the cache is really just the correctness of whoever is allowed to speak on that segment.

Operational tip: after renumbering or a NIC swap, stale ARP/ND entries cause "ghost" connectivity until they time out or get flushed. Flush entries only on systems you actually administer.

---

## 4. Related mechanisms

| Mechanism | Summary | Security note |
|:---|:---|:---|
| Proxy ARP | A router answers ARP for a non-local IP as if it were on-link | Extends L2 trust, audit it if unintentional |
| Gratuitous ARP (GARP) | An announcement where SPA=TPA | Legitimate for failover/HA, also a spoofing vector if unfiltered |
| Inverse ARP | MAC to IP (rare on modern Ethernet) | Special context (Frame Relay era and similar) |
| ARP probe / announce (RFC 5227) | Checks for address conflicts before an IP is used | Useful for duplicate address detection |

```
  Normal ARP:     "Who has B? Tell A"     →  "B is at MAC_B"
  Gratuitous:     "A is at MAC_A"         →  (announce / update caches)
  Proxy:          "Who has X (remote)?"   →  Router replies with own MAC
```

---

## 5. On-link MITM, concept only

This is a concept, not a procedure. If a malicious host on the same segment manages to get a victim to store

$$
IP_{\mathsf{gateway}} \mapsto MAC_{\mathsf{attacker}}
$$

(optionally the reverse too), frames meant for the gateway can be redirected to the attacker. An attacker who also forwards the traffic can observe or modify cleartext sessions. That is a MITM at layer 2.

This exploits ARP's basic property: there is no cryptographic authentication of the IP to MAC binding.

> Educational note: step by step poisoning instructions, tool commands for spoofing, or attack playbooks are deliberately left out. The goal of this section is understanding why switch controls and segmentation are needed, not performing the attack.

Any successful on-link redirection breaks the assumption that "frames to the gateway MAC reach the gateway." Encrypting higher layers (TLS) limits the confidentiality impact, but it does not remove the value of L2 integrity, especially for availability and for protocols that are not end-to-end encrypted.

---

## 6. Defenses: DAI, static ARP, segmentation

| Control | How it works (intuition) | Fits |
|:---|:---|:---|
| Dynamic ARP Inspection (DAI) | Switch validates ARP against trusted bindings (usually from DHCP Snooping) | Enterprise access VLANs |
| DHCP Snooping | Records (MAC, IP, port, VLAN) from legitimate DHCP | Foundation for DAI |
| Static ARP / static neigh | Fixed binding on a critical host/router | Gateways, small servers, OT |
| Port security | Limits the number of MACs per port | Access edge |
| Private VLAN / microsegmentation | Limits host-to-host lateral movement | Cloud / DC / campus |
| Separate management plane | Out-of-band or a dedicated VRF for management | Infrastructure |
| RA Guard / ND controls | The IPv6 analog | Dual-stack |

Segmentation is still the strongest control architecturally: the smaller the broadcast domain, the smaller the blast radius of L2 snooping or spoofing.

Trust model:

```
  [User VLAN] --DAI+DHCP Snoop--> [L3 gateway] --ACL--> [Server VLAN]
        │                              │
        └──── no hairpin L2 freely ────┘
```

Static ARP alone does not scale to a DHCP fleet. Combine DAI at the access layer with monitoring. For very small, genuinely trusted enclaves, static mappings on routers remain practical.

---

## 7. Detection & monitoring

Signals worth investigating in a lab or production environment you own:

| Signal | Possible meaning |
|:---|:---|
| Gateway MAC changes on many hosts at once | Unstable binding / L2 anomaly |
| Duplicate IP (two MACs claim one IP) | Conflict or spoofing |
| ARP request storm | Loop, misconfiguration, or aggressive scanning |
| DAI drop counters rising | ARP violating recorded bindings |
| TLS/VPN still fine but a weird captive portal | Possible L2 redirect plus active interception |

Defensive tooling for hosts/switches you own:

```bash
# Compare neighbor state against admin expectations
ip neigh show
bridge fdb show          # if using a Linux bridge

# Observe ARP on an interface you own (not attacking anything)
sudo tcpdump -ni eth0 arp
```

Correlate the results with switch syslog (DAI denies) and the DHCP lease inventory.

---

## 8. Security notes: defense summary

| Issue | Risk | Defense |
|:---|:---|:---|
| Unauthenticated ARP | Forged cache binding | DAI + DHCP Snooping |
| Flat L2 | Easy lateral MITM / recon | VLAN / microsegmentation |
| Unrestricted GARP | Mass cache overwrite | Rate limiting / inspection policy |
| Stale static maps | Outage after a NIC swap | Runbook for updating static ARP |
| IPv6 ignored | Gap left by an "ARP only" focus | RA Guard, ND inspection |
| Cleartext protocols | Data is readable if MITM succeeds | TLS everywhere, plus HSTS |

Principle: treat local L2 as trusted only as far as switch policy actually enforces it. End-to-end encryption complements link-level access control, it does not replace it.

---

## 9. Cheatsheet: admin / your own lab

```bash
# ── Inspect neighbor table ───────────────────────────────────
ip neigh show
ip -4 neigh show dev eth0
ip -6 neigh show

# ── Manage entries on YOUR host (careful in prod) ────────────
sudo ip neigh add 10.0.0.1 lladdr aa:bb:cc:dd:ee:ff dev eth0 nud permanent
sudo ip neigh del 10.0.0.1 dev eth0
sudo ip neigh flush dev eth0

# ── Trigger resolution (legitimate traffic) ──────────────────
ping -c 1 10.0.0.9
ip neigh get 10.0.0.9 dev eth0

# ── Passive observation on interfaces you own ────────────────
sudo tcpdump -ni eth0 'arp' -vv
sudo tcpdump -ni eth0 'arp and arp[6:2] == 2'   # replies only

# ── MAC / FDB visibility (Linux bridge) ──────────────────────
ip link show
bridge link show
bridge fdb show
```

| Command | Use |
|:---|:---|
| `ip neigh` | View/edit the ARP/ND cache |
| `tcpdump arp` | Audit ARP traffic on your own NIC |
| `bridge fdb` | View MAC learning on the bridge |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - W. Richard Stevens, *UNIX Network Programming, Vol. 1*, `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 826 (ARP), RFC 5227 (IPv4 Address Conflict Detection), RFC 4861 (NDP)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on. No poisoning playbook included.
