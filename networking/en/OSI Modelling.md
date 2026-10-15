# OSI Model

> **LearnCybersecurity** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-038` | **Phase 2:** Networking
> **Est. study:** 6-8h | **Level:** Beginner
> **Prerequisites:** LC-005
> **Book map:** Kurose & Ross, Computer Networking Ch.1-2; Stallings, Network Security Essentials Ch.2
<!-- LC-CURRICULUM-END -->

## Table of contents

1. What the OSI model is, and why it matters
2. The seven layers, one by one
3. How data travels: encapsulation
4. TCP vs UDP
5. Ports you should know
6. Which device works at which layer
7. Attacks and defenses, layer by layer
8. Troubleshooting with the layers
9. OSI vs the TCP/IP model
10. Quick reference

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Protocol | An agreed set of rules two computers follow so they can understand each other |
| Layer | One "job" in networking. Each layer handles its own task and hands the result to the next |
| PDU | The name for the chunk of data at a given layer (bits, frame, packet, segment, data) |
| MAC address | The hardware ID burned into a network card, used inside one local network |
| IP address | The logical address used to route data across different networks |
| Port | A number that says which program on a computer the data is for (web = 80, SSH = 22) |
| Header | Extra info a layer adds in front of the data (addresses, ports, and so on) |
| Encapsulation | Wrapping the data in headers as it moves down the layers |
| Frame / packet / segment | The data unit at the Data Link / Network / Transport layer |

---

## 1. What the OSI Model Is, and Why It Matters

The **OSI model** (Open Systems Interconnection) is a way of splitting "how computers talk over a network" into **7 layers**, each with one clear job. It was published by the ISO standards body in 1984.

Think of sending a parcel. One person writes the letter, another puts it in an envelope and addresses it, a courier decides the route, a truck physically carries it. Each step only cares about its own job and trusts the others to do theirs. Networking works the same way: each layer does its part and hands off to the next.

The OSI model is a **teaching and troubleshooting map**. Real networks actually run on the simpler TCP/IP model (Section 9), but OSI is the shared vocabulary everyone uses to describe where something happens.

Why it matters for security:

- Knowing *which layer* an attack hits tells you where to put the defense (a web firewall won't stop an attack on the cables).
- Understanding how data is wrapped layer by layer is the basis of packet analysis.
- Knowing which protocols live at each layer guides firewall and IDS/IPS rules.

### The seven layers at a glance

```
┌───────┬──────────────────┬────────────────────────────────────────────┐
│ Layer │   Name           │  What it does                               │
├───────┼──────────────────┼────────────────────────────────────────────┤
│   7   │  Application     │  Protocols apps use (HTTP, DNS, SSH)        │
│   6   │  Presentation    │  Formatting, encryption, compression        │
│   5   │  Session         │  Starting, keeping, and ending conversations │
│   4   │  Transport       │  TCP/UDP, ports, reliable delivery           │
│   3   │  Network         │  IP addresses, routing between networks      │
│   2   │  Data Link       │  MAC addresses, switches, frames             │
│   1   │  Physical        │  Cables, radio, raw bits                     │
└───────┴──────────────────┴────────────────────────────────────────────┘

A memory trick, top to bottom:
  "All People Seem To Need Data Processing"
