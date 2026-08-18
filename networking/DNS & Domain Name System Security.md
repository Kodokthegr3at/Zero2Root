# 🧭 DNS & Domain Name System Security

> **LearnCybersecurity** | Networking Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Kurose & Ross — *Computer Networking*; Stallings — *Network Security Essentials*; Benvenuti — *Understanding Linux Network Internals*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-041` | **Phase 2:** Networking  
> **Est. study:** 4h | **Level:** Intermediate  
> **Prerequisites:** LC-039  
> **Book map:** Kurose & Ross Â Computer Networking Ch.2; Stallings Â Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Hierarchy | Hierarki namespace DNS | DNS namespace tree | DNS名前空間の階層 |
| 2 | Resolution | Algoritma resolusi | Recursive & iterative lookup | 再帰・反復解決 |
| 3 | Record Types | Jenis resource record | RR types & semantics | RRの種類と意味 |
| 4 | DNSSEC | Tanda tangan & rantai trust | RRSIG / DS / chain of trust | DNSSECと信頼連鎖 |
| 5 | Privacy | DoH & DoT | Encrypted DNS transports | DoH・DoT |
| 6 | Zone Transfer | Risiko misconfig AXFR | AXFR as config risk | ゾーン転送のリスク |
| 7 | Cache Poisoning | Konsep & pertahanan | Poisoning concept + defenses | キャッシュ汚染の概念 |
| 8 | Security Notes | Deteksi & hardening | Defense & detection | 防御と検知 |
| 9 | Cheatsheet | dig / resolvectl | Admin CLI lab | 管理CLI |

---

## 1. 🌳 DNS Hierarchy — Namespace Tree

### 🇮🇩 Bahasa Indonesia
**DNS (Domain Name System)** memetakan nama hierarkis ke resource (paling sering alamat IP). Namespace adalah **pohon terbalik** berakar di **root** (`.`). Setiap label dipisah titik; nama FQDN dibaca dari kanan ke kiri:

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www
```

Nama penuh: `www.example.com.` (titik akhir = root).

| Level | Contoh | Peran |
|:---|:---|:---|
| Root | `.` | Tip hierarki; root NS |
| TLD | `com`, `id`, `jp` | Dikelola registry |
| SLD / zone | `example.com` | Organisasi / zona otoritatif |
| Host / label | `www`, `mail` | Resource dalam zona |

Delegasi: parent menyimpan **NS** (+ glue **A/AAAA**) untuk child zone. Otoritas zona = set nameserver yang menjawab **AA** (Authoritative Answer) untuk nama di dalam zona.

### 🇬🇧 English
DNS is a distributed hierarchical database. No single server holds the whole tree; authority is **delegated** downward. Clients usually talk to a **recursive resolver**; that resolver walks the tree (or uses cache) to obtain an answer.

### 🇯🇵 日本語
DNSは分散階層データベースです。権威は親から子へ**委任**され、クライアントは通常**再帰リゾルバ**に問い合わせます。

---

## 2. 🔄 Resolution Algorithm

### 🇮🇩 Bahasa Indonesia
Dua peran utama:

| Peran | Perilaku |
|:---|:---|
| **Stub resolver** | Di OS/aplikasi; kirim query ke recursive resolver yang dikonfigurasi |
| **Recursive resolver** | Melakukan lookup penuh atas nama stub; boleh cache |
| **Authoritative server** | Menjawab hanya untuk zona yang dilayaninya |

Algoritma iteratif (intuisi Kurose):

$$
\begin{aligned}
&Q \leftarrow \text{query}(name, type) \\
&S \leftarrow \text{root hint set} \\
&\textbf{while } true: \\
&\quad R \leftarrow \mathsf{Query}(S, Q) \\
&\quad \textbf{if } R \text{ is answer or NXDOMAIN:} \; \textbf{return } R \\
&\quad S \leftarrow \text{referral NS (and glue) from } R
\end{aligned}
$$

```
Stub ──Q──► Recursive ──iterative──► Root
                 │                      │
                 │◄──── referral ───────┘
                 ├──► TLD NS
                 │◄── referral
                 └──► Auth NS ──► Answer (AA)
```

**Caching:** TTL pada RR membatasi lama cache. Jawaban negatif juga di-cache (RFC 2308) dengan aturan terpisah.

### 🇬🇧 English
Recursion offloads tree-walking from clients. Authoritative servers should typically **not** recurse for the public Internet (reduce amp/abuse surface). Separating recursive and authoritative roles is standard operational hygiene.

### 🇯🇵 日本語
再帰と権威の役割を分離するのが運用の基本です。公開権威サーバで不用意に再帰を有効にしないでください。

---

## 3. 📋 Resource Record Types

