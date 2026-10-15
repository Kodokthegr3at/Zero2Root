# Ekspresi: Sintaks, Tipe, dan Evaluasi

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-001` | **Fase 0:** Fondasi
> **Estimasi belajar:** 2-3 jam | **Level:** Pemula
> **Prasyarat:** -
> **Peta buku:** K. N. King, C Programming Ch.2-5; Friedl, Mastering Regular Expressions Ch.1-4; Sweigart, Automate the Boring Stuff Ch.1-6
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik | Deskripsi |
|---|-------|-----------|
| 1 | Ekspresi Aritmetika | Operasi matematika dan aritmetika |
| 2 | Ekspresi Logika | Logika boolean (AND, OR, NOT) |
| 3 | Ekspresi Relasional | Perbandingan nilai (==, !=, <, >) |
| 4 | Ekspresi Penugasan | Penugasan dan compound operator |
| 5 | Ekspresi Kondisional (Ternary) | Ekspresi kondisional tiga operand |
| 6 | Ekspresi Lambda | Fungsi anonim ringkas |
| 7 | Regular Expression (RegEx) | Pencocokan pola string |
| 8 | Ekspresi Bitwise | Operasi level bit dan manipulasi biner |
| 9 | Ekspresi Cast | Konversi tipe data (widening/narrowing) |
| 10 | Ekspresi Pembuatan Objek | Alokasi memori dan pembuatan objek |
| 11 | Catatan Keamanan | Risiko dan pertahanan ekspresi |
| 12 | Ringkasan dan Cheatsheet | Tabel ringkasan dan cheatsheet cepat |

---

## 1. Ekspresi Aritmetika

**Ekspresi aritmetika** adalah ekspresi yang menghasilkan nilai numerik melalui operasi matematika dasar seperti penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), pembagian (`/`), dan sisa bagi atau modulo (`%`).

Dalam pemrograman sistem (C/C++) dan bahasa modern (Java, Python), urutan evaluasi mengikuti aturan presedensi operator (BODMAS/PEMDAS). Operasi perkalian, pembagian, dan modulo dievaluasi lebih dulu sebelum penjumlahan dan pengurangan, kecuali diatur eksplisit menggunakan tanda kurung `()`.

Secara formal (K. N. King), ekspresi aritmetika bilangan bulat dapat ditulis:

```text
E  ::=  number | ( E ) | E + E | E - E | E * E | E / E | E % E
```

Artinya: sebuah ekspresi bisa berupa angka, ekspresi di dalam tanda kurung, atau dua ekspresi yang digabung dengan `+`, `-`, `*`, `/`, atau `%`.

Operator dengan level yang sama dievaluasi dari kiri ke kanan, dan `*`, `/`, `%` selalu didahulukan sebelum `+` dan `-`.

Integer overflow terjadi kalau hasil perhitungan terlalu besar (atau terlalu kecil) untuk tipenya. `int` 32-bit signed hanya bisa menampung -2.147.483.648 sampai 2.147.483.647; lewat satu langkah dari batas atas, nilainya berputar balik. Di C, ini sering jadi penyebab buffer dialokasikan terlalu kecil.

```java
// ── Contoh Java ─────────────────────────────────────────────
int a = 10;
int b = 3;

int penjumlahan  = a + b;           // 13   — Penjumlahan
int pengurangan  = a - b;           // 7    — Pengurangan
int perkalian    = a * b;           // 30   — Perkalian
int pembagian    = a / b;           // 3    — Pembagian bilangan bulat
int sisa_bagi    = a % b;           // 1    — Sisa bagi (Modulo)
double pangkat   = Math.pow(a, 2); // 100.0 — Pangkat
```

```c
/* ── Contoh C (K. N. King - C Programming Standard) ────────── */
#include <stdio.h>

int main(void) {
    int total_seconds = 3665;
    int hours   = total_seconds / 3600;       /* 1 jam */
    int minutes = (total_seconds % 3600) / 60; /* 1 menit */
    int seconds = total_seconds % 60;         /* 5 detik */
    
    printf("Time: %02d:%02d:%02d\n", hours, minutes, seconds);
    return 0;
}
```

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `+` | Penjumlahan | `10 + 3` | `13` |
| `-` | Pengurangan | `10 - 3` | `7` |
| `*` | Perkalian | `10 * 3` | `30` |
| `/` | Pembagian | `10 / 3` | `3` (integer) |
| `%` | Modulo (sisa bagi) | `10 % 3` | `1` |

---

## 2. Ekspresi Logika (Boolean)

**Ekspresi logika** adalah ekspresi yang mengevaluasi kondisi ke nilai boolean (`true` atau `false`) menggunakan operator logika `&&` (Logical AND), `||` (Logical OR), dan `!` (Logical NOT).

Bahasa pemrograman modern menggunakan short-circuit evaluation:
- Pada operasi `A && B`, jika `A` bernilai `false`, maka `B` tidak akan dievaluasi karena hasilnya pasti `false`.
- Pada operasi `A || B`, jika `A` bernilai `true`, maka `B` tidak akan dievaluasi karena hasilnya pasti `true`.

```java
// ── Contoh short-circuit evaluation ────────────────────────
String username = getUsername();
// Jika username null, username.length() TIDAK PERNAH dipanggil (menghindari NullPointerException)
if (username != null && username.length() > 3) {
    System.out.println("Valid user format");
}

