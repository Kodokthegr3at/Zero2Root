# 🔗 ARP & Local Network Attacks

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Kurose & Ross — *Computer Networking*; Benvenuti — *Understanding Linux Network Internals*; Stallings — *Network Security Essentials*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-042` | **Phase 2:** Networking  
> **Est. study:** 4h | **Level:** Advanced  
> **Prerequisites:** LC-039, LC-040  
> **Book map:** Kurose & Ross Â Computer Networking Ch.4-5; Stallings Â Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Role of ARP | Peran ARP di L2/L3 | Why ARP exists | ARPの役割 |
| 2 | Request / Reply | Format & alur | Packet exchange | 要求と応答 |
| 3 | ARP Cache | Tabel & aging | Cache semantics | キャッシュ |
| 4 | Proxy & Variants | Proxy ARP, GARP | Related mechanisms | 派生メカニズム |
| 5 | MITM Concept | Konsep tinggi | High-level MITM | MITMの概念 |
| 6 | Defenses | DAI, static, segmentasi | Hardening controls | 防御策 |
| 7 | Detection | Gejala & monitoring | What to watch | 検知 |
| 8 | Security Notes | Checklist defensif | Defense summary | 防御まとめ |
| 9 | Cheatsheet | ip neigh / tcpdump | Admin CLI | 管理CLI |

---

## 1. 🎯 Why ARP Exists

### 🇮🇩 Bahasa Indonesia
Pada Ethernet/IPv4, pengiriman frame membutuhkan **alamat MAC** destinasi di L2, sementara aplikasi/routing memakai **alamat IP** di L3. **ARP (Address Resolution Protocol)** menyelesaikan:

$$
\mathsf{ARP}:\ \mathsf{IPv4} \;\longrightarrow\; \mathsf{MAC}
$$

hanya di **link lokal** (broadcast domain yang sama). Router tidak di-ARP lintas subnet untuk host jauh — host meng-ARP **gateway** lalu mengirim frame ke MAC gateway.

```
  Host A                    L2 switch                   Host B
  IP 10.0.0.5               (broadcast domain)          IP 10.0.0.9
  MAC aa:aa:…  ──────── ARP who-has 10.0.0.9 ────────►
               ◄─────── ARP is-at bb:bb:… ────────────
  Frame dst=bb:bb ───────────────────────────────────►
