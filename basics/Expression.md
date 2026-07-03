# 🧮 Expression

> 📅 Dibuat: 2026 | 🇮🇩 Bahasa Indonesia · 🇯🇵 日本語

---

## 📖 Daftar Isi / 目次

| # | Expression | 🇮🇩 Bahasa Indonesia | 🇯🇵 日本語 |
|---|-----------|---------------------|----------|
| 1 | Arithmetic Expression | Ekspresi matematika | 算術式 |
| 2 | Logical (Boolean) Expression | Ekspresi logika | 論理式 |
| 3 | Relational Expression | Ekspresi relasional | 関係式 |
| 4 | Assignment Expression | Ekspresi penugasan | 代入式 |
| 5 | Conditional (Ternary) Expression | Ekspresi kondisional | 条件式（三項演算子） |
| 6 | Lambda Expression | Ekspresi lambda | ラムダ式 |
| 7 | Regular Expression (Regex) | Ekspresi reguler | 正規表現 |
| 8 | Bitwise Expression | Ekspresi bitwise | ビット演算式 |
| 9 | Cast Expression | Ekspresi cast | キャスト式 |
| 10 | Object Creation Expression | Ekspresi pembuatan objek | オブジェクト生成式 |

---

## 1. ➕ Arithmetic Expression — Ekspresi Aritmatika

### 🇮🇩 Bahasa Indonesia
**Arithmetic Expression** adalah ekspresi untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

### 🇯🇵 日本語
**算術式**（Arithmetic Expression）は加算・減算・乗算・除算などの数学的な演算を行う式です。

```java
int a = 10;
int b = 3;

int penjumlahan  = a + b;    // 13  — tambah / 加算
int pengurangan  = a - b;    // 7   — kurang / 減算
int perkalian    = a * b;    // 30  — kali / 乗算
int pembagian    = a / b;    // 3   — bagi (integer) / 除算
int sisa_bagi    = a % b;    // 1   — modulo / 剰余
double pangkat   = Math.pow(a, 2);  // 100.0 — pangkat / べき乗

System.out.println(penjumlahan);   // 13
System.out.println(sisa_bagi);     // 1
```

| Operator | 🇮🇩 Fungsi | 🇯🇵 機能 | Contoh | Hasil |
|----------|-----------|---------|--------|-------|
| `+` | Penjumlahan | 加算 | `10 + 3` | `13` |
| `-` | Pengurangan | 減算 | `10 - 3` | `7` |
| `*` | Perkalian | 乗算 | `10 * 3` | `30` |
| `/` | Pembagian | 除算 | `10 / 3` | `3` |
| `%` | Sisa bagi (modulo) | 剰余 | `10 % 3` | `1` |

---

## 2. ✅ Logical (Boolean) Expression — Ekspresi Logika

### 🇮🇩 Bahasa Indonesia
**Logical Expression** adalah ekspresi yang menghasilkan nilai `true` atau `false` berdasarkan operasi logika.

### 🇯🇵 日本語
**論理式**（Logical Expression）は論理演算に基づいて `true` または `false` の値を返す式です。

```java
boolean a = true;
boolean b = false;

System.out.println(a && b);    // false — AND / かつ (両方がtrueのときtrue)
System.out.println(a || b);    // true  — OR  / または (どちらかがtrueのときtrue)
System.out.println(!a);        // false — NOT / でない (反転)
System.out.println(a && !b);   // true  — AND + NOT

// Contoh penggunaan nyata / 実際の使用例
int umur = 20;
boolean punyaSIM = true;

boolean bolehMenyetir = (umur >= 17) && punyaSIM;
System.out.println(bolehMenyetir);   // true
```

| Operator | 🇮🇩 Nama | 🇯🇵 名前 | Hasil |
|----------|---------|---------|-------|
| `&&` | DAN (AND) | 論理AND | `true` hanya jika keduanya `true` |
| `\|\|` | ATAU (OR) | 論理OR | `true` jika salah satu `true` |
| `!` | TIDAK (NOT) | 論理NOT | Membalikkan nilai boolean |

