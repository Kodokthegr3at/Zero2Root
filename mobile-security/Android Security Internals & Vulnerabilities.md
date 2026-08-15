# 📱 Android Security Internals & Vulnerabilities

> **LearnCybersecurity** | Mobile Application Security Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---

## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Architecture & Sandbox | Arsitektur Android & Application Sandbox | Android Security Architecture & UID Isolation | Androidセキュリティアーキテクチャとサンドボックス |
| 2 | Component Security | 4 Komponen: Activity, Service, Receiver, Provider | Core Android Components & Intent Filters | Androidの4大コンポーネントとIntentセキュリティ |
| 3 | IPC & Binder | Mekanisme Binder & AIDL Security | Inter-Process Communication (Binder & AIDL) | プロセス間通信（Binder）と権限検証 |
| 4 | Reverse Engineering | Decompilation (JADX, APKTool) & Smali | Decompilation, APKTool, JADX & Smali Code | APK逆コンパイル（JADX/APKTool）とSmali解析 |
| 5 | Dynamic Instrumentation | Hooking fungsi menggunakan Frida | Dynamic Instrumentation & Frida Hooking | Fridaによる動的計装と関数フック |
| 6 | Common Vulnerabilities | Insecure storage, Intent Redirection, Tapjacking | High-Risk Android Vulnerability Patterns | 代表的なAndroid脆弱性と悪用例 |
| 7 | Cheatsheet | Perintah ADB & Frida cheatsheet | ADB, APKTool & Frida CLI Cheatsheet | ADB・APKTool・Fridaチートシート |

---

## 1. 🏗️ Android Security Architecture & Application Sandbox

### 🇮🇩 Bahasa Indonesia
Android dibangun di atas kernel Linux yang dimodifikasi. Keamanan inti Android bertumpu pada **Application Sandbox**:
- Setiap aplikasi Android yang diinstal diberikan **Linux User ID (UID)** yang unik (misal `u0_a145` / UID `10145`).
- Setiap aplikasi berjalan di dalam proses proses Virtual Machine (ART - Android Runtime) terpisah.
- Berdasarkan model izin standar Linux (DAC), aplikasi A tidak dapat membaca data di direktori privat aplikasi B (`/data/data/com.target.app/`), kecuali jika kedua aplikasi ditandatangani dengan sertifikat pengembang yang sama dan berbagi `sharedUserId`.
- Lapisan pertahanan tambahan diperkuat oleh **SELinux (Security-Enhanced Linux)** dalam mode *Enforcing* (MAC - Mandatory Access Control) dan *seccomp* system call filters.

### 🇬🇧 English
Android is architected on top of a customized Linux kernel. Android's core isolation mechanism is the **Application Sandbox**:
- Each installed Android application is assigned a unique, dedicated **Linux User ID (UID)** (e.g., `u0_a145` / UID `10145`).
- Each application executes within an isolated process running its own instance of the Android Runtime (ART).
- Under Linux Discretionary Access Control (DAC), App A is strictly forbidden from accessing private files of App B (`/data/data/com.target.app/`), unless both apps are signed with identical developer keys and declare a `sharedUserId`.
- This baseline is augmented by **SELinux (Security-Enhanced Linux)** in *Enforcing* mode (Mandatory Access Control) and kernel *seccomp* filters.

### 🇯🇵 日本語
AndroidはカスタマイズされたLinuxカーネル上に構築されており、そのセキュリティ基盤は**アプリケーションサンドボックス**に基づいています：
- インストールされた各アプリには一意の**LinuxユーザーID（UID）**（例：`u0_a145`）が割り当てられます。
- 各アプリは独立したプロセスおよびAndroid Runtime（ART）インスタンス内で実行されます。
- Linuxのアクセス制御（DAC）により、アプリAはアプリBのプライベート領域（`/data/data/com.target.app/`）にアクセスできません。
- さらに、**SELinux（Enforcingモード）**と*seccomp*システムコールフィルターによってカーネルレベルの多層防御が実現されています。

```
┌─────────────────────────────────────────────────────────────┐
│                 ANDROID SYSTEM ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────┤
│ Applications        │ System Apps & Third-Party Apps (APK)  │
├─────────────────────┼───────────────────────────────────────┤
│ Application Frame.  │ Activity Mgr, Package Mgr, Content Mgr│
├─────────────────────┼───────────────────────────────────────┤
│ Android Runtime     │ ART (Ahead-of-Time / JIT Compiler)    │
│ & Core Libraries    │ Bionic Libc, OpenSSL/BoringSSL, SQLite│
├─────────────────────┼───────────────────────────────────────┤
│ Hardware Abstract.  │ HAL Modules (Camera, Audio, Bluetooth)│
├─────────────────────┼───────────────────────────────────────┤
│ Linux Kernel        │ Drivers, Binder IPC, SELinux, Memory  │
└─────────────────────┴───────────────────────────────────────┘
```

---

## 2. 🧩 The 4 Core Android Components & Security

```
┌────────────────────────────────────────────────────────────────────────┐
│                      4 CORE ANDROID COMPONENTS                         │
├───────────────────┬───────────────────────────────┬────────────────────┤
│ Component         │ Function                      │ Security Concern   │
├───────────────────┼───────────────────────────────┼────────────────────┤
│ **Activity**      │ Antarmuka UI layar pengguna   │ Exported Activity  │
│ **Service**       │ Tugas latar belakang (audio)  │ Unprotected binder │
│ **Broadcast Rcv** │ Penerima event sistem/aplikasi│ Broadcast injection│
│ **Content Prov.** │ Berbagi basis data terstruktur│ SQLi & Path Trav.  │
└───────────────────┴───────────────────────────────┴────────────────────┘
```

