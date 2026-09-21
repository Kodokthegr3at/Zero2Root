# Linux File System

> LearnCybersecurity | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-005` | **Phase 0:** Foundations
> **Est. study:** 5-6h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Brian Ward, How Linux Works Ch.3-5 (FHS, /proc, /sys); William Shotts, The Linux Command Line Ch.3
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic |
|---|-------|
| 1 | What is the Linux File System |
| 2 | Full directory tree |
| 3 | Root directory (`/`) |
| 4 | `/bin` - essential command binaries |
| 5 | `/sbin` - system admin binaries |
| 6 | `/etc` - system configuration files |
| 7 | `/home` - user home directories |
| 8 | `/root` - root user's home |
| 9 | `/var` - variable data and logs |
| 10 | `/tmp` - temporary files |
| 11 | `/usr` - Unix shared resources |
| 12 | `/lib` - shared libraries |
| 13 | `/dev` - device files |
| 14 | `/proc` - process and kernel info |
| 15 | `/sys` - hardware and kernel info |
| 16 | `/mnt` and `/media` - mount points |
| 17 | `/opt` - optional software |
| 18 | `/boot` - boot files |
| 19 | `/srv` - server service data |
| 20 | Security note: sensitive directories and defensive hardening |
| 21 | Practical workflow |

---

## 1. Overview: What Is the Linux File System

The Linux file system is a hierarchical structure that organizes all files and directories on a Linux system. Unlike Windows, which uses separate drives (C:, D:, and so on), Linux uses one single directory tree starting from `/` (root).

Everything in Linux, hardware, processes, configuration, and user data, is represented as a file and organized in this hierarchy. This principle is known as "Everything is a file."

The standard governing this structure is called FHS (Filesystem Hierarchy Standard), which defines the purpose and contents of each major directory so that structure stays consistent across Linux distributions.

Why it matters for cybersecurity:

- Knowing where config files are stored is a reconnaissance target.
- Understanding which directories are writable points to potential privilege escalation.
- Knowing log locations matters for forensics and auditing.
- Knowing where binaries live matters for lateral movement and persistence.

---

## 2. File Tree: Full Directory Structure

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

## 3. `/` — Root Directory

`/` is the topmost directory in the Linux file system hierarchy, the starting point of all paths. All other directories are branches from this root. Only the root user has full write permissions directly to the root directory.

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

## 4. `/bin` — Essential User Binaries

`/bin` contains essential binaries needed by all users, even when the system is in single-user or recovery mode. The most basic commands you use daily live here.

```bash
# Common binaries found in /bin
ls /bin

bash    cat    chmod   chown   cp     date
echo    grep   gzip    kill    ln     ls
mkdir   mount  mv      nano    ping   ps
pwd     rm     rmdir   sh      sleep  tar
touch   uname  vi      which   ...
```

| Binary | Function |
|--------|----------|
| `bash` | Primary shell |
| `ls` | List directory contents |
| `cp` | Copy files |
| `mv` | Move/rename files |
| `rm` | Remove files |
| `cat` | Show file contents |
| `grep` | Search text in files |
| `chmod` | Change file permissions |
| `ping` | Check network connection |

---

## 5. `/sbin` — System Administration Binaries

`/sbin` contains binaries for system administration that are typically only run by the root user. It holds tools for disk management, network configuration, and system maintenance.

```bash
# Common binaries in /sbin
ls /sbin

