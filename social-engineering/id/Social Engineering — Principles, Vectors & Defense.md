# Social Engineering: Prinsip, Vektor & Pertahanan

> **Zero2Root** | Seri Human Factor Security
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

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Social engineering (SE) | Menipu orang supaya memberi akses, informasi, atau melakukan sesuatu, tanpa perlu meretas komputer |
| Pretext | Cerita palsu yang dipakai penyerang ("Saya dari IT", "Saya vendor baru") |
| Rapport | Keakraban yang sengaja dibangun penyerang supaya kamu lengah |
| OSINT | Open-source intelligence: informasi yang bisa dicari siapa saja secara publik (LinkedIn, website kantor, media sosial) |
| Verifikasi out-of-band | Mengecek permintaan lewat jalur *lain* yang sudah kamu percaya. Contoh: ada email minta transfer, kamu telepon pengirimnya ke nomor di direktori kantor, bukan nomor yang ada di email itu |
| Callback | Tutup telepon, lalu telepon balik orangnya ke nomor resminya |
| Dual control | Tindakan sensitif butuh persetujuan dua orang, jadi satu orang yang tertipu tidak cukup |
| BEC | Business Email Compromise: penipuan lewat email supaya staf mengirim uang ke rekening yang salah |
| SOC | Security Operations Center: tim yang menerima dan menangani laporan keamanan |
| RoE | Rules of Engagement: dokumen bertanda tangan yang mengatur apa yang boleh dan tidak boleh dilakukan saat pengujian keamanan |

---

## 1. Manusia sebagai permukaan serangan

Firewall dan antivirus tidak ada gunanya kalau penyerang cukup membujuk karyawan untuk "membukakan pintu". Mitnick (*The Art of Deception*) menyebut tiga kebiasaan manusia yang dimanfaatkan penyerang: kita suka menolong, kita menghindari konflik, dan kita percaya pada orang yang terlihat punya wewenang.

Serangan social engineering paling mungkin berhasil kalau:

- korban **percaya** pada orang yang menghubunginya,
- permintaannya terasa **mendesak**,
- korban **punya akses** ke sesuatu yang berharga, dan
- **tidak ada cara mudah untuk mengecek** permintaan itu.

Hilangkan salah satunya, terutama yang terakhir, dan serangan jadi jauh lebih sulit.

Jadi social engineering tidak menyerang bug di software. Yang diserang adalah cara manusia berpikir dan celah di prosedur kantor. Karena itu pertahanannya juga lebih banyak di manusia dan proses: prosedur yang jelas, budaya yang membolehkan orang bilang "sebentar, saya cek dulu", dan cara yang bisa diandalkan untuk memverifikasi permintaan.

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

Psikolog Robert Cialdini menjelaskan beberapa hal yang membuat orang gampang bilang "iya". Hadnagy membangun kerangka social engineering-nya dari prinsip-prinsip ini. Kita mempelajarinya supaya bisa **mengenali** manipulasi, bukan memakainya.

| Prinsip | Maksudnya | Cara penyerang memakainya | Cara bertahan |
|:---|:---|:---|:---|
| Reciprocity (balas budi) | Kita merasa berutang pada orang yang pernah membantu | "Minggu lalu saya bantu kamu, tolong kirim file itu ya" | Bantuan apa pun tidak menggantikan prosedur normal |
| Commitment / consistency | Kita ingin konsisten dengan ucapan sebelumnya | "Tadi kamu bilang bisa bantu..." | Kamu selalu boleh berubah pikiran kalau ada yang terasa janggal |
| Social proof | Kita ikut-ikutan orang lain | "Semua staf sudah update lewat link ini" | Cek ke sumber resmi, bukan ke "semua orang" |
| Authority (otoritas) | Kita patuh pada atasan atau seragam | "IT Director minta reset sekarang juga" | Telepon balik ke nomor resmi; minta persetujuan orang kedua |
| Liking (rasa suka) | Kita mau menolong orang yang kita suka | Banyak basa-basi ramah, lalu tiba-tiba minta hal sensitif | Ramah tidak sama dengan berwenang |
| Scarcity / urgency | Kita panik kalau takut kehilangan sesuatu | "Akunmu ditutup dalam 15 menit" | Aturan: tidak ada tindakan sensitif di bawah tekanan waktu mendadak |
| Unity (rasa satu kelompok) | Kita percaya pada "orang kita sendiri" | Mengaku dari komunitas atau perusahaan partner yang sama | Tetap verifikasi identitas, seakrab apa pun kelihatannya |

