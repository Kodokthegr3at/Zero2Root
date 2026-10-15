# OSINT: Framework & Teknik Open Source Intelligence

> **LearnCybersecurity** | Seri Intelligence & Reconnaissance
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: buku pegangan Bazzell / komunitas & *Open Source Intelligence Methods and Tools*, `~/Documents/Books/CyberSec/OSINT/`
> Catatan: hanya sumber legal dan publik; hormati hukum, ToS, dan etika investigasi.

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-069` | **Fase 7:** Specialized
> **Estimasi belajar:** 5 jam | **Level:** Intermediate
> **Prasyarat:** LC-058
> **Peta buku:** Akhgar et al., Open Source Intelligence Methods and Tools
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Apa itu OSINT (dan apa yang bukan)
2. Siklus intelijen
3. Perencanaan & arahan: pertanyaan yang baik
4. Disiplin koleksi (sumber legal)
5. Pemrosesan & analisis
6. Geolokasi sebagai keterampilan verifikasi
7. OPSEC untuk investigator
8. Sock puppet: peringatan etika
9. Batas hukum & etika
10. Cheatsheet workflow

---

## 1. Apa itu OSINT (dan apa yang bukan)

Open Source Intelligence (OSINT) adalah intelijen yang dikumpulkan dari informasi yang tersedia secara publik dan sah, lalu diproses menjadi insight yang bisa ditindaklanjuti.

```text
kumpulkan (sumber publik yang legal) → olah → analisis → bagikan hasilnya
```

| Termasuk OSINT | Bukan OSINT |
|:---|:---|
| Berita, situs resmi, filing perusahaan | Mengakses akun tanpa izin |
| Metadata yang dipublikasikan | Hacking / phishing untuk mendapatkan data |
| Citra satelit/peta publik | Melanggar paywall dengan kredensial curian |
| Postingan publik | Doxxing / pelecehan |

Kualitas OSINT lebih ditentukan oleh tradecraft daripada "tool rahasia": pertanyaan yang jelas, kritik sumber, korelasi, dan dokumentasi. Tool berganti-ganti, tapi siklus intelijen tidak berubah.

---

## 2. Siklus intelijen

```
        ┌──────────── Direction / Requirements ────────────┐
        │                                                  │
        ▼                                                  │
   Collection ──▶ Processing ──▶ Analysis ──▶ Dissemination ┘
        ▲                         │
        └────── Feedback / gaps ──┘
```

| Fase | Pertanyaan kunci | Output |
|:---|:---|:---|
| Direction | Apa yang harus dijawab? Siapa konsumennya? | PIR (Priority Intelligence Requirements) |
| Collection | Sumber mana yang legal dan relevan? | Raw data + provenance |
| Processing | Bagaimana menormalkan dan menyimpan? | Dataset terstruktur |
| Analysis | Apa yang bermakna / masih tidak pasti? | Assessment + confidence |
| Dissemination | Bagaimana melapor tanpa overclaim? | Report / brief |
| Feedback | Apa yang masih bolong? | PIR baru |

### Bahasa confidence (disiplin)

Hindari absolutisme. Gunakan skala:

```text
tingkat keyakinan:  rendah  /  sedang  /  tinggi
```

Pisahkan dengan jelas antara fakta yang teramati dan inferensi.

---

## 3. Perencanaan & arahan: pertanyaan yang baik

PIR yang buruk: "Cari semua tentang X."

PIR yang baik:

1. Apakah organisasi X mengoperasikan ASN / rentang IP publik sendiri?
2. Domain mana yang terhubung ke merek X menurut data publik WHOIS/CT logs?
3. Apakah ada lowongan pekerjaan yang mengungkap stack teknologi mereka (OSINT teknis untuk tujuan defensif)?

PIR (priority intelligence requirement) yang baik itu bisa dijawab, punya tenggat waktu, dan terkait dengan keputusan yang nyata.

Collection plan: sumber → metode → legal check → storage → analyst.

---

## 4. Disiplin koleksi (sumber legal)

### 4.1 Kategori sumber

| Kategori | Contoh | Catatan |
|:---|:---|:---|
| Official | Regulator, filing perusahaan, portal pemerintah | Kredibilitas tinggi; cek pembaruan |
| Media | Berita, wawancara | Mungkin ada bias & kesalahan |
| Technical public | DNS, CT logs, BGP publik, paste publik (cek ToS) | Perhatikan rate-limit; jangan abuse |
| Social / UGC | Postingan publik | Konteks mudah hilang; arsipkan |
| Imagery | Maps, Street View, citra satelit publik | Perhatikan etika untuk lokasi sensitif |
| Academic / papers | Prosiding, preprint | Verifikasi versi |

### 4.2 Catatan provenance (wajib)

Untuk setiap artefak, catat:

```text
URL  |  waktu (UTC)  |  hash  |  siapa yang mengumpulkan  |  tool apa  |  catatan
```

Tanpa provenance, hasil analisis mudah digugat kredibilitasnya.

### 4.3 Kritik sumber

- Siapa penulisnya? Apa insentifnya?
- Apakah ini sumber primer atau sekunder?
- Bisakah dikorelasikan dengan sumber independen lain?

---

## 5. Pemrosesan & analisis

### Processing

- Deduplikasi entity (orang, organisasi, domain, IP).
- Menyusun timeline.
- Normalisasi nama (perhatikan unicode / homoglyph).
- Menandai reliability sumber.

### Pola analisis

| Pola | Deskripsi | Risiko kesalahan |
|:---|:---|:---|
| Link analysis | Menghubungkan antar entity | False friendship / kesamaan nama semu |
| Temporal | Urutan peristiwa | Kesalahan timezone |
| Geospatial | Peta dan bayangan / landmark | Confirmation bias |
| Technical correlation | DNS ↔ sertifikat ↔ hosting | Noise dari shared hosting |

```
Raw captures
    │
    ▼
