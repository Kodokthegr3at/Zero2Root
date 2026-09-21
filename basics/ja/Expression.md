# 式: 構文、型、評価

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-001` | **フェーズ0:** 基礎
> **学習目安:** 2-3時間 | **レベル:** 初級
> **前提知識:** なし
> **書籍対応:** K. N. King, C Programming Ch.2-5; Friedl, Mastering Regular Expressions Ch.1-4; Sweigart, Automate the Boring Stuff Ch.1-6
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック | 説明 |
|---|---------|------|
| 1 | 算術式 | 数学・算術演算 |
| 2 | 論理式 | ブール論理（AND、OR、NOT） |
| 3 | 関係式 | 値の比較（==、!=、<、>） |
| 4 | 代入式 | 代入と複合代入演算子 |
| 5 | 条件式（三項演算子） | 三項演算子による条件式 |
| 6 | ラムダ式 | 簡潔な無名関数 |
| 7 | 正規表現（RegEx） | 文字列パターン照合 |
| 8 | ビット演算式 | ビット単位の演算と操作 |
| 9 | キャスト式 | データ型変換（拡大・縮小キャスト） |
| 10 | オブジェクト生成式 | メモリ確保とオブジェクト生成 |
| 11 | セキュリティノート | 式のリスクと防御コントロール |
| 12 | 要約とチートシート | 要約表とクイックチートシート |

---

## 1. 算術式

**算術式**は、加算（`+`）、減算（`-`）、乗算（`*`）、除算（`/`）、剰余（`%`）などの基本的な数学演算を通じて数値を算出する式です。

システムプログラミング（C/C++）や現代的な言語（Java、Python）では、評価順序は演算子の優先順位（BODMAS/PEMDAS）に従います。乗算、除算、剰余は、丸括弧 `()` で明示的にグループ化されていない限り、加算や減算よりも優先して評価されます。

形式的には（K. N. King）、整数算術式は次の文法で表せます。

$$
E ::= n \mid (E) \mid E \;+\; E \mid E \;-\; E \mid E \;\times\; E \mid E \;/\; E \mid E \bmod E
$$

左結合で、優先順位は \(\times,/,\% \;>\; +,-\) です。幅 \(w\) ビットの整数オーバーフローは、結果が \(\bigl[-2^{w-1},\,2^{w-1}-1\bigr]\)（符号付き）または \(\bigl[0,\,2^{w}-1\bigr]\)（符号なし）の範囲を外れたときに発生し、Cでのバッファ確保サイズ誤りの典型的な原因になります。

```java
// ── Javaの例 ─────────────────────────────────────────────
int a = 10;
int b = 3;

int sum        = a + b;           // 13   — 加算
int difference = a - b;           // 7    — 減算
int product    = a * b;           // 30   — 乗算
int quotient   = a / b;           // 3    — 整数除算
int remainder  = a % b;           // 1    — 剰余
double power   = Math.pow(a, 2); // 100.0 — べき乗
```

```c
/* ── Cの例（K. N. King - C Programming Standard） ────────── */
#include <stdio.h>

int main(void) {
    int total_seconds = 3665;
    int hours   = total_seconds / 3600;       /* 1時間 */
    int minutes = (total_seconds % 3600) / 60; /* 1分 */
    int seconds = total_seconds % 60;         /* 5秒 */
    
    printf("Time: %02d:%02d:%02d\n", hours, minutes, seconds);
    return 0;
}
```

| 演算子 | 機能 | 例 | 結果 |
|--------|------|-----|------|
| `+` | 加算 | `10 + 3` | `13` |
| `-` | 減算 | `10 - 3` | `7` |
| `*` | 乗算 | `10 * 3` | `30` |
| `/` | 除算 | `10 / 3` | `3`（整数） |
| `%` | 剰余（モジュロ） | `10 % 3` | `1` |

---

## 2. 論理式（ブール式）

**論理式**は、論理演算子 `&&`（論理積 AND）、`||`（論理和 OR）、`!`（論理否定 NOT）を使用して、条件をブール値（`true` または `false`）として評価する式です。

現代のプログラミング言語は短絡評価（ショートサーキット評価）を採用しています。

- `A && B` では、`A` が `false` の場合、式全体が `false` に確定するため `B` は評価されません。
- `A || B` では、`A` が `true` の場合、式全体が `true` に確定するため `B` は評価されません。

```java
// ── 短絡評価の例 ────────────────────────
String username = getUsername();
// usernameがnullの場合、username.length()は呼び出されない（NullPointerExceptionを回避）
if (username != null && username.length() > 3) {
    System.out.println("Valid user format");
}

