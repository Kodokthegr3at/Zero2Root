# Android Security Internals & Application Hardening

> **LearnCybersecurity** | Mobile Application Security Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Nikolay Elenkov, *Android Security Internals*; Android Open Source Project (AOSP) Security docs

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-066` | **Phase 7:** Specialized
> **Est. study:** 6-8h | **Level:** Advanced
> **Prerequisites:** LC-054, LC-047
> **Book map:** Elenkov, Android Security Internals (full)
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic |
|---|-------|
| 1 | Android security architecture stack |
| 2 | UID sandbox and DAC isolation |
| 3 | Permission model |
| 4 | Components and Intents |
| 5 | Binder IPC |
| 6 | SELinux overview |
| 7 | Storage and cryptography |
| 8 | Application review methodology |
| 9 | Common weakness classes |
| 10 | Cheatsheet |

---

## 1. Android Security Architecture Stack

Android is a layered system built on top of a customized Linux kernel. Its security does not rely on a single control, but on defense in depth (Elenkov, Ch.1-2):

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

Each layer assumes the layer above it may already be compromised. A compromise of one app should not imply the compromise of another app, of system services, or of the kernel; that is the design goal behind the sandbox and MAC combination. If a higher layer is breached, the layer below limits the damage. App isolation and MAC are the core of this design.

---

## 2. Application Sandbox: Unique UID Isolation

At install time, the Package Manager allocates a unique Linux UID for each application (for example, `u0_a145`, which corresponds to UID `10145`). An app's private data lives at:

```text
/data/data/<package name>/
```

owned by (uid_pkg, uid_pkg), typically with mode `0700`.

Formal isolation model (DAC):

App A can read app B's private data only if both run as the same UID. That only happens when both use `sharedUserId` and are signed with the same key.

`sharedUserId` is deprecated on modern API levels and should be avoided in new designs. Isolation is further reinforced by ART and process isolation: one process per app, unless multi-process is explicitly declared in the manifest.

Sandbox failure modes worth watching for during review include world-readable files, the legacy `MODE_WORLD_*` flags, exported components that proxy privileged data, and misuse of `sharedUserId` or a shared signing key across multiple apps. In practice, the points reviewers check most often are world-readable files, over-exported components, and apps sharing the same signing key.

| Control | Layer | Function |
|:---|:---|:---|
| Unique UID | Kernel DAC | File and process isolation |
| Process isolation | Zygote/ART | Crash and memory boundary |
| SELinux domain | MAC | Restricts even root/system paths |
| seccomp | Kernel | Filters dangerous syscalls |

---

## 3. Permission Model

### 3.1 Classification

| Class | Example | When requested | Risk if misused |
|:---|:---|:---|:---|
| Normal | `INTERNET`, `VIBRATE` | Automatically at install | Relatively low |
| Dangerous | `CAMERA`, `READ_CONTACTS` | Runtime prompt | High privacy impact |
| Signature | System-only APIs | Same signing certificate | Bridges into privileged access |
| Special | `SYSTEM_ALERT_WINDOW` | Granted through Settings | Overlay / UI phishing |

The least-privilege principle: request only the permissions a feature actually needs. During review, map each permission to a concrete use case. A permission with no clear justification is a smell.

Declared in `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

For runtime permissions (API 23+): call `checkSelfPermission`, then `requestPermissions`, and handle denial gracefully rather than force-crashing.

Over-permissioning expands the blast radius after a compromise. Treat every permission grant as part of the app's trust-boundary documentation.

---

## 4. Components, Export Surface, and Intents

Android has four core components:

| Component | Role | Export risk |
|:---|:---|:---|
| Activity | UI entry point | Deep-link hijacking, task-affinity abuse |
| Service | Background work | Unauthorized start/bind |
| BroadcastReceiver | Event listener | Spoofed broadcasts |
| ContentProvider | Data sharing | SQL injection / path traversal / IDOR |

Safe default rule:

```text
not needed from outside the app   → exported = false
public IPC really required        → exported = true + a permission
```

