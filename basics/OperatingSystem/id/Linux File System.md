# Linux File System

> Zero2Root | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-005` | **Fase 0:** Fondasi
> **Estimasi belajar:** 5-6 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Brian Ward, How Linux Works Ch.3-5 (FHS, /proc, /sys); William Shotts, The Linux Command Line Ch.3
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik |
|---|-------|
| 1 | Apa itu Linux File System |
| 2 | Pohon direktori lengkap |
| 3 | Direktori akar (`/`) |
| 4 | `/bin` - binary perintah esensial |
| 5 | `/sbin` - binary sistem administrator |
| 6 | `/etc` - file konfigurasi sistem |
| 7 | `/home` - direktori pengguna |
| 8 | `/root` - home untuk root user |
| 9 | `/var` - data variabel & log |
| 10 | `/tmp` - file sementara |
| 11 | `/usr` - resource Unix bersama |
| 12 | `/lib` - library bersama |
| 13 | `/dev` - file perangkat |
| 14 | `/proc` - info proses & kernel |
| 15 | `/sys` - info hardware & kernel |
| 16 | `/mnt` & `/media` - mount point |
| 17 | `/opt` - software opsional |
| 18 | `/boot` - file booting |
| 19 | `/srv` - data layanan server |
| 20 | Catatan keamanan: direktori sensitif & hardening |
| 21 | Workflow praktis |

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| File system | Cara sistem operasi menata file ke dalam pohon direktori |
| Root (`/`) | Puncak tunggal pohon Linux; semua menggantung darinya |
| FHS | Filesystem Hierarchy Standard: makna yang disepakati untuk tiap direktori teratas |
| Path | Lokasi sebuah file, absolut (`/etc/passwd`) atau relatif (`../log`) |
| Binary | File program terkompilasi (ada di `/bin`, `/usr/bin`, `/sbin`) |
| Mount | Memasang disk atau perangkat ke dalam pohon pada direktori tertentu |
| Device file | File di bawah `/dev` yang mewakili hardware |
| Pseudo-filesystem | `/proc` dan `/sys`: bukan file nyata di disk, tapi tampilan langsung dari kernel |

---

## 1. Overview: Apa Itu Linux File System

Linux File System adalah struktur hierarki yang mengorganisir semua file dan direktori di sistem Linux. Berbeda dengan Windows yang menggunakan drive terpisah (C:, D:, dll.), Linux menggunakan satu pohon direktori tunggal yang dimulai dari `/` (root).

Semua yang ada di Linux, hardware, proses, konfigurasi, hingga data pengguna, direpresentasikan sebagai file dan diorganisir dalam hierarki ini. Prinsip ini dikenal sebagai "Everything is a file."

Standar yang mengatur struktur ini disebut FHS (Filesystem Hierarchy Standard), yang mendefinisikan tujuan dan isi dari setiap direktori utama agar konsisten antar distribusi Linux.

Mengapa hal ini penting untuk cybersecurity:

- Mengetahui di mana file konfigurasi disimpan adalah target rekognisi.
- Memahami direktori mana yang dapat ditulis menunjukkan potensi privilege escalation.
- Mengenal lokasi log berguna untuk forensik dan audit.
- Mengetahui di mana binary tersimpan berguna untuk lateral movement dan persistence.

---

## 2. File Tree: Struktur Direktori Lengkap

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

## 3. `/` — Direktori Akar

`/` adalah direktori paling atas dalam hierarki file system Linux, titik awal dari semua path. Semua direktori lain adalah cabang dari root ini. Hanya root user yang memiliki izin penuh untuk menulis ke direktori root secara langsung.

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

## 4. `/bin` — Binary Perintah Esensial

`/bin` berisi binary esensial yang dibutuhkan oleh semua pengguna, bahkan saat sistem dalam mode single-user atau recovery. Perintah-perintah paling dasar yang kamu gunakan sehari-hari tinggal di sini.

```bash
# Common binaries found in /bin
ls /bin