// ── 論理演算 ───────────────────────────────────────
boolean isAuthenticated = true;
boolean hasAdminRole    = false;

boolean canAccessDashboard = isAuthenticated && hasAdminRole; // false
boolean canViewPublicPage  = isAuthenticated || hasAdminRole; // true
boolean isGuest            = !isAuthenticated;                // false
```

| 演算子 | 名称 | 動作 |
|--------|------|------|
| `&&` | 論理AND | 両方のオペランドが `true` の場合のみ `true` を返す |
| `\|\|` | 論理OR | 少なくとも1つのオペランドが `true` なら `true` を返す |
| `!` | 論理NOT | ブール値を反転する（`true` → `false`、`false` → `true`） |

---

## 3. 関係式

**関係式**は、等値（`==`）、不等（`!=`）、大なり（`>`）、小なり（`<`）、以上（`>=`）、以下（`<=`）などの関係演算子を使用して2つのオペランドを比較する式です。評価結果は常にブール型になります。

サイバーセキュリティでは、関係比較の不適切な処理（PHPの曖昧な比較 `==` と厳密な比較 `===`の混同、JavaScriptの型強制など）が、認証バイパス脆弱性（Type Juggling）の原因になります。

```c
/* ── C / Linuxシステムにおける関係式 ────────────── */
#include <stdio.h>

int main(void) {
    int user_uid = 1000;
    int root_uid = 0;
    
    int is_root = (user_uid == root_uid);       /* 結果は0（false） */
    int is_non_root = (user_uid >= 1000);      /* 結果は1（true）  */
    
    printf("Is Root: %d | Is Standard User: %d\n", is_root, is_non_root);
    return 0;
}
```

| 演算子 | 意味 | 例 | 結果 |
|--------|------|-----|------|
| `==` | 等しい | `10 == 10` | `true` |
| `!=` | 等しくない | `10 != 20` | `true` |
| `>` | より大きい | `15 > 10` | `true` |
| `<` | より小さい | `5 < 10` | `true` |
| `>=` | 以上 | `10 >= 10` | `true` |
| `<=` | 以下 | `9 <= 10` | `true` |

---

## 4. 代入式

**代入式**は、右辺の値（R-value）を左辺の変数やメモリ領域（L-value）に代入する式です。基本代入（`=`）のほか、`+=`、`-=`、`*=`、`/=`、`%=`、`<<=`、`>>=`、`&=`、`^=`、`|=` などの複合代入演算子が利用できます。

代入演算子は右結合性を持つため、`x = y = z = 10` という式はまず `z = 10` が評価され、その結果が `y` に、最後に `x` に代入されます。

```java
// ── 複合代入と前置・後置インクリメント ──────────────
int counter = 0;

counter += 5;    // counter = counter + 5  → 5
counter *= 2;    // counter = counter * 2  → 10
counter -= 3;    // counter = counter - 3  → 7
counter %= 4;    // counter = counter % 4  → 3

