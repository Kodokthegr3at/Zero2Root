# OSINT: Open Source Intelligence Framework & Techniques

> **Zero2Root** | Intelligence & Reconnaissance Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Bazzell / community handbooks & *Open Source Intelligence Methods and Tools*, `~/Documents/Books/CyberSec/OSINT/`
> Note: legal and public sources only; respect the law, ToS, and investigative ethics.

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-069` | **Phase 7:** Specialized
> **Est. study:** 5h | **Level:** Intermediate
> **Prerequisites:** LC-058
> **Book map:** Akhgar et al., Open Source Intelligence Methods and Tools
<!-- LC-CURRICULUM-END -->

## Table of contents

1. What OSINT is (and is not)
2. The intelligence cycle
3. Planning & direction: good questions
4. Collection disciplines (legal sources)
5. Processing & analysis
6. Geolocation as a verification skill
7. OPSEC for investigators
8. Sock puppets: an ethics warning
9. Legal & ethical bounds
10. Workflow cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| OSINT | Intelligence built from publicly available, lawfully accessible information |
| Collection | Gathering the raw information |
| Analysis | Turning collected data into useful, qualified conclusions |
| Provenance | A record of where each piece of evidence came from |
| PIR | Priority Intelligence Requirement: the specific question you're answering |
| OPSEC | Protecting your own footprint while you research |
| Corroboration | Confirming a claim with two or more independent sources |
| Attribution | Linking activity to a person or group (done carefully) |

---

## 1. What OSINT is (and is not)

Open Source Intelligence (OSINT) is intelligence collected from information that is publicly available and lawfully accessible, then processed into actionable insight.

```text
collect (legal, public sources) → process → analyze → share the results
```

| OSINT | Not OSINT |
|:---|:---|
| News, official sites, filings | Accessing an account without authorization |
| Published metadata | Hacking / phishing to obtain data |
| Public satellite/map imagery | Bypassing a paywall with stolen credentials |
| Public posts | Doxxing / harassment |

OSINT quality depends less on "secret tools" and more on tradecraft: clear questions, source criticism, correlation, and documentation. Tools change; the intelligence cycle does not.

---

## 2. The intelligence cycle

```
        ┌──────────── Direction / Requirements ────────────┐
        │                                                  │
        ▼                                                  │
   Collection ──▶ Processing ──▶ Analysis ──▶ Dissemination ┘
        ▲                         │
        └────── Feedback / gaps ──┘
```

| Phase | Key question | Output |
|:---|:---|:---|
| Direction | What must be answered? Who is the consumer? | PIR (Priority Intelligence Requirements) |
| Collection | Which sources are legal and relevant? | Raw data + provenance |
| Processing | How is it normalized and stored? | Structured dataset |
| Analysis | What is meaningful / still uncertain? | Assessment + confidence |
| Dissemination | How is it reported without overclaiming? | Report / brief |
| Feedback | What is still missing? | New PIRs |

### Confidence language (discipline)

Avoid absolutism. Use a scale:

```text
confidence:  low  /  moderate  /  high
```

Clearly separate observed fact from inference.

---

## 3. Planning & direction: good questions

A weak PIR: "Find everything about X."

A good PIR:

1. Does organization X operate its own ASN / public IP range?
2. Which domains are linked to brand X according to public WHOIS/CT log data?
3. Do any job postings reveal their technology stack (technical OSINT for defensive purposes)?

A good PIR (priority intelligence requirement) can actually be answered, has a deadline, and is tied to a real decision.

Collection plan: sources → methods → legal check → storage → analyst.

---

## 4. Collection disciplines (legal sources)

### 4.1 Source categories

| Category | Examples | Notes |
|:---|:---|:---|
| Official | Regulators, company filings, government portals | High credibility; check for updates |
| Media | News, interviews | May carry bias and errors |
| Technical public | DNS, CT logs, public BGP, public pastes (check ToS) | Watch rate limits; do not abuse |
| Social / UGC | Public posts | Context is easily lost; archive it |
| Imagery | Maps, Street View, public satellite imagery | Mind the ethics for sensitive locations |
| Academic / papers | Proceedings, preprints | Verify the version |

### 4.2 Provenance record (mandatory)

For every artifact, record:

```text
URL  |  time (UTC)  |  hash  |  who collected it  |  which tool  |  notes
```

Without provenance, an analysis is easy to challenge.

### 4.3 Source criticism

- Who is the author? What is their incentive?
- Is this a primary or secondary source?
- Can it be correlated with an independent source?

---

## 5. Processing & analysis

### Processing

- Deduplicate entities (people, organizations, domains, IPs).
- Build a timeline.
- Normalize names (watch for unicode / homoglyphs).
- Tag source reliability.

### Analysis patterns

| Pattern | Description | Risk of error |
|:---|:---|:---|
| Link analysis | Connects entities | False friendship / name collisions |
| Temporal | Sequence of events | Timezone mistakes |
| Geospatial | Maps and shadows / landmarks | Confirmation bias |
| Technical correlation | DNS ↔ certificate ↔ hosting | Shared-hosting noise |

```
Raw captures
    │
    ▼