bash    cat    chmod   chown   cp     date
echo    grep   gzip    kill    ln     ls
mkdir   mount  mv      nano    ping   ps
pwd     rm     rmdir   sh      sleep  tar
touch   uname  vi      which   ...
```

| Binary | Fungsi |
|--------|--------|
| `bash` | Shell utama |
| `ls` | Daftar isi direktori |
| `cp` | Salin file |
| `mv` | Pindah/rename file |
| `rm` | Hapus file |
| `cat` | Tampilkan isi file |
| `grep` | Cari teks dalam file |
| `chmod` | Ubah permission file |
| `ping` | Cek koneksi jaringan |

---

## 5. `/sbin` — Binary Administrasi Sistem

`/sbin` berisi binary untuk administrasi sistem yang umumnya hanya dijalankan oleh root user. Isinya berupa tools untuk manajemen disk, konfigurasi jaringan, dan maintenance sistem.

```bash
# Common binaries in /sbin
ls /sbin

fdisk      fsck       ifconfig   init       ip
iptables   mkfs       mount      reboot     route
shutdown   sshd       swapon     umount     useradd
userdel    usermod    ...
```

| Binary | Fungsi |
|--------|--------|
| `ifconfig` | Konfigurasi antarmuka jaringan |
| `iptables` | Manajemen firewall |
| `fdisk` | Manajemen partisi disk |
| `useradd` | Tambah user baru |
| `reboot` | Restart sistem |
| `fsck` | Periksa & perbaiki filesystem |

---

## 6. `/etc` — File Konfigurasi Sistem

`/etc` adalah direktori terpenting dari perspektif keamanan. Direktori ini berisi semua file konfigurasi sistem, mulai dari akun pengguna, password, konfigurasi jaringan, hingga pengaturan service. Seluruh isi `/etc` hanya boleh diubah oleh root user.

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
10.10.10.1  target.lab

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

### File Kritis di `/etc`

| File | Isi | Nilai Pentest |
|------|-----|----------------|
| `/etc/passwd` | Info akun user | Tinggi |
| `/etc/shadow` | Password terenkripsi | Kritis |
| `/etc/group` | Definisi grup | Sedang |
| `/etc/sudoers` | Izin sudo | Kritis |
| `/etc/hosts` | Resolusi hostname statis | Sedang |
| `/etc/ssh/sshd_config` | Konfigurasi SSH | Tinggi |
| `/etc/crontab` | Cron jobs sistem | Tinggi |
| `/etc/fstab` | Tabel mount filesystem | Sedang |
| `/etc/resolv.conf` | Konfigurasi DNS | Sedang |

Catatan pentesting: `/etc/passwd` dan `/etc/shadow` adalah target utama dalam privilege escalation. Jika bisa membaca `/etc/shadow`, gunakan tools seperti `john` atau `hashcat` untuk crack hash password.

---

## 7. `/home` — Direktori Pengguna

`/home` berisi direktori pribadi untuk setiap pengguna biasa. Setiap user memiliki subdirektori sendiri (`/home/username`) yang menjadi tempat penyimpanan file personal, konfigurasi aplikasi, dan file tersembunyi (dotfiles).

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

### File Tersembunyi Penting (Dotfiles) di `/home`

| File | Isi |
|------|-----|
| `.bashrc` | Konfigurasi shell bash |
| `.bash_history` | Riwayat perintah |
| `.bash_profile` | Login shell config |
| `.ssh/id_rsa` | Private key SSH |
| `.ssh/authorized_keys` | Kunci yang diizinkan login |
| `.profile` | Environment variables |
| `.gitconfig` | Konfigurasi Git |

---

## 8. `/root` — Home untuk Root User

`/root` adalah direktori home untuk superuser (root). Berbeda dari user biasa yang home-nya ada di `/home/username`, root memiliki direktori tersendiri di `/root`. Direktori ini hanya bisa diakses oleh root.

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

Catatan pentesting: mendapatkan akses ke `/root` berarti sistem sepenuhnya dikuasai (fully compromised). File `.bash_history` di sini bisa mengungkap password, perintah sensitif, atau lateral movement yang dilakukan admin.

---

## 9. `/var` — Data Variabel & Log

`/var` berisi data yang sering berubah selama operasi sistem normal, terutama log, spool, database runtime, dan file web server. Nama "var" berasal dari "variable". Direktori paling penting di sini untuk keamanan adalah `/var/log`.

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

### Subdirektori Penting di `/var`

| Direktori | Isi |
|-----------|-----|
| `/var/log` | Log sistem dan aplikasi |
| `/var/www` | File web server |
| `/var/spool` | Antrean print & cron |
| `/var/lib` | Data aplikasi persisten |
| `/var/mail` | Mailbox pengguna |
| `/var/tmp` | File temp persisten |

---

## 10. `/tmp` — File Sementara

`/tmp` adalah direktori untuk file sementara yang dibuat oleh proses dan pengguna. Isi direktori ini dihapus otomatis saat sistem reboot. Semua pengguna bisa membaca dan menulis ke `/tmp`, yang menjadikannya lokasi favorit untuk aktivitas berbahaya.

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

Catatan pentesting: `/tmp` adalah lokasi standar untuk drop payload karena world-writable. Saat melakukan post-exploitation, selalu periksa `/tmp` untuk menemukan artefak dari attacker lain atau aktivitas mencurigakan lainnya.

---

## 11. `/usr` — Resource Unix Bersama

`/usr` berisi mayoritas program dan data yang digunakan pengguna. Ini adalah direktori terbesar di sebagian besar sistem Linux. Berbeda dengan `/bin` yang hanya berisi binary paling esensial, `/usr/bin` berisi semua binary non-esensial untuk pengguna biasa.

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

| Direktori | Isi |
|-----------|-----|
| `/usr/bin` | Binary pengguna non-esensial |
| `/usr/sbin` | Binary sistem non-esensial |
| `/usr/lib` | Library untuk /usr/bin |
| `/usr/local` | Software yang dikompilasi lokal |
| `/usr/share` | Data arsitektur-independen |
| `/usr/include` | C header files |

---

## 12. `/lib` — Library Bersama

`/lib` berisi shared libraries (setara dengan .dll di Windows) yang dibutuhkan oleh binary di `/bin` dan `/sbin`. Direktori ini juga berisi kernel modules di `/lib/modules/`.

```bash
# List shared libraries
$ ls /lib/x86_64-linux-gnu/ | head -10

