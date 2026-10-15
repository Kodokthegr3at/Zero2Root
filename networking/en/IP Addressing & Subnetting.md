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
2. Reading an address in binary
3. Subnet masks and CIDR
4. A worked example: splitting a network
5. Private and special address ranges
6. How routers choose a path
7. NAT: sharing one public address
8. ICMP, ping, and traceroute
9. Security notes
10. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| IP address | The logical address of a device on a network, like `192.168.1.10` |
| Octet | One of the four numbers in an IPv4 address (each is 8 bits, 0–255) |
| Subnet | A smaller slice carved out of a larger network |
| Subnet mask | The marker that says which part of an address is "network" and which is "host" |
| CIDR `/n` | A short way to write the mask: `/24` means the first 24 bits are the network part |
| Network address | The first address in a subnet; it names the subnet itself |
| Broadcast address | The last address in a subnet; a message to everyone on it |
| Gateway | The router a device sends traffic to when the destination is on another network |
| NAT | Letting many private devices share one public IP address |
| Private address | An address (like `192.168.x.x`) usable only inside a local network, not on the public Internet |

---

## 1. IPv4 vs IPv6

An **IP address** is the logical name a device uses on a network (OSI Layer 3). It's what lets a packet be routed from one network to another.

| | IPv4 | IPv6 |
|:---|:---|:---|
| Length | 32 bits | 128 bits |
| Looks like | `192.168.1.1` | `2001:db8::1` |
| How many addresses | about 4.3 billion | about 3.4 × 10³⁸ (effectively endless) |
| Setup | manual or DHCP | auto (SLAAC) or DHCPv6 |
| Broadcast | yes | no (uses multicast instead) |

IPv4 simply ran out of addresses, which is why NAT (Section 7) and eventually IPv6 appeared. Security tools need to understand both, because a device often has **both** at once (dual-stack), and an unwatched IPv6 address is an easy thing to forget about.

---

## 2. Reading an Address in Binary

Each of the four numbers in an IPv4 address (each **octet**) is really 8 bits. Each bit stands for a value:

```text
bit:     b7   b6   b5   b4   b3   b2   b1   b0
value:  128   64   32   16    8    4    2    1
```

To turn bits into the decimal number, add up the values where the bit is 1:

```text
11000000  →  128 + 64            = 192
10101000  →  128 +    32 + 8     = 168
```

So `11000000.10101000.00000001.00000001` is just `192.168.1.1`. Subnetting is all about where you draw a line through those 32 bits.

---

## 3. Subnet Masks and CIDR

An address has two parts: a **network** part (which network am I on?) and a **host** part (which device am I?). The **subnet mask** marks the boundary. In CIDR notation, `/n` means "the first n bits are network, the rest are host."

```text
/24  →  11111111.11111111.11111111.00000000  =  255.255.255.0
        └────── 24 network bits ──────┘└ 8 host bits ┘
```

From the mask you can work out three key addresses of a subnet:

```text
network address = the lowest address (all host bits 0)  → names the subnet
broadcast       = the highest address (all host bits 1) → "everyone here"
usable hosts    = everything in between

Example, 192.168.1.0/24:
  network   = 192.168.1.0
  broadcast = 192.168.1.255
  usable    = 192.168.1.1  …  192.168.1.254   (254 devices)
```

Two addresses are on the **same subnet** only if they share the same network part. That's exactly what decides whether your computer talks to another device directly, or has to send through the gateway.

### Quick mask reference

| CIDR | Mask | Host bits | Total addresses | Usable devices |
|:---:|:---|:---:|:---:|:---:|
| /24 | 255.255.255.0 | 8 | 256 | 254 |
| /25 | 255.255.255.128 | 7 | 128 | 126 |
| /26 | 255.255.255.192 | 6 | 64 | 62 |
| /27 | 255.255.255.224 | 5 | 32 | 30 |
| /28 | 255.255.255.240 | 4 | 16 | 14 |
| /30 | 255.255.255.252 | 2 | 4 | 2 |

The pattern: each extra bit of host space **doubles** the number of addresses. "Usable" is always two fewer, because the network and broadcast addresses can't be assigned to a device. (The `/30` with 2 usable hosts is the classic choice for a link between two routers.)

---

## 4. A Worked Example: Splitting a Network

Say you have `192.168.1.0/24` (256 addresses) and want to split it into **four equal subnets**.

Four pieces means borrowing 2 more bits from the host part (because 2² = 4), which turns `/24` into `/26`. Each `/26` has 64 addresses:

| # | Network | Usable range | Broadcast |
|:---:|:---|:---|:---|
| 1 | 192.168.1.0/26 | .1 – .62 | .63 |
| 2 | 192.168.1.64/26 | .65 – .126 | .127 |
| 3 | 192.168.1.128/26 | .129 – .190 | .191 |
| 4 | 192.168.1.192/26 | .193 – .254 | .255 |

Two rules make this easy to do in your head:

- Each subnet is 64 wide, so the networks step by 64: `.0, .64, .128, .192`.
- The broadcast is always `next network − 1`.

When different subnets need different sizes (a big office LAN, a tiny 2-address router link), you give each one the smallest subnet that fits, biggest first, without overlapping. That's called **VLSM** (Variable Length Subnet Mask).

---

## 5. Private and Special Address Ranges

