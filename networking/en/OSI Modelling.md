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

1. Overview: what is the OSI model
2. Layer 1: Physical
3. Layer 2: Data Link
4. Layer 3: Network
5. Layer 4: Transport
6. Layer 5: Session
7. Layer 6: Presentation
8. Layer 7: Application
9. Data encapsulation
10. TCP vs UDP comparison
11. Common ports
12. Protocols per layer
13. Network devices per layer
14. Security notes: attacks per layer
15. Practical workflow: network recon & analysis

---

## 1. Overview: what is the OSI model

The OSI Model (Open Systems Interconnection Model) is a standardized conceptual framework that defines how network communication systems work, divided into 7 layers. It was developed by the ISO (International Organization for Standardization) in 1984.

Each layer has specific responsibilities and only communicates with the layers directly above and below it. The model is referential: real implementations typically use the TCP/IP model (4 layers), but OSI remains the standard for understanding, troubleshooting, and network analysis.

Why it matters for cybersecurity:

- Understanding at which layer an attack occurs helps with attack vector identification.
- Understanding data encapsulation supports packet analysis and network forensics.
- Knowing the protocols at each layer informs firewall and IDS/IPS configuration.
- Understanding network devices supports network pentesting and reconnaissance.
- Analyzing abnormal traffic supports threat hunting and incident response.

### OSI model, visual overview

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

Mnemonic to remember the layers (top to bottom):
  "All People Seem To Need Data Processing"
