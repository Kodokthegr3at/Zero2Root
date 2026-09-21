# DNS & Domain Name System Security

> **LearnCybersecurity** | Networking Fundamentals Series
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

1. DNS hierarchy (namespace tree)
2. Resolution algorithm
3. Resource record types
4. DNSSEC (signatures & chain of trust)
5. DNS privacy (DoT & DoH)
6. Zone transfer (misconfiguration risk)
7. Cache poisoning (concept & defenses)
8. Security notes (detection & hardening)
9. Admin cheatsheet

---

## 1. DNS hierarchy: namespace tree

DNS (Domain Name System) maps hierarchical names to resources, most often IP addresses. The namespace is an inverted tree rooted at the root (`.`). Labels are separated by dots, and an FQDN reads right to left:

```
                    .  (root)
                   / \
                 com  org  ...
                /  \
           example  google
              /
           www
```

The full name is `www.example.com.` (the trailing dot marks the root).

| Level | Example | Role |
|:---|:---|:---|
| Root | `.` | Top of the hierarchy, root NS |
| TLD | `com`, `id`, `jp` | Managed by a registry |
| SLD / zone | `example.com` | An organization / authoritative zone |
| Host / label | `www`, `mail` | A resource inside the zone |

Delegation works like this: the parent holds an NS record (plus glue A/AAAA) for the child zone. A zone's authority is really just the set of nameservers that answer with the AA (Authoritative Answer) flag for names inside that zone.

DNS is a distributed hierarchical database. No single server holds the whole tree; authority is delegated downward. Clients usually talk to a recursive resolver, and that resolver walks the tree (or uses its cache) to get an answer.

---

## 2. Resolution algorithm

There are three main roles in the resolution process:

| Role | Behavior |
|:---|:---|
| Stub resolver | Runs in the OS/application, sends queries to the configured recursive resolver |
| Recursive resolver | Does the full lookup on the stub's behalf, and may cache |
| Authoritative server | Only answers for the zones it serves |

The iterative algorithm, intuitively (following Kurose):

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

Caching: the TTL on each RR caps how long it can stay cached. Negative answers get cached too (RFC 2308), under a separate set of rules from positive answers.

Recursion offloads tree-walking from clients. Authoritative servers should typically not recurse for the public internet, since that reduces the amplification/abuse surface. Separating the recursive and authoritative roles is standard operational hygiene: do not casually enable recursion on a public authoritative server.

---

## 3. Resource record types

| Type | Short function | Example data |
|:---|:---|:---|
| A | IPv4 host | `93.184.216.34` |
| AAAA | IPv6 host | `2606:2800:...` |
| NS | Delegation / zone nameserver | `ns1.example.com.` |
| CNAME | Alias to a canonical name | `www → origin.cdn.net.` |
| MX | Mail exchanger plus preference | `10 mail.example.com.` |
| TXT | Free text (SPF, verification, and similar) | `"v=spf1 ..."` |
| SOA | Start of Authority (serial, timers) | zone metadata |
| PTR | Reverse (in-addr.arpa / ip6.arpa) | hostname |
| SRV | Service location | `_sip._tcp...` |
| DNSKEY | Zone public key (DNSSEC) | key material |
| DS | Hash of the child's key, stored at the parent (DNSSEC) | digest |
| RRSIG | Signature over an RRset | signature |
| NSEC / NSEC3 | Proof of non-existence | authenticated denial |

An RRset is the set of all RRs sharing the same name, type, and class. DNSSEC operations sign the whole RRset, not one RR pulled out separately from its siblings.

The classic wire format runs over UDP/53 (large answers fall back to TCP/53 or EDNS0). EDNS0 extends the allowed UDP size and carries extra options, including the DO bit that flags "DNSSEC OK" and cookies.

---

## 4. DNSSEC: signatures & chain of trust

DNSSEC adds authentication and integrity to DNS data, not confidentiality. A validating resolver confirms an answer really came from the right zone and was not altered in transit or in cache.

Core components:

| RR | Role |
|:---|:---|
| DNSKEY | Zone public key (ZSK / KSK) |
| RRSIG | Signature over an RRset |
| DS | Digest of the child's DNSKEY, stored at the parent |
| NSEC/NSEC3 | Proof that a name/type does not exist |

RRSIG verification, conceptually: for RRset $R$ and public key $K$:

$$
\mathsf{Verify}\big(K_{\mathsf{pub}},\; R,\; \mathsf{RRSIG}(R)\big) = \mathsf{accept/reject}
$$

Abstractly, with a $\mathsf{Sign}/\mathsf{Verify}$ signature scheme:

$$
\mathsf{RRSIG}(R) = \mathsf{Sign}_{K_{\mathsf{priv}}}(\mathsf{Hash}(R) \;\|\; \mathsf{meta})
$$

where $\mathsf{meta}$ includes the algorithm, labels, original TTL, inception/expiration, key tag, and signer name.

Chain of trust:

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

A resolver needs a trust anchor, usually at the root. If the DS at the parent matches the child's DNSKEY, and the RRSIG is valid and inside its time window, the RRset is Secure. A validation failure produces Bogus, meaning the answer must not be used. A zone that doesn't use DNSSEC at all is Insecure, which is not the same as Bogus.

DNSSEC stops undetected substitution of forged answers along the path or in cache, provided validators are enabled end to end. It does not encrypt queries; use DoT/DoH for confidentiality of the question itself.

---

## 5. DNS privacy: DoT & DoH

