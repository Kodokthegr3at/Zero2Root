# Arsitektur TCP/IP & Pemrograman Socket

> **LearnCybersecurity** | Seri Networking Fundamentals
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stevens, *UNIX Network Programming*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-039` | **Fase 2:** Networking
> **Estimasi belajar:** 5-6 jam | **Level:** Intermediate
> **Prasyarat:** LC-038
> **Peta buku:** Kurose & Ross, Computer Networking Ch.3-4; Stevens, UNIX Network Programming Vol.1 Ch.1-6
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Model 4 lapisan TCP/IP
2. Header IPv4: field inti
3. Segmen TCP: field esensial
4. Mesin status TCP (disederhanakan)
5. Three-way handshake
6. Congestion control: intuisi window
7. Overview Socket API: C & Python
8. SYN flood: konsep & SYN cookies
9. Catatan keamanan: hardening stack
10. Cheatsheet

---

## 1. Model 4 lapisan TCP/IP

Model Internet praktis (Kurose) sering digambarkan sebagai empat lapisan, dibandingkan tujuh lapisan OSI:

| Layer | Peran | Contoh |
|:---|:---|:---|
| Application | Semantik aplikasi | HTTP, DNS, SSH |
| Transport | Proses-ke-proses | TCP, UDP, QUIC* |
| Internet | Routing host-ke-host | IPv4, IPv6, ICMP |
| Link / Network Access | Hop lokal | Ethernet, Wi-Fi |

*QUIC berjalan di atas UDP tetapi menyediakan reliability/security mirip transport modern.

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

Enkapsulasi: setiap lapisan menambahkan header (dan kadang trailer). Demultiplexing naik memakai EtherType, IP protocol, dan port number.

Kontrol keamanan ada di setiap layer (802.1X, IPsec, TLS, autentikasi aplikasi). Defense in depth berarti tidak bergantung pada jaminan satu layer saja.

---

## 2. Header IPv4: field inti

Header minimum berukuran 20 byte (tanpa options):

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

| Field | Makna keamanan / operasional |
|:---|:---|
| Version | 4 vs 6 |
| IHL | Panjang header; options jarang dipakai dan sering difilter |
| DSCP/ECN | QoS / notifikasi kongesti |
| Total Length | Ukuran datagram |
| ID / Flags / Offset | Fragmentasi, berisiko terhadap serangan reassembly jika stack lemah (OS modern jauh lebih tahan) |
| TTL | Hop limit; mencegah loop; dipakai sebagai heuristik OS |
| Protocol | 6=TCP, 17=UDP, 1=ICMP, dan seterusnya |
| Checksum | Hanya untuk header (IPv4) |
| Src / Dst | Pengalamatan; src dapat di-spoof jika tidak ada ingress filter |

```text
ukuran header  = IHL × 4 byte
ukuran payload = Total Length - ukuran header

Contoh: Total Length = 60, IHL = 5  →  header = 20 byte  →  payload = 40 byte
```

---

## 3. Segmen TCP: field esensial

TCP menyediakan stream berorientasi koneksi, reliability (ACK, retransmit), ordering, dan flow control.

| Field | Fungsi |
|:---|:---|
| Src / Dst Port | Demultiplexing ke socket |
| Seq | Byte offset stream pengirim |
| Ack | Byte berikutnya yang diharapkan (jika flag ACK diset) |
| Data Offset | Ukuran header TCP |
| Flags | SYN, ACK, FIN, RST, PSH, URG, ECE, CWR, dan seterusnya |
| Window | Flow control dari sisi receiver |
| Checksum | Menghitung pseudo-header IP + TCP |
| Urgent / Options | SACK, Timestamp, MSS, Window Scale, dan seterusnya |

Identitas koneksi berupa 4-tuple (atau 5-tuple jika protokol disertakan):

```text
(IP sumber, port sumber, IP tujuan, port tujuan)
```

---

## 4. Mesin status TCP (disederhanakan)

Status utama (mengikuti Stevens / diagram klasik):

```
  CLOSED ──passive open──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──active open───► SYN_SENT ──────────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT_1 ──► FIN_WAIT_2 ──► TIME_WAIT ──► CLOSED
  ESTABLISHED ──FIN──► CLOSE_WAIT ──► LAST_ACK ──► CLOSED
