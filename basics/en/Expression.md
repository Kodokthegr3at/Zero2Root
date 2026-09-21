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

| # | Topic | Description |
|---|-------|-------------|
| 1 | Arithmetic Expression | Mathematical and arithmetic operations |
| 2 | Logical Expression | Boolean logic (AND, OR, NOT) |
| 3 | Relational Expression | Value comparison (==, !=, <, >) |
| 4 | Assignment Expression | Assignment and compound operators |
| 5 | Conditional (Ternary) | Three-operand conditional expression |
| 6 | Lambda Expression | Concise anonymous functions |
| 7 | Regular Expression (RegEx) | String pattern matching |
| 8 | Bitwise Expression | Bit-level operations and binary manipulation |
| 9 | Cast Expression | Data type conversion (widening/narrowing) |
| 10 | Object Creation Expression | Memory allocation and object instantiation |
| 11 | Security Note | Expression risks and defensive controls |
| 12 | Summary and Cheatsheet | Summary table and quick cheatsheet |

---

## 1. Arithmetic Expression

An **Arithmetic Expression** evaluates to a numeric value through standard mathematical operations: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and remainder or modulo (`%`).

In system programming (C/C++) and modern languages (Java, Python), the evaluation order follows operator precedence (BODMAS/PEMDAS). Multiplication, division, and modulo take precedence over addition and subtraction, unless explicitly grouped using parentheses `()`.

Formally (per K. N. King), integer arithmetic expressions can be described by the grammar:

$$
E ::= n \mid (E) \mid E \;+\; E \mid E \;-\; E \mid E \;\times\; E \mid E \;/\; E \mid E \bmod E
$$

evaluated left-associatively with precedence \(\times,/,\% \;>\; +,-\). Integer overflow on a \(w\)-bit type occurs when a result leaves \(\bigl[-2^{w-1},\,2^{w-1}-1\bigr]\) (signed) or \(\bigl[0,\,2^{w}-1\bigr]\) (unsigned), a common root cause of undersized buffer allocations in C.

```java
// ── Java Example ─────────────────────────────────────────────
int a = 10;
int b = 3;

int sum        = a + b;           // 13   — Addition
int difference = a - b;           // 7    — Subtraction
int product    = a * b;           // 30   — Multiplication
int quotient   = a / b;           // 3    — Integer division
int remainder  = a % b;           // 1    — Modulo (remainder)
double power   = Math.pow(a, 2); // 100.0 — Power
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

| Operator | Function | Example | Result |
|----------|----------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3` (integer) |
| `%` | Modulo (remainder) | `10 % 3` | `1` |

---

## 2. Logical (Boolean) Expression

A **Logical Expression** evaluates conditions into a boolean value (`true` or `false`) using the logical operators `&&` (Logical AND), `||` (Logical OR), and `!` (Logical NOT).

Modern programming languages implement short-circuit evaluation:
- In `A && B`, if `A` evaluates to `false`, `B` is not evaluated because the entire expression is guaranteed to be `false`.
- In `A || B`, if `A` evaluates to `true`, `B` is not evaluated because the entire expression is guaranteed to be `true`.

```java
// ── Short-circuit evaluation example ────────────────────────
String username = getUsername();
// If username is null, username.length() is never called (avoids NullPointerException)
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

| Operator | Name | Behavior |
|----------|------|----------|
| `&&` | Logical AND | Returns `true` only if both operands are `true` |
| `\|\|` | Logical OR | Returns `true` if at least one operand is `true` |
| `!` | Logical NOT | Inverts the boolean state (`true` to `false`, `false` to `true`) |

---

## 3. Relational Expression

A **Relational Expression** compares two operands using relational operators: equality (`==`), inequality (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`). The result is always a boolean value.

In cybersecurity, improperly handled relational comparisons (such as PHP loose comparison `==` vs. strict `===`, or JavaScript type coercion) frequently introduce authentication bypass vulnerabilities known as type juggling.

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

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `10 == 10` | `true` |
| `!=` | Not equal to | `10 != 20` | `true` |
| `>` | Greater than | `15 > 10` | `true` |
| `<` | Less than | `5 < 10` | `true` |
| `>=` | Greater than or equal | `10 >= 10` | `true` |
| `<=` | Less than or equal | `9 <= 10` | `true` |

---

