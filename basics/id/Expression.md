# Expression: Sintaks, Jenis, dan Evaluasi

> **Zero2Root** | Seri Basics | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-001` | **Fase 0:** Fondasi
> **Estimasi belajar:** 2-3 jam | **Level:** Pemula
> **Prasyarat:** -
> **Peta buku:** K. N. King, C Programming Ch.2-5; Friedl, Mastering Regular Expressions Ch.1-4; Sweigart, Automate the Boring Stuff Ch.1-6
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu expression
2. Expression aritmetika
3. Expression logika (boolean)
4. Expression relasional (perbandingan)
5. Expression assignment
6. Expression conditional (ternary)
7. Expression lambda
8. Regular expression (RegEx)
9. Expression bitwise
10. Expression cast
11. Expression pembuatan objek
12. Catatan keamanan
13. Cheatsheet

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Expression (ekspresi) | Potongan kode apa pun yang menghasilkan sebuah nilai, seperti `2 + 2` atau `x > 5` |
| Operator | Simbol yang melakukan sesuatu: `+`, `&&`, `==`, `<<` |
| Operand | Nilai yang dikerjakan operator (di `2 + 3`, operand-nya 2 dan 3) |
| Precedence (prioritas) | Urutan operator dijalankan (`*` sebelum `+`, seperti matematika sekolah) |
| Boolean | Nilai yang hanya bisa `true` atau `false` |
| Short-circuit | Berhenti mengecek logika lebih awal begitu jawabannya sudah pasti |
| Overflow | Saat angka terlalu besar untuk tipenya lalu berputar balik |
| Cast | Mengubah nilai dari satu tipe ke tipe lain |
| RegEx | Bahasa pola untuk mencocokkan teks |

---

## 1. Apa Itu Expression

**Expression** adalah potongan kode apa pun yang menghasilkan satu nilai. `2 + 2` adalah expression (menghasilkan `4`). Begitu juga `umur > 18` (menghasilkan `true` atau `false`), dan `"admin".toUpperCase()`.

Expression dibangun dari **operand** (nilainya) dan **operator** (simbol yang menggabungkannya). Materi ini menelusuri keluarga operator utama, urutan jalannya, dan bug keamanan yang muncul kalau expression dievaluasi secara ceroboh, terutama pada input yang tidak tepercaya.

---

## 2. Expression Aritmetika

**Expression aritmetika** menghasilkan angka memakai operator matematika yang sudah dikenal: tambah (`+`), kurang (`-`), kali (`*`), bagi (`/`), dan sisa bagi (`%`).

Urutannya mengikuti matematika sekolah (BODMAS/PEMDAS): `*`, `/`, `%` jalan sebelum `+` dan `-`, dan tanda kurung `()` mengalahkan semuanya. Operator dengan level yang sama jalan dari kiri ke kanan.

> **Hati-hati integer overflow.** Tiap tipe integer punya batas maksimum. `int` 32-bit signed berhenti di 2.147.483.647; tambah satu lagi, ia berputar balik ke angka negatif besar. Di C, ini penyebab klasik program mengalokasikan buffer yang terlalu kecil, yang berujung bug memori.

```java
// ── Java ─────────────────────────────────────────────────────
int a = 10, b = 3;
int sum        = a + b;          // 13
int difference = a - b;          // 7
int product    = a * b;          // 30
int quotient   = a / b;          // 3    (pembagian integer membuang pecahan)
int remainder  = a % b;          // 1    (sisa setelah dibagi)
```

```c
/* ── C: memecah detik menjadi j:m:d dengan / dan % ─────────── */
#include <stdio.h>
int main(void) {
    int total_seconds = 3665;
    int hours   = total_seconds / 3600;        /* 1 */
    int minutes = (total_seconds % 3600) / 60; /* 1 */
    int seconds = total_seconds % 60;          /* 5 */
    printf("Time: %02d:%02d:%02d\n", hours, minutes, seconds);
    return 0;
}
```

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `+` | Tambah | `10 + 3` | `13` |
| `-` | Kurang | `10 - 3` | `7` |
| `*` | Kali | `10 * 3` | `30` |
| `/` | Bagi | `10 / 3` | `3` (integer) |
| `%` | Sisa bagi | `10 % 3` | `1` |

---

## 3. Expression Logika (Boolean)

**Expression logika** menggabungkan nilai true/false menjadi satu jawaban true/false, memakai AND (`&&`), OR (`||`), dan NOT (`!`).

Kebanyakan bahasa bersifat **short-circuit**: mereka berhenti begitu jawabannya pasti. Di `A && B`, kalau `A` sudah `false`, `B` tidak pernah dicek. Ini bukan sekadar optimasi; ini alat keamanan. Pemakaian klasiknya adalah mengecek sesuatu tidak kosong *sebelum* memakainya:

```java
// Kalau username null, username.length() tidak pernah dijangkau (tidak crash)
if (username != null && username.length() > 3) {
    System.out.println("Valid user format");
}