```

| State | Arti singkat |
|:---|:---|
| LISTEN | Menunggu SYN |
| SYN_SENT / SYN_RCVD | Handshake baru separuh jalan |
| ESTABLISHED | Transfer data berlangsung |
| TIME_WAIT | Menunggu 2×MSL agar segmen lama benar-benar mati |
| CLOSE_WAIT | Peer sudah mengirim FIN; aplikasi lokal harus close |

`ss -tan` menampilkan state pada host Linux Anda, berguna untuk mendiagnosis kebocoran koneksi atau flood.

`TIME_WAIT` sering dikira bug, padahal ini fitur untuk menjaga korektnes protokol. Melakukan tuning membutuhkan pemahaman soal MSL dan apakah sistem Anda lebih berat sebagai client atau server. Jangan menonaktifkannya begitu saja tanpa memahami konsekuensinya.

---

## 5. Three-way handshake

Pembukaan koneksi:

```text
1. C → S:  SYN,      seq=x
2. S → C:  SYN+ACK,  seq=y, ack=x+1
3. C → S:  ACK,      ack=y+1
```

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

Kedua sisi menyepakati initial sequence number (ISN) masing-masing. ISN modern dibuat dengan cara yang diperkuat, bukan sekadar counter naif, untuk mengurangi risiko spoofing yang bisa diprediksi.

Teardown: umumnya FIN/ACK empat arah, atau RST untuk abort paksa.

Middlebox dan load balancer harus menangani state handshake dengan hati-hati. Asimetri jalur dan SYN timeout saling berinteraksi dengan mekanisme pertahanan DoS seperti SYN cookies.

---

## 6. Congestion control: intuisi window

Flow control: `rwnd` berasal dari receiver (field Window, yang diskalakan).
Congestion control: pengirim membatasi diri sendiri dengan cwnd (congestion window) agar tidak merusak jalur bersama dengan trafik lain.

Bytes in flight (intuisi):

```text
byte in flight ≤ nilai terkecil antara cwnd dan rwnd
```

Pengirim dibatasi oleh batas yang lebih kecil: kemampuan jaringan (cwnd) atau kemampuan penerima (rwnd).

Fase klasik (intuisi ala Reno; implementasi modern memakai CUBIC, BBR, dan lainnya):

| Fase | Perilaku |
|:---|:---|
| Slow start | `cwnd` tumbuh eksponensial per RTT hingga mencapai ssthresh |
| Congestion avoidance | Pertumbuhan menjadi lebih linear |
| Sinyal loss | Triple-dup ACK / RTO menyebabkan `cwnd` diturunkan dan ssthresh disesuaikan |

```text
slow start: cwnd bertambah satu MSS untuk setiap ACK yang diterima
            (jadi kira-kira berlipat dua setiap round trip)
