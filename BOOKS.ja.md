**言語:** [English](BOOKS.md) | [Bahasa Indonesia](BOOKS.id.md) | [日本語](BOOKS.ja.md)

# 参考文献ライブラリ: `~/Documents/Books/`

> **Zero2Root** | カリキュラムIDに対応したローカル書籍カタログ
> 2026年 | すべてのパスは `/home/kodok/Documents/Books/` からの相対パス

このカタログは、ローカルライブラリ内のすべてのPDFをZero2Rootのレッスンに対応付けている。各`LC-xxx`のノートを読む前後に、対応する章を読むこと。

---

## Linux & シェル

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| Brian Ward, *How Linux Works (第3版)* | `CyberSec/Linux/203.How Linux Works_ What Every Superuser Should Know.pdf` | LC-005, LC-008-035 | カーネル空間とユーザー空間、`/proc`/`/sys`、ブート、ストレージ、ネットワークスタック、systemd、セキュリティ |
| William Shotts, *The Linux Command Line (第2版)* | `CyberSec/Linux/The Linux Command Line.pdf` | LC-008-020, LC-037, LC-071 | シェル文法、ナビゲーション、パイプライン、vim、スクリプティング、ジョブ制御 |
| Jeffrey Friedl, *Mastering Regular Expressions (第3版)* | `CyberSec/Linux/OReilly.Mastering.Regular.Expressions.3rd.Edition.www.EBooksWorld.ir.pdf` | LC-001, LC-020, LC-037 | NFA/DFA、貪欲マッチ、バックトラッキング、ReDoS、grep/sed/awkパターン |

---

## ネットワーキング

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| Kurose & Ross, *Computer Networking (第6版)* | `CyberSec/Networking/computernetworking.pdf` | LC-038-042, LC-044 | OSI/TCP-IP、遅延・損失・スループット、HTTP/DNS、ルーティング、トランスポート層 |
| William Stallings, *Network Security Essentials (第4版)* | `CyberSec/Networking/Network-security-essentials-4th-edition-william-stallings.pdf` | LC-033-034, LC-038, LC-041-043, LC-054-057 | 機密性・完全性・認証、ファイアウォール、IDS、TLS、無線セキュリティ |
| Christian Benvenuti, *Understanding Linux Network Internals* | `CyberSec/Networking/Understanding Linux Network Internals (2005).pdf` | LC-026, LC-031-032, LC-034 | sk_buff、Netfilter、ルーティングキャッシュ、ソケット層、ドライバとのやり取り |
| W. Richard Stevens, *UNIX Network Programming Vol.1 (第3版)* | `CyberSec/Networking/UNIX Network Programming Volume 1, 3rd edition - W. Richard Stevens.pdf` | LC-018, LC-026, LC-031, LC-039, LC-067 | ソケットAPI、TCPステートマシン、I/O多重化、エコーサーバー |
| Matthew Gast, *802.11 Wireless Networks (第2版)* | `CyberSec/Networking/802_11_Wireless_Networks__The_Definitive_Guide__O__039_Reilly_Networking_.pdf` | LC-043 | フレームタイプ、WPA2の4-wayハンドシェイク、PMKID、チャネル構造 |

---

## Webアプリケーションセキュリティ

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| Stuttard & Pinto, *The Web Application Hacker's Handbook (第2版)* | `CyberSec/Web App/The Web Application Hackers Handbook-Honest.pdf` | LC-044-052 | HTTP攻撃対象領域、SQLi、XSS、CSRF、認証の欠陥、ロジックバグ |
| Michal Zalewski, *The Tangled Web* | `CyberSec/Web App/thetangledweb_ebook.pdf` | LC-044-053 | ブラウザセキュリティモデル、SOP、CSP、Cookie、現代のWebの癖 |

---

## 暗号技術

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| David Wong, *Real-World Cryptography (2021)* | `CyberSec/Cryptography/Real-World-Cryptography-12.10.2021.-.pdf` | LC-053-057 | 対称鍵/AEAD、RSA/ECC、ハッシュ、署名、TLS 1.3、実務上の落とし穴 |

---

