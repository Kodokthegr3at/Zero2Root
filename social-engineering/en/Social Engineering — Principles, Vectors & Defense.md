# Social Engineering: Principles, Vectors & Defense

> **Zero2Root** | Human Factor Security Series
> Last updated: 2026 | Author: kodoktheGr3at
> Primary refs: Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*; Kevin Mitnick, *The Art of Deception*; Joe Gray, *Practical Social Engineering*

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-068` | **Phase 7:** Specialized
> **Est. study:** 4-5h | **Level:** Intermediate
> **Prerequisites:** LC-058
> **Book map:** Hadnagy, Social Engineering 2nd Ed.; Mitnick, The Art of Deception; Gray, Practical Social Engineering
<!-- LC-CURRICULUM-END -->

## Table of Contents

1. The human layer as attack surface
2. Cialdini's principles of influence (defense lens)
3. Social engineering narrative cycle
4. Common vectors (concepts)
5. Detection signals: red flags
6. Awareness training that works
7. Organizational controls
8. Ethics, law & authorized testing
9. Social engineering incident response
10. Defense cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Social engineering (SE) | Tricking a person into giving access, information, or taking an action, instead of hacking a computer |
| Pretext | The fake story the attacker uses ("I'm from IT", "I'm the new vendor") |
| Rapport | The friendly connection an attacker builds so you lower your guard |
| OSINT | Open-source intelligence: information anyone can find publicly (LinkedIn, the company website, social media) |
| Out-of-band verification | Checking a request through a *different* channel you already trust. Example: an email asks for a transfer, so you call the sender at the number in the company directory, not the number in the email |
| Callback | Hanging up and calling the person back on their official number |
| Dual control | A sensitive action needs two people to approve it, so one tricked person isn't enough |
| BEC | Business Email Compromise: an email scam that tricks staff into sending money to the wrong account |
| SOC | Security Operations Center: the team that receives and handles security reports |
| RoE | Rules of Engagement: a signed document saying what a security test may and may not do |

---

## 1. The Human Layer as Attack Surface

Firewalls and antivirus don't help if an attacker can simply convince an employee to open the door. Mitnick (*The Art of Deception*) points out three human habits attackers rely on: we like to help, we avoid conflict, and we trust anyone who looks like an authority.

A social engineering attempt is most likely to work when:

- the target **trusts** the person contacting them,
- the request feels **urgent**,
- the target **has access** to something valuable, and
- there is **no easy way to verify** the request.

Take away even one of these, especially the last one, and the attack gets much harder.

So social engineering doesn't attack a bug in software. It attacks how people think and the gaps in a company's procedures. That means the defense is also mostly people and process: clear procedures, a culture where it's fine to say "let me check first," and a reliable way to verify requests.

```
┌──────────────┐     trust / fear / greed      ┌──────────────┐
│  Attacker    │ ─────────────────────────────▶│   Target     │
│  narrative   │◀──── info / access / action ──│   human      │
└──────────────┘                               └──────────────┘
        │                                              │
        └────────── defense: verify out-of-band ───────┘
