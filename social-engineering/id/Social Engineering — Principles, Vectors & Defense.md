# Social Engineering: Prinsip, Vektor & Pertahanan

> **LearnCybersecurity** | Seri Human Factor Security
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*; Kevin Mitnick, *The Art of Deception*; Joe Gray, *Practical Social Engineering*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-068` | **Fase 7:** Specialized
> **Estimasi belajar:** 4-5 jam | **Level:** Intermediate
> **Prasyarat:** LC-058
> **Peta buku:** Hadnagy, Social Engineering 2nd Ed.; Mitnick, The Art of Deception; Gray, Practical Social Engineering
<!-- LC-CURRICULUM-END -->

## Daftar isi

1. Manusia sebagai permukaan serangan
2. Prinsip pengaruh Cialdini (lensa pertahanan)
3. Siklus narasi social engineering
4. Vektor umum (konsep)
5. Sinyal deteksi: red flags
6. Pelatihan kesadaran yang efektif
7. Kontrol organisasi
8. Etika, hukum & pengujian berizin
9. Incident response social engineering
10. Cheatsheet pertahanan

---

## 1. Manusia sebagai permukaan serangan

Keamanan teknis dapat dilewati jika penyerang berhasil meyakinkan manusia untuk memberikan akses, rahasia, atau melakukan tindakan tertentu. Mitnick (*Art of Deception*) menekankan bahwa orang cenderung ingin membantu, takut konflik, dan percaya pada otoritas yang tampak sah.

$$
\mathsf{Risk}_{SE} = f(\mathsf{Trust},\; \mathsf{Urgency},\; \mathsf{Access},\; \mathsf{VerificationGap})
$$

Semakin besar trust dan urgency, serta semakin lemah verifikasi, semakin tinggi kemungkinan keberhasilan rekayasa sosial.

Social engineering (SE) mengeksploitasi bias kognitif dan celah pada proses organisasi, bukan terutama memory corruption. Pertahanannya adalah proses, budaya, dan jalur verifikasi, bukan sekadar aturan firewall tambahan.

```
┌──────────────┐     trust / fear / greed      ┌──────────────┐
│  Attacker    │ ─────────────────────────────▶│   Target     │
│  narrative   │◀──── info / access / action ──│   human      │
└──────────────┘                               └──────────────┘
        │                                              │
        └────────── defense: verify out-of-band ───────┘
