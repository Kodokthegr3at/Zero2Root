# TCP/IPアーキテクチャとソケットプログラミング

> **LearnCybersecurity** | ネットワーク基礎シリーズ
> 最終更新: 2026年 | 著者: kodoktheGr3at
> 主要参考文献: Kurose & Ross『Computer Networking』、Stevens『UNIX Network Programming』、Benvenuti『Understanding Linux Network Internals』、Stallings『Network Security Essentials』

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-039` | **フェーズ2:** ネットワーキング
> **想定学習時間:** 5〜6時間 | **レベル:** 中級
> **前提科目:** LC-038
> **書籍対応:** Kurose & Ross, Computer Networking 第3-4章、Stevens, UNIX Network Programming Vol.1 第1-6章
<!-- LC-CURRICULUM-END -->

## 目次

1. TCP/IPの4層モデル
2. IPv4ヘッダー: 中心となるフィールド
3. TCPセグメント: 重要なフィールド
4. TCPの状態遷移（簡略版）
5. 3ウェイハンドシェイク
6. 輻輳制御: ウィンドウの直感的理解
7. ソケットAPIの概要: CとPython
8. SYNフラッド: 概念とSYN cookie
9. セキュリティノート: スタックのハードニング
10. チートシート

---

## 1. TCP/IPの4層モデル

実務的なインターネットモデル（Kuroseの言い方）は、OSIの7層と比べて、しばしば4層として説明される。

| 層 | 役割 | 例 |
|:---|:---|:---|
| Application | アプリケーションのセマンティクス | HTTP、DNS、SSH |
| Transport | プロセス間通信 | TCP、UDP、QUIC* |
| Internet | ホスト間のルーティング | IPv4、IPv6、ICMP |
| Link / Network Access | ローカルなホップ | Ethernet、Wi-Fi |

*QUICはUDPの上で動作するが、現代的なトランスポート層に近い信頼性とセキュリティ機能を提供する。

```
  ┌─────────────────────────────┐
  │  Application  (HTTP, …)     │
  ├─────────────────────────────┤
  │  Transport    (TCP/UDP)     │
  ├─────────────────────────────┤
  │  Internet     (IP)          │
  ├─────────────────────────────┤
  │  Link         (Eth/802.11)  │
  └─────────────────────────────┘
         encapsulation ↓
  [Eth][IP][TCP][App data][FCS]