// ── Operasi logika ───────────────────────────────────────
boolean isAuthenticated = true;
boolean hasAdminRole    = false;

boolean canAccessDashboard = isAuthenticated && hasAdminRole; // false
boolean canViewPublicPage  = isAuthenticated || hasAdminRole; // true
boolean isGuest            = !isAuthenticated;                // false
```

| Operator | Nama | Perilaku |
|----------|------|----------|
| `&&` | DAN (Logical AND) | Mengembalikan `true` hanya jika kedua operand `true` |
| `\|\|` | ATAU (Logical OR) | Mengembalikan `true` jika minimal satu operand `true` |
| `!` | TIDAK (Logical NOT) | Membalik nilai boolean (`true` → `false`, `false` → `true`) |

---

## 3. Ekspresi Relasional

**Ekspresi relasional** membandingkan dua operand menggunakan operator relasional seperti sama dengan (`==`), tidak sama dengan (`!=`), lebih besar (`>`), lebih kecil (`<`), lebih besar atau sama (`>=`), dan lebih kecil atau sama (`<=`). Hasil evaluasinya selalu bertipe boolean.

Dalam cybersecurity, perbandingan relasional yang salah penanganan (seperti loose comparison di PHP atau type coercion di JavaScript) sering menjadi akar celah autentikasi (Type Juggling).

```c
/* ── Ekspresi relasional di C / sistem Linux ────────────── */
#include <stdio.h>

int main(void) {
    int user_uid = 1000;
    int root_uid = 0;
    
    int is_root = (user_uid == root_uid);       /* hasil 0 (false) */
    int is_non_root = (user_uid >= 1000);      /* hasil 1 (true)  */
    
    printf("Is Root: %d | Is Standard User: %d\n", is_root, is_non_root);
    return 0;
}
```

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `10 == 10` | `true` |
| `!=` | Tidak sama dengan | `10 != 20` | `true` |
| `>` | Lebih besar dari | `15 > 10` | `true` |
| `<` | Lebih kecil dari | `5 < 10` | `true` |
| `>=` | Lebih besar atau sama | `10 >= 10` | `true` |
| `<=` | Lebih kecil atau sama | `9 <= 10` | `true` |

---

## 4. Ekspresi Penugasan

**Ekspresi penugasan** menetapkan nilai sisi kanan (R-value) ke variabel atau lokasi memori sisi kiri (L-value). Selain penugasan dasar (`=`), bahasa modern menyediakan compound assignment operator seperti `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`.

Operator penugasan bersifat right-associative, artinya `x = y = z = 10` akan mengevaluasi `z = 10` lebih dulu, lalu `y = z`, dan akhirnya `x = y`.

```java
// ── Compound assignment & pre/post increment ──────────────
int counter = 0;

counter += 5;    // counter = counter + 5  → 5
counter *= 2;    // counter = counter * 2  → 10
counter -= 3;    // counter = counter - 3  → 7
counter %= 4;    // counter = counter % 4  → 3

// Evaluasi prefix vs postfix
int a = 5;
int b = ++a;     // Prefix: a menjadi 6, lalu b diisi 6
int c = a++;     // Postfix: c diisi 6, lalu a menjadi 7
```

---

## 5. Ekspresi Kondisional (Ternary)

**Ekspresi kondisional** (sering disebut ternary operator karena membutuhkan tiga operand) adalah bentuk ringkas dari struktur kendali `if-else` yang mengevaluasi dan mengembalikan salah satu dari dua ekspresi berdasarkan kondisi boolean.

Sintaks: `condition ? expression_if_true : expression_if_false;`

```python
# ── Ternary inline di Python ─────────────────────────────────
user_role = "admin"
access_level = 100 if user_role == "admin" else 10
print(f"Access Level: {access_level}")
```

```c
/* ── Ekspresi ternary di C ───────────────────────────────────── */
#include <stdio.h>