fdisk      fsck       ifconfig   init       ip
iptables   mkfs       mount      reboot     route
shutdown   sshd       swapon     umount     useradd
userdel    usermod    ...
```

| Binary | Function |
|--------|----------|
| `ifconfig` | Configure network interfaces |
| `iptables` | Firewall management |
| `fdisk` | Disk partition management |
| `useradd` | Add new user |
| `reboot` | Restart system |
| `fsck` | Check & repair filesystem |

---

## 6. `/etc` — System Configuration Files

`/etc` is the most important directory from a security perspective. It contains all system configuration files, from user accounts, passwords, and network config, to service settings. All contents of `/etc` should only be modified by the root user.

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

### Critical Files in `/etc`

| File | Contents | Pentest Value |
|------|----------|----------------|
| `/etc/passwd` | User account info | High |
| `/etc/shadow` | Encrypted passwords | Critical |
| `/etc/group` | Group definitions | Medium |
| `/etc/sudoers` | Sudo permissions | Critical |
| `/etc/hosts` | Static hostname resolution | Medium |
| `/etc/ssh/sshd_config` | SSH configuration | High |
| `/etc/crontab` | System cron jobs | High |
| `/etc/fstab` | Filesystem mount table | Medium |
| `/etc/resolv.conf` | DNS configuration | Medium |

Pentesting note: `/etc/passwd` and `/etc/shadow` are primary targets in privilege escalation. If you can read `/etc/shadow`, use tools such as `john` or `hashcat` to crack the password hashes.

---

## 7. `/home` — User Home Directories

`/home` contains personal directories for each regular user. Each user has their own subdirectory (`/home/username`), which stores personal files, application configurations, and hidden files (dotfiles).

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

### Key Hidden Files (Dotfiles) in `/home`

| File | Contents |
|------|----------|
| `.bashrc` | Bash shell configuration |
| `.bash_history` | Command history |
| `.bash_profile` | Login shell config |
| `.ssh/id_rsa` | SSH private key |
| `.ssh/authorized_keys` | Authorized SSH keys |
| `.profile` | Environment variables |
| `.gitconfig` | Git configuration |

---

## 8. `/root` — Root User's Home

`/root` is the home directory for the superuser (root). Unlike regular users, whose home is in `/home/username`, root has its own dedicated directory at `/root`. This directory is accessible only by root.

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

Pentesting note: getting access to `/root` means the system is fully compromised. The `.bash_history` file here can reveal passwords, sensitive commands, or lateral movement performed by an admin.

---

## 9. `/var` — Variable Data & Logs

`/var` contains data that frequently changes during normal system operation, especially logs, spools, runtime databases, and web server files. The name "var" comes from "variable." The most security-important directory here is `/var/log`.

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

### Key Subdirectories in `/var`

| Directory | Contents |
|-----------|----------|
| `/var/log` | System and app logs |
| `/var/www` | Web server files |
| `/var/spool` | Print & cron queues |
| `/var/lib` | Persistent app data |
| `/var/mail` | User mailboxes |
| `/var/tmp` | Persistent temp files |

---

## 10. `/tmp` — Temporary Files

`/tmp` is the directory for temporary files created by processes and users. Its contents are automatically cleared on reboot. All users can read and write to `/tmp`, which makes it a favorite location for malicious activity.

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

Pentesting note: `/tmp` is the standard location to drop a payload because it is world-writable. During post-exploitation, always check `/tmp` for artifacts left by other attackers or for other suspicious activity.

---

## 11. `/usr` — Unix Shared Resources

`/usr` contains the majority of programs and data used by users. It is the largest directory on most Linux systems. Unlike `/bin`, which holds only the most essential binaries, `/usr/bin` contains all non-essential binaries for regular users.

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

| Directory | Contents |
|-----------|----------|
| `/usr/bin` | Non-essential user binaries |
| `/usr/sbin` | Non-essential system binaries |
| `/usr/lib` | Libraries for /usr/bin |
| `/usr/local` | Locally compiled software |
| `/usr/share` | Architecture-independent data |
| `/usr/include` | C header files |

---

## 12. `/lib` — Shared Libraries

`/lib` contains shared libraries (equivalent to .dll files on Windows) needed by binaries in `/bin` and `/sbin`. It also contains kernel modules in `/lib/modules/`.

```bash
# List shared libraries
$ ls /lib/x86_64-linux-gnu/ | head -10

# List loaded kernel modules
$ lsmod

# List kernel modules directory
$ ls /lib/modules/$(uname -r)/
```

---

## 13. `/dev` — Device Files

`/dev` contains device files, virtual representations of all hardware connected to the system. In Linux, all hardware is treated as a file, including disks, terminals, and special devices such as `/dev/null`.

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

### Important Device Files

| Device | Function |
|--------|----------|
| `/dev/sda` | First hard disk |
| `/dev/sda1` | First partition of sda |
| `/dev/null` | Discard all output |
| `/dev/zero` | Infinite null bytes output |
| `/dev/random` | Random number generator |
| `/dev/tty` | Current terminal |

---

## 14. `/proc` — Process & Kernel Information

`/proc` is a virtual filesystem, not a real directory on disk, but an interface to kernel and running-process information. Each process has a subdirectory named after its PID. It is extremely useful for forensics and debugging.

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

## 15. `/sys` — Hardware & Kernel Interface

`/sys` is another virtual filesystem providing an interface to kernel structure and hardware. It is more structured than `/proc` and is used to view and modify hardware settings in real time.

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

## 16. `/mnt` & `/media` — Mount Points

- `/mnt` is used for temporary manual mounts by administrators (for example USB drives, NFS shares, ISO images).
- `/media` is used for auto-mounting removable media (USB, CD-ROM) automatically by the system.

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

## 17. `/opt` — Optional Software

`/opt` is used for third-party or optional software not managed by the distro's package manager. Software installed here is usually self-contained in its own subdirectory.

```bash
# Common contents of /opt
$ ls /opt
google/   lampp/   BurpSuite/   vmware/

