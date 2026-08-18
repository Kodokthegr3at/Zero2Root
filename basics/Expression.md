# 🧮 Expression — Syntax, Types & Evaluation

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-001` | **Phase 0:** Foundations  
> **Est. study:** 2-3h | **Level:** Beginner  
> **Prerequisites:** -  
> **Book map:** K. N. King Â C Programming Ch.2-5; Friedl Â Mastering Regular Expressions Ch.1-4; Sweigart Â Automate the Boring Stuff Ch.1-6
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Arithmetic Expression | Operasi matematika & aritmatika | Mathematical & arithmetic operations | 数学・算術演算 |
| 2 | Logical Expression | Logika boolean (AND, OR, NOT) | Boolean logic (AND, OR, NOT) | ブール論理（AND、OR、NOT） |
| 3 | Relational Expression | Perbandingan nilai (==, !=, <, >) | Value comparison (==, !=, <, >) | 値の比較（==、!=、<、>） |
| 4 | Assignment Expression | Penugasan & compound operators | Assignment & compound operators | 代入と複合代入演算子 |
| 5 | Conditional (Ternary) | Ekspresi kondisional tiga operand | Three-operand conditional expression | 三項演算子による条件式 |
| 6 | Lambda Expression | Fungsi anonim ringkas | Concise anonymous functions | 簡潔な無名関数（ラムダ式） |
| 7 | Regular Expression (RegEx) | Pencocokan pola string | String pattern matching | 文字列パターン照合（正規表現） |
| 8 | Bitwise Expression | Operasi level bit & manipulasi biner | Bit-level operations & binary manipulation | ビット単位の演算と操作 |
| 9 | Cast Expression | Konversi tipe data (widening/narrowing) | Data type conversion (widening/narrowing) | データ型変換（拡大・縮小キャスト） |
| 10 | Object Creation Expression | Alokasi memori & pembuatan objek | Memory allocation & object instantiation | メモリ確保とオブジェクト生成 |
| 11 | Security Note | Risiko & pertahanan ekspresi | Expression risks & defensive controls | 式のリスクと防御コントロール |
| 12 | Summary & Cheatsheet | Tabel ringkasan & cheatsheet cepat | Summary table & quick cheatsheet | 要約表とクイックチートシート |

---

## 1. ➕ Arithmetic Expression — Mathematical Operations

### 🇮🇩 Bahasa Indonesia
**Arithmetic Expression** adalah ekspresi yang menghasilkan nilai numerik melalui operasi matematika dasar seperti penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), pembagian (`/`), dan sisa bagi atau modulo (`%`). 

Dalam pemrograman sistem (C/C++) dan bahasa modern (Java, Python), urutan evaluasi mengikuti aturan **presedensi operator** (BODMAS/PEMDAS). Operasi perkalian, pembagian, dan modulo dievaluasi lebih dulu sebelum penjumlahan dan pengurangan, kecuali diatur eksplisit menggunakan tanda kurung `()`.

Secara formal (K. N. King), ekspresi aritmetika bilangan bulat dapat ditulis:

$$
E ::= n \mid (E) \mid E \;+\; E \mid E \;-\; E \mid E \;\times\; E \mid E \;/\; E \mid E \bmod E
$$

dengan evaluasi mengikuti asosiatif kiri dan prioritas \(\times,/,\% \;>\; +,-\). Integer overflow pada tipe lebar \(w\) bit terjadi ketika hasil berada di luar \(\bigl[-2^{w-1},\,2^{w-1}-1\bigr]\) (signed two's complement) atau \(\bigl[0,\,2^{w}-1\bigr]\) (unsigned) — sering memicu alokasi buffer yang salah ukuran di C.

### 🇬🇧 English
An **Arithmetic Expression** is an expression that evaluates to a numeric value through standard mathematical operations such as addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and remainder or modulo (`%`).

In system programming (C/C++) and modern languages (Java, Python), the evaluation order strictly adheres to **operator precedence** (BODMAS/PEMDAS). Multiplication, division, and modulo operations take precedence over addition and subtraction, unless explicitly grouped using parentheses `()`.

Formally (per K. N. King), integer arithmetic expressions can be described by the grammar:

$$
E ::= n \mid (E) \mid E \;+\; E \mid E \;-\; E \mid E \;\times\; E \mid E \;/\; E \mid E \bmod E
$$

evaluated left-associatively with precedence \(\times,/,\% \;>\; +,-\). Integer overflow on a \(w\)-bit type occurs when a result leaves \(\bigl[-2^{w-1},\,2^{w-1}-1\bigr]\) (signed) or \(\bigl[0,\,2^{w}-1\bigr]\) (unsigned) — a common root cause of undersized buffer allocations in C.

### 🇯🇵 日本語
**算術式**（Arithmetic Expression）は、加算（`+`）、減算（`-`）、乗算（`*`）、除算（`/`）、剰余（`%`）などの基本的な数学演算を通じて数値を算出する式です。

システムプログラミング（C/C++）や現代的な言語（Java、Python）では、評価順序は**演算子の優先順位**（BODMAS/PEMDAS）に従います。乗算、除算、剰余は、丸括弧 `()` で明示的にグループ化されていない限り、加算や減算よりも優先して評価されます。

形式的には（K. N. King）、整数算術式は次の文法で表せます：

$$
E ::= n \mid (E) \mid E \;+\; E \mid E \;-\; E \mid E \;\times\; E \mid E \;/\; E \mid E \bmod E
$$

左結合で、優先順位は \(\times,/,\% \;>\; +,-\) です。幅 \(w\) ビットの整数オーバーフローは結果が \(\bigl[-2^{w-1},\,2^{w-1}-1\bigr]\)（符号付き）または \(\bigl[0,\,2^{w}-1\bigr]\)（符号なし）を外れたときに発生し、Cでのバッファ確保ミスの典型的な原因になります。

```java
// ── Java Example ─────────────────────────────────────────────
int a = 10;
int b = 3;