```

---

## 2. The Seven Layers, One by One

### Layer 1 — Physical: moving raw bits

The lowest layer. It carries plain 1s and 0s as electrical pulses, light, or radio waves. It doesn't understand what the data means; it just moves signals from A to B. This is cables, fiber, connectors, radio, and the devices that only repeat signals (hubs, repeaters).

Useful, harmless commands to inspect it:

```bash
ip link show            # is the interface up? (Linux)
ethtool eth0            # speed, duplex, "Link detected: yes"
ip -s link show eth0    # error counters (bad cable, interference)
```

| Media | Typical speed | Max distance |
|-------|-------|---------------|
| Cat5e cable | 1 Gbps | 100 m |
| Cat6 cable | 10 Gbps | 55 m |
| Fiber (single-mode) | 100 Gbps+ | 40–80 km |
| Wi-Fi 6 | up to ~9.6 Gbps | ~100 m |

### Layer 2 — Data Link: talking to the device next door

This layer moves data between two devices on the **same local network**, using **MAC addresses** (the hardware ID of each network card). Its data unit is the **frame**. The main device here is the **switch**, which learns which MAC is on which port and forwards frames accordingly.

```bash
ip link show      # your own MAC address
ip neigh show     # the ARP table: which IP maps to which MAC
```

Protocols to know: **Ethernet** (wired LAN frames), **ARP** (finds the MAC for an IP, covered in LC-042), **802.1Q** (VLAN tags), **STP** (stops loops between switches).

### Layer 3 — Network: finding a path across networks

This layer gets data from one network to another using **IP addresses**, and chooses the route. Its data unit is the **packet**, and its main device is the **router**.

```bash
ip addr show          # your IP addresses
ip route show         # your routing table / default gateway
ping -c 4 8.8.8.8     # can I reach that host at all? (ICMP)
traceroute 8.8.8.8    # what path do packets take?
```

Protocols: **IPv4/IPv6** (addressing), **ICMP** (ping and error messages), **OSPF/BGP** (routers sharing routes).

### Layer 4 — Transport: getting data to the right program, reliably

This layer connects **programs**, not just machines, using **port numbers**. It has two main choices:

- **TCP:** sets up a connection first, guarantees everything arrives in order, re-sends anything lost. Used for web, SSH, email.
- **UDP:** just fires data off with no setup and no guarantees. Faster, used for DNS, video calls, games.

```bash
ss -tulnp             # which ports are open and listening (Linux)
nc -zv host 22        # is a given TCP port reachable?
```

### Layer 5 — Session: managing the conversation

Starts, maintains, and cleanly ends a "session" between two applications. If a transfer drops, the session layer is the idea that lets it resume from the right place. Examples: NetBIOS and SMB sessions (Windows file sharing), RPC, iSCSI.

### Layer 6 — Presentation: translating and securing the data

The "translator". It makes sure data from one system can be read by another: character encodings (ASCII, Unicode), compression (gzip), and **encryption (TLS lives here)**. Base64 and image formats like JPEG/PNG are presentation-layer concerns too.

```bash
echo "Hello" | base64          # encode
echo "SGVsbG8K" | base64 -d    # decode
openssl s_client -connect example.com:443 </dev/null   # inspect a TLS connection
```

### Layer 7 — Application: what programs actually speak

The top layer, closest to the user. It's the **network protocols** applications use, not the apps themselves. HTTP, DNS, FTP, SSH, SMTP, SNMP, LDAP, RDP, SMB all live here.

> Note: "Application layer" does **not** mean Chrome or Firefox. It means the protocol (HTTP) those programs speak.

```bash
curl -I https://example.com    # look at HTTP response headers
dig example.com                # DNS lookup
```

| Protocol | Port | Use |
|----------|------|----------|
| HTTP / HTTPS | 80 / 443 | Web |
| DNS | 53 | Name lookups |
| SSH | 22 | Secure remote shell |
| FTP | 21 | File transfer (cleartext) |
| SMTP | 25 | Sending email |
| SMB | 445 | Windows file sharing |
| RDP | 3389 | Remote desktop |

---

## 3. How Data Travels: Encapsulation

When you send something, it moves **down** the layers on your machine. Each layer wraps the data in its own **header**, like putting a letter inside envelopes inside bigger envelopes. On the other side, each layer unwraps its envelope on the way **up**.

```
YOUR COMPUTER (going down)              THE OTHER COMPUTER (going up)

L7  Data                               L7  Data
L6  Data                               L6  Data
L5  Data                               L5  Data
L4  [TCP header | Data]  = Segment     L4  [TCP header | Data]
L3  [IP header | Segment] = Packet     L3  [IP header | ...]
L2  [MAC header | Packet | FCS] = Frame L2 [MAC header | ... | FCS]
L1  101000110101...  = Bits            L1  101000110101...

            ─────── physical medium ───────>
