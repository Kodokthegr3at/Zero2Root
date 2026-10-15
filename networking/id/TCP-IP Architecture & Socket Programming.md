# Arsitektur TCP/IP & Socket Programming

> **LearnCybersecurity** | Seri Dasar Networking
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Kurose & Ross, *Computer Networking*; Stevens, *UNIX Network Programming*; Benvenuti, *Understanding Linux Network Internals*; Stallings, *Network Security Essentials*

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-039` | **Fase 2:** Networking
> **Estimasi belajar:** 5-6 jam | **Level:** Menengah
> **Prasyarat:** LC-038
> **Peta buku:** Kurose & Ross, Computer Networking Ch.3-4; Stevens, UNIX Network Programming Vol.1 Ch.1-6
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Model TCP/IP 4 layer
2. Isi sebuah paket IP
3. Isi sebuah segmen TCP
4. Perjalanan hidup sebuah koneksi TCP
5. Handshake 3 langkah
6. Flow control dan congestion control, versi sederhana
7. Socket: cara program benar-benar memakai jaringan
8. SYN flood dan SYN cookie
9. Catatan keamanan
10. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| TCP/IP | Model 4 layer sungguhan yang dipakai Internet |
| Paket / segmen | Potongan data di Internet layer (paket) dan Transport layer (segmen) |
| Header | Label yang ditempelkan sebuah layer di depan data: dari siapa, untuk siapa, dsb. |
| Port | Angka yang memilih data itu untuk program yang mana |
| Socket | "Colokan" program ke jaringan: satu ujung dari sebuah koneksi |
| 4-tuple | Yang membuat sebuah koneksi unik: IP sumber + port sumber + IP tujuan + port tujuan |
| TTL | "Time to live": penghitung yang turun satu di tiap router, supaya paket yang tersesat akhirnya mati |
| SYN / ACK / FIN / RST | Flag TCP: mulai, akui, selesai, dan reset mendadak |
| Window | Seberapa banyak data yang mau diterima penerima sebelum berhenti dulu |
| Spoofing | Memalsukan alamat sumber sebuah paket |

---

## 1. Model TCP/IP 4 Layer

Model OSI (LC-038) punya 7 layer untuk mengajar. Jaringan nyata berjalan di atas model **4 layer** yang lebih ramping. Tiap layer membungkus layer di atasnya dengan sebuah header, seperti amplop bersusun.

| Layer | Tugasnya | Contoh |
|:---|:---|:---|
| Application | Apa yang sebenarnya ingin dikatakan aplikasi | HTTP, DNS, SSH |
| Transport | Menyampaikan ke program yang tepat, dengan andal atau cepat | TCP, UDP, QUIC |
| Internet | Menyampaikan ke mesin yang tepat, melintasi jaringan | IPv4, IPv6, ICMP |
| Link | Menyampaikan lewat satu lompatan fisik | Ethernet, Wi-Fi |

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
         turun ↓
  [Eth][IP][TCP][data aplikasi][FCS]
```

Saat naik, tiap layer membaca dan melepas header-nya sendiri, lalu menentukan menyerahkan sisanya ke siapa (memakai EtherType, field protokol IP, dan nomor port). Kontrol keamanan ada di setiap layer: tidak ada satu layer ajaib, karena itu pertahanan nyata menumpuk beberapa (defense in depth).

---

## 2. Isi Sebuah Paket IP

Tugas Internet layer adalah pengalamatan dan routing. Header IPv4 minimal 20 byte. Kamu tidak perlu menghafal tata letak bit-nya, tapi sebaiknya mengenali field yang penting untuk keamanan.

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
```

| Field | Kenapa penting |
|:---|:---|
| Version | 4 atau 6 |
| Total Length | Seberapa besar seluruh paketnya |
| Fragmentation (ID/Flags/Offset) | Memecah paket besar; stack lama bisa ditipu saat penyusunan ulang, yang modern menanganinya dengan baik |
| TTL | Turun 1 tiap router; mencegah paket berputar selamanya, dan membocorkan petunjuk OS pengirim |
| Protocol | Isinya apa: 6 = TCP, 17 = UDP, 1 = ICMP |
| Source / Destination | Alamatnya; **sumber bisa dipalsukan** kecuali jaringan memfilternya |

```text
ukuran header  = IHL × 4 byte
ukuran payload = Total Length − ukuran header

