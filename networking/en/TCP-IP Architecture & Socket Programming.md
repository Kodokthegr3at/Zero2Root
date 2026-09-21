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

1. TCP/IP four-layer model
2. IPv4 header: core fields
3. TCP segment: essential fields
4. TCP state machine (simplified)
5. Three-way handshake
6. Congestion control: window intuition
7. Socket API overview: C & Python
8. SYN flood: concept & SYN cookies
9. Security notes: stack hardening
10. Cheatsheet

---

## 1. TCP/IP four-layer model

The practical Internet model (Kurose) is often described as four layers, compared to OSI's seven:

| Layer | Role | Examples |
|:---|:---|:---|
| Application | Application semantics | HTTP, DNS, SSH |
| Transport | Process-to-process | TCP, UDP, QUIC* |
| Internet | Host-to-host routing | IPv4, IPv6, ICMP |
| Link / Network Access | Local hop | Ethernet, Wi-Fi |

*QUIC runs over UDP but provides reliability/security similar to a modern transport protocol.

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
         encapsulation ↓
  [Eth][IP][TCP][App data][FCS]
```

Encapsulation: each layer adds a header (and sometimes a trailer). Demultiplexing on the way up uses the EtherType, the IP protocol field, and port numbers.

Security controls exist at every layer (802.1X, IPsec, TLS, application auth). Defense in depth means not relying on a single layer's assurances.

---

## 2. IPv4 header: core fields

Minimum header size is 20 bytes (without options):

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
|                    Options (if IHL > 5) …                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Field | Security / operational meaning |
|:---|:---|
| Version | 4 vs 6 |
| IHL | Header length; options are rare and often filtered |
| DSCP/ECN | QoS / congestion notification |
| Total Length | Datagram size |
| ID / Flags / Offset | Fragmentation; a risk for reassembly attacks on weak stacks (modern OSes are far more resilient) |
| TTL | Hop limit; prevents loops; used as an OS heuristic |
| Protocol | 6=TCP, 17=UDP, 1=ICMP, and so on |
| Checksum | Header only (IPv4) |
| Src / Dst | Addressing; the source can be spoofed without ingress filtering |

$$
\mathsf{Payload\ size} = \mathsf{TotalLength} - 4\cdot\mathsf{IHL}
$$

---

## 3. TCP segment: essential fields

TCP provides a connection-oriented byte stream, reliability (ACK, retransmit), ordering, and flow control.

| Field | Function |
|:---|:---|
| Src / Dst Port | Demux to a socket |
| Seq | Byte offset of the sender's stream |
| Ack | Next expected byte (when the ACK flag is set) |
| Data Offset | Size of the TCP header |
| Flags | SYN, ACK, FIN, RST, PSH, URG, ECE, CWR, and so on |
| Window | Receiver's flow control |
| Checksum | Covers the IP + TCP pseudo-header |
| Urgent / Options | SACK, Timestamp, MSS, Window Scale, and so on |

The connection identity is a 4-tuple (or a 5-tuple if the protocol is included):

$$
(srcIP,\ srcPort,\ dstIP,\ dstPort)
$$

---

## 4. TCP state machine (simplified)

Main states (following Stevens / the classic diagram):

```
  CLOSED ──passive open──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──active open───► SYN_SENT ──────────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT_1 ──► FIN_WAIT_2 ──► TIME_WAIT ──► CLOSED
  ESTABLISHED ──FIN──► CLOSE_WAIT ──► LAST_ACK ──► CLOSED