int penjumlahan  = a + b;           // 13   — Add / Penjumlahan / 加算
int pengurangan  = a - b;           // 7    — Subtract / Pengurangan / 減算
int perkalian    = a * b;           // 30   — Multiply / Perkalian / 乗算
int pembagian    = a / b;           // 3    — Integer Division / Pembagian / 除算
int sisa_bagi    = a % b;           // 1    — Modulo (Remainder) / Sisa bagi / 剰余
double pangkat   = Math.pow(a, 2); // 100.0 — Power / Pangkat / べき乗
```

```c
/* ── C Example (K. N. King - C Programming Standard) ────────── */
#include <stdio.h>

int main(void) {
    int total_seconds = 3665;
    int hours   = total_seconds / 3600;       /* 1 hour */
    int minutes = (total_seconds % 3600) / 60; /* 1 minute */
    int seconds = total_seconds % 60;         /* 5 seconds */
    
    printf("Time: %02d:%02d:%02d\n", hours, minutes, seconds);
    return 0;
}
```

| Operator | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 | Example | Result |
|----------|-----------|-------------|---------|---------|--------|
| `+` | Penjumlahan | Addition | 加算 | `10 + 3` | `13` |
| `-` | Pengurangan | Subtraction | 減算 | `10 - 3` | `7` |
| `*` | Perkalian | Multiplication | 乗算 | `10 * 3` | `30` |
| `/` | Pembagian | Division | 除算 | `10 / 3` | `3` (integer) |
| `%` | Modulo (Sisa bagi) | Modulo (Remainder) | 剰余 | `10 % 3` | `1` |

---

## 2. ✅ Logical (Boolean) Expression — Boolean Logic

### 🇮🇩 Bahasa Indonesia
**Logical Expression** adalah ekspresi yang mengevaluasi kondisi ke nilai boolean (`true` atau `false`) menggunakan operator logika `&&` (Logical AND), `||` (Logical OR), dan `!` (Logical NOT).

Bahasa pemrograman modern menggunakan **short-circuit evaluation**:
- Pada operasi `A && B`, jika `A` bernilai `false`, maka `B` tidak akan dievaluasi karena hasilnya pasti `false`.
- Pada operasi `A || B`, jika `A` bernilai `true`, maka `B` tidak akan dievaluasi karena hasilnya pasti `true`.

### 🇬🇧 English
A **Logical Expression** is an expression that evaluates conditions into a boolean value (`true` or `false`) utilizing logical operators `&&` (Logical AND), `||` (Logical OR), and `!` (Logical NOT).

Modern programming languages implement **short-circuit evaluation**:
- In `A && B`, if `A` evaluates to `false`, `B` is not evaluated because the entire expression is guaranteed to be `false`.
- In `A || B`, if `A` evaluates to `true`, `B` is not evaluated because the entire expression is guaranteed to be `true`.

### 🇯🇵 日本語
**論理式**（Logical Expression）は、論理演算子 `&&`（論理積 AND）、`||`（論理和 OR）、`!`（論理否定 NOT）を使用して、条件をブール値（`true` または `false`）として評価する式です。

現代のプログラミング言語は**短絡評価（ショートサーキット評価）**を採用しています：
- `A && B` では、`A` が `false` の場合、式全体が `false` に確定するため `B` は評価されません。
- `A || B` では、`A` が `true` の場合、式全体が `true` に確定するため `B` は評価されません。

```java
// ── Short-circuit evaluation example ────────────────────────
String username = getUsername();
// If username is null, username.length() is NEVER called (avoids NullPointerException)
if (username != null && username.length() > 3) {
    System.out.println("Valid user format");
}

