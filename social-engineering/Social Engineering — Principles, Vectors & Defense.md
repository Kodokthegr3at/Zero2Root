# 🎭 Social Engineering — Principles, Vectors & Defense

> **LearnCybersecurity** | Human Factor Security Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Christopher Hadnagy — *Social Engineering: The Science of Human Hacking*; Kevin Mitnick — *The Art of Deception*; Joe Gray — *Practical Social Engineering*

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-068` | **Phase 7:** Specialized  
> **Est. study:** 4-5h | **Level:** Intermediate  
> **Prerequisites:** LC-058  
> **Book map:** Hadnagy Â Social Engineering 2nd Ed.; Mitnick Â The Art of Deception; Gray Â Practical Social Engineering
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Human Layer | Manusia sebagai permukaan | Human attack surface | 人的攻撃面 |
| 2 | Cialdini Principles | 6(+1) prinsip pengaruh | Influence principles | 影響力の原理 |
| 3 | Attack Narrative | Siklus rekayasa sosial | SE engagement cycle | SEの流れ |
| 4 | Common Vectors | Vektor tipikal | Common vectors | 代表的な経路 |
| 5 | Detection Signals | Sinyal deteksi | Red flags | 検知シグナル |
| 6 | Awareness Training | Program kesadaran | Training program | 啓発訓練 |
| 7 | Organizational Defense | Kontrol organisasi | Org controls | 組織防御 |
| 8 | Ethics & Law | Etika & hukum | Legal ethics | 倫理と法 |
| 9 | Incident Response | Respons insiden SE | SE incident handling | インシデント対応 |
| 10 | Cheatsheet | Kartu cepat defense | Defense cheatsheet | 防御チートシート |

---

## 1. 🧠 The Human Layer as Attack Surface

### 🇮🇩 Bahasa Indonesia
Keamanan teknis dapat dilewati jika penyerang meyakinkan manusia untuk **memberikan akses, rahasia, atau tindakan**. Mitnick (*Art of Deception*) menekankan: orang cenderung membantu, takut konflik, dan percaya pada otoritas yang tampak sah.

$$
\mathsf{Risk}_{SE} = f(\mathsf{Trust},\; \mathsf{Urgency},\; \mathsf{Access},\; \mathsf{VerificationGap})
$$

Semakin besar trust + urgency dan semakin lemah verifikasi, semakin tinggi keberhasilan rekayasa sosial.

### 🇬🇧 English
Social engineering (SE) exploits cognitive biases and organizational process gaps — not (primarily) memory corruption. Defense is process + culture + verification channels, not another firewall rule alone.

### 日本語
ソーシャルエンジニアリングは認知バイアスと業務手順の隙を突きます。防御は技術だけでなく検証文化です。

```
┌──────────────┐     trust / fear / greed      ┌──────────────┐
│  Attacker    │ ─────────────────────────────▶│   Target     │
│  narrative   │◀──── info / access / action ──│   human      │
└──────────────┘                               └──────────────┘
        │                                              │
        └────────── defense: verify out-of-band ───────┘