// 前置(prefix)と後置(postfix)の評価の違い
int a = 5;
int b = ++a;     // 前置: aが先に6になり、bに6が代入される
int c = a++;     // 後置: cに6が代入されてから、aが7になる
```

---

## 5. 条件式（三項演算子）

**条件式**（3つのオペランドを取ることから三項演算子とも呼ばれる）は、`if-else` 制御構造をインラインで簡潔に記述したもので、ブール条件に基づいて2つの式のうちいずれか1つを評価して返します。

構文：`条件 ? trueの場合の式 : falseの場合の式;`

```python
# ── Pythonのインライン三項演算 ─────────────────────────────────
user_role = "admin"
access_level = 100 if user_role == "admin" else 10
print(f"Access Level: {access_level}")
```

```c
/* ── Cの三項演算子 ───────────────────────────────────── */
#include <stdio.h>

int main(void) {
    int port = 443;
    const char *protocol = (port == 443) ? "HTTPS (Encrypted)" : "HTTP (Cleartext)";
    printf("Port %d runs %s\n", port, protocol);
    return 0;
}
```

---

## 6. ラムダ式

**ラムダ式**は、高階関数の引数として渡したり変数に格納したりできる無名関数（名前を持たない関数）です。Java 8以降、Python（`lambda`）、C++11（`[](){}`）、最近のC#など、現代の言語で広く採用されています。

セキュリティ分析やログ監視において、ラムダ式はネットワークパケットのフィルタリング、Webアクセスログの抽出、リアルタイムイベント変換を簡潔に書くために有用です。

```python
# ── ログ解析用のPythonラムダ ────────────────────────────
logs = [
    {"ip": "192.168.1.10", "status": 200, "path": "/index.html"},
    {"ip": "10.0.0.5",     "status": 404, "path": "/admin.php"},
    {"ip": "172.16.0.4",   "status": 401, "path": "/login"},
    {"ip": "10.0.0.5",     "status": 500, "path": "/api/v1/debug"}
]

# ラムダを使って失敗したリクエスト（status >= 400）を抽出
failed_requests = list(filter(lambda entry: entry["status"] >= 400, logs))
print(f"Suspicious / Failed Events: {failed_requests}")
```

```java
// ── JavaのラムダとStream API ─────────────────────────────────
import java.util.*;
import java.util.stream.*;

List<String> endpoints = Arrays.asList("/api/v1/users", "/admin", "/login", "/config.json");