```

カプセル化: 各層はヘッダー（時にはトレーラーも）をデータに追加していく。上位方向へのデマルチプレクシングには、EtherType、IPのプロトコル番号、ポート番号が使われる。

セキュリティの制御はすべての層に存在する（802.1X、IPsec、TLS、アプリケーションレベルの認証など）。多層防御とは、特定の1つの層の保証だけに頼らないという考え方である。

---

## 2. IPv4ヘッダー: 中心となるフィールド

ヘッダーの最小サイズはオプションなしで20バイトである。

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |    TOS/DSCP   |         Total Length          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|    Fragment Offset      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |   Protocol    |        Header Checksum        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if IHL > 5) …                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| フィールド | セキュリティ/運用上の意味 |
|:---|:---|
| Version | 4か6か |
| IHL | ヘッダー長。オプションはあまり使われず、しばしばフィルタされる |
| DSCP/ECN | QoSや輻輳通知 |
| Total Length | データグラムのサイズ |
| ID / Flags / Offset | フラグメンテーション。実装の弱いスタックでは再構成攻撃のリスクになる（現代のOSははるかに耐性が高い） |
| TTL | ホップ数の上限。ループを防ぎ、OSの推定にも使われる |
| Protocol | 6=TCP、17=UDP、1=ICMPなど |
| Checksum | IPv4ではヘッダーのみが対象 |
| Src / Dst | アドレッシング。ingressフィルタがなければ送信元は偽装できる |

$$
\mathsf{Payload\ size} = \mathsf{TotalLength} - 4\cdot\mathsf{IHL}
$$

---

## 3. TCPセグメント: 重要なフィールド

TCPは接続指向のバイトストリームを提供し、信頼性（ACK、再送）、順序保証、フロー制御を備えている。

| フィールド | 機能 |
|:---|:---|
| Src / Dst Port | ソケットへのデマルチプレクシング |
| Seq | 送信側ストリームにおけるバイトオフセット |
| Ack | 次に期待されるバイト（ACKフラグが立っている場合） |
| Data Offset | TCPヘッダーのサイズ |
| Flags | SYN、ACK、FIN、RST、PSH、URG、ECE、CWRなど |
| Window | 受信側によるフロー制御 |
| Checksum | IP + TCPの疑似ヘッダーを対象に計算 |
| Urgent / Options | SACK、Timestamp、MSS、Window Scaleなど |

コネクションの識別は4-tuple（プロトコルを含めれば5-tuple）で行われる。

$$
(srcIP,\ srcPort,\ dstIP,\ dstPort)
$$

---

## 4. TCPの状態遷移（簡略版）

主要な状態（Stevens、および古典的な図に基づく）:

```
  CLOSED ──passive open──► LISTEN ──SYN──► SYN_RCVD ──ACK──► ESTABLISHED
  CLOSED ──active open───► SYN_SENT ──────────SYN+ACK──► ESTABLISHED

  ESTABLISHED ──FIN──► FIN_WAIT_1 ──► FIN_WAIT_2 ──► TIME_WAIT ──► CLOSED
  ESTABLISHED ──FIN──► CLOSE_WAIT ──► LAST_ACK ──► CLOSED
```

| 状態 | 簡単な意味 |
|:---|:---|
| LISTEN | SYNを待っている状態 |
| SYN_SENT / SYN_RCVD | ハンドシェイクが半分終わった状態 |
| ESTABLISHED | データ転送が行われている状態 |
| TIME_WAIT | 古いセグメントが確実に消えるまで2×MSL待っている状態 |
| CLOSE_WAIT | 相手側からFINを受け取っており、ローカルのアプリケーションがcloseすべき状態 |

`ss -tan` は自分が所有するLinuxホスト上の状態を表示し、コネクションリークやフラッドの診断に役立つ。

`TIME_WAIT` はしばしばバグと誤解されるが、これはプロトコルの正しさを保証するための機能である。チューニングするにはMSLの理解と、自分のシステムがクライアント寄りかサーバー寄りかの理解が必要になる。中身を理解しないまま無効化してはならない。

---

## 5. 3ウェイハンドシェイク

コネクションの確立:

$$
\begin{aligned}
1&\colon\ \mathsf{C \to S}:\ \mathsf{SYN},\ seq=x \\
2&\colon\ \mathsf{S \to C}:\ \mathsf{SYN\text{+}ACK},\ seq=y,\ ack=x+1 \\
3&\colon\ \mathsf{C \to S}:\ \mathsf{ACK},\ ack=y+1
\end{aligned}
$$

```
  Client                     Server
    │  SYN, seq=x               │
    │──────────────────────────►│
    │  SYN+ACK, seq=y, ack=x+1  │
    │◄──────────────────────────│
    │  ACK, ack=y+1             │
    │──────────────────────────►│
    │      ESTABLISHED          │