Contoh: Total Length = 60, IHL = 5  →  header = 20 byte  →  payload = 40 byte
```

Poin keamanan terpenting di sini: alamat sumber sebuah paket IP **hanyalah klaim**. Tanpa filter di tepi jaringan, penyerang bisa menulis alamat sumber apa pun yang dia mau (spoofing).

---

## 3. Isi Sebuah Segmen TCP

TCP mengubah pengiriman IP yang "sebisanya" dan tidak andal menjadi aliran byte yang andal dan berurutan. Caranya lewat field-field di header-nya.

| Field | Gunanya |
|:---|:---|
| Port Sumber / Tujuan | Program mana di tiap ujung |
| Sequence number | Posisi data ini di dalam aliran |
| Acknowledgement number | "Aku sudah menerima semua sampai di sini" |
| Flags | SYN (mulai), ACK (akui), FIN (selesai), RST (reset), dan lainnya |
| Window | Seberapa banyak lagi yang bisa diterima penerima saat ini |
| Checksum | Menangkap data yang rusak |

Satu koneksi dikenali oleh empat hal sekaligus, si **4-tuple**:

```text
(IP sumber, port sumber, IP tujuan, port tujuan)
```

Dua tab browser ke situs yang sama hanya berbeda di port sumber, dan itu sudah cukup untuk memisahkannya.

---

## 4. Perjalanan Hidup Sebuah Koneksi TCP

Koneksi TCP melewati serangkaian state, seperti panggilan telepon dari memanggil, lalu bicara, lalu menutup.

```
  CLOSED ──listen──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──connect─► SYN_SENT ───────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT ──► TIME_WAIT ──► CLOSED
```

| State | Artinya |
|:---|:---|
| LISTEN | Server menunggu ada yang menyambung |
| SYN_SENT / SYN_RCVD | Handshake sedang berjalan |
| ESTABLISHED | Tersambung, data mengalir |
| TIME_WAIT | Baru ditutup; menunggu sebentar supaya paket lama yang tersesat mati |
| CLOSE_WAIT | Pihak lain menutup; aplikasimu masih perlu menutup |

```bash
ss -tan      # lihat semua koneksi TCP dan state-nya (Linux)
```

Kebingungan yang umum: banyaknya entri `TIME_WAIT` terlihat seperti bug padahal normal dan sehat. Jangan mematikan `TIME_WAIT` tanpa paham kenapa ada; ia melindungi dari paket lama yang disalahartikan sebagai paket baru.

---

## 5. Handshake 3 Langkah

Sebelum data mengalir, kedua pihak menyelaraskan diri dalam tiga langkah. Anggap saja: "Kamu dengar aku?" — "Ya, kamu dengar aku?" — "Ya."

```
  Client                     Server
    │  SYN, seq=x               │   1. "Ayo bicara, counter-ku mulai dari x"
    │──────────────────────────►│
    │  SYN+ACK, seq=y, ack=x+1  │   2. "Oke, punyaku mulai dari y, x-mu kuterima"
    │◄──────────────────────────│
    │  ACK, ack=y+1             │   3. "y-mu kuterima, ayo mulai"
    │──────────────────────────►│
    │      ESTABLISHED          │
```

Tiap pihak memilih angka awal (**initial sequence number**, ISN). Sistem modern membuat ISN dengan cara yang sulit ditebak, jadi penyerang dari luar jalur tidak mudah menebaknya dan menyuntikkan data palsu. Penutupan adalah pertukaran sopan serupa berupa FIN/ACK, atau satu RST untuk menutup koneksi secara paksa.

---

## 6. Flow Control dan Congestion Control, Versi Sederhana

TCP terus menjawab dua pertanyaan: "Apakah penerima mengikuti?" dan "Apakah jaringan mengikuti?"

- **Flow control** melindungi *penerima*: ia mengumumkan **window** (`rwnd`) yang menyatakan seberapa banyak yang sanggup diterima.
- **Congestion control** melindungi *jaringan*: pengirim menjaga batasnya sendiri (`cwnd`) supaya tidak membanjiri jalur bersama.

```text
data yang boleh "melayang" ≤ nilai terkecil antara cwnd dan rwnd
```

Pengirim dibatasi oleh yang lebih kecil. Saat koneksi mulai, `cwnd` tumbuh cepat (**slow start**, yang sebenarnya berlipat dua tiap round trip), lalu tumbuh hati-hati, dan mundur tajam saat paket mulai hilang.

```text
slow start: cwnd bertambah satu segmen tiap ACK
            → kira-kira berlipat dua tiap round trip
```

Kamu jarang mengaturnya manual. Yang kamu amati adalah round-trip time, retransmisi, dan penundaan akibat buffer. Sisi keamanan: banjir traffic TCP atau UDP bisa membuat jalur macet sampai jadi denial of service, karena itu rate limiting dan perencanaan kapasitas penting.

---

## 7. Socket: Cara Program Benar-Benar Memakai Jaringan

**Socket** adalah pegangan program atas sebuah koneksi jaringan, satu ujung percakapan. Server TCP mengikuti resep yang tetap:

```text
socket  →  bind  →  listen  →  accept (loop)  →  recv / send  →  close
```

Client lebih sederhana: `socket → connect → send / recv → close`.

### Contoh Python 3

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))   # listen di port 8080
    s.listen(128)
    conn, peer = s.accept()     # tunggu sebuah client
    with conn:
        data = conn.recv(4096)
        conn.sendall(b"OK\n")
```

