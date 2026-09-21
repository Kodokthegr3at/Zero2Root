# Linuxファイルシステム

> LearnCybersecurity | 基礎シリーズ | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-005` | **フェーズ0:** 基礎
> **推定学習時間:** 5-6時間 | **レベル:** 初級
> **前提:** LC-001
> **書籍対応:** Brian Ward, How Linux Works 第3-5章（FHS、/proc、/sys）; William Shotts, The Linux Command Line 第3章
<!-- LC-CURRICULUM-END -->

## 目次

| # | トピック |
|---|---------|
| 1 | Linuxファイルシステムとは |
| 2 | ディレクトリツリー全体 |
| 3 | ルートディレクトリ（`/`） |
| 4 | `/bin` — 必須コマンドバイナリ |
| 5 | `/sbin` — システム管理バイナリ |
| 6 | `/etc` — システム設定ファイル |
| 7 | `/home` — ユーザーのホームディレクトリ |
| 8 | `/root` — rootユーザーのホーム |
| 9 | `/var` — 可変データとログ |
| 10 | `/tmp` — 一時ファイル |
| 11 | `/usr` — Unix共有リソース |
| 12 | `/lib` — 共有ライブラリ |
| 13 | `/dev` — デバイスファイル |
| 14 | `/proc` — プロセスとカーネル情報 |
| 15 | `/sys` — ハードウェアとカーネル情報 |
| 16 | `/mnt` と `/media` — マウントポイント |
| 17 | `/opt` — オプションソフトウェア |
| 18 | `/boot` — ブートファイル |
| 19 | `/srv` — サーバーサービスデータ |
| 20 | セキュリティノート: 機微なディレクトリと防御的ハードニング |
| 21 | 実践ワークフロー |

---

## 1. 概要: Linuxファイルシステムとは

Linuxファイルシステムは、システム上のすべてのファイルとディレクトリを整理する階層構造である。C:、D:のように複数のドライブを使うWindowsとは違い、Linuxは`/`（ルート）から始まる単一のディレクトリツリーを使う。

Linuxではハードウェア、プロセス、設定、ユーザーデータといったすべてのものがファイルとして表現され、この階層に整理される。この原則は「すべてはファイルである」として知られている。

この構造を規定する標準はFHS（Filesystem Hierarchy Standard）と呼ばれ、各主要ディレクトリの目的と内容を定義することで、Linuxディストリビューション間で構造の一貫性を保っている。

セキュリティにとって重要な理由:

- 設定ファイルがどこにあるかを知ることは、偵察の対象になる。
- どのディレクトリが書き込み可能かを理解することは、権限昇格の手がかりになる。
- ログの場所を知ることは、フォレンジックや監査にとって重要である。
- バイナリの場所を知ることは、横展開や永続化にとって重要である。

---

## 2. ファイルツリー: ディレクトリ構造全体

```
/                          ← Root of the entire file system
│
├── bin/                   ← Essential user binaries (ls, cp, cat, bash...)
├── sbin/                  ← System admin binaries (ifconfig, fdisk, reboot...)
├── etc/                   ← System-wide configuration files
│   ├── passwd             ← User account info
│   ├── shadow             ← Encrypted passwords
│   ├── group              ← Group definitions
│   ├── hosts              ← Static hostname resolution
│   ├── fstab              ← Filesystem mount table
│   ├── crontab            ← System-wide cron jobs
│   ├── sudoers             ← Sudo permissions
│   ├── ssh/               ← SSH daemon config
│   │   └── sshd_config
│   ├── apt/               ← APT package manager config
│   │   └── sources.list
│   ├── nginx/              ← Nginx web server config
│   ├── apache2/            ← Apache web server config
│   ├── systemd/            ← Systemd unit files
│   │   └── system/
│   ├── cron.d/             ← Additional cron jobs
│   ├── cron.daily/
│   ├── cron.weekly/
│   └── cron.monthly/
│
├── home/                  ← Home directories for regular users
│   ├── alice/              ← Alice's personal directory
│   │   ├── Desktop/
│   │   ├── Documents/
│   │   ├── Downloads/
│   │   ├── .bashrc        ← User shell config (hidden)
│   │   ├── .bash_history  ← Command history (hidden)
│   │   └── .ssh/           ← SSH keys (hidden)
│   │       ├── id_rsa     ← Private key
│   │       ├── id_rsa.pub ← Public key
│   │       └── authorized_keys
│   └── bob/
│
├── root/                  ← Home directory for root user
│   ├── .bashrc
│   ├── .bash_history
│   └── .ssh/
│
├── var/                   ← Variable data (changes frequently)
│   ├── log/                ← System & application logs
│   │   ├── syslog         ← General system log
│   │   ├── auth.log       ← Authentication log
│   │   ├── apache2/        ← Apache logs
│   │   │   ├── access.log
│   │   │   └── error.log
│   │   ├── nginx/          ← Nginx logs
│   │   └── mysql/          ← MySQL logs
│   ├── www/                ← Web server document root
│   │   └── html/           ← Default web files
│   ├── mail/                ← Mail spool
│   ├── spool/               ← Print & cron spools
│   │   └── cron/            ← Per-user crontabs
│   └── lib/                 ← Persistent application data
│
├── tmp/                   ← Temporary files (cleared on reboot)
│
├── usr/                   ← Unix Shared Resources (read-only)
│   ├── bin/                ← Non-essential user binaries
│   ├── sbin/                ← Non-essential system binaries
│   ├── lib/                 ← Libraries for /usr/bin & /usr/sbin
│   ├── local/                ← Locally installed software
│   │   ├── bin/
│   │   ├── lib/
│   │   └── share/
│   ├── share/                ← Architecture-independent data
│   │   ├── man/              ← Manual pages
│   │   └── doc/              ← Documentation
│   └── include/               ← C header files
│
├── lib/                   ← Shared libraries for /bin & /sbin
│   ├── x86_64-linux-gnu/
│   └── modules/            ← Kernel modules
│
├── lib64/                 ← 64-bit shared libraries
│
├── dev/                   ← Device files (virtual)
│   ├── sda                ← First hard disk
│   ├── sda1               ← First partition of sda
│   ├── tty                ← Terminal devices
│   ├── null               ← Null device (discards all input)
│   ├── zero               ← Zero device (outputs null bytes)
│   ├── random              ← Random number generator
│   └── urandom             ← Non-blocking random generator
│
├── proc/                  ← Virtual FS: process & kernel info
│   ├── 1/                  ← Info for PID 1 (systemd)
│   │   ├── cmdline        ← Command line of the process
│   │   ├── status         ← Process status
│   │   └── fd/              ← Open file descriptors
│   ├── cpuinfo             ← CPU information
│   ├── meminfo              ← Memory information
│   ├── net/                 ← Network information
│   │   └── tcp             ← Active TCP connections
│   ├── version              ← Kernel version
│   └── mounts               ← Mounted filesystems
│
├── sys/                   ← Virtual FS: hardware & kernel interface
│   ├── class/
│   ├── block/
│   └── bus/
│
├── mnt/                   ← Temporary manual mount point
│
├── media/                 ← Auto-mounted removable media
│   ├── cdrom/
│   └── usb/
│
├── opt/                   ← Optional/third-party software
│   ├── google/
│   └── lampp/
│
├── boot/                  ← Boot loader & kernel files
│   ├── grub/                ← GRUB bootloader config
│   │   └── grub.cfg
│   ├── vmlinuz              ← Compressed Linux kernel
│   └── initrd.img           ← Initial RAM disk image
│
├── srv/                   ← Data served by the system
│   ├── http/                ← Web server data
│   └── ftp/                 ← FTP server data
│
├── run/                   ← Runtime data (PID files, sockets)
│
└── snap/                  ← Snap package mount points
```

---

## 3. `/` — ルートディレクトリ

`/`はLinuxファイルシステム階層のいちばん上にあるディレクトリで、すべてのパスの出発点である。他のすべてのディレクトリはこのルートから枝分かれしている。ルートディレクトリ直下への完全な書き込み権限を持つのはrootユーザーだけである。

```bash
# Navigate to root
$ cd /

