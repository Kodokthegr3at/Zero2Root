# 📱 Android Security Internals & Application Hardening

> **LearnCybersecurity** | Mobile Application Security Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at  
> 📚 Primary refs: Nikolay Elenkov — *Android Security Internals*; Android Open Source Project (AOSP) Security docs

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-066` | **Phase 7:** Specialized  
> **Est. study:** 6-8h | **Level:** Advanced  
> **Prerequisites:** LC-054, LC-047  
> **Book map:** Elenkov Â Android Security Internals (full)
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Architecture Stack | Lapisan keamanan Android | Android security stack | Androidセキュリティ階層 |
| 2 | UID Sandbox | Isolasi UID & DAC | Application sandbox & DAC | UIDサンドボックス |
| 3 | Permissions Model | Izin install-time & runtime | Permission model | パーミッションモデル |
| 4 | Components & Intents | Activity, Service, Receiver, Provider | Components & Intent safety | コンポーネントとIntent |
| 5 | Binder IPC | Binder, AIDL, identity | Binder IPC & identity | Binder IPC |
| 6 | SELinux Overview | MAC & domain policy | SELinux on Android | SELinux概要 |
| 7 | Storage & Crypto | Keystore, encrypted FS | Secure storage | 安全なストレージ |
| 8 | App Review Method | Metodologi review APK | Secure coding & review | アプリレビュー手法 |
| 9 | Common Weak Classes | Kelas kelemahan umum | Vulnerability classes | 代表的な弱点クラス |
| 10 | Cheatsheet | ADB & review CLI | Lab cheatsheet | チートシート |

---

## 1. 🏗️ Android Security Architecture Stack

### 🇮🇩 Bahasa Indonesia
Android adalah sistem berlapis di atas kernel Linux yang dikustomisasi. Keamanan tidak bergantung pada satu kontrol, melainkan **defense in depth** (Elenkov, Ch.1–2):

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

### 🇬🇧 English
Each layer assumes the layer above may be compromised. Compromise of one app should not imply compromise of another app, of system services, or of the kernel — that is the design goal of the sandbox + MAC stack.

### 🇯🇵 日本語
上位層が侵害されても下位層が被害を限定する設計です。アプリアイソレーションとMACが中核になります。

---

## 2. 🧱 Application Sandbox — Unique UID Isolation

### 🇮🇩 Bahasa Indonesia
Pada instalasi, Package Manager mengalokasikan **Linux UID unik** per aplikasi (contoh: `u0_a145` → UID `10145`). Data privat hidup di:

$$
\mathsf{AppData}(pkg) = /\mathsf{data}/\mathsf{data}/pkg/
$$

dengan ownership $(uid_{pkg}, uid_{pkg})$ dan mode tipikal `0700`.

**Model formal isolasi (DAC):**

$$
\mathsf{Access}(A \rightarrow B.\mathsf{data}) = \mathsf{true}
\iff uid_A = uid_B \lor \mathsf{sharedUserId} \land \mathsf{sameSigningKey}
$$

`sharedUserId` sudah **deprecated** pada API modern — hindari pada desain baru. Isolasi diperkuat ART/process isolation: satu proses per app (kecuali multi-process eksplisit di manifest).

### 🇬🇧 English
Sandbox failure modes to watch in review: world-readable files, `MODE_WORLD_*` legacy flags, exported components that proxy privileged data, and misuse of `sharedUserId` / matching signing keys across apps.

### 日本語
レビューでは世界読取可能ファイル、エクスポート過剰なコンポーネント、同一署名キー共有を重点確認します。

| Kontrol | Lapisan | Fungsi |
|:---|:---|:---|
| Unique UID | Kernel DAC | Isolasi file & process |
| Process isolation | Zygote/ART | Crash & memory boundary |
| SELinux domain | MAC | Batasi bahkan root/system paths |
| seccomp | Kernel | Filter syscall berbahaya |

---

## 3. 🔐 Permissions Model

### 3.1 Klasifikasi
| Kelas | Contoh | Kapan diminta | Risiko jika disalahgunakan |
|:---|:---|:---|:---|
| Normal | `INTERNET`, `VIBRATE` | Install-time auto | Relatif rendah |
| Dangerous | `CAMERA`, `READ_CONTACTS` | Runtime prompt | Privasi tinggi |
| Signature | System-only APIs | Same signing cert | Privilege bridge |
| Special | `SYSTEM_ALERT_WINDOW` | Settings grant | Overlay / phishing UI |

### 🇮🇩 Bahasa Indonesia
Prinsip **least privilege**: minta izin minimal yang dibutuhkan fitur. Di review, petakan setiap permission ke *use-case* konkret. Permission tanpa justifikasi = smell.

Deklarasi di `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Runtime (API 23+): cek `checkSelfPermission` → `requestPermissions` → handle denial gracefully (jangan force-crash).