boolean isAuthenticated = true;
boolean hasAdminRole    = false;
boolean canAccessAdmin  = isAuthenticated && hasAdminRole;  // false (butuh keduanya)
boolean canViewPublic   = isAuthenticated || hasAdminRole;  // true  (butuh salah satu)
boolean isGuest         = !isAuthenticated;                 // false (kebalikannya)
```

| Operator | Nama | True kalau… |
|----------|------|-------------|
| `&&` | AND | kedua sisi true |
| `\|\|` | OR | minimal satu sisi true |
| `!` | NOT | membalik true jadi false dan sebaliknya |

---

## 4. Expression Relasional (Perbandingan)

**Expression relasional** membandingkan dua nilai dan mengembalikan boolean. Ini adalah `==` (sama), `!=` (tidak sama), `>`, `<`, `>=`, `<=`.

> **Sisi keamanan — type juggling.** Beberapa bahasa membolehkan membandingkan nilai dengan tipe berbeda secara longgar. `==` di PHP dan `==` di JavaScript diam-diam mengonversi tipe sebelum membandingkan, dan itu pernah menyebabkan authentication bypass sungguhan (misalnya, dua string berbeda sama-sama dianggap "sama dengan nol"). Solusinya adalah perbandingan **strict**: `===` di PHP/JS, atau perbandingan bertipe yang tidak mengonversi. Jangan pernah membandingkan hash password dengan `==` longgar.

```c
int user_uid = 1000;
int root_uid = 0;
int is_root     = (user_uid == root_uid);   /* 0 (false) */
int is_standard = (user_uid >= 1000);       /* 1 (true)  */
```

| Operator | Arti | Contoh → hasil |
|----------|------|----------------|
| `==` | Sama | `10 == 10` → true |
| `!=` | Tidak sama | `10 != 20` → true |
| `>` `<` | Lebih besar / kecil | `15 > 10` → true |
| `>=` `<=` | Lebih besar / kecil atau sama | `10 >= 10` → true |

---

## 5. Expression Assignment

**Assignment** menyimpan sebuah nilai ke variabel dengan `=`. Bentuk gabungannya menggabungkan operasi dengan assignment: `x += 5` artinya `x = x + 5`.

Assignment bersifat **right-associative**: `x = y = z = 10` jalan dari kanan ke kiri, jadi `z` dapat 10 dulu, lalu `y`, lalu `x`.

```java
int counter = 0;
counter += 5;   // 5   (counter = counter + 5)
counter *= 2;   // 10
counter -= 3;   // 7