```

---

## 2. 📐 Cialdini’s Principles of Influence (Defense Lens)

Hadnagy membangun kerangka SE di atas psikologi pengaruh. Pahami prinsip ini **untuk mendeteksi manipulasi**, bukan untuk menyiapkan kampanye tipuan.

| Principle | Intuisi | Contoh manipulasi | Pertahanan |
|:---|:---|:---|:---|
| **Reciprocity** | Hutang budi | “Saya bantu dulu, tolong balas kirim file” | Kebijakan: hadiah ≠ bypass prosedur |
| **Commitment / Consistency** | Konsisten dengan pernyataan awal | “Tadi Anda bilang bisa bantu…” | Izinkan ubah keputusan bila fakta baru |
| **Social proof** | Ikuti orang lain | “Semua staf sudah update lewat link ini” | Verifikasi sumber resmi |
| **Authority** | Patuhi atasan / seragam | “IT Director minta reset sekarang” | Callback ke nomor resmi; dual control |
| **Liking** | Tolong orang yang disukai | Rapport berlebihan + permintaan sensitif | Pisahkan ramah dari otorisasi |
| **Scarcity / Urgency** | Takut kehilangan | “Akun ditutup dalam 15 menit” | SLA: tidak ada aksi sensitif di bawah tekanan waktu palsu |
| **Unity** (ed.) | “Kita satu kelompok” | Identitas palsu komunitas/vendor | Badge + identitas terverifikasi |

### Formalisasi sederhana
$$
\mathsf{Compliance} \uparrow \;\text{when}\; \sum_i w_i \cdot \mathsf{Principle}_i > \mathsf{VerificationFriction}
$$

Defense menaikkan **VerificationFriction** (callback, ticket, dual approval) tanpa menghancurkan produktivitas.

---

## 3. 🔄 Social Engineering Narrative Cycle

Dari *Practical Social Engineering* / Hadnagy (siklus generik, **bukan playbook serangan**):

```
OSINT (publik) → Pretext design → Contact → Rapport → Ask → Exit → Report
```

| Fase | Apa yang terjadi | Kontrol defense |
|:---|:---|:---|
| OSINT | Pengumpulan info publik tentang org/orang | Minimasi jejak publik; privacy training |
| Pretext | Cerita yang “masuk akal” | Challenge story yang minta akses |
| Contact | Email, telepon, tatap muka, chat | Channel resmi + banner peringatan |
| Rapport | Membangun kenyamanan | Waspadai permintaan mendadak setelah basa-basi |
| Ask | Permintaan aksi/info | Never skip verification for “small” asks |
| Exit | Menutup tanpa alarm | Logging & after-action review |
| Report | (Di red team berizin) dokumentasi | Hanya dengan RoE tertulis |

> Catatan keras: repository ini **tidak** mengajarkan setup phishing kit, Evilginx, BadUSB payload, atau skrip penipuan. Fokus: psikologi + deteksi + pelatihan.

---

## 4. 📡 Common Vectors (Konsep)

| Vektor | Deskripsi singkat | Apa yang diminta biasanya |
|:---|:---|:---|
| **Phishing / spear-phishing** | Pesan tipuan bermuatan CTA | Kredensial, malware click, wire change |
| **Vishing** | Telepon / VoIP | Reset password, MFA code, data pelanggan |
| **Smishing** | SMS / chat mobile | Link “paket” / “bank” |
| **Pretexting (helpdesk)** | Meniru karyawan/vendor | Unlock akun, tambah ke VPN group |
| **Impersonation** | Physical / badge surfing | Tailgating, “tamu vendor” |
| **Business Email Compromise (BEC)** | Penyimpangan wire / invoice | Ubah rekening pembayaran |
| **Quid pro quo** | “Saya bantu IT, Anda install…” | Remote access tools |

$$
\mathsf{Impact} = \mathsf{PrivilegeGranted} \times \mathsf{DataSensitivity} \times \mathsf{SpeedOfDetection}^{-1}
$$

---

## 5. 🚩 Detection Signals — Red Flags

### Bahasa / konten
- Urgensi ekstrem + ancaman hukuman.
- Permintaan bypass prosedur (“jangan bilang siapa-siapa”).
- Ketidaksesuaian domain email (homoglyph, subdomain aneh).
- Permintaan **MFA code**, password, atau seed phrase (sahih IT **tidak** meminta ini).
- Perubahan rekening vendor tanpa verifikasi dual-channel.

### Proses
- Kontak masuk di luar jam + desak segera.
- Meminta remote tool tidak standar.
- Menolak ticket / callback.

### Tabel cepat triage

| Sinyal | Severity | Tindakan segera |
|:---|:---:|:---|
| Minta password / MFA | Tinggi | Hentikan; laporkan SOC |
| Ubah wire instructions | Tinggi | Dual approval finance |
| Link “login portal” | Sedang–Tinggi | Lapor; jangan klik; verifikasi portal resmi |
| Vendor “baru” tanpa PO | Sedang | Procurement verify |
| Tailgate di pintu | Sedang | Challenge politely; security escort |

---

## 6. 🎓 Awareness Training That Works

Pelatihan buruk = video tahunan yang dilupa. Pelatihan baik = **berulang, terukur, tanpa malu-malukan**.

### Desain program
1. **Baseline** — survei + simulasi berizin (internal phishing simulation dengan RoE & HR buy-in).
2. **Teach principles** — Cialdini + prosedur callback, bukan “jangan klik link” semata.
3. **Just-in-time** — tips saat musim pajak, payroll, vendor renewals.
4. **Role-based** — finance (BEC), helpdesk (pretext), executives (whaling).
5. **Measure** — report rate ↑, repeat-click ↓, time-to-report ↓.
6. **No shame culture** — yang melapor cepat = perilaku yang dihadiahi.

$$
\mathsf{TrainingROI} \propto \frac{\mathsf{ReportRate} \times \mathsf{PreventedLoss}}{\mathsf{ProgramCost}}
$$

### Micro-curriculum (contoh 15 menit)
| Menit | Isi |
|:---:|:---|
| 0–3 | Cerita nyata (anonim) di industri Anda |
| 3–8 | 3 red flags + cara verifikasi |
| 8–12 | Latihan skenario (vishing script defense) |
| 12–15 | Cara lapor + apa yang terjadi setelah lapor |

---

## 7. 🏢 Organizational Controls

| Kontrol | Implementasi | Melawan |
|:---|:---|:---|
| Out-of-band verification | Callback ke nomor di HR directory | Vishing / BEC |
| Dual control | 2 orang untuk wire & privilege | Fraud tunggal |
| Least privilege + JIT | Akses terbatas waktu | Pretext helpdesk |
| Email authentication | SPF, DKIM, DMARC enforce | Spoof domain |
| Banner external mail | “External” warning | Fake internal |
| Helpdesk identity proof | Employee ID + callback | Account takeover social |
| Physical access policy | Badge + visitor escort | Tailgating |
| MFA resistant where possible | Phishing-resistant MFA (passkeys/FIDO2) | Credential harvest |
| Data classification | Jangan sebut data sensitif di telepon | Oversharing |

```
Request sensitive action
        │
        ▼
  Ticket required? ──no──▶ deny / redirect
        │ yes
        ▼
  Identity proof (policy)
        │
        ▼
  Out-of-band confirm (if high risk)
        │
        ▼
  Dual approval (if financial / admin)
        │
        ▼
  Execute + audit log
