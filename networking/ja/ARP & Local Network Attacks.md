# ARPとローカルネットワーク攻撃

> **LearnCybersecurity** | ネットワーク基礎シリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at
> 主要参考文献: Kurose & Ross『Computer Networking』、Benvenuti『Understanding Linux Network Internals』、Stallings『Network Security Essentials』

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-042` | **フェーズ2:** ネットワーキング
> **想定学習時間:** 4時間 | **レベル:** 上級
> **前提科目:** LC-039, LC-040
> **書籍対応:** Kurose & Ross, Computer Networking 第4-5章、Stallings, Network Security Essentials 第8章
<!-- LC-CURRICULUM-END -->

## 目次

1. ARPが存在する理由
2. ARP要求と応答
3. ARPキャッシュ（ネイバーテーブル）
4. 関連メカニズム（プロキシARP、GARP）
5. ローカルリンク上のMITMという概念
6. 防御策（DAI、静的ARP、セグメンテーション）
7. 検知と監視
8. セキュリティノート（防御のまとめ）
9. 管理者向けチートシート

---

## 1. ARPが存在する理由

Ethernet/IPv4では、フレームを届けるためにL2の宛先MACアドレスが必要になる一方、アプリケーションやルーティングはL3のIPアドレスを使う。ARP（Address Resolution Protocol）はこの2つを橋渡しする。

```text
ARP:  IPv4 address  →  MAC address
```

この解決はローカルリンク、つまり同一ブロードキャストドメイン内でしか機能しない。ルーターは、遠くのホストのためにサブネットをまたいでARPされることはない。ホストは自分のゲートウェイに対してARPを行い、そのゲートウェイのMACアドレス宛にフレームを送る。

```
  Host A                    L2 switch                   Host B
  IP 10.0.0.5               (broadcast domain)          IP 10.0.0.9
  MAC aa:aa:…  ──────── ARP who-has 10.0.0.9 ────────►
               ◄─────── ARP is-at bb:bb:… ────────────
  Frame dst=bb:bb ───────────────────────────────────►
```

IPv6ではARPの代わりにNDP（Neighbor Discovery）を使う。考え方はARPと同じ（L3からL2への解決）で、ICMPv6のメッセージとして運ばれる点が異なる。

ARPはtrust-on-first-use、つまり最初に見た情報をそのまま信頼するソフトステートなマッピングプロトコルであり、暗号的な真正性の検証は組み込まれていない。この設計上の性質こそが、ローカルリンクにおける整合性制御が重要になる理由である。

---

## 2. ARP要求と応答

ARPはEtherType `0x0806` を持つEthernetフレームに包まれて運ばれる。主な操作は2種類ある。

| `op` | 名称 | 意味 |
|:---:|:---|:---|
| 1 | Request | 「IPₜ は誰が持っている？ IPₛ に教えてほしい」 |
| 2 | Reply | 「IPₜ は MACₜ にある」 |

重要なフィールド（Ethernet上のIPv4の場合）:

| フィールド | 典型的な内容 |
|:---|:---|
| HTYPE / PTYPE | Ethernet / IPv4 |
| HLEN / PLEN | 6 / 4 |
| SHA / SPA | 送信者MAC / 送信者IP |
| THA / TPA | 宛先MAC / 宛先IP |

Requestは通常Ethernetのブロードキャスト（`ff:ff:ff:ff:ff:ff`）として送られ、THAはゼロのことが多い。Replyは特殊なケースを除き、通常は要求元のSHA宛にユニキャストで返される。

標準的な流れ:

```text
A → broadcast:  "Who has IP_B? Tell A"
B → A:          "IP_B is at MAC_B"
```

このやり取りの後、A は `dst MAC = MAC_B` としてIPフレームを送信できるようになる。

明示的なrequest/reply以外にも、ホストはカーネルやスタックの実装次第で、受動的に観測したパケットからもマッピングを学習することがある。求めてもいない、あるいは予期しない応答は古典的な整合性の懸念であり、これがDHCPバインディングに照らしてARPを検証するスイッチ機能が存在する理由になっている。

---

## 3. ARPキャッシュ（ネイバーテーブル）

カーネルは一時的なマッピングを保持する。

```text
IP  →  (MAC, state, interface, expiry)
```

| 状態 | 一般的な挙動 |
|:---|:---|
| Incomplete | 要求は送ったが、まだ応答がない |
| Reachable / stale | マッピングは存在し、再確認されることもある |
| TTL / gc | 古くなったエントリは破棄または更新される |
| Failures | 再試行回数に上限があり、その後ネイバーエラーになる |

最近のLinuxでは、`ip neigh` コマンドでネイバーの状態（IPv4向けのARP、IPv6向けのNDISC）を確認できる。この状態を理解しておくと、「host unreachable on-link」のようなトラブルシューティングに役立つ。

更新ルールを直感的に言えば、正当に見える応答であればエントリを新規作成したり上書きしたりできてしまう。追加のL2検証なしでは、キャッシュの正しさは結局のところ「そのセグメント上で誰が発言できるか」の正しさそのものにすぎない。

運用上の注意点として、アドレスの振り直しやNIC交換の後は、古いARP/NDエントリがタイムアウトまたはフラッシュされるまで「幽霊」のような接続性の問題を引き起こすことがある。フラッシュ操作は、自分が本当に管理しているシステムに対してのみ行うこと。

---

## 4. 関連メカニズム

| メカニズム | 概要 | セキュリティ上の注意 |
|:---|:---|:---|
| プロキシARP | ルーターが非ローカルなIPに対して、まるでon-linkであるかのようにARPへ応答する | L2の信頼範囲を広げるため、意図しない設定になっていないか監査する |
| Gratuitous ARP（GARP） | SPA=TPAとなるアナウンス | フェイルオーバーやHAでは正当な用途だが、フィルタしなければなりすましの手段にもなる |
| Inverse ARP | MACからIPへの解決（現代のEthernetでは稀） | 特殊な文脈（Frame Relay時代など）で使われた |
| ARP probe / announce（RFC 5227） | IPを使い始める前にアドレス競合を確認する | 重複アドレス検知に有用 |

```
  Normal ARP:     "Who has B? Tell A"     →  "B is at MAC_B"
  Gratuitous:     "A is at MAC_A"         →  (announce / update caches)
  Proxy:          "Who has X (remote)?"   →  Router replies with own MAC