# List loaded kernel modules
$ lsmod

# List kernel modules directory
$ ls /lib/modules/$(uname -r)/
```

---

## 13. `/dev` — File Perangkat

`/dev` berisi file perangkat (device files), representasi virtual dari semua hardware yang terhubung ke sistem. Di Linux, semua hardware diperlakukan sebagai file, termasuk disk, terminal, dan perangkat khusus seperti `/dev/null`.

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

### File Perangkat Penting

| Perangkat | Fungsi |
|-----------|--------|
| `/dev/sda` | Hard disk pertama |
| `/dev/sda1` | Partisi pertama sda |
| `/dev/null` | Buang semua output |
| `/dev/zero` | Output null bytes tak terbatas |
| `/dev/random` | Generator angka acak |
| `/dev/tty` | Terminal saat ini |

---

## 14. `/proc` — Info Proses & Kernel

`/proc` adalah virtual filesystem, bukan direktori nyata di disk, melainkan interface ke informasi kernel dan proses yang sedang berjalan. Setiap proses memiliki subdirektori bernama sesuai PID-nya. Direktori ini sangat berguna untuk forensik dan debugging.

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

## 15. `/sys` — Info Hardware & Kernel

`/sys` adalah virtual filesystem lain yang menyediakan interface ke struktur kernel dan hardware. Direktori ini lebih terstruktur dari `/proc` dan digunakan untuk melihat dan mengubah pengaturan hardware secara real-time.

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

## 16. `/mnt` & `/media` — Mount Point

- `/mnt` digunakan untuk mount sementara secara manual oleh administrator (misalnya USB drive, NFS share, ISO image).
- `/media` digunakan untuk auto-mount media yang dapat dilepas (USB, CD-ROM) secara otomatis oleh sistem.

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

## 17. `/opt` — Software Opsional

`/opt` digunakan untuk software pihak ketiga atau opsional yang tidak dikelola oleh package manager distro. Software yang diinstal di sini biasanya self-contained dalam subdirektorinya sendiri.

```bash
# Common contents of /opt
$ ls /opt
google/   lampp/   BurpSuite/   vmware/