### 🚨 Exported Component Vulnerability (`android:exported="true"`)
Jika sebuah komponen di `AndroidManifest.xml` dideklarasikan `exported="true"` (atau memiliki `<intent-filter>` tanpa secara eksplisit menetapkan `exported="false"`), aplikasi pihak ketiga yang tidak memiliki hak dapat memanggil komponen tersebut secara langsung melalui Intent!

```xml
<!-- VULNERABLE: Admin Activity exported to all third-party apps -->
<activity android:name=".AdminSettingsActivity" android:exported="true" />
```

```bash
# Attacker triggers private exported admin screen via ADB
adb shell am start -n com.target.app/.AdminSettingsActivity
```

---

## 3. 🔄 Inter-Process Communication (IPC) & Binder

### 🇮🇩 Bahasa Indonesia
Karena setiap aplikasi terisolasi dalam UID yang berbeda, semua komunikasi antar-proses (IPC) di Android menggunakan driver kernel khusus bernama **Binder**:
1. Client mengirim pesan transaksi `transact()` melalui interface proxy.
2. Driver `/dev/binder` di kernel memvalidasi PID dan UID pengirim (`IPCThreadState::getCallingUid()`).
3. Server memproses transaksi di fungsi `onTransact()`.
4. Jika server lupa memverifikasi UID atau custom permission di `onTransact()`, penyerang lokal dapat mengeksekusi fungsi server berhak tinggi (*Privilege Escalation*).

---

## 4. 🔬 APK Reverse Engineering & Decompilation

```bash
# ── STEP 1: PULL APK FROM DEVICE VIA ADB ─────────────────────
adb shell pm path com.target.app
adb pull /data/app/~~.../base.apk app.apk

# ── STEP 2: DISASSEMBLE RESOURCES & SMALI CODE (APKTOOL) ─────
apktool d app.apk -o decompiled_app/

# ── STEP 3: DECOMPILE DEX TO JAVA SOURCE CODE (JADX) ─────────
jadx-gui app.apk
# Or CLI decompilation:
jadx -d source_code/ app.apk

# ── STEP 4: REPACKAGING & SIGNING MODIFIED APK ───────────────
apktool b decompiled_app/ -o modified.apk
keytool -genkey -v -keystore test.keystore -alias test -keyalg RSA -keysize 2048 -validity 10000
apksigner sign --ks test.keystore --ks-pass pass:password modified.apk
```

---

## 5. 💉 Dynamic Instrumentation with Frida

**Frida** memungkinkan injeksi skrip JavaScript ke dalam proses aplikasi Android yang sedang berjalan untuk memanipulasi memori, mem-bypass SSL Pinning, dan mengabaikan root detection secara real-time.

```javascript
// ── FRIDA SCRIPT: UNIVERSAL ANDROID SSL PINNING BYPASS ────────
Java.perform(function () {
    console.log("[*] Injecting Universal SSL Pinning Bypass...");

    var TrustManagerImpl = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    TrustManagerImpl.verifyChain.implementation = function (untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
        console.log("[+] Intercepted and bypassed SSL Pinning for host: " + host);
        return untrustedChain;
    };
});
```

```bash
# ── LAUNCH FRIDA ON DEVICE ───────────────────────────────────
adb push frida-server /data/local/tmp/
adb shell "chmod 755 /data/local/tmp/frida-server && /data/local/tmp/frida-server &"

# Hook target app with script
frida -U -f com.target.app -l bypass_ssl.js --no-pause
```

---

## 6. 🚨 Critical Android Vulnerability Vectors

### 1. Insecure Local Data Storage
- Kredensial, API key, atau token sesi disimpan dalam format plaintext di `SharedPreferences` (`/data/data/com.target.app/shared_prefs/*.xml`) atau database SQLite tanpa enkripsi (SQLCipher).
- Backup data diizinkan secara default (`android:allowBackup="true"`), memungkinkan ekstraksi data pribadi melalui `adb backup`.

### 2. Intent Redirection & Injection
Aplikasi menerima Intent dari sumber luar dan meneruskannya ke fungsi `startActivity()` tanpa memvalidasi tujuan akhir, memungkinkan penyerang mengakses internal non-exported activities atau mencuri file internal via `FileProvider`.

---

## 7. 🧠 Quick Reference Cheatsheet

```bash
# ── ADB RECONNAISSANCE ───────────────────────────────────────
adb devices                    # List attached devices / emulators
adb logcat | grep -iE "token|pass|http" # Monitor real-time logs
adb shell dumpsys package com.target.app # Inspect app permissions & components

# ── CONTENT PROVIDER QUERYING ────────────────────────────────
adb shell content query --uri content://com.target.app.provider/users
```

---

> 📚 **References & Book Sources:**
> - Nikolay Elenkov — *Android Security Internals: An In-Depth Guide to Android's Security Architecture* (`~/Documents/Books/CyberSec/Android/`)
> - David Kennedy et al. — *Metasploit: The Penetration Tester's Guide* (`~/Documents/Books/CyberSec/Android/`)
> - [OWASP Mobile Application Security (MASVS & MASTG)](https://mas.owasp.org/)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