### Pola di balik semuanya

Setiap prinsip mendorong kamu untuk bertindak **cepat** dan **tanpa mengecek**. Jadi pertahanannya selalu sama: tambahkan satu langkah pengecekan singkat (callback, ticket, persetujuan orang kedua) sebelum hal sensitif dilakukan. Langkahnya harus cukup cepat supaya orang benar-benar mau menjalankannya, tapi cukup tegas supaya tidak bisa dilewati hanya karena didesak.

---

## 3. Siklus narasi social engineering

Kebanyakan serangan social engineering mengikuti langkah yang mirip (berdasarkan *Practical Social Engineering* dan Hadnagy). Ini gambaran umum untuk mengenali serangan, bukan panduan untuk melakukannya.

```
Riset → Susun cerita → Hubungi → Bangun kepercayaan → Minta → Pergi → (Laporan)
```

| Langkah | Yang dilakukan penyerang | Cara bertahan |
|:---|:---|:---|
| Riset (OSINT) | Mengumpulkan info publik tentang kantor atau orangnya | Kurangi info yang dibagikan ke publik; ajari staf soal privasi |
| Susun cerita (pretext) | Membuat alasan yang masuk akal untuk menghubungi kamu | Curigai cerita apa pun yang ujungnya minta akses |
| Hubungi | Lewat email, telepon, tatap muka, atau chat | Pakai jalur resmi; pasang banner peringatan di email dari luar |
| Bangun kepercayaan (rapport) | Membuat kamu merasa nyaman | Perhatikan kalau ada permintaan mendadak setelah basa-basi |
| Minta | Meminta tindakan atau informasi | Jangan pernah lewati pengecekan hanya karena permintaannya terasa "kecil" |
| Pergi | Mengakhiri percakapan tanpa menimbulkan curiga | Simpan log; tinjau ulang kejadiannya setelah itu |
| Laporan | (Hanya di pengujian berizin) menulis hasil pengujian | Hanya boleh dengan RoE tertulis |

Penting: repository ini tidak mengajarkan cara membuat phishing kit, memasang tool seperti Evilginx, membuat perangkat BadUSB, atau menulis skrip penipuan. Fokusnya adalah psikologi, deteksi, dan pelatihan.

---

## 4. Vektor umum (konsep)

"Vektor" artinya jalur yang dipakai serangan untuk sampai ke korban.

| Vektor | Apa itu | Biasanya minta apa |
|:---|:---|:---|
| Phishing / spear-phishing | Pesan palsu yang menyuruh kamu klik atau membalas. Spear-phishing menyasar satu orang tertentu | Password, klik link malware, mengubah pembayaran |
| Vishing | Telepon penipuan (voice phishing) | Reset password, kode MFA, data pelanggan |
| Smishing | SMS atau chat penipuan | Klik link palsu "paket" atau "bank" |
| Pretexting (helpdesk) | Menelepon helpdesk sambil mengaku sebagai karyawan atau vendor | Membuka kunci akun, ditambahkan ke VPN |
| Penyamaran fisik | Datang langsung dan berlagak seperti orang dalam | Ikut masuk lewat pintu yang terkunci di belakang staf (tailgating) |
| Business Email Compromise (BEC) | Invoice palsu atau email palsu dari "CEO" | Mengganti rekening tujuan pembayaran |
| Quid pro quo | "Saya bantu beresin masalah IT-mu, install ini dulu ya" | Memasang tool remote access |

### Seberapa parah dampaknya?

Kerugian makin besar kalau:

- korban memberi **akses yang lebih besar** (akun admin lebih berbahaya daripada akun biasa),
- datanya **makin sensitif** (data pelanggan jauh lebih berbahaya daripada menu makan siang), dan
- perusahaan **makin lama sadar** (akses selama satu jam jauh lebih ringan daripada satu bulan).

---

## 5. Sinyal deteksi: red flags

### Dari isi pesannya

- Sangat mendesak plus ada ancaman ("lakukan sekarang atau kamu dipecat").
- Minta melewati prosedur normal atau merahasiakannya ("jangan bilang siapa-siapa").
- Alamat email yang hampir sama dengan aslinya, misalnya `paypa1.com` padahal seharusnya `paypal.com`, atau subdomain yang aneh.
- Minta kode MFA, password, atau seed phrase crypto. Staf IT asli tidak akan pernah meminta ini.
- Vendor mengganti nomor rekening tanpa konfirmasi lewat jalur kedua.

