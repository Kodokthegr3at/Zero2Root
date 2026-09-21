# DNSとDomain Name Systemのセキュリティ

> **LearnCybersecurity** | ネットワーク基礎シリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at
> 主要参考文献: Kurose & Ross『Computer Networking』、Stallings『Network Security Essentials』、Benvenuti『Understanding Linux Network Internals』

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-041` | **フェーズ2:** ネットワーキング
> **想定学習時間:** 4時間 | **レベル:** 中級
> **前提科目:** LC-039
> **書籍対応:** Kurose & Ross, Computer Networking 第2章、Stallings, Network Security Essentials 第8章
<!-- LC-CURRICULUM-END -->

## 目次

1. DNSの階層構造（namespace tree）
2. 名前解決のアルゴリズム
3. リソースレコードの種類
4. DNSSEC（署名と信頼の連鎖）
5. DNSのプライバシー（DoT・DoH）
6. ゾーン転送（設定不備のリスク）
7. キャッシュポイズニング（概念と防御）
8. セキュリティノート（検知とハードニング）
9. 管理者向けチートシート

---

## 1. DNSの階層構造: namespace tree

DNS（Domain Name System）は階層的な名前をリソース、たいていはIPアドレスにマッピングする仕組みである。ネームスペースはルート（`.`）を根とする逆さまの木構造になっている。各ラベルはドットで区切られ、FQDNは右から左に読む。

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www
```

完全な名前は `www.example.com.` となる（末尾のドットはルートを表す）。

| レベル | 例 | 役割 |
|:---|:---|:---|
| ルート | `.` | 階層の頂点、root NS |
| TLD | `com`, `id`, `jp` | レジストリが管理 |
| SLD / ゾーン | `example.com` | 組織 / 権威ゾーン |
| ホスト / ラベル | `www`, `mail` | ゾーン内のリソース |

委任の仕組みは、親ゾーンが子ゾーンのためにNSレコード（とグルーとなるA/AAAA）を保持するというものである。あるゾーンの権威とは、要するにそのゾーン内の名前に対してAA（Authoritative Answer）フラグ付きで応答するネームサーバーの集合にほかならない。

DNSは分散型の階層データベースである。木構造全体を単一のサーバーが保持することはなく、権威は下位へと委任されていく。クライアントは通常、再帰リゾルバに問い合わせ、そのリゾルバが木を辿る（あるいはキャッシュを使う）ことで答えを得る。

---

## 2. 名前解決のアルゴリズム

名前解決には主に3つの役割が関わる。

| 役割 | 振る舞い |
|:---|:---|
| スタブリゾルバ | OSやアプリケーション内で動作し、設定済みの再帰リゾルバへクエリを送る |
| 再帰リゾルバ | スタブに代わって完全なlookupを行い、結果をキャッシュすることもある |
| 権威サーバー | 自分が担当するゾーンについてのみ応答する |

反復的なアルゴリズムを直感的に表すと（Kuroseの説明に沿う形で）次のようになる。

$$
\begin{aligned}
&Q \leftarrow \text{query}(name, type) \\
&S \leftarrow \text{root hint set} \\
&\textbf{while } true: \\
&\quad R \leftarrow \mathsf{Query}(S, Q) \\
&\quad \textbf{if } R \text{ is answer or NXDOMAIN:} \; \textbf{return } R \\
&\quad S \leftarrow \text{referral NS (and glue) from } R
\end{aligned}
$$

```
Stub ──Q──► Recursive ──iterative──► Root
                 │                      │
                 │◄──── referral ───────┘
                 ├──► TLD NS
                 │◄── referral
                 └──► Auth NS ──► Answer (AA)
```

キャッシュについて: 各RRのTTLがキャッシュ可能な期間を制限する。否定的な応答（NXDOMAINなど）もキャッシュされ（RFC 2308）、肯定応答とは別のルールに従う。

再帰は木を辿る処理をクライアントから肩代わりする。権威サーバーは通常、公開インターネットに対して再帰を行うべきではない。そうすることでamplificationや悪用の攻撃対象領域を減らせるからである。再帰と権威の役割を分離するのは標準的な運用上の作法であり、公開権威サーバーで不用意に再帰を有効にすべきではない。

---

## 3. リソースレコードの種類

| タイプ | 概要 | データ例 |
|:---|:---|:---|
| A | IPv4のホスト | `93.184.216.34` |
| AAAA | IPv6のホスト | `2606:2800:...` |
| NS | 委任 / ゾーンのネームサーバー | `ns1.example.com.` |
| CNAME | 正規名へのエイリアス | `www → origin.cdn.net.` |
| MX | メール交換とその優先度 | `10 mail.example.com.` |
| TXT | 自由記述のテキスト（SPFや検証用など） | `"v=spf1 ..."` |
| SOA | Start of Authority（シリアル、各種タイマー） | ゾーンのメタデータ |
| PTR | 逆引き（in-addr.arpa / ip6.arpa） | ホスト名 |
| SRV | サービスの所在 | `_sip._tcp...` |
| DNSKEY | ゾーンの公開鍵（DNSSEC） | 鍵素材 |
| DS | 親ゾーンに置かれる、子のDNSKEYのハッシュ（DNSSEC） | ダイジェスト |
| RRSIG | RRsetに対する署名 | 署名 |
| NSEC / NSEC3 | 非存在証明 | authenticated denial |