# List root directory contents
$ ls -la /

drwxr-xr-x  20 root root 4096 Jun  1 00:00 .
drwxr-xr-x  20 root root 4096 Jun  1 00:00 ..
drwxr-xr-x   2 root root 4096 Jun  1 00:00 bin
drwxr-xr-x   3 root root 4096 Jun  1 00:00 boot
drwxr-xr-x  18 root root 3800 Jun  1 00:00 dev
drwxr-xr-x 135 root root 4096 Jun  1 00:00 etc
drwxr-xr-x   3 root root 4096 Jun  1 00:00 home
...
```

---

## 4. `/bin` — 必須ユーザーバイナリ

`/bin`には、システムがシングルユーザーモードやリカバリーモードにあるときでも、全ユーザーが必要とする必須バイナリが入っている。日常的に使う最も基本的なコマンドはここにある。

```bash
# Common binaries found in /bin
ls /bin

bash    cat    chmod   chown   cp     date
echo    grep   gzip    kill    ln     ls
mkdir   mount  mv      nano    ping   ps
pwd     rm     rmdir   sh      sleep  tar
touch   uname  vi      which   ...
```

| バイナリ | 機能 |
|---------|------|
| `bash` | 主要なシェル |
| `ls` | ディレクトリの内容を一覧表示 |
| `cp` | ファイルをコピー |
| `mv` | ファイルを移動/リネーム |
| `rm` | ファイルを削除 |
| `cat` | ファイルの内容を表示 |
| `grep` | ファイル内のテキストを検索 |
| `chmod` | ファイル権限を変更 |
| `ping` | ネットワーク接続を確認 |

---

## 5. `/sbin` — システム管理バイナリ

`/sbin`には、通常rootユーザーだけが実行するシステム管理用のバイナリが入っている。ディスク管理、ネットワーク設定、システムメンテナンス用のツールを持つ。

```bash
# Common binaries in /sbin
ls /sbin