// ++ dan -- mengubah variabel sebanyak satu. Posisinya penting:
int a = 5;
int b = ++a;    // "pre": a jadi 6 dulu, lalu b = 6
int c = a++;    // "post": c = 6 dulu, lalu a jadi 7
```

---

## 6. Expression Conditional (Ternary)

**Operator ternary** adalah `if-else` ringkas yang menghasilkan sebuah nilai. Dibaca sebagai "kondisi ? nilai-kalau-true : nilai-kalau-false".

```python
user_role = "admin"
access_level = 100 if user_role == "admin" else 10   # bentuk Python
```

```c
int port = 443;
const char *protocol = (port == 443) ? "HTTPS (terenkripsi)" : "HTTP (cleartext)";
```

Pakai untuk pilihan singkat salah satu dari dua. Untuk yang punya banyak cabang, `if-else` biasa tetap lebih mudah dibaca.

---

## 7. Expression Lambda

**Lambda** adalah fungsi kecil tanpa nama yang bisa kamu oper seperti sebuah nilai. Java 8+, Python (`lambda`), C++ (`[]{}`), dan JavaScript (`() => {}`) semuanya punya. Lambda bersinar untuk memfilter dan mengubah list, yang terus-menerus muncul di analisis log.

```python
# Simpan hanya request yang gagal (status HTTP 400 ke atas)
logs = [
    {"ip": "192.168.1.10", "status": 200},
    {"ip": "10.0.0.5",     "status": 404},
    {"ip": "172.16.0.4",   "status": 401},
]
failed = list(filter(lambda e: e["status"] >= 400, logs))
```

```java
// Simpan hanya endpoint yang terlihat sensitif, lalu jadikan huruf besar
List<String> sensitive = endpoints.stream()
    .filter(ep -> ep.contains("admin") || ep.contains("config"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```

---

## 8. Regular Expression (RegEx)

**Regular expression** adalah pola untuk mencocokkan teks. Dipakai untuk validasi input, mencari di log, dan menulis signature deteksi (Snort, Suricata, YARA).

```bash
# Cari alamat IPv4 di sebuah log
grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# Cari yang berbentuk hash MD5 (32 karakter hex)
grep -E -i '\b[a-f0-9]{32}\b' hashes.txt

# Cari yang berbentuk AWS access key
grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| Bagian | Artinya |
|--------|---------|
| `^` / `$` | Awal / akhir teks |
| `.` | Satu karakter apa saja |
| `\d` / `\w` / `\s` | Satu digit / karakter kata / spasi |
| `*` / `+` / `?` | Nol-atau-lebih / satu-atau-lebih / opsional |
| `{n,m}` | Antara n dan m kali |
| `[...]` | Satu karakter mana saja dari set |
| `(A\|B)` | A atau B |

> **Risiko ReDoS:** pola yang ditulis buruk dengan pengulangan bersarang (seperti `(a+)+$`) bisa memakan waktu eksponensial pada input tertentu, membekukan program. Penyerang bisa memicunya dengan sengaja. Jaga pola tetap sederhana, pasang timeout pencocokan, atau pakai engine waktu-linear.

---

## 9. Expression Bitwise

**Expression bitwise** bekerja pada 1 dan 0 individual dari sebuah angka. Muncul di kriptografi, matematika subnet, permission Unix, dan reverse engineering.

Operatornya: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), left shift (`<<`), right shift (`>>`).

```c
/* XOR bisa dibalik: menerapkan kunci yang sama dua kali mengembalikan aslinya */
char original  = 'A';              /* 01000001 */
char key       = 0x5A;             /* 01011010 */
char encrypted = original ^ key;   /* 00011011 */
char decrypted = encrypted ^ key;  /* 01000001 → 'A' lagi */

/* Permission Unix sebagai bit: read=4, write=2, execute=1 */
int rwx = (1 << 2) | (1 << 1) | (1 << 0);  /* 4 | 2 | 1 = 7 (rwx) */
int can_execute = (rwx & 1);               /* tes bit execute */
```

| Operator | Nama | Contoh (`a=5` `0101`, `b=3` `0011`) | Hasil |
|----------|------|-------------------------------------|-------|
| `&` | AND | `0101 & 0011` → `0001` | `1` |
| `\|` | OR | `0101 \| 0011` → `0111` | `7` |
| `^` | XOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | NOT | membalik tiap bit | `-6` |
| `<<` | Left shift | `0101 << 1` → `1010` (×2) | `10` |
| `>>` | Right shift | `0101 >> 1` → `0010` (÷2) | `2` |

---

## 10. Expression Cast

**Cast** mengubah nilai dari satu tipe ke tipe lain. Dua jenis:

- **Widening (aman):** tipe kecil → tipe lebih besar, seperti `int` → `double`. Tidak ada yang hilang; bahasa melakukannya untukmu.
- **Narrowing (berisiko):** tipe besar → tipe lebih kecil, seperti `double` → `int`, atau `int` 32-bit → `char` 8-bit. Kamu harus memintanya secara eksplisit, dan datanya bisa **terpotong (truncated)**.

```c
int large = 300;
/* 300 tidak muat di 8 bit. Hanya 8 bit terendah yang bertahan: 300 → 44 */
unsigned char truncated = (unsigned char)large;   /* 44, bukan 300 */
```

Pemotongan diam-diam itu sumber bug keamanan nyata: pengecekan panjang lolos pada nilai besar, tapi nilai kecil yang terpotong itulah yang sebenarnya dipakai.

---

## 11. Expression Pembuatan Objek

**Expression pembuatan objek** membangun objek baru di memori, biasanya dengan `new`, yang menjalankan konstruktor objek itu.

```java
TargetHost target = new TargetHost("192.168.1.1", 443);
target.scan();
```

Di bahasa yang dikelola (Java, Python, C#) memorinya dibersihkan untukmu. Di C/C++, memori yang kamu alokasikan (`new` / `malloc`) harus dibebaskan (`delete` / `free`) tepat sekali, atau kamu dapat kebocoran (tidak pernah dibebaskan) atau bug use-after-free (memakainya setelah dibebaskan).

---

## 12. Catatan Keamanan

Expression berubah jadi kerentanan saat input tak tepercaya dievaluasi sebagai kode atau dipakai tanpa pengecekan. Temanya: perlakukan input sebagai data, bukan instruksi.

| Risiko | Apa yang salah | Pertahanan |
|:---|:---|:---|
| Injeksi expression language (SpEL/OGNL) | Teks user dievaluasi sebagai expression sisi server | Jangan pernah mengevaluasi input sebagai expression; allowlist template |
| ReDoS | String rancangan membuat regex jalan sangat lama | Pola sederhana, timeout pencocokan, engine waktu-linear |
| Type juggling | `==` longgar menganggap nilai tak sama jadi sama | Equality strict (`===` / perbandingan bertipe), terutama untuk rahasia |
| Integer overflow (C) | Sebuah ukuran berputar balik dan buffer dialokasikan kurang | Cek sebelum mengalokasikan; `-fsanitize=undefined,integer` |
| Shell `eval` / `$((...))` pada input | Input jadi perintah | Jangan `eval` input mentah; quote; pakai parser sungguhan |

---

## 13. Cheatsheet

| Kategori | Operator | Menghasilkan |
|----------|----------|--------------|
| Aritmetika | `+ - * / %` | sebuah angka |
| Logika | `&& \|\| !` | true/false (short-circuit) |
| Relasional | `== != < > <= >=` | true/false |
| Assignment | `= += -= *= /=` | menyimpan nilai |
| Ternary | `cond ? a : b` | salah satu dari dua nilai |
| Lambda | `(x) -> ...` | sebuah fungsi |
| RegEx | `^ $ \d \w .*` | kecocokan teks |
| Bitwise | `& \| ^ ~ << >>` | hasil level bit |
| Cast | `(type) value` | nilai yang dikonversi |
| Objek | `new Class()` | objek baru |

---

> **Referensi dan Sumber Buku:**
> - K. N. King, *C Programming: A Modern Approach (2nd Edition)* (`~/Documents/Books/Programming/C /`)
> - Al Sweigart, *Automate the Boring Stuff with Python (2nd Edition)* (`~/Documents/Books/Programming/Python/`)
> - Jeffrey E.F. Friedl, *Mastering Regular Expressions (3rd Edition)* (`~/Documents/Books/CyberSec/Linux/`)
> - Dafydd Stuttard & Marcus Pinto, *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - Scott Meyers, *Effective Modern C++* (`~/Documents/Books/Programming/ C++/`)

> **Zero2Root** | Seri Basics | kodoktheGr3at | 2026
> **Repositori:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Masukan dan kontribusi diterima.** Buka issue atau PR kalau menemukan kesalahan.
