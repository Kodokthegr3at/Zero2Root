# 🔎 OSINT — Open Source Intelligence Framework & Techniques

> **LearnCybersecurity** | Intelligence & Reconnaissance Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Bazzell / community handbooks & *Open Source Intelligence Methods and Tools* — `~/Documents/Books/CyberSec/OSINT/`  
> ⚠️ Hanya sumber **legal & publik**; hormati hukum, ToS, dan etika investigasi.

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-069` | **Phase 7:** Specialized  
> **Est. study:** 5h | **Level:** Intermediate  
> **Prerequisites:** LC-058  
> **Book map:** Akhgar et al. Â Open Source Intelligence Methods and Tools
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | What is OSINT | Definisi & batas | OSINT definition | OSINTとは |
| 2 | Intelligence Cycle | Siklus intelijen | Intel cycle | インテリジェンス循環 |
| 3 | Planning & Direction | Perencanaan | Planning | 計画 |
| 4 | Collection Disciplines | Koleksi legal | Collection | 合法的収集 |
| 5 | Processing & Analysis | Olah & analisis | Process & analyze | 処理と分析 |
| 6 | Geolocation Skills | Verifikasi lokasi | Geolocation verify | 位置検証 |
| 7 | OPSEC for Investigators | OPSEC peneliti | Investigator OPSEC | 調査側OPSEC |
| 8 | Sock Puppets Ethics | Persona & etika | Sock puppet ethics | ソックパペット倫理 |
| 9 | Legal & Ethical Bounds | Hukum & etika | Legal bounds | 法的境界 |
| 10 | Cheatsheet | Workflow cepat | Workflow sheet | チートシート |

---

## 1. 📘 What OSINT Is (and Is Not)

### 🇮🇩 Bahasa Indonesia
**Open Source Intelligence (OSINT)** adalah intelijen yang dikumpulkan dari informasi **tersedia secara publik / sah** lalu diproses menjadi insight yang dapat ditindaklanjuti.

$$
\mathsf{OSINT} = \mathsf{Collect}_{\text{legal public}} \rightarrow \mathsf{Process} \rightarrow \mathsf{Analyze} \rightarrow \mathsf{Disseminate}
$$

| OSINT | Bukan OSINT |
|:---|:---|
| Berita, situs resmi, filings | Akses akun tanpa izin |
| Metadata yang dipublikasikan | Hack / phishing untuk data |
| Satelit/peta publik | Melanggar paywall dengan credential curian |
| Postingan publik | Doxxing / pelecehan |

### 🇬🇧 English
OSINT quality depends less on “secret tools” and more on **tradecraft**: clear questions, source criticism, correlation, and documentation. Tools change; the intelligence cycle does not.

### 日本語
OSINTの本質はツール名ではなく、問い・批判的検証・相関・文書化です。

---

## 2. 🔄 The Intelligence Cycle

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
| **Direction** | Apa yang harus dijawab? Siapa konsumen? | PIR (Priority Intelligence Requirements) |
| **Collection** | Sumber mana yang legal & relevan? | Raw data + provenance |
| **Processing** | Bagaimana menormalkan & menyimpan? | Structured dataset |
| **Analysis** | Apa yang berarti / tidak pasti? | Assessment + confidence |
| **Dissemination** | Bagaimana melapor tanpa overclaim? | Report / brief |
| **Feedback** | Apa yang masih bolong? | New PIRs |

### Confidence language (disiplin)
Hindari absolutisme. Gunakan skala:

$$
\mathsf{Confidence} \in \{\mathsf{low},\;\mathsf{moderate},\;\mathsf{high}\}
$$

serta pisahkan **fakta teramati** vs **inferensi**.

---

## 3. 🎯 Planning & Direction — Good Questions

PIR yang buruk: “Cari semua tentang X.”  
PIR yang baik:

1. Apakah organisasi $X$ mengoperasikan ASN / rentang IP publik sendiri?
2. Domain mana yang terhubung ke merek $X$ menurut WHOIS/CT logs (data publik)?
3. Apakah ada lowongan yang mengungkapkan stack teknologi (OSINT teknis defensif)?

$$
\mathsf{GoodPIR} \iff \mathsf{Answerable} \land \mathsf{TimeBound} \land \mathsf{DecisionLinked}
$$

**Collection plan:** sumber → metode → legal check → storage → analyst.

---

## 4. 📚 Collection Disciplines (Legal Sources)

### 4.1 Kategori sumber
| Kategori | Contoh | Catatan |
|:---|:---|:---|
| **Official** | Regulator, company filings, gov portals | Tinggi kredibilitas; cek update |
| **Media** | Berita, wawancara | Bias & kesalahan mungkin |
| **Technical public** | DNS, CT logs, public BGP, public paste (cek ToS) | Rate-limit; jangan abuse |
| **Social / UGC** | Postingan publik | Konteks mudah hilang; arsipkan |
| **Imagery** | Maps, Street View, satelit publik | Etika lokasi sensitif |
| **Academic / papers** | Prosiding, preprint | Verifikasi versi |

### 4.2 Provenance record (wajib)
Untuk tiap artefak catat:

$$
\langle \mathsf{URL},\; \mathsf{UTC},\; \mathsf{hash},\; \mathsf{collector},\; \mathsf{tool},\; \mathsf{notes} \rangle
$$

Tanpa provenance, analisis mudah digugat.

### 4.3 Source criticism
- Siapa penulisnya? Apa insentifnya?
- Apakah primary atau secondary?
- Apakah bisa dikorelasikan dengan sumber independen?

---

## 5. 🧪 Processing & Analysis

### Processing
- Deduplikasi entity (orang, org, domain, IP).
- Timeline construction.
- Normalisasi nama (unicode / homoglyph awareness).
- Tag reliability.

### Analysis patterns
| Pola | Deskripsi | Risiko kesalahan |
|:---|:---|:---|
| Link analysis | Hubungkan entity | False friendship / homonym |
| Temporal | Urutan peristiwa | Timezone mistakes |
| Geospatial | Peta & bayangan / landmark | Confirmation bias |
| Technical correlation | DNS ↔ cert ↔ hosting | Shared hosting noise |

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

### Output template (ringkas)
1. Bluf (bottom line up front)  
2. Key judgments  
3. Evidence summary (with links/hashes)  
4. Alternatives considered  
5. Gaps & next collection  

---

## 6. 🗺️ Geolocation as a Verification Skill

Geolocation OSINT = **verifikasi klaim lokasi** dari foto/video publik, bukan pelacakan harassive.

### Teknik konsep (defense / verification)
| Sinyal | Cara dipakai |
|:---|:---|
| Landmark | Cocokkan siluet bangunan dengan peta publik |
| Signage / language | Petunjuk negara/kota |
| Sun / shadow | Estimasi waktu/arah (kasar) |
| Vegetation / climate | Konsistensi regional |
| Infrastructure | Tiang listrik, marka jalan, setir kiri/kanan |
| EXIF (jika ada) | Hanya jika metadata masih tertanam & legal diakses |

$$
\mathsf{LocationClaim} \models \mathsf{Corroborated}
\iff \ge 2\ \mathsf{IndependentSignals}\ \mathsf{agree}
$$

**Etika:** jangan publikasikan alamat rumah pribadi; jangan doxx. Untuk IR/DFIR internal, ikuti kebijakan privasi organisasi.

---

## 7. 🛡️ OPSEC for Investigators

Peneliti juga bisa menjadi target (counter-OSINT).

| Risiko | Mitigasi |
|:---|:---|
| Kebocoran identitas nyata | Pisahkan identitas kerja investigasi |
| Fingerprinting browser | Profil terpisah; batasi ekstensi |
| Geo leak | VPN/policy org; jangan campur akun personal |
| Malicious documents | Sandbox; jangan aktifkan makro sembarangan |
| Opposing surveillance | Jangan unggah bukti ke platform acak |

```
Personal life  ≠  Investigation workspace
     │                    │
   private            logged, policy-bound, legal