### 🇬🇧 English
Over-permissioning expands blast radius after compromise. Treat permission grants as part of the app’s trust boundary documentation.

### 日本語
過剰な権限要求は侵害時の被害半径を広げます。権限は信頼境界の一部として文書化します。

---

## 4. 📦 Components, Export Surface & Intents

Android punya empat komponen inti:

| Komponen | Peran | Risiko ekspor |
|:---|:---|:---|
| **Activity** | UI entry | Deep-link hijack, task affinity abuse |
| **Service** | Background work | Unauthorized start/bind |
| **BroadcastReceiver** | Event listener | Spoofed broadcasts |
| **ContentProvider** | Data sharing | SQLi / path traversal / IDOR |

**Aturan aman default:**

$$
\mathsf{exported} = 
\begin{cases}
\mathsf{false} & \text{jika tidak perlu diakses luar app} \\
\mathsf{true} + \mathsf{permission} & \text{jika IPC publik diperlukan}
\end{cases}
$$

Intent = pesan IPC. Intent **eksplisit** menargetkan komponen pasti; Intent **implisit** memakai action/category/data — lebih rawan hijacking jika tidak diproteksi.

```
App A ──Intent──▶ ActivityManager ──resolve──▶ App B component
                      │
                      └─ enforce: exported? permission? caller UID?
```

> **Defense:** jangan ekspor Activity sensitif; validasi semua extra; gunakan `PendingIntent` dengan flag immutability di API modern; batasi deep link dengan App Links + autoVerify.

---

## 5. 🔗 Binder IPC — Identity & AIDL

### 🇮🇩 Bahasa Indonesia
**Binder** adalah bus IPC utama Android (Elenkov, Ch.6). Setiap transaksi membawa identitas pemanggil yang dapat diverifikasi di sisi service:

$$
\begin{aligned}
uid_{caller} &= \mathsf{Binder.getCallingUid}() \\
pid_{caller} &= \mathsf{Binder.getCallingPid}()
\end{aligned}
$$

Service yang mengekspos AIDL **wajib** memvalidasi UID/permission sebelum operasi privileged. Jangan percaya parameter dari client tanpa otorisasi.

### 🇬🇧 English
Binder identity is the cornerstone of Android IPC trust. A common design bug is performing privileged work based solely on “the binder call arrived,” without checking caller identity or holding a signature/dangerous permission.

### 日本語
Binder呼び出しが来ただけでは不十分です。呼び出し元UIDと権限を必ず検証します。

| Pola aman | Pola berbahaya |
|:---|:---|
| `enforceCallingPermission(...)` | Trust-all binder stubs |
| Signature permission on service | Exported service, no permission |
| Clear calling identity only when needed | Permanent identity clearing bugs |
| Input validation on Parcel fields | Blind deserialize / path from client |

---

## 6. 🛡️ SELinux on Android — MAC Overview

### 🇮🇩 Bahasa Indonesia
SELinux menambah **Mandatory Access Control** di atas DAC. Setiap proses punya **security context** (user:role:type:sensitivity). Kebijakan type-enforcement memutuskan apakah domain $D$ boleh operasi $op$ pada tipe objek $T$:

$$
\mathsf{Allow}(D, T, op) \in \mathsf{Policy}
$$

Mode produksi Android: **Enforcing**. `permissive` hanya untuk debugging perangkat milik sendiri.

Konsep penting bagi developer/reviewer:
- App pihak ketiga biasanya di domain `untrusted_app` (versi bervariasi per API level).
- Vendor/system services punya domain lebih sempit.
- Kebijakan di-compile ke binary; audit denial muncul di `logcat` / `dmesg` sebagai `avc: denied`.

### 🇬🇧 English
SELinux is not a substitute for app-level permission checks; it is a backstop that limits damage when DAC or framework bugs occur. Understanding domains helps explain “why can’t this app open that device node?” without inventing kernel bypass recipes.

### 日本語
SELinuxはDACの代替ではなく、侵害時の被害を抑える後段防御です。

```
untrusted_app ──X──▶ /dev/block/*     (typical deny)
system_server ──✓──▶ framework sockets (policy allow)
```

---

## 7. 🔑 Secure Storage & Cryptography APIs