### Dari cara memintanya

- Menghubungi di luar jam kerja plus mendesak dijawab sekarang.
- Menyuruh kamu memasang tool remote yang tidak biasa.
- Menolak dibuatkan ticket atau menolak ditelepon balik.

### Tabel tindakan cepat

| Yang kamu lihat | Bahaya | Langsung lakukan |
|:---|:---:|:---|
| Minta password / kode MFA | Tinggi | Hentikan percakapan; laporkan ke SOC |
| Minta ganti data pembayaran | Tinggi | Minta persetujuan kedua dari finance |
| Link ke "halaman login" | Sedang-Tinggi | Laporkan; jangan diklik; buka situs aslinya sendiri |
| Vendor "baru" tanpa purchase order | Sedang | Cek ke bagian procurement |
| Ada orang ikut masuk di belakangmu lewat pintu akses | Sedang | Tanya dengan sopan siapa dia; panggil security untuk mendampingi |

---

## 6. Pelatihan kesadaran yang efektif

Pelatihan yang buruk itu video setahun sekali yang langsung dilupakan. Pelatihan yang baik dilakukan rutin, diukur hasilnya, dan tidak pernah mempermalukan siapa pun.

### Cara menyusun programnya

1. **Mulai dari kondisi awal.** Lakukan survei dan simulasi phishing berizin (dengan RoE tertulis dan persetujuan HR) untuk melihat posisi tim saat ini.
2. **Ajarkan alasannya.** Jelaskan prinsip-prinsip pengaruh dan kebiasaan callback. Sekadar "jangan klik link" tidak cukup.
3. **Pilih waktu yang tepat.** Kirim tips singkat saat penipuan sedang ramai: musim pajak, gajian, perpanjangan kontrak vendor.
4. **Sesuaikan dengan peran.** Finance belajar soal BEC, helpdesk soal penelepon palsu, eksekutif soal whaling (phishing yang menyasar pimpinan).
5. **Ukur hasilnya.** Tanda bagus: makin banyak yang melapor, makin sedikit yang klik berulang, laporan masuk makin cepat.
6. **Jangan mempermalukan.** Orang yang cepat melapor dipuji, walaupun dia sempat klik.

### Apakah pelatihannya sepadan?

Pelatihan dianggap berhasil kalau makin banyak orang melaporkan pesan mencurigakan dan makin sedikit serangan yang berhasil, dibandingkan biaya programnya. Karena itu jumlah laporan sering jadi ukuran yang lebih baik daripada jumlah klik: satu laporan cepat bisa melindungi satu kantor.

### Contoh sesi 15 menit

| Menit | Isi |
|:---:|:---|
| 0-3 | Cerita nyata (disamarkan) dari industri kamu |
| 3-8 | Tiga red flag dan cara mengecek masing-masing |
| 8-12 | Latihan: menghadapi skenario telepon penipuan |
| 12-15 | Cara melapor dan apa yang terjadi setelah melapor |

---

## 7. Kontrol organisasi

Ini aturan dan alat yang dipasang perusahaan supaya satu orang yang tertipu tidak langsung jadi bencana.

| Kontrol | Cara kerjanya | Yang dicegah |
|:---|:---|:---|
| Verifikasi out-of-band | Telepon balik ke nomor di direktori HR | Telepon penipuan, BEC |
| Dual control | Transfer uang dan perubahan akses harus disetujui dua orang | Satu orang tertipu lalu terjadi fraud |
| Least privilege + JIT | Orang hanya dapat akses yang dibutuhkan, dan hanya untuk waktu terbatas (just-in-time) | Helpdesk tertipu lalu memberi akses berlebihan |
| Email authentication | Aktifkan SPF, DKIM, dan DMARC, supaya server email bisa mendeteksi email yang memalsukan domain kantor | Email palsu atas nama domain kantor sendiri |
| Banner email eksternal | Label "External" pada email dari luar kantor | Email "internal" palsu |
| Cek identitas di helpdesk | ID karyawan plus callback sebelum reset apa pun | Pengambilalihan akun lewat helpdesk |
| Kebijakan akses fisik | Badge dan pendamping untuk tamu | Tailgating |
| MFA yang tahan phishing | Passkey atau security key FIDO2, yang tidak akan jalan di situs palsu | Password yang dicuri |
| Klasifikasi data | Beri label data sensitif dan jangan pernah menyebutkannya lewat telepon | Oversharing (membagi info terlalu banyak) |