```

両者はそれぞれ自分の初期シーケンス番号（ISN）に合意する。現代のISNは単純なカウンタではなく強化された方式で生成されており、予測可能なスプーフィングのリスクを減らしている。

終了処理: 典型的には4方向でのFIN/ACKのやり取り、あるいは強制的に打ち切るRSTが使われる。

ミドルボックスやロードバランサは、ハンドシェイクの状態を慎重に扱う必要がある。経路の非対称性やSYNタイムアウトは、SYN cookieのようなDoS対策と相互に影響し合う。

---

## 6. 輻輳制御: ウィンドウの直感的理解

フロー制御: `rwnd` は受信側から通知される値である（スケーリングされたWindowフィールド）。
輻輳制御: 送信側はcwnd（congestion window）によって自らを制限し、共有経路に過度な負荷をかけないようにする。

飛行中のバイト数（直感的な理解）:

$$
\mathsf{in\_flight} \le \min(\mathsf{cwnd},\, \mathsf{rwnd})
$$

古典的なフェーズ（Reno的な直感、現代の実装はCUBICやBBRなどを使う）:

| フェーズ | 挙動 |
|:---|:---|
| Slow start | `cwnd` はssthreshに達するまでRTTごとに指数関数的に増加する |
| Congestion avoidance | 増加がより線形に近づく |
| Loss signal | Triple-dup ACKやRTOによって `cwnd` が下がり、ssthreshが調整される |

$$
\text{slow start（概算）:}\quad \mathsf{cwnd} \leftarrow \mathsf{cwnd} + \mathsf{MSS}\ \text{per ACK}
$$

セキュリティとの関連: UDP/TCPフラッドはcongestive DoSを引き起こしうる。レート制限とキャパシティプランニングがその運用上の対策となる。

`cwnd` を手動でチューニングすることはまれで、実際に観測するのはRTT、再送率、バッファブロートである。BBRは古いアルゴリズムのように損失だけに反応するのではなく、ボトルネック帯域幅とRTTをモデル化する。

---

## 7. ソケットAPIの概要: CとPython

ソケットは通信のエンドポイントを抽象化したもの（Stevensの用語）である。TCPサーバーのパターンは次のとおりである。

1. `socket` → 2. `bind` → 3. `listen` → 4. `accept` ループ → 5. `recv`/`send` → 6. `close`

クライアントのパターン: `socket` → `connect` → `send`/`recv` → `close`。

### C（スケッチ）

```c
int s = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr = {0};
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = htonl(INADDR_ANY);
bind(s, (struct sockaddr*)&addr, sizeof addr);
listen(s, 128);
int c = accept(s, NULL, NULL);
/* read/write on c */
close(c); close(s);
```

### Python 3

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8080))
    s.listen(128)
    conn, peer = s.accept()
    with conn:
        data = conn.recv(4096)
        conn.sendall(b"OK\n")
```

| 呼び出し | 意味 |
|:---|:---|
| `bind` | ローカルのアドレス/ポートを結びつける |
| `listen` | SYNキュー / backlog |
| `accept` | 確立済みのコネクションをキューから取り出す |
| `connect` | Active open |
| `SO_REUSEADDR` | 高速な再バインドを許可する（TIME_WAITへの影響を理解しておく） |

UDPは `SOCK_DGRAM` を使い、`sendto`/`recvfrom` で通信し、ハンドシェイクは行わない。

バイトオーダーは常に明示的に扱い（`htons`/`inet_pton`）、`send` が部分的にしか送れない場合に対応し、ネットワークを信頼できないものとして扱う。入力を検証し、タイムアウトを設定し、機密性の高いアプリケーションにはTLSのラッパー（`ssl` モジュールやOpenSSL）を使うことが望ましい。

---

## 8. SYNフラッド: 概念とSYN cookie

概念: 攻撃者は大量のSYNセグメント（多くの場合スプーフィングされている）を送信し、サーバーにhalf-open状態（SYN_RCVD）を割り当てさせ続け、テーブルやbacklogを使い果たさせる。その結果、正規のクライアントが接続できなくなる。これはDoSの一種である。

$$
\#\{\mathsf{SYN\_RCVD}\} \uparrow\ \Rightarrow\ \mathsf{resource\ exhaustion}
$$

SYN cookie（防御策）: サーバーはSYNを受け取った時点では完全なTCBを保持しない。ISNは、4-tupleとタイムスタンプ/MSSのビットに対する秘密鍵付きハッシュとしてエンコードされる。最終的なACKが有効なcookieを含んでいる場合にのみ、実際の状態が作られる。

