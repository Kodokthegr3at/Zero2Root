# Android Security Internals & Application Hardening

> **LearnCybersecurity** | Seri Mobile Application Security
> Terakhir diperbarui: 2026 | Penulis: kodoktheGr3at
> Referensi utama: Nikolay Elenkov, *Android Security Internals*; dokumentasi Security dari Android Open Source Project (AOSP)

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-066` | **Fase 7:** Spesialisasi
> **Estimasi belajar:** 6-8 jam | **Level:** Lanjutan
> **Prasyarat:** LC-054, LC-047
> **Peta buku:** Elenkov, Android Security Internals (lengkap)
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik |
|---|-------|
| 1 | Lapisan arsitektur keamanan Android |
| 2 | Sandbox UID & isolasi DAC |
| 3 | Model permission |
| 4 | Komponen & Intent |
| 5 | Binder IPC |
| 6 | Ringkasan SELinux |
| 7 | Storage & kriptografi |
| 8 | Metodologi review aplikasi |
| 9 | Kelas kelemahan umum |
| 10 | Cheatsheet |

---

## 1. Lapisan Arsitektur Keamanan Android

Android adalah sistem berlapis di atas kernel Linux yang dikustomisasi. Keamanannya tidak bergantung pada satu kontrol tunggal, melainkan pertahanan berlapis (Elenkov, Bab 1-2):

```
┌──────────────────────────────────────────────────────────────┐
│  Apps (APK) — signed, permission-gated, UID-isolated         │
├──────────────────────────────────────────────────────────────┤
│  Framework APIs — PackageManager, ActivityManager, Keystore  │
├──────────────────────────────────────────────────────────────┤
│  Native daemons / HAL — Binder clients & services            │
├──────────────────────────────────────────────────────────────┤
│  Linux kernel — UID/GID DAC, capabilities, seccomp           │
├──────────────────────────────────────────────────────────────┤
│  SELinux MAC (Enforcing) — type enforcement domains          │
└──────────────────────────────────────────────────────────────┘
```

Setiap lapisan menganggap lapisan di atasnya bisa saja sudah dikompromikan. Kompromi pada satu aplikasi seharusnya tidak berarti kompromi pada aplikasi lain, pada layanan sistem, atau pada kernel, itulah tujuan desain dari kombinasi sandbox dan MAC. Kalau lapisan atas jebol, lapisan bawah membatasi dampaknya. Isolasi aplikasi dan MAC adalah inti dari desain ini.

---

## 2. Application Sandbox, Isolasi UID Unik

Saat instalasi, Package Manager mengalokasikan UID Linux yang unik untuk tiap aplikasi (contoh: `u0_a145` sama dengan UID `10145`). Data privat aplikasi berada di:

$$
\mathsf{AppData}(pkg) = /\mathsf{data}/\mathsf{data}/pkg/
$$

dengan ownership $(uid_{pkg}, uid_{pkg})$ dan mode tipikal `0700`.

Model formal isolasi (DAC):

$$
\mathsf{Access}(A \rightarrow B.\mathsf{data}) = \mathsf{true}
\iff uid_A = uid_B \lor \mathsf{sharedUserId} \land \mathsf{sameSigningKey}
$$

`sharedUserId` sudah deprecated di API modern, hindari dipakai pada desain baru. Isolasi diperkuat lagi oleh ART dan process isolation: satu proses per aplikasi, kecuali multi-process dideklarasikan secara eksplisit di manifest.

Failure mode sandbox yang perlu diwaspadai saat review: file yang world-readable, flag lama `MODE_WORLD_*`, komponen yang diekspor lalu memproxy data privileged, dan penyalahgunaan `sharedUserId` atau signing key yang sama di beberapa aplikasi. Saat review, titik yang paling sering diperiksa adalah file world-readable, komponen yang terlalu banyak diekspor, dan penggunaan signing key yang sama antar aplikasi.

| Kontrol | Lapisan | Fungsi |
|:---|:---|:---|
| Unique UID | Kernel DAC | Isolasi file & process |
| Process isolation | Zygote/ART | Batas crash & memory |
| SELinux domain | MAC | Membatasi bahkan path root/system |
| seccomp | Kernel | Filter syscall berbahaya |

---

## 3. Model Permission

### 3.1 Klasifikasi
| Kelas | Contoh | Kapan diminta | Risiko jika disalahgunakan |
|:---|:---|:---|:---|
| Normal | `INTERNET`, `VIBRATE` | Otomatis saat install | Relatif rendah |
| Dangerous | `CAMERA`, `READ_CONTACTS` | Prompt saat runtime | Privasi tinggi |
| Signature | API khusus sistem | Signing cert yang sama | Jembatan privilege |
| Special | `SYSTEM_ALERT_WINDOW` | Diberikan lewat Settings | Overlay / UI phishing |

Prinsip least privilege: minta izin seminimal mungkin yang dibutuhkan fitur. Saat review, petakan tiap permission ke use-case konkretnya. Permission tanpa justifikasi jelas adalah tanda bahaya.

Deklarasi di `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Untuk runtime (API 23+): cek `checkSelfPermission`, lalu `requestPermissions`, dan tangani penolakan dengan baik (jangan sampai force-crash).