fdisk      fsck       ifconfig   init       ip
iptables   mkfs       mount      reboot     route
shutdown   sshd       swapon     umount     useradd
userdel    usermod    ...
```

| バイナリ | 機能 |
|---------|------|
| `ifconfig` | ネットワークインターフェースを設定 |
| `iptables` | ファイアウォール管理 |
| `fdisk` | ディスクパーティション管理 |
| `useradd` | 新規ユーザーを追加 |
| `reboot` | システムを再起動 |
| `fsck` | ファイルシステムの検査と修復 |

---

## 6. `/etc` — システム設定ファイル

`/etc`はセキュリティの観点から最も重要なディレクトリである。ユーザーアカウント、パスワード、ネットワーク設定からサービス設定まで、すべてのシステム設定ファイルが入っている。`/etc`の内容はrootユーザーだけが変更すべきである。

```bash
# List /etc contents
$ ls /etc

# ── CRITICAL FILES IN /etc ──────────────────────────────────

# User accounts (readable by all)
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
alice:x:1000:1000:Alice:/home/alice:/bin/bash

# Encrypted passwords (root only!)
$ sudo cat /etc/shadow
root:$6$xyz...:18000:0:99999:7:::

# Group definitions
$ cat /etc/group
sudo:x:27:alice
docker:x:999:alice

# Static hostname resolution
$ cat /etc/hosts
127.0.0.1   localhost
10.10.10.1  target.htb

# Sudo permissions
$ sudo cat /etc/sudoers

# SSH server configuration
$ cat /etc/ssh/sshd_config

# Network interfaces (Debian/Ubuntu)
$ cat /etc/network/interfaces

# DNS resolver config
$ cat /etc/resolv.conf

