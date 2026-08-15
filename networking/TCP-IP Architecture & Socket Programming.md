# 🌐 TCP/IP Architecture & Socket Programming

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | TCP/IP Model | Model 4 Layer TCP/IP vs OSI | TCP/IP 4-Layer Architecture | TCP/IP 4層アーキテクチャ |
| 2 | TCP vs UDP | Karakteristik TCP & UDP | TCP vs UDP Deep Dive | TCPとUDPの詳細比較 |
| 3 | TCP 3-Way Handshake | Proses koneksi & terminasi | Connection & Teardown Lifecycle | 3ウェイハンドシェイクと切断手順 |
| 4 | TCP Flags & Header | Struktur header & 6 TCP flag | TCP Header Anatomy & Flags | TCPヘッダー構造とフラグ |
| 5 | Socket Programming | Konsep socket & API C/Python | Network Sockets & API Workflows | ソケット通信とプログラミング |
| 6 | Security Note | Serangan transport layer | Transport Layer Attack Vectors | トランスポート層の攻撃手法 |
| 7 | Cheatsheet | Referensi cepat & summary | Quick Reference Cheatsheet | クイックリファレンスと要約 |

---

## 1. 🏗️ TCP/IP Model — 4-Layer Network Architecture

### 🇮🇩 Bahasa Indonesia
**TCP/IP (Transmission Control Protocol / Internet Protocol)** adalah suite protokol komunikasi standar yang menjadi tulang punggung internet modern. Berbeda dengan model teoritis OSI 7 layer, TCP/IP menggunakan model praktis 4 layer:

1. **Application Layer (Layer 4)**: Menangani protokol aplikasi tingkat tinggi yang berinteraksi langsung dengan user (HTTP, HTTPS, SSH, DNS, FTP, SMTP). Menggabungkan fungsi Layer 5, 6, dan 7 pada model OSI.
2. **Transport Layer (Layer 3)**: Mengatur komunikasi *host-to-host*, keandalan data (*reliability*), kontrol aliran (*flow control*), dan multiplexing port (TCP, UDP, SCTP).
3. **Internet Layer (Layer 2)**: Bertanggung jawab atas pengalamatan logis, enkapsulasi paket, dan *routing* melintasi berbagai jaringan (IPv4, IPv6, ICMP, ARP).
4. **Network Access / Link Layer (Layer 1)**: Mengatur transmisi frame fisik pada media transmisi lokal dan pengalamatan perangkat keras MAC (Ethernet, Wi-Fi 802.11, PPP).

### 🇬🇧 English
The **TCP/IP (Transmission Control Protocol / Internet Protocol)** suite is the foundational communication framework powering the global Internet. While the OSI model is a 7-layer theoretical construct, TCP/IP organizes real-world protocols into a streamlined 4-layer stack:

1. **Application Layer (Layer 4)**: Hosts user-facing and high-level protocols (HTTP, HTTPS, SSH, DNS, FTP, SMTP). Merges OSI Layers 5 (Session), 6 (Presentation), and 7 (Application).
2. **Transport Layer (Layer 3)**: Delivers *host-to-host* communication, stream reliability, congestion management, and port multiplexing (TCP, UDP, SCTP).
3. **Internet Layer (Layer 2)**: Governs logical addressing, packet encapsulation, and path determination across heterogeneous networks (IPv4, IPv6, ICMP, ARP).
4. **Network Access / Link Layer (Layer 1)**: Translates IP datagrams into physical hardware frames (MAC addresses) across physical mediums (Ethernet, Wi-Fi 802.11, Fiber).

### 🇯🇵 日本語
**TCP/IP（Transmission Control Protocol / Internet Protocol）**は、インターネット全体を支える通信プロトコル群です。理論的なOSI 7層モデルに対し、TCP/IPは実用的な4層アーキテクチャを採用しています：

1. **アプリケーション層（Layer 4）**: ユーザーやアプリケーションが直接利用するプロトコル群（HTTP、HTTPS、SSH、DNS、FTP、SMTP）。OSIのセッション層・プレゼンテーション層・アプリケーション層を統合。
2. **トランスポート層（Layer 3）**: ホスト間通信、信頼性保証、フロー制御、ポートによる多重化を担当（TCP、UDP）。
3. **インターネット層（Layer 2）**: 論理IPアドレスの割り当て、パケットのカプセル化、およびネットワーク間のルーティングを担当（IPv4、IPv6、ICMP）。
4. **ネットワークアクセス層 / リンク層（Layer 1）**: 物理メディア上でのフレーム送受信およびMACアドレスによる通信を管理（Ethernet、Wi-Fi 802.11）。

