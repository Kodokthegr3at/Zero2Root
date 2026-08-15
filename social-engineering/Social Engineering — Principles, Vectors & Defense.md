# 🎭 Social Engineering — Principles, Attack Vectors & Defense

> **LearnCybersecurity** | Human Element & Social Engineering Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Psychology & Principles | 6 Prinsip Persuasi Cialdini | Psychological Triggers & Cialdini's Laws | 心理誘導の原則（ロバート・チャルディーニ） |
| 2 | Pretexting & Elicitation | Skenario rekayasa & teknik elisitasi | Pretexting Frameworks & Elicitation | プリテキスティングと情報引き出し技術 |
| 3 | Phishing Taxonomy | Spear Phishing, Vishing, Quishing | Phishing, Spear Phishing, Vishing & Quishing | フィッシング、スピアフィッシング、ビッシング |
| 4 | AiTM Phishing (MFA Bypass)| Evilginx2 & pencurian session cookie | Adversary-in-the-Middle (AiTM) & MFA Bypass | AiTM（Evilginx2）によるMFA回避とセッション強奪 |
| 5 | Physical Infiltration | Tailgating, RFID Cloner, BadUSB | Physical Infiltration, RFID & BadUSB | 物理侵入、RFID複製、BadUSB攻撃 |
| 6 | Defense & FIDO2 | Program kesadaran & autentikasi FIDO2 | Security Culture & Phishing-Resistant MFA | セキュリティ文化の醸成とFIDO2ハードウェア認証 |
| 7 | Cheatsheet | Referensi cepat skenario & mitigasi | Social Engineering Assessment Cheatsheet | ソーシャルエンジニアリング診断チートシート |

---

## 1. 🧠 Robert Cialdini's 6 Principles of Influence

### 🇮🇩 Bahasa Indonesia
Sosial engineering mengeksploitasi celah psikologis manusia (*human vulnerability*) daripada kerentanan perangkat lunak. Dr. Robert Cialdini merumuskan 6 prinsip psikologis utama yang sering dimanipulasi oleh penyerang:

1. **Authority (Otoritas)**: Manusia cenderung patuh pada figur otoritas (Direktur, IT Helpdesk, Polisi, Pengacara).
2. **Urgency / Fear (Urgensi & Ketakutan)**: Menimbulkan kepanikan agar korban bertindak cepat tanpa berpikir kritis (*"Akun Anda akan dibekukan dalam 10 menit!"*).
3. **Social Proof (Bukti Sosial)**: Manusia mengikuti perilaku mayoritas (*"Semua rekan tim di divisi Anda sudah menandatangani formulir ini"*).
4. **Scarcity (Kelangkaan)**: Menawarkan peluang yang terbatas (*"Hanya tersisa 2 voucher bonus"*).
5. **Reciprocity (Timbal Balik)**: Memberikan bantuan atau hadiah kecil terlebih dahulu untuk memicu rasa sungkan atau kewajiban membalas budi.
6. **Liking / Sympathy (Ketertarikan & Simpati)**: Membangun rapport persahabatan, pujian, atau berpura-pura membutuhkan pertolongan mendesak.

### 🇬🇧 English
Social engineering targets cognitive vulnerabilities in the human mind rather than algorithmic flaws in code. Dr. Robert Cialdini codified 6 fundamental psychological triggers weaponized by social engineers:

1. **Authority**: Deeply conditioned compliance towards perceived figures of authority (CEOs, Law Enforcement, Enterprise IT Support).
2. **Urgency & Fear**: Artificially manufacturing panic to bypass rational cognitive deliberation (*"Your corporate account will be permanently terminated within 10 minutes!"*).
3. **Social Proof**: Conformity bias where targets mirror perceived group consensus (*"The rest of your department has already verified their credentials"*).
4. **Scarcity**: Leveraging fear of missing out (FOMO) regarding limited corporate bonuses or critical security patches.
5. **Reciprocity**: Offering an unsolicited favor or assistance to induce a subconscious psychological obligation to return the favor.
6. **Liking & Rapport**: Establishing immediate interpersonal charisma, compliments, or feigned distress to foster compliance.

### 🇯🇵 日本語
ソーシャルエンジニアリングは、ソフトウェアの脆弱性ではなく人間の認知バイアス（心理的脆弱性）を突く攻撃手法です。ロバート・チャルディーニ博士が提唱した6つの影響力の武器が悪用されます：

1. **権威（Authority）**: 役員、警察、システム管理者などの権威者に対する無条件の服従傾向。
2. **緊急性・恐怖（Urgency / Fear）**: 思考時間を奪い衝動的な行動を促す圧力（「10分以内に対応しないとアカウントが削除されます」）。
3. **社会的証明（Social Proof）**: 「他の社員は全員手続きを完了しています」という同調圧力。
4. **希少性（Scarcity）**: 限定性や特別感を演出して行動を促す。
5. **返報性（Reciprocity）**: 先に小さな親切や情報を提供し、相手に借りを返したいという心理を抱かせる。
6. **好意（Liking）**: 親近感、褒め言葉、または困っている姿を見せて同情を引く。

```
┌─────────────────────────────────────────────────────────────┐
│                 6 PRINCIPLES OF PERSUASION                  │
├─────────────────┬───────────────────────────────────────────┤
│ 1. Authority    │ Meniru figur bos, aparat hukum, atau IT   │
│ 2. Urgency      │ "Akun Anda diblokir dalam 15 menit!"      │
│ 3. Social Proof │ "Semua karyawan divisi keuangan sudah..." │
│ 4. Scarcity     │ "Hanya tersisa 3 kupon bonus!"            │
│ 5. Reciprocity  │ Memberi bantuan kecil untuk memicu balasan│
│ 6. Liking       │ Membangun koneksi personal & pujian       │
└─────────────────┴───────────────────────────────────────────┘
```

