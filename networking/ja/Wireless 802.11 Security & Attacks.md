# Wireless 802.11のセキュリティと攻撃

> **LearnCybersecurity** | ネットワーク基礎シリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at
> 主要参考文献: 『802.11 Wireless Networks: The Definitive Guide』、Stallings『Network Security Essentials』、Kurose & Ross『Computer Networking』

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-043` | **フェーズ2:** ネットワーキング
> **想定学習時間:** 5時間 | **レベル:** 上級
> **前提科目:** LC-038
> **書籍対応:** Gast, 802.11 Wireless Networks（全体）、Stallings, Network Security Essentials 第8章
<!-- LC-CURRICULUM-END -->

## 目次

1. 802.11のアーキテクチャとフレーミングの概要
2. セキュリティの変遷（概略）
3. WPA2: PMK、PTK、GTKと4ウェイハンドシェイク
4. WPA3-Personal: SAE（概要レベル）
5. 管理フレームとデオーセンティケーション（DoSの概念）
6. 防御と監視
7. セキュリティノート: 防御のまとめ
8. チートシート

---

## 1. 802.11のアーキテクチャとフレーミングの概要

IEEE 802.11はWLANを定義する。ステーション（STA）、アクセスポイント（AP）、BSS（Basic Service Set）から構成される。同一SSIDを持つ複数のBSSはESSを形成できる。媒体は半二重であり、チャネルアクセスにはCSMA/CA（イーサネットの古典的なCSMA/CDではない）が使われる。

フレームには3つのクラスがある。

| クラス | 役割 | 例 |
|:---|:---|:---|
| Data | LLC/IPのペイロードを運ぶ | QoSデータ |
| Control | 媒体アクセスを補助する | RTS/CTS、ACK |
| Management | メンバーシップとディスカバリ | Beacon、Probe、Auth、Assoc、Deauth、Disassoc |

```
  ┌────────────── ESS / SSID "CORP" ──────────────┐
  │   AP1 (BSS1)              AP2 (BSS2)          │
  │    ↑↑↑                     ↑↑↑                │
  │   STA                      STA                │
  └───────────────────────────────────────────────┘
         │
         └── wired DS (Distribution System) ──► LAN/Internet
```

BeaconはSSID（あるいは隠しSSID）、機能、セキュリティIE（RSN）を告知する。Associationは、ユニキャストデータが暗号化される前（現代のネットワークの場合）に、STAをAPに結びつける。

802.11のヘッダーは、SA/DA/BSSIDを区別するために複数のアドレスフィールド（ToDS/FromDS）を使う。詳細はO'Reillyの書籍『802.11 Wireless Networks』に譲る。

無線は電波の届く範囲で共有されるブロードキャスト媒体である。機密性と完全性は、「屋内にいるかどうか」ではなく、RSNのようなリンク層のセキュリティに依存する。近くにいる受信者は、保護されていない管理フレームや設定の甘いネットワークを聞き取れると常に想定しておくべきである。

---

## 2. セキュリティの変遷（概略）

| 時代 | 仕組み | 実運用上の位置づけ |
|:---|:---|:---|
| Open | リンクの暗号化なし | キャプティブポータル+アプリケーションレベルのTLSにのみ適する |
| WEP | RC4 + 弱いIV | 非推奨/破られている。使用しない |
| WPA-PSK（TKIP） | 過渡的な方式 | レガシー。可能なら避ける |
| WPA2-Personal | PSK + CCMP（AES） | 依然として一般的。弱いPSKはリスクになる |
| WPA2-Enterprise | 802.1X / EAP + RADIUS | オフィス環境の標準 |
| WPA3-Personal | SAE | オフラインでのPSK推測に対する耐性が向上 |
| WPA3-Enterprise | EAP + 192ビットスイートのオプション | 高い保証レベル |

Beacon内のRSN（Robust Security Network）IEは、提供される暗号スイートとAKMを示す。CCMP（AES-CCM）はWPA2で期待されるデータ用暗号であり、GCMPはより新しいPHYやWPA3のコンテキストで登場する。

---

## 3. WPA2: PMK、PTK、GTKと4ウェイハンドシェイク

ハンドシェイクの目的は、長期的な秘密情報から新鮮なセッション鍵を導出し、PSKを平文のまま無線上に送ることなく、双方が同じ秘密を持っていることを確認することである。

PMK（Pairwise Master Key）:

- Personal（PSK）: PMKはパスフレーズとSSIDから導出される（古典的なWPA2-PSKではPBKDF2-HMAC-SHA1を4096回反復）。

$$
\mathsf{PMK} = \mathsf{PBKDF2}(\mathsf{passphrase},\; \mathsf{SSID},\; 4096,\; 256\text{ bits})
$$

- Enterprise: PMKは802.1Xが成功した後のEAP/MSKから得られる（セッション/ユーザーごとであり、共有PSKより優れている）。

PTK（Pairwise Transient Key）は、PMKにnonceとMACアドレスを加えて導出される。

$$
\begin{aligned}
\mathsf{PTK} &= \mathsf{PRF\text{-}X}\big(
  \mathsf{PMK},\;
  \texttt{"Pairwise key expansion"},\\
  &\quad \min(AA,SPA) \,\|\, \max(AA,SPA) \,\|\,
  \min(ANonce,SNonce) \,\|\, \max(ANonce,SNonce)
\big)
\end{aligned}
$$

ここで $AA$ はAPのMAC（BSSID）、$SPA$ はSTAのMACである。PTKは次のように分割される。

| 部分 | 機能 |
|:---|:---|
| KCK | Key Confirmation Key（EAPOL-KeyのMICに使用） |
| KEK | Key Encryption Key（鍵material をラップする） |
| TK | ユニキャストデータのCCMPに使うTemporal Key |

GTK（Group Temporal Key）: APからすべての関連付け済みSTAへのマルチキャスト/ブロードキャスト鍵であり、ハンドシェイク（またはグループキーハンドシェイク）の中でラップされた形で配布される。

### 4ウェイハンドシェイク（EAPOL-Key）: 概念的な流れ

```
  AP                                         STA
   │  Msg1: ANonce                            │
   │─────────────────────────────────────────►│
   │          (STAがPTKを計算。SNonceを保持)   │
   │  Msg2: SNonce + MIC                      │
   │◄─────────────────────────────────────────│
   │  (APがPTKを計算し、MICを検証)             │
   │  Msg3: GTK + MIC + install               │
   │─────────────────────────────────────────►│
   │  Msg4: MIC / Ack                         │
   │◄─────────────────────────────────────────│
   │         CCMP（TK/GTK）で暗号化されたデータ │
