# DNS & Domain Name System Security

> **Zero2Root** | Networking Fundamentals Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Kurose & Ross, *Computer Networking*; Stallings, *Network Security Essentials*; Benvenuti, *Understanding Linux Network Internals*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-041` | **Phase 2:** Networking
> **Est. study:** 4h | **Level:** Intermediate
> **Prerequisites:** LC-039
> **Book map:** Kurose & Ross, Computer Networking Ch.2; Stallings, Network Security Essentials Ch.8
<!-- LC-CURRICULUM-END -->

## Table of contents

1. What DNS is, and the name tree
2. How a lookup actually happens
3. Record types you'll meet
4. DNSSEC: proving an answer is genuine
5. DNS privacy: DoT and DoH
6. Zone transfer: a configuration risk
7. Cache poisoning, and how it's prevented
8. Security notes
9. Cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| DNS | The Internet's "phone book": it turns names like `example.com` into IP addresses |
| Resolver | The service that does lookups for you (usually your ISP's or a public one) |
| Authoritative server | The server that holds the real answers for a given domain |
| Record (RR) | One entry in DNS: a name plus a value (an address, a mail server, and so on) |
| Zone | One domain's set of records, managed as a unit |
| TTL | How long an answer may be cached before it must be looked up again |
| Cache | A saved copy of recent answers, so the same lookup is instant next time |
| DNSSEC | Digital signatures on DNS answers, so you can tell a forged one apart |
| DoT / DoH | DNS sent over an encrypted connection (over TLS, or over HTTPS) |

---

## 1. What DNS Is, and the Name Tree

Computers talk in IP addresses, but people remember names. **DNS** (Domain Name System) is the service that translates one into the other: you type `example.com`, DNS gives back `93.184.216.34`. It's the Internet's phone book.

Names are organized as an upside-down tree, read **right to left**, starting from the root:

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www            →  full name: www.example.com.
```

| Level | Example | Who runs it |
|:---|:---|:---|
| Root | `.` | The root servers |
| TLD (top-level domain) | `com`, `id`, `jp` | A registry |
| Domain / zone | `example.com` | An organization |
| Host | `www`, `mail` | A machine inside the domain |

No single server knows the whole tree. Each level **delegates** the next one downward ("ask the `.com` servers, they'll point you to `example.com`'s servers"). That delegation is what makes DNS scale to the whole Internet.

---

## 2. How a Lookup Actually Happens

Three players are involved:

| Player | Role |
|:---|:---|
| Stub resolver | The tiny client inside your OS; it just asks the resolver |
| Recursive resolver | Does the legwork, and remembers (caches) answers |
| Authoritative server | Holds the real records for a domain |

When the resolver doesn't already have the answer cached, it walks the tree from the top:

```text
1. ask a root server          → "I don't know, but ask the .com servers"
2. ask a .com server          → "ask example.com's servers"
3. ask example.com's server   → "www.example.com is 93.184.216.34"  ✓
```

```
You ──► Recursive resolver ──► Root
                │                │  "ask .com"
                ├──► .com ───────┘
                │     │  "ask example.com"
                └──► example.com ──► Answer
                │
        caches the answer for its TTL, so next time is instant
```

Every record has a **TTL** that says how long it can be cached. Caching is what keeps DNS fast; without it, every click would walk the whole tree again.

A note on hygiene: a **recursive** resolver (walks the tree for clients) and an **authoritative** server (answers for a domain) are different jobs. A public authoritative server should not also do open recursion, because that becomes an abuse and amplification magnet.

---

## 3. Record Types You'll Meet

| Type | What it holds | Example |
|:---|:---|:---|
| A | An IPv4 address | `93.184.216.34` |
| AAAA | An IPv6 address | `2606:2800:...` |
| CNAME | An alias ("this name is really that name") | `www → origin.cdn.net.` |
| MX | Where email for the domain goes | `10 mail.example.com.` |
| NS | Which servers are authoritative for the zone | `ns1.example.com.` |
| TXT | Free text (used for SPF, domain verification) | `"v=spf1 ..."` |
| PTR | The reverse: an IP back to a name | used in reverse lookups |
| DNSKEY / RRSIG / DS | DNSSEC keys and signatures (Section 4) | key / signature data |

DNS normally travels over UDP port 53 (small and fast); large answers fall back to TCP port 53.

---

## 4. DNSSEC: Proving an Answer Is Genuine

Plain DNS has a weakness: when an answer arrives, there's no built-in way to know it really came from the right place and wasn't swapped out along the way. **DNSSEC** fixes this by adding **digital signatures** (the signature idea comes from LC-055).

Each zone signs its records. A resolver that validates can check the signature and be sure the answer is authentic and unmodified:

```text
check:  Verify(zone's public key, the records, the signature) → genuine / forged
```

The trust is chained from the root downward, like certificate chains in PKI (LC-057): the root vouches for `.com`, `.com` vouches for `example.com`, and so on. A resolver only needs to trust the root to trust the whole chain.

```
root (trusted starting point)
  │ vouches for
  ▼
.com
  │ vouches for
  ▼
example.com  ──signs──►  its own records
```