Permintaan izin yang berlebihan memperluas blast radius kalau aplikasi dikompromikan. Perlakukan setiap permission grant sebagai bagian dari dokumentasi trust boundary aplikasi.

---

## 4. Komponen, Permukaan Ekspor & Intent

Android punya empat komponen inti:

| Komponen | Peran | Risiko ekspor |
|:---|:---|:---|
| Activity | UI entry point | Deep-link hijack, penyalahgunaan task affinity |
| Service | Pekerjaan di background | Start/bind tanpa otorisasi |
| BroadcastReceiver | Event listener | Broadcast yang dipalsukan |
| ContentProvider | Berbagi data | SQLi / path traversal / IDOR |

Aturan aman default:

$$
\mathsf{exported} =
\begin{cases}
\mathsf{false} & \text{jika tidak perlu diakses dari luar app} \\
\mathsf{true} + \mathsf{permission} & \text{jika IPC publik memang dibutuhkan}
\end{cases}
$$

Intent adalah pesan IPC. Intent eksplisit menargetkan komponen tertentu secara pasti; Intent implisit memakai action/category/data, dan lebih rawan hijacking kalau tidak diproteksi.

```
App A ──Intent──▶ ActivityManager ──resolve──▶ App B component
                      │
                      └─ enforce: exported? permission? caller UID?
```

Pertahanan: jangan ekspor Activity yang sensitif, validasi semua data extra, gunakan `PendingIntent` dengan flag immutability di API modern, dan batasi deep link dengan App Links plus autoVerify.

---

## 5. Binder IPC, Identitas & AIDL

Binder adalah bus IPC utama di Android (Elenkov, Bab 6). Setiap transaksi membawa identitas pemanggil yang bisa diverifikasi di sisi service:

$$
\begin{aligned}
uid_{caller} &= \mathsf{Binder.getCallingUid}() \\
pid_{caller} &= \mathsf{Binder.getCallingPid}()
\end{aligned}
$$

Service yang mengekspos AIDL wajib memvalidasi UID atau permission sebelum menjalankan operasi privileged. Jangan percaya parameter dari client tanpa otorisasi.

Identitas Binder adalah fondasi kepercayaan IPC di Android. Bug desain yang umum terjadi adalah menjalankan pekerjaan privileged hanya berdasarkan "ada panggilan binder yang masuk", tanpa memeriksa identitas pemanggil atau mensyaratkan signature/dangerous permission. Panggilan Binder yang datang saja tidak cukup sebagai bukti otorisasi, UID dan permission pemanggil harus selalu diverifikasi.

