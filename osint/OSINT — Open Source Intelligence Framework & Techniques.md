# 🌐 OSINT — Open Source Intelligence Framework & Techniques

> **LearnCybersecurity** | Intelligence & Reconnaissance Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | OSINT Cycle | Siklus intelijen 6 tahap | The 6-Phase Intelligence Lifecycle | OSINTインテリジェンスサイクル |
| 2 | OPSEC & Personas | Anonimitas, sock puppets, VPN/Tor | Researcher OPSEC & Sock Puppets | 調査員のOPSEC（運用セキュリティ） |
| 3 | Domain & Infrastructure | Rekon domain, IP, BGP & CDN | Infrastructure, DNS & ASN Reconnaissance | ドメイン・インフラ・ASN調査 |
| 4 | SOCMINT & People | SOCMINT, username & geolokasi | Social Media Intelligence & Geolocation | 人物調査・SOCMINT・画像位置特定 |
| 5 | Threat Intel & Breaches | Database kebocoran data & DeHashed | Breach Databases, Leaks & Threat Intel | 漏洩データベースと脅威インテリジェンス |
| 6 | Automated Frameworks | Recon-ng, SpiderFoot, theHarvester | Automated OSINT Tool Suites | OSINT自動化フレームワーク |
| 7 | Cheatsheet | Referensi cepat tool & link OSINT | Comprehensive OSINT Cheatsheet | OSINTツール・コマンドチートシート |

---

## 1. 🔄 The 6-Phase OSINT Intelligence Cycle

### 🇮🇩 Bahasa Indonesia
**Open Source Intelligence (OSINT)** adalah proses pengumpulan, pemrosesan, dan analisis data yang tersedia secara publik dari berbagai sumber terbuka untuk menghasilkan intelijen yang dapat ditindaklanjuti (*actionable intelligence*). OSINT mengikuti siklus terstruktur 6 tahap:

1. **Planning & Direction**: Menentukan tujuan investigasi, batasan ruang lingkup, dan persyaratan OPSEC.
2. **Collection**: Mengumpulkan data mentah secara sistematis dari mesin pencari, media sosial, domain registry, sertifikat SSL, dan arsip publik.
3. **Processing**: Membersihkan, menyaring, mendekode, dan menormalkan data ke dalam format terstruktur.
4. **Analysis & Production**: Menghubungkan titik-titik informasi (*correlation*), mengidentifikasi pola, dan membangun peta relasi antar-entitas.
5. **Dissemination**: Menyajikan laporan temuan intelijen dalam bentuk dokumen teknis atau visualisasi grafik.
6. **Feedback**: Mengevaluasi keakuratan intelijen dan menyempurnakan strategi pengumpulan data berikutnya.

### 🇬🇧 English
**Open Source Intelligence (OSINT)** is the systematic discipline of collecting, processing, and analyzing publicly available information from overt sources to produce actionable intelligence. OSINT follows a rigorous 6-phase lifecycle:

1. **Planning & Direction**: Defining objectives, scope boundaries, legal considerations, and strict OPSEC posture.
2. **Collection**: Systematically harvesting raw data from search engines, social networks, DNS registries, SSL transparency logs, and public archives.
3. **Processing**: Sanitizing, decoding, deduplicating, and formatting collected data into structured tables or graphs.
4. **Analysis & Production**: Correlating data points, synthesizing intelligence, and identifying underlying adversary infrastructure or personnel patterns.
5. **Dissemination**: Publishing structured technical reports and relational entity graphs.
6. **Feedback**: Evaluating intelligence fidelity and updating investigative requirements.

### 🇯🇵 日本語
**OSINT（オープンソース・インテリジェンス）**は、公開されている合法的な情報源（検索エンジン、SNS、DNSレコード、証明書ログなど）からデータを収集・処理・分析し、実用的なインテリジェンスを導き出す手法です。6つの段階からなる標準サイクルに従います：

1. **計画と方針決定**: 調査対象、範囲、法的制約、およびOPSEC（運用セキュリティ）要件の策定。
2. **情報収集**: 公開ソースからの系統的な生データ収集。
3. **データ処理**: データの正規化、重複排除、構造化。
4. **分析と統合**: データの関連付け、パターン認識、相関関係の可視化。
5. **報告と共有**: 構造化されたレポートやグラフによる調査結果の提供。
6. **評価とフィードバック**: インテリジェンスの正確性評価と収集計画の改善。

```
  ┌────────────────────────────────────────────────────────┐
  │                 OSINT INTELLIGENCE CYCLE               │
  ├───────────────────┬────────────────────────────────────┤
  │ 1. Planning       │ Menentukan sasaran, batasan, OPSEC │
  │ 2. Collection     │ Mengumpulkan raw data dari web     │
  │ 3. Processing     │ Normalisasi data, decoding, filter │
  │ 4. Analysis       │ Menghubungkan pola, korelasi graph │
  │ 5. Dissemination  │ Laporan intelijen terstruktur      │
  │ 6. Feedback       │ Evaluasi akurasi hasil intelijen   │
  └───────────────────┴────────────────────────────────────┘
```

