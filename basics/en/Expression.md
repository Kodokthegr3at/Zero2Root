# Expression: Syntax, Types, and Evaluation

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-001` | **Phase 0:** Foundations
> **Est. study:** 2-3h | **Level:** Beginner
> **Prerequisites:** -
> **Book map:** K. N. King, C Programming Ch.2-5; Friedl, Mastering Regular Expressions Ch.1-4; Sweigart, Automate the Boring Stuff Ch.1-6
<!-- LC-CURRICULUM-END -->

## Table of Contents

1. What an expression is
2. Arithmetic expressions
3. Logical (boolean) expressions
4. Relational (comparison) expressions
5. Assignment expressions
6. Conditional (ternary) expressions
7. Lambda expressions
8. Regular expressions (RegEx)
9. Bitwise expressions
10. Cast expressions
11. Object creation expressions
12. Security notes
13. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Expression | Any piece of code that produces a value, like `2 + 2` or `x > 5` |
| Operator | A symbol that does something: `+`, `&&`, `==`, `<<` |
| Operand | The value an operator works on (in `2 + 3`, the operands are 2 and 3) |
| Precedence | The order operators run in (`*` before `+`, like in school math) |
| Boolean | A value that is only ever `true` or `false` |
| Short-circuit | Stopping a logical check early once the answer is already known |
| Overflow | When a number grows too big for its type and wraps around |
| Cast | Converting a value from one type to another |
| RegEx | A pattern language for matching text |

---

## 1. What an Expression Is

An **expression** is any piece of code that works out to a single value. `2 + 2` is an expression (it produces `4`). So is `age > 18` (it produces `true` or `false`), and so is `"admin".toUpperCase()`.

Expressions are built from **operands** (the values) and **operators** (the symbols that combine them). This lesson walks through the main families of operators, the order they run in, and the security bugs that creep in when expressions are evaluated carelessly, especially on untrusted input.

---

## 2. Arithmetic Expressions

An **arithmetic expression** produces a number using the familiar math operators: add (`+`), subtract (`-`), multiply (`*`), divide (`/`), and remainder (`%`).

The order follows ordinary school math (BODMAS/PEMDAS): `*`, `/`, `%` run before `+` and `-`, and parentheses `()` override everything. Operators of the same level run left to right.

> **Watch out for integer overflow.** Every integer type has a maximum. A 32-bit signed `int` tops out at 2,147,483,647; add one more and it wraps around to a large negative number. In C, this is a classic reason a program allocates a buffer that's too small, which leads to memory bugs.

```java
// ── Java ─────────────────────────────────────────────────────
int a = 10, b = 3;
int sum        = a + b;          // 13
int difference = a - b;          // 7
int product    = a * b;          // 30
int quotient   = a / b;          // 3    (integer division drops the fraction)
int remainder  = a % b;          // 1    (the "left over" after dividing)
```

```c
/* ── C: splitting seconds into h:m:s with / and % ──────────── */
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

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Add | `10 + 3` | `13` |
| `-` | Subtract | `10 - 3` | `7` |
| `*` | Multiply | `10 * 3` | `30` |
| `/` | Divide | `10 / 3` | `3` (integer) |
| `%` | Remainder | `10 % 3` | `1` |

---

## 3. Logical (Boolean) Expressions

A **logical expression** combines true/false values into a single true/false answer, using AND (`&&`), OR (`||`), and NOT (`!`).

Most languages are **short-circuit**: they stop as soon as the answer is certain. In `A && B`, if `A` is already `false`, `B` is never checked. This is not just an optimization; it's a safety tool. The classic use is checking something isn't empty *before* using it:

```java
// If username is null, username.length() is never reached (no crash)
if (username != null && username.length() > 3) {
    System.out.println("Valid user format");
}

boolean isAuthenticated = true;
boolean hasAdminRole    = false;
boolean canAccessAdmin  = isAuthenticated && hasAdminRole;  // false (needs both)
boolean canViewPublic   = isAuthenticated || hasAdminRole;  // true  (needs either)
boolean isGuest         = !isAuthenticated;                 // false (the opposite)
```

| Operator | Name | True when… |
|----------|------|------------|
| `&&` | AND | both sides are true |
| `\|\|` | OR | at least one side is true |
| `!` | NOT | flips true to false and back |

---