# System hostname
$ cat /etc/hostname
```

### `/etc`内の重要ファイル

| ファイル | 内容 | ペンテストでの価値 |
|---------|------|---------------------|
| `/etc/passwd` | ユーザーアカウント情報 | 高 |
| `/etc/shadow` | 暗号化されたパスワード | 最重要 |
| `/etc/group` | グループ定義 | 中 |
| `/etc/sudoers` | sudo権限 | 最重要 |
| `/etc/hosts` | 静的ホスト名解決 | 中 |
| `/etc/ssh/sshd_config` | SSH設定 | 高 |
| `/etc/crontab` | システムのcronジョブ | 高 |
| `/etc/fstab` | ファイルシステムのマウントテーブル | 中 |
| `/etc/resolv.conf` | DNS設定 | 中 |

ペンテストのメモ: `/etc/passwd`と`/etc/shadow`は権限昇格における主要なターゲットである。`/etc/shadow`が読めるなら、`john`や`hashcat`のようなツールでパスワードハッシュをクラックできる。

---

## 7. `/home` — ユーザーのホームディレクトリ

`/home`には、各一般ユーザーの個人用ディレクトリが入っている。各ユーザーは自分専用のサブディレクトリ（`/home/username`）を持ち、そこに個人ファイル、アプリケーション設定、隠しファイル（ドットファイル）を保存する。

```bash
# List all user home directories
$ ls /home
alice  bob  charlie

# Explore a user's home directory
$ ls -la /home/alice

drwxr-xr-x  alice alice  .
drwxr-xr-x  root  root   ..
-rw-------  alice alice  .bash_history   ← command history!
-rw-r--r--  alice alice  .bashrc
-rw-r--r--  alice alice  .profile
drwx------  alice alice  .ssh/           ← SSH keys!
drwxr-xr-x  alice alice  Desktop/
drwxr-xr-x  alice alice  Documents/
drwxr-xr-x  alice alice  Downloads/

# High-value files in /home for pentesting
$ cat /home/alice/.bash_history     # command history
$ cat /home/alice/.ssh/id_rsa       # private SSH key
$ ls /home/alice/.ssh/authorized_keys
```

### `/home`内の主要な隠しファイル（ドットファイル）

| ファイル | 内容 |
|---------|------|
| `.bashrc` | Bashシェルの設定 |
| `.bash_history` | コマンド履歴 |
| `.bash_profile` | ログインシェルの設定 |
| `.ssh/id_rsa` | SSH秘密鍵 |
| `.ssh/authorized_keys` | 許可されたSSH公開鍵 |
| `.profile` | 環境変数 |
| `.gitconfig` | Gitの設定 |

---

## 8. `/root` — rootユーザーのホーム

`/root`はスーパーユーザー（root）のホームディレクトリである。ホームが`/home/username`にある一般ユーザーとは違い、rootは`/root`に専用のディレクトリを持つ。このディレクトリはrootのみがアクセスできる。

```bash
# Access root's home (requires root)
$ sudo ls -la /root

drwx------  root root  .
drwxr-xr-x  root root  ..
-rw-------  root root  .bash_history   ← root's command history!
-rw-r--r--  root root  .bashrc
drwx------  root root  .ssh/
-rw-------  root root  .ssh/id_rsa

# Check root's command history (privilege escalation gold!)
$ sudo cat /root/.bash_history
```

ペンテストのメモ: `/root`へのアクセスを得るということは、システムが完全に侵害されたことを意味する。ここの`.bash_history`には、管理者が実行したパスワード、機微なコマンド、横展開の痕跡が残っていることがある。

---

## 9. `/var` — 可変データとログ

`/var`には、通常のシステム運用中に頻繁に変化するデータ、特にログ、スプール、ランタイムデータベース、Webサーバーファイルが入っている。名前の「var」は「variable（可変）」に由来する。ここで最もセキュリティ上重要なディレクトリは`/var/log`である。

```bash
# ── LOGS — /var/log ─────────────────────────────────────────

# General system log
$ tail -f /var/log/syslog

# Authentication log (login attempts, sudo usage)
$ tail -f /var/log/auth.log
$ grep "Failed password" /var/log/auth.log
$ grep "Accepted password" /var/log/auth.log

# Apache web server logs
$ tail -f /var/log/apache2/access.log
$ tail -f /var/log/apache2/error.log

# Nginx logs
$ tail -f /var/log/nginx/access.log

# Kernel messages
$ tail -f /var/log/kern.log