```

| State | Short meaning |
|:---|:---|
| LISTEN | Waiting for a SYN |
| SYN_SENT / SYN_RCVD | Handshake halfway through |
| ESTABLISHED | Data transfer in progress |
| TIME_WAIT | Waiting 2xMSL so old segments truly die out |
| CLOSE_WAIT | Peer has sent FIN; the local application must close |

`ss -tan` shows state on your own Linux host, useful for diagnosing a connection leak or a flood.

`TIME_WAIT` is often mistaken for a bug; it is a correctness feature. Tuning it requires understanding MSL and whether your system is client-heavy or server-heavy. Do not disable it without understanding the consequences.

---

## 5. Three-way handshake

Connection setup:

$$
\begin{aligned}
1&\colon\ \mathsf{C \to S}:\ \mathsf{SYN},\ seq=x \\
2&\colon\ \mathsf{S \to C}:\ \mathsf{SYN\text{+}ACK},\ seq=y,\ ack=x+1 \\
3&\colon\ \mathsf{C \to S}:\ \mathsf{ACK},\ ack=y+1
\end{aligned}
$$

```
  Client                     Server
    │  SYN, seq=x               │
    │──────────────────────────►│
    │  SYN+ACK, seq=y, ack=x+1  │
    │◄──────────────────────────│
    │  ACK, ack=y+1             │
    │──────────────────────────►│
    │      ESTABLISHED          │
```

Both sides agree on their own initial sequence numbers (ISN). Modern ISNs are generated in a hardened way rather than as a naive counter, to reduce the risk of predictable spoofing.

Teardown: typically a four-way FIN/ACK exchange, or a RST for an abrupt abort.

Middleboxes and load balancers need to handle handshake state carefully. Path asymmetry and SYN timeouts interact with DoS defenses such as SYN cookies.

---

## 6. Congestion control: window intuition

Flow control: `rwnd` comes from the receiver (the Window field, scaled).
Congestion control: the sender limits itself with cwnd (congestion window) so it does not overload a shared path.

Bytes in flight (intuition):

$$
\mathsf{in\_flight} \le \min(\mathsf{cwnd},\, \mathsf{rwnd})
$$

Classic phases (Reno-style intuition; modern implementations use CUBIC, BBR, and others):

| Phase | Behavior |
|:---|:---|
| Slow start | `cwnd` grows exponentially per RTT up to ssthresh |
| Congestion avoidance | Growth becomes closer to linear |
| Loss signal | Triple-dup ACK / RTO causes `cwnd` to drop and ssthresh to adjust |

$$
\text{slow start (approx.):}\quad \mathsf{cwnd} \leftarrow \mathsf{cwnd} + \mathsf{MSS}\ \text{per ACK}
$$

Security relevance: UDP/TCP floods can cause congestive DoS; rate limiting and capacity planning are the operational controls for it.

You rarely tune `cwnd` by hand; what you observe is RTT, retransmission rate, and bufferbloat. BBR models bottleneck bandwidth and RTT rather than only reacting to loss the way older algorithms do.

---

## 7. Socket API overview: C & Python

A socket is an abstraction of a communication endpoint (Stevens's term). TCP server pattern:

1. `socket` → 2. `bind` → 3. `listen` → 4. `accept` loop → 5. `recv`/`send` → 6. `close`

Client pattern: `socket` → `connect` → `send`/`recv` → `close`.

### C (sketch)

```c
int s = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr = {0};
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = htonl(INADDR_ANY);
bind(s, (struct sockaddr*)&addr, sizeof addr);
listen(s, 128);
int c = accept(s, NULL, NULL);
/* read/write on c */
close(c); close(s);
```

### Python 3

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))
    s.listen(128)
    conn, peer = s.accept()
    with conn:
        data = conn.recv(4096)
        conn.sendall(b"OK\n")
```

| Call | Meaning |
|:---|:---|
| `bind` | Attach a local address/port |
| `listen` | SYN queue / backlog |
| `accept` | Pull an established connection off the queue |
| `connect` | Active open |
| `SO_REUSEADDR` | Allow a fast rebind (understand the TIME_WAIT implications) |

UDP uses `SOCK_DGRAM`, with `sendto`/`recvfrom`, and no handshake.