---

## 2. 🥷 Researcher OPSEC & Sock Puppet Architecture

### 🇮🇩 Bahasa Indonesia
Investigator OSINT wajib menjaga **Operational Security (OPSEC)** agar jejak digital pribadi tidak bocor ke target yang sedang diinvestigasi:
- **Sock Puppets (Identitas Anonim)**: Profil media sosial buatan yang memiliki riwayat kredibel, email burner, nomor virtual VoIP (bukan nomor pribadi), dan foto profil wajah hasil AI (*Generated Photos* / *ThisPersonDoesNotExist*).
- **Environment Isolation**: Menggunakan dedicated virtual machine (Whonix / Tails) dengan browser bersih tanpa ekstensi personal, dipasangkan dengan multi-hop VPN atau jaringan Tor.
- **Canary & Fingerprint Prevention**: Jangan pernah mengeklik tautan yang dikirim langsung oleh target tanpa sandbox, untuk mencegah *IP grabber* atau browser fingerprinting (Canvas/WebGL).

---

## 3. 🌍 Infrastructure, DNS & ASN Reconnaissance

```bash
# ── WHOIS & ASN EXPLORATION ──────────────────────────────────
whois target.com
whois -h whois.radb.net -- "-i origin AS13335" # Temukan IP prefixes milik target ASN

# ── CERTIFICATE TRANSPARENCY SUBDOMAIN DISCOVERY ─────────────
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sort -u

# ── REVERSE IP & SHARED HOSTING LOOKUP ───────────────────────
dig +short target.com
curl -s "https://api.hackertarget.com/reverseiplookup/?q=93.184.216.34"
```

---

## 4. 📸 SOCMINT & Imagery Geolocation (IMINT)

```bash
# ── EXIF METADATA EXTRACTION ─────────────────────────────────
exiftool sample_image.jpg | grep -iE "GPS|Camera|Model|Date|Software"

# ── MULTI-PLATFORM USERNAME RECONNAISSANCE ───────────────────
# Cari username di 300+ media sosial secara paralel
sherlock username_target
maigret username_target --pdf --html
```

- **Reverse Image Search Engines**:
  - **Google Lens**: Kuat untuk produk, landmark, dan lokasi wisata.
  - **Yandex Images**: Algoritma pengenalan wajah (*facial recognition*) dan lanskap paling akurat di industri OSINT.
  - **TinEye**: Melacak kemunculan pertama gambar di internet (*chronological history*).
- **Shadow & Solar Geometry**:
  - Menggunakan **SunCalc.org** untuk menghitung azimuth, panjang bayangan, dan waktu pengambilan foto berdasarkan perkiraan lokasi geografis.

---

## 5. 💥 Breach Databases & Threat Intelligence

- **DeHashed / LeakCheck / HaveIBeenPwned**: Menemukan kredensial yang bocor dari insiden peretasan sebelumnya untuk memetakan password reuse atau format username karyawan.
- **Wayback Machine & Common Crawl**:
  ```bash
  # Ekstraksi seluruh riwayat URL target yang pernah di-crawl di masa lalu
  waybackurls target.com | sort -u > archive_urls.txt
  gau target.com --subs | sort -u > all_urls.txt
  ```

---

## 6. 🛠️ Comprehensive OSINT CLI Cheatsheet

```bash
# ── THEHARVESTER RECONNAISSANCE ──────────────────────────────
theHarvester -d target.com -b google,bing,linkedin,crtsh,virustotal -l 500

# ── RECON-NG FRAMEWORK WORKFLOW ──────────────────────────────
recon-ng
[recon-ng][default] > marketplace install all
[recon-ng][default] > workspaces create TargetAudit
[recon-ng][default][TargetAudit] > modules load recon/domains-hosts/hackertarget
[recon-ng][default][TargetAudit][hackertarget] > options set SOURCE target.com
[recon-ng][default][TargetAudit][hackertarget] > run
[recon-ng][default][TargetAudit][hackertarget] > show hosts

# ── SPIDERFOOT OSINT ENGINE ──────────────────────────────────
# Start local OSINT web GUI
spiderfoot -l 127.0.0.1:5001
```

---

> 📚 **References & Book Sources:**
> - Babak Akhgar et al. — *Open Source Intelligence Methods and Tools* (`~/Documents/Books/CyberSec/OSINT/`)
> - Christopher Hadnagy — *Social Engineering: The Science of Human Hacking (2nd Edition)* (`~/Documents/Books/CyberSec/Social Engineering/`)
> - Peter Kim — *The Hacker Playbook 3: Practical Guide To Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Michael Bazzell — *Open Source Intelligence Techniques (10th Edition)*
> - [OSINT Framework Online Portal](https://osintframework.com/)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