```

Keterkaitan dengan keamanan: flood UDP/TCP dapat menyebabkan congestive DoS; rate-limit dan capacity planning adalah kontrol operasional untuk itu.

Tuning `cwnd` secara manual jarang dilakukan; yang biasa diamati adalah RTT, tingkat retransmisi, dan bufferbloat. BBR memodelkan bottleneck bandwidth dan RTT, bukan hanya bereaksi terhadap loss seperti algoritma lama.

---

## 7. Overview Socket API: C & Python

Socket adalah abstraksi endpoint komunikasi (istilah Stevens). Pola server TCP:

1. `socket` → 2. `bind` → 3. `listen` → 4. loop `accept` → 5. `recv`/`send` → 6. `close`

Pola client: `socket` → `connect` → `send`/`recv` → `close`.

### C (sketsa)

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

| Call | Makna |
|:---|:---|
| `bind` | Mengaitkan alamat/port lokal |
| `listen` | Antrian SYN / backlog |
| `accept` | Mengambil koneksi yang sudah established |
| `connect` | Active open |
| `SO_REUSEADDR` | Mengizinkan rebind cepat (perlu paham implikasi TIME_WAIT) |

UDP memakai `SOCK_DGRAM`, dengan `sendto`/`recvfrom`, tanpa handshake.

Selalu tentukan byte order dengan jelas (`htons`/`inet_pton`), tangani kemungkinan `send` parsial, dan perlakukan jaringan sebagai lingkungan yang tidak dapat dipercaya: validasi input, set timeout, dan gunakan pembungkus TLS (modul `ssl` / OpenSSL) untuk aplikasi yang sensitif.

---

## 8. SYN flood: konsep & SYN cookies

Konsep: penyerang mengirim banyak segmen SYN (sering di-spoof) agar server mengalokasikan half-open state (SYN_RCVD) sampai tabel atau backlog-nya habis, sehingga client yang sah gagal connect. Ini adalah bentuk DoS.

Makin banyak koneksi setengah terbuka yang menumpuk, makin dekat server kehabisan sumber daya.

SYN cookies (pertahanan): server tidak menyimpan TCB penuh saat menerima SYN. ISN dikodekan dengan hash rahasia dari 4-tuple ditambah bit timestamp/MSS. State baru dibuat hanya ketika ACK final membawa cookie yang valid.

```text
ISN ≈ Hash(secret, addresses, ports, time) + MSS bits
```

(Implementasi di level kernel bervariasi, tetapi intuisinya sama.)

Kontrol lain yang relevan: `tcp_syncookies`, backlog yang wajar, rate-limit SYN atau SYN proxy di load balancer, serta anycast scrubbing untuk layanan publik.

Catatan: tidak ada PoC flood atau perintah tool ofensif di catatan ini.

Untuk VIP yang menghadap Internet, aktifkan dan pantau metrik SYN cookie / SYN proxy. Kombinasikan dengan connection limit per prefix sumber bila relevan.

---

## 9. Catatan keamanan: hardening stack

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| SYN flood | Menghabiskan slot half-open | SYN cookies, rate-limit, capacity planning |
| Src yang di-spoof | Reflection / penyalahgunaan SYN | BCP38 / uRPF |
| Injeksi RST | Memutus sesi (jika sequence bisa ditebak) | Transport terenkripsi; ISN modern |
| Aplikasi TCP cleartext | Sniffing / MITM | TLS 1.3 |
| Bind terbuka ke `0.0.0.0` | Eksposur tidak sengaja | Bind ke interface internal; firewall |
| Backlog terlalu besar | Tekanan memori | Tuning plus monitoring lewat `ss` |
| Trik fragmentasi | Evasi IDS (pada stack lama) | Normalisasi; default stack modern sudah lebih baik |

Kebersihan lab: eksperimen handshake dan socket hanya pada host/VM milik Anda sendiri; pantau dengan `ss` dan `tcpdump` secara defensif.

---

## 10. Cheatsheet: admin, observasi, kode lab minimal

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
| `ss` | State TCP/UDP modern (pengganti `netstat`) |
| `tcpdump` | Observasi flag SYN/FIN/RST |
| `sysctl` | Parameter stack pada host lab |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - W. Richard Stevens, *UNIX Network Programming, Volume 1 (3rd Edition)*, `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - RFC 791 (IPv4), RFC 9293 (TCP), RFC 4987 (tinjauan literatur SYN cookies)
> - `man ss`, `man tcpdump`, `man 7 ip`, `man 7 tcp`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Edukasi dan lab pada sistem milik sendiri, tanpa PoC flood atau exploit.