```
┌─────────────────────────────────────────────────────────────┐
│                   TCP/IP 4-LAYER MODEL                      │
├───────────────────┬───────────────────────────┬─────────────┤
│ TCP/IP Layer      │ Protocols                 │ Data Unit   │
├───────────────────┼───────────────────────────┼─────────────┤
│ 4. Application    │ HTTP, HTTPS, SSH, DNS     │ Data        │
│ 3. Transport      │ TCP, UDP, SCTP            │ Segment     │
│ 2. Internet       │ IPv4, IPv6, ICMP, ARP     │ Packet      │
│ 1. Network Access │ Ethernet, 802.11 Wi-Fi    │ Frame / Bit │
└───────────────────┴───────────────────────────┴─────────────┘
```

---

## 2. ⚖️ TCP vs UDP — Transport Protocol Comparison

### 🇮🇩 Bahasa Indonesia
Dua protokol utama pada Transport Layer memiliki filosofi desain yang berlawanan:
- **TCP (Connection-Oriented)**: Menjamin bahwa data terkirim secara utuh, berurutan, dan tanpa duplikasi. Melakukan *handshake* sebelum transfer data, menggunakan *acknowledgment* (ACK), dan mekanisme retransmisi bila terjadi *packet loss*.
- **UDP (Connectionless)**: Mengirimkan datagram tanpa mendirikan koneksi terlebih dahulu (*fire-and-forget*). Mengorbankan keandalan demi latensi sangat rendah (*low latency*).

| Parameter | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|:---|:---|:---|
| **Koneksi** | Connection-Oriented (3-Way Handshake) | Connectionless (Langsung kirim) |
| **Keandalan (Reliability)** | Sangat Tinggi (ACK + Retransmisi Otomatis) | Tidak ada jaminan pengiriman (Best Effort) |
| **Urutan Data** | Terjamin (Sequence Number) | Tidak terjamin (bisa tiba acak) |
| **Header Size** | 20 – 60 Bytes | 8 Bytes (Sangat ringan) |
| **Flow & Congestion Control**| Ada (Sliding Window, AIMD, BBR) | Tidak ada |
| **Kecepatan & Overhead** | Lebih lambat, overhead lebih besar | Sangat cepat, overhead minimal |
| **Contoh Protokol** | HTTP/1.1, HTTPS, SSH, FTP, SMTP, BGP | DNS, DHCP, VoIP, TFTP, NTP, QUIC/HTTP3, Streaming |

---

## 3. 🤝 TCP 3-Way Handshake & Connection Teardown

### 🇮🇩 Bahasa Indonesia
Sebelum TCP dapat mentransfer data, client dan server harus melakukan **3-Way Handshake** untuk menyepakati nomor urut awal (*Initial Sequence Number / ISN*) dan mengonfirmasi kesiapan kedua pihak.

#### 1. Pembentukan Koneksi (3-Way Handshake)
1. **SYN (Synchronize)**: Client mengirim paket dengan flag `SYN=1` dan nomor urut acak `Seq = X` ke server.
2. **SYN-ACK (Synchronize-Acknowledge)**: Server menerima SYN, merespons dengan `SYN=1, ACK=1`, nomor urut server `Seq = Y`, dan `Ack = X + 1`.
3. **ACK (Acknowledge)**: Client mengirim konfirmasi balik `ACK=1`, `Seq = X + 1`, dan `Ack = Y + 1`. Koneksi resmi berstatus **ESTABLISHED**.

```
Client                                                  Server
  │                                                       │
  │─── 1. [SYN] Seq=X ───────────────────────────────────>│ (LISTEN -> SYN_RCVD)
  │                                                       │
  │<── 2. [SYN, ACK] Seq=Y, Ack=X+1 ─────────────────────│
  │                                                       │
  │─── 3. [ACK] Seq=X+1, Ack=Y+1 ────────────────────────>│ (ESTABLISHED)
  │                                                       │
  │═════════════════ DATA TRANSFER PHASE ═════════════════│
```

#### 2. Pemutusan Koneksi (4-Way Teardown)
1. **FIN**: Pihak yang ingin menutup mengirim paket `FIN=1` (`Seq = A`).
2. **ACK**: Pihak penerima merespons dengan `ACK=1` (`Ack = A + 1`).
3. **FIN**: Pihak kedua mengirim `FIN=1` (`Seq = B`) ketika siap menutup.
4. **ACK**: Pihak pertama mengonfirmasi dengan `ACK=1` (`Ack = B + 1`) dan memasuki state `TIME_WAIT`.

---

## 4. 🏷️ TCP Header Anatomy & Control Flags

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |        Urgent Pointer         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### 🚩 6 Core TCP Control Flags