---

## 3. 🔍 Relational Expression — Ekspresi Relasional

### 🇮🇩 Bahasa Indonesia
**Relational Expression** adalah ekspresi yang membandingkan dua nilai menggunakan operator seperti `==`, `>`, `<`, atau `!=`. Hasilnya selalu `true` atau `false`.

### 🇯🇵 日本語
**関係式**（Relational Expression）は `==`、`>`、`<`、`!=` などの演算子を使って2つの値を比較する式です。結果は常に `true` または `false` になります。

```java
int x = 10;
int y = 20;

System.out.println(x == y);   // false — sama dengan / 等しい
System.out.println(x != y);   // true  — tidak sama / 等しくない
System.out.println(x > y);    // false — lebih besar / より大きい
System.out.println(x < y);    // true  — lebih kecil / より小さい
System.out.println(x >= 10);  // true  — lebih besar atau sama / 以上
System.out.println(x <= 9);   // false — lebih kecil atau sama / 以下

// Contoh penggunaan / 使用例
int nilai = 75;
boolean lulus = nilai >= 60;
System.out.println(lulus);    // true
```

| Operator | 🇮🇩 Arti | 🇯🇵 意味 | Contoh | Hasil |
|----------|---------|---------|--------|-------|
| `==` | Sama dengan | 等しい | `10 == 10` | `true` |
| `!=` | Tidak sama dengan | 等しくない | `10 != 20` | `true` |
| `>` | Lebih besar dari | より大きい | `10 > 5` | `true` |
| `<` | Lebih kecil dari | より小さい | `10 < 5` | `false` |
| `>=` | Lebih besar atau sama | 以上 | `10 >= 10` | `true` |
| `<=` | Lebih kecil atau sama | 以下 | `10 <= 9` | `false` |

---

## 4. 📥 Assignment Expression — Ekspresi Penugasan

### 🇮🇩 Bahasa Indonesia
**Assignment Expression** adalah ekspresi yang memberikan atau menetapkan nilai ke sebuah variabel.

### 🇯🇵 日本語
**代入式**（Assignment Expression）は変数に値を代入・設定する式です。

```java
int a = 10;       // assignment dasar / 基本代入

// Compound assignment / 複合代入演算子
a += 5;           // a = a + 5  → 15
a -= 3;           // a = a - 3  → 12
a *= 2;           // a = a * 2  → 24
a /= 4;           // a = a / 4  → 6
a %= 4;           // a = a % 4  → 2

// Increment & Decrement
int b = 5;
b++;              // b = b + 1  → 6
b--;              // b = b - 1  → 5
++b;              // pre-increment  → 6
--b;              // pre-decrement  → 5

// Multiple assignment / 複数代入
int x, y, z;
x = y = z = 100;  // x=100, y=100, z=100
System.out.println(x + " " + y + " " + z);   // 100 100 100
```

| Operator | 🇮🇩 Arti | 🇯🇵 意味 | Contoh | Setara dengan |
|----------|---------|---------|--------|---------------|
| `=` | Penugasan dasar | 基本代入 | `a = 10` | `a = 10` |
| `+=` | Tambah lalu simpan | 加算代入 | `a += 5` | `a = a + 5` |
| `-=` | Kurang lalu simpan | 減算代入 | `a -= 3` | `a = a - 3` |
| `*=` | Kali lalu simpan | 乗算代入 | `a *= 2` | `a = a * 2` |
| `/=` | Bagi lalu simpan | 除算代入 | `a /= 4` | `a = a / 4` |
| `%=` | Modulo lalu simpan | 剰余代入 | `a %= 4` | `a = a % 4` |

---

## 5. ❓ Conditional (Ternary) Expression — Ekspresi Kondisional