| Mekanisme | Fungsi | Catatan defense |
|:---|:---|:---|
| **Android Keystore** | Hardware-backed keys (TEE/StrongBox bila ada) | Jangan ekstrak key material ke app memory kecuali perlu |
| **EncryptedSharedPreferences / Jetpack Security** | Preferensi terenkripsi | Lebih baik dari SharedPreferences plaintext |
| **SQLCipher / encrypted Room** | DB at rest | Kunci dari Keystore, bukan hardcode |
| **File-Based Encryption (FBE)** | Enkripsi filesystem perangkat | CE vs DE storage contexts |
| **Network Security Config** | TLS trust anchors, cleartext policy | Blokir cleartext di production |

**Anti-pattern:** menyimpan token/API key di `SharedPreferences` plaintext, di resource XML, atau di string konstanta dalam DEX.

$$
\mathsf{Secret}_{ok} \subseteq \mathsf{Keystore}\ \cup\ \mathsf{server\text{-}side}
$$

---

## 8. 🔍 Application Security Review Methodology

Metodologi **defense-oriented** (bukan bypass playbook):

### 8.1 Static review pipeline
1. **Inventory** — package name, min/target SDK, permissions, exported components.
2. **Manifest threat model** — setiap `exported=true` butuh owner + permission story.
3. **Code paths** — WebView settings, crypto usage, file I/O, IPC handlers, deep links.
4. **Third-party SDK** — trackers, ads, unexpected permission proxies.
5. **Secrets scan** — API keys, private URLs, debug endpoints.

Alat lab umum (analisis milik sendiri / izin eksplisit): `aapt`/`aapt2`, `apkanalyzer`, **JADX**, **APKTool** (untuk memahami resource/smali), `dexdump`.

### 8.2 Dynamic review (owned device / emulator)
- Exercise auth flows; inspect traffic dengan proxy **hanya** pada build debug milik Anda.
- Verifikasi Keystore usage, backup flags (`allowBackup`), dan logging berlebih.
- Uji denial-of-permission paths dan error handling.

### 8.3 Secure coding checklist (developer)
| Kontrol | Praktik |
|:---|:---|
| Input | Validasi Intent extras, URI, provider queries (parameterized) |
| WebView | `setJavaScriptEnabled` hanya bila perlu; batasi `addJavascriptInterface` |
| Crypto | Android Keystore + AES-GCM; larang ECB & hard-coded IV |
| IPC | Least-export; permission-gated services |
| Logging | Tidak log PII/token |
| Backup | `android:allowBackup="false"` bila data sensitif |
| Cleartext | `cleartextTrafficPermitted=false` |

> **Hard rule (edukasi):** catatan ini **tidak** mencakup resep bypass SSL pinning, Frida hook untuk melemahkan TLS, atau prosedur root exploit. Fokus: arsitektur, review, dan hardening.

---

## 9. ⚠️ Common Weakness Classes (Konsep)

| Kelas | Gejala | Mitigasi |
|:---|:---|:---|
| Insecure data at rest | Token di prefs/DB plaintext | Keystore + encrypted storage |
| Over-exported components | Activity/Service tanpa permission | `exported=false` / signature perm |
| Intent redirection | Proxy Intent dari caller | Jangan forward Intent mentah; allowlist |
| Path traversal in Provider | `../` di query path | Canonicalize + root jail |
| SQL injection in Provider | String concat query | Selection args parameterized |
| Tapjacking / overlay | UI obscured | `filterTouchesWhenObscured`, modern overlay limits |
| Weak TLS config | Cleartext / trust-all TrustManager | Network Security Config; never trust-all |
| Debuggable release | `android:debuggable=true` | Pastikan release non-debuggable |

---

## 10. 🛠️ Lab Cheatsheet (Perangkat / Emulator Milik Sendiri)

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

## 🔐 Security Notes — Threats & Defenses

| Ancaman | Mekanisme | Pertahanan |
|:---|:---|:---|
| Cross-app data theft | Weak DAC / world-readable | Strict sandbox; no MODE_WORLD_* |
| Confused deputy | Exported proxy components | Permission + validate caller |
| Secret leakage | Logging, backup, DEXstrings | Keystore; scrub logs; allowBackup=false |
| MITM on mobile API | Cleartext / broken trust | TLS + NSC; pin hanya dengan ops maturity |
| Privilege abuse | Over-broad permissions | Least privilege; runtime UX clarity |
| Policy bypass hopes | “Disable SELinux” folklore | Keep Enforcing; fix app design |

---

> 📚 **References & Book Sources**
> - Nikolay Elenkov — *Android Security Internals: An In-Depth Guide to Android’s Security Architecture* — `~/Documents/Books/CyberSec/Android/`
> - AOSP — Security & SELinux documentation; Android Developers — Security best practices
> - OWASP Mobile Application Security (MAS) / MASVS — verification categories

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> ⚖️ Hanya untuk edukasi, review aplikasi milik sendiri, dan pengujian berizin. Tidak untuk akses tidak sah.
