# ARP & Serangan Jaringan Lokal

> **LearnCybersecurity** | Seri Networking Fundamentals
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-042` | **Fase 2:** Networking
> **Estimasi belajar:** 4 jam | **Level:** Advanced
> **Prasyarat:** LC-039, LC-040
> **Peta buku:** Kurose & Ross, Computer Networking Ch.4-5; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Kenapa ARP ada
2. ARP Request & Reply
3. ARP Cache (Neighbor Table)
4. Mekanisme terkait (Proxy ARP, GARP)
5. Konsep MITM di jaringan lokal
6. Pertahanan (DAI, static ARP, segmentasi)
7. Deteksi & monitoring
8. Catatan keamanan (ringkasan pertahanan)
9. Cheatsheet admin

---

## 1. Kenapa ARP ada

Pada Ethernet/IPv4, pengiriman frame membutuhkan alamat MAC tujuan di layer 2, sementara aplikasi dan routing memakai alamat IP di layer 3. ARP (Address Resolution Protocol) menjembatani dua dunia ini:

$$
\mathsf{ARP}:\ \mathsf{IPv4} \;\longrightarrow\; \mathsf{MAC}
$$

Resolusi ini hanya berlaku di link lokal, yaitu broadcast domain yang sama. Router tidak di-ARP lintas subnet untuk host jauh. Host cukup meng-ARP gateway-nya, lalu mengirim frame ke MAC gateway itu.

```
  Host A                    L2 switch                   Host B
  IP 10.0.0.5               (broadcast domain)          IP 10.0.0.9
  MAC aa:aa:…  ──────── ARP who-has 10.0.0.9 ────────►
               ◄─────── ARP is-at bb:bb:… ────────────
  Frame dst=bb:bb ───────────────────────────────────►
```

IPv6 memakai NDP (Neighbor Discovery), bukan ARP, dengan konsep serupa (resolusi L3 ke L2) lewat pesan ICMPv6.

ARP sendiri adalah protokol pemetaan bersifat trust-on-first-use dan soft-state, tanpa autentikasi kriptografis bawaan. Karena desain inilah, kontrol integritas di link lokal (DAI, entri statis, segmentasi) menjadi penting.

---

## 2. ARP Request & Reply

ARP dibungkus dalam frame Ethernet dengan EtherType `0x0806`. Ada dua operasi utama:

| `op` | Nama | Makna |
|:---:|:---|:---|
| 1 | Request | "Who has $IP_t$? Tell $IP_s$" |
| 2 | Reply | "$IP_t$ is at $MAC_t$" |

Field penting (IPv4 over Ethernet):

| Field | Isi tipikal |
|:---|:---|
| HTYPE / PTYPE | Ethernet / IPv4 |
| HLEN / PLEN | 6 / 4 |
| SHA / SPA | Sender MAC / Sender IP |
| THA / TPA | Target MAC / Target IP |

Request biasanya dikirim sebagai Ethernet broadcast (`ff:ff:ff:ff:ff:ff`), dengan THA sering diisi nol. Reply biasanya dikirim unicast ke SHA peminta, kecuali pada kasus khusus.

Alur kanonik:

$$
\begin{aligned}
A &\xrightarrow{\mathsf{ARP\,Req}(TPA=B)} \mathsf{Broadcast} \\
B &\xrightarrow{\mathsf{ARP\,Rep}(SPA=B,\,SHA=MAC_B)} A
\end{aligned}
$$

Setelah pertukaran ini, $A$ dapat mengirim frame IP dengan `dst MAC = MAC_B`.

Selain lewat request/reply eksplisit, host juga bisa belajar mapping dari paket yang mereka amati secara pasif, tergantung implementasi kernel/stack-nya. Reply yang tidak diminta atau tidak terduga adalah masalah integritas klasik, dan inilah alasan fitur switch memvalidasi ARP terhadap binding DHCP.

---

## 3. ARP Cache (Neighbor Table)

Kernel menyimpan pemetaan sementara:

$$
\mathsf{Cache}:\ (IP) \mapsto (MAC,\; \mathsf{state},\; \mathsf{iface},\; \mathsf{expiry})
$$

| Aspek | Perilaku umum |
|:---|:---|
| Incomplete | Request terkirim, belum ada reply |
| Reachable / stale | Ada mapping, bisa di-probe ulang |
| TTL / gc | Entri basi dibuang atau di-refresh |
| Failures | Retry terbatas lalu error neighbor |

Di Linux modern, `ip neigh` menampilkan state neighbor (ARP untuk IPv4, NDISC untuk IPv6). Memahami state ini membantu troubleshooting kasus "host unreachable on-link".

Aturan update secara intuitif: reply yang tampak sah dapat membuat atau menimpa entri cache. Tanpa validasi L2 tambahan, kebenaran cache sama saja dengan kebenaran siapa saja yang bisa berbicara di segmen tersebut.

Tips operasional: setelah renumbering alamat atau penggantian NIC, entri ARP/ND yang basi bisa menyebabkan konektivitas "hantu" sampai entri itu kedaluwarsa atau di-flush. Lakukan flush hanya pada sistem yang benar-benar Anda kelola sendiri.

---

## 4. Mekanisme terkait

| Mekanisme | Ringkasan | Catatan keamanan |
|:---|:---|:---|
| Proxy ARP | Router menjawab ARP untuk IP non-lokal seolah on-link | Memperluas trust L2, audit jika tidak disengaja |
| Gratuitous ARP (GARP) | Pengumuman SPA=TPA | Sah untuk failover/HA, tapi juga vektor spoof jika tidak difilter |
| Inverse ARP | MAC ke IP (jarang di Ethernet modern) | Konteks khusus (era Frame Relay, dan sejenisnya) |
| ARP probe / announce (RFC 5227) | Cek konflik alamat sebelum sebuah IP dipakai | Berguna untuk deteksi duplicate address |

```
  Normal ARP:     "Who has B? Tell A"     →  "B is at MAC_B"
  Gratuitous:     "A is at MAC_A"         →  (announce / update caches)
  Proxy:          "Who has X (remote)?"   →  Router replies with own MAC