### 🇮🇩 Bahasa Indonesia
**Conditional Expression** atau **Ternary Expression** adalah ekspresi yang memilih satu dari dua nilai berdasarkan suatu kondisi. Disebut *ternary* karena menggunakan tiga operand.

### 🇯🇵 日本語
**条件式**（Conditional Expression）または**三項演算子**は条件に基づいて2つの値のうち1つを選択する式です。3つのオペランドを使うため *ternary*（三項）と呼ばれます。

```java
// Sintaks / 構文:
// kondisi ? nilai_jika_true : nilai_jika_false
// 条件 ? trueの場合の値 : falseの場合の値

int umur = 20;
String status = (umur >= 18) ? "Dewasa" : "Belum Dewasa";
System.out.println(status);   // Dewasa

// Setara dengan if-else / if-else文と同等
if (umur >= 18) {
    status = "Dewasa";
} else {
    status = "Belum Dewasa";
}

// Contoh lain / 他の例
int a = 10, b = 20;
int maks = (a > b) ? a : b;
System.out.println(maks);     // 20

// Nested ternary (hindari jika terlalu kompleks) / ネストは複雑になるので注意
int nilai = 85;
String grade = (nilai >= 90) ? "A" : (nilai >= 80) ? "B" : (nilai >= 70) ? "C" : "D";
System.out.println(grade);    // B
```

---

## 6. λ Lambda Expression — Ekspresi Lambda

### 🇮🇩 Bahasa Indonesia
**Lambda Expression** adalah ekspresi untuk mendefinisikan fungsi atau implementasi *functional interface* secara ringkas, tanpa perlu membuat class anonim secara eksplisit. Diperkenalkan di Java 8.

### 🇯🇵 日本語
**ラムダ式**（Lambda Expression）は関数や*関数型インターフェース*の実装を簡潔に定義するための式です。匿名クラスを明示的に作成する必要がなく、Java 8で導入されました。

```java
import java.util.*;
import java.util.stream.*;

// ── Sintaks dasar / 基本構文 ───────────────────────────────
// (parameter) -> { body }
// (パラメータ) -> { 処理 }

// Tanpa parameter / パラメータなし
Runnable salam = () -> System.out.println("Halo dari Lambda!");
salam.run();   // Halo dari Lambda!

// Dengan satu parameter / 1つのパラメータ
// (int x) -> x * x   →   bisa disingkat: x -> x * x
java.util.function.Function<Integer, Integer> kuadrat = x -> x * x;
System.out.println(kuadrat.apply(5));   // 25

// Dengan dua parameter / 2つのパラメータ
java.util.function.BiFunction<Integer, Integer, Integer> tambah = (a, b) -> a + b;
System.out.println(tambah.apply(3, 7)); // 10

// ── Contoh nyata dengan List / Listを使った実際の例 ────────
List<String> nama = Arrays.asList("Budi", "Andi", "Citra", "Dewi");

// Urutkan dengan lambda / ラムダでソート
nama.sort((a, b) -> a.compareTo(b));

// forEach dengan lambda / ラムダでforEach
nama.forEach(n -> System.out.println(n));

// Stream + lambda / Stream + ラムダ
List<String> hurufA = nama.stream()
    .filter(n -> n.startsWith("A"))
    .collect(Collectors.toList());
System.out.println(hurufA);   // [Andi]
```

---

## 7. 🔎 Regular Expression (Regex) — Ekspresi Reguler

### 🇮🇩 Bahasa Indonesia
**Regular Expression** (Regex) adalah ekspresi berupa pola teks yang digunakan untuk mencari, mencocokkan, atau memvalidasi string. Sangat berguna untuk validasi input seperti email, nomor telepon, atau password.

### 🇯🇵 日本語
**正規表現**（Regular Expression / Regex）はテキストパターンを表す式で、文字列の検索・照合・検証に使われます。メールアドレス、電話番号、パスワードなどの入力検証に非常に役立ちます。