```

---

## 5. ローカルリンク上のMITM、概念のみ

これは概念の説明であり、手順書ではない。同一セグメント上の悪意あるホストが、被害者に次のような対応関係を記憶させることに成功したとする。

```text
IP of the gateway  →  MAC of the attacker
```

（さらに逆方向も成立させる場合もある）。このとき、本来ゲートウェイへ向かうはずのフレームが攻撃者へリダイレクトされうる。トラフィックを転送もする攻撃者であれば、暗号化されていないセッションを観測したり改ざんしたりできる。これがL2におけるMITMである。

これはARPの基本的な性質、すなわちIPとMACの対応関係に暗号的な認証がまったく存在しないという点を悪用している。

> 教育的な注記: ポイズニングの手順、なりすましに使うツールのコマンド、攻撃のプレイブックはこの文書には意図的に含めていない。ここでの目的は攻撃を実行することではなく、なぜスイッチによる制御とセグメンテーションが必要なのかを理解することにある。

on-linkのリダイレクトが成功すると、「ゲートウェイのMAC宛のフレームは必ずゲートウェイに届く」という前提が崩れる。上位層でのTLSによる暗号化は機密性への影響を抑えるが、それでもL2の整合性が持つ価値、特に可用性や、エンドツーエンドで暗号化されないプロトコルに対する価値がなくなるわけではない。

---

## 6. 防御策: DAI、静的ARP、セグメンテーション

| 制御 | 仕組み（直感的な説明） | 適した場面 |
|:---|:---|:---|
| Dynamic ARP Inspection（DAI） | スイッチが信頼できるバインディング（通常はDHCP Snoopingから得たもの）に照らしてARPを検証する | エンタープライズのアクセスVLAN |
| DHCP Snooping | 正当なDHCPから (MAC, IP, ポート, VLAN) を記録する | DAIの基盤 |
| 静的ARP / 静的neigh | 重要なホストやルーターに固定のバインディングを設定する | ゲートウェイ、小規模サーバー、OT環境 |
| ポートセキュリティ | ポートごとに許可するMAC数を制限する | アクセスエッジ |
| プライベートVLAN / マイクロセグメンテーション | ホスト間の横方向移動を制限する | クラウド、データセンター、キャンパス |
| 管理プレーンの分離 | アウトオブバンド、または管理専用VRF | インフラ全般 |
| RA Guard / ND制御 | IPv6における類似の仕組み | デュアルスタック環境 |

アーキテクチャの観点では、セグメンテーションが依然として最も強力な制御である。ブロードキャストドメインが小さいほど、L2でのスヌーピングやなりすましが及ぼす被害範囲（blast radius）も小さくなる。

信頼モデル:

```
  [User VLAN] --DAI+DHCP Snoop--> [L3 gateway] --ACL--> [Server VLAN]
        │                              │
        └──── no hairpin L2 freely ────┘