// ── Logical operations ───────────────────────────────────────
boolean isAuthenticated = true;
boolean hasAdminRole    = false;

boolean canAccessDashboard = isAuthenticated && hasAdminRole; // false
boolean canViewPublicPage  = isAuthenticated || hasAdminRole; // true
boolean isGuest            = !isAuthenticated;                // false
```

| Operator | 🇮🇩 Nama | 🇬🇧 Name | 🇯🇵 名前 | Behavior |
|----------|---------|---------|---------|----------|
| `&&` | DAN (Logical AND) | Logical AND | 論理AND | Returns `true` only if **both** operands are `true` |
| `\|\|` | ATAU (Logical OR) | Logical OR | 論理OR | Returns `true` if **at least one** operand is `true` |
| `!` | TIDAK (Logical NOT) | Logical NOT | 論理NOT | Inverts boolean state (`true` → `false`, `false` → `true`) |

---

## 3. 🔍 Relational Expression — Comparison Operators

### 🇮🇩 Bahasa Indonesia
**Relational Expression** membandingkan dua operand menggunakan operator relasional seperti sama dengan (`==`), tidak sama dengan (`!=`), lebih besar (`>`), lebih kecil (`<`), lebih besar atau sama (`>=`), dan lebih kecil atau sama (`<=`). Hasil evaluasinya selalu bertipe boolean.

Dalam cybersecurity, perbandingan relasional yang salah penanganan (seperti *loose comparison* di PHP atau *type coercion* di JavaScript) sering menjadi akar celah autentikasi (*Type Juggling*).

### 🇬🇧 English
A **Relational Expression** compares two operands using relational operators including equality (`==`), inequality (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`). The result is strictly a boolean value.

In cybersecurity, improperly handled relational comparisons (such as PHP loose comparisons `==` vs strict `===`, or JavaScript type coercion) frequently introduce critical authentication bypass vulnerabilities (*Type Juggling*).

### 🇯🇵 日本語
**関係式**（Relational Expression）は、等値（`==`）、不等（`!=`）、大なり（`>`）、小なり（`<`）、以上（`>=`）、以下（`<=`）などの関係演算子を使用して2つのオペランドを比較する式です。評価結果は常にブール型になります。

サイバーセキュリティでは、関係比較の不適切な処理（PHPの曖昧な比較 `==` と厳密な比較 `===`、JavaScriptの型強制など）が、重大な認証バイパス脆弱性（*Type Juggling*）の原因となります。

```c
/* ── Relational Expression in C / Linux Systems ────────────── */
#include <stdio.h>

int main(void) {
    int user_uid = 1000;
    int root_uid = 0;
    
    int is_root = (user_uid == root_uid);       /* evaluates to 0 (false) */
    int is_non_root = (user_uid >= 1000);      /* evaluates to 1 (true)  */
    
    printf("Is Root: %d | Is Standard User: %d\n", is_root, is_non_root);
    return 0;
}
```

| Operator | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 | Example | Result |
|----------|---------|------------|---------|---------|--------|
| `==` | Sama dengan | Equal to | 等しい | `10 == 10` | `true` |
| `!=` | Tidak sama dengan | Not equal to | 等しくない | `10 != 20` | `true` |
| `>` | Lebih besar dari | Greater than | より大きい | `15 > 10` | `true` |
| `<` | Lebih kecil dari | Less than | より小さい | `5 < 10` | `true` |
| `>=` | Lebih besar atau sama | Greater than or equal | 以上 | `10 >= 10` | `true` |
| `<=` | Lebih kecil atau sama | Less than or equal | 以下 | `9 <= 10` | `true` |

---

## 4. 📥 Assignment Expression — Variable Assignments

