# TCP/IP Architecture & Socket Programming

> **LearnCybersecurity** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Kurose & Ross, *Computer Networking*; Stevens, *UNIX Network Programming*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-039` | **Phase 2:** Networking
> **Est. study:** 5-6h | **Level:** Intermediate
> **Prerequisites:** LC-038
> **Book map:** Kurose & Ross, Computer Networking Ch.3-4; Stevens, UNIX Network Programming Vol.1 Ch.1-6
<!-- LC-CURRICULUM-END -->

## Table of contents

1. The 4-layer TCP/IP model
2. Inside an IP packet
3. Inside a TCP segment
4. The life of a TCP connection
5. The 3-way handshake
6. Flow and congestion control, made simple
7. Sockets: how programs actually use the network
8. SYN flood and SYN cookies
9. Security notes
10. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| TCP/IP | The real 4-layer model the Internet runs on |
| Packet / segment | The chunk of data at the Internet layer (packet) and Transport layer (segment) |
| Header | The label a layer sticks on the front of the data: who it's from, who it's for, and so on |
| Port | A number that picks which program the data is for |
| Socket | A program's "plug" into the network: one endpoint of a connection |
| 4-tuple | What uniquely identifies a connection: source IP + source port + destination IP + destination port |
| TTL | "Time to live": a counter that drops by one at each router, so lost packets eventually die |
| SYN / ACK / FIN / RST | TCP flags: start, acknowledge, finish, and abrupt reset |
| Window | How much data a receiver is willing to accept before pausing |
| Spoofing | Faking the source address of a packet |

---

## 1. The 4-Layer TCP/IP Model

The OSI model (LC-038) has 7 layers for teaching. Real networks run on a leaner **4-layer** model. Each layer wraps the one above it in a header, like nesting envelopes.

| Layer | Its job | Examples |
|:---|:---|:---|
| Application | What the app actually means to say | HTTP, DNS, SSH |
| Transport | Get it to the right program, reliably or quickly | TCP, UDP, QUIC |
| Internet | Get it to the right machine, across networks | IPv4, IPv6, ICMP |
| Link | Get it across one physical hop | Ethernet, Wi-Fi |

```
  ┌─────────────────────────────┐
  │  Application  (HTTP, …)     │
  ├─────────────────────────────┤
  │  Transport    (TCP/UDP)     │
  ├─────────────────────────────┤
  │  Internet     (IP)          │
  ├─────────────────────────────┤
  │  Link         (Eth/802.11)  │
  └─────────────────────────────┘
         going down ↓
  [Eth][IP][TCP][App data][FCS]
```

On the way up, each layer reads and strips its own header, then decides who to hand the rest to (using the EtherType, the IP protocol field, and port numbers). Security controls exist at every layer: there's no single magic layer, which is why real defense stacks several (defense in depth).

---

## 2. Inside an IP Packet

The Internet layer's job is addressing and routing. An IPv4 header is at least 20 bytes. You don't need to memorize the bit layout, but you should recognize the fields that matter for security.

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |    TOS/DSCP   |         Total Length          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|    Fragment Offset      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |   Protocol    |        Header Checksum        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Field | Why it matters |
|:---|:---|
| Version | 4 or 6 |
| Total Length | How big the whole packet is |
| Fragmentation (ID/Flags/Offset) | Splitting a big packet; old stacks could be tricked during reassembly, modern ones handle it well |
| TTL | Drops by 1 per router; stops packets looping forever, and leaks a hint about the sender's OS |
| Protocol | What's inside: 6 = TCP, 17 = UDP, 1 = ICMP |
| Source / Destination | The addresses; **the source can be faked** unless the network filters it |

```text
header size  = IHL × 4 bytes
payload size = Total Length − header size

Example: Total Length = 60, IHL = 5  →  header = 20 bytes  →  payload = 40 bytes
```

The most important security point here: an IP packet's **source address is just a claim**. Without filtering at the network edge, an attacker can write any source address they like (spoofing).

---

## 3. Inside a TCP Segment

TCP turns IP's unreliable "best effort" delivery into a reliable, ordered stream of bytes. It does this with the fields in its header.

| Field | What it's for |
|:---|:---|
| Source / Destination Port | Which program on each end |
| Sequence number | The position of this data in the stream |
| Acknowledgement number | "I've received everything up to here" |
| Flags | SYN (start), ACK (acknowledge), FIN (finish), RST (reset), and others |
| Window | How much more the receiver can accept right now |
| Checksum | Catches corrupted data |

A single connection is identified by four things together, the **4-tuple**:

```text
(source IP, source port, destination IP, destination port)
```

Two different browser tabs to the same site differ only in the source port, and that's enough to keep them apart.

---

## 4. The Life of a TCP Connection

A TCP connection moves through a series of states, like a phone call going from dialing, to talking, to hanging up.

```
  CLOSED ──listen──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──connect─► SYN_SENT ───────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT ──► TIME_WAIT ──► CLOSED
```

| State | Meaning |
|:---|:---|
| LISTEN | A server waiting for someone to connect |
| SYN_SENT / SYN_RCVD | Handshake in progress |
| ESTABLISHED | Connected, data flowing |
| TIME_WAIT | Just closed; waiting a moment so stray old packets die out |
| CLOSE_WAIT | The other side hung up; your app still needs to close |

```bash
ss -tan      # see every TCP connection and its state (Linux)
```

A common confusion: lots of `TIME_WAIT` entries look like a bug but are normal and healthy. Don't disable `TIME_WAIT` without understanding why it exists; it protects against old packets being mistaken for new ones.

---

## 5. The 3-Way Handshake

Before any data flows, both sides sync up in three steps. Think of it as: "Can you hear me?" — "Yes, can you hear me?" — "Yes."

```
  Client                     Server
    │  SYN, seq=x               │   1. "Let's talk, my counter starts at x"
    │──────────────────────────►│
    │  SYN+ACK, seq=y, ack=x+1  │   2. "OK, mine starts at y, got your x"
    │◄──────────────────────────│
    │  ACK, ack=y+1             │   3. "Got your y, let's go"
    │──────────────────────────►│
    │      ESTABLISHED          │