```

---

## 2. Prinsip pengaruh Cialdini (lensa pertahanan)

Hadnagy membangun kerangka SE di atas psikologi pengaruh. Pahami prinsip ini untuk mendeteksi manipulasi, bukan untuk menyiapkan kampanye tipuan.

| Prinsip | Intuisi | Contoh manipulasi | Pertahanan |
|:---|:---|:---|:---|
| Reciprocity | Hutang budi | "Saya bantu dulu, tolong balas kirim file" | Kebijakan: hadiah tidak boleh membuka jalan bypass prosedur |
| Commitment / Consistency | Konsisten dengan pernyataan awal | "Tadi Anda bilang bisa bantu…" | Tetap izinkan perubahan keputusan bila ada fakta baru |
| Social proof | Mengikuti orang lain | "Semua staf sudah update lewat link ini" | Verifikasi lewat sumber resmi |
| Authority | Patuh pada atasan / seragam | "IT Director minta reset sekarang" | Callback ke nomor resmi; dual control |
| Liking | Menolong orang yang disukai | Rapport berlebihan diikuti permintaan sensitif | Pisahkan keramahan dari otorisasi |
| Scarcity / Urgency | Takut kehilangan | "Akun ditutup dalam 15 menit" | SLA: tidak ada aksi sensitif di bawah tekanan waktu palsu |
| Unity | "Kita satu kelompok" | Identitas palsu sebagai komunitas/vendor | Badge dan identitas yang terverifikasi |

### Formalisasi sederhana

$$
\mathsf{Compliance} \uparrow \;\text{when}\; \sum_i w_i \cdot \mathsf{Principle}_i > \mathsf{VerificationFriction}
$$

Pertahanan bekerja dengan menaikkan VerificationFriction (callback, ticket, dual approval) tanpa menghancurkan produktivitas.

---

## 3. Siklus narasi social engineering

Dari *Practical Social Engineering* / Hadnagy (siklus generik, bukan playbook serangan):

```
OSINT (publik) → Pretext design → Contact → Rapport → Ask → Exit → Report
```

| Fase | Apa yang terjadi | Kontrol pertahanan |
|:---|:---|:---|
| OSINT | Pengumpulan info publik tentang organisasi/orang | Minimalkan jejak publik; pelatihan privasi |
| Pretext | Menyusun cerita yang "masuk akal" | Tantang cerita yang meminta akses |
| Contact | Email, telepon, tatap muka, chat | Channel resmi + banner peringatan |
| Rapport | Membangun kenyamanan | Waspadai permintaan mendadak setelah basa-basi |
| Ask | Permintaan aksi/info | Jangan pernah lewati verifikasi hanya karena permintaannya terasa "kecil" |
| Exit | Menutup tanpa memicu alarm | Logging & after-action review |
| Report | (Pada red team berizin) dokumentasi | Hanya dengan RoE tertulis |

Catatan keras: repository ini tidak mengajarkan setup phishing kit, Evilginx, payload BadUSB, atau skrip penipuan. Fokusnya adalah psikologi, deteksi, dan pelatihan.

---

## 4. Vektor umum (konsep)

| Vektor | Deskripsi singkat | Apa yang biasanya diminta |
|:---|:---|:---|
| Phishing / spear-phishing | Pesan tipuan dengan CTA | Kredensial, klik malware, perubahan wire |
| Vishing | Telepon / VoIP | Reset password, kode MFA, data pelanggan |
| Smishing | SMS / chat mobile | Link "paket" / "bank" |
| Pretexting (helpdesk) | Menyamar sebagai karyawan/vendor | Unlock akun, tambah ke VPN group |
| Impersonation | Fisik / badge surfing | Tailgating, "tamu vendor" |
| Business Email Compromise (BEC) | Penyimpangan wire / invoice | Mengubah rekening pembayaran |
| Quid pro quo | "Saya bantu IT, Anda install…" | Remote access tools |

$$
\mathsf{Impact} = \mathsf{PrivilegeGranted} \times \mathsf{DataSensitivity} \times \mathsf{SpeedOfDetection}^{-1}
$$

---

## 5. Sinyal deteksi: red flags

### Bahasa / konten

- Urgensi ekstrem plus ancaman hukuman.
- Permintaan untuk melewati prosedur ("jangan bilang siapa-siapa").
- Ketidaksesuaian domain email (homoglyph, subdomain yang aneh).
- Permintaan kode MFA, password, atau seed phrase (IT yang sah tidak akan meminta ini).
- Perubahan rekening vendor tanpa verifikasi dual-channel.

### Proses

- Kontak masuk di luar jam kerja plus desakan segera.
- Meminta penggunaan remote tool yang tidak standar.
- Menolak proses ticket / callback.

### Tabel triage cepat

| Sinyal | Severity | Tindakan segera |
|:---|:---:|:---|
| Minta password / MFA | Tinggi | Hentikan; laporkan ke SOC |
| Mengubah wire instructions | Tinggi | Dual approval dari finance |
| Link "login portal" | Sedang-Tinggi | Laporkan; jangan diklik; verifikasi portal resmi |
| Vendor "baru" tanpa PO | Sedang | Verifikasi lewat procurement |
| Tailgate di pintu | Sedang | Tantang dengan sopan; kawal dari security |

---

## 6. Pelatihan kesadaran yang efektif

Pelatihan buruk adalah video tahunan yang cepat dilupakan. Pelatihan baik bersifat berulang, terukur, dan tidak mempermalukan siapa pun.

### Desain program

1. Baseline: survei plus simulasi berizin (simulasi phishing internal dengan RoE dan dukungan HR).
2. Ajarkan prinsipnya: Cialdini plus prosedur callback, bukan sekadar "jangan klik link".
3. Just-in-time: tips saat musim pajak, payroll, atau perpanjangan kontrak vendor.
4. Role-based: finance (BEC), helpdesk (pretext), eksekutif (whaling).
5. Ukur hasilnya: tingkat laporan naik, repeat-click turun, time-to-report turun.
6. Budaya tanpa rasa malu: pelaporan cepat adalah perilaku yang dihargai.

$$
\mathsf{TrainingROI} \propto \frac{\mathsf{ReportRate} \times \mathsf{PreventedLoss}}{\mathsf{ProgramCost}}
$$

### Contoh micro-curriculum (15 menit)

| Menit | Isi |
|:---:|:---|
| 0-3 | Cerita nyata (anonim) dari industri Anda |
| 3-8 | 3 red flags plus cara memverifikasinya |
| 8-12 | Latihan skenario (defense terhadap skrip vishing) |
| 12-15 | Cara melapor dan apa yang terjadi setelah melapor |

---

## 7. Kontrol organisasi

| Kontrol | Implementasi | Melawan |
|:---|:---|:---|
| Verifikasi out-of-band | Callback ke nomor di direktori HR | Vishing / BEC |
| Dual control | 2 orang untuk wire transfer & privilege | Fraud tunggal |
| Least privilege + JIT | Akses terbatas waktu | Pretext helpdesk |
| Email authentication | Penegakan SPF, DKIM, DMARC | Spoofing domain |
| Banner email eksternal | Peringatan "External" | Email internal palsu |
| Bukti identitas di helpdesk | Employee ID + callback | Account takeover lewat social engineering |
| Kebijakan akses fisik | Badge + kawalan tamu | Tailgating |
| MFA yang resisten phishing bila memungkinkan | Passkeys/FIDO2 | Pencurian kredensial |
| Klasifikasi data | Jangan sebut data sensitif lewat telepon | Oversharing |

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

## 8. Etika, hukum & pengujian berizin

| Aktivitas | Syarat |
|:---|:---|
| Red team SE / simulasi phishing | RoE tertulis, legal, HR, dan sponsor eksekutif |
| OSINT terhadap karyawan | Batasi pada sumber publik; hormati hukum privasi lokal |
| Impersonation fisik | Izin fasilitas + safety stop |
| Mengajarkan teknik tipuan secara detail | Hindari "kit siap pakai"; fokus pada deteksi |

Undang-undang berbeda per yurisdiksi (penipuan, akses komputer, perekaman panggilan). Simulasi tanpa izin dapat melanggar hukum dan kontrak kerja.

---

## 9. Incident response social engineering

1. Contain: jangan melanjutkan percakapan tipuan; amankan akun jika kredensial sudah terpapar.
2. Preserve: simpan header email, nomor telepon, rekaman (jika legal), dan chat log.
3. Reset: password, session, MFA device bila perlu; review forward rules.
4. Notify: SOC / IR; finance jika kasus BEC; legal jika menyangkut data pelanggan.
5. Hunt: cek mailbox rules, delegate inbox baru, VPN yang tidak biasa.
6. Lessons: update pelatihan dan kontrol; jangan menyalahkan korban yang sudah melapor.

$$
t_{\text{detect}} \downarrow \Rightarrow \mathsf{ExpectedLoss} \downarrow
$$

---

## 10. Cheatsheet pertahanan

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
| Helpdesk | Tidak ada reset tanpa proof sesuai policy |
| Finance | Dual channel untuk perubahan pembayaran |
| Exec assistant | Checklist whaling sebelum jadwal/transfer |
| Security | Ukur report rate, bukan hanya click rate |

---

## Catatan keamanan: ancaman & pertahanan

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Pencurian kredensial | Fake login / vishing | FIDO2; jangan pernah berbagi MFA; laporkan |
| Fraud BEC | Invoice / CEO fraud | Dual control; callback ke vendor |
| Pretext ke helpdesk | Social reset | Bukti identitas yang kuat |
| Tailgating | Mengikuti masuk secara fisik | Budaya menantang orang asing; turnstile |
| Oversharing | Penyalahgunaan rapport | Klasifikasi data; need-to-know |
| Budaya malu | Insiden disembunyikan | Hargai pelaporan yang cepat |

Yang tidak dibahas: konstruksi kit phishing, proxy credential harvesting, payload BadUSB, atau skrip tipuan siap pakai.

---

> **Referensi & sumber buku**
> - Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Kevin Mitnick & William Simon, *The Art of Deception*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Joe Gray, *Practical Social Engineering*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Robert Cialdini, *Influence* (prinsip yang dirujuk lewat literatur SE)

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Edukasi dan pelatihan berizin. Jangan gunakan untuk penipuan atau akses tidak sah.