### 🇮🇩 Bahasa Indonesia
**Assignment Expression** menetapkan nilai sisi kanan (R-value) ke variabel atau lokasi memori sisi kiri (L-value). Selain penugasan dasar (`=`), bahasa modern menyediakan operator majemuk (*compound assignment*) seperti `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`.

Operator penugasan bersifat *right-associative*, artinya `x = y = z = 10` akan mengevaluasi `z = 10` lebih dulu, lalu `y = z`, dan akhirnya `x = y`.

### 🇬🇧 English
An **Assignment Expression** assigns the value of the right-hand operand (R-value) to the left-hand storage location or variable (L-value). Besides basic assignment (`=`), modern languages support *compound assignment operators* such as `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`.

Assignment operators are *right-associative*, meaning an expression like `x = y = z = 10` evaluates `z = 10` first, then assigns the result to `y`, and finally to `x`.

### 🇯🇵 日本語
**代入式**（Assignment Expression）は、右辺の値（R-value）を左辺の変数やメモリ領域（L-value）に格納・代入する式です。基本代入（`=`）のほか、`+=`、`-=`、`*=`、`/=`、`%=`、`<<=`、`>>=`、`&=`、`^=`、`|=` などの*複合代入演算子*が利用可能です。

代入演算子は*右結合性（Right-associative）*を持つため、`x = y = z = 10` という式はまず `z = 10` が評価され、その結果が `y` に、最後に `x` に代入されます。

```java
// ── Compound Assignments & Pre/Post Increments ──────────────
int counter = 0;

counter += 5;    // counter = counter + 5  → 5
counter *= 2;    // counter = counter * 2  → 10
counter -= 3;    // counter = counter - 3  → 7
counter %= 4;    // counter = counter % 4  → 3

// Prefix vs Postfix evaluation
int a = 5;
int b = ++a;     // Prefix: a becomes 6, then b is assigned 6
int c = a++;     // Postfix: c is assigned 6, then a becomes 7
```

---

## 5. ❓ Conditional (Ternary) Expression — Inline Decisions

### 🇮🇩 Bahasa Indonesia
**Conditional Expression** (sering disebut **Ternary Operator** karena membutuhkan tiga operand) adalah bentuk ringkas dari struktur kendali `if-else` yang mengevaluasi dan mengembalikan salah satu dari dua ekspresi berdasarkan kondisi boolean.

Sintaks: `condition ? expression_if_true : expression_if_false;`

### 🇬🇧 English
A **Conditional Expression** (commonly called the **Ternary Operator** because it takes three operands) is a concise inline alternative to an `if-else` control structure that evaluates and returns one of two expressions based on a boolean condition.

Syntax: `condition ? expression_if_true : expression_if_false;`

### 🇯🇵 日本語
**条件式**（Conditional Expression、3つのオペランドを取ることから**三項演算子**とも呼ばれる）は、`if-else` 制御構造をインラインで簡潔に記述したもので、ブール条件に基づいて2つの式のうちいずれか1つを評価して返します。

構文：`条件 ? trueの場合の式 : falseの場合の式;`

```python
# ── Python inline ternary ─────────────────────────────────────
user_role = "admin"
access_level = 100 if user_role == "admin" else 10
print(f"Access Level: {access_level}")
```

```c
/* ── C Ternary Expression ───────────────────────────────────── */
#include <stdio.h>

int main(void) {
    int port = 443;
    const char *protocol = (port == 443) ? "HTTPS (Encrypted)" : "HTTP (Cleartext)";
    printf("Port %d runs %s\n", port, protocol);
    return 0;
}
```

---

## 6. λ Lambda Expression — Functional Abstractions

### 🇮🇩 Bahasa Indonesia
**Lambda Expression** adalah blok kode anonim (fungsi tanpa nama) yang dapat diteruskan sebagai argumen ke metode atau disimpan dalam variabel. Diperkenalkan pada Java 8, Python (`lambda`), C++11 (`[](){}`), dan modern C#.

Dalam analisis keamanan dan pemrosesan log, lambda sangat efisien untuk memfilter paket jaringan, parsing log web server, dan transformasi data cepat.

### 🇬🇧 English
A **Lambda Expression** is an anonymous function (a function without a declared name) that can be passed as an argument to higher-order functions or assigned to variables. Supported across modern programming languages (Java 8+, Python `lambda`, C++11 lambdas, JavaScript arrow functions `() => {}`).

In cybersecurity telemetry and log analysis, lambdas provide powerful, concise syntax for filtering network packet streams, parsing server access logs, and real-time event transformation.