Structured entities (graph)
    │
    ▼
Hypotheses H1..Hn
    │
    ├─ corroborate
    └─ falsify
         │
         ▼
Assessment + confidence + gaps
```

### Template output (ringkas)

1. BLUF (bottom line up front)
2. Key judgments
3. Ringkasan bukti (dengan link/hash)
4. Alternatif yang dipertimbangkan
5. Gaps & koleksi lanjutan

---

## 6. Geolokasi sebagai keterampilan verifikasi

Geolokasi dalam OSINT berarti memverifikasi klaim lokasi dari foto/video publik, bukan pelacakan yang mengarah ke harassment.

### Teknik konsep (verifikasi, bukan serangan)

| Sinyal | Cara pakai |
|:---|:---|
| Landmark | Mencocokkan siluet bangunan dengan peta publik |
| Signage / bahasa | Petunjuk negara/kota |
| Matahari / bayangan | Estimasi kasar waktu/arah |
| Vegetasi / iklim | Konsistensi regional |
| Infrastruktur | Tiang listrik, marka jalan, posisi setir kiri/kanan |
| EXIF (jika ada) | Hanya jika metadata masih tertanam dan aksesnya legal |

Anggap klaim lokasi terkonfirmasi hanya jika minimal dua petunjuk yang saling independen menunjukkan hal yang sama.

Etika: jangan publikasikan alamat rumah pribadi; jangan doxx. Untuk IR/DFIR internal, ikuti kebijakan privasi organisasi.

---

## 7. OPSEC untuk investigator

Peneliti sendiri juga bisa menjadi target (counter-OSINT).

| Risiko | Mitigasi |
|:---|:---|
| Kebocoran identitas asli | Pisahkan identitas kerja investigasi dari identitas pribadi |
| Fingerprinting browser | Profil terpisah; batasi ekstensi |
| Kebocoran lokasi geografis | VPN/kebijakan organisasi; jangan campur dengan akun pribadi |
| Dokumen berbahaya | Gunakan sandbox; jangan aktifkan makro sembarangan |
| Surveillance balik dari target | Jangan unggah bukti ke platform sembarangan |

```
Personal life  ≠  Investigation workspace
     │                    │
   private            logged, policy-bound, legal
