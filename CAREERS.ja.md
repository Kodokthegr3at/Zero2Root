**言語:** [English](CAREERS.md) | [Bahasa Indonesia](CAREERS.id.md) | [日本語](CAREERS.ja.md)

# Zero2Root: キャリアパス

> サイバーセキュリティは一つの仕事ではない。このページでは代表的な職種ごとに、日々の仕事内容、準備に役立つZero2Rootのレッスン、そして同じくらい大事な、Zero2Rootがまだ扱っていない内容をまとめている。足りない部分はほかの教材で補ってほしい。
> このページは日本語のレッスンファイルにのみリンクしている。順序立てたカリキュラム全体は[ROADMAP.ja.md](ROADMAP.ja.md)を参照。

---

## このページの読み方

1. どの進路も下の**共通基礎**から始める。すでに理解しているレッスンは飛ばしてよい。
2. 次に、自分の職種のレッスンを記載順に進める。
3. **カバー範囲**は、その職種の内容をZero2Rootが現時点でどれだけ教えているかを正直に示す。*十分*はジュニアに必要な内容の大部分がある、*一部*は重要なトピックが欠けている、*最小限*は大部分を外部の教材で学ぶ必要がある、という意味。
4. **最初の仕事向き**は、セキュリティ経験がなくても採用されることが多い職種を示す。それ以外は関連する仕事を1〜2年経験した後に就くことが多い。
5. 時間は読む時間と実習の目安で、書籍を読む時間は含まない。

---

## 一覧

