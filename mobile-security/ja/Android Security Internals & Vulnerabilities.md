# Androidセキュリティ内部構造とアプリケーションの堅牢化

> **LearnCybersecurity** | モバイルアプリケーションセキュリティシリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at
> 主要参考文献: Nikolay Elenkov『Android Security Internals』、Android Open Source Project(AOSP)のセキュリティ文書

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-066` | **フェーズ7:** 専門分野
> **想定学習時間:** 6-8時間 | **レベル:** 上級
> **前提:** LC-054, LC-047
> **書籍対応:** Elenkov, Android Security Internals(全体)
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック |
|---|-------|
| 1 | Androidセキュリティアーキテクチャの階層 |
| 2 | UIDサンドボックスとDAC分離 |
| 3 | パーミッションモデル |
| 4 | コンポーネントとIntent |
| 5 | Binder IPC |
| 6 | SELinuxの概要 |
| 7 | ストレージと暗号 |
| 8 | アプリケーションレビューの方法論 |
| 9 | よくある弱点のクラス |
| 10 | チートシート |

---

## 重要な用語

この教材でよく出てくる言葉である。

| 用語 | 意味 |
|:---|:---|
| アプリサンドボックス | 各アプリが独自のLinuxユーザーとして隔離されて動く |
| UID | Androidが各アプリに割り当てる固有のLinuxユーザーID |
| パーミッション | アプリが要求すべき権限(カメラ、位置、SMS) |
| コンポーネント | アプリの構成要素(アクティビティ、サービス、コンテントプロバイダ) |
| エクスポートされたコンポーネント | 他アプリから到達できるコンポーネント — 不注意だと攻撃対象 |
| Binder | Androidの主要なアプリ間メッセージ(IPC)のしくみ |
| APK | Androidアプリが配布されるパッケージファイル |
| Keystore | アプリの鍵や秘密を安全に保管する場所 |

---

## 1. Androidセキュリティアーキテクチャの階層

AndroidはカスタマイズされたLinuxカーネルの上に構築された階層型システムだ。そのセキュリティは単一の制御に依存するのではなく、多層防御によって成り立っている(Elenkov, 第1-2章)。

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

各層は、その上の層がすでに侵害されている可能性を前提としている。一つのアプリが侵害されても、それが別のアプリやシステムサービス、カーネルの侵害を意味してはならない。これがサンドボックスとMACを組み合わせた設計の目的だ。上位層が破られても、下位層が被害を限定する。アプリの分離とMACがこの設計の中核をなしている。

---

## 2. アプリケーションサンドボックス: ユニークなUIDによる分離

インストール時に、Package Managerは各アプリケーションにユニークなLinux UIDを割り当てる(例: `u0_a145`はUID `10145`に対応する)。アプリのプライベートデータは次の場所に置かれる。

```text
/data/data/<package name>/
```

所有者は(uid_pkg, uid_pkg)で、典型的なモードは`0700`だ。

分離の形式モデル(DAC):

アプリAがアプリBのプライベートデータを読めるのは、両者が同じUIDで動いている場合だけだ。それは、両方が `sharedUserId` を使い、同じ鍵で署名されているときにしか起きない。

`sharedUserId`は現行のAPIレベルでは非推奨であり、新規設計では避けるべきだ。分離はさらにARTとプロセス分離によっても補強されている。マニフェストでマルチプロセスが明示的に宣言されていない限り、アプリごとに1プロセスとなる。

レビュー時に注意すべきサンドボックスの失敗パターンには、world-readableなファイル、旧来の`MODE_WORLD_*`フラグ、権限を要する処理をプロキシしてしまうエクスポート済みコンポーネント、複数アプリ間での`sharedUserId`や署名鍵の共有などがある。実務上、レビュアーが最もよく確認するのはworld-readableなファイル、過剰にエクスポートされたコンポーネント、そして同一の署名鍵を共有するアプリの存在だ。

| コントロール | 層 | 機能 |
|:---|:---|:---|
| ユニークUID | カーネルDAC | ファイルとプロセスの分離 |
| プロセス分離 | Zygote/ART | クラッシュとメモリの境界 |
| SELinuxドメイン | MAC | rootやシステムのパスすら制限する |
| seccomp | カーネル | 危険なシステムコールをフィルタする |

---

## 3. パーミッションモデル

### 3.1 分類

| クラス | 例 | 要求されるタイミング | 悪用された場合のリスク |
|:---|:---|:---|:---|
| Normal | `INTERNET`, `VIBRATE` | インストール時に自動付与 | 比較的低い |
| Dangerous | `CAMERA`, `READ_CONTACTS` | 実行時のプロンプト | プライバシーへの影響が大きい |
| Signature | システム専用API | 同一の署名証明書 | 権限の高い領域への橋渡し |
| Special | `SYSTEM_ALERT_WINDOW` | 設定画面から付与 | オーバーレイ/UIフィッシング |

最小権限の原則: 機能が実際に必要とする権限だけを要求する。レビューでは、各パーミッションを具体的なユースケースに対応付ける。明確な根拠のないパーミッションは危険信号だ。

`AndroidManifest.xml`での宣言:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

実行時パーミッション(API 23以降)では、`checkSelfPermission`を呼び、続いて`requestPermissions`を呼び、拒否された場合も強制的にクラッシュさせず適切に処理する。

過剰な権限要求は、侵害が起きた際の被害範囲を広げる。すべてのパーミッション付与を、アプリの信頼境界を示すドキュメントの一部として扱うべきだ。

---

## 4. コンポーネント、エクスポート面、Intent

Androidには4つの中核コンポーネントがある。

| コンポーネント | 役割 | エクスポート時のリスク |
|:---|:---|:---|
| Activity | UIのエントリポイント | ディープリンクの乗っ取り、task affinityの悪用 |
| Service | バックグラウンド処理 | 権限のないstart/bind |
| BroadcastReceiver | イベントリスナー | 偽装されたブロードキャスト |
| ContentProvider | データ共有 | SQLインジェクション/パストラバーサル/IDOR |

安全なデフォルトルール:

```text
アプリ外から呼ばれる必要がない   → exported = false
公開IPCが本当に必要              → exported = true + パーミッション
```

IntentはIPCメッセージだ。明示的Intentは特定のコンポーネントを直接指定する。暗黙的Intentはaction/category/dataのマッチングに依存し、保護がなければ乗っ取りに対してより無防備になる。

```
App A ──Intent──▶ ActivityManager ──resolve──▶ App B component
                      │
                      └─ enforce: exported? permission? caller UID?
