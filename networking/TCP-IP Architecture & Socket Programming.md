# 🧱 TCP/IP Architecture & Socket Programming

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Kurose & Ross — *Computer Networking*; Stevens — *UNIX Network Programming*; Benvenuti — *Understanding Linux Network Internals*; Stallings — *Network Security Essentials*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-039` | **Phase 2:** Networking  
> **Est. study:** 5-6h | **Level:** Intermediate  
> **Prerequisites:** LC-038  
> **Book map:** Kurose & Ross Â Computer Networking Ch.3-4; Stevens Â UNIX Network Programming Vol.1 Ch.1-6
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Layer Model | Model 4 lapisan | TCP/IP layers | 4層モデル |
| 2 | IPv4 Header | Field header IPv4 | Header fields | IPv4ヘッダ |
| 3 | TCP Overview | Segmen & field | Segment structure | TCPセグメント |
| 4 | State Machine | Mesin status TCP | TCP states | 状態遷移 |
| 5 | Handshake | Three-way handshake | Connection setup | 3ウェイ |
| 6 | Congestion | Intuisi cwnd | Congestion window | 輻輳窓 |
| 7 | Sockets | API C & Python | Socket overview | ソケットAPI |
| 8 | SYN Flood | Konsep & SYN cookies | DoS concept + defense | SYN洪水と防御 |
| 9 | Security Notes | Hardening stack | Defense notes | 防御ノート |
| 10 | Cheatsheet | ss / tcpdump / code | Admin & lab CLI | チートシート |

---

## 1. 📚 TCP/IP Four-Layer Model

### 🇮🇩 Bahasa Indonesia
Model Internet praktis (Kurose) sering digambarkan empat lapisan (dibanding tujuh OSI):

| Layer | Peran | Contoh |
|:---|:---|:---|
| **Application** | Semantik aplikasi | HTTP, DNS, SSH |
| **Transport** | Proses-to-proses | TCP, UDP, QUIC* |
| **Internet** | Host-to-host routing | IPv4, IPv6, ICMP |
| **Link / Network Access** | Hop lokal | Ethernet, Wi-Fi |

\*QUIC di UDP tetapi menyediakan reliability/security mirip transport modern.

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

**Encapsulation:** setiap lapisan menambah header (dan kadang trailer). Demultiplexing naik memakai EtherType, IP protocol, port numbers.

### 🇬🇧 English
Security controls exist at every layer (802.1X, IPsec, TLS, app auth). Defense in depth means not relying on a single layer’s assurances.

### 🇯🇵 日本語
各層に防御を置くのが防御深度です。TLSだけ、ファイアウォールだけに依存しないでください。

---

## 2. 📦 IPv4 Header — Core Fields

Header minimum 20 byte (tanpa options):

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

| Field | Makna keamanan / operasi |
|:---|:---|
| **Version** | 4 vs 6 |
| **IHL** | Panjang header; options jarang & sering difilter |
| **DSCP/ECN** | QoS / congestion notification |
| **Total Length** | Ukuran datagram |
| **ID / Flags / Offset** | Fragmentasi — risiko reassembly attack jika stack lemah (modern OS jauh lebih baik) |
| **TTL** | Hop limit; cegah loop; heuristik OS |
| **Protocol** | 6=TCP, 17=UDP, 1=ICMP, … |
| **Checksum** | Header only (IPv4) |
| **Src / Dst** | Addressing; src dapat di-spoof tanpa ingress filter |

$$
\mathsf{Payload\ size} = \mathsf{TotalLength} - 4\cdot\mathsf{IHL}
$$

---

## 3. 📮 TCP Segment — Essential Fields

TCP menyediakan **stream berorientasi koneksi**, reliability (ACK, retransmit), ordering, dan flow control.

| Field | Fungsi |
|:---|:---|
| Src / Dst **Port** | Demux ke socket |
| **Seq** | Byte offset stream pengirim |
| **Ack** | Next byte expected (jika ACK set) |
| **Data Offset** | Ukuran header TCP |
| Flags | SYN, ACK, FIN, RST, PSH, URG, ECE, CWR, … |
| **Window** | Flow control receiver |
| **Checksum** | Pseudo-header IP + TCP |
| Urgent / Options | SACK, Timestamp, MSS, Window Scale, …

Identitas koneksi 4-tuple (atau 5 dengan proto):

$$
(srcIP,\ srcPort,\ dstIP,\ dstPort)
$$

---

## 4. 🔄 TCP State Machine (Simplified)

### 🇮🇩 Bahasa Indonesia
Status utama (Stevens / diagram klasik):

```
  CLOSED ──passive open──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──active open───► SYN_SENT ──────────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT_1 ──► FIN_WAIT_2 ──► TIME_WAIT ──► CLOSED
  ESTABLISHED ──FIN──► CLOSE_WAIT ──► LAST_ACK ──► CLOSED