```

Each layer only reads *its own* header. The data unit gets a different name at each level: **bits** (L1), **frame** (L2), **packet** (L3), **segment** (L4), and just **data** above that.

---

## 4. TCP vs UDP

Both live at Layer 4, but they behave very differently.

| Aspect | TCP | UDP |
|--------|-----|-----|
| Data unit | Segment | Datagram |
| Connection | Yes (3-way handshake) | No |
| Reliable? | Yes, re-sends lost data | No guarantee |
| In order? | Yes | Not guaranteed |
| Speed | Slower (more overhead) | Faster |
| Good for | Web, SSH, file transfer, email | DNS, video calls, games |

### The TCP 3-way handshake

Before TCP sends real data, both sides say hello in three steps. It's like a phone call: "Can you hear me?" — "Yes, can you hear me?" — "Yes."

```
Client                          Server
  │──── SYN ─────────────────────>│   1. "I want to talk"
  │<─── SYN + ACK ────────────────│   2. "OK, and I want to talk too"
  │──── ACK ─────────────────────>│   3. "Great, let's go"
  │<════ data flows both ways ═══>│
```

Closing the connection is a similar polite exchange (FIN / ACK) in both directions.

---

## 5. Ports You Should Know

A **port** is a number from 0 to 65535 that says which service on a machine the traffic is for. Three ranges:

- **0–1023:** well-known ports (HTTP 80, SSH 22). On most systems only an administrator can open these.
- **1024–49151:** registered ports for specific apps.
- **49152–65535:** temporary ports, picked automatically for each outgoing connection.

```bash
# Simple, legitimate discovery of what's open on a host you own
nmap host              # the common ports
nmap -p- host          # every port
nc -zv host 443        # check one specific port
```

| Port | Service | Why it's sensitive |
|------|---------|--------------------|
| 21 | FTP | Sends passwords in cleartext |
| 22 | SSH | A common login target; use keys, not passwords |
| 23 | Telnet | Cleartext; should be retired |
| 25 | SMTP | Email; can be abused to enumerate users or relay spam |
| 53 | DNS | Can leak internal names (zone transfer) |
| 80 / 443 | HTTP / HTTPS | The whole web-attack surface |
| 139 / 445 | NetBIOS / SMB | Windows file sharing; historically very exploited |
| 3389 | RDP | Remote desktop; a frequent brute-force target |
| 3306 / 5432 | MySQL / PostgreSQL | Databases exposed with weak or default logins |
| 6379 | Redis | Often left with no authentication at all |

---

## 6. Which Device Works at Which Layer

| Layer | Devices | Job |
|-------|---------|-----|
| 7 Application | Web firewall (WAF), proxy, load balancer | Filter and inspect HTTP/TLS |
| 4 Transport | Stateful firewall | Allow/block by port and connection |
| 3 Network | Router, Layer-3 switch | Route between networks |
| 2 Data Link | Switch, bridge, access point | Forward frames by MAC |
| 1 Physical | Hub, repeater, cable, network card | Carry the signal |

A quick way to see the Layer-3 router your own machine uses:

```bash
ip route | grep default    # the default gateway = your router
```

---

## 7. Attacks and Defenses, Layer by Layer

Every layer can be attacked in its own way. The goal here is to recognize **what kind of attack belongs to which layer, and how it's defended**, so you can place the right control. This is a defender's map, not an attack manual: specific exploit commands are intentionally left out, and other lessons (LC-042 ARP, LC-039 Wireless, the web module) go deeper on the concepts.

| Layer | Example attacks (what they are) | How to defend |
|-------|---------------------------------|---------------|
| 7 Application | SQL injection, XSS, request forgery, phishing: abusing the app's own logic | Input validation, patching, a web application firewall |
| 6 Presentation | TLS downgrade / SSL stripping: forcing a weaker or plaintext connection | Enforce HTTPS (HSTS), modern TLS 1.3, reject old ciphers |
| 5 Session | Session hijacking, credential-replay attacks: reusing a stolen session or hash | Rotate session tokens, require MFA, harden authentication |
| 4 Transport | SYN flood, port scanning, UDP flood: exhausting or probing services | SYN cookies, rate limiting, a stateful firewall |
| 3 Network | IP spoofing, ICMP flood, route poisoning: faking addresses or routes | Ingress filtering (uRPF), ACLs, ICMP rate limits |
| 2 Data Link | ARP spoofing, MAC flooding, VLAN hopping: tricking the local switch | Dynamic ARP Inspection, switch port security |
| 1 Physical | Wiretapping, rogue "evil twin" Wi-Fi, jamming | Physical access control, always encrypt (VPN, HTTPS) |

The single most useful takeaway: a control only protects its own layer. Encryption at Layer 6 does nothing against someone unplugging a cable at Layer 1, and a Layer-7 web firewall does nothing against a Layer-2 ARP spoof. Real security stacks defenses at several layers at once (defense in depth).

---

## 8. Troubleshooting with the Layers

The layers give you a checklist when "it's not working." Start at the bottom and work up: if a lower layer is broken, nothing above it can work.

```
Can't reach a server?