RRsetとは、名前・タイプ・クラスが同一であるRRの集合を指す。DNSSECの署名操作はこのRRset全体に対して行われ、兄弟レコードから切り離した単一のRRに対して行われるわけではない。

古典的なワイヤーフォーマットはUDP/53上で動く（応答が大きい場合はTCP/53、またはEDNS0にフォールバックする）。EDNS0は許容されるUDPサイズを拡張し、「DNSSEC OK」を示すDOビットやcookiesといった追加オプションも運ぶ。

---

## 4. DNSSEC: 署名と信頼の連鎖

DNSSECはDNSデータに認証と完全性を追加するものであり、機密性を追加するものではない。検証を行うリゾルバは、応答が正しいゾーンに由来し、経路上やキャッシュ上で改ざんされていないことを確認する。

中核となる要素:

| RR | 役割 |
|:---|:---|
| DNSKEY | ゾーンの公開鍵（ZSK / KSK） |
| RRSIG | RRsetに対する署名 |
| DS | 子ゾーンのDNSKEYのダイジェストで、親ゾーンに保持される |
| NSEC/NSEC3 | 名前やタイプが存在しないことの証明 |

RRSIGの検証を概念的に表すと、RRset $R$ と公開鍵 $K$ に対して次のようになる。

$$
\mathsf{Verify}\big(K_{\mathsf{pub}},\; R,\; \mathsf{RRSIG}(R)\big) = \mathsf{accept/reject}
$$

署名方式 $\mathsf{Sign}/\mathsf{Verify}$ を使って抽象的に書けば、

$$
\mathsf{RRSIG}(R) = \mathsf{Sign}_{K_{\mathsf{priv}}}(\mathsf{Hash}(R) \;\|\; \mathsf{meta})
$$

であり、$\mathsf{meta}$ にはアルゴリズム、ラベル数、original TTL、有効開始・終了時刻、key tag、signer nameなどが含まれる。

信頼の連鎖:

```
Trust Anchor (root KSK, hardcoded/managed)
        │  validates
        ▼
   root DNSKEY ──RRSIG──► root zone data
        │  DS for .com
        ▼
   com DNSKEY ──► … ──DS──► example.com DNSKEY
                                │
                                ▼
                         RRSIG on example.com RRsets
```

リゾルバにはtrust anchorが必要で、通常はrootに置かれる。親ゾーンのDSが子ゾーンのDNSKEYと一致し、RRSIGが有効かつ時間窓内にあれば、そのRRsetはSecureとみなされる。検証に失敗するとBogusとなり、その応答は使ってはならない。DNSSECをまったく使っていないゾーンはInsecureであり、これはBogusとは異なる。

DNSSECは、バリデータがエンドツーエンドで有効になっている限り、経路上やキャッシュ上で偽造された応答が気づかれずにすり替わることを防ぐ。ただしクエリ自体を暗号化するわけではない。質問内容の機密性が必要な場合はDoT/DoHを使う。

---

## 5. DNSのプライバシー: DoT・DoH

| 方式 | ポート / フレーミング | 特性 |
|:---|:---|:---|
| 従来のDNS | UDP/TCP 53 | 質問・応答とも平文 |
| DoT（DNS over TLS） | TCP 853 | DNSをTLSで包む |
| DoH（DNS over HTTPS） | TCP 443 | DNSをHTTP(S) API上に載せる |

メリットは、これまで平文でやり取りされていたクエリ・応答に対する受動的な盗聴と経路上での改ざんを防げることにある。

一方で現実的なトレードオフもある。特定のDoHベンダーのような中央集権的なリゾルバは、それでも名前解決のメタデータを見ることができるため、プライバシーポリシーは意識的に選ぶ必要がある。企業環境では、ロギングやDLPを維持するために内部リゾルバの利用を強制し、勝手なDoH利用をブロックすることが多い。これは文書化し、利用者に周知しておくべきである。ラボや製品にとって理想的な組み合わせは、DNSSEC検証も行うリゾルバに対してDoT/DoHを使うことである。

---

## 6. ゾーン転送: 設定不備のリスク

AXFR（フルゾーン転送）とIXFR（差分転送）は、secondaryがprimaryのゾーン内容を複製するために使われる。これは正当な運用機能であって「攻撃」ではない。しかし、制限なく誰にでも許可されている場合、内部ホストや命名規則を含むゾーンの内容全体を外部の者がダウンロードできてしまう。

このような設定不備から生じるリスク:

- 内部の名前一覧が露出する
- 他の攻撃の前段階となる偵察を助けてしまう
- アクセス制御（理想的にはTSIGとの併用）がない場合、偽のsecondaryが現れうる

自分が管理するゾーンに対するハードニング策:

- AXFR/IXFRを既知のsecondaryのIPだけに制限する
- primaryとsecondaryの間でTSIG（HMACベースの共有秘密鍵）を使う
- ホスト名の「security through obscurity」に頼らず、セグメンテーションと最小権限の原則を維持する