| Pola aman | Pola berbahaya |
|:---|:---|
| `enforceCallingPermission(...)` | Binder stub yang mempercayai semua caller |
| Signature permission pada service | Service diekspor tanpa permission |
| Membersihkan calling identity hanya saat diperlukan | Bug yang membersihkan identity secara permanen |
| Validasi input pada field Parcel | Deserialize buta / path langsung dari client |

---

## 6. SELinux di Android, Ringkasan MAC

SELinux menambahkan Mandatory Access Control di atas DAC. Setiap proses punya security context (user:role:type:sensitivity). Kebijakan type enforcement menentukan apakah domain $D$ boleh melakukan operasi $op$ pada tipe objek $T$:

$$
\mathsf{Allow}(D, T, op) \in \mathsf{Policy}
$$

Mode produksi Android adalah Enforcing. Mode `permissive` hanya dipakai untuk debugging pada perangkat milik sendiri.

Konsep penting bagi developer dan reviewer:
- Aplikasi pihak ketiga biasanya berada di domain `untrusted_app` (versinya bervariasi tergantung API level).
- Layanan vendor/system punya domain yang jauh lebih sempit.
- Kebijakan ini di-compile ke binary; denial-nya muncul di `logcat`/`dmesg` sebagai `avc: denied`.

SELinux bukan pengganti pemeriksaan permission di level aplikasi, melainkan backstop yang membatasi kerusakan kalau bug DAC atau bug framework terjadi. Memahami domain SELinux membantu menjawab pertanyaan seperti "kenapa aplikasi ini tidak bisa membuka device node itu?" tanpa harus mengarang cara bypass kernel.

```
untrusted_app ──X──▶ /dev/block/*     (typical deny)
system_server ──✓──▶ framework sockets (policy allow)
```

---

## 7. Storage & API Kriptografi yang Aman

| Mekanisme | Fungsi | Catatan defense |
|:---|:---|:---|
| Android Keystore | Kunci berbasis hardware (TEE/StrongBox bila tersedia) | Jangan ekstrak key material ke memory aplikasi kecuali benar-benar perlu |
| EncryptedSharedPreferences / Jetpack Security | Preferensi terenkripsi | Lebih baik dibanding SharedPreferences plaintext |
| SQLCipher / encrypted Room | Database saat disimpan (at rest) | Kunci diambil dari Keystore, bukan hardcode |
| File-Based Encryption (FBE) | Enkripsi filesystem perangkat | Perhatikan konteks storage CE vs DE |
| Network Security Config | Trust anchor TLS, kebijakan cleartext | Blokir cleartext di production |

Anti-pattern: menyimpan token atau API key di `SharedPreferences` plaintext, di resource XML, atau sebagai string konstanta di dalam DEX.

$$
\mathsf{Secret}_{ok} \subseteq \mathsf{Keystore}\ \cup\ \mathsf{server\text{-}side}
$$

---

## 8. Metodologi Review Keamanan Aplikasi

Metodologi ini berorientasi defense, bukan playbook bypass.

### 8.1 Static review pipeline
1. Inventory: package name, min/target SDK, permission, komponen yang diekspor.
2. Threat model manifest: setiap `exported=true` butuh owner dan alasan permission yang jelas.
3. Code path: setting WebView, penggunaan crypto, file I/O, handler IPC, deep link.
4. SDK pihak ketiga: tracker, iklan, proxy permission yang tidak terduga.
5. Secrets scan: API key, URL privat, endpoint debug.

Tool lab yang umum dipakai (untuk analisis milik sendiri atau dengan izin eksplisit): `aapt`/`aapt2`, `apkanalyzer`, JADX, APKTool (untuk memahami resource/smali), `dexdump`.

### 8.2 Dynamic review (perangkat/emulator milik sendiri)
- Jalankan alur autentikasi, periksa traffic dengan proxy, hanya pada build debug milik Anda sendiri.
- Verifikasi penggunaan Keystore, flag backup (`allowBackup`), dan logging yang berlebihan.
- Uji jalur penolakan permission dan error handling-nya.