```

IPv6 memakai **NDP** (Neighbor Discovery), bukan ARP — konsep serupa (resolusi L3→L2) dengan pesan ICMPv6.

### 🇬🇧 English
ARP is a **trust-on-first-use / soft-state** mapping protocol with no built-in cryptographic authenticity. That design choice is why local-link integrity controls matter.

### 🇯🇵 日本語
ARP自体に暗号的認証はありません。同一L2セグメントでは別途の防御（DAI、静的エントリ、セグメント分離）が重要です。

---

## 2. 📨 ARP Request & Reply

### 🇮🇩 Bahasa Indonesia
ARP dibungkus Ethernet: EtherType `0x0806`. Operasi utama:

| `op` | Nama | Makna |
|:---:|:---|:---|
| 1 | Request | “Who has $IP_t$? Tell $IP_s$” |
| 2 | Reply | “$IP_t$ is at $MAC_t$” |

Field penting (IPv4 over Ethernet):

| Field | Isi tipikal |
|:---|:---|
| HTYPE / PTYPE | Ethernet / IPv4 |
| HLEN / PLEN | 6 / 4 |
| SHA / SPA | Sender MAC / Sender IP |
| THA / TPA | Target MAC / Target IP |

**Request:** biasanya Ethernet **broadcast** (`ff:ff:ff:ff:ff:ff`), THA sering nol.  
**Reply:** biasanya **unicast** ke SHA peminta (kecuali kasus khusus).

Alur kanonik:

$$
\begin{aligned}
A &\xrightarrow{\mathsf{ARP\,Req}(TPA=B)} \mathsf{Broadcast} \\
B &\xrightarrow{\mathsf{ARP\,Rep}(SPA=B,\,SHA=MAC_B)} A
\end{aligned}
$$

Setelah itu $A$ dapat mengirim frame IP dengan `dst MAC = MAC_B`.

### 🇬🇧 English
Hosts also learn from packets they observe (implementation-dependent). Unsolicited or unexpected replies are a classic integrity concern — hence switch features that validate ARP against DHCP bindings.

### 日本語
実装によっては観測パケットからも学習します。予期しないARP応答は整合性リスクです。

---

## 3. 🗄️ ARP Cache (Neighbor Table)

### 🇮🇩 Bahasa Indonesia
Kernel menyimpan mapping sementara:

$$
\mathsf{Cache}:\ (IP) \mapsto (MAC,\; \mathsf{state},\; \mathsf{iface},\; \mathsf{expiry})
$$

| Aspek | Perilaku umum |
|:---|:---|
| Incomplete | Request terkirim, belum reply |
| Reachable / stale | Ada mapping; bisa di-probe ulang |
| TTL / gc | Entri basi dibuang atau di-refresh |
| Failures | Retry terbatas lalu error neighbor |

Di Linux modern, `ip neigh` menampilkan state neighbor (ARP untuk IPv4, NDISC untuk IPv6). Memahami state membantu troubleshooting “host unreachable on-link”.

**Update rules (intuisi):** reply yang tampak sah dapat **membuat atau menimpa** entri. Tanpa validasi L2 tambahan, kebenaran cache = kebenaran siapa yang bisa berbicara di segmen.

### 🇬🇧 English
Operational tip: after renumbering or NIC replacement, stale ARP/ND entries cause “ghost” connectivity until timeout or flush — flush **only on systems you administer**.

### 🇯🇵 日本語
アドレスやNIC変更後は古いneighborが残ることがあります。管理下ホストでのみキャッシュを消して再学習させます。

---

## 4. 🔀 Related Mechanisms

| Mekanisme | Ringkasan | Catatan keamanan |
|:---|:---|:---|
| **Proxy ARP** | Router menjawab ARP untuk IP non-lokal seolah on-link | Memperluas trust L2; audit jika tak disengaja |
| **Gratuitous ARP (GARP)** | Pengumuman SPA=TPA | Sah untuk failover/HA; juga vektor spoof jika tak difilter |
| **Inverse ARP** | MAC→IP (jarang di Ethernet modern) | Konteks khusus (Frame Relay era, dll.) |
| **ARP probe / announce** (RFC 5227) | Cek konflik alamat sebelum pakai IP | Baik untuk deteksi duplicate address |

```
  Normal ARP:     "Who has B? Tell A"     →  "B is at MAC_B"
  Gratuitous:     "A is at MAC_A"         →  (announce / update caches)
  Proxy:          "Who has X (remote)?"   →  Router replies with own MAC
```

---

## 5. ⚠️ On-Link MITM — High-Level Concept Only

### 🇮🇩 Bahasa Indonesia
**Konsep (bukan prosedur):** jika host jahat di segmen yang sama berhasil membuat korban menyimpan

$$
IP_{\mathsf{gateway}} \mapsto MAC_{\mathsf{attacker}}
$$

(dan opsional sebaliknya), maka frame yang seharusnya ke gateway dapat dialihkan ke penyerang. Penyerang yang juga meneruskan traffic dapat mengamati atau mengubah sesi cleartext ⇒ **MITM pada L2**.

Ini memanfaatkan sifat ARP: **tidak ada autentikasi kriptografi** pada binding IP–MAC.

> Catatan edukasi: langkah demi langkah poisoning, tool command untuk spoof, atau playbook serangan **sengaja tidak disertakan**. Fokus catatan ini: memahami mengapa kontrol switch & segmentasi diperlukan.

### 🇬🇧 English
Any successful on-link redirection breaks the assumption “frames to the gateway MAC reach the gateway.” Encrypt higher layers (TLS) limits confidentiality impact; it does not remove the value of L2 integrity for availability and for protocols that are not end-to-end encrypted.

### 🇯🇵 日本語
L2での経路横取りは、上位のTLSがあっても可用性や非暗号プロトコルに影響し得ます。セグメント設計とスイッチ制御が第一防衛線です。

---

## 6. 🛡️ Defenses — DAI, Static ARP, Segmentation

### 🇮🇩 Bahasa Indonesia

| Kontrol | Cara kerja (intuisi) | Cocok untuk |
|:---|:---|:---|
| **Dynamic ARP Inspection (DAI)** | Switch memvalidasi ARP terhadap binding terpercaya (sering dari DHCP Snooping) | Access VLAN enterprise |
| **DHCP Snooping** | Catat (MAC, IP, port, VLAN) dari DHCP sah | Fondasi DAI |
| **Static ARP / static neigh** | Binding tetap di host/router kritis | Gateway, server kecil, OT |
| **Port security** | Batasi MAC per port | Access edge |
| **Private VLAN / microseg** | Batasi lateral host-to-host | Cloud / DC / campus |
| **Separate mgmt plane** | Out-of-band / VRF manajemen | Infrastruktur |
| **RA Guard / ND controls** | Analog IPv6 | Dual-stack |

**Segmentasi** tetap kontrol paling kuat secara arsitektural: semakin kecil broadcast domain, semakin kecil blast radius snooping/spoof L2.

Model kepercayaan:

```
  [User VLAN] --DAI+DHCP Snoop--> [L3 gateway] --ACL--> [Server VLAN]
        │                              │
        └──── no hairpin L2 freely ────┘