```

| State | Arti singkat |
|:---|:---|
| LISTEN | Menunggu SYN |
| SYN_SENT / SYN_RCVD | Handshake setengah jalan |
| ESTABLISHED | Data transfer |
| TIME_WAIT | Menunggu 2×MSL agar segmen lama mati |
| CLOSE_WAIT | Peer sudah FIN; aplikasi harus close |

`ss -tan` menampilkan state pada host Linux Anda — berguna untuk diagnose leak koneksi atau flood.

### 🇬🇧 English
`TIME_WAIT` is often mistaken for a bug; it is a correctness feature. Tuning requires understanding of MSL and whether you are client or server heavy.

### 日本語
`TIME_WAIT`は仕様上の保護です。安易に無効化しないでください。

---

## 5. 🤝 Three-Way Handshake

### 🇮🇩 Bahasa Indonesia
Pembukaan koneksi:

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

Kedua sisi menyepakati initial sequence numbers (ISN). ISN modern diperkuat (bukan counter naif) untuk mengurangi spoofing prediktif.

**Teardown:** FIN/ACK empat arah tipikal, atau RST untuk abort.

### 🇬🇧 English
Middleboxes and load balancers must handle handshake state carefully; asymmetry and SYN timeouts interact with DoS defenses such as SYN cookies.

### 🇯🇵 日本語
ロードバランサやファイアウォールも握手状態を正しく扱う必要があります。

---

## 6. 📉 Congestion Control — Window Intuition

### 🇮🇩 Bahasa Indonesia
**Flow control:** `rwnd` dari receiver (field Window, diskalakan).  
**Congestion control:** pengirim membatasi diri dengan **cwnd** (congestion window) agar tidak merusak jalur bersama.

Bytes in flight (intuisi):

$$
\mathsf{in\_flight} \le \min(\mathsf{cwnd},\, \mathsf{rwnd})
$$

Fase klasik (Reno-style intuition; implementasi modern: CUBIC, BBR, …):

| Fase | Perilaku |
|:---|:---|
| Slow start | `cwnd` tumbuh eksponensial per RTT hingga ssthresh |
| Congestion avoidance | Pertumbuhan lebih linear |
| Loss signal | Triple-dup ACK / RTO ⇒ turunkan `cwnd`, sesuaikan ssthresh |

$$
\text{slow start (approx):}\quad \mathsf{cwnd} \leftarrow \mathsf{cwnd} + \mathsf{MSS}\ \text{per ACK}
$$

Keamanan terkait: flood UDP/TCP dapat menyebabkan **congestive DoS**; rate-limit dan capacity planning adalah kontrol operasional.

### 🇬🇧 English
You rarely tune `cwnd` by hand; you observe RTT, retransmission rate, and bufferbloat. BBR models bottleneck bandwidth and RTT rather than only loss.

### 日本語
損失ベースとBBRなどモデルベースの違いを理解すると性能障害の切り分けが楽になります。

---

## 7. 🔌 Socket API Overview — C & Python

### 🇮🇩 Bahasa Indonesia
**Socket** adalah abstraksi endpoint (Stevens). Pola server TCP:

1. `socket` → 2. `bind` → 3. `listen` → 4. `accept` loop → 5. `recv`/`send` → 6. `close`

Pola client: `socket` → `connect` → `send`/`recv` → `close`.

#### C (sketsa)
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

#### Python 3
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

| Call | Makna |
|:---|:---|
| `bind` | Kaitkan alamat/port lokal |
| `listen` | Antrian SYN/backlog |
| `accept` | Ambil koneksi established |
| `connect` | Active open |
| `SO_REUSEADDR` | Izinkan rebind cepat (pahami TIME_WAIT) |

UDP: `SOCK_DGRAM`, `sendto`/`recvfrom`, tanpa handshake.

### 🇬🇧 English
Always define byte order (`htons`/`inet_pton`), handle partial `send`, and treat the network as hostile: validate inputs, set timeouts, prefer TLS wrappers (`ssl` module / OpenSSL) for sensitive apps.

### 日本語
タイムアウト、入力検証、部分送信、TLS化がソケットプログラミングの基本衛生です。

---

## 8. 🌊 SYN Flood — Concept & SYN Cookies

### 🇮🇩 Bahasa Indonesia
**Konsep:** penyerang mengirim banyak segmen **SYN** (sering spoofed) agar server mengalokasikan **half-open state** (SYN_RCVD) hingga tabel/backlog habis ⇒ klien sah gagal connect (**DoS**).

$$
\#\{\mathsf{SYN\_RCVD}\} \uparrow\ \Rightarrow\ \mathsf{resource\ exhaustion}
$$

**SYN cookies (pertahanan):** server **tidak** menyimpan TCB penuh pada SYN; ISN dikodekan dengan hash rahasia atas 4-tuple + timestamp/MSS bits. Hanya ketika ACK final membawa cookie valid, state dibuat.

$$
\mathsf{ISN}_s \approx \mathsf{Hash}_{k}(addrs, ports,\; t) \;+\; \mathsf{encode}(\mathsf{MSS})
$$

(Implementasi kernel bervariasi; intuisi sama.)

Kontrol lain: `tcp_syncookies`, backlog wajar, SYN rate-limit / SYN proxy di load balancer, anycast scrubbing untuk layanan publik.

> Tidak ada PoC flood atau tool command ofensif di catatan ini.

### 🇬🇧 English
Enable and monitor SYN-cookie / SYN-proxy metrics on Internet-facing VIPs. Combine with connection limits per source prefix where appropriate.

### 日本語
インターネット公開VIPではSYN cookieやレート制限のメトリクスを監視します。

---

## 9. 🔐 Security Notes — Stack Hardening

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| SYN flood | Habiskan half-open | SYN cookies, rate-limit, capacity |
| Spoofed src | Reflection / syn abuse | BCP38 / uRPF |
| RST injection | Putus sesi (jika seq tebak) | Encrypted transport; modern ISN |
| Cleartext TCP apps | Sniff / MITM | TLS 1.3 |
| Open bind `0.0.0.0` | Ekspos tak sengaja | Bind internal; firewall |
| Large backlog | Memory pressure | Tune + monitoring `ss` |
| Fragment tricks | Evasion IDS (legacy) | Normalize; modern stack defaults |

**Lab hygiene:** eksperimen handshake & socket hanya pada host/VM milik Anda; pantau dengan `ss` dan `tcpdump` defensif.

---

## 10. 🧠 Cheatsheet — Admin, Observe, Minimal Lab Code

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

| Alat | Kegunaan |
|:---|:---|
| `ss` | State TCP/UDP modern (ganti `netstat`) |
| `tcpdump` | Observasi flag SYN/FIN/RST |
| `sysctl` | Parameter stack di host lab |

---

> 📚 **References & Book Sources**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach* — `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - W. Richard Stevens — *UNIX Network Programming, Volume 1 (3rd Edition)* — `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - Christian Benvenuti — *Understanding Linux Network Internals* — `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings — *Network Security Essentials (4th Edition)* — `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - RFC 791 (IPv4), RFC 9293 (TCP), RFC 4987 (SYN cookies overview literature)
> - `man ss`, `man tcpdump`, `man 7 ip`, `man 7 tcp`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & lab pada sistem milik sendiri — tanpa PoC flood atau exploit.