```

Each side picks a starting number (the **initial sequence number**, ISN). Modern systems generate the ISN in a hard-to-predict way, so an off-path attacker can't easily guess it and inject fake data. Closing is a similar polite exchange of FIN/ACK, or a single RST to slam the connection shut.

---

## 6. Flow and Congestion Control, Made Simple

TCP constantly answers two questions: "Is the receiver keeping up?" and "Is the network keeping up?"

- **Flow control** protects the *receiver*: it advertises a **window** (`rwnd`) saying how much it can take.
- **Congestion control** protects the *network*: the sender keeps its own limit (`cwnd`) so it doesn't flood a shared link.

```text
data allowed in flight ≤ the smaller of cwnd and rwnd
```

The sender is held back by whichever is smaller. When a connection starts, `cwnd` grows quickly (**slow start**, which actually doubles each round trip), then grows carefully, and backs off sharply when packets start getting lost.

```text
slow start: cwnd grows by one segment for each ACK
            → roughly doubles every round trip
```

You rarely tune this by hand. What you watch is round-trip time, retransmissions, and buffering delays. Security angle: floods of TCP or UDP traffic can congest a link into a denial of service, which is why rate limiting and capacity planning matter.

---

## 7. Sockets: How Programs Actually Use the Network

A **socket** is a program's handle on a network connection, one endpoint of the conversation. A TCP server follows a fixed recipe:

```text
socket  →  bind  →  listen  →  accept (loop)  →  recv / send  →  close
```

A client is simpler: `socket → connect → send / recv → close`.

### Python 3 example

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))   # listen on port 8080
    s.listen(128)
    conn, peer = s.accept()     # wait for a client
    with conn:
        data = conn.recv(4096)
        conn.sendall(b"OK\n")
```

| Call | What it does |
|:---|:---|
| `bind` | Claim a local address and port |
| `listen` | Start accepting connections (with a queue) |
| `accept` | Take the next ready connection |
| `connect` | Reach out to a server (client side) |

UDP is simpler: no handshake, use `sendto` / `recvfrom`.

Treat the network as hostile. Validate everything you read, set timeouts so a stalled peer can't hang you forever, and wrap sensitive traffic in TLS (Python's `ssl` module) rather than inventing your own protection.

---

## 8. SYN Flood and SYN Cookies

**The problem:** in the handshake, when a server gets a SYN it sets aside a little memory for the half-finished connection and waits for the final ACK. An attacker can send a flood of SYNs (often with faked source addresses) and never complete them. The server fills up with half-open connections and runs out of room for real users. That's a **SYN flood**, a kind of denial of service.

**The defense — SYN cookies:** instead of reserving memory on every SYN, the server encodes the needed information into the sequence number it sends back, protected by a secret. It only creates real connection state when a valid final ACK comes back carrying that encoded value. A flood of SYNs that never complete then costs the server almost nothing.

```text
reply sequence number ≈ Hash(secret, the 4-tuple, time) + size info
```

Other defenses: a sensible connection queue size, rate limiting SYNs per source, and a SYN-handling proxy or scrubbing service in front of public servers.

> This lesson explains the concept and defense, not how to run a flood.

---

## 9. Security Notes

| Issue | Risk | Defense |
|:---|:---|:---|
| SYN flood | Fills the server's half-open slots | SYN cookies, rate limiting, capacity planning |
| Spoofed source | Reflection and flood abuse | Source-address filtering at the edge (BCP38 / uRPF) |
| RST injection | Killing a session if the sequence is guessable | Encrypted transport; hard-to-guess ISNs |
| Cleartext TCP apps | Sniffing and tampering | TLS 1.3 |
| Listening on `0.0.0.0` | Exposed to every network by accident | Bind to an internal interface; firewall |

Lab hygiene: experiment with handshakes and sockets only on machines you own, and watch what happens defensively with `ss` and `tcpdump`.

---

## 10. Cheatsheet

```bash
# ── See connection state ─────────────────────────────────────
ss -tan                 # all TCP connections + state
ss -tanp state syn-recv # half-open connections (flood symptom)
ss -s                   # summary counts

# ── Watch your own interface ─────────────────────────────────
sudo tcpdump -ni eth0 'tcp[tcpflags] & tcp-syn != 0'   # SYN packets
sudo tcpdump -ni lo port 8080 -vv

# ── Read kernel settings (change only on your own lab host) ──
sysctl net.ipv4.tcp_syncookies
sysctl net.core.somaxconn
```

| Tool | Use |
|:---|:---|
| `ss` | Modern view of TCP/UDP state (replaces `netstat`) |
| `tcpdump` | Watch SYN / FIN / RST flags on your NIC |
| `sysctl` | Read or tune stack settings on a lab host |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - W. Richard Stevens, *UNIX Network Programming, Volume 1 (3rd Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 791 (IPv4), RFC 9293 (TCP), RFC 4987 (SYN flood / cookies)
> - `man ss`, `man tcpdump`, `man 7 ip`, `man 7 tcp`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs on systems you own, no flood PoCs or exploits.