| Flag | Name | Function / Deskripsi | Cybersecurity Context |
|:---|:---|:---|:---|
| **SYN** | Synchronize | Memulai koneksi & menyelaraskan sequence number | Target **SYN Flood DoS** & **Nmap SYN Scan (`-sS`)** |
| **ACK** | Acknowledgment | Mengonfirmasi penerimaan data / paket sebelumnya | Digunakan dalam **ACK Scan (`-sA`)** untuk memetakan aturan firewall |
| **FIN** | Finish | Menutup koneksi secara anggun (*graceful teardown*) | Digunakan dalam **FIN Scan (`-sF`)** untuk melewati filter paket |
| **RST** | Reset | Membatalkan/menolak koneksi secara instan | Port tertutup mengirim RST; digunakan dalam **TCP Reset Attack** |
| **PSH** | Push | Menginstruksikan buffer agar segera meneruskan data ke aplikasi | Manipulasi transfer data interaktif (SSH, Telnet, Shell) |
| **URG** | Urgent | Menandakan data pada segmen ini berstatus mendesak | Digunakan dalam **Xmas Scan (`-sX`)** (kombinasi FIN+PSH+URG) |

---

## 5. 💻 Socket Programming Fundamentals (Python & C)

### 🇮🇩 Bahasa Indonesia
**Network Socket** adalah titik akhir (*endpoint*) komunikasi dua arah antara dua program yang berjalan di jaringan. Socket diidentifikasi oleh kombinasi **IP Address + Port Number + Transport Protocol**.

### 🐍 Python TCP Server & Client Implementation

```python
# ── TCP SERVER (server.py) ──────────────────────────────────
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

# AF_INET = IPv4, SOCK_STREAM = TCP
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_sock.bind((SERVER_IP, SERVER_PORT))
server_sock.listen(5)
print(f"[*] Listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    client_sock, client_addr = server_sock.accept()
    print(f"[+] Accepted connection from {client_addr[0]}:{client_addr[1]}")
    
    data = client_sock.recv(1024)
    print(f"[>] Received: {data.decode('utf-8')}")
    
    response = b"ACK: Command received by server\n"
    client_sock.sendall(response)
    client_sock.close()
```

```python
# ── TCP CLIENT (client.py) ──────────────────────────────────
import socket

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9999

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((TARGET_IP, TARGET_PORT))

payload = "HELLO SERVER - EXECUTING RECON".encode("utf-8")
client_sock.sendall(payload)

reply = client_sock.recv(4096)
print(f"[<] Server response: {reply.decode('utf-8')}")
client_sock.close()
```

---

## 6. 🔐 Security Notes — Transport Layer Attack Vectors

### 1. SYN Flood DoS (Denial of Service)
Penyerang mengirim ribuan paket `SYN` dengan alamat IP palsu (*spoofed IP*) tanpa pernah mengirim paket `ACK` balasan. Akibatnya, memori buffer server (*SYN Backlog Queue*) penuh terisi status `SYN_RECV`, mencegah user sah melakukan koneksi.
- **Mitigasi**: Aktifkan **SYN Cookies** pada kernel Linux:
  ```bash
  sudo sysctl -w net.ipv4.tcp_syncookies=1
  ```

### 2. TCP Session Hijacking & Reset Attack
Jika penyerang berada pada jalur lalu lintas (*Man-in-the-Middle*) atau mampu memprediksi **Sequence Number** dengan tepat:
- Penyerang dapat menyuntikkan paket data jahat dengan nomor sequence yang sah.
- Penyerang dapat mengirim paket `RST` palsu untuk memutus komunikasi penting antar-server (misal: koneksi BGP router).

---

## 7. 🧠 Quick Reference Cheatsheet

```bash
# ── SOCKET & PORT MONITORING ─────────────────────────────────
ss -tulpn                      # List all listening TCP/UDP sockets with PIDs
netstat -ant                   # Check established and listening TCP connections
lsof -i :80                    # Find process bound to port 80

# ── PACKET DISSECTION & ANALYSIS ─────────────────────────────
sudo tcpdump -nn -i eth0 tcp port 80          # Capture HTTP TCP traffic
sudo tcpdump -nn 'tcp[tcpflags] & (tcp-syn) != 0' # Capture SYN packets only

# ── NETWORK UTILITIES ────────────────────────────────────────
nc -lvnp 4444                  # Netcat TCP listener (Reverse shell catcher)
nc -zv 192.168.1.1 20-100      # Simple TCP port banner grabbing
```

---

> 📚 **References & Book Sources:**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach (6th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - W. Richard Stevens — *UNIX Network Programming (Volume 1, 3rd Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Christian Benvenuti — *Understanding Linux Network Internals* (`~/Documents/Books/CyberSec/Networking/`)
> - William Stallings — *Network Security Essentials: Applications and Standards (4th Edition)* (`~/Documents/Books/CyberSec/Networking/`)
> - Justin Seitz & Tim Arnold — *Black Hat Python (2nd Edition)* (`~/Documents/Books/CyberSec/Programming/`)
> - `man socket`, `man 7 tcp`, `man 7 ip`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