```

---

## 2. Cialdini's Principles of Influence (Defense Lens)

Psychologist Robert Cialdini described a handful of things that make people say "yes." Hadnagy built his social engineering framework on them. We study them here so you can **spot** manipulation, not use it.

| Principle | What it means | How an attacker uses it | How to defend |
|:---|:---|:---|:---|
| Reciprocity | We feel we owe people who helped us | "I helped you last week, can you send me that file?" | A favor never replaces the normal procedure |
| Commitment / consistency | We want to stick with what we said earlier | "You said earlier you could help..." | You're always allowed to change your mind when something feels off |
| Social proof | We copy what others do | "Everyone on staff already updated through this link" | Check with the official source, not with "everyone" |
| Authority | We obey bosses and uniforms | "The IT Director wants this reset right now" | Call back on the official number; require a second approver |
| Liking | We help people we like | Lots of friendly chat, then a sensitive request | Being friendly is not the same as being authorized |
| Scarcity / urgency | We panic when something might be lost | "Your account closes in 15 minutes" | Rule: no sensitive action under sudden time pressure |
| Unity | We trust "one of us" | Pretending to be from the same community or partner company | Verify identity, no matter how familiar they seem |

### The pattern behind all of them

Every principle pushes you to act **quickly** and **without checking**. So the defense is always the same idea: add a short checking step (a callback, a ticket, a second approver) before anything sensitive happens. The step should be quick enough that people actually follow it, but firm enough that pressure can't skip it.

---

## 3. Social Engineering Narrative Cycle

Most social engineering attempts follow similar steps (based on *Practical Social Engineering* and Hadnagy). This is a general picture for recognizing attacks, not a guide for running one.

```
Research → Build a story → Make contact → Build trust → Ask → Leave → (Report)
```

| Step | What the attacker does | How to defend |
|:---|:---|:---|
| Research (OSINT) | Collects public info about the company or person | Share less publicly; teach staff about privacy |
| Build a story (pretext) | Creates a believable reason to contact you | Be suspicious of any story that ends with asking for access |
| Make contact | Email, phone, in person, chat | Use official channels; show warning banners on outside email |
| Build trust (rapport) | Makes you feel comfortable | Notice when a sudden request comes right after small talk |
| Ask | Requests an action or information | Never skip checking just because the request seems "small" |
| Leave | Ends the conversation without raising suspicion | Keep logs; review what happened afterward |
| Report | (Only in authorized testing) writes up the results | Only allowed with a signed RoE |

Important: this repository does not teach how to build phishing kits, set up tools like Evilginx, make BadUSB devices, or write scam scripts. The focus is on psychology, detection, and training.

---

## 4. Common Vectors (Concepts)

A "vector" is simply the route the attack comes through.

| Vector | What it is | What it usually asks for |
|:---|:---|:---|
| Phishing / spear-phishing | A fake message asking you to click or reply. Spear-phishing targets one specific person | Passwords, clicking a malware link, changing a payment |
| Vishing | Scam phone call (voice phishing) | Password reset, MFA code, customer data |
| Smishing | Scam SMS or chat message | Clicking a fake "package delivery" or "bank" link |
| Pretexting (helpdesk) | Calling the helpdesk while pretending to be an employee or vendor | Unlocking an account, adding them to the VPN |
| Physical impersonation | Showing up in person pretending to belong there | Following staff through a locked door (tailgating) |
| Business Email Compromise (BEC) | Fake invoice or fake "CEO" email | Changing the bank account a payment goes to |
| Quid pro quo | "I'll fix your IT problem, just install this" | Installing a remote access tool |

### How bad can it get?

The damage grows when:

- the victim gives **more access** (an admin account is worse than a normal one),
- the data involved is **more sensitive** (customer data is worse than a lunch menu), and
- the company **notices later** (an hour of access is far less damaging than a month).

---

## 5. Detection Signals: Red Flags

### In the message itself

- Extreme urgency plus a threat ("do this now or you'll be fired").
- A request to skip the normal procedure or keep it secret ("don't tell anyone").
- An email address that almost matches the real one, like `paypa1.com` instead of `paypal.com`, or a strange subdomain.
- A request for your MFA code, password, or crypto seed phrase. Real IT staff never ask for these.
- A vendor changing their bank account without confirming through a second channel.

### In how the request is made

- Contact outside working hours plus pressure to answer right away.
- Asking you to install an unusual remote-control tool.
- Refusing to open a ticket or to let you call them back.

### Quick action table

| What you notice | Danger | What to do right away |
|:---|:---:|:---|
| Asks for a password / MFA code | High | Stop the conversation; report to the SOC |
| Asks to change payment details | High | Get a second approval from finance |
| A link to a "login page" | Medium-High | Report it; don't click; open the real site yourself |
| A "new" vendor with no purchase order | Medium | Check with procurement |
| Someone following you through a secure door | Medium | Politely ask who they are; call security to escort them |

---

## 6. Awareness Training That Works

Bad training is a yearly video everyone forgets. Good training happens often, is measured, and never embarrasses anyone.

### How to design the program

1. **Start with a baseline.** Run a survey and an authorized phishing simulation (with a signed RoE and HR approval) to see where people stand.
2. **Teach the why.** Explain the influence principles and the callback habit. "Don't click links" alone isn't enough.
3. **Time it well.** Send short tips when scams peak: tax season, payroll, vendor renewals.
4. **Tailor it by role.** Finance learns about BEC, the helpdesk about fake callers, executives about whaling (phishing aimed at senior leaders).
5. **Measure it.** Good signs: more people report, fewer people click twice, reports arrive faster.
6. **No shaming.** People who report quickly get praised, even if they clicked first.

### Is the training paying off?

The training is worth it when more people report suspicious messages and fewer attacks succeed, compared to what the program costs. That's why the report rate is often a better measure than the click rate: one fast report can protect the whole company.

### Example 15-minute session

| Minute | Content |
|:---:|:---|
| 0-3 | A real (anonymized) story from your industry |
| 3-8 | Three red flags and how to check each one |
| 8-12 | Practice: respond to a fake phone call scenario |
| 12-15 | How to report, and what happens after you do |

---

## 7. Organizational Controls

These are the rules and tools a company puts in place so that one tricked person can't cause a disaster.

| Control | How it works | What it stops |
|:---|:---|:---|
| Out-of-band verification | Call back on the number in the HR directory | Phone scams, BEC |
| Dual control | Two people must approve money transfers and access changes | One person being tricked into fraud |
| Least privilege + JIT | People only get the access they need, and only for a limited time (just-in-time) | Helpdesk tricks that grant too much access |
| Email authentication | Turn on SPF, DKIM, and DMARC, which let mail servers detect emails pretending to come from your domain | Fake emails from your own domain |
| External email banner | An "External" label on mail from outside the company | Fake "internal" emails |
| Helpdesk identity check | Employee ID plus a callback before any reset | Account takeover through the helpdesk |
| Physical access policy | Badges and escorts for visitors | Tailgating |
| Phishing-resistant MFA | Passkeys or FIDO2 security keys, which won't work on a fake site | Stolen passwords |
| Data classification | Label sensitive data and never share it over the phone | Oversharing |

How a sensitive request should flow:

```
Request sensitive action
        │
        ▼
  Ticket required? ──no──▶ deny / redirect
        │ yes
        ▼
  Identity proof (policy)
        │
        ▼
  Out-of-band confirm (if high risk)
        │
        ▼
  Dual approval (if financial / admin)
        │
        ▼
  Execute + audit log