### 🇯🇵 日本語
**ラムダ式**（Lambda Expression）は、高階関数の引数として渡したり変数に格納したりできる無名関数（名前を持たない関数）です。Java 8+、Python（`lambda`）、C++11、JavaScript（アロー関数 `() => {}`）などで広く採用されています。

セキュリティ分析やログ監視において、ラムダ式はネットワークパケットのフィルタリング、Webアクセスログの抽出、リアルタイムイベント変換を簡潔に実装するために極めて有用です。

```python
# ── Python Lambda for Log Analysis ────────────────────────────
logs = [
    {"ip": "192.168.1.10", "status": 200, "path": "/index.html"},
    {"ip": "10.0.0.5",     "status": 404, "path": "/admin.php"},
    {"ip": "172.16.0.4",   "status": 401, "path": "/login"},
    {"ip": "10.0.0.5",     "status": 500, "path": "/api/v1/debug"}
]

# Filter failed requests (status >= 400) using lambda
failed_requests = list(filter(lambda entry: entry["status"] >= 400, logs))
print(f"Suspicious / Failed Events: {failed_requests}")
```

```java
// ── Java Lambda & Stream API ─────────────────────────────────
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

## 7. 🔎 Regular Expression (RegEx) — Pattern Matching

### 🇮🇩 Bahasa Indonesia
**Regular Expression (RegEx)** adalah ekspresi formal yang mendefinisikan pola pencarian teks. Digunakan untuk validasi data, ekstraksi string, pencarian log forensik (SIEM/grep), dan pembentukan aturan deteksi (Suricata/Snort/YARA).

Referensi mendalam: *Mastering Regular Expressions (3rd Edition)* oleh Jeffrey E.F. Friedl (`~/Documents/Books/Linux/`).

### 🇬🇧 English
A **Regular Expression (RegEx)** is a formal sequence of characters defining a search pattern. Extensively applied in input validation, string tokenization, forensic log searching (SIEM/grep), and intrusion detection signatures (Suricata/Snort/YARA).

Reference standard: *Mastering Regular Expressions (3rd Edition)* by Jeffrey E.F. Friedl (`~/Documents/Books/Linux/`).

### 🇯🇵 日本語
**正規表現**（Regular Expression / RegEx）は、テキストの検索パターンを定義する形式言語式です。入力検証、文字列のトークン化、フォレンジックログの調査（SIEM/grep）、侵入検知ルール（Suricata/Snort/YARA）で不可欠な技術です。

標準参照資料：Jeffrey E.F. Friedl 著『Mastering Regular Expressions (3rd Edition)』（`~/Documents/Books/Linux/`）。

```bash
# ── Common Cybersecurity Regex Examples with grep ────────────

# Match valid IPv4 addresses
$ grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# Match MD5 Hashes (32 hex characters)
$ grep -E -i '\b[a-f0-9]{32}\b' sample_hashes.txt

# Match sensitive AWS Access Key IDs
$ grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| Metacharacter | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|---------------|--------------|----------------|---------|
| `^` / `$` | Awal / Akhir string | Start / End of string | 文字列の先頭 / 末尾 |
| `.` | Karakter apa saja (kecuali newline) | Any character (except newline) | 任意の1文字 |
| `\d` / `\D` | Digit angka (0-9) / Non-digit | Digit (0-9) / Non-digit | 数字（0-9） / 非数字 |
| `\w` / `\W` | Alfanumerik + `_` / Non-word | Word char (a-z, 0-9, _) / Non-word | 単語構成文字 / 非単語文字 |
| `\s` / `\S` | Whitespace (spasi, tab) / Non-space | Whitespace / Non-whitespace | 空白文字 / 非空白文字 |
| `*` / `+` / `?` | 0+, 1+, atau 0-1 kemunculan | Quantifiers: 0+, 1+, or 0-1 occurrences | 量指定子：0回以上、1回以上、0または1回 |
| `{n,m}` | Antara n hingga m kali | Between n and m times | n回以上m回以下 |
| `[...]` | Character class (salah satu karakter) | Character class set | 文字クラス（指定文字のいずれか） |
| `(A\|B)` | Alternasi (pilihan A atau B) | Alternation (group match A or B) | 選択（AまたはBに一致） |

---

## 8. 🔢 Bitwise Expression — Low-Level Bit Operations