# ── WEB FILES — /var/www ────────────────────────────────────

# Default Apache web root
$ ls /var/www/html/
$ cat /var/www/html/index.html

# ── CRON SPOOLS — /var/spool/cron ───────────────────────────
$ sudo ls /var/spool/cron/crontabs/
```

### `/var`の主要サブディレクトリ

| ディレクトリ | 内容 |
|-------------|------|
| `/var/log` | システムとアプリケーションのログ |
| `/var/www` | Webサーバーファイル |
| `/var/spool` | 印刷とcronのキュー |
| `/var/lib` | 永続的なアプリケーションデータ |
| `/var/mail` | ユーザーのメールボックス |
| `/var/tmp` | 永続的な一時ファイル |

---

## 10. `/tmp` — 一時ファイル

`/tmp`はプロセスやユーザーが作成する一時ファイル用のディレクトリである。中身は再起動時に自動的に消去される。全ユーザーが`/tmp`への読み書きができるため、悪意ある活動の格好の置き場所になりやすい。

```bash
# /tmp is world-writable
$ ls -la / | grep tmp
drwxrwxrwt  root root  tmp     ← "t" = sticky bit

# Common pentesting uses of /tmp
$ ls -la /tmp/                  # check for suspicious files

# Common attacker patterns in /tmp
# - Dropped payloads: /tmp/shell.elf
# - Compiled exploits: /tmp/exploit
# - Exfiltration staging: /tmp/loot.tar.gz
```

ペンテストのメモ: `/tmp`は誰でも書き込めるため、ペイロードを置く標準的な場所になっている。ポストエクスプロイテーションの際は、他の攻撃者が残した痕跡や不審な活動がないか、常に`/tmp`を確認する。

---

## 11. `/usr` — Unix共有リソース

`/usr`には、ユーザーが使うプログラムとデータの大部分が入っている。ほとんどのLinuxシステムで最大のディレクトリだ。最小限のバイナリしか持たない`/bin`とは違い、`/usr/bin`は一般ユーザー向けの必須ではないバイナリすべてを含む。

```bash
$ ls /usr
bin  include  lib  lib64  local  sbin  share  src

# Most installed programs go here
$ ls /usr/bin | head -20
nmap  python3  gcc  vim  curl  wget  ssh  ...

# Locally compiled/installed software
$ ls /usr/local/bin

# Man pages
$ ls /usr/share/man/

# Documentation
$ ls /usr/share/doc/
```

| ディレクトリ | 内容 |
|-------------|------|
| `/usr/bin` | 必須ではないユーザーバイナリ |
| `/usr/sbin` | 必須ではないシステムバイナリ |
| `/usr/lib` | `/usr/bin`用のライブラリ |
| `/usr/local` | ローカルでビルドされたソフトウェア |
| `/usr/share` | アーキテクチャに依存しないデータ |
| `/usr/include` | Cヘッダーファイル |

---

## 12. `/lib` — 共有ライブラリ

`/lib`には、`/bin`や`/sbin`のバイナリが必要とする共有ライブラリ（Windowsの.dllファイルに相当）が入っている。また、`/lib/modules/`にカーネルモジュールも含まれる。

```bash
# List shared libraries
$ ls /lib/x86_64-linux-gnu/ | head -10

# List loaded kernel modules
$ lsmod

# List kernel modules directory
$ ls /lib/modules/$(uname -r)/
```

---

## 13. `/dev` — デバイスファイル

`/dev`には、システムに接続されたすべてのハードウェアを仮想的に表現したデバイスファイルが入っている。Linuxでは、ディスクや端末、`/dev/null`のような特殊デバイスも含め、すべてのハードウェアがファイルとして扱われる。

```bash
# List block devices (hard drives, partitions)
$ lsblk
$ ls /dev/sd*
/dev/sda   /dev/sda1   /dev/sda2

# Special devices
$ ls /dev/null       # discards everything written to it
$ ls /dev/zero       # produces infinite null bytes
$ ls /dev/random     # generates random bytes (blocking)
$ ls /dev/urandom    # generates random bytes (non-blocking)
$ ls /dev/tty        # current terminal