### 8.3 Checklist secure coding (developer)
| Kontrol | Praktik |
|:---|:---|
| Input | Validasi Intent extras, URI, dan query provider (parameterized) |
| WebView | `setJavaScriptEnabled` hanya kalau perlu; batasi `addJavascriptInterface` |
| Crypto | Android Keystore + AES-GCM; larang ECB dan IV hardcode |
| IPC | Ekspor seminimal mungkin; service yang dibatasi permission |
| Logging | Jangan log PII/token |
| Backup | `android:allowBackup="false"` bila datanya sensitif |
| Cleartext | `cleartextTrafficPermitted=false` |

Aturan tegas (edukasi): catatan ini tidak mencakup resep bypass SSL pinning, Frida hook untuk melemahkan TLS, atau prosedur root exploit. Fokusnya adalah arsitektur, review, dan hardening.

---

## 9. Kelas Kelemahan Umum (Konsep)

| Kelas | Gejala | Mitigasi |
|:---|:---|:---|
| Insecure data at rest | Token di prefs/DB dalam bentuk plaintext | Keystore + encrypted storage |
| Komponen over-exported | Activity/Service tanpa permission | `exported=false` / signature permission |
| Intent redirection | Meneruskan Intent mentah dari caller | Jangan forward Intent mentah; pakai allowlist |
| Path traversal di Provider | `../` di query path | Canonicalize + root jail |
| SQL injection di Provider | Query lewat string concat | Selection args yang parameterized |
| Tapjacking / overlay | UI tertutup elemen lain | `filterTouchesWhenObscured`, batasan overlay modern |
| Konfigurasi TLS lemah | Cleartext / TrustManager trust-all | Network Security Config; jangan pernah trust-all |
| Debuggable release | `android:debuggable=true` | Pastikan build release tidak debuggable |

---

## 10. Cheatsheet Lab (Perangkat / Emulator Milik Sendiri)

```bash
# ── Inventory paket & permission ─────────────────────────────
adb shell pm list packages -f
adb shell dumpsys package com.example.app | less

# ── Manifest / APK metadata ──────────────────────────────────
aapt dump badging app.apk
aapt dump permissions app.apk
apkanalyzer manifest print app.apk

# ── Decompile untuk review (lab Anda) ────────────────────────
jadx -d out_jadx app.apk
apktool d app.apk -o out_apktool

# ── Log & SELinux denials (diagnostik) ───────────────────────
adb logcat | grep -E 'avc:|AndroidRuntime|keystore'
adb shell getenforce

# ── Backup flag & debuggable (cek, jangan abuse) ─────────────
aapt dump xmltree app.apk AndroidManifest.xml | grep -E 'debuggable|allowBackup'
```

---

## Catatan Keamanan, Ancaman & Pertahanan

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Pencurian data antar aplikasi | DAC lemah / world-readable | Sandbox ketat; tidak ada MODE_WORLD_* |
| Confused deputy | Komponen proxy yang diekspor | Permission + validasi caller |
| Kebocoran secret | Logging, backup, string di DEX | Keystore; bersihkan log; allowBackup=false |
| MITM pada API mobile | Cleartext / trust rusak | TLS + NSC; pinning hanya dengan kematangan ops yang cukup |
| Penyalahgunaan privilege | Permission yang terlalu luas | Least privilege; UX runtime yang jelas |
| Berharap bisa bypass kebijakan | Mitos "disable SELinux saja" | Tetap Enforcing; perbaiki desain aplikasi |

---

> **Referensi dan Sumber Buku**
> - Nikolay Elenkov, *Android Security Internals: An In-Depth Guide to Android's Security Architecture*, `~/Documents/Books/CyberSec/Android/`
> - AOSP, dokumentasi Security & SELinux; Android Developers, Security best practices
> - OWASP Mobile Application Security (MAS) / MASVS, kategori verifikasi

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Hanya untuk edukasi, review aplikasi milik sendiri, dan pengujian berizin. Bukan untuk akses tidak sah.