int main(void) {
    int port = 443;
    const char *protocol = (port == 443) ? "HTTPS (Encrypted)" : "HTTP (Cleartext)";
    printf("Port %d runs %s\n", port, protocol);
    return 0;
}
```

---

## 6. Ekspresi Lambda

**Ekspresi lambda** adalah blok kode anonim (fungsi tanpa nama) yang dapat diteruskan sebagai argumen ke metode atau disimpan dalam variabel. Diperkenalkan pada Java 8, Python (`lambda`), C++11 (`[](){}`), dan C# modern.

Dalam analisis keamanan dan pemrosesan log, lambda sangat efisien untuk memfilter paket jaringan, parsing log web server, dan transformasi data cepat.

```python
# ── Lambda Python untuk analisis log ────────────────────────────
logs = [
    {"ip": "192.168.1.10", "status": 200, "path": "/index.html"},
    {"ip": "10.0.0.5",     "status": 404, "path": "/admin.php"},
    {"ip": "172.16.0.4",   "status": 401, "path": "/login"},
    {"ip": "10.0.0.5",     "status": 500, "path": "/api/v1/debug"}
]

# Filter request gagal (status >= 400) memakai lambda
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

## 7. Regular Expression (RegEx)

**Regular Expression (RegEx)** adalah ekspresi formal yang mendefinisikan pola pencarian teks. Digunakan untuk validasi data, ekstraksi string, pencarian log forensik (SIEM/grep), dan pembentukan aturan deteksi (Suricata/Snort/YARA).

Referensi mendalam: *Mastering Regular Expressions (3rd Edition)* oleh Jeffrey E.F. Friedl (`~/Documents/Books/Linux/`).

```bash
# ── Contoh regex cybersecurity umum dengan grep ────────────

# Mencocokkan alamat IPv4 valid
$ grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# Mencocokkan hash MD5 (32 karakter hex)
$ grep -E -i '\b[a-f0-9]{32}\b' sample_hashes.txt

# Mencocokkan AWS Access Key ID sensitif
$ grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| Metacharacter | Deskripsi |
|---------------|-----------|
| `^` / `$` | Awal / akhir string |
| `.` | Karakter apa saja (kecuali newline) |
| `\d` / `\D` | Digit angka (0-9) / non-digit |
| `\w` / `\W` | Alfanumerik + `_` / non-word |
| `\s` / `\S` | Whitespace (spasi, tab) / non-space |
| `*` / `+` / `?` | 0+, 1+, atau 0-1 kemunculan |
| `{n,m}` | Antara n hingga m kali |
| `[...]` | Character class (salah satu karakter) |
| `(A\|B)` | Alternasi (pilihan A atau B) |

---

## 8. Ekspresi Bitwise

**Ekspresi bitwise** memanipulasi bit biner secara langsung pada tipe data integer. Digunakan secara luas dalam kriptografi (XOR cipher, hashing), sistem jaringan (subnet masking), permission sistem file Unix, dan analisis malware/shellcode.

Operasi bitwise meliputi AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), left shift (`<<`), dan right shift (`>>`).

```c
/* ── Enkripsi XOR bitwise & permission masking di C ───────── */
#include <stdio.h>

int main(void) {
    /* 1. Obfuskasi XOR sederhana (Key: 0x5A) */
    char original = 'A';              /* Binary: 01000001 */
    char key = 0x5A;                  /* Binary: 01011010 */
    
    char encrypted = original ^ key;  /* Binary: 00011011 */
    char decrypted = encrypted ^ key; /* Binary: 01000001 ('A') */
    
    printf("Original: %c | Encrypted: 0x%X | Decrypted: %c\n", original, (unsigned char)encrypted, decrypted);
    
    /* 2. Permission file Linux (Read=4, Write=2, Execute=1) */
    int rwx = (1 << 2) | (1 << 1) | (1 << 0); /* 4 | 2 | 1 = 7 */
    int is_executable = (rwx & 1);             /* Cek bit execute */
    printf("Permission Octal: %d | Executable: %s\n", rwx, is_executable ? "YES" : "NO");
    
    return 0;
}
```

| Operator | Nama | Operasi bit (`a=5 [0101]`, `b=3 [0011]`) | Hasil |
|----------|------|-------------------------------------------|-------|
| `&` | Bitwise AND | `0101 & 0011` → `0001` | `1` |
| `\|` | Bitwise OR | `0101 \| 0011` → `0111` | `7` |
| `^` | Bitwise XOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | Bitwise NOT | `~0101` → `...11111010` | `-6` (2's comp) |
| `<<` | Left Shift | `0101 << 1` → `1010` (kali 2) | `10` |
| `>>` | Right Shift | `0101 >> 1` → `0010` (bagi 2) | `2` |

---

## 9. Ekspresi Cast

**Ekspresi cast** mengonversi ekspresi dari satu tipe data ke tipe data lain. Dibagi menjadi dua kategori utama:

1. **Widening cast (implicit)**: konversi dari tipe data lebih kecil ke lebih besar (misal `int` ke `double`). Aman dan dilakukan otomatis oleh kompilator tanpa risiko kehilangan presisi.
2. **Narrowing cast (explicit)**: konversi dari tipe data lebih besar ke lebih kecil (misal `double` ke `int`, atau `int` ke `short`). Membutuhkan casting manual `(tipe)nilai` dan berisiko memotong data (data truncation) atau overflow.

```c
/* ── Contoh kerentanan integer truncation di C ─────────── */
#include <stdio.h>