# Useful pentesting tricks
$ cat /dev/null        # empty output
$ dd if=/dev/zero of=file.bin bs=1M count=10  # create 10MB zero file
$ cat /dev/urandom | base64 | head -c 32      # generate random string
```

### 重要なデバイスファイル

| デバイス | 機能 |
|---------|------|
| `/dev/sda` | 最初のハードディスク |
| `/dev/sda1` | sdaの最初のパーティション |
| `/dev/null` | 出力をすべて破棄 |
| `/dev/zero` | 無限にヌルバイトを出力 |
| `/dev/random` | 乱数生成器 |
| `/dev/tty` | 現在の端末 |

---

## 14. `/proc` — プロセスとカーネル情報

`/proc`はディスク上の実在するディレクトリではなく、カーネルと実行中プロセスの情報にアクセスするための仮想ファイルシステムである。各プロセスはそのPIDにちなんだ名前のサブディレクトリを持つ。フォレンジックやデバッグに非常に役立つ。

```bash
# View CPU information
$ cat /proc/cpuinfo

# View memory information
$ cat /proc/meminfo

# View kernel version
$ cat /proc/version
Linux version 5.15.0-91-generic

# View all running processes
$ ls /proc/ | grep -E '^[0-9]+'

# Inspect a specific process (PID 1 = systemd)
$ cat /proc/1/cmdline
$ cat /proc/1/status
$ ls /proc/1/fd/             # open file descriptors

# View active network connections
$ cat /proc/net/tcp

# View mounted filesystems
$ cat /proc/mounts

# System uptime
$ cat /proc/uptime
```

---

## 15. `/sys` — ハードウェアとカーネルの情報

`/sys`はもう一つの仮想ファイルシステムで、カーネルの構造とハードウェアへのインターフェースを提供する。`/proc`よりも構造化されており、ハードウェア設定をリアルタイムで確認・変更するのに使われる。

```bash
# View block devices
$ ls /sys/block/

# View network interfaces
$ ls /sys/class/net/
eth0  lo  wlan0

# View CPU details
$ ls /sys/devices/system/cpu/
```

---

## 16. `/mnt` と `/media` — マウントポイント

- `/mnt`は、管理者が手動で一時的にマウントする際に使う（USBドライブ、NFS共有、ISOイメージなど）。
- `/media`は、リムーバブルメディア（USB、CD-ROM）をシステムが自動でマウントする際に使う。

```bash
# Manually mount a USB drive
$ sudo mount /dev/sdb1 /mnt/usb

# Unmount
$ sudo umount /mnt/usb

# Check mounted filesystems
$ mount | grep /mnt
$ df -h

# Auto-mounted USB usually appears here
$ ls /media/username/
```

---

## 17. `/opt` — オプションソフトウェア

`/opt`は、ディストリビューションのパッケージマネージャーが管理しないサードパーティやオプションのソフトウェア用に使われる。ここにインストールされるソフトウェアは、通常自分専用のサブディレクトリ内に完結している。

```bash
# Common contents of /opt
$ ls /opt
google/   lampp/   BurpSuite/   vmware/

# Example: Burp Suite installed in /opt
$ ls /opt/BurpSuite/
BurpSuitePro  jre/  burpsuite_pro.jar
```

---

## 18. `/boot` — ブートファイル

`/boot`には、Linuxカーネル、初期RAMディスク（initrd）、GRUBブートローダーの設定など、システムを起動するために必要なすべてのファイルが入っている。何をしているか分かっていない限り、このディレクトリの内容は変更しないこと。

```bash
$ ls /boot

grub/           # GRUB bootloader config directory
vmlinuz-5.15.0  # Compressed Linux kernel
initrd.img      # Initial RAM disk image
config-5.15.0   # Kernel build configuration
System.map      # Kernel symbol table

# View GRUB configuration
$ cat /boot/grub/grub.cfg

# View current kernel version
$ uname -r
5.15.0-91-generic
```

---

## 19. `/srv` — サーバーサービスデータ

`/srv`には、システム上で動くサーバーサービスが提供するデータ（Webファイル、FTP、リポジトリデータなど）が入っている。使い方はディストリビューションによって異なる。

```bash
$ ls /srv
http/   ftp/   git/