```

静的ARPだけでは大規模なDHCP環境には対応できない。アクセス層でのDAIと監視を組み合わせるべきである。一方で、本当に小規模で信頼できるエンクレーブであれば、ルーター上の静的マッピングは依然として現実的な選択肢である。

---

## 7. 検知と監視

自分が管理するラボや本番環境で調査に値する兆候は次のとおりである。

| 兆候 | 考えられる意味 |
|:---|:---|
| 多数のホストで同時にゲートウェイのMACが変わる | バインディングの不安定化、またはL2の異常 |
| IPアドレスの重複（2つのMACが同じIPを主張する） | 競合、またはなりすまし |
| ARP requestのストーム | ループ、設定ミス、または積極的なスキャン |
| DAIのdropカウンタの増加 | 記録済みのバインディングに反するARP |
| TLS/VPNは正常なのに妙なcaptive portalが出る | L2リダイレクトに加えてアクティブな介入が起きている可能性 |

自分が所有するホストやスイッチのための防御ツール:

```bash
# 管理者が期待する状態とneighborテーブルを比較する
ip neigh show
bridge fdb show          # Linuxブリッジの場合

# 自分が所有するインターフェース上でARPを観測する（攻撃ではない）
sudo tcpdump -ni eth0 arp
```

結果は、スイッチのsyslog（DAI denyのログ）やDHCPリース台帳と突き合わせて相関を取る。

---

## 8. セキュリティノート: 防御のまとめ

| 課題 | リスク | 防御策 |
|:---|:---|:---|
| ARPに認証がない | キャッシュバインディングの偽装 | DAI + DHCP Snooping |
| フラットなL2構成 | 横方向のMITMや偵察が容易になる | VLAN / マイクロセグメンテーション |
| GARPが無制限 | キャッシュの大規模な上書き | レート制限 / インスペクションポリシー |
| 静的マップが古いまま | NIC交換後の障害 | 静的ARPを更新する運用手順（ランブック） |
| IPv6が対象外 | 「ARPだけ」に注目することで生じる抜け道 | RA Guard、ND inspection |
| 平文プロトコル | MITMが成功するとデータが読み取られる | 全面的なTLS化、加えてHSTS |

原則として、ローカルなL2はスイッチのポリシーが実際に強制している範囲でしか信頼できないと考えるべきである。エンドツーエンド暗号化はリンクレベルのアクセス制御を補完するものであり、それに置き換わるものではない。

---

## 9. チートシート: 管理者 / 自分のラボ用

```bash
# ── Inspect neighbor table ───────────────────────────────────
ip neigh show
ip -4 neigh show dev eth0
ip -6 neigh show

# ── Manage entries on YOUR host (careful in prod) ────────────
sudo ip neigh add 10.0.0.1 lladdr aa:bb:cc:dd:ee:ff dev eth0 nud permanent
sudo ip neigh del 10.0.0.1 dev eth0
sudo ip neigh flush dev eth0

# ── Trigger resolution (legitimate traffic) ──────────────────
ping -c 1 10.0.0.9
ip neigh get 10.0.0.9 dev eth0

# ── Passive observation on interfaces you own ────────────────
sudo tcpdump -ni eth0 'arp' -vv
sudo tcpdump -ni eth0 'arp and arp[6:2] == 2'   # replies only

# ── MAC / FDB visibility (Linux bridge) ──────────────────────
ip link show
bridge link show
bridge fdb show
```

| コマンド | 用途 |
|:---|:---|
| `ip neigh` | ARP/NDキャッシュの表示・変更 |
| `tcpdump arp` | 自分のNIC上のARPトラフィックを監査する |
| `bridge fdb` | ブリッジ上のMAC学習状況を確認する |

---

> **参考文献と書籍**
> - James Kurose & Keith Ross『Computer Networking: A Top-Down Approach』`~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - Christian Benvenuti『Understanding Linux Network Internals』`~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings『Network Security Essentials (4th Edition)』`~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - W. Richard Stevens『UNIX Network Programming, Vol. 1』`~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - RFC 826（ARP）、RFC 5227（IPv4アドレス競合検知）、RFC 4861（NDP）

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 自分が所有する、または許可を得たネットワークでの学習・検証を前提とした資料。ポイズニングの手順書ではない。