## 4. Relational (Comparison) Expressions

A **relational expression** compares two values and gives back a boolean. These are `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`.

> **Security angle — type juggling.** Some languages let you compare values of different types loosely. PHP's `==` and JavaScript's `==` will quietly convert types before comparing, which has caused real authentication bypasses (for example, two different strings both being treated as "equal to zero"). The fix is **strict** comparison: PHP/JS `===`, or typed comparisons that don't coerce. Never compare password hashes with loose `==`.

```c
int user_uid = 1000;
int root_uid = 0;
int is_root     = (user_uid == root_uid);   /* 0 (false) */
int is_standard = (user_uid >= 1000);       /* 1 (true)  */
```

| Operator | Meaning | Example → result |
|----------|---------|------------------|
| `==` | Equal | `10 == 10` → true |
| `!=` | Not equal | `10 != 20` → true |
| `>` `<` | Greater / less than | `15 > 10` → true |
| `>=` `<=` | Greater / less or equal | `10 >= 10` → true |

---

## 5. Assignment Expressions

An **assignment** stores a value into a variable with `=`. Compound forms combine an operation with the assignment: `x += 5` means `x = x + 5`.

Assignment is **right-associative**: `x = y = z = 10` runs right to left, so `z` gets 10 first, then `y`, then `x`.

```java
int counter = 0;
counter += 5;   // 5   (counter = counter + 5)
counter *= 2;   // 10
counter -= 3;   // 7

// ++ and -- change a variable by one. Where they sit matters:
int a = 5;
int b = ++a;    // "pre": a becomes 6 first, then b = 6
int c = a++;    // "post": c = 6 first, then a becomes 7
```

---

## 6. Conditional (Ternary) Expressions

The **ternary operator** is a compact `if-else` that produces a value. It reads as "condition ? value-if-true : value-if-false".

```python
user_role = "admin"
access_level = 100 if user_role == "admin" else 10   # Python's form
```

```c
int port = 443;
const char *protocol = (port == 443) ? "HTTPS (encrypted)" : "HTTP (cleartext)";
```

Use it for short either/or choices. For anything with several branches, a normal `if-else` stays more readable.

---

## 7. Lambda Expressions

A **lambda** is a small, nameless function you can pass around like a value. Java 8+, Python (`lambda`), C++ (`[]{}`), and JavaScript (`() => {}`) all have them. They shine for filtering and transforming lists, which comes up constantly in log analysis.

```python
# Keep only the failed requests (HTTP status 400 and up)
logs = [
    {"ip": "192.168.1.10", "status": 200},
    {"ip": "10.0.0.5",     "status": 404},
    {"ip": "172.16.0.4",   "status": 401},
]
failed = list(filter(lambda e: e["status"] >= 400, logs))
```

```java
// Keep only endpoints that look sensitive, then upper-case them
List<String> sensitive = endpoints.stream()
    .filter(ep -> ep.contains("admin") || ep.contains("config"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```

---

## 8. Regular Expressions (RegEx)

A **regular expression** is a pattern for matching text. It's used for input validation, searching logs, and writing detection signatures (Snort, Suricata, YARA).

```bash
# Find IPv4 addresses in a log
grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# Find things shaped like an MD5 hash (32 hex characters)
grep -E -i '\b[a-f0-9]{32}\b' hashes.txt

# Find things shaped like an AWS access key
grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| Piece | Means |
|-------|-------------|
| `^` / `$` | Start / end of the text |
| `.` | Any single character |
| `\d` / `\w` / `\s` | A digit / a word character / whitespace |
| `*` / `+` / `?` | Zero-or-more / one-or-more / optional |
| `{n,m}` | Between n and m times |
| `[...]` | Any one character from the set |
| `(A\|B)` | A or B |

> **ReDoS risk:** a badly written pattern with nested repeats (like `(a+)+$`) can take exponential time on certain inputs, freezing the program. An attacker can trigger that on purpose. Keep patterns simple, set match timeouts, or use a linear-time engine.

---

## 9. Bitwise Expressions

A **bitwise expression** works on the individual 1s and 0s of a number. It shows up in cryptography, subnet math, Unix permissions, and reverse engineering.

The operators: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), left shift (`<<`), right shift (`>>`).

```c
/* XOR is reversible: applying the same key twice gives the original back */
char original  = 'A';              /* 01000001 */
char key       = 0x5A;             /* 01011010 */
char encrypted = original ^ key;   /* 00011011 */
char decrypted = encrypted ^ key;  /* 01000001 → 'A' again */