| Mechanism | Port / framing | Properties |
|:---|:---|:---|
| Classic DNS | UDP/TCP 53 | Cleartext question & answer |
| DoT (DNS over TLS) | TCP 853 | DNS wrapped inside TLS |
| DoH (DNS over HTTPS) | TCP 443 | DNS carried over an HTTP(S) API |

The benefit is preventing passive eavesdropping and on-path manipulation of the query/response, which used to travel in cleartext.

There are real operational trade-offs. A centralized resolver, such as a particular DoH vendor, can still see resolution metadata, so pick a privacy policy deliberately. Enterprises often force internal resolvers and block ad hoc DoH so that logging and DLP keep working; document and communicate that choice to users. An ideal combination for a lab or a product is DoT/DoH pointed at a resolver that also validates DNSSEC.

---

## 6. Zone transfer: misconfiguration risk

AXFR (full zone transfer) and IXFR (incremental) let a secondary replicate the primary's zone contents. This is a legitimate operational feature, not an "attack". But if it's allowed from any source without restriction, the entire zone contents, including internal hosts and naming scheme, can be downloaded by an outsider.

Risks from this kind of misconfiguration:

- Exposure of internal name inventory
- Helping reconnaissance before some other attack
- Rogue secondaries appearing if there is no access control, ideally combined with TSIG

Hardening steps for admins of your own zone:

- Restrict AXFR/IXFR to known secondary IPs only
- Use TSIG (an HMAC-based shared secret) between primary and secondary
- Do not rely on "security through obscurity" for hostnames; keep applying segmentation and least privilege

Note: this document has no attack procedure, only configuration awareness and a defensive checklist.

Treat an open zone transfer as a configuration defect. Monitor for unexpected AXFR attempts in authoritative server logs.

---

## 7. Cache poisoning: concept & defenses

Cache poisoning, conceptually, happens when a recursive resolver stores an incorrect name-to-data binding because it accepted a forged answer that looked valid (matching ID/question) before the real answer arrived, or because of weaknesses in transaction prediction.

A high-level threat model (Kaminsky-era intuition): the historical transaction guess-space is too small if

$$
|\mathcal{S}| = 2^{16}\;(\mathsf{TXID}) \times \#\{\text{src ports}\}
$$

is small, and an attacker can flood spoofed answers for a query it triggers itself.

Modern defenses (not an attack cookbook):

| Control | Effect |
|:---|:---|
| Source port randomization | Enlarges the transaction guess-space |
| Random TXID | Mandatory for a long time now, combined with port randomization |
| DNS cookies (RFC 7873) | A client-server token that cuts down cheap spoofing |
| DNSSEC validation | A forged answer fails verification and becomes Bogus |
| 0x20 encoding / QNAME case | Extra entropy on the wire, where supported |
| Network path security | Limits who can inject packets on the resolver's path |

Detection signals: a spike in SERVFAIL on a zone that's normally healthy, an RRset that suddenly changes without any legitimate zone update, or a mismatch against another validating resolver's view.

The right defense is defense in depth: entropy on the query transaction combined with cryptographic authenticity through DNSSEC. Neither one alone is a complete operational story.

---

## 8. Security notes: defense & detection

| Issue | Risk | Defense / detection |
|:---|:---|:---|
| Cleartext DNS | Sniffing / on-path tampering | DoT/DoH, a trusted path |
| Non-validating resolver | Undetected forgery | Enable DNSSEC validation |
| Open recursive | Abuse / amplification | Client ACLs, separate auth from recursive |
| Open AXFR | Zone dump | ACL + TSIG, alert on logs |
| Rogue resolver (via DHCP/RA) | Resolution redirect | DHCP snooping, RA Guard, DoH policy |
| Stale trust anchors | False Bogus / outage | RFC 5011 automation, plus monitoring |

Lab hygiene: only test resolvers and zones you own. When diagnosing a Bogus status, compare a `dig +dnssec` answer against another validating public resolver.

---

## 9. Cheatsheet: legitimate admin / lab

```bash
# ── Basic lookup (your system) ────────────────────────────────
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
delv example.com A          # validating lookup if configured

# ── Reverse / SOA ────────────────────────────────────────────
dig -x 93.184.216.34
dig SOA example.com +noall +answer

# ── Check if YOUR authoritative allows transfer to YOU only ──
# (run from an allowed secondary; expect REFUSED from any other host)
dig AXFR example.com @ns1.example.com

# ── Local stub / systemd-resolved ────────────────────────────
resolvectl status
resolvectl query example.com
```

| Command | Use |
|:---|:---|
| `dig +short` | Terse answer |
| `dig +dnssec` | Show RRSIG / DO |
| `dig +trace` | Simulate the walk from root |
| `delv` | Client-side DNSSEC validation via BIND tools |

---

> **References & book sources**
> - James Kurose & Keith Ross, *Computer Networking: A Top-Down Approach*, `~/Documents/Books/CyberSec/Networking/computernetworking.pdf`
> - William Stallings, *Network Security Essentials (4th Edition)*, `~/Documents/Books/CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf`
> - Christian Benvenuti, *Understanding Linux Network Internals*, `~/Documents/Books/CyberSec/Networking/Understanding Linux Network Internals (2005).pdf`
> - RFC 1034/1035 (DNS), RFC 4033-4035 (DNSSEC), RFC 7858 (DoT), RFC 8484 (DoH), RFC 7873 (Cookies)
> - `man dig`, `man resolvectl`

> **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Educational material and labs on systems or zones you own or are authorized to test. No attack procedures included.
