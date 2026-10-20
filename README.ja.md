**言語:** [English](README.md) | [Bahasa Indonesia](README.id.md) | [日本語](README.ja.md)

# Zero2Root

[![GitHub stars](https://img.shields.io/github/stars/Kodokthegr3at/Zero2Root?style=social)](https://github.com/Kodokthegr3at/Zero2Root/stargazers)

![Lessons](https://img.shields.io/badge/lessons-76-blue) ![Languages](https://img.shields.io/badge/languages-ID%20%C2%B7%20EN%20%C2%B7%20JA-success) ![Level](https://img.shields.io/badge/level-beginner%20%E2%86%92%20advanced-orange) ![Phases](https://img.shields.io/badge/phases-11-blueviolet) [![Last commit](https://img.shields.io/github/last-commit/Kodokthegr3at/Zero2Root)](https://github.com/Kodokthegr3at/Zero2Root/commits/main) [![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

> **ゼロからroot(管理者権限)まで** — Linux内部構造、ネットワーキング、Webアプリケーションセキュリティ、暗号技術、リバースエンジニアリングなどを扱う、3言語対応のサイバーセキュリティ知識ベース兼キャリアロードマップで、攻撃と防御の両方を含む。このページは日本語版であり、日本語のレッスンファイルにのみリンクしている。他の2言語は上のEnglishまたはBahasa Indonesiaを開くこと。

---

## はじめに

| ドキュメント | 目的 |
|:---------|:--------|
| [ROADMAP.ja.md](ROADMAP.ja.md) | 主要な学習パス: 76レッスン（`LC-001`から`LC-076`）、11フェーズ、前提条件 |
| [CAREERS.ja.md](CAREERS.ja.md) | キャリアパス: サイバーセキュリティの13職種、それぞれのレッスン、学習時間、まだ扱っていない内容 |
| [BOOKS.ja.md](BOOKS.ja.md) | `~/Documents/Books/`にあるローカルPDFカタログ、各レッスンに対応 |
| [curriculum.json](curriculum.json) | 機械可読なカリキュラムマニフェスト（ID、パス、書籍の章） |

おすすめの始め方: まず[CAREERS.ja.md](CAREERS.ja.md)で職種を選ぶ。決まっていなければ[ROADMAP.ja.md](ROADMAP.ja.md)を開き、**LC-001**から始め、[BOOKS.ja.md](BOOKS.ja.md)でリンクされた書籍の章を読んでから、レッスンファイルを開く（各ファイルの冒頭に`Curriculum ID`ブロックがある）。

---

## カテゴリ

各レッスンは一つのフェーズに、各フェーズは一つのカテゴリに属する。[CAREERS.ja.md](CAREERS.ja.md)で職種を選ぶと、自分に必要なカテゴリが分かる。

| カテゴリ | フェーズ | 内容 |
|:---|:---|:---|
| 基礎 | 0, 1, 2, 4 | コンピュータ、Linux、ネットワーク、暗号。どの進路でも必要。 |
| 攻撃側 (レッドチーム) | 3, 5 | Web攻撃、ペンテスト手法、スキャン、エクスプロイト、権限昇格。ラボと許可された検証でのみ使う。 |
| エクスプロイトとリバースエンジニアリング | 6 | メモリのバグ、シェルコード、アセンブリ、マルウェアの静的・動的解析。 |
| 防御側 (ブルーチーム) | 9 | SOCとログ、ネットワーク監視、スレットハンティング、インシデント対応とフォレンジック。 |
| 専門分野 | 7, 10 | Active Directory、Android、PythonとGoによるセキュリティツール開発、ソーシャルエンジニアリング、OSINT、ハードウェアとIoT。 |
| ボーナス | 8 | エディタと生産性のスキル。 |

---

## このリポジトリについて

このリポジトリは、攻撃的セキュリティ、Linux内部構造、ネットワークプロトコル分析、Webアプリケーションのペネトレーションテスト、暗号技術、リバースエンジニアリング、マルウェア分析、バイナリエクスプロイテーション、セキュリティプログラミング、ソーシャルエンジニアリング、OSINT、モバイルセキュリティ、ハードウェア/IoTセキュリティ、ブルーチームの防御（SOC、ネットワーク監視、スレットハンティング、インシデント対応とフォレンジック）を扱う自習用の知識ベースだ。

各レッスンは、インドネシア語、英語、日本語それぞれで独立した3つのファイルとして存在し、各トピックの`id/`、`en/`、`ja/`サブフォルダに保存されている。それぞれに比較表、コマンドの実例、セキュリティノート、チートシート、そして`~/Documents/Books/`にローカル保存された技術書への参照が含まれる。

---

## リポジトリマップ

```
Zero2Root/
  basics/               # コンピューティングの基礎、Git、OSファイルシステム、PowerShell/CMD
  linux/                # シェル、ワークフロー、システム管理、ネットワーキング、ハードニング
  networking/           # OSIモデル、TCP/IP、DNS、ARP、サブネッティング、無線セキュリティ
  web/                  # HTTP/HTTPS、SQLi、XSS、CSRF、SSRF、LFI/RFI、アップロード、JWT/セッション攻撃
  cryptography/         # 対称鍵/公開鍵暗号、ハッシュ、PKI、TLS 1.3
  ethical-hacking/      # PTES手法、Nmap、Metasploit、権限昇格
  binary-exploitation/  # スタックバッファオーバーフロー、シェルコーディング、対策
  malware-analysis/     # 静的/動的トリアージ、サンドボックス化、x86/x64アセンブリ
  mobile-security/      # Android内部構造、サンドボックス化、Binder IPC、リバースエンジニアリング
  programming-security/ # ツール開発のための攻撃的なPythonとGo
  social-engineering/   # 影響力の原理、経路、組織的防御
  osint/                # インテリジェンスのライフサイクル、OPSEC、調査フレームワーク
  hardware-iot/         # UART/JTAG/SPI、ファームウェア抽出、CANバス
  blue-team/            # SOC、ログ分析、ネットワーク監視、スレットハンティング、IRとフォレンジック
  active-directory/     # ドメイン、ドメインコントローラー、オブジェクト、グループポリシー、トラスト
```

すべてのトピックフォルダは同じレイアウトに従う。基本ディレクトリの下に`id/`、`en/`、`ja/`サブフォルダがあり、それぞれにその言語向けに独立して翻訳・執筆された同じレッスンファイル群が入っている。

---

## 1. 基礎とオペレーティングシステム (`basics/`)

コンピューティングの基礎、Git、OSファイルシステム、PowerShell/CMD.

| LC-ID | トピック |
|:------|:------|
| `LC-001` | [Expression](basics/ja/Expression.md) |
| `LC-002` | [Git — Version Control System](basics/ja/Git%20%E2%80%94%20Version%20Control%20System.md) |
| `LC-003` | [PowerShell](basics/ja/PowerShell.md) |
| `LC-004` | [Windows Command Prompt (cmd.exe)](basics/ja/Windows%20Command%20Prompt%20%28cmd.exe%29.md) |
| `LC-005` | [Linux File System](basics/OperatingSystem/ja/Linux%20File%20System.md) |
| `LC-006` | [Windows File System](basics/OperatingSystem/ja/Windows%20File%20System.md) |
| `LC-007` | [macOS File System](basics/OperatingSystem/ja/macOS%20File%20System.md) |

---

## 2. Linuxの基礎とセキュリティ (`linux/`)

シェル、ワークフロー、システム管理、ネットワーキング、ハードニング.

| LC-ID | トピック |
|:------|:------|
| `LC-008` | [Linux Structure — History, Philosophy, Architecture & Filesystem](linux/ja/01.%20Linux%20Structure%20%E2%80%94%20History%2C%20Philosophy%2C%20Architecture%20%26%20Filesystem.md) |
| `LC-009` | [Linux Distributions (Distros)](linux/ja/02.%20Linux%20Distributions%20%28Distros%29.md) |
| `LC-010` | [Introduction to Shell](linux/ja/03.%20Introduction%20to%20Shell.md) |
| `LC-011` | [Prompt Description & PS1 Customization](linux/ja/04.%20Prompt%20Description%20%26%20PS1%20Customization.md) |
| `LC-012` | [Getting Help — man, --help, apropos](linux/ja/05.%20Getting%20Help%20%E2%80%94%20man%2C%20--help%2C%20apropos.md) |
| `LC-013` | [System Information — Kernel, Hardware & Environment](linux/ja/06.%20System%20Information%20%E2%80%94%20Kernel%2C%20Hardware%20%26%20Environment.md) |
| `LC-014` | [Navigation — Moving Through the Linux Filesystem](linux/ja/07.%20Navigation%20%E2%80%94%20Moving%20Through%20the%20Linux%20Filesystem.md) |
| `LC-015` | [Working with Files & Directories](linux/ja/08.%20Working%20with%20Files%20%26%20Directories.md) |
| `LC-016` | [Editing Files — Nano & Vim](linux/ja/09.%20Editing%20Files%20%E2%80%94%20Nano%20%26%20Vim.md) |
| `LC-017` | [Find Files & Directories](linux/ja/10.%20Find%20Files%20%26%20Directories.md) |
| `LC-018` | [File Descriptors & Redirections](linux/ja/11.%20File%20Descriptors%20%26%20Redirections.md) |
| `LC-019` | [Filter Contents — Output Filtering & Text Processing](linux/ja/12.%20Filter%20Contents%20%E2%80%94%20Output%20Filtering%20%26%20Text%20Processing.md) |
| `LC-020` | [Regular Expressions (RegEx)](linux/ja/13.%20Regular%20Expressions%20%28RegEx%29.md) |
| `LC-021` | [Permission Management](linux/ja/14.%20Permission%20Management.md) |
| `LC-022` | [User Management](linux/ja/15.%20User%20Management.md) |
| `LC-023` | [Package Management](linux/ja/16.%20Package%20Management.md) |
| `LC-024` | [Service and Process Management](linux/ja/17.%20Service%20and%20Process%20Management.md) |
| `LC-025` | [Task Scheduling](linux/ja/18.%20Task%20Scheduling.md) |
| `LC-026` | [Network Services](linux/ja/19.%20Network%20Services.md) |
| `LC-027` | [Working with Web Services](linux/ja/20.%20Working%20with%20Web%20Services.md) |
| `LC-028` | [Backup and Restore](linux/ja/21.%20Backup%20and%20Restore.md) |
| `LC-029` | [File System Management](linux/ja/22.%20File%20System%20Management.md) |
| `LC-030` | [Containerization](linux/ja/23.%20Containerization.md) |
| `LC-031` | [Linux Networking — Interfaces & Routing](linux/ja/24.%20Linux%20Networking%20%E2%80%94%20Interfaces%20%26%20Routing.md) |
| `LC-032` | [Linux Networking — Diagnostics & Packet Analysis](linux/ja/25.%20Linux%20Networking%20%E2%80%94%20Diagnostics%20%26%20Packet%20Analysis.md) |
| `LC-033` | [Linux Security — Threat Model & Hardening Theory](linux/ja/26.%20Linux%20Security%20%E2%80%94%20Threat%20Model%20%26%20Hardening%20Theory.md) |
| `LC-034` | [Firewall Setup](linux/ja/27.%20Firewall%20Setup.md) |
| `LC-035` | [System Logs](linux/ja/28.%20System%20Logs.md) |
| `LC-036` | [Solaris — Linux Distributions vs Solaris](linux/ja/29.%20Solaris%20%E2%80%94%20Linux%20Distributions%20vs%20Solaris.md) |
| `LC-037` | [Shortcuts — Bash Tips & Tricks](linux/ja/30.%20Shortcuts%20%E2%80%94%20Bash%20Tips%20%26%20Tricks.md) |
| `LC-071` | [Neovim — Tips & Tricks](linux/Tips%20%26%20Tricks/ja/Neovim%20%E2%80%94%20Tips%20%26%20Tricks.md) |

---

## 3. コンピュータネットワークとプロトコル (`networking/`)

OSIモデル、TCP/IP、DNS、ARP、サブネッティング、無線セキュリティ.

| LC-ID | トピック |
|:------|:------|
| `LC-038` | [OSI Modelling](networking/ja/OSI%20Modelling.md) |
| `LC-039` | [TCP-IP Architecture & Socket Programming](networking/ja/TCP-IP%20Architecture%20%26%20Socket%20Programming.md) |
| `LC-040` | [IP Addressing & Subnetting](networking/ja/IP%20Addressing%20%26%20Subnetting.md) |
| `LC-041` | [DNS & Domain Name System Security](networking/ja/DNS%20%26%20Domain%20Name%20System%20Security.md) |
| `LC-042` | [ARP & Local Network Attacks](networking/ja/ARP%20%26%20Local%20Network%20Attacks.md) |
| `LC-043` | [Wireless 802.11 Security & Attacks](networking/ja/Wireless%20802.11%20Security%20%26%20Attacks.md) |

---

## 4. Webアプリケーションセキュリティ (`web/`)

HTTP/HTTPS、SQLi、XSS、CSRF、SSRF、LFI/RFI、アップロード、JWT/セッション攻撃.

| LC-ID | トピック |
|:------|:------|
| `LC-044` | [HTTP & cURL](web/HTTP/ja/1.%20HTTP%20%26%20cURL.md) |
| `LC-045` | [HTTP Requests, Responses & Status Codes](web/HTTP/ja/2.%20HTTP%20Requests%2C%20Responses%20%26%20Status%20Codes.md) |
| `LC-046` | [HTTP Headers & Security Headers](web/HTTP/ja/3.%20HTTP%20Headers%20%26%20Security%20Headers.md) |
| `LC-047` | [SQL Injection (SQLi)](web/Vulnerabilities/ja/1.%20SQL%20Injection%20%28SQLi%29.md) |
| `LC-048` | [Cross-Site Scripting (XSS)](web/Vulnerabilities/ja/2.%20Cross-Site%20Scripting%20%28XSS%29.md) |
| `LC-049` | [Cross-Site Request Forgery (CSRF)](web/Vulnerabilities/ja/3.%20Cross-Site%20Request%20Forgery%20%28CSRF%29.md) |
| `LC-050` | [Server-Side Request Forgery (SSRF)](web/Vulnerabilities/ja/4.%20Server-Side%20Request%20Forgery%20%28SSRF%29.md) |
| `LC-051` | [Command Injection & File Inclusion (LFI & RFI)](web/Vulnerabilities/ja/5.%20Command%20Injection%20%26%20File%20Inclusion%20%28LFI%20%26%20RFI%29.md) |
| `LC-052` | [File Upload Vulnerabilities & Web Shells](web/Vulnerabilities/ja/6.%20File%20Upload%20Vulnerabilities%20%26%20Web%20Shells.md) |
| `LC-053` | [Authentication, Session & JWT Attacks](web/Vulnerabilities/ja/7.%20Authentication%2C%20Session%20%26%20JWT%20Attacks.md) |

---

## 5. 暗号技術とPKI (`cryptography/`)

対称鍵/公開鍵暗号、ハッシュ、PKI、TLS 1.3.

| LC-ID | トピック |
|:------|:------|
| `LC-054` | [Symmetric Cryptography & Block Ciphers](cryptography/ja/1.%20Symmetric%20Cryptography%20%26%20Block%20Ciphers.md) |
| `LC-055` | [Asymmetric Cryptography & Key Exchange](cryptography/ja/2.%20Asymmetric%20Cryptography%20%26%20Key%20Exchange.md) |
| `LC-056` | [Hash Functions & Message Authentication](cryptography/ja/3.%20Hash%20Functions%20%26%20Message%20Authentication.md) |
| `LC-057` | [Public Key Infrastructure (PKI) & TLS 1.3](cryptography/ja/4.%20Public%20Key%20Infrastructure%20%28PKI%29%20%26%20TLS%201.3.md) |

---

## 6. 倫理的ハッキングとペネトレーションテスト (`ethical-hacking/`)

PTES手法、Nmap、Metasploit、権限昇格.

| LC-ID | トピック |
|:------|:------|
| `LC-058` | [Penetration Testing Methodology & Reconnaissance](ethical-hacking/ja/1.%20Penetration%20Testing%20Methodology%20%26%20Reconnaissance.md) |
| `LC-059` | [Port Scanning & Network Enumeration (Nmap)](ethical-hacking/ja/2.%20Port%20Scanning%20%26%20Network%20Enumeration%20%28Nmap%29.md) |
| `LC-060` | [Metasploit Framework & Exploitation](ethical-hacking/ja/3.%20Metasploit%20Framework%20%26%20Exploitation.md) |
| `LC-061` | [Privilege Escalation & Post-Exploitation](ethical-hacking/ja/4.%20Privilege%20Escalation%20%26%20Post-Exploitation.md) |

---

## 7. バイナリエクスプロイテーション (`binary-exploitation/`)

スタックバッファオーバーフロー、シェルコーディング、対策.

| LC-ID | トピック |
|:------|:------|
| `LC-062` | [Stack Buffer Overflow & Shellcoding](binary-exploitation/ja/Stack%20Buffer%20Overflow%20%26%20Shellcoding.md) |

---

## 8. リバースエンジニアリングとマルウェア分析 (`malware-analysis/`)

静的/動的トリアージ、サンドボックス化、x86/x64アセンブリ.

| LC-ID | トピック |
|:------|:------|
| `LC-063` | [Static Malware Analysis Fundamentals](malware-analysis/ja/1.%20Static%20Malware%20Analysis%20Fundamentals.md) |
| `LC-064` | [Dynamic Malware Analysis & Sandboxing](malware-analysis/ja/2.%20Dynamic%20Malware%20Analysis%20%26%20Sandboxing.md) |
| `LC-065` | [x86 & x64 Assembly for Reverse Engineering](malware-analysis/ja/3.%20x86%20%26%20x64%20Assembly%20for%20Reverse%20Engineering.md) |

---

## 9. モバイルアプリケーションセキュリティ (`mobile-security/`)

Android内部構造、サンドボックス化、Binder IPC、リバースエンジニアリング.

| LC-ID | トピック |
|:------|:------|
| `LC-066` | [Android Security Internals & Vulnerabilities](mobile-security/ja/Android%20Security%20Internals%20%26%20Vulnerabilities.md) |

---

## 10. セキュリティプログラミングとツール開発 (`programming-security/`)

ツール開発のための攻撃的なPythonとGo.

| LC-ID | トピック |
|:------|:------|
| `LC-067` | [Offensive Python & Go for Pentesters](programming-security/ja/Offensive%20Python%20%26%20Go%20for%20Pentesters.md) |

---

## 11. ソーシャルエンジニアリングと人的要因 (`social-engineering/`)

影響力の原理、経路、組織的防御.

| LC-ID | トピック |
|:------|:------|
| `LC-068` | [Social Engineering — Principles, Vectors & Defense](social-engineering/ja/Social%20Engineering%20%E2%80%94%20Principles%2C%20Vectors%20%26%20Defense.md) |

---

## 12. OSINT (`osint/`)

インテリジェンスのライフサイクル、OPSEC、調査フレームワーク.

| LC-ID | トピック |
|:------|:------|
| `LC-069` | [OSINT — Open Source Intelligence Framework & Techniques](osint/ja/OSINT%20%E2%80%94%20Open%20Source%20Intelligence%20Framework%20%26%20Techniques.md) |

---

## 13. ハードウェアとIoTセキュリティ (`hardware-iot/`)

UART/JTAG/SPI、ファームウェア抽出、CANバス.

| LC-ID | トピック |
|:------|:------|
| `LC-070` | [Hardware & IoT Security — Interfaces, Firmware & Automotive](hardware-iot/ja/Hardware%20%26%20IoT%20Security%20%E2%80%94%20Interfaces%2C%20Firmware%20%26%20Automotive.md) |

---

## 14. ブルーチームと防御セキュリティ (`blue-team/`)

SOCとログ分析、ネットワーク監視、スレットハンティング、インシデント対応とフォレンジック。

| LC-ID | トピック |
|:------|:------|
| `LC-072` | [SOC & Log Analysis](blue-team/ja/1.%20SOC%20%26%20Log%20Analysis.md) |
| `LC-073` | [Network Security Monitoring (Wireshark, Zeek, Suricata)](blue-team/ja/2.%20Network%20Security%20Monitoring%20%28Wireshark%2C%20Zeek%2C%20Suricata%29.md) |
| `LC-074` | [Threat Hunting & Detection Engineering (Sigma, YARA, ATT&CK)](blue-team/ja/3.%20Threat%20Hunting%20%26%20Detection%20Engineering%20%28Sigma%2C%20YARA%2C%20ATT%26CK%29.md) |
| `LC-075` | [Incident Response & Digital Forensics](blue-team/ja/4.%20Incident%20Response%20%26%20Digital%20Forensics.md) |

---

## 15. Active Directoryセキュリティ (`active-directory/`)

ドメイン、ドメインコントローラー、オブジェクト、グループポリシー、トラスト。

| LC-ID | トピック |
|:------|:------|
| `LC-076` | [Active Directory Fundamentals](active-directory/ja/1.%20Active%20Directory%20Fundamentals.md) |

---

## カバー状況

Zero2Rootはまだすべてを扱っていない。以下のトピックは現在ないので、自分の進路に必要ならほかの教材で学んでほしい。[CAREERS.ja.md](CAREERS.ja.md)の各職種にも、不足している内容を記載している。

| トピック | 状況 | 影響の大きい職種 |
|:---|:---|:---|
| Active Directory: 攻撃、防御、Windowsイベントログ (基礎はLC-076にある) | 一部あり | ペンテスター、レッドチーム、SOCアナリスト |
| クラウドセキュリティ (AWS、Azure、GCP、Kubernetes) | 予定あり | クラウドセキュリティエンジニア |
| DevSecOpsとセキュアSDLC (CIでのスキャン、サプライチェーン) | 予定あり | AppSec・DevSecOpsエンジニア |
| AIとLLMのセキュリティ | 予定あり | AppSec、レッドチーム |
| GRC (リスク、ISO 27001、NIST CSF、個人情報保護法) | 予定あり | GRCアナリスト |
| APIセキュリティ、ヒープのエクスプロイト、ファジング、iOS | 未定 | Webペンテスター、脆弱性リサーチャー、モバイル |

---

## 参考文献ライブラリ

このリポジトリのすべての内容は、`~/Documents/Books/`にローカル保存された技術参考書に基づいて書かれている。各レッスンに対応した完全なカタログは[BOOKS.ja.md](BOOKS.ja.md)を参照。

---

## 法的免責事項

このリポジトリに含まれるすべてのドキュメント、コマンド、攻撃ベクターは、教育目的、防御的な監査、そして許可されたペネトレーションテストのためだけのものだ。この資料の使用によって生じた不正な行為、設定ミス、損害について、著者は一切の責任を負わない。

---

## 著者と貢献

- メンテナー: `kodoktheGr3at`
- GitHub: [github.com/Kodokthegr3at](https://github.com/Kodokthegr3at)
- リポジトリ: [github.com/Kodokthegr3at/Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
- フィードバック、改善提案、プルリクエストを歓迎する。