An Intent is an IPC message. An explicit Intent targets a specific component directly; an implicit Intent relies on action/category/data matching, and is more exposed to hijacking if left unprotected.

```
App A ──Intent──▶ ActivityManager ──resolve──▶ App B component
                      │
                      └─ enforce: exported? permission? caller UID?
```

Defense: do not export sensitive Activities, validate all extras, use `PendingIntent` with the immutability flag on modern API levels, and constrain deep links with App Links plus autoVerify.

---

## 5. Binder IPC: Identity and AIDL

Binder is Android's primary IPC bus (Elenkov, Ch.6). Every transaction carries a caller identity that the service side can verify:

```text
uid_caller = Binder.getCallingUid()
pid_caller = Binder.getCallingPid()
```

A service that exposes an AIDL interface must validate the caller's UID or permission before performing any privileged operation. Never trust a parameter coming from the client without authorization.

Binder identity is the foundation of IPC trust on Android. A common design bug is performing privileged work based only on "a binder call arrived," without checking caller identity or requiring a signature or dangerous permission. The mere arrival of a Binder call is not sufficient proof of authorization; the caller's UID and permission must always be verified.

| Safe pattern | Dangerous pattern |
|:---|:---|
| `enforceCallingPermission(...)` | A binder stub that trusts every caller |
| Signature permission on the service | Service exported with no permission |
| Clearing calling identity only when necessary | A bug that clears identity permanently |
| Input validation on Parcel fields | Blind deserialization, or a path taken straight from the client |

---

## 6. SELinux on Android: A MAC Overview

SELinux adds Mandatory Access Control on top of DAC. Every process has a security context (user:role:type:sensitivity). Type enforcement policy decides whether domain D may perform operation op on object type T:

An action is allowed only if the policy contains a rule that explicitly allows it. Everything else is denied.

Android's production mode is Enforcing. `permissive` mode is used only for debugging on a device you own.

Concepts worth knowing for developers and reviewers:

- Third-party apps typically run in the `untrusted_app` domain (the exact version varies by API level).
- Vendor and system services run in far narrower domains.
- The policy is compiled into a binary; denials appear in `logcat`/`dmesg` as `avc: denied`.

SELinux is not a substitute for application-level permission checks. It is a backstop that limits the damage when a DAC bug or a framework bug occurs. Understanding SELinux domains helps answer questions like "why can't this app open that device node?" without having to invent a kernel-bypass method.

```
untrusted_app ──X──▶ /dev/block/*     (typical deny)
system_server ──✓──▶ framework sockets (policy allow)
```

---

## 7. Secure Storage and Cryptography APIs

| Mechanism | Function | Defense notes |
|:---|:---|:---|
| Android Keystore | Hardware-backed keys (TEE/StrongBox where available) | Do not extract key material into app memory unless truly necessary |
| EncryptedSharedPreferences / Jetpack Security | Encrypted preferences | Better than plaintext SharedPreferences |
| SQLCipher / encrypted Room | Database encryption at rest | Key comes from Keystore, not hardcoded |
| File-Based Encryption (FBE) | Device filesystem encryption | Mind the CE vs DE storage contexts |
| Network Security Config | TLS trust anchors, cleartext policy | Block cleartext in production |

Anti-pattern: storing a token or API key in plaintext `SharedPreferences`, in an XML resource, or as a hardcoded string constant inside the DEX.

Secrets belong only in the Android Keystore or on the server.

---

## 8. Application Security Review Methodology

This methodology is defense-oriented, not a bypass playbook.

### 8.1 Static review pipeline

1. Inventory: package name, min/target SDK, permissions, exported components.
2. Manifest threat model: every `exported=true` needs an owner and a clear permission rationale.
3. Code paths: WebView settings, crypto usage, file I/O, IPC handlers, deep links.
4. Third-party SDKs: trackers, ads, unexpected permission proxies.
5. Secrets scan: API keys, private URLs, debug endpoints.