$$
\mathsf{ISN}_s \approx \mathsf{Hash}_{k}(addrs, ports,\; t) \;+\; \mathsf{encode}(\mathsf{MSS})
$$

（カーネルごとに実装は異なるが、基本的な考え方は同じである。）

その他の関連する対策: `tcp_syncookies`、妥当なbacklogの設定、ロードバランサでのSYNレート制限やSYNプロキシ、公開サービスに対するエニーキャストによるスクラビングなど。

注記: この文書にはフラッドのPoCや攻撃的なツールのコマンドは含まれていない。

インターネットに公開されたVIPでは、SYN cookieやSYNプロキシのメトリクスを有効にして監視する。必要に応じて、送信元プレフィックスごとのコネクション数制限と組み合わせるとよい。

---

## 9. セキュリティノート: スタックのハードニング

| 課題 | リスク | 防御策 |
|:---|:---|:---|
| SYNフラッド | half-openスロットの枯渇 | SYN cookie、レート制限、キャパシティプランニング |
| 送信元の偽装 | リフレクションやSYNの悪用 | BCP38 / uRPF |
| RSTインジェクション | シーケンス番号が推測できる場合にセッションを切断される | 暗号化されたトランスポート、現代的なISN生成 |
| 平文のTCPアプリケーション | 盗聴やMITM | TLS 1.3 |
| `0.0.0.0` への開いたbind | 意図しない露出 | 内部インターフェースへのbind、ファイアウォール |
| 過大なbacklog | メモリ圧迫 | チューニングと `ss` による監視 |
| フラグメンテーションのトリック | （レガシーなスタックでの）IDS回避 | 正規化。現代のスタックはデフォルトである程度対応済み |

ラボでの心得: ハンドシェイクやソケットの実験は自分が所有するホスト/VM上でのみ行い、`ss` と `tcpdump` で防御的に監視すること。

---

## 10. チートシート: 管理、観測、最小限のラボ用コード

```bash
# ── Connection tables ────────────────────────────────────────
ss -tan
ss -tanp state syn-recv
ss -s
ip -s link

# ── Capture YOUR interface traffic (troubleshooting) ─────────
sudo tcpdump -ni eth0 'tcp[tcpflags] & (tcp-syn) != 0'
sudo tcpdump -ni lo port 8080 -vv

# ── Kernel knobs (read; change only on lab hosts you own) ────
sysctl net.ipv4.tcp_syncookies
sysctl net.core.somaxconn
sysctl net.ipv4.tcp_max_syn_backlog

# ── Quick local listener / client (Python) ───────────────────
python3 - <<'PY'
import socket, threading
def serve():
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 8080)); s.listen(1)
        c,_=s.accept(); print(c.recv(64)); c.close()
threading.Thread(target=serve, daemon=True).start()
with socket.create_connection(("127.0.0.1", 8080)) as c:
    c.sendall(b"hello"); print("sent")
PY
```

| ツール | 用途 |
|:---|:---|
| `ss` | モダンなTCP/UDPの状態確認（`netstat` の代替） |
| `tcpdump` | SYN/FIN/RSTフラグの観測 |
| `sysctl` | ラボホスト上でのスタックパラメータ確認 |

---

> **参考文献と書籍**
> - James Kurose & Keith Ross『Computer Networking: A Top-Down Approach』`~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - W. Richard Stevens『UNIX Network Programming, Volume 1 (3rd Edition)』`~/Documents/Books/CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf`
> - Christian Benvenuti『Understanding Linux Network Internals』`~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - William Stallings『Network Security Essentials (4th Edition)』`~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - RFC 791（IPv4）、RFC 9293（TCP）、RFC 4987（SYN cookieに関する文献レビュー）
> - `man ss`、`man tcpdump`、`man 7 ip`、`man 7 tcp`

> **リポジトリ:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> 自分が所有するシステムでの学習・検証を前提とした資料。フラッドのPoCやエクスプロイトは含まない。