## 4. Assignment Expression

An **Assignment Expression** assigns the value of the right-hand operand (R-value) to the left-hand storage location or variable (L-value). Besides basic assignment (`=`), modern languages support compound assignment operators such as `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`.

Assignment operators are right-associative: an expression like `x = y = z = 10` evaluates `z = 10` first, then assigns the result to `y`, and finally to `x`.

```java
// ── Compound Assignments & Pre/Post Increments ──────────────
int counter = 0;

counter += 5;    // counter = counter + 5  → 5
counter *= 2;    // counter = counter * 2  → 10
counter -= 3;    // counter = counter - 3  → 7
counter %= 4;    // counter = counter % 4  → 3

// Prefix vs postfix evaluation
int a = 5;
int b = ++a;     // Prefix: a becomes 6, then b is assigned 6
int c = a++;     // Postfix: c is assigned 6, then a becomes 7
```

---

## 5. Conditional (Ternary) Expression

A **Conditional Expression** (commonly called the ternary operator because it takes three operands) is a concise inline alternative to an `if-else` control structure. It evaluates and returns one of two expressions based on a boolean condition.

Syntax: `condition ? expression_if_true : expression_if_false;`

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

## 6. Lambda Expression

A **Lambda Expression** is an anonymous function (a function without a declared name) that can be passed as an argument to a higher-order function or assigned to a variable. Supported across modern languages: Java 8+, Python (`lambda`), C++11 lambdas, and JavaScript arrow functions (`() => {}`).

In security telemetry and log analysis, lambdas offer a concise way to filter network packet streams, parse server access logs, and transform events in real time.

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

## 7. Regular Expression (RegEx)

A **Regular Expression (RegEx)** is a formal sequence of characters defining a search pattern. It is used for input validation, string tokenization, forensic log searching (SIEM/grep), and intrusion detection signatures (Suricata/Snort/YARA).

Reference: *Mastering Regular Expressions (3rd Edition)* by Jeffrey E.F. Friedl (`~/Documents/Books/Linux/`).

```bash
# ── Common Cybersecurity Regex Examples with grep ────────────

# Match valid IPv4 addresses
$ grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log

# Match MD5 hashes (32 hex characters)
$ grep -E -i '\b[a-f0-9]{32}\b' sample_hashes.txt

# Match sensitive AWS Access Key IDs
$ grep -E 'AKIA[0-9A-Z]{16}' source_code.py
```

| Metacharacter | Description |
|---------------|-------------|
| `^` / `$` | Start / end of string |
| `.` | Any character (except newline) |
| `\d` / `\D` | Digit (0-9) / non-digit |
| `\w` / `\W` | Word char (a-z, 0-9, _) / non-word |
| `\s` / `\S` | Whitespace / non-whitespace |
| `*` / `+` / `?` | Quantifiers: 0+, 1+, or 0-1 occurrences |
| `{n,m}` | Between n and m times |
| `[...]` | Character class set |
| `(A\|B)` | Alternation (matches A or B) |

---

## 8. Bitwise Expression

A **Bitwise Expression** directly manipulates individual binary bits of integer data types. It is used in cryptography (XOR ciphers, SHA/AES hashing rounds), network subnet calculation, Unix permission masking, and malware reverse engineering / shellcode decoding.

Core operators: AND (`&`), OR (`|`), XOR (`^`), bitwise NOT (`~`), left shift (`<<`), and right shift (`>>`).

```c
/* ── Bitwise XOR Encryption & Permission Masking in C ───────── */
#include <stdio.h>

int main(void) {
    /* 1. Simple XOR obfuscation (key: 0x5A) */
    char original = 'A';              /* Binary: 01000001 */
    char key = 0x5A;                  /* Binary: 01011010 */
    
    char encrypted = original ^ key;  /* Binary: 00011011 */
    char decrypted = encrypted ^ key; /* Binary: 01000001 ('A') */
    
    printf("Original: %c | Encrypted: 0x%X | Decrypted: %c\n", original, (unsigned char)encrypted, decrypted);
    
    /* 2. Linux file permissions (Read=4, Write=2, Execute=1) */
    int rwx = (1 << 2) | (1 << 1) | (1 << 0); /* 4 | 2 | 1 = 7 */
    int is_executable = (rwx & 1);             /* Check execute bit */
    printf("Permission Octal: %d | Executable: %s\n", rwx, is_executable ? "YES" : "NO");
    
    return 0;
}
```