```

KCKによるMICの検証は、両者が同じPTKを導出したこと、つまり同じPMKを保持していることを証明する。

WPA2-Personalのセキュリティは、結局のところPSKのエントロピーに依存する。エントロピーの低いパスフレーズは、キャプチャされたハンドシェイクに対するオフライン推測への道を開いてしまう。この文書ではクラッキングの手順をあえて記載していない。緩和策としては、長くランダムなPSKを使うこと、あるいはより望ましくはWPA3-SAEやEnterprise（802.1X）を使うことが挙げられる。

---

## 4. WPA3-Personal: SAE（概要レベル）

SAE（Simultaneous Authentication of Equals）はDragonflyプロトコル（パスワード認証鍵交換）をベースにしている。双方は楕円曲線/有限体群上でのオンラインのやり取りを通じてパスワードの知識を証明し、その後PMKを導出する。

望ましい性質（直感的な理解）:

| 性質 | 運用上の意味 |
|:---|:---|
| PAKE | パスワードは、WPA2と同じ意味での「ハッシュ化可能なPSK」としては使われない |
| オフライン耐性 | ハンドシェイクを捕捉するだけでは、従来のPSKのような安価なオフライン検証手段は得られない |
| 将来を見据えた設計 | RSN内のより現代的な暗号技術と組み合わされている |

SAEであっても、自明でないパスワードは依然として必要である（オンラインかつレート制限された推測に対する保護として）。トランジションモード（WPA2+WPA3）は、レガシーなSTAを無理に共存させると、セキュリティ態勢を弱めることがある。これは自組織の端末インベントリとのトレードオフとして理解しておく必要がある。

SAEはパスフレーズ方式のネットワークにおける脅威モデルを変えるものであるが、`password123` のようなパスワードを使ってよいという意味ではない。EAP-TLSを使ったEnterpriseは、組織にとって依然として最も信頼できる選択肢である。

---

## 5. 管理フレームとデオーセンティケーション（DoSの概念）

古典的な管理フレーム（deauth、disassoc）の多くは、歴史的にデータフレームと同等の保護なしで送信されてきた。その結果、電波の届く範囲にいる送信者は、STAを強制的にAPから切断させることができ、これは概念上、DoSまたは可用性の阻害にあたる。

$$
\mathsf{Deauth}:\ \mathsf{STA} \leftrightarrow \mathsf{AP}\ \text{session torn down (state cleared)}
$$

副次的な影響として、端末側のポリシーが弱い場合、ユーザーが似たような不正なSSID（イービルツイン）に再接続してしまうことがある。緩和策としては、ユーザー教育、WPA3、Enterprise証明書の検証、PMFが挙げられる。

Protected Management Frames（PMF / 802.11w）は、重要な管理フレームの一部を保護し、WPA3では必須となっている。端末インベントリに応じて、PMFのcapable/required設定を有効にすべきである。

注記: この文書には、フレームインジェクションのコマンド一覧、クラッキングツール、DoSの手順書は含まれていない。

原因不明の大量切断が発生した場合は、可用性インシデントとして扱う。APのログ、周辺のRFの変化、PMFが強制されているかどうかを相関させて調べるとよい。

---

## 6. 防御と監視

| 制御 | 目的 |
|:---|:---|
| WPA3 / PMF required | 古典的なdeauth攻撃を減らし、WPA2-Personalを強化する |
| 802.1X + EAP-TLS | デバイス/ユーザーごとの識別、セッションごとのPMK |
| WEP/TKIPの無効化 | 弱い暗号方式を排除する |
| SSIDごとに強く一意なPSK（PSKを使う場合） | 高いエントロピー、定期的なローテーション |
| クライアント分離 / AP分離 | Wi-Fiクライアント間の横方向の移動を減らす |
| ゲスト用と社内用のSSIDを分離 | ファイアウォールによるセグメンテーション |
| Rogue AP検知 | 同一チャネル上の見慣れないBSSID/SSIDを検知する |
| 継続的なRF調査 | ノイズやチャネル利用率のベースラインを把握する |
| WPS PINの無効化 | 弱いPSK復元経路を排除する |

検知のアイデア: BSSIDだけが異なる双子のSSID beacon、自分のラボでのエアキャプチャにおけるdeauthの急増、ローミングポリシーなしで頻繁にBSSIDを切り替えるクライアント、EAP失敗の急増など。

---

## 7. セキュリティノート: 防御のまとめ

| 課題 | リスク | 防御策 |
|:---|:---|:---|
| 弱いPSK | リンクの機密性が損なわれる | 長くランダムなPSK、またはWPA3/Enterprise |
| レガシーなWEP/TKIP | 容易に破られる暗号 | CCMP/GCMPのみを強制する |
| 保護されていない管理フレーム | Deauth DoS | PMF / WPA3 |
| フラットなWi-FiとLAN | 関連付け後の横方向移動 | 分離 + NAC |
| イービルツイン | 認証情報のフィッシング | ユーザー教育、EAPサーバー証明書の検証 |
| 弱いIoT向けWi-Fi | ネットワークの弱点になる | 別のSSID/VLANに分離する |

ラボでの心得: 監査は、自分が許可を得ているAPとスペクトラムに限定する。キャプチャは自分のネットワークのトラブルシューティングのために行い、近隣のネットワークを攻撃するために使わない。

---

## 8. チートシート: 正規の管理/ラボ用

```bash
# ── Link state (Linux, interface Anda) ───────────────────────
iw dev
iw dev wlan0 link
iw dev wlan0 info
iwlist wlan0 scanning 2>/dev/null | head   # legacy; prefer iw scan