# Example: Burp Suite installed in /opt
$ ls /opt/BurpSuite/
BurpSuitePro  jre/  burpsuite_pro.jar
```

---

## 18. `/boot` — File Booting

`/boot` berisi semua file yang diperlukan untuk booting sistem, termasuk kernel Linux, initial RAM disk (initrd), dan konfigurasi bootloader GRUB. Jangan mengubah isi direktori ini kecuali kamu tahu apa yang kamu lakukan.

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

## 19. `/srv` — Data Layanan Server

`/srv` berisi data yang disajikan oleh layanan server yang berjalan di sistem, seperti file web, FTP, atau data repositori. Penggunaannya bervariasi antar distribusi.

```bash
$ ls /srv
http/   ftp/   git/

# Example: web files served from /srv
$ ls /srv/http/
index.html  assets/  uploads/
```

---

## 20. Catatan Keamanan: Direktori Sensitif & Defensive Hardening

Direktori berikut bernilai tinggi bagi penyerang maupun defender. Gunakan daftar ini untuk audit izin, monitoring, dan hardening pada sistem yang kamu kelola. Ini bukan panduan eksploit PrivEsc.

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

### Fokus Defensive Hardening

| Kontrol | Tindakan |
|---------|----------|
| Permissions | Mode ketat pada `/etc/shadow` dan SSH keys |
| Sudo | `visudo`, sudoers least-privilege, tanpa NOPASSWD luas |
| World-writable | Sticky bit; batasi `noexec` di `/tmp` jika kebijakan mengizinkan |
| Integrity | AIDE/Tripwire pada `/etc`, cron, dan unit systemd |
| Logging | Kirim log ke syslog/journal remote; batasi penghapusan lokal |
| SSH | `PermitRootLogin no`; file kunci mode 600 |
| Web roots | Tanpa file `.env` atau kredensial di bawah document root |

Defense-first: perubahan SUID yang tidak terduga, `/etc/cron*` yang writable, atau script service yang world-writable adalah temuan hardening. Perbaiki dengan prinsip least privilege dan change monitoring (lihat *How Linux Works*).

### Tabel Prioritas Keamanan Direktori

| Direktori | Tingkat Risiko | Alasan |
|-----------|----------------|--------|
| `/etc/shadow` | Kritis | Hash password |
| `/etc/sudoers` | Kritis | Izin root |
| `/root/` | Kritis | Data root user |
| `/home/*/.ssh/` | Tinggi | SSH private keys |
| `/var/log/` | Tinggi | Rekam aktivitas |
| `/tmp/` | Tinggi | World-writable |
| `/etc/passwd` | Sedang | Info username |
| `/var/www/` | Sedang | Kode web app |
| `/etc/cron*` | Sedang | Task terjadwal |

---

## Tabel Referensi Direktori Lengkap

| Direktori | Fungsi | Tipe |
|-----------|--------|------|
| `/` | Direktori akar | Real |
| `/bin` | Binary esensial pengguna | Real |
| `/sbin` | Binary sistem admin | Real |
| `/etc` | Konfigurasi sistem | Real |
| `/home` | Home direktori user | Real |
| `/root` | Home untuk root | Real |
| `/var` | Data variabel & log | Real |
| `/tmp` | File sementara | Real |
| `/usr` | Resource Unix bersama | Real |
| `/lib` | Shared libraries | Real |
| `/dev` | File perangkat | Virtual |
| `/proc` | Info proses & kernel | Virtual |
| `/sys` | Info hardware & kernel | Virtual |
| `/mnt` | Mount point manual | Real |
| `/media` | Mount point auto | Real |
| `/opt` | Software opsional | Real |
| `/boot` | File booting | Real |
| `/srv` | Data layanan server | Real |
| `/run` | Data runtime | Virtual |

---

## 21. Contoh Workflow Praktis

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

## Cheatsheet Referensi Cepat

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

## Latihan

### Task 1: di mana letaknya?

| Yang dicari | Direktori / file |
|:---|:---|
| Daftar semua akun user | |
| Hash password | |
| Log login SSH (Debian/Ubuntu) | |
| File website default Apache | |
| Info CPU, langsung dari kernel | |
| Kernel Linux yang di-boot | |
| Software pihak ketiga seperti Burp Suite | |
| Folder yang bisa ditulis semua user dan dikosongkan saat reboot | |

<details><summary>Kunci jawaban</summary>

`/etc/passwd` · `/etc/shadow` · `/var/log/auth.log` · `/var/www/html` · `/proc/cpuinfo` · `/boot` (file `vmlinuz`) · `/opt` · `/tmp`

</details>

### Task 2: jelajahi sistemmu

Jalankan di Linux-mu sendiri:

```bash
grep -c . /etc/passwd                      # Soal 1
grep "/bin/bash$" /etc/passwd | cut -d: -f1   # Soal 2
ls -l /etc/shadow                          # Soal 3
ls -ld /tmp                                # Soal 4
cat /proc/version                          # Soal 5
```

1. Ada berapa baris (akun) di `/etc/passwd`?
2. Akun mana saja yang memakai shell bash?
3. Siapa pemilik `/etc/shadow`, dan apakah user biasa boleh membacanya?
4. Huruf terakhir di permission `/tmp` adalah `t`. Apa artinya?
5. Versi kernel berapa yang sedang jalan?

<details><summary>Kunci jawaban</summary>

Jawaban 1, 2, dan 5 tergantung mesinmu.

3. Pemiliknya `root`, dan biasanya grupnya `shadow` (atau `root` di Fedora). User biasa tidak bisa membacanya.
4. Sticky bit. Semua orang boleh membuat file di `/tmp`, tapi hanya pemilik file yang boleh menghapus atau mengganti nama file miliknya.

</details>

### Task 3: real atau virtual?

Mana yang benar-benar tersimpan di disk, dan mana yang dibuat kernel saat itu juga: `/etc`, `/proc`, `/home`, `/sys`, `/dev/null`?

<details><summary>Kunci jawaban</summary>

Tersimpan di disk: `/etc`, `/home`. Dibuat kernel: `/proc`, `/sys`, `/dev/null`. Cobalah `ls -l /proc/cpuinfo`: ukurannya 0 byte, padahal `cat` menampilkan banyak isi.

</details>

### Task 4: audit sebagai admin

Kamu admin server ini. Jalankan lalu nilai apakah hasilnya aman:

```bash
ls -ld ~/.ssh ; ls -l ~/.ssh 2>/dev/null
find / -xdev -type f -perm -0002 2>/dev/null | head
grep -i "^PermitRootLogin" /etc/ssh/sshd_config
```

1. Permission yang aman untuk folder `~/.ssh` dan private key di dalamnya berapa?
2. Perintah `find` kedua mencari apa? Kenapa hasilnya perlu dicek?
3. Nilai `PermitRootLogin` yang disarankan apa?

<details><summary>Kunci jawaban</summary>

1. Folder `700`, private key `600`. SSH bahkan menolak memakai key yang bisa dibaca orang lain.
2. Mencari file yang bisa ditulis semua user (world-writable). Kalau file itu skrip yang dijalankan root atau cron, siapa pun bisa mengubahnya dan menumpang hak root.
3. `no`, atau `prohibit-password` kalau root memang harus login dengan key.

</details>

### Lab gratis

| Tool | Yang bisa dilatih | Biaya |
|:---|:---|:---|
| OverTheWire Bandit (overthewire.org) | Navigasi file system dan mencari file lewat SSH, level 0 sampai 10 | Gratis |
| `man hier` | Penjelasan resmi tiap direktori, langsung di terminal | Gratis |
| VM Ubuntu atau Debian (VirtualBox) | Lab bebas rusak untuk mencoba semua perintah | Gratis |

Kamu dianggap lulus pelajaran ini kalau Task 1 bisa dijawab tanpa melihat materi dan kamu bisa menjelaskan kenapa `/proc` disebut virtual.

---

---

> Referensi & Sumber Buku:
> - Brian Ward, *How Linux Works: What Every Superuser Should Know* (3rd Edition) (`~/Documents/Books/CyberSec/Linux/`)
> - William Shotts, *The Linux Command Line* (2nd Edition) (`~/Documents/Books/CyberSec/Linux/`)
> - Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (referenced in curriculum library)
> - [Linux Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
> - `man hier` — manual page untuk Linux filesystem hierarchy
> - [GTFOBins](https://gtfobins.github.io) — kesadaran defender terhadap SUID/sudo binary berbahaya

> Zero2Root | Basics Series | kodoktheGr3at | 2026