```

---

## 5. Konsep MITM di jaringan lokal (level tinggi saja)

Ini konsep, bukan prosedur. Jika host jahat di segmen yang sama berhasil membuat korban menyimpan

$$
IP_{\mathsf{gateway}} \mapsto MAC_{\mathsf{attacker}}
$$

(dan secara opsional sebaliknya juga), maka frame yang seharusnya menuju gateway bisa dialihkan ke penyerang. Penyerang yang juga meneruskan trafik dapat mengamati atau mengubah sesi cleartext, dan inilah yang disebut MITM di layer 2.

Ini memanfaatkan sifat dasar ARP: tidak ada autentikasi kriptografis pada binding IP ke MAC.

> Catatan edukasi: langkah demi langkah poisoning, perintah tool untuk spoofing, atau playbook serangan sengaja tidak disertakan di sini. Fokus catatan ini adalah memahami kenapa kontrol switch dan segmentasi diperlukan.

Redirection on-link yang berhasil mematahkan asumsi "frame ke MAC gateway pasti sampai ke gateway". Enkripsi di layer atas (TLS) membatasi dampak terhadap kerahasiaan data, tapi tidak menghilangkan nilai integritas L2 untuk ketersediaan layanan dan untuk protokol yang tidak dienkripsi end-to-end.

---

## 6. Pertahanan: DAI, static ARP, segmentasi

| Kontrol | Cara kerja (intuisi) | Cocok untuk |
|:---|:---|:---|
| Dynamic ARP Inspection (DAI) | Switch memvalidasi ARP terhadap binding terpercaya (biasanya dari DHCP Snooping) | Access VLAN enterprise |
| DHCP Snooping | Mencatat (MAC, IP, port, VLAN) dari DHCP yang sah | Fondasi untuk DAI |
| Static ARP / static neigh | Binding tetap di host/router kritis | Gateway, server kecil, OT |
| Port security | Membatasi jumlah MAC per port | Access edge |
| Private VLAN / microsegmentation | Membatasi pergerakan lateral host ke host | Cloud / DC / campus |
| Separate management plane | Out-of-band atau VRF khusus manajemen | Infrastruktur |
| RA Guard / kontrol ND | Analog untuk IPv6 | Dual-stack |

Segmentasi tetap menjadi kontrol paling kuat secara arsitektural: semakin kecil broadcast domain, semakin kecil blast radius dari snooping atau spoofing di L2.

Model kepercayaan:

```
  [User VLAN] --DAI+DHCP Snoop--> [L3 gateway] --ACL--> [Server VLAN]
        │                              │
        └──── no hairpin L2 freely ────┘
```

Static ARP saja tidak bisa scale ke armada DHCP besar. Kombinasikan DAI di access layer dengan monitoring. Untuk enclave kecil yang benar-benar tepercaya, mapping statis di router tetap praktis dipakai.

---

## 7. Deteksi & monitoring

Gejala berikut patut diinvestigasi di lab atau produksi milik Anda:

| Sinyal | Makna yang mungkin |
|:---|:---|
| MAC gateway berubah di banyak host secara bersamaan | Binding tidak stabil / anomali L2 |
| IP duplikat (dua MAC mengklaim satu IP) | Konflik atau spoofing |
| Storm ARP request | Loop, misconfig, atau scan agresif |
| Drop counter DAI naik | ARP melanggar binding yang tercatat |
| TLS/VPN tetap OK tapi captive portal aneh | Kemungkinan L2 redirect plus intercept aktif |

Alat defensif untuk host/switch milik Anda sendiri:

```bash
# Bandingkan neighbor vs harapan admin
ip neigh show
bridge fdb show          # jika bridge Linux

# Observasi ARP di interface yang Anda miliki (bukan menyerang)
sudo tcpdump -ni eth0 arp
```

Korelasikan hasilnya dengan syslog switch (DAI denies) dan inventory DHCP lease.

---

## 8. Catatan keamanan: ringkasan pertahanan

| Isu | Risiko | Pertahanan |
|:---|:---|:---|
| ARP tanpa autentikasi | Binding cache palsu | DAI + DHCP Snooping |
| L2 flat | Lateral MITM / recon mudah dilakukan | VLAN / microsegmentation |
| GARP tidak dibatasi | Cache overwrite massal | Rate-limit / inspect policy |
| Static map basi | Outage setelah ganti NIC | Runbook untuk update ARP statis |
| IPv6 diabaikan | Celah karena fokus hanya di "ARP saja" | RA Guard, ND inspection |
| Protokol cleartext | Data terbaca kalau MITM berhasil | TLS di mana-mana, plus HSTS |

Prinsipnya: anggap L2 lokal hanya bisa dipercaya sejauh policy switch menegakkannya. Enkripsi end-to-end melengkapi, bukan menggantikan, kontrol akses di link.

---

## 9. Cheatsheet: admin / lab sendiri

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
| `tcpdump arp` | Audit trafik ARP di NIC Anda |
| `bridge fdb` | Lihat learning MAC di bridge |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - W. Richard Stevens, *UNIX Network Programming, Vol. 1*, `~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 826 (ARP), RFC 5227 (IPv4 Address Conflict Detection), RFC 4861 (NDP)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab pada jaringan milik sendiri atau yang sudah berizin. Tidak ada playbook poisoning di sini.