| Type | Fungsi singkat | Contoh data |
|:---|:---|:---|
| **A** | IPv4 host | `93.184.216.34` |
| **AAAA** | IPv6 host | `2606:2800:…` |
| **NS** | Delegasi / nameserver zona | `ns1.example.com.` |
| **CNAME** | Alias ke nama kanonik | `www → origin.cdn.net.` |
| **MX** | Mail exchanger + preference | `10 mail.example.com.` |
| **TXT** | Teks bebas (SPF, verifikasi, …) | `"v=spf1 …"` |
| **SOA** | Start of Authority (serial, timers) | zone meta |
| **PTR** | Reverse (in-addr.arpa / ip6.arpa) | nama host |
| **SRV** | Service location | `_sip._tcp…` |
| **DNSKEY** | Public key zona (DNSSEC) | key material |
| **DS** | Hash key child di parent (DNSSEC) | digest |
| **RRSIG** | Signature atas RRset | signature |
| **NSEC / NSEC3** | Proof of non-existence | authenticated denial |

**RRset:** semua RR dengan nama + type + class sama. Operasi DNSSEC menandatangani **RRset**, bukan satu RR tunggal secara terpisah dari siblings.

Wire format klasik: UDP/53 (jawaban besar → TCP/53 atau EDNS0). EDNS0 memperluas ukuran UDP dan membawa opsi (DO bit untuk DNSSEC OK, cookies, dll.).

---

## 4. 🔏 DNSSEC — Signatures & Chain of Trust

### 🇮🇩 Bahasa Indonesia
**DNSSEC** menambah **otentikasi & integritas** data DNS (bukan kerahasiaan). Resolver yang validasi memastikan jawaban berasal dari zona yang benar dan tidak diubah di transit/cache.

Komponen inti:

| RR | Peran |
|:---|:---|
| DNSKEY | Kunci publik zona (ZSK / KSK) |
| RRSIG | Tanda tangan atas RRset |
| DS | Digest DNSKEY child, disimpan di **parent** |
| NSEC/NSEC3 | Bukti nama/type tidak ada |

**Verifikasi RRSIG (konsep):** untuk RRset $R$ dan kunci publik $K$:

$$
\mathsf{Verify}\big(K_{\mathsf{pub}},\; R,\; \mathsf{RRSIG}(R)\big) = \mathsf{accept/reject}
$$

Secara abstrak (skema tanda tangan $\mathsf{Sign}/\mathsf{Verify}$):

$$
\mathsf{RRSIG}(R) = \mathsf{Sign}_{K_{\mathsf{priv}}}(\mathsf{Hash}(R) \;\|\; \mathsf{meta})
$$

di mana $\mathsf{meta}$ mencakup algorithm, labels, original TTL, inception/expiration, key tag, signer name.

**Chain of trust:**

```
Trust Anchor (root KSK, hardcoded/managed)
        │  validates
        ▼
   root DNSKEY ──RRSIG──► root zone data
        │  DS for .com
        ▼
   com DNSKEY ──► … ──DS──► example.com DNSKEY
                                │
                                ▼
                         RRSIG on example.com RRsets
```

Resolver membutuhkan **trust anchor** (biasanya root). Jika DS di parent cocok dengan DNSKEY child dan RRSIG valid serta dalam jendela waktu, RRset **Secure**. Kegagalan validasi ⇒ **Bogus** (jangan pakai jawaban). Zona tanpa DNSSEC ⇒ **Insecure** (bukan Bogus).

### 🇬🇧 English
DNSSEC stops **undetected** substitution of forged answers along the path or in cache — provided validators are enabled end-to-end. It does **not** encrypt queries; use DoT/DoH for confidentiality of the question.

### 🇯🇵 日本語
DNSSECは改ざん・なりすましの**検知**を提供します。クエリの秘匿はDoT/DoHの役割です。バリデーションを有効にしないと効果が限定されます。

---

## 5. 🔐 DNS Privacy — DoT & DoH

| Mekanisme | Port / framing | Sifat |
|:---|:---|:---|
| Classic DNS | UDP/TCP 53 | Cleartext question & answer |
| **DoT** (DNS over TLS) | TCP 853 | DNS di dalam TLS |
| **DoH** (DNS over HTTPS) | TCP 443 | DNS di HTTP(S) API |

Manfaat: mencegah **pengintaian pasif** dan manipulasi on-path terhadap query/response di jalur cleartext.

Trade-off operasional:
- Resolver pusat (mis. vendor DoH) dapat melihat metadata resolusi — pilih kebijakan privasi dengan sadar.
- Enterprise sering **memaksa** resolver internal + blokir DoH liar agar logging/DLP tetap jalan — dokumentasikan & komunikasikan.
- Kombinasi ideal lab/produk: **DoT/DoH ke resolver yang memvalidasi DNSSEC**.

---

## 6. 📤 Zone Transfer — Misconfiguration Risk

### 🇮🇩 Bahasa Indonesia
**AXFR** (full zone transfer) dan **IXFR** (incremental) dipakai agar secondary meniru zona primary. Ini **fitur operasional sah**, bukan “serangan” — tetapi jika diizinkan ke **semua sumber**, seluruh isi zona (host internal, naming scheme) dapat diunduh oleh pihak luar.

Risiko misconfig:
- Exposure inventori nama internal
- Membantu recon sebelum serangan lain
- Secondary palsu jika tidak ada kontrol akses + (idealnya) TSIG