# Example: Burp Suite installed in /opt
$ ls /opt/BurpSuite/
BurpSuitePro  jre/  burpsuite_pro.jar
```

---

## 18. `/boot` — Boot Files

`/boot` contains all files required to boot the system, including the Linux kernel, the initial RAM disk (initrd), and the GRUB bootloader configuration. Do not modify the contents of this directory unless you know what you are doing.

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

## 19. `/srv` — Server Service Data

`/srv` contains data served by server services running on the system, such as web files, FTP, or repository data. Its usage varies across distributions.

```bash
$ ls /srv
http/   ftp/   git/

# Example: web files served from /srv
$ ls /srv/http/
index.html  assets/  uploads/
```

---

## 20. Security Note: Sensitive Directories & Defensive Hardening

The following directories are high-value to attackers and to defenders. Use this list for permission audits, monitoring, and hardening on systems you manage; it is not a PrivEsc exploit guide.

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

### Defensive Hardening Focus

| Control | Action |
|---------|--------|
| Permissions | Strict modes on `/etc/shadow` and SSH keys |
| Sudo | `visudo`, least-privilege sudoers, no broad NOPASSWD |
| World-writable | Sticky bit; restrict `noexec` on `/tmp` where policy allows |
| Integrity | AIDE/Tripwire on `/etc`, cron, and systemd units |
| Logging | Ship logs to remote syslog/journal; restrict local deletion |
| SSH | `PermitRootLogin no`; key files at mode 600 |
| Web roots | No `.env` files or credentials under the document root |

Defense-first: unexpected SUID changes, a writable `/etc/cron*`, or world-writable service scripts are hardening findings. Remediate with least privilege and change monitoring (see *How Linux Works*).

### Directory Security Priority Table

| Directory | Risk Level | Reason |
|-----------|-----------|--------|
| `/etc/shadow` | Critical | Password hashes |
| `/etc/sudoers` | Critical | Root permissions |
| `/root/` | Critical | Root user data |
| `/home/*/.ssh/` | High | SSH private keys |
| `/var/log/` | High | Activity records |
| `/tmp/` | High | World-writable |
| `/etc/passwd` | Medium | Username info |
| `/var/www/` | Medium | Web app code |
| `/etc/cron*` | Medium | Scheduled tasks |

---

## Complete Directory Reference Table

| Directory | Function | Type |
|-----------|----------|------|
| `/` | Root directory | Real |
| `/bin` | Essential user binaries | Real |
| `/sbin` | System admin binaries | Real |
| `/etc` | System configuration | Real |
| `/home` | User home directories | Real |
| `/root` | Root user's home | Real |
| `/var` | Variable data & logs | Real |
| `/tmp` | Temporary files | Real |
| `/usr` | Unix shared resources | Real |
| `/lib` | Shared libraries | Real |
| `/dev` | Device files | Virtual |
| `/proc` | Process & kernel info | Virtual |
| `/sys` | Hardware & kernel info | Virtual |
| `/mnt` | Manual mount point | Real |
| `/media` | Auto mount point | Real |
| `/opt` | Optional software | Real |
| `/boot` | Boot files | Real |
| `/srv` | Server service data | Real |
| `/run` | Runtime data | Virtual |

---

## 21. Practical Workflow Example

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

## Quick Reference Cheatsheet

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

> References & Book Sources:
> - Brian Ward, *How Linux Works: What Every Superuser Should Know* (3rd Edition) (`~/Documents/Books/CyberSec/Linux/`)
> - William Shotts, *The Linux Command Line* (2nd Edition) (`~/Documents/Books/CyberSec/Linux/`)
> - Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (referenced in curriculum library)
> - [Linux Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
> - `man hier` — manual page for the Linux filesystem hierarchy
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - [GTFOBins](https://gtfobins.github.io) — defender awareness of dangerous SUID/sudo binaries

> LearnCybersecurity | Basics Series | kodoktheGr3at | 2026