Structured entities (graph)
    │
    ▼
Hypotheses H1..Hn
    │
    ├─ corroborate
    └─ falsify
         │
         ▼
Assessment + confidence + gaps
```

### Output template (brief)

1. BLUF (bottom line up front)
2. Key judgments
3. Evidence summary (with links/hashes)
4. Alternatives considered
5. Gaps & next collection

---

## 6. Geolocation as a verification skill

Geolocation in OSINT means verifying a location claim from public photos/videos, not harassment-oriented tracking.

### Conceptual techniques (verification, not offense)

| Signal | How it is used |
|:---|:---|
| Landmark | Matching a building's silhouette against public maps |
| Signage / language | Country/city clues |
| Sun / shadow | Rough estimate of time/direction |
| Vegetation / climate | Regional consistency |
| Infrastructure | Power poles, road markings, left/right-hand drive |
| EXIF (if present) | Only when metadata is still embedded and access is lawful |

Treat a location claim as confirmed only when at least two independent clues agree.

Ethics: do not publish a private home address; do not doxx. For internal IR/DFIR work, follow the organization's privacy policy.

---

## 7. OPSEC for investigators

Investigators themselves can become targets (counter-OSINT).

| Risk | Mitigation |
|:---|:---|
| Leaking your real identity | Separate your investigation identity from your personal one |
| Browser fingerprinting | Use a separate profile; limit extensions |
| Geo leak | VPN/org policy; do not mix in personal accounts |
| Malicious documents | Sandbox them; do not enable macros carelessly |
| Being surveilled by the target | Do not upload evidence to random platforms |

```
Personal life  ≠  Investigation workspace
     │                    │
   private            logged, policy-bound, legal
```

OPSEC in one sentence:

the more you reuse the same identity, device, payment method, or writing habits across different investigations, the easier you are to trace.

Minimize reuse across contexts.

---

## 8. Sock puppets: an ethics warning

A sock puppet is a persona account used for collection. In many professional contexts:

| Status | View |
|:---|:---|
| Academic / hobbyist | Often violates platform ToS |
| Law enforcement / official intel | Governed by strict policy and law |
| Bug bounty / pentest | Usually out of scope without explicit authorization |
| Journalism | Bound by codes of ethics and local law |

### Hard warnings

- Never use a persona to deceive a vulnerable individual, for grooming, or for fraud.
- Do not harvest data behind a login that requires a fake identity if doing so breaks the law or the ToS.
- Prefer genuinely public sources that require no deceptive authentication.
- If your organization permits persona use, document the approval, the boundaries, and the data retention policy.

This note does not provide a recipe for building a persona to infiltrate a community. The focus is explaining why it is legally and ethically risky, and how to avoid relying on it.

---

## 9. Legal & ethical bounds

| Boundary | Practice |
|:---|:---|
| Computer access law | Do not bypass access controls |
| Privacy (GDPR-style) | Minimize data; keep the purpose clear; limit retention |
| Platform ToS | Aggressive automation can breach the contract |
| Copyright | Do not mass-redistribute protected content |
| Safety | Do not doxx; do not publish sensitive PII |
| Workplace | Follow the RoE and legal counsel's guidance |

Quick ethics check:

```text
1. Would I be comfortable if this were published?
2. Could I defend it in court?
3. Is this the least harmful way to do it?
```

If any answer is "no," stop and request a legal review.

---

## 10. Workflow cheatsheet

```text
1. Write the PIR (1-3 questions)
2. Legal check: public? ToS? jurisdiction?
3. Collect with provenance (URL, UTC, hash)
4. Process → entity graph + timeline
5. Analyze → judgments + confidence + alternatives
6. Report BLUF; flag gaps
7. Reduce data; store per retention policy
8. Review investigator OPSEC
```

| Need | Public collection direction (example class) |
|:---|:---|
| Domain footprint | Public DNS history, CT logs |
| Org structure | Company filings, press, career pages |
| Infrastructure hints | Job posts, public cloud docs, status pages |
| Incident context | Vendor advisories, public timelines |
| Image verification | Maps + landmark corroboration |

---

## Security notes: threats & defenses

| Threat | Mechanism | Defense |
|:---|:---|:---|
| Investigator doxxed | Counter-OSINT | Segregated personas/devices (per policy) |
| Poisoned sources | Disinformation / fake leaks | Multi-source corroboration |
| Overcollection | Hoarding PII | Minimization + retention policy |
| ToS / legal breach | Aggressive scraping | Manual/public APIs; legal counsel |
| Bias cascade | Seeing what you want to see | Red-team your own hypothesis |
| Unsafe handling | Malicious files | Sandbox analysis |

Not covered: bypassing a paywall with stolen credentials, hacking accounts, malware for collection, or a doxxing playbook.

---

> **References & book sources**
> - *Open Source Intelligence Methods and Tools*, `~/Documents/Books/CyberSec/OSINT/`
> - Public tradecraft: the intelligence cycle (ICD-style confidence language), source criticism
> - Platform policies and local computer-crime / privacy statutes (always check current law)

> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Legal and ethical OSINT only. Not a license to compromise systems or people.