| 職種 | 仕事内容 | 最初の仕事向き | 共通基礎の後のレッスン数 | 学習時間 | カバー範囲 |
|:---|:---|:---|:---|:---|:---|
| [SOCアナリスト](#socアナリスト) | 多くのシステムからのアラートを監視し、本物の攻撃を見分けてエスカレーションする | はい | 17 | 75-91 | 十分 |
| [インシデント対応・フォレンジックアナリスト (DFIR)](#インシデント対応フォレンジックアナリスト-dfir) | 攻撃が確定したら引き継ぎ、封じ込め、ディスクとメモリから証拠を集め、タイムラインを再構成し、報告書を書く | いいえ | 12 | 58-69 | 十分 |
| [スレットハンター・検知エンジニア](#スレットハンター検知エンジニア) | アラートを出すルールを書いて調整し、それをすり抜けた攻撃者を能動的に探す | いいえ | 9 | 47-57 | 十分 |
| [ペネトレーションテスター](#ペネトレーションテスター) | 書面の許可を得てネットワークやアプリケーションを検証し、本物の攻撃者より先に弱点を見つけ、修正方法を報告する | いいえ | 26 | 105-124 | 一部 |
| [Webアプリケーションペンテスター・バグハンター](#webアプリケーションペンテスターバグハンター) | WebサイトとAPIに集中し、インジェクション、アクセス制御、セッションのバグを見つけて、所有者やバグバウンティに報告する | いいえ | 15 | 59-72 | 十分 |
| [レッドチームオペレーター](#レッドチームオペレーター) | 数週間にわたり現実的な攻撃者を演じ、ブルーチームが気付くかを試す | いいえ | 24 | 107-131 | 一部 |
| [マルウェアアナリスト・リバースエンジニア](#マルウェアアナリストリバースエンジニア) | 不審なファイルを分解し、何をするのか、どう検知するのか、どう後始末するのかを調べる | いいえ | 7 | 40-50 | 十分 |
| [脆弱性リサーチャー・エクスプロイト開発者](#脆弱性リサーチャーエクスプロイト開発者) | ソフトウェアの新しいバグを見つけ、悪用可能かを示して、ベンダーが修正できるようにする | いいえ | 4 | 25-32 | 最小限 |
| [アプリケーションセキュリティ・DevSecOpsエンジニア](#アプリケーションセキュリティdevsecopsエンジニア) | 開発者と協力してコードを安全にリリースする | いいえ | 15 | 58-72 | 一部 |
| [クラウドセキュリティエンジニア](#クラウドセキュリティエンジニア) | AWS、Azure、Google Cloud上のアカウント、ID、ネットワーク、ワークロードを守る | いいえ | 8 | 32-37 | 最小限 |
| [脅威インテリジェンス・OSINTアナリスト](#脅威インテリジェンスosintアナリスト) | 公開・非公開の情報源から攻撃グループと手口を追跡し、防御側が使える助言にまとめる | いいえ | 5 | 25-30 | 一部 |
| [モバイル・IoTセキュリティスペシャリスト](#モバイルiotセキュリティスペシャリスト) | スマホアプリ、スマートデバイス、そのファームウェアを、アプリのコードから基板まで検証する | いいえ | 14 | 66-81 | 一部 |
| [GRC・セキュリティコンプライアンスアナリスト](#grcセキュリティコンプライアンスアナリスト) | ISO 27001やNIST CSFなどの基準に沿ってリスク、ポリシー、監査を管理する | はい | 5 | 25-29 | 最小限 |

---

## 共通基礎 (すべての進路)

すべての職種で共通するレッスン。コンピュータ、Linux、ネットワークの仕組みと、Webの基本。約108〜128時間。

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-001` | [Expression](basics/ja/Expression.md) | 初級 | 2-3時間 |
| 2 | `LC-002` | [Git — Version Control System](basics/ja/Git%20%E2%80%94%20Version%20Control%20System.md) | 初級 | 3-4時間 |
| 3 | `LC-005` | [Linux File System](basics/OperatingSystem/ja/Linux%20File%20System.md) | 初級 | 5-6時間 |
| 4 | `LC-006` | [Windows File System](basics/OperatingSystem/ja/Windows%20File%20System.md) | 初級 | 5-6時間 |
| 5 | `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/ja/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) | 初級 | 3-4時間 |
| 6 | `LC-009` | [Linux Distributions (Distros)](linux/ja/02.%20Linux%20Distributions%20%28Distros%29.md) | 初級 | 2-3時間 |
| 7 | `LC-010` | [Introduction to Shell](linux/ja/03.%20Introduction%20to%20Shell.md) | 初級 | 4-5時間 |
| 8 | `LC-011` | [Prompt Description & PS1 Customization](linux/ja/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) | 初級 | 2時間 |
| 9 | `LC-012` | [Getting Help — man, --help, apropos](linux/ja/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) | 初級 | 2時間 |
| 10 | `LC-013` | [System Information — Kernel, Hardware & Environment](linux/ja/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) | 初級 | 3時間 |
| 11 | `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/ja/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) | 初級 | 2-3時間 |
| 12 | `LC-015` | [Working with Files & Directories](linux/ja/08.%20Working%20with%20Files%20%26%20Directories.md) | 初級 | 3-4時間 |
| 13 | `LC-016` | [Editing Files — Nano & Vim](linux/ja/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) | 初級 | 4-5時間 |
| 14 | `LC-017` | [Find Files & Directories](linux/ja/10.%20Find%20Files%20%26%20Directories.md) | 初級 | 3時間 |
| 15 | `LC-018` | [File Descriptors & Redirections](linux/ja/11.%20File%20Descriptors%20%26%20Redirections.md) | 中級 | 4時間 |
| 16 | `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/ja/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) | 中級 | 4-5時間 |
| 17 | `LC-020` | [Regular Expressions (RegEx)](linux/ja/13.%20Regular%20Expressions%20%28RegEx%29.md) | 中級 | 5-6時間 |
| 18 | `LC-021` | [Permission Management](linux/ja/14.%20Permission%20Management.md) | 中級 | 4-5時間 |
| 19 | `LC-022` | [User Management](linux/ja/15.%20User%20Management.md) | 中級 | 4時間 |
| 20 | `LC-024` | [Service and Process Management](linux/ja/17.%20Service%20and%20Process%20Management.md) | 中級 | 4-5時間 |
| 21 | `LC-026` | [Network Services](linux/ja/19.%20Network%20Services.md) | 中級 | 4時間 |
| 22 | `LC-031` | [Linux Networking — Interfaces & Routing](linux/ja/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) | 中級 | 4時間 |
| 23 | `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/ja/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) | 中級 | 4-5時間 |
| 24 | `LC-035` | [System Logs](linux/ja/28.%20System%20Logs.md) | 中級 | 3-4時間 |
| 25 | `LC-038` | [OSI Modelling](networking/ja/OSI%20Modelling.md) | 初級 | 6-8時間 |
| 26 | `LC-039` | [TCP-IP Architecture & Socket Programming](networking/ja/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) | 中級 | 5-6時間 |
| 27 | `LC-040` | [IP Addressing & Subnetting](networking/ja/IP%20Addressing%20%26%20Subnetting.md) | 中級 | 4-5時間 |
| 28 | `LC-041` | [DNS & Domain Name System Security](networking/ja/DNS%20%26%20Domain%20Name%20System%20Security.md) | 中級 | 4時間 |
| 29 | `LC-044` | [HTTP & cURL](web/HTTP/ja/1.%20HTTP%20%26%20cURL.md) | 初級 | 3時間 |
| 30 | `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/ja/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) | 初級 | 3時間 |

---

## SOCアナリスト

**仕事内容:** 多くのシステムからのアラートを監視し、本物の攻撃を見分けてエスカレーションする。サイバーセキュリティで最も一般的な最初の仕事。

**最初の仕事向き:** はい  
**Zero2Rootでのカバー範囲:** 十分

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/ja/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | 初級 | 3-4時間 |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 4 | `LC-034` | [Firewall Setup](linux/ja/27.%20Firewall%20Setup.md) | 上級 | 4時間 |
| 5 | `LC-042` | [ARP & Local Network Attacks](networking/ja/ARP%20%26%20Local%20Network%20Attacks.md) | 上級 | 4時間 |
| 6 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | 中級 | 3-4時間 |
| 7 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 8 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 9 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/ja/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | 中級 | 3-4時間 |
| 12 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/ja/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | 中級 | 4-5時間 |
| 13 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 14 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/ja/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | 中級 | 6-7時間 |
| 15 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |
| 16 | `LC-075` | [Incident Response & Digital Forensics](blue-team/ja/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | 上級 | 7-9時間 |
| 17 | `LC-076` | [Active Directory Fundamentals](active-directory/ja/1.%20Active%20Directory%20Fundamentals.md) | 中級 | 5-6時間 |

この進路の学習時間: 共通基礎とは別に約75〜91時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Active DirectoryとWindowsイベントログの詳細
- 特定製品を使ったSIEMの実習
- フィッシングメール分析の独立したレッスン
- クラウドのログ (AWS CloudTrail、Microsoft 365)

---

## インシデント対応・フォレンジックアナリスト (DFIR)

**仕事内容:** 攻撃が確定したら引き継ぎ、封じ込め、ディスクとメモリから証拠を集め、タイムラインを再構成し、報告書を書く。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 十分

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-007` | [macOS File System](basics/OperatingSystem/ja/macOS%20File%20System.md) | 初級 | 4-5時間 |
| 3 | `LC-028` | [Backup and Restore](linux/ja/21.%20Backup%20and%20Restore.md) | 中級 | 3時間 |
| 4 | `LC-029` | [File System Management](linux/ja/22.%20File%20System%20Management.md) | 中級 | 4-5時間 |
| 5 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 6 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | 上級 | 5-6時間 |
| 7 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/ja/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | 上級 | 5時間 |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 9 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/ja/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | 中級 | 6-7時間 |
| 10 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |
| 11 | `LC-075` | [Incident Response & Digital Forensics](blue-team/ja/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | 上級 | 7-9時間 |
| 12 | `LC-076` | [Active Directory Fundamentals](active-directory/ja/1.%20Active%20Directory%20Fundamentals.md) | 中級 | 5-6時間 |

この進路の学習時間: 共通基礎とは別に約58〜69時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Windowsレジストリとアーティファクトのフォレンジック詳細
- モバイル端末のフォレンジック
- クラウドでのインシデント対応

---

## スレットハンター・検知エンジニア

**仕事内容:** アラートを出すルールを書いて調整し、それをすり抜けた攻撃者を能動的に探す。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 十分

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/ja/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | 上級 | 5-6時間 |
| 3 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/ja/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | 上級 | 5-6時間 |
| 4 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | 上級 | 5-6時間 |
| 5 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/ja/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | 上級 | 5時間 |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |
| 7 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 8 | `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/ja/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) | 中級 | 6-7時間 |
| 9 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約47〜57時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Detection-as-codeとルールのCIパイプライン
- ログパイプラインのデータエンジニアリング

---

## ペネトレーションテスター

**仕事内容:** 書面の許可を得てネットワークやアプリケーションを検証し、本物の攻撃者より先に弱点を見つけ、修正方法を報告する。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 一部

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/ja/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | 初級 | 3-4時間 |
| 3 | `LC-025` | [Task Scheduling](linux/ja/18.%20Task%20Scheduling.md) | 中級 | 3-4時間 |
| 4 | `LC-027` | [Working with Web Services](linux/ja/20.%20Working%20with%20Web%20Services.md) | 中級 | 3-4時間 |
| 5 | `LC-030` | [Containerization](linux/ja/23.%20Containerization.md) | 上級 | 4-5時間 |
| 6 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 7 | `LC-034` | [Firewall Setup](linux/ja/27.%20Firewall%20Setup.md) | 上級 | 4時間 |
| 8 | `LC-042` | [ARP & Local Network Attacks](networking/ja/ARP%20%26%20Local%20Network%20Attacks.md) | 上級 | 4時間 |
| 9 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/ja/Wireless%20802.11%20Security%20%26%20Attacks.md) | 上級 | 5時間 |
| 10 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | 中級 | 3-4時間 |
| 11 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 12 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 13 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | 中級 | 3時間 |
| 14 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 15 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 16 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | 上級 | 3-4時間 |
| 17 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 18 | `LC-056` | [Hash Functions & Message Authentication](cryptography/ja/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | 中級 | 3-4時間 |
| 19 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 20 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/ja/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | 中級 | 4-5時間 |
| 21 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/ja/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | 中級 | 4時間 |
| 22 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/ja/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | 上級 | 5-6時間 |
| 23 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/ja/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | 上級 | 5-6時間 |
| 24 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |
| 25 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/ja/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | 中級 | 5時間 |
| 26 | `LC-076` | [Active Directory Fundamentals](active-directory/ja/1.%20Active%20Directory%20Fundamentals.md) | 中級 | 5-6時間 |

この進路の学習時間: 共通基礎とは別に約105〜124時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Active Directoryの攻撃と防御 (内部テストの多くはADが関わる)
- ペンテスト報告書の書き方
- クラウドのペネトレーションテスト

---

## Webアプリケーションペンテスター・バグハンター

**仕事内容:** WebサイトとAPIに集中し、インジェクション、アクセス制御、セッションのバグを見つけて、所有者やバグバウンティに報告する。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 十分

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/ja/20.%20Working%20with%20Web%20Services.md) | 中級 | 3-4時間 |
| 2 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | 中級 | 3-4時間 |
| 3 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 4 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 5 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | 中級 | 3時間 |
| 6 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 7 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 8 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | 上級 | 3-4時間 |
| 9 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 10 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/ja/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | 中級 | 4-5時間 |
| 11 | `LC-056` | [Hash Functions & Message Authentication](cryptography/ja/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | 中級 | 3-4時間 |
| 12 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/ja/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | 中級 | 4-5時間 |
| 14 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |
| 15 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/ja/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | 中級 | 5時間 |

この進路の学習時間: 共通基礎とは別に約59〜72時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- APIセキュリティ (RESTとGraphQL) の独立したレッスン
- OAuthとSSOの欠陥の詳細
- 安全でないデシリアライゼーション

---

## レッドチームオペレーター

**仕事内容:** 数週間にわたり現実的な攻撃者を演じ、ブルーチームが気付くかを試す。通常は数年のペンテスト経験の後に就く。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 一部

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-004` | [Windows Command Prompt (cmd.exe)](basics/ja/Windows%20Command%20Prompt%20%28cmd.exe%29.md) | 初級 | 3-4時間 |
| 3 | `LC-030` | [Containerization](linux/ja/23.%20Containerization.md) | 上級 | 4-5時間 |
| 4 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 5 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | 中級 | 3-4時間 |
| 6 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 7 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 8 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | 中級 | 3時間 |
| 9 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 10 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 11 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | 上級 | 3-4時間 |
| 12 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 13 | `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/ja/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) | 中級 | 4-5時間 |
| 14 | `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/ja/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) | 中級 | 4時間 |
| 15 | `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/ja/3.%20Metasploit%20Framework%20%26%20Exploitation.md) | 上級 | 5-6時間 |
| 16 | `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/ja/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) | 上級 | 5-6時間 |
| 17 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/ja/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | 上級 | 6-8時間 |
| 18 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/ja/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | 上級 | 8-10時間 |
| 19 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |
| 20 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/ja/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | 中級 | 4-5時間 |
| 21 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/ja/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | 中級 | 5時間 |
| 22 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 23 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |
| 24 | `LC-076` | [Active Directory Fundamentals](active-directory/ja/1.%20Active%20Directory%20Fundamentals.md) | 中級 | 5-6時間 |

この進路の学習時間: 共通基礎とは別に約107〜131時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Active Directoryの攻撃経路
- C2インフラとOPSEC
- エンドポイント検知の仕組みと、攻撃者がそれを避けようとする理由

---

## マルウェアアナリスト・リバースエンジニア

**仕事内容:** 不審なファイルを分解し、何をするのか、どう検知するのか、どう後始末するのかを調べる。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 十分

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-003` | [PowerShell](basics/ja/PowerShell.md) | 初級 | 4-5時間 |
| 2 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/ja/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | 上級 | 6-8時間 |
| 3 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | 上級 | 5-6時間 |
| 4 | `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/ja/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) | 上級 | 5時間 |
| 5 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/ja/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | 上級 | 8-10時間 |
| 6 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |
| 7 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約40〜50時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- Windows内部構造の詳細
- アンパックと解析妨害の手口
- .NETとAndroidのマルウェア

---

## 脆弱性リサーチャー・エクスプロイト開発者

**仕事内容:** ソフトウェアの新しいバグを見つけ、悪用可能かを示して、ベンダーが修正できるようにする。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 最小限

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/ja/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | 上級 | 6-8時間 |
| 2 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | 上級 | 5-6時間 |
| 3 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/ja/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | 上級 | 8-10時間 |
| 4 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約25〜32時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- ヒープのエクスプロイト
- ファジング
- カーネルとブラウザのエクスプロイト
- 最新の緩和策の詳細 (CFG、CET、サンドボックス)

---

## アプリケーションセキュリティ・DevSecOpsエンジニア

**仕事内容:** 開発者と協力してコードを安全にリリースする。設計とコードをレビューし、ビルドパイプラインにセキュリティチェックを加える。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 一部

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/ja/20.%20Working%20with%20Web%20Services.md) | 中級 | 3-4時間 |
| 2 | `LC-030` | [Containerization](linux/ja/23.%20Containerization.md) | 上級 | 4-5時間 |
| 3 | `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) | 中級 | 3-4時間 |
| 4 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 5 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 6 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | 中級 | 3時間 |
| 7 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 8 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 9 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | 上級 | 3-4時間 |
| 10 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 11 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/ja/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | 中級 | 4-5時間 |
| 12 | `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/ja/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) | 中級 | 4-5時間 |
| 13 | `LC-056` | [Hash Functions & Message Authentication](cryptography/ja/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) | 中級 | 3-4時間 |
| 14 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 15 | `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約58〜72時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- セキュアSDLCと脅威モデリング
- CIでのSAST、DAST、依存関係スキャン
- ソフトウェアサプライチェーンのセキュリティ
- シークレット管理

---

## クラウドセキュリティエンジニア

**仕事内容:** AWS、Azure、Google Cloud上のアカウント、ID、ネットワーク、ワークロードを守る。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 最小限

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-027` | [Working with Web Services](linux/ja/20.%20Working%20with%20Web%20Services.md) | 中級 | 3-4時間 |
| 2 | `LC-030` | [Containerization](linux/ja/23.%20Containerization.md) | 上級 | 4-5時間 |
| 3 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 4 | `LC-034` | [Firewall Setup](linux/ja/27.%20Firewall%20Setup.md) | 上級 | 4時間 |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 6 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 7 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 8 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |

この進路の学習時間: 共通基礎とは別に約32〜37時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- クラウドIAM (AWS、Azure、GCP)
- Kubernetesのセキュリティ
- Infrastructure as Codeとその設定ミス
- クラウドのログと検知

---

## 脅威インテリジェンス・OSINTアナリスト

**仕事内容:** 公開・非公開の情報源から攻撃グループと手口を追跡し、防御側が使える助言にまとめる。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 一部

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) | 上級 | 5-6時間 |
| 2 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/ja/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | 中級 | 4-5時間 |
| 3 | `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/ja/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) | 中級 | 5時間 |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 5 | `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約25〜30時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- インテリジェンスのフレームワーク (ダイヤモンドモデル、キルチェーン) の詳細
- 共有形式 (STIX/TAXII、MISP)
- インテリジェンス報告書の書き方

---

## モバイル・IoTセキュリティスペシャリスト

**仕事内容:** スマホアプリ、スマートデバイス、そのファームウェアを、アプリのコードから基板まで検証する。

**最初の仕事向き:** いいえ。通常は関連職で1〜2年の経験を積んだ後  
**Zero2Rootでのカバー範囲:** 一部

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-043` | [Wireless 802.11 Security & Attacks](networking/ja/Wireless%20802.11%20Security%20%26%20Attacks.md) | 上級 | 5時間 |
| 2 | `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) | 中級 | 5-6時間 |
| 3 | `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) | 中級 | 4-5時間 |
| 4 | `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) | 中級 | 3時間 |
| 5 | `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) | 上級 | 3-4時間 |
| 6 | `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) | 上級 | 4-5時間 |
| 7 | `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) | 上級 | 3-4時間 |
| 8 | `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) | 上級 | 4-5時間 |
| 9 | `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/ja/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) | 中級 | 4-5時間 |
| 10 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 11 | `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/ja/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) | 上級 | 6-8時間 |
| 12 | `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/ja/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) | 上級 | 8-10時間 |
| 13 | `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/ja/Android%20Security%20Internals%20%26%20Vulnerabilities.md) | 上級 | 6-8時間 |
| 14 | `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/ja/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) | 上級 | 6-8時間 |