**Hardening (admin zona Anda):**
- Batasi AXFR/IXFR ke IP secondary yang dikenal
- Gunakan **TSIG** (shared secret HMAC) antar primary–secondary
- Jangan andalkan “security through obscurity” nama host; tetap segmentasi & least privilege

> Tidak ada prosedur serangan di catatan ini — hanya kesadaran konfigurasi & checklist defensif.

### 🇬🇧 English
Treat open zone transfer as a **configuration defect**. Monitor for unexpected AXFR attempts in authoritative logs.

### 🇯🇵 日本語
ゾーン転送の開放は設定不備です。許可IPとTSIGで制限し、ログで異常なAXFRを監視します。

---

## 7. 🧪 Cache Poisoning — Concept & Defenses

### 🇮🇩 Bahasa Indonesia
**Cache poisoning (konsep):** recursive resolver menyimpan binding nama→data yang **salah** karena menerima jawaban palsu yang tampak sah (matching ID/question) sebelum jawaban asli, atau karena kelemahan prediksi transaksi.

Model ancaman tinggi-level (Kaminsky-era intuition): ruang tebakan transaksi historis terlalu kecil jika:

$$
|\mathcal{S}| = 2^{16}\;(\mathsf{TXID}) \times \#\{\text{src ports}\}
$$

kecil, dan penyerang dapat membanjiri jawaban spoof untuk query yang ia picu.

**Pertahanan modern (bukan cookbook serangan):**

| Kontrol | Efek |
|:---|:---|
| **Source port randomization** | Perbesar ruang tebakan transaksi |
| **TXID random** | Sudah lama wajib; kombinasi dengan port |
| **DNS cookies** (RFC 7873) | Token klien–server mengurangi spoof murah |
| **DNSSEC validation** | Jawaban palsu gagal verifikasi ⇒ Bogus |
| **0x20 encoding / QNAME case** | Entropy ekstra di wire (di mana didukung) |
| **Network path security** | Batasi siapa yang bisa inject di jalur resolver |

Deteksi: lonjakan SERVFAIL pada zona yang biasanya aman, RRset yang tiba-tiba berubah tanpa perubahan zona, ketidakcocokan dengan pandangan resolver validasi lain.

### 🇬🇧 English
Defense-in-depth: entropy on the query transaction **plus** cryptographic authenticity (DNSSEC). Neither alone is a complete operational story.

### 🇯🇵 日本語
トランザクションの乱数化とDNSSEC検証を組み合わせるのが現代的な防御です。

---

## 8. 🔐 Security Notes — Defense & Detection

| Isu | Risiko | Pertahanan / deteksi |
|:---|:---|:---|
| Cleartext DNS | Sniff / on-path tamper | DoT/DoH; path terpercaya |
| Non-validating resolver | Forgery tak terdeteksi | Aktifkan DNSSEC validation |
| Open recursive | Abuse / amplification | ACL klien; pisah auth vs recursive |
| Open AXFR | Zone dump | ACL + TSIG; alert di log |
| Rogue resolver (DHCP/RA) | Redirect resolusi | DHCP snooping, RA Guard, policy DoH |
| Stale trust anchors | False Bogus / outage | Automasi RFC 5011 / monitoring |

**Lab hygiene:** uji hanya resolver & zona **milik Anda**. Bandingkan jawaban `dig +dnssec` vs resolver publik yang memvalidasi ketika mendiagnosis Bogus.

---

## 9. 🧠 Cheatsheet — Legitimate Admin / Lab

```bash
# ── Basic lookup (sistem Anda) ───────────────────────────────
dig example.com A +noall +answer
dig example.com AAAA
dig MX example.com
dig NS example.com

# ── Trace iterative path (observability) ─────────────────────
dig +trace example.com

# ── DNSSEC inspection ────────────────────────────────────────
dig example.com A +dnssec +multi
dig DNSKEY example.com +multi
dig DS example.com +short
delv example.com A          # validating lookup jika dikonfigurasi

# ── Reverse / SOA ────────────────────────────────────────────
dig -x 93.184.216.34
dig SOA example.com +noall +answer

# ── Check if YOUR authoritative allows transfer to YOU only ──
# (jalankan dari secondary yang diizinkan; expect REFUSED dari host lain)
dig AXFR example.com @ns1.example.com

# ── Local stub / systemd-resolved ────────────────────────────
resolvectl status
resolvectl query example.com
```

| Perintah | Kegunaan |
|:---|:---|
| `dig +short` | Jawaban ringkas |
| `dig +dnssec` | Tampilkan RRSIG / DO |
| `dig +trace` | Simulasikan jalan dari root |
| `delv` | Validasi DNSSEC sisi klien BIND tools |

---

> 📚 **References & Book Sources**
> - James Kurose & Keith Ross — *Computer Networking: A Top-Down Approach* — `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings — *Network Security Essentials (4th Edition)* — `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Christian Benvenuti — *Understanding Linux Network Internals* — `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - RFC 1034/1035 (DNS), RFC 4033–4035 (DNSSEC), RFC 7858 (DoT), RFC 8484 (DoH), RFC 7873 (Cookies)
> - `man dig`, `man resolvectl`

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & lab pada sistem/zona milik sendiri atau berizin — tanpa prosedur serangan.