```java
import java.util.regex.*;

// ── Pola dasar / 基本パターン ──────────────────────────────
// \d     = angka (digit) / 数字
// \w     = kata (huruf, angka, _) / 単語文字
// \s     = spasi / 空白
// .      = karakter apapun / 任意の文字
// *      = 0 atau lebih / 0回以上
// +      = 1 atau lebih / 1回以上
// ?      = 0 atau 1 / 0回か1回
// {n}    = tepat n kali / ちょうどn回
// ^      = awal string / 文字列の先頭
// $      = akhir string / 文字列の末尾
// [abc]  = salah satu dari a, b, c / a、b、cのいずれか

// ── Contoh penggunaan / 使用例 ─────────────────────────────

// 1. Cek apakah string cocok dengan pola / パターン一致チェック
String email = "budi@example.com";
boolean valid = email.matches("^[\\w.-]+@[\\w.-]+\\.[a-z]{2,}$");
System.out.println(valid);   // true

// 2. Validasi nomor telepon / 電話番号の検証
String telepon = "08123456789";
boolean validTelepon = telepon.matches("^0[0-9]{9,12}$");
System.out.println(validTelepon);   // true

// 3. Cari pola dalam string / 文字列内でパターンを検索
String teks = "Harga: Rp 50000 dan Rp 75000";
Pattern p = Pattern.compile("\\d+");
Matcher m = p.matcher(teks);

while (m.find()) {
    System.out.println("Ditemukan: " + m.group());
}
// Ditemukan: 50000
// Ditemukan: 75000

// 4. Ganti pola / パターンを置換
String hasil = teks.replaceAll("\\d+", "***");
System.out.println(hasil);   // Harga: Rp *** dan Rp ***

// 5. Split berdasarkan pola / パターンで分割
String data = "nama,umur,kota";
String[] parts = data.split(",");
for (String s : parts) System.out.println(s);
// nama
// umur
// kota
```

| Pola | 🇮🇩 Arti | 🇯🇵 意味 | Contoh Match |
|------|---------|---------|--------------|
| `\d` | Satu digit angka | 1つの数字 | `0`–`9` |
| `\w` | Huruf, angka, atau `_` | 英数字またはアンダースコア | `a`–`z`, `0`–`9`, `_` |
| `\s` | Spasi / whitespace | 空白文字 | ` `, `\t`, `\n` |
| `.` | Karakter apapun | 任意の1文字 | `a`, `5`, `@` |
| `+` | 1 atau lebih | 1回以上 | `\d+` → `123` |
| `*` | 0 atau lebih | 0回以上 | `\d*` → `` atau `123` |
| `?` | Opsional (0 atau 1) | 省略可能 | `colou?r` → `color` atau `colour` |
| `^` | Awal string | 文字列の先頭 | `^Hello` |
| `$` | Akhir string | 文字列の末尾 | `world$` |

---

## 8. 🔢 Bitwise Expression — Ekspresi Bitwise

### 🇮🇩 Bahasa Indonesia
**Bitwise Expression** adalah ekspresi yang melakukan operasi langsung pada **bit** dari suatu nilai biner. Sering digunakan dalam pemrograman sistem, enkripsi, dan optimasi performa.

### 🇯🇵 日本語
**ビット演算式**（Bitwise Expression）は2進数値の**ビット**に対して直接演算を行う式です。システムプログラミング・暗号化・パフォーマンス最適化でよく使われます。

```java
int a = 5;    // biner: 0101 / 2進数: 0101
int b = 3;    // biner: 0011 / 2進数: 0011

System.out.println(a & b);    // 1  — AND  | 0101 & 0011 = 0001
System.out.println(a | b);    // 7  — OR   | 0101 | 0011 = 0111
System.out.println(a ^ b);    // 6  — XOR  | 0101 ^ 0011 = 0110
System.out.println(~a);       // -6 — NOT  | ~0101 = 1111...1010
System.out.println(a << 1);   // 10 — Left Shift  | 0101 → 1010
System.out.println(a >> 1);   // 2  — Right Shift | 0101 → 0010

// Contoh praktis: cek bilangan genap/ganjil / 偶数・奇数チェック
int angka = 7;
if ((angka & 1) == 0) {
    System.out.println("Genap / 偶数");
} else {
    System.out.println("Ganjil / 奇数");   // → Ganjil
}
```