Common lab tools (for analyzing your own apps, or with explicit authorization): `aapt`/`aapt2`, `apkanalyzer`, JADX, APKTool (for understanding resources/smali), `dexdump`.

### 8.2 Dynamic review (your own device or emulator)

- Exercise auth flows and inspect traffic with a proxy, only on your own debug build.
- Verify Keystore usage, the `allowBackup` flag, and excessive logging.
- Test permission-denial paths and their error handling.

### 8.3 Secure coding checklist (developer)

| Control | Practice |
|:---|:---|
| Input | Validate Intent extras, URIs, and provider queries (parameterized) |
| WebView | Enable `setJavaScriptEnabled` only when needed; restrict `addJavascriptInterface` |
| Crypto | Android Keystore plus AES-GCM; ban ECB and hardcoded IVs |
| IPC | Least-export; permission-gated services |
| Logging | Never log PII or tokens |
| Backup | `android:allowBackup="false"` when data is sensitive |
| Cleartext | `cleartextTrafficPermitted=false` |

Hard rule (educational scope): this note does not cover SSL pinning bypass recipes, Frida hooks for weakening TLS, or root exploit procedures. The focus is architecture, review, and hardening.

---

## 9. Common Weakness Classes (Conceptual)

| Class | Symptom | Mitigation |
|:---|:---|:---|
| Insecure data at rest | Token stored in prefs/DB as plaintext | Keystore plus encrypted storage |
| Over-exported components | Activity/Service with no permission | `exported=false` / signature permission |
| Intent redirection | Forwarding a raw Intent from the caller | Do not forward raw Intents; use an allowlist |
| Path traversal in a Provider | `../` in a query path | Canonicalize plus root jail |
| SQL injection in a Provider | Query built with string concatenation | Parameterized selection arguments |
| Tapjacking / overlay | UI obscured by another element | `filterTouchesWhenObscured`, modern overlay restrictions |
| Weak TLS configuration | Cleartext, or a trust-all TrustManager | Network Security Config; never trust-all |
| Debuggable release | `android:debuggable=true` | Ensure release builds are non-debuggable |

---

## 10. Lab Cheatsheet (Your Own Device / Emulator)

```bash
# ── Package & permission inventory ────────────────────────────
adb shell pm list packages -f
adb shell dumpsys package com.example.app | less

# ── Manifest / APK metadata ───────────────────────────────────
aapt dump badging app.apk
aapt dump permissions app.apk
apkanalyzer manifest print app.apk

# ── Decompile for review (your own lab) ───────────────────────
jadx -d out_jadx app.apk
apktool d app.apk -o out_apktool

# ── Logs & SELinux denials (diagnostics) ──────────────────────
adb logcat | grep -E 'avc:|AndroidRuntime|keystore'
adb shell getenforce

# ── Backup flag & debuggable check (inspect, do not abuse) ────
aapt dump xmltree app.apk AndroidManifest.xml | grep -E 'debuggable|allowBackup'
```

---

## Security Notes: Threats and Defenses

| Threat | Mechanism | Defense |
|:---|:---|:---|
| Cross-app data theft | Weak DAC / world-readable files | Strict sandbox; no MODE_WORLD_* |
| Confused deputy | Exported proxy components | Permission checks plus caller validation |
| Secret leakage | Logging, backups, DEX strings | Keystore; scrub logs; allowBackup=false |
| MITM on mobile API traffic | Cleartext, or broken trust | TLS plus NSC; pin only with sufficient ops maturity |
| Privilege abuse | Overly broad permissions | Least privilege; clear runtime UX |
| Hoping to bypass policy | The "just disable SELinux" myth | Keep Enforcing; fix the app design instead |

---

> **References & Book Sources**
> - Nikolay Elenkov, *Android Security Internals: An In-Depth Guide to Android's Security Architecture*, `~/Documents/Books/CyberSec/Android/`
> - AOSP, Security & SELinux documentation; Android Developers, Security best practices
> - OWASP Mobile Application Security (MAS) / MASVS, verification categories

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> For education, review of your own applications, and authorized testing only. Not for unauthorized access.