L1 Physical:   Is the cable in / Wi-Fi connected? Is the link up?
               ip link show eth0   → look for "state UP"

L2 Data Link:  Can you see the gateway's MAC?
               ip neigh show

L3 Network:    Can you ping the gateway, then a public IP?
               ping 192.168.1.1  then  ping 8.8.8.8
               ip route show     → is there a default route?

L4 Transport:  Is the port actually open?
               nc -zv target 443

L5/6 Session/Presentation:  Is the TLS certificate valid / not expired?
               openssl s_client -connect target:443

L7 Application: What does the service say?
               curl -v https://target   → check the status code and logs
```

---

## 9. OSI vs the TCP/IP Model

Real networks run on the 4-layer TCP/IP model. OSI's seven layers map onto it like this:

```
OSI Model                    TCP/IP Model          Examples
Layer 7 Application  ┐
Layer 6 Presentation ├──────  Application          HTTP, DNS, SSH, TLS
Layer 5 Session      ┘
Layer 4 Transport    ───────  Transport            TCP, UDP
Layer 3 Network      ───────  Internet             IP, ICMP
Layer 2 Data Link    ┐
Layer 1 Physical     ┴──────  Network Access       Ethernet, Wi-Fi, ARP
```

Use OSI to *reason and talk* about where something happens; the traffic on the wire is TCP/IP.

---

## 10. Quick Reference

```text
LAYER CHEAT SHEET (top → bottom)
  L7 Application   HTTP, DNS, SSH, SMB          (what apps speak)
  L6 Presentation  TLS, Base64, JPEG            (format & encryption)
  L5 Session       NetBIOS, RPC, SMB sessions   (managing the conversation)
  L4 Transport     TCP (reliable), UDP (fast)   [PORTS]
  L3 Network       IP, ICMP, routing            [IP ADDRESSES]
  L2 Data Link     Ethernet, ARP, VLAN          [MAC ADDRESSES]
  L1 Physical      cables, radio, bits          [HARDWARE]

DATA UNIT PER LAYER
  L7–L5 Data → L4 Segment/Datagram → L3 Packet → L2 Frame → L1 Bits

MEMORY TRICKS
  top → bottom:  All People Seem To Need Data Processing
  bottom → top:  Please Do Not Throw Sausage Pizza Away
```

### Complete OSI reference table

| Layer | Name | PDU | Address | Device | Key protocols |
|-------|------|-----|---------|--------|---------------|
| 7 | Application | Data | — | WAF, proxy | HTTP, DNS, SSH |
| 6 | Presentation | Data | — | — | TLS, MIME |
| 5 | Session | Data | — | — | NetBIOS, RPC |
| 4 | Transport | Segment / Datagram | Port | Firewall | TCP, UDP |
| 3 | Network | Packet | IP address | Router | IPv4, IPv6, ICMP |
| 2 | Data Link | Frame | MAC address | Switch | Ethernet, ARP |
| 1 | Physical | Bits | — | Hub, NIC | Ethernet, DSL |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 793 (TCP), RFC 768 (UDP)
> - Nmap and Wireshark official documentation, the IANA port number registry

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on.