```

---

## 8. Ethics, Law & Authorized Testing

| Activity | What you need first |
|:---|:---|
| Social engineering test / phishing simulation | A signed RoE, plus approval from legal, HR, and an executive |
| Researching employees (OSINT) | Use public sources only; follow local privacy law |
| Physical impersonation test | Permission from the building owner and a way to stop the test safely |
| Teaching deception techniques | Don't hand out ready-to-use kits; focus on detection |

Laws differ by country (fraud, computer access, recording calls). A test without permission can break the law and your employment contract.

---

## 9. Social Engineering Incident Response

What to do after someone has been tricked:

1. **Contain:** stop talking to the attacker. If a password was given away, lock or secure the account.
2. **Preserve evidence:** keep the email (with headers), phone numbers, recordings (if legal), and chat logs.
3. **Reset:** change passwords, sign out all sessions, and replace MFA devices if needed. Check for email forwarding rules the attacker may have added.
4. **Notify:** tell the SOC / incident response team, finance for payment fraud, and legal if customer data is involved.
5. **Hunt:** look for new mailbox rules, new people with access to the inbox, and unusual VPN logins.
6. **Learn:** update the training and the controls. Never blame the person who reported it; they helped.

**The faster someone reports, the smaller the damage.** This is the most important habit to build.

---

## 10. Defense Cheatsheet

```text
CHECK BEFORE YOU ACT
[ ] Is someone rushing me?
[ ] Did I verify who they are through an official channel?
[ ] Am I being asked to skip a normal procedure?
[ ] Am I being asked for a secret (password / MFA code / seed phrase)?
[ ] Is this about changing a bank account or admin access?

IF YES TO ANY → STOP → OPEN A TICKET / CALL BACK → REPORT
```

| Role | One habit to keep |
|:---|:---|
| Every employee | Report anything suspicious, even if you might be wrong |
| Helpdesk | No reset without the identity proof the policy requires |
| Finance | Confirm every payment change through a second channel |
| Executive assistant | Run the whaling checklist before scheduling or transfers |
| Security team | Track how many people report, not just how many click |

---

## Security Notes: Threats & Defenses

| Threat | How it happens | Defense |
|:---|:---|:---|
| Password theft | Fake login page / scam call | FIDO2; never share MFA codes; report |
| BEC fraud | Fake invoice / fake CEO email | Dual control; call the vendor back |
| Helpdesk pretexting | Caller tricks helpdesk into a reset | Strong identity check |
| Tailgating | Following someone through a secure door | A culture where asking "who are you?" is normal; turnstiles |
| Oversharing | Attacker builds trust, then asks for too much | Data classification; share only what's needed |
| Shame culture | People hide incidents out of embarrassment | Praise fast reporting |

Not covered: building phishing kits, credential-stealing proxies, BadUSB payloads, or ready-made scam scripts.

---

> **References & Book Sources**
> - Christopher Hadnagy, *Social Engineering: The Science of Human Hacking*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Kevin Mitnick & William Simon, *The Art of Deception*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Joe Gray, *Practical Social Engineering*, `~/Documents/Books/CyberSec/Social Engineering/`
> - Robert Cialdini, *Influence* (principles referenced via the SE literature)

> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Educational and authorized training use only. Do not use this for fraud or unauthorized access.