| Operator | 🇮🇩 Nama | 🇯🇵 名前 | Contoh | Hasil |
|----------|---------|---------|--------|-------|
| `&` | AND bitwise | ビットAND | `5 & 3` | `1` |
| `\|` | OR bitwise | ビットOR | `5 \| 3` | `7` |
| `^` | XOR bitwise | ビットXOR | `5 ^ 3` | `6` |
| `~` | NOT bitwise (komplemen) | ビット反転 | `~5` | `-6` |
| `<<` | Geser kiri | 左シフト | `5 << 1` | `10` |
| `>>` | Geser kanan | 右シフト | `5 >> 1` | `2` |

---

## 9. 🔄 Cast Expression — Ekspresi Cast

### 🇮🇩 Bahasa Indonesia
**Cast Expression** adalah ekspresi yang mengubah suatu nilai dari satu tipe data ke tipe data lain. Ada dua jenis: **widening** (otomatis, aman) dan **narrowing** (manual, bisa kehilangan data).

### 🇯🇵 日本語
**キャスト式**（Cast Expression）はある値を一つのデータ型から別のデータ型に変換する式です。**拡大変換**（自動・安全）と**縮小変換**（手動・データ損失の可能性あり）の2種類があります。

```java
// ── Widening Cast (otomatis / 自動) ───────────────────────
// int → long → float → double
int i = 100;
long l = i;        // otomatis / 自動変換
float f = i;       // otomatis / 自動変換
double d = i;      // otomatis / 自動変換

System.out.println(l);   // 100
System.out.println(f);   // 100.0
System.out.println(d);   // 100.0

// ── Narrowing Cast (manual / 手動) ────────────────────────
// double → float → long → int → short → byte
double pi = 3.14159;
int piInt = (int) pi;        // desimal dipotong / 小数部分が切り捨て
System.out.println(piInt);   // 3 (bukan 3.14!)

float piFloat = (float) pi;
System.out.println(piFloat); // 3.14159

// ── Cast pada Object (Upcasting & Downcasting) ────────────
// アップキャストとダウンキャスト
class Hewan { void suara() { System.out.println("..."); } }
class Kucing extends Hewan {
    void suara() { System.out.println("Meow!"); }
    void cakarKuku() { System.out.println("Mencakar!"); }
}

Hewan h = new Kucing();     // Upcasting — otomatis / 自動
h.suara();                  // Meow! (polymorphism)

Kucing k = (Kucing) h;      // Downcasting — manual / 手動
k.cakarKuku();              // Mencakar!

// ── String conversion / 文字列変換 ────────────────────────
int angka = 42;
String str = String.valueOf(angka);   // int → String
int balik  = Integer.parseInt(str);   // String → int
double dbl = Double.parseDouble("3.14");  // String → double
```

| Jenis Cast | 🇮🇩 Keterangan | 🇯🇵 説明 | Contoh |
|------------|---------------|---------|--------|
| **Widening** | Otomatis, tidak ada risiko kehilangan data | 自動変換、データ損失なし | `int → double` |
| **Narrowing** | Manual `(tipe)`, bisa kehilangan presisi/data | 手動変換、精度損失の可能性 | `double → int` |
| **Upcasting** | Child → Parent, otomatis | 子→親クラス、自動 | `Kucing → Hewan` |
| **Downcasting** | Parent → Child, manual & berisiko | 親→子クラス、手動、注意が必要 | `Hewan → Kucing` |

---