```

**OPSEC formula (intuisi):**

$$
\mathsf{Exposure} \propto \mathsf{Reuse}(\mathsf{Identity},\;\mathsf{Device},\;\mathsf{Payment},\;\mathsf{LanguageHabits})
$$

Minimalkan reuse antar konteks.

---

## 8. 🧦 Sock Puppets — Ethics Warning

**Sock puppet** = akun persona untuk pengumpulan. Di banyak konteks profesional:

| Status | Pandangan |
|:---|:---|
| Akademik / hobi | Sering melanggar ToS platform |
| LE / intel resmi | Diatur kebijakan & hukum ketat |
| Bug bounty / pentest | Biasanya **di luar scope** tanpa izin eksplisit |
| Wartawan | Kode etik & hukum lokal |

### Peringatan keras
- Jangan gunakan persona untuk mengelabui individu rentan, grooming, atau penipuan.
- Jangan panen data di balik login yang memerlukan identitas palsu jika melanggar hukum/ToS.
- Prefer **sumber benar-benar publik** tanpa autentikasi tipuan.
- Jika organisasi Anda mengizinkan persona: dokumentasikan approval, batasan, dan retensi data.

> Catatan ini **tidak** memberi resep membuat persona untuk penyusupan komunitas. Fokus: mengapa berisiko secara hukum/etika dan bagaimana menghindari ketergantungan padanya.

---

## 9. ⚖️ Legal & Ethical Bounds

| Batas | Praktik |
|:---|:---|
| Hukum akses komputer | Jangan bypass kontrol akses |
| Privasi / GDPR-like | Minimasi data; tujuan jelas; retensi terbatas |
| ToS platform | Automation agresif bisa melanggar kontrak |
| Copyright | Jangan redistribusi konten dilindungi secara massal |
| Safety | Jangan doxx; jangan publikasikan PII sensitif |
| Workplace | Ikuti RoE & counsel |

**Uji cepat etika:**

$$
\mathsf{WouldPublish?} \land \mathsf{WouldDefendInCourt?} \land \mathsf{LeastHarm?}
$$

Jika salah satu “tidak,” berhenti dan minta review hukum.

---

## 10. 🛠️ Workflow Cheatsheet

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
| Org structure | Filings, press, career pages |
| Infra hints | Job posts, public cloud docs, status pages |
| Incident context | Vendor advisories, public timelines |
| Image verify | Maps + landmark corroboration |

---

## 🔐 Security Notes — Threats & Defenses

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Investigator dox | Counter-OSINT | Segregated personas/devices (policy) |
| Poisoned sources | Disinfo / fake leaks | Multi-source corroboration |
| Overcollection | Hoarding PII | Minimasi + retention |
| ToS / legal breach | Aggressive scraping | Manual/public APIs; counsel |
| Bias cascade | Seeing what you want | Red team the hypothesis |
| Unsafe handling | Malicious files | Sandbox analysis |

> **Tidak dibahas:** bypass paywall dengan kredensial curian, hacking akun, malware untuk koleksi, atau doxxing playbook.

---

> 📚 **References & Book Sources**
> - *Open Source Intelligence Methods and Tools* — `~/Documents/Books/CyberSec/OSINT/`
> - Tradecraft publik: intelligence cycle (ICD-style confidence language), source criticism
> - Platform policies & local computer-crime / privacy statutes (always check current law)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ OSINT legal & etis saja. Bukan lisensi untuk menyusupi sistem atau orang.