この進路の学習時間: 共通基礎とは別に約66〜81時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- iOSのセキュリティ
- Bluetooth Low Energy
- モバイルアプリ通信の傍受の詳細

---

## GRC・セキュリティコンプライアンスアナリスト

**仕事内容:** ISO 27001やNIST CSFなどの基準に沿ってリスク、ポリシー、監査を管理する。ツールより人と文書を扱う仕事が多い。

**最初の仕事向き:** はい  
**Zero2Rootでのカバー範囲:** 最小限

**レッスン (共通基礎の後、この順で):**

| # | ID | レッスン | レベル | 時間 |
|:---|:---|:---|:---|:---|
| 1 | `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) | 上級 | 4時間 |
| 2 | `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) | 上級 | 5時間 |
| 3 | `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/ja/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) | 中級 | 4-5時間 |
| 4 | `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) | 初級 | 5-6時間 |
| 5 | `LC-075` | [Incident Response & Digital Forensics](blue-team/ja/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) | 上級 | 7-9時間 |

この進路の学習時間: 共通基礎とは別に約25〜29時間。

**Zero2Rootでまだ扱っていない内容** (ほかの教材で学ぶ):

- リスク評価の手法
- ISO 27001、NIST CSFなどのフレームワーク
- インドネシアと日本の個人情報保護法 (UU PDP、APPI)
- 監査と証跡の収集