| Panggilan | Yang dilakukan |
|:---|:---|
| `bind` | Mengklaim alamat dan port lokal |
| `listen` | Mulai menerima koneksi (dengan antrean) |
| `accept` | Mengambil koneksi berikutnya yang siap |
| `connect` | Menghubungi server (sisi client) |

UDP lebih sederhana: tanpa handshake, pakai `sendto` / `recvfrom`.

Anggap jaringan itu bermusuhan. Validasi semua yang kamu baca, pasang timeout supaya peer yang macet tidak menggantungmu selamanya, dan bungkus traffic sensitif dengan TLS (modul `ssl` di Python), bukan menciptakan proteksi sendiri.

---

## 8. SYN Flood dan SYN Cookie

**Masalahnya:** di handshake, ketika server menerima SYN, ia menyisihkan sedikit memori untuk koneksi yang belum selesai lalu menunggu ACK terakhir. Penyerang bisa mengirim banjir SYN (sering dengan alamat sumber palsu) dan tidak pernah menyelesaikannya. Server penuh oleh koneksi setengah terbuka dan kehabisan ruang untuk pengguna sungguhan. Itulah **SYN flood**, sejenis denial of service.

**Pertahanannya — SYN cookie:** alih-alih memesan memori tiap SYN, server menyandikan informasi yang dibutuhkan ke dalam sequence number yang dikirimnya balik, dilindungi oleh sebuah rahasia. Server baru membuat state koneksi sungguhan ketika ACK terakhir yang valid kembali membawa nilai sandi itu. Banjir SYN yang tidak pernah selesai jadi nyaris tidak membebani server.

```text
sequence number balasan ≈ Hash(rahasia, 4-tuple, waktu) + info ukuran
```

Pertahanan lain: ukuran antrean koneksi yang masuk akal, membatasi laju SYN per sumber, dan proxy penanganan SYN atau layanan scrubbing di depan server publik.

> Materi ini menjelaskan konsep dan pertahanannya, bukan cara menjalankan flood.

---

## 9. Catatan Keamanan

| Masalah | Risiko | Pertahanan |
|:---|:---|:---|
| SYN flood | Memenuhi slot setengah terbuka server | SYN cookie, rate limiting, perencanaan kapasitas |
| Sumber dipalsukan | Penyalahgunaan reflection dan flood | Filter alamat sumber di tepi (BCP38 / uRPF) |
| Injeksi RST | Mematikan session kalau sequence-nya bisa ditebak | Transport terenkripsi; ISN yang sulit ditebak |
| Aplikasi TCP cleartext | Penyadapan dan perubahan | TLS 1.3 |
| Listen di `0.0.0.0` | Terekspos ke tiap jaringan tanpa sengaja | Bind ke interface internal; firewall |

Kebersihan lab: bereksperimen dengan handshake dan socket hanya di mesin milikmu, dan amati secara defensif dengan `ss` dan `tcpdump`.

---

## 10. Cheatsheet

```bash
# ── Lihat state koneksi ──────────────────────────────────────
ss -tan                 # semua koneksi TCP + state
ss -tanp state syn-recv # koneksi setengah terbuka (gejala flood)
ss -s                   # ringkasan jumlah

# ── Amati interface milikmu ──────────────────────────────────
sudo tcpdump -ni eth0 'tcp[tcpflags] & tcp-syn != 0'   # paket SYN
sudo tcpdump -ni lo port 8080 -vv

# ── Baca setting kernel (ubah hanya di host lab milikmu) ─────
sysctl net.ipv4.tcp_syncookies
sysctl net.core.somaxconn
```

| Tool | Kegunaan |
|:---|:---|
| `ss` | Tampilan modern state TCP/UDP (pengganti `netstat`) |
| `tcpdump` | Mengamati flag SYN / FIN / RST di NIC-mu |
| `sysctl` | Membaca atau mengatur setting stack di host lab |

---

> **Referensi & sumber buku**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - W. Richard Stevens, *UNIX Network Programming, Volume 1 (3rd Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 791 (IPv4), RFC 9293 (TCP), RFC 4987 (SYN flood / cookie)
> - `man ss`, `man tcpdump`, `man 7 ip`, `man 7 tcp`

> **Repositori:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Materi edukasi dan lab di sistem milik sendiri, tanpa PoC flood atau eksploit.