注記: この文書に攻撃手順は含まれておらず、設定に関する意識づけと防御チェックリストのみを扱っている。

開かれたゾーン転送は設定上の欠陥として扱うべきである。権威サーバーのログで、予期しないAXFRの試行がないか監視する。

---

## 7. キャッシュポイズニング: 概念と防御

キャッシュポイズニングは概念的に言えば、再帰リゾルバが本物の応答より先に、一見正当に見える（IDやquestionが一致する）偽の応答を受け入れてしまうこと、あるいはトランザクション予測の弱さによって、名前と誤ったデータの対応関係を保持してしまうことを指す。

高いレベルでの脅威モデル（Kaminsky時代の直感的な説明）としては、過去のトランザクション推測空間が次のように小さければ危険だった。

$$
|\mathcal{S}| = 2^{16}\;(\mathsf{TXID}) \times \#\{\text{src ports}\}
$$

この値が小さく、かつ攻撃者が自ら引き起こしたクエリに対して偽の応答を大量に送りつけられる場合である。

現代的な防御策（攻撃の手順書ではない）:

| 制御 | 効果 |
|:---|:---|
| Source port randomization | トランザクションの推測空間を広げる |
| ランダムなTXID | 以前から必須で、ポートのランダム化と組み合わせる |
| DNS cookies（RFC 7873） | クライアント・サーバー間のトークンで安価ななりすましを減らす |
| DNSSEC validation | 偽の応答は検証に失敗し、Bogusとして扱われる |
| 0x20 encoding / QNAMEの大文字小文字 | 対応している場合、ワイヤー上にエントロピーを追加する |
| ネットワーク経路のセキュリティ | リゾルバの通信経路にパケットを注入できる相手を制限する |

検知の兆候: 通常は安定しているゾーンでSERVFAILが急増する、正当なゾーン更新がないのにRRsetが突然変わる、他の検証済みリゾルバの見え方と食い違う、といったものが挙げられる。

正しい防御は多層防御である。クエリのトランザクションにエントロピーを持たせることと、DNSSECによる暗号学的な真正性の両方を組み合わせる。どちらか一方だけでは、運用として完結した対策にはならない。

---

## 8. セキュリティノート: 防御と検知

| 課題 | リスク | 防御 / 検知 |
|:---|:---|:---|
| 平文のDNS | 盗聴 / 経路上での改ざん | DoT/DoH、信頼できる経路 |
| 検証を行わないリゾルバ | 偽造が検知されない | DNSSEC検証を有効化する |
| オープンな再帰 | 悪用 / amplification | クライアントACL、authとrecursiveの分離 |
| 開かれたAXFR | ゾーンダンプ | ACL + TSIG、ログでのアラート |
| 不正なリゾルバ（DHCP/RA経由） | 名前解決のリダイレクト | DHCP snooping、RA Guard、DoHのポリシー |
| trust anchorが古いまま | 誤ったBogus判定 / 障害 | RFC 5011による自動更新、加えて監視 |

ラボでの心構え: テスト対象は自分が所有するリゾルバとゾーンだけにする。Bogus状態を診断する際は、`dig +dnssec` の結果を、別の検証を行う公開リゾルバの結果と比較する。

---

## 9. チートシート: 正当な管理者 / ラボ用

```bash
# ── Basic lookup (自分のシステム) ─────────────────────────────
dig example.com A +noall +answer
dig example.com AAAA
dig MX example.com
dig NS example.com

# ── Trace iterative path (observability) ─────────────────────
dig +trace example.com

# ── DNSSEC inspection ────────────────────────────────────────
dig example.com A +dnssec +multi
dig DNSKEY example.com +multi
dig DS example.com +short
delv example.com A          # 設定されていればvalidating lookupになる

# ── Reverse / SOA ────────────────────────────────────────────
dig -x 93.184.216.34
dig SOA example.com +noall +answer

# ── Check if YOUR authoritative allows transfer to YOU only ──
# (許可されたsecondaryから実行すること。他のホストからはREFUSEDになるはず)
dig AXFR example.com @ns1.example.com

# ── Local stub / systemd-resolved ────────────────────────────
resolvectl status
resolvectl query example.com
```

| コマンド | 用途 |
|:---|:---|
| `dig +short` | 簡潔な応答のみ表示 |
| `dig +dnssec` | RRSIG / DOを表示 |
| `dig +trace` | rootからの経路をシミュレート |
| `delv` | BINDツールによるクライアント側DNSSEC検証 |

---

> **参考文献と書籍**
> - James Kurose & Keith Ross『Computer Networking: A Top-Down Approach』`~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings『Network Security Essentials (4th Edition)』`~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Christian Benvenuti『Understanding Linux Network Internals』`~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - RFC 1034/1035（DNS）、RFC 4033-4035（DNSSEC）、RFC 7858（DoT）、RFC 8484（DoH）、RFC 7873（Cookies）
> - `man dig`、`man resolvectl`

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 自分が所有する、または許可を得たシステム・ゾーンでの学習・検証を前提とした資料。攻撃手順は含まれていない。
