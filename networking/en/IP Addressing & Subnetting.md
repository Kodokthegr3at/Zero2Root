# IP Addressing, Subnetting & Network Routing

> **LearnCybersecurity** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-040` | **Phase 2:** Networking
> **Est. study:** 4-5h | **Level:** Intermediate
> **Prerequisites:** LC-038
> **Book map:** Kurose & Ross, Computer Networking Ch.4; Stallings, Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->

## Table of contents

1. IPv4 vs IPv6
2. Binary representation & mask algebra
3. Core CIDR formulas
4. Worked example: `192.168.1.0/26`
5. RFC 1918 & special ranges
6. Routing: longest prefix match
7. NAT & PAT
8. ICMP & diagnostics
9. Security notes
10. Cheatsheet

---

## 1. IPv4 vs IPv6

An IP address is a logical identifier at the network layer (OSI L3 / TCP-IP Internet layer) that lets packets be routed between networks.

| Characteristic | IPv4 | IPv6 |
|:---|:---|:---|
| Length | 32-bit (4 octets) | 128-bit |
| Notation | Dotted decimal `192.168.1.1` | Hex `2001:db8::1` |
| Address space | $2^{32} \approx 4.29\times 10^9$ | $2^{128} \approx 3.4\times 10^{38}$ |
| Header | 20 to 60 B (with options) | 40 B fixed + extension headers |
| Configuration | Manual / DHCP | SLAAC / DHCPv6 |
| Broadcast | Present | Absent (multicast/anycast instead) |

IPv4 address exhaustion drove the adoption of CIDR, NAT, and eventually IPv6. Security tooling needs to understand both stacks, including dual-stack hosts and IPv6 exposure that administrators sometimes overlook.

---

## 2. Binary representation & mask algebra

### 2.1 Octet

One octet is $8$ bits, with a value of $0..255$:

$$
v = b_7\cdot 2^7 + b_6\cdot 2^6 + \cdots + b_0\cdot 2^0
$$

Example: `192` = `11000000`, `168` = `10101000`.

### 2.2 Network mask

A prefix length $p$ (CIDR `/p`) means the leftmost $p$ bits are the **network** portion and the rest, $h=32-p$, are the **host** portion (for IPv4):

$$
\mathsf{mask} = \underbrace{1\ldots 1}_{p}\,\underbrace{0\ldots 0}_{32-p}
$$

Core operations:

$$
\begin{aligned}
\mathsf{NetworkAddress}(A,p) &= A \land \mathsf{mask}(p) \\
\mathsf{Broadcast}(A,p) &= A \lor \neg\mathsf{mask}(p) \\
\mathsf{HostBits}(A,p) &= A \land \neg\mathsf{mask}(p)
\end{aligned}
$$

Two addresses $A,B$ sit on the same subnet if and only if:

$$
A \land \mathsf{mask}(p) = B \land \mathsf{mask}(p)
$$

---

## 3. Core CIDR formulas

Take a prefix `/p` for IPv4 ($0 \le p \le 32$), with $h = 32 - p$.

| Quantity | Formula |
|:---|:---|
| Block size (total addresses) | $N = 2^{h} = 2^{32-p}$ |
| Usable hosts (classic subnet) | $N_{\text{usable}} = 2^{h} - 2$ (except `/31` point-to-point links under RFC 3021, and `/32` as a host route) |
| Number of subnets when $n$ bits are borrowed from the parent block | $2^{n}$ |
| Decimal subnet mask | convert $\mathsf{mask}(p)$ to 4 octets |
| Increment / stride between subnets | $2^{h}$ in the relevant octet |

**Quick mask table:**

| Prefix | Mask | $h$ | Total | Usable |
|:---:|:---|:---:|:---:|:---:|
| /8 | 255.0.0.0 | 24 | 16,777,216 | 16,777,214 |
| /16 | 255.255.0.0 | 16 | 65,536 | 65,534 |
| /24 | 255.255.255.0 | 8 | 256 | 254 |
| /25 | 255.255.255.128 | 7 | 128 | 126 |
| /26 | 255.255.255.192 | 6 | 64 | 62 |
| /27 | 255.255.255.224 | 5 | 32 | 30 |
| /28 | 255.255.255.240 | 4 | 16 | 14 |
| /30 | 255.255.255.252 | 2 | 4 | 2 |
| /32 | 255.255.255.255 | 0 | 1 | 1 (host) |

### VLSM (Variable Length Subnet Mask)

VLSM allocates blocks of uneven size: large subnets for access networks, `/30` or `/31` for router links. The blocks must not overlap and must be aligned on the $2^{h}$ boundary.

Procedure:

1. Sort host requirements from largest to smallest.
2. For a requirement of $H$ hosts, pick the smallest $h$ such that $2^{h}-2 \ge H$ (or $2^{h}\ge H$ for special cases such as point-to-point links).
3. Take the next prefix that is still free and aligned.

---

## 4. Worked example: `192.168.1.0/26`

$$
p=26,\quad h=6,\quad N=2^6=64,\quad N_{\text{usable}}=62
$$

Mask: `255.255.255.192` (`11111111.11111111.11111111.11000000`).

Splitting `192.168.1.0/24` into `/26` blocks borrows $n=2$ bits, giving $2^2=4$ subnets:

| # | Network | Usable range | Broadcast |
|:---:|:---|:---|:---|
| 0 | 192.168.1.0/26 | .1 – .62 | .63 |
| 1 | 192.168.1.64/26 | .65 – .126 | .127 |
| 2 | 192.168.1.128/26 | .129 – .190 | .191 |
| 3 | 192.168.1.192/26 | .193 – .254 | .255 |

Alignment check: the network address must be evenly divisible by 64 in the last octet.

The rule that always holds: `broadcast = network + size - 1`, and the next subnet starts at `network + size`.

---

## 5. RFC 1918 & special ranges

```
┌────────────────────────────────────────────────────────────┐
│ RFC 1918 PRIVATE BLOCKS                                    │
│  10.0.0.0/8        (10.0.0.0 – 10.255.255.255)             │
│  172.16.0.0/12     (172.16.0.0 – 172.31.255.255)           │
│  192.168.0.0/16    (192.168.0.0 – 192.168.255.255)         │
├────────────────────────────────────────────────────────────┤
│ SPECIAL                                                    │
│  127.0.0.0/8       loopback                                │
│  169.254.0.0/16    link-local (APIPA)                      │
│  224.0.0.0/4       IPv4 multicast                          │
│  0.0.0.0/8         "this network" / unspecified            │
│  100.64.0.0/10     CGNAT (RFC 6598)                        │
└────────────────────────────────────────────────────────────┘
```

Private addresses are not globally unique and may overlap between organizations. Reaching the public Internet requires NAT or a dual-stack public address.

---

## 6. Routing: longest prefix match

A router chooses the route with the longest prefix that matches the destination:

$$
\mathsf{route}(D) = \arg\max_{r:\; D\in r.\mathsf{prefix}} |r.p|
$$

Example: for $D=$ `192.168.1.10`, if the routing table has `192.168.0.0/16` via A and `192.168.1.0/24` via B, the router picks the `/24` route because it is more specific.

Default route: `0.0.0.0/0` for IPv4, `::/0` for IPv6.

---

## 7. NAT & PAT

NAT (Network Address Translation) maps addresses at a network boundary, typically between a private and a public address space.

| Type | Mapping | Use |
|:---|:---|:---|
| Static NAT | Fixed 1 to 1 | Servers that need a stable public IP |
| Dynamic NAT | From a public pool | Rarely used on its own in SOHO setups |
| PAT / overload | Many to 1 via a port | Typical home/office setup |

The PAT model, intuitively:

$$
(sip, sport, dip, dport, proto) \;\leftrightarrow\; (SIP_{pub}, SPORT', dip, dport, proto)
$$

The state table on the NAT device remembers $SPORT'$ so replies get routed back to the correct private host.

Security implication: NAT is not a firewall. The network still needs stateful filtering, a reverse proxy, and hardening. NAT also complicates end-to-end communication (VoIP, IPsec); IPv6 restores direct host-to-host addressability, so security design has to adjust accordingly.

Understand NAT for troubleshooting and architecture, not as an access-control mechanism by itself.

---

## 8. ICMP & diagnostics

### Ping

- IPv4: Echo Request Type 8, Echo Reply Type 0.
- Ping measures reachability and a sampled RTT, not throughput.

**TTL / Hop Limit heuristics** (rough, and admin-adjustable):

| Initial TTL observed | OS hint |
|:---:|:---|
| ~64 | Most Linux/Unix |
| ~128 | Most Windows |
| ~255 | Most network devices |

### Traceroute

Traceroute sends packets with $TTL=1,2,3,\ldots$ in sequence. Each hop that decrements the TTL to 0 replies with an ICMP Time Exceeded (Type 11). Building the sequence of replies reconstructs the path hop by hop, though the path may be asymmetric or partially filtered.

---

## 9. Security notes

| Issue | Risk | Defense |
|:---|:---|:---|
| IP spoofing | Disguises the packet source, often used for reflection attacks | uRPF, ingress/egress ACLs, BCP38 |
| Overly flat L3 | Easy lateral movement once one host is compromised | VLAN/subnet segmentation plus east-west firewalling |
| Exposed management | SSH/RDP sitting on a regular user segment | Separate management VRF/VLAN |
| Shadow IPv6 | Dual-stack hosts that go unmonitored | IPv6 inventory, RA Guard |
| Overly open ICMP policy | Reconnaissance and abuse | Rate-limit; do not blanket-block all ICMP (PMTUD needs Type 3 Code 4) |

Lab hygiene: map interfaces and routes on a machine you own (`ip addr`, `ip route`) before experimenting with routing or firewall changes. A misconfigured prefix is a common root cause of outages.

---

## 10. Cheatsheet

### CIDR mental math

- `/24` → 256 addresses, stride 1 in the last octet
- `/25` → 128 addresses, stride 128
- `/26` → 64 addresses, stride 64
- `/27` → 32 addresses, stride 32
- `/28` → 16 addresses, stride 16
- `/30` → 4 addresses, stride 4 (typical for point-to-point links)

```bash
# ── Inspection (your host) ────────────────────────────────────
ip -c addr show
ip route show
ip -4 route get 1.1.1.1
ip neighbor show

# ── Diagnostics ──────────────────────────────────────────────
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
mtr -n 1.1.1.1

# ── Subnet calculator helpers ────────────────────────────────
ipcalc 192.168.1.0/26          # if installed
python3 -c "import ipaddress as i; n=i.ip_network('192.168.1.0/26');
print(n.network_address, n.broadcast_address, n.num_addresses)"
```

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1918, RFC 4632 (CIDR), RFC 3021 (/31), RFC 6598 (CGNAT)
> - `man ip`, `man ping`, `man traceroute`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on.