Some ranges are reserved for use inside local networks. They're not unique worldwide, so they can't appear directly on the public Internet; they reach it through NAT (Section 7).

```
┌────────────────────────────────────────────────────────────┐
│ PRIVATE (RFC 1918) — free to use inside your own network   │
│  10.0.0.0/8        10.0.0.0     – 10.255.255.255           │
│  172.16.0.0/12     172.16.0.0   – 172.31.255.255           │
│  192.168.0.0/16    192.168.0.0  – 192.168.255.255          │
├────────────────────────────────────────────────────────────┤
│ SPECIAL                                                    │
│  127.0.0.0/8       loopback ("this machine")               │
│  169.254.0.0/16    link-local (shows up when DHCP fails)   │
│  224.0.0.0/4       multicast                               │
└────────────────────────────────────────────────────────────┘
```

Seeing a `169.254.x.x` address on a machine is a useful clue: it usually means DHCP didn't answer, so the device picked an address by itself.

---

## 6. How Routers Choose a Path

A router may know several routes that could fit a destination. The rule is simple: **the most specific one wins** (longest prefix match).

```text
Destination: 192.168.1.10

Route A: 192.168.0.0/16  via router X   (broad: a whole /16)
Route B: 192.168.1.0/24  via router Y   (specific: just this /24)

→ the router picks B, because /24 is more specific than /16
```

If nothing else matches, traffic falls to the **default route** `0.0.0.0/0` (`::/0` for IPv6), which is how your machine reaches the wider Internet through its gateway.

---

## 7. NAT: Sharing One Public Address

Your home has one public IP but many devices. **NAT** (Network Address Translation) lets them all share it. The router rewrites the private source address of outgoing traffic to its own public address, and remembers which internal device each conversation belongs to (by tracking the port numbers) so replies get back to the right one.

```text
laptop 192.168.1.10:51000  →  router  →  public 203.0.113.5:62000  →  Internet
                                 (remembers the mapping)
reply  ←──────────────────────  router  ←───────────────────────────  reply
```

| Type | What it does |
|:---|:---|
| Static NAT | A fixed 1-to-1 mapping, for a server that needs a steady public IP |
| PAT / "overload" | Many devices behind one public IP (the normal home/office setup) |

Important security point: **NAT is not a firewall.** It hides internal addresses as a side effect, but it doesn't decide what's allowed. You still need real filtering. IPv6 often skips NAT entirely (there are enough addresses), so don't assume "we have NAT" means "we're protected."

---

## 8. ICMP, Ping, and Traceroute

**ICMP** is the network layer's messenger protocol: it carries reachability checks and error reports.

**Ping** sends an ICMP "are you there?" and waits for a reply. It tells you if a host is reachable and roughly how long the round trip takes, nothing more.

The reply's **TTL** gives a rough hint about the other system (these are just defaults and can be changed):

| TTL seen | Likely system |
|:---:|:---|
| ~64 | Linux / Unix / macOS |
| ~128 | Windows |
| ~255 | A network device (router, switch) |

**Traceroute** is a clever use of TTL. It sends packets with TTL = 1, then 2, then 3, and so on. Each router that drops a packet when the TTL hits 0 reports back, so you learn the path hop by hop.

```bash
ping -c 4 1.1.1.1      # reachable? round-trip time?
traceroute -n 1.1.1.1  # what path does it take?
```

---

## 9. Security Notes

| Issue | Risk | Defense |
|:---|:---|:---|
| IP spoofing | Faking the source to hide or to bounce attacks off others | Source filtering at the edge (BCP38 / uRPF) |
| One big flat network | If one host is hacked, the attacker reaches everything easily | Split into subnets/VLANs with filtering between them |
| Exposed management | SSH/RDP sitting on the normal user network | A separate management subnet |
| Forgotten IPv6 | A dual-stack host that nobody is monitoring on v6 | Inventory IPv6 too; RA Guard |
| Blocking all ICMP | Breaks useful diagnostics and path-MTU discovery | Rate-limit instead of a blanket block |

Lab hygiene: look at your own interfaces and routes (`ip addr`, `ip route`) before changing anything. A wrong subnet mask or route is one of the most common causes of an outage.

---

## 10. Cheatsheet

### Mental math

- `/24` → 256 addresses, networks step by 1 in the last octet
- `/25` → 128 addresses, step by 128
- `/26` → 64 addresses, step by 64
- `/27` → 32 addresses, step by 32
- `/28` → 16 addresses, step by 16
- `/30` → 4 addresses (2 usable), the classic router-to-router link

```bash
# ── Inspect your own machine ─────────────────────────────────
ip -c addr show
ip route show
ip -4 route get 1.1.1.1    # which route/gateway would be used?
ip neighbor show

# ── Diagnostics ──────────────────────────────────────────────
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
mtr -n 1.1.1.1             # live, continuous traceroute

# ── Subnet calculators ───────────────────────────────────────
ipcalc 192.168.1.0/26       # if installed
python3 -c "import ipaddress as i; n=i.ip_network('192.168.1.0/26'); \
print(n.network_address, n.broadcast_address, n.num_addresses)"
```

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1918, RFC 4632 (CIDR), RFC 3021 (/31), RFC 6598 (CGNAT)
> - `man ip`, `man ping`, `man traceroute`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on.