```

### 🇬🇧 English
Static ARP alone does not scale to DHCP fleets; combine **DAI** at the access layer with monitoring. For very small trusted enclaves, static mappings on routers remain practical.

### 日本語
大規模DHCP環境ではDAIが現実的です。小規模の重要ノードには静的ARPも有効です。

---

## 7. 📡 Detection & Monitoring

Gejala yang patut diinvestigasi di lab/produksi Anda:

| Sinyal | Makna mungkin |
|:---|:---|
| MAC gateway berubah di banyak host bersamaan | Binding tidak stabil / anomali L2 |
| Duplikat IP (two MACs claim one IP) | Konflik atau spoof |
| Storm ARP request | Loop, misconfig, atau scan agresif |
| DAI drop counters naik | ARP melanggar binding |
| TLS/VPN tetap OK tapi captive aneh | Bisa L2 redirect + active intercept |

Alat defensif (host/switch milik Anda):

```bash
# Bandingkan neighbor vs harapan admin
ip neigh show
bridge fdb show          # jika bridge Linux

# Observasi ARP di interface yang Anda miliki (bukan menyerang)
sudo tcpdump -ni eth0 arp
```

Korelasikan dengan syslog switch (DAI denies) dan inventory DHCP leases.

---

## 8. 🔐 Security Notes — Defense Summary

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| Unauthenticated ARP | Cache binding palsu | DAI + DHCP Snooping |
| Flat L2 | Lateral MITM / recon mudah | VLAN / microsegmentation |
| GARP unrestricted | Cache overwrite massal | Rate-limit / inspect policy |
| Stale static maps | Outage setelah ganti NIC | Runbook update ARP statis |
| IPv6 ignored | Bypass fokus “ARP only” | RA Guard, ND inspection |
| Cleartext protocols | Data terbaca jika MITM sukses | TLS di mana-mana + HSTS |

**Prinsip:** anggap L2 lokal sebagai **trusted only as far as switch policy enforces**. Enkripsi end-to-end melengkapi, bukan menggantikan, kontrol akses link.

---

## 9. 🧠 Cheatsheet — Admin / Own Lab

```bash
# ── Inspect neighbor table ───────────────────────────────────
ip neigh show
ip -4 neigh show dev eth0
ip -6 neigh show

# ── Manage entries on YOUR host (careful in prod) ────────────
sudo ip neigh add 10.0.0.1 lladdr aa:bb:cc:dd:ee:ff dev eth0 nud permanent
sudo ip neigh del 10.0.0.1 dev eth0
sudo ip neigh flush dev eth0

# ── Trigger resolution (legitimate traffic) ──────────────────
ping -c 1 10.0.0.9
ip neigh get 10.0.0.9 dev eth0

# ── Passive observation on interfaces you own ────────────────
sudo tcpdump -ni eth0 'arp' -vv
sudo tcpdump -ni eth0 'arp and arp[6:2] == 2'   # replies only

# ── MAC / FDB visibility (Linux bridge) ──────────────────────
ip link show
bridge link show
bridge fdb show
```

| Perintah | Kegunaan |
|:---|:---|
| `ip neigh` | Lihat/ubah ARP/ND cache |
| `tcpdump arp` | Audit traffic ARP di NIC Anda |
| `bridge fdb` | Lihat learning MAC di bridge |

---

> 📚 **References & Book Sources**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach* — `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti — *Understanding Linux Network Internals* — `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings — *Network Security Essentials (4th Edition)* — `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - W. Richard Stevens — *UNIX Network Programming, Vol. 1* — `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 826 (ARP), RFC 5227 (IPv4 Address Conflict Detection), RFC 4861 (NDP)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & lab pada jaringan milik sendiri / berizin — tanpa playbook poisoning.