```

OPSEC dalam satu kalimat:

makin sering kamu memakai identitas, perangkat, metode pembayaran, atau gaya bahasa yang sama di berbagai investigasi, makin mudah kamu dilacak.

Minimalkan penggunaan ulang identitas antar konteks.

---

## 8. Sock puppet: peringatan etika

Sock puppet adalah akun persona yang dipakai untuk pengumpulan data. Dalam banyak konteks profesional:

| Status | Pandangan |
|:---|:---|
| Akademik / hobi | Sering melanggar ToS platform |
| Penegak hukum / intel resmi | Diatur oleh kebijakan dan hukum yang ketat |
| Bug bounty / pentest | Biasanya di luar scope tanpa izin eksplisit |
| Wartawan | Terikat kode etik dan hukum lokal |

### Peringatan keras

- Jangan gunakan persona untuk mengelabui individu rentan, grooming, atau penipuan.
- Jangan memanen data di balik login yang memerlukan identitas palsu jika itu melanggar hukum atau ToS.
- Lebih baik memakai sumber yang benar-benar publik tanpa autentikasi tipuan.
- Jika organisasi Anda mengizinkan pemakaian persona, dokumentasikan approval, batasan, dan kebijakan retensi datanya.

Catatan ini tidak memberikan resep untuk membuat persona demi menyusup ke komunitas tertentu. Fokusnya adalah menjelaskan mengapa hal itu berisiko secara hukum dan etika, serta bagaimana menghindari ketergantungan padanya.

---

## 9. Batas hukum & etika

| Batas | Praktik |
|:---|:---|
| Hukum akses komputer | Jangan bypass kontrol akses |
| Privasi (gaya GDPR) | Minimalkan data; tujuan jelas; retensi terbatas |
| ToS platform | Automation yang agresif bisa melanggar kontrak |
| Hak cipta | Jangan redistribusi konten yang dilindungi secara massal |
| Keselamatan | Jangan doxx; jangan publikasikan PII yang sensitif |
| Tempat kerja | Ikuti RoE (rules of engagement) dan arahan bagian hukum |

Uji cepat etika:

```text
1. Apakah saya nyaman kalau ini dipublikasikan?
2. Apakah saya bisa mempertanggungjawabkannya di pengadilan?
3. Apakah ini cara yang paling sedikit merugikan?
```

Jika salah satu jawabannya "tidak," berhenti dan minta review hukum.

---

## 10. Cheatsheet workflow

```text
1. Tulis PIR (1–3 pertanyaan)
2. Legal check: publik? ToS? yurisdiksi?
3. Collect dengan provenance (URL, UTC, hash)
4. Process → entity graph + timeline
5. Analyze → judgments + confidence + alternatives
6. Report BLUF; tandai gaps
7. Reduce data; store per retention policy
8. Review OPSEC investigator
```

| Kebutuhan | Arah koleksi publik (contoh kelas) |
|:---|:---|
| Domain footprint | DNS history publik, CT logs |
| Struktur organisasi | Filing perusahaan, press, halaman karier |
| Petunjuk infrastruktur | Lowongan kerja, dokumentasi cloud publik, status page |
| Konteks insiden | Advisory vendor, timeline publik |
| Verifikasi gambar | Maps + korroborasi landmark |

---

## Catatan keamanan: ancaman & pertahanan

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Investigator di-dox | Counter-OSINT | Persona/device terpisah (sesuai kebijakan) |
| Sumber yang diracuni | Disinformasi / kebocoran palsu | Korroborasi multi-sumber |
| Overcollection | Menimbun PII | Minimalisasi + kebijakan retensi |
| Pelanggaran ToS / hukum | Scraping yang agresif | Pakai API manual/publik; konsultasi hukum |
| Bias cascade | Melihat apa yang ingin dilihat | Red-team hipotesis sendiri |
| Penanganan tidak aman | File berbahaya | Analisis di sandbox |

Yang tidak dibahas: bypass paywall dengan kredensial curian, hacking akun, malware untuk koleksi data, atau playbook doxxing.

---

> **Referensi & sumber buku**
> - *Open Source Intelligence Methods and Tools*, `~/Documents/Books/CyberSec/OSINT/`
> - Tradecraft publik: siklus intelijen (bahasa confidence gaya ICD), kritik sumber
> - Kebijakan platform & undang-undang kejahatan komputer/privasi lokal (selalu cek hukum yang berlaku saat ini)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Hanya OSINT yang legal dan etis. Bukan lisensi untuk menyusupi sistem atau orang.