Alur yang seharusnya untuk permintaan sensitif:

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

| Aktivitas | Yang harus ada dulu |
|:---|:---|
| Pengujian social engineering / simulasi phishing | RoE tertulis, plus persetujuan legal, HR, dan eksekutif |
| Riset tentang karyawan (OSINT) | Hanya pakai sumber publik; ikuti hukum privasi setempat |
| Uji penyamaran fisik | Izin pemilik gedung dan cara untuk menghentikan pengujian dengan aman |
| Mengajarkan teknik penipuan | Jangan bagikan kit siap pakai; fokus ke deteksi |

Hukum di tiap negara berbeda (penipuan, akses komputer, perekaman telepon). Pengujian tanpa izin bisa melanggar hukum dan kontrak kerja.

---

## 9. Incident response social engineering

Yang harus dilakukan setelah ada yang tertipu:

1. **Tahan:** berhenti bicara dengan penyerang. Kalau password sudah diberikan, kunci atau amankan akunnya.
2. **Simpan bukti:** simpan email (beserta header-nya), nomor telepon, rekaman (kalau legal), dan log chat.
3. **Reset:** ganti password, keluarkan semua sesi login, dan ganti perangkat MFA kalau perlu. Cek apakah penyerang menambahkan aturan forward email.
4. **Beri tahu:** lapor ke SOC / tim incident response, ke finance kalau menyangkut pembayaran, dan ke legal kalau ada data pelanggan yang terlibat.
5. **Telusuri:** cari aturan mailbox baru, orang baru yang punya akses ke inbox, dan login VPN yang tidak biasa.
6. **Ambil pelajaran:** perbarui pelatihan dan kontrolnya. Jangan pernah menyalahkan orang yang melapor; dia sudah membantu.

**Makin cepat seseorang melapor, makin kecil kerugiannya.** Ini kebiasaan paling penting yang perlu dibangun.

---

## 10. Cheatsheet pertahanan

```text
CEK SEBELUM BERTINDAK
[ ] Apakah ada yang mendesak saya?
[ ] Sudahkah saya memastikan identitasnya lewat jalur resmi?
[ ] Apakah saya diminta melewati prosedur normal?
[ ] Apakah saya diminta rahasia (password / kode MFA / seed phrase)?
[ ] Apakah ini soal ganti rekening atau akses admin?

KALAU ADA YANG "YA" → STOP → BUAT TICKET / TELEPON BALIK → LAPOR
```

| Peran | Satu kebiasaan yang harus dijaga |
|:---|:---|
| Semua karyawan | Laporkan apa pun yang mencurigakan, walaupun mungkin salah |
| Helpdesk | Tidak ada reset tanpa bukti identitas sesuai kebijakan |
| Finance | Konfirmasi setiap perubahan pembayaran lewat jalur kedua |
| Asisten eksekutif | Jalankan checklist whaling sebelum mengatur jadwal atau transfer |
| Tim security | Hitung berapa banyak yang melapor, bukan cuma berapa banyak yang klik |

---

## Catatan keamanan: ancaman & pertahanan

| Ancaman | Cara terjadinya | Pertahanan |
|:---|:---|:---|
| Pencurian password | Halaman login palsu / telepon penipuan | FIDO2; jangan pernah bagikan kode MFA; laporkan |
| Fraud BEC | Invoice palsu / email palsu dari "CEO" | Dual control; telepon balik vendornya |
| Pretexting ke helpdesk | Penelepon menipu helpdesk supaya reset akun | Cek identitas yang ketat |
| Tailgating | Ikut masuk di belakang orang lewat pintu akses | Budaya yang menganggap wajar bertanya "Anda siapa?"; turnstile |
| Oversharing | Penyerang membangun keakraban, lalu minta terlalu banyak | Klasifikasi data; bagikan seperlunya saja |
| Budaya malu | Orang menyembunyikan insiden karena malu | Hargai pelaporan yang cepat |

Yang tidak dibahas: membuat phishing kit, proxy pencuri kredensial, payload BadUSB, atau skrip penipuan siap pakai.

---

> **Referensi & sumber buku**
> - Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Kevin Mitnick & William Simon, *The Art of Deception*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Joe Gray, *Practical Social Engineering*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Robert Cialdini, *Influence* (prinsip yang dirujuk lewat literatur SE)

> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Edukasi dan pelatihan berizin. Jangan gunakan untuk penipuan atau akses tidak sah.