int main(void) {
    int large_number = 300;
    /* 300 dalam biner (16-bit): 0000 0001 0010 1100 */
    /* Cast ke unsigned char 8-bit mengambil 8 bit terendah: 0010 1100 = 44 */
    unsigned char truncated = (unsigned char)large_number;
    
    printf("Original: %d | Truncated: %d\n", large_number, truncated);
    return 0;
}
```

---

## 10. Ekspresi Pembuatan Objek

**Ekspresi pembuatan objek** mengalokasikan memori di area heap dan menginisialisasi objek baru menggunakan kata kunci `new` serta memanggil konstruktor terkait. Di bahasa tanpa garbage collection otomatis seperti C++, alokasi dinamis dilakukan dengan `new`/`malloc` dan wajib dibebaskan dengan `delete`/`free` untuk mencegah memory leak.

```java
// ── Instansiasi objek Java ────────────────────────────────
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
        // Ekspresi pembuatan objek
        TargetHost target = new TargetHost("192.168.1.1", 443);
        target.scan();
    }
}
```

---

## 11. Catatan Keamanan: Risiko dan Pertahanan Ekspresi

Pemahaman evaluasi ekspresi penting untuk audit dan hardening. Input tidak tepercaya yang dievaluasi sebagai kode sering memicu kerentanan. Fokus di bawah adalah deteksi dan mitigasi.

1. **Expression Language (EL) / OGNL Injection**: jangan evaluasi ekspresi dari input pengguna. Gunakan allowlist template, matikan evaluasi dinamis (SpEL/OGNL) pada data request, dan sandbox interpreter jika wajib ada.
2. **ReDoS**: hindari nested quantifier yang catastrophic, tetapkan timeout atau pakai engine linear-time, dan uji pola dengan fuzzer string panjang (*Mastering Regular Expressions* / WAHH).
3. **Type Juggling**: pakai perbandingan ketat (`===` atau typed compare), validasi tipe di boundary API, dan jangan bandingkan hash string dengan `==`.
4. **Integer overflow (C)**: gunakan tipe lebar cukup, cek sebelum alokasi (`size_t` overflow check), aktifkan sanitizer (`-fsanitize=undefined,integer`), dan ikuti disiplin K. N. King untuk batas tipe.
5. **Bash / eval surfaces**: jangan `eval` atau `$((...))` atas input mentah, quote variabel, dan utamakan parser terstruktur.

Checklist pertahanan: jangan `eval` input tidak tepercaya, pakai strict equality, batasi kompleksitas regex, pakai checked arithmetic, terapkan aturan WAF/SAST untuk SpEL/OGNL, dan buat unit test untuk nilai batas: 0, serta nilai terbesar dan terkecil dari tipenya.

---

## 12. Ringkasan dan Cheatsheet

| Kategori | Operator / Sintaks | Deskripsi |
|----------|---------------------|-----------|
| Aritmetika | `+`, `-`, `*`, `/`, `%` | Operasi matematika dasar |
| Logika | `&&`, `\|\|`, `!` | Operasi logika boolean dengan short-circuit |
| Relasional | `==`, `!=`, `<`, `>`, `<=`, `>=` | Perbandingan nilai |
| Penugasan | `=`, `+=`, `-=`, `*=`, `/=` | Penugasan nilai ke memori |
| Ternary | `cond ? val1 : val2` | Kondisional inline ringkas |
| Lambda | `(param) -> { body }` | Fungsi anonim tanpa nama |
| RegEx | `^`, `$`, `\d`, `\w`, `.*` | Pencocokan pola string |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | Operasi langsung pada bit |
| Cast | `(type) value` | Konversi tipe data |
| Object | `new ClassName()` | Alokasi heap dan instansiasi |

---

> **Referensi dan sumber buku:**
> - K. N. King, *C Programming: A Modern Approach (2nd Edition)* (`~/Documents/Books/Programming/C /`)
> - Al Sweigart, *Automate the Boring Stuff with Python (2nd Edition)* (`~/Documents/Books/Programming/Python/`)
> - Jeffrey E.F. Friedl, *Mastering Regular Expressions (3rd Edition)* (`~/Documents/Books/CyberSec/Linux/`)
> - Dafydd Stuttard & Marcus Pinto, *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - Scott Meyers, *Effective Modern C++* (`~/Documents/Books/Programming/ C++/`)

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