Important: DNSSEC proves answers are **genuine**, but it does **not** hide them. The questions and answers still travel in the clear. For privacy, you need DoT or DoH (next section).

---

## 5. DNS Privacy: DoT and DoH

Classic DNS is sent in plaintext, so anyone on the path can see every name you look up, and potentially tamper with it. Two mechanisms encrypt it:

| Mechanism | How | Port |
|:---|:---|:---|
| Classic DNS | Plaintext | UDP/TCP 53 |
| DoT (DNS over TLS) | DNS wrapped in a TLS connection | TCP 853 |
| DoH (DNS over HTTPS) | DNS carried over HTTPS, so it blends in with web traffic | TCP 443 |

The benefit is stopping passive snooping and on-path tampering with your lookups. There's a trade-off, though: whichever resolver you use (including a big DoH provider) still sees your queries, so choose one whose privacy policy you trust. Many organizations deliberately force internal resolvers and block ad-hoc DoH so that their security logging keeps working. The best combination is encrypted transport (DoT/DoH) **plus** a resolver that validates DNSSEC.

---

## 6. Zone Transfer: A Configuration Risk

A **zone transfer** (AXFR) is a legitimate feature: it lets a backup DNS server copy the full list of records from the main one. The problem is when it's left open to anyone.

If a stranger can request a zone transfer, they can download your **entire** list of internal hostnames at once: servers, naming scheme, the lot. That's a goldmine for reconnaissance, handed over without any real attack.

How to keep your own zone safe:

- Allow zone transfers only to your known backup servers, by IP.
- Protect the transfer with **TSIG** (a shared secret that both servers check).
- Don't rely on secret hostnames for security; keep applying segmentation and least privilege.

> This lesson is about recognizing and fixing the misconfiguration, not performing it. Watch your authoritative-server logs for unexpected transfer attempts.

---

## 7. Cache Poisoning, and How It's Prevented

**The idea:** a resolver caches whatever answer it accepts. If an attacker can slip a **forged** answer in before the real one arrives, and make it look valid, the resolver caches the wrong address and hands it to everyone for as long as the TTL lasts. That sends victims to the attacker's server while the address bar still shows the real name.

For the forgery to be accepted, it has to match the resolver's question and a couple of random values. Historically those random values were too small to be safe. The modern defenses all work by making a forged answer far harder to fake or easier to detect:

| Defense | What it does |
|:---|:---|
| Random source port + random query ID | Hugely increases what an attacker has to guess |
| DNS cookies | A shared token that rejects cheap off-path spoofing |
| DNSSEC validation | A forged answer fails the signature check and is thrown out |
| Encrypted transport (DoT/DoH) | Keeps an on-path attacker from reading or injecting |

Warning signs worth noticing: an address that suddenly changes with no legitimate update, a spike in resolution failures, or a resolver's answer disagreeing with another trusted one. The real protection is defense in depth: randomness to make guessing hard, **plus** DNSSEC to make forgery detectable.

---

## 8. Security Notes

| Issue | Risk | Defense / detection |
|:---|:---|:---|
| Plaintext DNS | Snooping and on-path tampering | DoT/DoH, a trusted resolver |
| Non-validating resolver | Forged answers go unnoticed | Turn on DNSSEC validation |
| Open recursive resolver | Abuse and amplification | Restrict clients; keep recursive and authoritative separate |
| Open zone transfer | Your whole zone gets dumped | Restrict by IP + TSIG; alert on logs |
| Rogue resolver pushed by DHCP | Your lookups get redirected | DHCP snooping, RA Guard, a DoH policy |

Lab hygiene: only test resolvers and zones you own. When an answer looks wrong, compare a `dig +dnssec` result against a second trusted public resolver.

---

## 9. Cheatsheet

```bash
# ── Basic lookups ────────────────────────────────────────────
dig example.com A +short       # just the IPv4 address
dig example.com AAAA           # IPv6
dig MX example.com             # mail servers
dig NS example.com             # authoritative name servers

# ── See the whole walk from the root ─────────────────────────
dig +trace example.com

# ── DNSSEC inspection ────────────────────────────────────────
dig example.com A +dnssec      # show signatures (RRSIG)
delv example.com A             # validating lookup, if configured

# ── Reverse lookup ───────────────────────────────────────────
dig -x 93.184.216.34

# ── Your own system resolver ─────────────────────────────────
resolvectl status
resolvectl query example.com
```

| Command | Use |
|:---|:---|
| `dig +short` | Terse answer |
| `dig +dnssec` | Show the DNSSEC signatures |
| `dig +trace` | Watch the lookup walk down from the root |
| `resolvectl` | Inspect the system's own resolver |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/`
> - RFC 1034/1035 (DNS), RFC 4033-4035 (DNSSEC), RFC 7858 (DoT), RFC 8484 (DoH), RFC 7873 (Cookies)
> - `man dig`, `man resolvectl`

> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Educational material and labs on systems or zones you own or are authorized to test. No attack procedures included.