# Example: web files served from /srv
$ ls /srv/http/
index.html  assets/  uploads/
```

---

## 20. セキュリティノート: 機微なディレクトリと防御的ハードニング

以下のディレクトリは攻撃者にとっても防御側にとっても価値が高い。このリストは、自分が管理するシステムの権限監査、監視、ハードニングのために使うものであり、権限昇格の攻略ガイドではない。

```bash
# ── HIGH-VALUE PATHS (inventory for defenders) ───────────────
/etc/passwd             # usernames & shells
/etc/shadow             # password hashes (root only) — mode 640, group shadow
/etc/sudoers            # sudo privileges — validate with visudo
/home/*/.bash_history   # may contain secrets — restrict perms, clear carefully
/home/*/.ssh/           # SSH keys — mode 700 dir / 600 private keys
/var/www/html/          # web roots — no secrets in tree; use secrets manager
/var/log/auth.log       # auth telemetry — protect integrity (append-only / remote)
/tmp/ /var/tmp/ /dev/shm/  # world-writable — sticky bit, noexec where policy allows
/etc/cron*/ /etc/systemd/system/  # persistence surfaces — inventory & alert on changes
```

### 防御的ハードニングの重点

| コントロール | 対応 |
|-------------|------|
| パーミッション | `/etc/shadow`とSSH鍵に厳格なモードを設定 |
| Sudo | `visudo`、最小権限のsudoers、広範なNOPASSWDを避ける |
| 誰でも書き込み可能な場所 | sticky bit、ポリシーが許す範囲で`/tmp`に`noexec` |
| 完全性 | `/etc`、cron、systemdユニットにAIDE/Tripwireを適用 |
| ログ | リモートのsyslog/journalへ転送し、ローカルでの削除を制限 |
| SSH | `PermitRootLogin no`、鍵ファイルはmode 600 |
| Webルート | ドキュメントルート配下に`.env`ファイルや認証情報を置かない |

防御優先の考え方: 予期しないSUIDの変更、書き込み可能な`/etc/cron*`、誰でも書き込めるサービススクリプトは、いずれもハードニングすべき所見である。最小権限と変更監視で是正する（*How Linux Works*参照）。

### ディレクトリのセキュリティ優先度

| ディレクトリ | リスクレベル | 理由 |
|-------------|-------------|------|
| `/etc/shadow` | 最重要 | パスワードハッシュ |
| `/etc/sudoers` | 最重要 | root権限 |
| `/root/` | 最重要 | rootユーザーのデータ |
| `/home/*/.ssh/` | 高 | SSH秘密鍵 |
| `/var/log/` | 高 | 活動記録 |
| `/tmp/` | 高 | 誰でも書き込み可能 |
| `/etc/passwd` | 中 | ユーザー名情報 |
| `/var/www/` | 中 | Webアプリケーションのコード |
| `/etc/cron*` | 中 | スケジュールタスク |

---

## ディレクトリ一覧リファレンス表

| ディレクトリ | 機能 | 種類 |
|-------------|------|------|
| `/` | ルートディレクトリ | 実体 |
| `/bin` | 必須ユーザーバイナリ | 実体 |
| `/sbin` | システム管理バイナリ | 実体 |
| `/etc` | システム設定 | 実体 |
| `/home` | ユーザーのホームディレクトリ | 実体 |
| `/root` | rootユーザーのホーム | 実体 |
| `/var` | 可変データとログ | 実体 |
| `/tmp` | 一時ファイル | 実体 |
| `/usr` | Unix共有リソース | 実体 |
| `/lib` | 共有ライブラリ | 実体 |
| `/dev` | デバイスファイル | 仮想 |
| `/proc` | プロセスとカーネル情報 | 仮想 |
| `/sys` | ハードウェアとカーネル情報 | 仮想 |
| `/mnt` | 手動マウントポイント | 実体 |
| `/media` | 自動マウントポイント | 実体 |
| `/opt` | オプションソフトウェア | 実体 |
| `/boot` | ブートファイル | 実体 |
| `/srv` | サーバーサービスデータ | 実体 |
| `/run` | ランタイムデータ | 仮想 |

---

## 21. 実践ワークフロー例

```bash
# ── SCENARIO: Post-exploitation filesystem reconnaissance ────

# 1. Identify the OS and kernel
$ uname -a
$ cat /etc/os-release

# 2. List all users on the system
$ cat /etc/passwd | grep "/bin/bash"

# 3. Hunt for password hashes
$ sudo cat /etc/shadow

# 4. Check sudo privileges
$ sudo -l
$ cat /etc/sudoers

# 5. Find SSH keys
$ find /home -name "id_rsa" 2>/dev/null
$ find /root -name "id_rsa" 2>/dev/null

# 6. Read command histories
$ cat /home/*/.bash_history 2>/dev/null
$ cat /root/.bash_history 2>/dev/null