List<String> sensitiveEndpoints = endpoints.stream()
    .filter(ep -> ep.contains("admin") || ep.contains("config"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());

System.out.println(sensitiveEndpoints); // [/ADMIN, /CONFIG.JSON]
```

---

## 7. 正規表現（RegEx）

**正規表現（RegEx）**は、テキストの検索パターンを定義する形式言語の式です。入力検証、文字列のトークン化、フォレンジックログの調査（SIEM/grep）、侵入検知ルールの作成（Suricata/Snort/YARA）で使われます。

参考文献：Jeffrey E.F. Friedl 著『Mastering Regular Expressions (3rd Edition)』（`~/Documents/Books/Linux/`）。

```bash
# ── grepによるサイバーセキュリティ向け正規表現の例 ────────────

# 有効なIPv4アドレスにマッチ
$ grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# MD5ハッシュ（16進数32文字）にマッチ
$ grep -E -i '\b[a-f0-9]{32}\b' sample_hashes.txt

# 機密性の高いAWSアクセスキーIDにマッチ
$ grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| メタ文字 | 説明 |
|----------|------|
| `^` / `$` | 文字列の先頭 / 末尾 |
| `.` | 任意の1文字（改行を除く） |
| `\d` / `\D` | 数字（0-9） / 非数字 |
| `\w` / `\W` | 単語構成文字（a-z、0-9、_） / 非単語文字 |
| `\s` / `\S` | 空白文字 / 非空白文字 |
| `*` / `+` / `?` | 量指定子：0回以上、1回以上、0または1回 |
| `{n,m}` | n回以上m回以下 |
| `[...]` | 文字クラス（指定文字のいずれか） |
| `(A\|B)` | 選択（AまたはBに一致） |

---

## 8. ビット演算式

**ビット演算式**は、整数データ型の個々のビットを直接操作する式です。暗号処理（XOR暗号、SHA/AESハッシュ演算）、ネットワークのサブネット計算、Unixファイルパーミッションの表現、マルウェア解析やシェルコードの復号など、幅広い場面で使われます。

主な演算子：AND（`&`）、OR（`|`）、XOR（`^`）、ビットNOT（`~`）、左シフト（`<<`）、右シフト（`>>`）。

```c
/* ── CによるビットXOR暗号化とパーミッションマスキング ───────── */
#include <stdio.h>

int main(void) {
    /* 1. 単純なXOR難読化（キー: 0x5A） */
    char original = 'A';              /* Binary: 01000001 */
    char key = 0x5A;                  /* Binary: 01011010 */
    
    char encrypted = original ^ key;  /* Binary: 00011011 */
    char decrypted = encrypted ^ key; /* Binary: 01000001 ('A') */
    
    printf("Original: %c | Encrypted: 0x%X | Decrypted: %c\n", original, (unsigned char)encrypted, decrypted);
    
    /* 2. Linuxファイルパーミッション（読み取り=4, 書き込み=2, 実行=1） */
    int rwx = (1 << 2) | (1 << 1) | (1 << 0); /* 4 | 2 | 1 = 7 */
    int is_executable = (rwx & 1);             /* 実行ビットを確認 */
    printf("Permission Octal: %d | Executable: %s\n", rwx, is_executable ? "YES" : "NO");
    
    return 0;
}
```

| 演算子 | 名称 | ビット演算（`a=5 [0101]`、`b=3 [0011]`） | 結果 |
|--------|------|--------------------------------------------|------|
| `&` | ビットAND | `0101 & 0011` → `0001` | `1` |
| `\|` | ビットOR | `0101 \| 0011` → `0111` | `7` |
| `^` | ビットXOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | ビット反転 | `~0101` → `...11111010` | `-6`（2の補数） |
| `<<` | 左シフト | `0101 << 1` → `1010`（2倍） | `10` |
| `>>` | 右シフト | `0101 >> 1` → `0010`（1/2） | `2` |

---

## 9. キャスト式

**キャスト式**は、評価された式をあるデータ型から別のデータ型に変換する式です。大きく2つに分けられます。

1. **拡大変換（暗黙的キャスト、widening）**: より小さい型から大きい型への変換（例：`int` から `double`）。安全で、コンパイラが自動的に行い、データ損失はありません。
2. **縮小変換（明示的キャスト、narrowing）**: より大きい型から小さい容量の型への変換（例：`double` から `int`、32ビット `int` から8ビット `char`）。明示的な構文 `(型)値` が必要で、切り捨てや整数オーバーフローのリスクを伴います。

```c
/* ── Cにおける整数切り捨て脆弱性の例 ─────────── */
#include <stdio.h>

int main(void) {
    int large_number = 300;
    /* 300を2進数(16bit)で表すと: 0000 0001 0010 1100 */
    /* 8ビットunsigned charへのキャストは下位8ビットのみを取る: 0010 1100 = 44 */
    unsigned char truncated = (unsigned char)large_number;
    
    printf("Original: %d | Truncated: %d\n", large_number, truncated);
    return 0;
}
```

---

## 10. オブジェクト生成式

**オブジェクト生成式**は、`new` キーワードを使用してヒープ領域に動的メモリを確保し、コンストラクタを呼び出して新しいインスタンスを初期化する式です。C++のような手動メモリ管理言語では、動的に確保したメモリはメモリリークやuse-after-freeを防ぐために `delete`/`free` で確実に解放する必要があります。

```java
// ── Javaにおけるオブジェクトのインスタンス化 ────────────────────────
public class TargetHost {
    private String hostname;
    private int port;

    public TargetHost(String hostname, int port) {
        this.hostname = hostname;
        this.port = port;
    }

    public void scan() {
        System.out.println("Scanning " + hostname + ":" + port);
    }

    public static void main(String[] args) {
        // オブジェクト生成式
        TargetHost target = new TargetHost("192.168.1.1", 443);
        target.scan();
    }
}
```

---

## 11. セキュリティノート: 式のリスクと防御コントロール

式評価の仕組みを理解することは、監査と堅牢化(ハードニング)のために重要です。信頼できない入力をコードとして評価すると、深刻な欠陥につながります。以下は検知と緩和策の要点です。

1. **Expression Language（EL）/ OGNLインジェクション**: ユーザー入力から得た式を評価してはいけません。リクエストデータに対する動的なSpEL/OGNL評価を無効化し、テンプレートは許可リスト方式にし、サンドボックス化はどうしても避けられない場合のみ行います。
2. **ReDoS**: 破滅的な入れ子量指定子を避け、マッチにタイムアウトを設けるか線形時間で動作するエンジンを使い、長い敵対的文字列でファジングして検証します（『Mastering Regular Expressions』やWAHHが詳しい）。
3. **Type Juggling**: 厳密な比較（`===` または型付き比較）を優先し、APIの境界で型を検証し、パスワードハッシュの比較に曖昧な `==` を使わないようにします。
4. **整数オーバーフロー（C）**: 十分な幅の型を使い、確保前にチェックし（`size_t` のオーバーフローチェック）、`-fsanitize=undefined,integer` を有効にし、K. N. Kingの型幅に関する規律に従います。
5. **シェル算術 / eval**: 生の入力に対して `eval` や `$((...))` を展開せず、変数をクォートし、構造化されたパーサを優先します。

防御チェックリスト: 信頼できない入力に `eval` を使わない、厳密な等価比較を使う、正規表現の複雑度に上限を設ける、算術演算はオーバーフローチェック付きで行う、式言語に対するSAST/WAFルールを整備する、境界値 \(0, 2^{w}-1, -2^{w-1}\) のテストを書く。

---

## 12. 要約とチートシート

| カテゴリ | 演算子・構文 | 説明 |
|----------|-------------|------|
| 算術 | `+`, `-`, `*`, `/`, `%` | 基本的な数学演算 |
| 論理 | `&&`, `\|\|`, `!` | 短絡評価によるブール論理 |
| 関係 | `==`, `!=`, `<`, `>`, `<=`, `>=` | 値の比較 |
| 代入 | `=`, `+=`, `-=`, `*=`, `/=` | 変数への値の代入 |
| 三項 | `cond ? val1 : val2` | インライン条件式 |
| ラムダ | `(param) -> { body }` | 簡潔な無名関数 |
| 正規表現 | `^`, `$`, `\d`, `\w`, `.*` | 文字列パターン照合 |
| ビット演算 | `&`, `\|`, `^`, `~`, `<<`, `>>` | ビットへの直接操作 |
| キャスト | `(type) value` | データ型の変換 |
| オブジェクト | `new ClassName()` | ヒープ確保とコンストラクタ呼び出し |

---

> **参考文献・書籍:**
> - K. N. King, *C Programming: A Modern Approach (2nd Edition)* (`~/Documents/Books/Programming/C /`)
> - Al Sweigart, *Automate the Boring Stuff with Python (2nd Edition)* (`~/Documents/Books/Programming/Python/`)
> - Jeffrey E.F. Friedl, *Mastering Regular Expressions (3rd Edition)* (`~/Documents/Books/CyberSec/Linux/`)
> - Dafydd Stuttard & Marcus Pinto, *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - Scott Meyers, *Effective Modern C++* (`~/Documents/Books/Programming/ C++/`)

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> **フィードバックや貢献を歓迎します。** 誤りを見つけた場合はissueまたはPRを開いてください。