```

---

## 2. Layer 1: Physical

The Physical Layer is the lowest layer in the OSI model. It handles transmission of raw bits (0s and 1s) across physical media. This layer does not care about the meaning of the data, it just moves electrical, optical, or radio signals from one point to another.

Key components:

- Cables (Ethernet, fiber optic, coaxial)
- Electrical, light, or radio wave signals
- Physical connectors and ports (RJ45, SFP, BNC)
- Repeater and hub devices

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

| Media | Speed | Max distance |
|-------|-------|---------------|
| Cat5e UTP | 1 Gbps | 100 meters |
| Cat6 UTP | 10 Gbps | 55 meters |
| Fiber single-mode | 100 Gbps+ | 40 to 80 km |
| Fiber multi-mode | 10 Gbps | 550 meters |
| Wi-Fi 6 (802.11ax) | 9.6 Gbps | ~100 meters |

---

## 3. Layer 2: Data Link

The Data Link Layer handles reliable data transfer between two directly connected nodes within the same network segment. It uses MAC addresses (Media Access Control) to identify devices and manages access to the physical media.

This layer is divided into two sub-layers:

- LLC (Logical Link Control): flow control and error checking
- MAC (Media Access Control): physical addressing and media access

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

| Protocol | Function | Pentest relevance |
|----------|----------|--------------------|
| ARP | IP to MAC resolution | Critical (ARP spoofing) |
| Ethernet II | Standard LAN frame | Medium |
| 802.1Q | VLAN tagging | High (VLAN hopping) |
| STP (802.1D) | Prevent network loops | High (STP attack) |
| PPP | Point-to-point link | Low |

---

## 4. Layer 3: Network

The Network Layer handles routing and logical addressing (IP addresses). It determines the best path to deliver data packets from source to destination across multiple different networks. The primary device at this layer is the router.

The data unit at this layer is called a packet.

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

| Protocol | Function | Pentest relevance |
|----------|----------|--------------------|
| IPv4 | 32-bit addressing | High |
| IPv6 | 128-bit addressing | High |
| ICMP | Control & error messages | High (ICMP flood) |
| OSPF | Dynamic routing protocol | Medium |
| BGP | Inter-AS routing | High (BGP hijack) |
| IPSec | IP encryption & auth | Low |

---

## 5. Layer 4: Transport

The Transport Layer handles end-to-end communication between applications on different hosts. It uses port numbers to identify communicating services/applications, and provides flow control, error recovery, and data segmentation.

Two main protocols:

- TCP (Transmission Control Protocol): connection-oriented, reliable, ordered
- UDP (User Datagram Protocol): connectionless, fast, no delivery guarantee

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

### TCP vs UDP comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed, uses ACK | No guarantee, fire and forget |
| Ordering | Ordered delivery | Out-of-order possible |
| Speed | Slower (overhead) | Faster |
| Use cases | HTTP, SSH, FTP, Email | DNS, DHCP, VoIP, video streaming |

### TCP 3-way handshake

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

## 6. Layer 5: Session

The Session Layer handles establishing, managing, and terminating communication sessions between applications. It ensures that if a connection is interrupted, the session can resume from the right point (checkpointing). It also controls dialog control (half-duplex vs full-duplex).

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

| Protocol | Function | Pentest relevance |
|----------|----------|--------------------|
| NetBIOS | Windows naming service | High |
| RPC | Remote procedure calls | High |
| SMB | Windows file sharing | Critical |
| SQL*Net | Oracle DB sessions | Medium |
| iSCSI | Storage over network | Medium |

---

## 7. Layer 6: Presentation

The Presentation Layer is the "translator" of the network. It handles data formatting, encryption/decryption, and compression. This layer ensures that data sent by one application can be read by another even if their internal formats differ.

Main responsibilities:

- Encoding/decoding: ASCII, Unicode, EBCDIC
- Encryption/decryption: SSL/TLS operates here
- Compression/decompression: gzip, zlib

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

| Format / protocol | Function | Pentest relevance |
|---------------------|----------|--------------------|
| SSL/TLS | Transport encryption | High (SSLstrip, downgrade) |
| ASCII/Unicode | Text encoding | Medium |
| Base64 | Binary to text encoding | High (payload obfuscation) |
| gzip/zlib | Data compression | Low |
| JPEG/PNG/GIF | Image formats | Medium (steganography) |
| MIME | Email multipart format | Medium |

---

## 8. Layer 7: Application

The Application Layer is the highest layer in the OSI model and the only layer that directly interacts with the end user. It provides the interface between applications and the network, and defines the protocols applications use to communicate.

> Note: the Application Layer does not mean the application itself (like Chrome or Firefox). It refers to the network protocols those applications use.

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

| Protocol | Port | Function | Pentest relevance |
|----------|------|----------|--------------------|
| HTTP | 80 | Unencrypted web | High |
| HTTPS | 443 | Encrypted web | High |
| DNS | 53 | Domain name resolution | High |
| FTP | 21 | File transfer (cleartext) | Critical |
| SSH | 22 | Secure shell | High |
| Telnet | 23 | Insecure shell | Critical |
| SMTP | 25 | Send email | High |
| POP3 | 110 | Retrieve email | Medium |
| IMAP | 143 | Manage email | Medium |
| SNMP | 161 | Network management | High |
| LDAP | 389 | Directory service | High |
| RDP | 3389 | Remote desktop | Critical |
| SMB | 445 | Windows file sharing | Critical |
| MSSQL | 1433 | SQL Server | High |
| MySQL | 3306 | MySQL database | High |
| RPC | 135 | Remote procedure call | High |

---

## 9. Data encapsulation

Encapsulation is the process where each OSI layer adds a header (and sometimes a trailer) to the data before passing it to the layer below. The reverse process is called de-encapsulation, which happens on the receiving side.

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

## 10. TCP vs UDP comparison

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

| Aspect | TCP | UDP |
|--------|-----|-----|
| PDU name | Segment | Datagram |
| Header size | 20 to 60 bytes | 8 bytes |
| Handshake | 3-way (SYN/SYN-ACK/ACK) | None |
| Reliability | Yes | No |
| Ordering | Yes (sequence numbers) | No |
| Flow control | Yes (windowing) | No |
| Error recovery | Yes (retransmit) | No |
| Speed | Slower | Faster |
| Broadcast | No | Yes |
| Multicast | No | Yes |
| Use cases | HTTP, SSH, FTP, SMTP | DNS, DHCP, VoIP, gaming |

---

## 11. Common ports

Ports are logical numbers (0 to 65535) that identify specific services or applications within a host. There are three categories:

- Well-known ports (0 to 1023): standardized, require root privileges
- Registered ports (1024 to 49151): registered with IANA
- Dynamic/private ports (49152 to 65535): used temporarily

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

### Critical ports reference table

| Port | Protocol | Service | Pentest risk | Notes |
|------|----------|---------|----------------|-------|
| 21 | TCP | FTP | Critical | Cleartext, anonymous login |
| 22 | TCP | SSH | High | Brute force, key auth |
| 23 | TCP | Telnet | Critical | Cleartext, deprecated |
| 25 | TCP | SMTP | High | User enum, relay abuse |
| 53 | TCP/UDP | DNS | High | Zone transfer, DNS poison |
| 67/68 | UDP | DHCP | High | Rogue DHCP, starvation |
| 80 | TCP | HTTP | High | Web attacks, SQLi, XSS |
| 88 | TCP/UDP | Kerberos | Critical | AS-REP roasting, Kerberoasting |
| 110 | TCP | POP3 | Medium | Cleartext credentials |
| 111 | TCP/UDP | RPC/rpcbind | High | NFS enumeration |
| 135 | TCP | MS-RPC | High | DCOM attacks |
| 139 | TCP | NetBIOS | High | SMB, null sessions |
| 143 | TCP | IMAP | Medium | Cleartext credentials |
| 161/162 | UDP | SNMP | High | Community string, info leak |
| 389 | TCP | LDAP | High | AD enumeration, null bind |
| 443 | TCP | HTTPS | High | Web attacks via HTTPS |
| 445 | TCP | SMB | Critical | EternalBlue, pass-the-hash |
| 512/513/514 | TCP | r-services | Critical | No auth, legacy |
| 873 | TCP | rsync | High | Unauth file access |
| 993 | TCP | IMAPS | Low | Encrypted |
| 995 | TCP | POP3S | Low | Encrypted |
| 1433 | TCP | MSSQL | High | SA account, xp_cmdshell |
| 1521 | TCP | Oracle DB | High | Default SID |
| 2049 | TCP/UDP | NFS | High | Unauth mount, root squash |
| 3306 | TCP | MySQL | High | Root no password |
| 3389 | TCP | RDP | Critical | BlueKeep, brute force |
| 5432 | TCP | PostgreSQL | High | Default credentials |
| 5900 | TCP | VNC | High | Weak/no auth |
| 6379 | TCP | Redis | Critical | No auth, RCE via config |
| 8080 | TCP | HTTP-alt | High | Dev servers, admin panels |
| 8443 | TCP | HTTPS-alt | High | Admin panels |
| 27017 | TCP | MongoDB | Critical | No auth default |

---

## 12. Protocols per layer

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

## 13. Network devices per layer

Each network device operates at a specific OSI layer. Understanding this matters for network segmentation, troubleshooting, and network-level attacks.

| OSI layer | Devices | Function |
|-----------|---------|-----------|
| Layer 7 | Application firewall, WAF, proxy, load balancer | Filter HTTP, SSL inspection |
| Layer 4 | Stateful firewall, load balancer | Port and connection filtering |
| Layer 3 | Router, Layer 3 switch, firewall | Inter-network routing |
| Layer 2 | Switch (L2), bridge, WAP | MAC-based switching |
| Layer 1 | Hub, repeater, cable, NIC, WAP | Physical signal transmission |

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

## 14. Security notes: attacks per OSI layer

Each OSI layer has distinct attack vectors. Understanding at which layer an attack occurs helps defenders place the right security controls, and helps attackers pick effective techniques.

> Educational note: the commands below are for authorized testing on networks you own or are permitted to test. They map attack categories to the layer they operate at, not a step-by-step attack guide against a target you do not control.

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

### OSI attack summary table

| Layer | Common attacks | Defense |
|-------|------------------|---------|
| 7 — Application | SQLi, XSS, RCE, CSRF, phishing | WAF, input validation, patching |
| 6 — Presentation | SSL stripping, TLS downgrade, cert spoofing | HSTS, cert pinning, TLS 1.3+ |
| 5 — Session | Session hijack, pass-the-hash, Kerberoasting | Token rotation, MFA, Kerberos hardening |
| 4 — Transport | SYN flood, port scan, UDP flood | SYN cookies, rate limiting, firewall |
| 3 — Network | IP spoof, ICMP flood, route poisoning | uRPF, ACL, ICMP rate limit |
| 2 — Data Link | ARP spoof, MAC flood, VLAN hopping | Dynamic ARP Inspection, port security |
| 1 — Physical | Wiretapping, evil twin, signal jamming | Physical security, encrypted protocols |

---

## 15. Practical workflow: network recon & analysis

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

### OSI troubleshooting approach

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

## OSI vs TCP/IP model

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

## Quick reference cheatsheet

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

## Complete OSI reference table

| Layer | Name | PDU | Address | Devices | Key protocols |
|-------|------|-----|---------|---------|-----------------|
| 7 | Application | Data | — | WAF, proxy | HTTP, FTP, DNS, SSH |
| 6 | Presentation | Data | — | — | SSL/TLS, MIME |
| 5 | Session | Data | — | — | NetBIOS, RPC |
| 4 | Transport | Segment/Datagram | Port | Firewall | TCP, UDP |
| 3 | Network | Packet | IP address | Router | IPv4, IPv6, ICMP |
| 2 | Data Link | Frame | MAC address | Switch | Ethernet, ARP, 802.1Q |
| 1 | Physical | Bits | — | Hub, NIC | DSL, Ethernet |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings, *Network Security Essentials: Applications and Standards (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Matthew Gast, *802.11 Wireless Networks: The Definitive Guide*, `~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - W. Richard Stevens, *UNIX Network Programming (Volume 1, 3rd Edition)*, `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 793 (TCP), RFC 768 (UDP)
> - Nmap and Wireshark official documentation, the IANA port number registry

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs for networks you own or are authorized to test on.