### 🇮🇩 Bahasa Indonesia
**Bitwise Expression** memanipulasi bit biner secara langsung pada tipe data integer. Digunakan secara luas dalam kriptografi (XOR cipher, hashing), sistem jaringan (subnet masking), permission sistem file Unix, dan analisis malware/shellcode.

Operasi bitwise meliputi AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Left Shift (`<<`), dan Right Shift (`>>`).

### 🇬🇧 English
A **Bitwise Expression** directly manipulates individual binary bits of integer data types. Universally utilized in cryptography (XOR ciphers, SHA/AES hashing rounds), network subnet calculation, Unix permission masking, and malware reverse engineering / shellcode decoding.

Core operators: AND (`&`), OR (`|`), XOR (`^`), Bitwise NOT (`~`), Left Shift (`<<`), and Right Shift (`>>`).

### 🇯🇵 日本語
**ビット演算式**（Bitwise Expression）は、整数データ型の個々のビットを直接操作する式です。暗号処理（XOR暗号、SHA/AESハッシュ演算）、ネットワークサブネット計算、Unixファイルパーミッション、マルウェア解析・シェルコードの復号で基礎となる演算です。

主要演算子：AND（`&`）、OR（`|`）、XOR（`^`）、ビットNOT（`~`）、左シフト（`<<`）、右シフト（`>>`）。

```c
/* ── Bitwise XOR Encryption & Permission Masking in C ───────── */
#include <stdio.h>

int main(void) {
    /* 1. Simple XOR Obfuscation (Key: 0x5A) */
    char original = 'A';              /* Binary: 01000001 */
    char key = 0x5A;                  /* Binary: 01011010 */
    
    char encrypted = original ^ key;  /* Binary: 00011011 */
    char decrypted = encrypted ^ key; /* Binary: 01000001 ('A') */
    
    printf("Original: %c | Encrypted: 0x%X | Decrypted: %c\n", original, (unsigned char)encrypted, decrypted);
    
    /* 2. Linux File Permissions (Read=4, Write=2, Execute=1) */
    int rwx = (1 << 2) | (1 << 1) | (1 << 0); /* 4 | 2 | 1 = 7 */
    int is_executable = (rwx & 1);             /* Check execute bit */
    printf("Permission Octal: %d | Executable: %s\n", rwx, is_executable ? "YES" : "NO");
    
    return 0;
}
```