## 10. 🏗️ Object Creation Expression — Ekspresi Pembuatan Objek

### 🇮🇩 Bahasa Indonesia
**Object Creation Expression** adalah ekspresi yang membuat *instance* (objek) baru dari sebuah class menggunakan keyword `new`. Operator `new` mengalokasikan memori di *heap* dan memanggil *constructor* dari class tersebut.

### 🇯🇵 日本語
**オブジェクト生成式**（Object Creation Expression）は `new` キーワードを使ってクラスから新しい*インスタンス*（オブジェクト）を作成する式です。`new` 演算子は*ヒープ*にメモリを確保し、クラスの*コンストラクタ*を呼び出します。

```java
// ── Sintaks dasar / 基本構文 ───────────────────────────────
// NamaClass namaVariabel = new NamaClass(argumen);
// クラス名 変数名 = new クラス名(引数);

class Mahasiswa {
    String nama;
    int nim;

    // Constructor
    Mahasiswa(String nama, int nim) {
        this.nama = nama;
        this.nim  = nim;
    }

    void tampil() {
        System.out.println("Nama: " + nama + ", NIM: " + nim);
    }
}

// Buat objek / オブジェクトの生成
Mahasiswa mhs1 = new Mahasiswa("Andi", 12345);
Mahasiswa mhs2 = new Mahasiswa("Budi", 67890);

mhs1.tampil();   // Nama: Andi, NIM: 12345
mhs2.tampil();   // Nama: Budi, NIM: 67890

// ── Object creation untuk class bawaan Java / Javaの組み込みクラス ──
String str   = new String("Halo");         // String
ArrayList<String> list = new ArrayList<>(); // ArrayList
HashMap<String, Integer> map = new HashMap<>(); // HashMap
Scanner sc   = new Scanner(System.in);     // Scanner

// ── Anonymous Object / 匿名オブジェクト ────────────────────
new Mahasiswa("Citra", 11111).tampil();    // langsung pakai tanpa variabel
// Nama: Citra, NIM: 11111

// ── Array Object / 配列オブジェクト ───────────────────────
int[] angka     = new int[5];             // array int ukuran 5
String[] bulan  = new String[12];         // array String ukuran 12
Mahasiswa[] mhs = new Mahasiswa[3];       // array objek Mahasiswa
```

---

## 📊 Ringkasan / まとめ

| # | Expression | 🇮🇩 Singkat | 🇯🇵 一言まとめ | Hasil |
|---|-----------|------------|--------------|-------|
| 1 | **Arithmetic** | Operasi matematika | 数学演算 | Angka |
| 2 | **Logical** | Operasi logika AND/OR/NOT | 論理演算 | `true`/`false` |
| 3 | **Relational** | Bandingkan dua nilai | 2値を比較 | `true`/`false` |
| 4 | **Assignment** | Beri nilai ke variabel | 変数に値を代入 | Nilai tersimpan |
| 5 | **Conditional / Ternary** | Pilih satu dari dua nilai | 2値から1つ選択 | Salah satu nilai |
| 6 | **Lambda** | Fungsi ringkas tanpa nama | 無名関数を簡潔に定義 | Fungsi / Function |
| 7 | **Regular Expression** | Pola pencarian teks | テキストのパターン検索 | Match/No match |
| 8 | **Bitwise** | Operasi langsung pada bit | ビット演算 | Nilai biner |
| 9 | **Cast** | Konversi tipe data | データ型変換 | Nilai tipe baru |
| 10 | **Object Creation** | Buat objek baru dengan `new` | `new`でオブジェクト生成 | Instance / Objek |

---

> 📚 **Referensi / 参考資料:**
> - [Oracle Java Documentation](https://docs.oracle.com/en/java/)
> - [W3Schools Java](https://www.w3schools.com/java/)
> - [GeeksforGeeks — Java Expressions](https://www.geeksforgeeks.org/java/)
> - [Regex101 — Regex Tester](https://regex101.com)