| Operator | Name | Bit Operation (`a=5 [0101]`, `b=3 [0011]`) | Result |
|----------|------|---------------------------------------------|--------|
| `&` | Bitwise AND | `0101 & 0011` → `0001` | `1` |
| `\|` | Bitwise OR | `0101 \| 0011` → `0111` | `7` |
| `^` | Bitwise XOR | `0101 ^ 0011` → `0110` | `6` |
| `~` | Bitwise NOT | `~0101` → `...11111010` | `-6` (2's comp) |
| `<<` | Left Shift | `0101 << 1` → `1010` (multiply by 2) | `10` |
| `>>` | Right Shift | `0101 >> 1` → `0010` (divide by 2) | `2` |

---

## 9. Cast Expression

A **Cast Expression** converts an evaluated expression from one data type to another, in two core forms:

1. **Widening cast (implicit)**: converts a smaller data type to a larger one (e.g., `int` to `double`). Safe, and performed automatically by the compiler without data loss.
2. **Narrowing cast (explicit)**: converts a larger data type into a smaller one (e.g., `double` to `int`, or 32-bit `int` to 8-bit `char`). Requires explicit syntax `(type)value` and carries the risk of truncation or integer overflow.

```c
/* ── Integer Truncation Vulnerability Example in C ─────────── */
#include <stdio.h>

int main(void) {
    int large_number = 300;
    /* 300 in binary (16-bit): 0000 0001 0010 1100 */
    /* Cast to 8-bit unsigned char takes the lowest 8 bits: 0010 1100 = 44 */
    unsigned char truncated = (unsigned char)large_number;
    
    printf("Original: %d | Truncated: %d\n", large_number, truncated);
    return 0;
}
```

---

## 10. Object Creation Expression

An **Object Creation Expression** allocates memory on the heap and initializes a new object instance using the `new` keyword, invoking its constructor. In unmanaged languages like C++, dynamically allocated memory (`new`/`malloc`) must be explicitly released (`delete`/`free`) to avoid memory leaks or use-after-free bugs.

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

## 11. Security Note: Expression Risks and Defensive Controls

Understanding expression evaluation matters for audit and hardening. Untrusted input evaluated as code is a common source of critical bugs. The focus below is detection and mitigation.

1. **Expression Language (EL) / OGNL Injection**: never evaluate user-supplied expressions. Disable dynamic SpEL/OGNL evaluation on request data, allowlist templates, and sandbox the interpreter only if it is unavoidable.
2. **ReDoS**: avoid catastrophic nested quantifiers, enforce match timeouts or use linear-time engines, and fuzz with long adversarial strings (*Mastering Regular Expressions* / WAHH).
3. **Type Juggling**: prefer strict equality (`===` or typed comparisons), validate types at API boundaries, and never compare password hashes with loose `==`.
4. **Integer Overflow (C)**: widen types, check before allocation (`size_t` overflow checks), enable `-fsanitize=undefined,integer`, and follow K. N. King's type-width discipline.
5. **Shell arithmetic / eval**: do not `eval` or expand `$((...))` on raw input, quote expansions, and prefer structured parsers.

Defense checklist: no `eval` on untrusted input, strict equality, regex complexity budgets, checked arithmetic, SAST/WAF rules for expression languages, and boundary tests for \(0, 2^{w}-1, -2^{w-1}\).

---

## 12. Summary and Cheatsheet

| Category | Operator / Syntax | Description |
|----------|--------------------|--------------|
| Arithmetic | `+`, `-`, `*`, `/`, `%` | Basic arithmetic computation |
| Logical | `&&`, `\|\|`, `!` | Short-circuit boolean logic |
| Relational | `==`, `!=`, `<`, `>`, `<=`, `>=` | Value comparison |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=` | Assign value to variable |
| Ternary | `cond ? val1 : val2` | Inline conditional ternary |
| Lambda | `(param) -> { body }` | Concise anonymous function |
| RegEx | `^`, `$`, `\d`, `\w`, `.*` | String pattern matching |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | Direct binary bit operations |
| Cast | `(type) value` | Type conversion / coercion |
| Object | `new ClassName()` | Heap allocation and constructor call |

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