| Operator | 🇮🇩 Nama | 🇬🇧 Operator Name | 🇯🇵 名前 | Bit Operation (`a=5 [0101]`, `b=3 [0011]`) | Result |
|----------|---------|------------------|---------|-------------------------------------------|--------|
| `&` | Bitwise AND | Bitwise AND | ビットAND | `0101 & 0011` → `0001` | `1` |
| `\|` | Bitwise OR | Bitwise OR | ビットOR | `0101 \| 0011` → `0111` | `7` |
| `^` | Bitwise XOR | Bitwise XOR | ビットXOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | Bitwise NOT | Bitwise NOT | ビット反転 | `~0101` → `...11111010` | `-6` (2's comp) |
| `<<` | Left Shift | Bitwise Left Shift | 左シフト | `0101 << 1` → `1010` (multiply by 2) | `10` |
| `>>` | Right Shift | Bitwise Right Shift | 右シフト | `0101 >> 1` → `0010` (divide by 2) | `2` |

---

## 9. 🔄 Cast Expression — Type Conversion

### 🇮🇩 Bahasa Indonesia
**Cast Expression** mengonversi ekspresi dari satu tipe data ke tipe data lain. Dibagi menjadi dua kategori utama:
1. **Widening Cast (Implicit)** — Konversi dari tipe data lebih kecil ke lebih besar (misal `int` ke `double`). Aman dan dilakukan otomatis oleh kompilator tanpa risiko kehilangan presisi.
2. **Narrowing Cast (Explicit)** — Konversi dari tipe data lebih besar ke lebih kecil (misal `double` ke `int`, atau `int` ke `short`). Membutuhkan casting manual `(tipe)nilai` dan berisiko memotong data (*data truncation*) atau overflow.

### 🇬🇧 English
A **Cast Expression** converts an evaluated expression from one data type to another. Categorized into two core mechanisms:
1. **Widening Cast (Implicit / Promotion)** — Converts smaller data types to larger types (e.g., `int` to `double`). Safe and performed automatically by the compiler without data loss.
2. **Narrowing Cast (Explicit)** — Converts larger data types into smaller capacities (e.g., `double` to `int`, or 32-bit `int` to 8-bit `char`). Requires explicit syntax `(type)val` and carries risk of truncation or integer overflow.

### 🇯🇵 日本語
**キャスト式**（Cast Expression）は、評価された式をあるデータ型から別のデータ型に明示的または暗黙的に変換する式です。
1. **拡大変換（暗黙的キャスト / Widening）** — より小さい型から大きい型への変換（例：`int` から `double`）。安全で、コンパイラが自動的に行いデータ損失はありません。
2. **縮小変換（明示的キャスト / Narrowing）** — より大きい型から小さい容量の型への変換（例：`double` から `int`、32ビット `int` から 8ビット `char`）。明示的な構文 `(型)値` が必要であり、切り捨てや整数オーバーフローのリスクを伴います。

```c
/* ── Integer Truncation Vulnerability Example in C ─────────── */
#include <stdio.h>

int main(void) {
    int large_number = 300;
    /* 300 in binary (16-bit): 0000 0001 0010 1100 */
    /* Cast to 8-bit unsigned char takes lowest 8 bits: 0010 1100 = 44 */
    unsigned char truncated = (unsigned char)large_number;
    
    printf("Original: %d | Truncated: %d\n", large_number, truncated);
    return 0;
}
```

---

## 10. 🏗️ Object Creation Expression — Instantiation

### 🇮🇩 Bahasa Indonesia
**Object Creation Expression** mengalokasikan memori di area *Heap* dan menginisialisasi objek baru menggunakan kata kunci `new` serta memanggil konstruktor terkait. Di bahasa tanpa garbage collection otomatis seperti C++, alokasi dinamis dilakukan dengan `new`/`malloc` dan wajib dibebaskan dengan `delete`/`free` untuk mencegah *Memory Leak*.

### 🇬🇧 English
An **Object Creation Expression** allocates memory dynamically on the *Heap* and initializes a new object instance using the `new` keyword while invoking its constructor. In unmanaged languages like C++, dynamically allocated memory (`new`/`malloc`) must be explicitly released (`delete`/`free`) to avoid *Memory Leaks* or *Use-After-Free* flaws.

### 🇯🇵 日本語
**オブジェクト生成式**（Object Creation Expression）は、`new` キーワードを使用して*ヒープ*領域に動的メモリを確保し、コンストラクタを呼び出して新しいインスタンスを初期化する式です。C++のような手動メモリ管理言語では、動的確保されたメモリは*メモリリーク*や*Use-After-Free*を防ぐため、`delete`/`free` で確実に解放する必要があります。

```java
// ── Java Object Instantiation ────────────────────────────────
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
        // Object creation expression
        TargetHost target = new TargetHost("192.168.1.1", 443);
        target.scan();
    }
}
```

---

## 11. 🔐 Security Note — Expression Risks & Defensive Controls

### 🇮🇩 Bahasa Indonesia
Pemahaman evaluasi ekspresi krusial untuk **audit & hardening**. Input tidak tepercaya yang dievaluasi sebagai kode sering memicu kerentanan; fokus di bawah adalah **deteksi + mitigasi**:

1. **Expression Language (EL) / OGNL Injection**: Jangan evaluasi ekspresi dari input pengguna. Gunakan allowlist template, matikan evaluasi dinamis (SpEL/OGNL) pada data request, dan sandbox interpreter jika wajib ada.
2. **ReDoS**: Hindari nested quantifiers catastrophik; tetapkan timeout/engine linear-time; uji pola dengan fuzzer panjang (*Mastering Regular Expressions* / WAHH).
3. **Type Juggling**: Pakai perbandingan ketat (`===` / typed compares); validasi tipe di boundary API; jangan bandingkan hash string dengan `==`.
4. **Integer Overflow (C)**: Gunakan tipe lebar cukup, cek sebelum alokasi (`size_t` overflow checks), enable sanitizer (`-fsanitize=undefined,integer`), dan ikuti disiplin K. N. King untuk batas tipe.
5. **Bash / eval surfaces**: Jangan `eval` atau `$((...))` atas input mentah; quote variabel; prefer parser terstruktur.

**Defense checklist:** never `eval` untrusted input · strict equality · regex complexity budgets · checked arithmetic · WAF/SAST rules for SpEL/OGNL · unit tests for boundary values \(0, 2^{w}-1, -2^{w-1}\).

### 🇬🇧 English
Expression evaluation literacy matters for **audit and hardening**. Untrusted input evaluated as code creates critical bugs; prioritize **detection and mitigation**:

1. **EL / OGNL Injection**: Never evaluate user-supplied expressions. Disable dynamic SpEL/OGNL on request data; allowlist templates; sandbox only if unavoidable.
2. **ReDoS**: Avoid catastrophic nested quantifiers; enforce match timeouts or linear-time engines; fuzz long adversarial strings (*Mastering Regular Expressions* / WAHH).
3. **Type Juggling**: Prefer strict equality (`===`); validate types at API boundaries; never compare password hashes with loose `==`.
4. **Integer Overflow (C)**: Widen types, check before allocation, enable `-fsanitize=undefined,integer`, and follow K. N. King type-width discipline.
5. **Shell arithmetic / eval**: Do not `eval` or expand `$((...))` on raw input; quote expansions; prefer structured parsers.

**Defense checklist:** no `eval` on untrusted input · strict equality · regex complexity budgets · checked arithmetic · SAST/WAF for expression languages · boundary tests for \(0, 2^{w}-1, -2^{w-1}\).

### 🇯🇵 日本語
式評価の理解は**監査と堅牢化**に不可欠です。信頼できない入力をコードとして評価すると重大な欠陥になります。重点は**検知と緩和**です：

1. **EL / OGNL インジェクション**: ユーザー入力の式評価を禁止。動的SpEL/OGNLを無効化し、テンプレートを許可リスト化、やむを得ない場合のみサンドボックス化。
2. **ReDoS**: 破滅的な入れ子量指定子を避け、タイムアウトや線形時間エンジンを使い、長い敵対文字列で検証（『Mastering Regular Expressions』等）。
3. **Type Juggling**: 厳密比較（`===`）と境界での型検証。ハッシュ比較に曖昧な `==` を使わない。
4. **整数オーバーフロー（C）**: 十分な幅の型、確保前チェック、`-fsanitize=undefined,integer`、K. N. King の型幅規律。
5. **シェル算術 / eval**: 生入力に対する `eval` や `$((...))` を避け、クォートし、構造化パーサを優先。

**防御チェックリスト:** 信頼できない入力の `eval` 禁止 · 厳密比較 · 正規表現複雑度上限 · 検査付き算術 · 式言語向け SAST/WAF · 境界値 \(0, 2^{w}-1, -2^{w-1}\) のテスト。

---

## 12. 📊 Summary & Cheatsheet

| Category | Operator / Syntax | 🇮🇩 Deskripsi | 🇬🇧 Description | 🇯🇵 説明 |
|----------|-------------------|--------------|----------------|---------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%` | Operasi matematika dasar | Basic arithmetic computation | 基本数学演算 |
| **Logical** | `&&`, `\|\|`, `!` | Operasi logika boolean | Short-circuit boolean logic | 短絡ブール論理演算 |
| **Relational** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Perbandingan nilai | Value comparison | 値の大小・等値比較 |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=` | Penugasan nilai ke memori | Assign value to variable | 変数への値代入 |
| **Ternary** | `cond ? val1 : val2` | Kondisional inline ringkas | Inline conditional ternary | インライン三項条件式 |
| **Lambda** | `(param) -> { body }` | Fungsi anonim tanpa nama | Concise anonymous function | 簡潔な無名関数 |
| **RegEx** | `^`, `$`, `\d`, `\w`, `.*` | Pencocokan pola string | String pattern matching | 文字列パターン照合 |
| **Bitwise** | `&`, `\|`, `^`, `~`, `<<`, `>>` | Operasi langsung pada bit | Direct binary bit operations | ビット直接操作演算 |
| **Cast** | `(type) value` | Konversi tipe data | Type conversion / coercion | データ型の変換 |
| **Object** | `new ClassName()` | Alokasi heap & instansiasi | Heap allocation & constructor | オブジェクトの動的生成 |

---

> 📚 **References & Book Sources:**
> - K. N. King — *C Programming: A Modern Approach (2nd Edition)* (`~/Documents/Books/Programming/C /`)
> - Al Sweigart — *Automate the Boring Stuff with Python (2nd Edition)* (`~/Documents/Books/Programming/Python/`)
> - Jeffrey E.F. Friedl — *Mastering Regular Expressions (3rd Edition)* (`~/Documents/Books/CyberSec/Linux/`)
> - Dafydd Stuttard & Marcus Pinto — *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - Scott Meyers — *Effective Modern C++* (`~/Documents/Books/Programming/ C++/`)

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026  
> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.