---

## 2. 🎭 Pretexting Frameworks & Information Elicitation

### 🇮🇩 Bahasa Indonesia
**Pretexting** adalah seni menciptakan skenario atau identitas palsu yang meyakinkan untuk memanipulasi target agar memberikan data rahasia.

**Teknik Elisitasi Informasi (Information Elicitation)**:
- **Artificial Ignorance (Berpura-pura Bodoh)**: Sengaja memberikan pernyataan teknis yang salah secara percaya diri, memicu target untuk mengoreksi dan membeberkan konfigurasi arsitektur jaringan internal yang sebenarnya.
- **Ego Baiting**: Memuji keahlian target secara berlebihan sehingga target membanggakan detail rahasia proyek internal perusahaan.
- **Mutual Ground**: Menggunakan jargon internal perusahaan (yang diperoleh sebelumnya dari OSINT LinkedIn/GitHub) agar dianggap sebagai rekan satu perusahaan.

---

## 3. 🎣 Modern Phishing Taxonomy

| Vector | Description / Mekanisme | Defense / Mitigasi |
|:---|:---|:---|
| **Spear Phishing** | Email tertarget tinggi yang dipersonalisasi dengan data pribadi/profesional korban. | DMARC/DKIM/SPF, AI Email Gateways |
| **Whaling / BEC** | Penipuan email yang meniru CEO/CFO untuk memicu transfer dana miliaran rupiah. | Verifikasi telepon dua pihak wajib |
| **Vishing (Voice)** | Panggilan suara penipuan menggunakan **AI Voice Cloning** (Deepfake suara bos). | Challenge questions berbasis out-of-band |
| **Smishing (SMS)** | Pesan SMS/WhatsApp dengan tautan credential harvester atau malware perbankan APK. | Filtering SMS operator, App blocker |
| **Quishing (QR)** | Kode QR fisik/email yang mengarahkan korban ke situs login palsu (Bypass filter email teks). | QR code scanner with URL preview |

---

## 4. 🥷 Adversary-in-the-Middle (AiTM) Phishing & MFA Bypass (Evilginx2)

### 🇮🇩 Bahasa Indonesia
Phishing tradisional yang hanya mencuri username dan password telah gagal jika korban mengaktifkan **MFA (Multi-Factor Authentication)** berbasis SMS atau OTP Authenticator App.

**AiTM Phishing (Evilginx2)** memposisikan dirinya sebagai proxy transparan di antara Korban dan Server Asli (Microsoft 365, Google, Okta):
1. Korban membuka link phishing (`login.attacker-m365.com`).
2. Evilginx2 meneruskan request ke Microsoft asli dan menampilkan halaman login asli secara real-time.
3. Korban memasukkan username, password, dan kode OTP MFA 6-digit.
4. Microsoft memvalidasi OTP dan menerbitkan **Session Cookie otentikasi (`ESTSAUTH`, `SignInStateCookie`)**.
5. Evilginx2 menangkap session cookie tersebut dan menyimpannya di log penyerang.
6. **Penyerang mengimpor cookie ke browser mereka dan login sebagai korban tanpa perlu memasukkan password atau OTP lagi!**

```
Victim Browser ───> [ Evilginx2 Reverse Proxy ] ───> [ Real Microsoft 365 ]
                         │                                    │
                         │ (Steals ESTSAUTH Session Cookie!)   │
                         ▼                                    ▼
                 [ Attacker Machine ]                [ User Authenticated ]
```

---

## 5. 🚪 Physical Infiltration & Hardware Implants

1. **Tailgating / Piggybacking**: Mengikuti karyawan resmi masuk ke area terbatas tanpa memindai kartu akses (misal dengan membawa nampan kopi di kedua tangan).
2. **RFID / NFC Cloning (Proxmark3 / Flipper Zero)**: Membaca ID kartu RFID 125kHz (HID Prox) atau 13.56MHz (MIFARE Classic) milik karyawan dari jarak dekat di lift/kafe dan menduplikasikannya ke kartu kosong dalam 2 detik.
3. **BadUSB / Rubber Ducky**: Perangkat USB yang menyamar sebagai keyboard HID. Saat ditancapkan, ia mengetik 1000 karakter per detik untuk membuka PowerShell dan mengunduh reverse shell.

---

## 6. 🛡️ Enterprise Defense: Phishing-Resistant MFA (FIDO2)

### 🇮🇩 Bahasa Indonesia
Satu-satunya pertahanan permanen yang **100% kebal terhadap serangan Evilginx2 / AiTM Phishing** adalah **FIDO2 / WebAuthn Hardware Security Keys (seperti YubiKey)**:
- Browser secara otomatis mengikat (*cryptographic binding*) proses autentikasi ke nama domain asal (*origin URL*).
- Kunci hardware menolak menandatangani respons tantangan jika URL pada address bar adalah `login.attacker-m365.com` bukan `login.microsoftonline.com` asli!

---

> 📚 **References & Book Sources:**
> - Christopher Hadnagy — *Social Engineering: The Science of Human Hacking (2nd Edition)* (`~/Documents/Books/CyberSec/Social Engineering/`)
> - Kevin Mitnick — *The Art of Deception: Controlling the Human Element of Security* (`~/Documents/Books/CyberSec/Social Engineering/`)
> - Joe Gray — *Practical Social Engineering: A Primer for the Ethical Hacker* (`~/Documents/Books/CyberSec/Social Engineering/`)
> - Peter Kim — *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