```

---

## 8. ⚖️ Ethics, Law & Authorized Testing

| Aktivitas | Syarat |
|:---|:---|
| Red team SE / phishing simulasi | RoE tertulis, legal, HR, executive sponsor |
| OSINT pada karyawan | Batasi sumber publik; hormati hukum privasi lokal |
| Impersonation physical | Izin fasilitas + safety stop |
| Mengajar teknik tipuan detail | Hindari “kit siap pakai”; fokus deteksi |

**Undang-undang** berbeda per yurisdiksi (penipuan, akses komputer, perekaman panggilan). Simulasi tanpa izin dapat melanggar hukum dan kontrak kerja.

---

## 9. 🚑 Social Engineering Incident Response

1. **Contain** — jangan lanjutkan percakapan tipuan; amankan akun jika kredensial terpapar.
2. **Preserve** — header email, nomor telepon, rekaman (jika legal), chat log.
3. **Reset** — password, session, MFA device bila perlu; review forward rules.
4. **Notify** — SOC / IR; finance jika BEC; legal jika data pelanggan.
5. **Hunt** — mailbox rules, new inbox delegates, unusual VPN.
6. **Lessons** — update training + kontrol; tanpa menyalahkan korban yang melapor.

$$
t_{\text{detect}} \downarrow \Rightarrow \mathsf{ExpectedLoss} \downarrow
$$

---

## 10. 🛠️ Defense Cheatsheet

```text
SEBUTKAN SEBELUM BERTINDAK
[ ] Apakah ada urgensi yang dipaksakan?
[ ] Apakah identitas terverifikasi lewat saluran resmi?
[ ] Apakah prosedur normal dilewati?
[ ] Apakah diminta rahasia (password/MFA/seed)?
[ ] Apakah ada perubahan rekening / akses admin?

JIKA YA PADA SALAH SATU → STOP → TICKET / CALLBACK → LAPOR
```

| Peran | Satu kebiasaan emas |
|:---|:---|
| Semua karyawan | Laporkan yang mencurigakan tanpa takut salah |
| Helpdesk | Tidak ada reset tanpa proof policy |
| Finance | Dual channel untuk ubah pembayaran |
| Exec assistant | Whaling checklist sebelum jadwal/transfer |
| Security | Ukur report rate, bukan hanya click rate |

---

## 🔐 Security Notes — Threats & Defenses

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Credential harvest | Fake login / vishing | FIDO2; never share MFA; report |
| BEC fraud | Invoice / CEO fraud | Dual control; vendor callbacks |
| Helpdesk pretext | Social reset | Strong identity proof |
| Tailgating | Physical follow-in | Challenge culture; turnstiles |
| Oversharing | Rapport abuse | Classification; need-to-know |
| Shame culture | Hide incidents | Reward fast reporting |

> **Tidak dibahas:** konstruksi kit phishing, proxy credential harvesting, payload BadUSB, atau skrip tipuan siap pakai.

---

> 📚 **References & Book Sources**
> - Christopher Hadnagy — *Social Engineering: The Science of Human Hacking* — `~/Documents/Books/CyberSec/Social Engineering/`
> - Kevin Mitnick & William Simon — *The Art of Deception* — `~/Documents/Books/CyberSec/Social Engineering/`
> - Joe Gray — *Practical Social Engineering* — `~/Documents/Books/CyberSec/Social Engineering/`
> - Robert Cialdini — *Influence* (principles referenced via SE literature)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Edukasi & pelatihan berizin. Jangan gunakan untuk penipuan atau akses tidak sah.