```

対策: 機微なActivityはエクスポートしない、すべてのextraを検証する、現行APIでは不変性フラグ付きの`PendingIntent`を使う、App Linksとautoverifyでディープリンクを制限する。

---

## 5. Binder IPC: 識別情報とAIDL

BinderはAndroidの主要なIPCバスだ(Elenkov, 第6章)。すべてのトランザクションは、サービス側で検証可能な呼び出し元の識別情報を伴う。

```text
uid_caller = Binder.getCallingUid()
pid_caller = Binder.getCallingPid()
```

AIDLインターフェースを公開するサービスは、権限を要する操作を実行する前に、呼び出し元のUIDやパーミッションを必ず検証しなければならない。認可なしにクライアントから渡されたパラメータを信用してはならない。

Binderの識別情報は、AndroidにおけるIPC信頼の基盤だ。よくある設計上のバグは、呼び出し元の識別情報を確認したり、署名パーミッションやdangerousパーミッションを要求したりすることなく、「Binder呼び出しが来た」というだけで権限を要する処理を実行してしまうことだ。Binder呼び出しが届いたという事実だけでは認可の証明にはならず、呼び出し元のUIDとパーミッションは常に検証する必要がある。

| 安全なパターン | 危険なパターン |
|:---|:---|
| `enforceCallingPermission(...)` | あらゆる呼び出し元を信用するBinderスタブ |
| サービスに設定されたsignatureパーミッション | パーミッションなしでエクスポートされたサービス |
| 必要なときだけcalling identityをクリアする | identityを恒久的にクリアしてしまうバグ |
| Parcelフィールドの入力検証 | 盲目的なデシリアライズ、クライアントから直接取ったパス |

---

## 6. AndroidにおけるSELinux: MACの概要

SELinuxはDACの上にMandatory Access Controlを追加する。すべてのプロセスはセキュリティコンテキスト(user:role:type:sensitivity)を持つ。Type Enforcementポリシーは、ドメインDがオブジェクトタイプTに対して操作opを行えるかどうかを決定する。

ポリシーに明示的に許可するルールがある操作だけが許され、それ以外はすべて拒否される。

Androidの本番モードはEnforcingだ。`permissive`モードは、自分が所有する端末でのデバッグ目的にのみ使う。

開発者やレビュアーが知っておくべき概念:

- サードパーティアプリは通常`untrusted_app`ドメインで動作する(具体的なバージョンはAPIレベルによって異なる)。
- ベンダーやシステムのサービスは、はるかに狭いドメインで動作する。
- ポリシーはバイナリにコンパイルされており、拒否は`logcat`/`dmesg`に`avc: denied`として現れる。

SELinuxはアプリケーションレベルのパーミッションチェックの代替ではない。DACやフレームワークにバグがあった場合に被害を限定するための後段の防御だ。SELinuxのドメインを理解しておくと、カーネルの回避方法をでっち上げることなく、「なぜこのアプリはあのデバイスノードを開けないのか」といった疑問に答えられるようになる。

```
untrusted_app ──X──▶ /dev/block/*     (typical deny)
system_server ──✓──▶ framework sockets (policy allow)
```

---

## 7. 安全なストレージと暗号API

| メカニズム | 機能 | 防御上の注意 |
|:---|:---|:---|
| Android Keystore | ハードウェアに裏付けられた鍵(利用可能であればTEE/StrongBox) | 本当に必要な場合を除き、鍵material をアプリのメモリに取り出さない |
| EncryptedSharedPreferences / Jetpack Security | 暗号化されたpreferences | プレーンテキストのSharedPreferencesより優れている |
| SQLCipher / 暗号化されたRoom | 保存データベースの暗号化 | 鍵はハードコードせずKeystoreから取得する |
| File-Based Encryption(FBE) | デバイスのファイルシステム暗号化 | CEストレージとDEストレージの文脈の違いに注意する |
| Network Security Config | TLSトラストアンカー、cleartextポリシー | 本番環境ではcleartextをブロックする |

アンチパターン: トークンやAPIキーを、プレーンテキストの`SharedPreferences`、XMLリソース、あるいはDEX内のハードコードされた文字列定数として保存すること。

秘密情報を置いてよいのは、Android Keystoreかサーバー側だけだ。

---

## 8. アプリケーションセキュリティレビューの方法論

この方法論は防御志向であり、回避手順のプレイブックではない。

### 8.1 静的レビューのパイプライン

1. インベントリ: パッケージ名、min/target SDK、パーミッション、エクスポートされたコンポーネント。
2. マニフェストの脅威モデル: `exported=true`にはすべて所有者と明確なパーミッションの根拠が必要。
3. コードパス: WebView設定、暗号の使い方、ファイルI/O、IPCハンドラ、ディープリンク。
4. サードパーティSDK: トラッカー、広告、予期しないパーミッションのプロキシ。
5. シークレットのスキャン: APIキー、非公開URL、デバッグ用エンドポイント。

一般的なラボツール(自分のアプリの分析、または明示的な許可がある場合): `aapt`/`aapt2`、`apkanalyzer`、JADX、APKTool(リソース/smaliの理解用)、`dexdump`。

### 8.2 動的レビュー(自分の端末/エミュレータ)

- 認証フローを実際に動かし、自分のデバッグビルドに限ってプロキシでトラフィックを検査する。
- Keystoreの使い方、`allowBackup`フラグ、過剰なロギングを確認する。
- パーミッション拒否時の経路とエラーハンドリングをテストする。

### 8.3 セキュアコーディングのチェックリスト(開発者向け)

| コントロール | プラクティス |
|:---|:---|
| 入力 | Intent extra、URI、provider クエリ(パラメータ化)を検証する |
| WebView | `setJavaScriptEnabled`は必要な場合のみ有効化し、`addJavascriptInterface`を制限する |
| 暗号 | Android Keystore + AES-GCM。ECBとハードコードされたIVは禁止する |
| IPC | エクスポートを最小限にし、サービスにパーミッションを設定する |
| ロギング | PIIやトークンをログに出さない |
| バックアップ | 機微なデータがある場合は`android:allowBackup="false"` |
| Cleartext | `cleartextTrafficPermitted=false` |

厳格なルール(教育目的): この資料はSSLピニングの回避手順、TLSを弱体化させるFridaフック、rootエクスプロイトの手順を扱わない。焦点はアーキテクチャ、レビュー、堅牢化にある。

---

## 9. よくある弱点のクラス(概念)

| クラス | 症状 | 緩和策 |
|:---|:---|:---|
| Insecure data at rest | トークンがprefs/DBにプレーンテキストで保存されている | Keystore+暗号化ストレージ |
| 過剰にエクスポートされたコンポーネント | パーミッションのないActivity/Service | `exported=false` / signatureパーミッション |
| Intentリダイレクション | 呼び出し元からの生のIntentをそのまま転送する | 生のIntentを転送しない。許可リストを使う |
| Providerでのパストラバーサル | クエリパス中の`../` | 正規化とルートジェイル |
| Providerでのsqlインジェクション | 文字列連結によるクエリ構築 | パラメータ化されたselection引数 |
| Tapjacking/オーバーレイ | 他の要素にUIが覆われる | `filterTouchesWhenObscured`、最近のオーバーレイ制限 |
| 弱いTLS設定 | Cleartext、またはtrust-allのTrustManager | Network Security Config。trust-allは絶対に使わない |
| デバッグ可能なリリース | `android:debuggable=true` | リリースビルドがデバッグ不可であることを保証する |

---

## 10. ラボチートシート(自分の端末/エミュレータ)

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

## セキュリティノート: 脅威と対策

| 脅威 | メカニズム | 対策 |
|:---|:---|:---|
| アプリ間でのデータ窃取 | 弱いDAC/world-readableなファイル | 厳格なサンドボックス。MODE_WORLD_*を使わない |
| Confused deputy | エクスポートされたプロキシコンポーネント | パーミッションチェックと呼び出し元の検証 |
| シークレットの漏洩 | ロギング、バックアップ、DEX内の文字列 | Keystore、ログの精査、allowBackup=false |
| モバイルAPI通信へのMITM | Cleartext、または壊れた信頼設定 | TLS+NSC。ピニングは運用の成熟度が十分な場合のみ |
| 権限の悪用 | 過度に広いパーミッション | 最小権限、明確な実行時UX |
| ポリシーの回避への期待 | 「SELinuxを無効化すればいい」という俗説 | Enforcingを維持し、アプリの設計を直す |

---

> **参考文献と書籍**
> - Nikolay Elenkov『Android Security Internals: An In-Depth Guide to Android's Security Architecture』`~/Documents/Books/CyberSec/Android/`
> - AOSP, Security & SELinux文書。Android Developers, セキュリティのベストプラクティス
> - OWASP Mobile Application Security(MAS)/MASVS, 検証カテゴリ

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 教育目的、自分自身のアプリケーションのレビュー、許可された範囲でのテストに限定する。不正アクセスを目的とするものではない。