Always define byte order explicitly (`htons`/`inet_pton`), handle a partial `send`, and treat the network as hostile: validate inputs, set timeouts, and prefer a TLS wrapper (the `ssl` module / OpenSSL) for sensitive applications.

---

## 8. SYN flood: concept & SYN cookies

Concept: an attacker sends many SYN segments (often spoofed) so the server allocates half-open state (SYN_RCVD) until its table or backlog fills up, causing legitimate clients to fail to connect. This is a form of DoS.

$$
\#\{\mathsf{SYN\_RCVD}\} \uparrow\ \Rightarrow\ \mathsf{resource\ exhaustion}
$$

SYN cookies (defense): the server does not store a full TCB on receiving a SYN. The ISN is encoded with a secret hash over the 4-tuple plus timestamp/MSS bits. State is only created once the final ACK carries a valid cookie.

$$
\mathsf{ISN}_s \approx \mathsf{Hash}_{k}(addrs, ports,\; t) \;+\; \mathsf{encode}(\mathsf{MSS})
$$

(Kernel implementations vary, but the intuition is the same.)

Other relevant controls: `tcp_syncookies`, a reasonable backlog, SYN rate limiting or a SYN proxy at the load balancer, and anycast scrubbing for public services.

Note: no flood PoC or offensive tool commands are included in this note.

For Internet-facing VIPs, enable and monitor SYN-cookie / SYN-proxy metrics. Combine with connection limits per source prefix where appropriate.

---

## 9. Security notes: stack hardening

| Issue | Risk | Defense |
|:---|:---|:---|
| SYN flood | Exhausts half-open slots | SYN cookies, rate limiting, capacity planning |
| Spoofed source | Reflection / SYN abuse | BCP38 / uRPF |
| RST injection | Tears down a session (if sequence is guessable) | Encrypted transport; modern ISN generation |
| Cleartext TCP apps | Sniffing / MITM | TLS 1.3 |
| Open bind to `0.0.0.0` | Unintentional exposure | Bind to an internal interface; firewall |
| Oversized backlog | Memory pressure | Tune it and monitor with `ss` |
| Fragmentation tricks | IDS evasion (on legacy stacks) | Normalization; modern stack defaults already handle this |

Lab hygiene: experiment with handshakes and sockets only on hosts/VMs you own; monitor defensively with `ss` and `tcpdump`.

---

## 10. Cheatsheet: admin, observation, minimal lab code

```bash
# ── Connection tables ────────────────────────────────────────
ss -tan
ss -tanp state syn-recv
ss -s
ip -s link

# ── Capture YOUR interface traffic (troubleshooting) ─────────
sudo tcpdump -ni eth0 'tcp[tcpflags] & (tcp-syn) != 0'
sudo tcpdump -ni lo port 8080 -vv

# ── Kernel knobs (read; change only on lab hosts you own) ────
sysctl net.ipv4.tcp_syncookies
sysctl net.core.somaxconn
sysctl net.ipv4.tcp_max_syn_backlog

# ── Quick local listener / client (Python) ───────────────────
python3 - <<'PY'
import socket, threading
def serve():
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 8080)); s.listen(1)
        c,_=s.accept(); print(c.recv(64)); c.close()
threading.Thread(target=serve, daemon=True).start()
with socket.create_connection(("127.0.0.1", 8080)) as c:
    c.sendall(b"hello"); print("sent")
PY
```

| Tool | Use |
|:---|:---|
| `ss` | Modern TCP/UDP state (replaces `netstat`) |
| `tcpdump` | Observe SYN/FIN/RST flags |
| `sysctl` | Stack parameters on a lab host |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - W. Richard Stevens, *UNIX Network Programming, Volume 1 (3rd Edition)*, `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - RFC 791 (IPv4), RFC 9293 (TCP), RFC 4987 (SYN cookies overview literature)
> - `man ss`, `man tcpdump`, `man 7 ip`, `man 7 tcp`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs on systems you own, no flood PoCs or exploits.