## Ethical Hacking & Exploitation

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| Peter Kim, *The Hacker Playbook 3* | `CyberSec/Ethical Hacking/The Hacker Playbook 3 - Practical Guide To Penetration Testing by Peter Kim.pdf` | LC-058-061 | 偵察、スキャン、エクスプロイト配送、権限昇格のプレイブック |
| Georgia Weidman, *Penetration Testing* | `CyberSec/Ethical Hacking/Penetration Testing - A hands-on introduction to Hacking.pdf` | LC-058-061 | ラボ構築、方法論、Metasploitの基礎、報告 |
| *Gray Hat Hacking* | `CyberSec/Handbook/gray-hat-hacking.pdf` | LC-003-004, LC-006, LC-061-062 | エクスプロイト開発のためのOS内部構造、Windows/Linuxの権限昇格 |
| Kennedy et al., *Metasploit: The Penetration Tester's Guide* | `CyberSec/Android/Metasploit - The Penetration Tester's Guide.pdf` | LC-060 | MSFアーキテクチャ、Meterpreter、モジュール開発 |
| *The Shellcoder's Handbook (第2版)* | `CyberSec/Handbook/Wiley.The.Shellcoders.Handbook.2nd.Edition.Aug.2007.pdf` | LC-062 | スタックオーバーフロー、ヒープ、シェルコード、保護機構の回避 |
| Erickson, *Hacking: The Art of Exploitation* | `CyberSec/Ethical Hacking/Hacking - The Next Generation.pdf` | LC-062 | Cのメモリモデル、アセンブリ、エクスプロイテーションの考え方 |

---

## マルウェアとリバースエンジニアリング

| 書籍 | パス | カリキュラムID | 主要な技術トピック |
|:-----|:-----|:---------------|:---------------------|
| Sikorski & Honig, *Practical Malware Analysis* | `CyberSec/Malware/practicalmalwareanalysis.pdf` | LC-063-065 | 静的/動的トリアージ、PE形式、デバッグ、パッカー |
| Andriesse, *Practical Binary Analysis* | `CyberSec/Malware/Practical Binary Analysis 1st Edition (2019).pdf` | LC-063-064 | ELF/PE解析、シンボリック実行の入門、バイナリリフティング |
| Dang et al., *Practical Reverse Engineering* | `CyberSec/Reverse Engineeering/Practical Reverse Engineering.pdf` | LC-065 | x86/x64/ARMの逆アセンブル、呼び出し規約、難読化 |
| *Rootkits and Bootkits* | `CyberSec/Malware/Rootkits and Bootkits - Reversing Modern Malware And Next Generation Threats (2019).pdf` | LC-063+ | カーネルモードの永続化、ブートチェーン |

---

## モバイル、プログラミング、OSINT、ハードウェア

| 書籍 | パス | カリキュラムID |
|:-----|:-----|:---------------|
| Elenkov, *Android Security Internals* | `CyberSec/Android/Android_Security_Internals-An_In-Depth_Guide_to_Android_s_Security_Architecture.pdf` | LC-066 |
| Seitz & Arnold, *Black Hat Python (第2版)* | `CyberSec/Programming/Black Hat Python, 2nd Edition (Justin Seitz Tim Arnold) (Z-Library).pdf` | LC-067 |
| Steele et al., *Black Hat Go* | `CyberSec/Programming/Black Hat Go [Tom Steele, Chris Patten & Dan Kottmann].pdf` | LC-067 |
| Hadnagy, *Social Engineering (第2版)* | `CyberSec/Social Engineering/socialengineering_thescienceofhumanhacking_2ndedition.pdf` | LC-068 |
| Mitnick, *The Art of Deception* | `CyberSec/Social Engineering/The Art of Deception.pdf` | LC-068 |
| Gray, *Practical Social Engineering* | `CyberSec/Social Engineering/practical_social_engineering_a_primer_for_the_ethical_hacker_171850098x.pdf` | LC-068 |
| Akhgar et al., *OSINT Methods and Tools* | `CyberSec/OSINT/Open Source Intelligence Methods and Tools.pdf` | LC-069 |
| *Hardware Hacking Handbook* | `CyberSec/Hardware/The Hardware Hacking Handbook.pdf` | LC-070 |
| *Practical IoT Hacking* | `CyberSec/Hardware/Practical IoT Hacking_ The Definitive Guide to Attacking the Internet of Things.pdf` | LC-070 |
| *The Car Hacker's Handbook* | `CyberSec/Hardware/thecarhackershandbook.pdf` | LC-070 |
| *IoT Hacker's Handbook (Gupta)* | `CyberSec/Handbook/The IoT Hackers Handbook A Practical Guide to Hacking the Internet of Things by Aditya Gupta (z-lib.org).pdf` | LC-070 |

---

## プログラミングの基礎

| 書籍 | パス | カリキュラムID |
|:-----|:-----|:---------------|
| K. N. King, *C Programming: A Modern Approach (第2版)* | `Programming/C /K. N. King - C Programming_ A Modern Approach Second Edition (2008, W. W. Norton & Company) - libgen.li.pdf` | LC-001, LC-062, LC-065 |
| Al Sweigart, *Automate the Boring Stuff with Python* | `Programming/Python/Automate the Boring Stuff with Python.pdf` | LC-001, LC-067 |
| Scott Meyers, *Effective Modern C++* | `Programming/ C++/Effective-Modern-C++.pdf` | LC-001 |

---

> `LC-001`から`LC-082`までの順序立てられた学習パスは[ROADMAP.ja.md](ROADMAP.ja.md)を参照。