# ── Scan SSIDs (observability on your radio) ─────────────────
sudo iw dev wlan0 scan | egrep 'BSS|SSID|RSN|capability'

# ── NetworkManager ───────────────────────────────────────────
nmcli general status
nmcli device wifi list
nmcli connection show
nmcli device wifi show-password   # only for profiles you own

# ── Regulatory / channel info ────────────────────────────────
iw reg get
iw phy phy0 info | less

# ── Hostapd / AP you operate: check config ideas ─────────────
# wpa=2, rsn_pairwise=CCMP, ieee80211w=2 (PMF required) on YOUR AP
# Prefer SAE (WPA3) when client inventory allows
```

| コマンド | 用途 |
|:---|:---|
| `iw … link` | 自分のSTAのBSSID、周波数、信号強度を表示する |
| `iw … scan` | 周辺環境を調査する（現地の法規制に従うこと） |
| `nmcli device wifi` | デスクトップ上のWi-Fiプロファイルを管理する |

---

> **参考文献と書籍**
> - Matthew Gast『802.11 Wireless Networks: The Definitive Guide』`~/Documents/Books/CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf`
> - William Stallings『Network Security Essentials (4th Edition)』`~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - James Kurose & Keith Ross『Computer Networking: A Top-Down Approach』`~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - IEEE 802.11i / WPA2 RSN、IEEE 802.11w（PMF）、WPA3（Wi-Fi Alliance）の仕様概要
> - `man iw`、`man nmcli`

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 自分が所有するWLANでの学習・運用を前提とした資料。クラッキング手順や攻撃インジェクションは含まない。