/* Unix permissions as bits: read=4, write=2, execute=1 */
int rwx = (1 << 2) | (1 << 1) | (1 << 0);  /* 4 | 2 | 1 = 7 (rwx) */
int can_execute = (rwx & 1);               /* test the execute bit */
```

| Operator | Name | Example (`a=5` `0101`, `b=3` `0011`) | Result |
|----------|------|-------------------------------------|--------|
| `&` | AND | `0101 & 0011` → `0001` | `1` |
| `\|` | OR | `0101 \| 0011` → `0111` | `7` |
| `^` | XOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | NOT | flips every bit | `-6` |
| `<<` | Left shift | `0101 << 1` → `1010` (×2) | `10` |
| `>>` | Right shift | `0101 >> 1` → `0010` (÷2) | `2` |

---

## 10. Cast Expressions

A **cast** converts a value from one type to another. Two kinds:

- **Widening (safe):** small type → bigger type, like `int` → `double`. Nothing is lost; the language does it for you.
- **Narrowing (risky):** big type → smaller type, like `double` → `int`, or a 32-bit `int` → an 8-bit `char`. You must ask for it explicitly, and data can be **truncated**.

```c
int large = 300;
/* 300 doesn't fit in 8 bits. Only the lowest 8 bits survive: 300 → 44 */
unsigned char truncated = (unsigned char)large;   /* 44, not 300 */
```

That silent truncation is a real security bug source: a length check passes on the big value, but the small truncated value is what actually gets used.

---

## 11. Object Creation Expressions

An **object creation expression** builds a new object in memory, usually with `new`, which runs the object's constructor.

```java
TargetHost target = new TargetHost("192.168.1.1", 443);
target.scan();
```

In managed languages (Java, Python, C#) the memory is cleaned up for you. In C/C++, memory you allocate (`new` / `malloc`) must be freed (`delete` / `free`) exactly once, or you get leaks (freeing never) or use-after-free bugs (using it after freeing).

---

## 12. Security Notes

Expressions turn into vulnerabilities when untrusted input gets evaluated as code or used without checks. The theme: treat input as data, never as instructions.

| Risk | What goes wrong | Defense |
|:---|:---|:---|
| Expression-language injection (SpEL/OGNL) | User text is evaluated as a server-side expression | Never evaluate user input as an expression; allowlist templates |
| ReDoS | A crafted string makes a regex run for ages | Simple patterns, match timeouts, linear-time engines |
| Type juggling | Loose `==` treats unlike values as equal | Strict equality (`===` / typed compares), especially for secrets |
| Integer overflow (C) | A size wraps around and a buffer is under-allocated | Check before allocating; `-fsanitize=undefined,integer` |
| Shell `eval` / `$((...))` on input | Input becomes a command | Don't `eval` raw input; quote; use real parsers |

---

## 13. Cheatsheet

| Category | Operators | Produces |
|----------|-----------|----------|
| Arithmetic | `+ - * / %` | a number |
| Logical | `&& \|\| !` | true/false (short-circuit) |
| Relational | `== != < > <= >=` | true/false |
| Assignment | `= += -= *= /=` | stores a value |
| Ternary | `cond ? a : b` | one of two values |
| Lambda | `(x) -> ...` | a function |
| RegEx | `^ $ \d \w .*` | a text match |
| Bitwise | `& \| ^ ~ << >>` | bit-level result |
| Cast | `(type) value` | a converted value |
| Object | `new Class()` | a new object |

---

> **References and Book Sources:**
> - K. N. King, *C Programming: A Modern Approach (2nd Edition)* (`~/Documents/Books/Programming/C /`)
> - Al Sweigart, *Automate the Boring Stuff with Python (2nd Edition)* (`~/Documents/Books/Programming/Python/`)
> - Jeffrey E.F. Friedl, *Mastering Regular Expressions (3rd Edition)* (`~/Documents/Books/CyberSec/Linux/`)
> - Dafydd Stuttard & Marcus Pinto, *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - Scott Meyers, *Effective Modern C++* (`~/Documents/Books/Programming/ C++/`)

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