# 7. Check web files for credentials
$ find /var/www -name "*.php" -exec grep -l "password" {} \;
$ find /var/www -name "config.php" 2>/dev/null

# 8. Check for writable directories
$ find / -writable -type d 2>/dev/null | grep -v proc

# 9. Look for scheduled tasks (persistence)
$ crontab -l
$ cat /etc/crontab
$ ls /etc/cron.d/
$ systemctl list-timers

# 10. Check running services
$ ps -aux
$ netstat -tulpn 2>/dev/null || ss -tulpn

# 11. Look for SUID binaries (privilege escalation)
$ find / -perm -4000 -type f 2>/dev/null

# 12. Check kernel version for exploits
$ uname -r
$ cat /proc/version
```

---

## クイックリファレンス早見表

```bash
# ── NAVIGATION ───────────────────────────────────────────────
cd /                             # go to root
ls -la /                         # list root contents
tree / -L 2                      # show 2-level tree (install: apt install tree)

# ── KEY FILES ────────────────────────────────────────────────
cat /etc/passwd                  # user accounts
sudo cat /etc/shadow             # password hashes
cat /etc/group                   # groups
cat /etc/hosts                   # hostname resolution
cat /etc/sudoers                 # sudo rules
cat /etc/ssh/sshd_config         # SSH config
cat /etc/crontab                 # system cron jobs
cat /proc/version                # kernel version
cat /proc/cpuinfo                # CPU info
cat /proc/meminfo                # memory info

# ── LOG FILES ────────────────────────────────────────────────
tail -f /var/log/syslog          # live system log
tail -f /var/log/auth.log        # live auth log
grep "Failed" /var/log/auth.log  # failed logins
grep "Accept" /var/log/auth.log  # successful logins

# ── FIND COMMANDS ────────────────────────────────────────────
find / -name "*.conf" 2>/dev/null           # find config files
find / -perm -4000 2>/dev/null              # find SUID files
find / -writable -type d 2>/dev/null        # find writable dirs
find /home -name "id_rsa" 2>/dev/null       # find SSH keys
find / -name "*.log" 2>/dev/null            # find log files
find / -name "config.php" 2>/dev/null       # find web configs

# ── DISK & MOUNT ─────────────────────────────────────────────
df -h                            # disk usage (human readable)
lsblk                            # list block devices
mount                            # show mounted filesystems
sudo mount /dev/sdb1 /mnt/usb   # mount a device
sudo umount /mnt/usb             # unmount a device
```

---

> 参考文献:
> - Brian Ward, *How Linux Works: What Every Superuser Should Know*（第3版） (`~/Documents/Books/CyberSec/Linux/`)
> - William Shotts, *The Linux Command Line*（第2版） (`~/Documents/Books/CyberSec/Linux/`)
> - Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*（カリキュラム蔵書で参照）
> - [Linux Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
> - `man hier` — Linuxファイルシステム階層のマニュアルページ
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - [GTFOBins](https://gtfobins.github.io) — 危険なSUID/sudoバイナリに対する防御側の認識向上のために参照

> LearnCybersecurity | 基礎シリーズ | kodoktheGr3at | 2026
