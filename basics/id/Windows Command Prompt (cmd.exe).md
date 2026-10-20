# Windows Command Prompt (cmd.exe)

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-004` | **Fase 0:** Fondasi
> **Estimasi belajar:** 3-4 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Gray Hat Hacking, bab enumerasi Windows
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu Command Prompt
2. Navigasi direktori
3. Manajemen file & folder
4. Informasi sistem
5. Perintah jaringan
6. User & proses
7. Enumerasi host (berizin)
8. Catatan keamanan: audit log & pertahanan LOLBin
9. Referensi cepat

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Command Prompt (CMD) | Penafsir perintah teks klasik Windows (`cmd.exe`) |
| Shell | Program yang menjalankan perintah yang kamu ketik |
| Working directory | Folder tempat perintahmu bekerja saat ini |
| Environment variable | Nilai bernama yang disimpan sistem, seperti `%USERPROFILE%` |
| Pipe (`\|`) | Mengirim output satu perintah ke perintah lain |
| Built-in vs external | Sebagian perintah ada di dalam CMD; lainnya program `.exe` terpisah |
| LOLBin | "Living off the land binary": tool bawaan yang sah tapi dipakai ulang penyerang untuk tujuan jahat |
| Enumerasi | Mengumpulkan fakta tentang host (user, share, service) yang kamu berizin memeriksanya |

---

## 1. Overview: Apa itu Command Prompt

**Command Prompt** (`cmd.exe`) adalah command-line interpreter bawaan Windows yang memungkinkan pengguna berinteraksi dengan sistem operasi melalui teks perintah, tanpa perlu antarmuka grafis (GUI). cmd.exe sudah ada sejak era MS-DOS dan masih digunakan hingga sekarang.

Dari perspektif cybersecurity, memahami CMD penting untuk:
- Enumerasi sistem setelah mendapatkan akses (post-exploitation)
- Scripting dan otomatisasi menggunakan batch file (`.bat`)
- Troubleshooting jaringan dan sistem

```cmd
REM Open Command Prompt
Win + R → type "cmd" → Enter

REM Open as Administrator
Win + X → "Command Prompt (Admin)" / "Terminal (Admin)"

REM Check the help menu
C:\> help

REM Get help for a specific command
C:\> help dir
C:\> dir /?
```

---

## 2. Navigasi Direktori

Perintah navigasi digunakan untuk berpindah antar direktori dan melihat isi folder, setara dengan `cd` dan `ls` di Linux.

```cmd
REM Show current directory
C:\Users\alex> cd

REM Change directory
C:\> cd Users\alex\Desktop

REM Go up one level
C:\Users\alex\Desktop> cd ..

REM Go to root of current drive
C:\Users\alex> cd \

REM Switch drives (C: to D:)
C:\> D:

REM List contents of current directory
C:\Users\alex> dir

REM List including hidden files
C:\Users\alex> dir /a

REM List recursively (all subfolders)
C:\Users\alex> dir /s

REM Print working directory path
C:\Users\alex> echo %cd%
```

| Command | Fungsi |
|---------|--------|
| `cd` | Tampilkan/pindah direktori |
| `cd ..` | Naik satu level |
| `cd \` | Ke root drive |
| `dir` | Daftar isi folder |
| `dir /a` | Termasuk file tersembunyi |
| `dir /s` | Rekursif (semua subfolder) |
| `tree` | Tampilkan struktur folder |

---

## 3. Manajemen File & Folder

Perintah-perintah ini digunakan untuk membuat, menyalin, memindahkan, dan menghapus file maupun folder.

```cmd
REM Create a new folder
C:\> mkdir newfolder
C:\> md newfolder

REM Remove an empty folder
C:\> rmdir newfolder
C:\> rd newfolder

REM Remove a folder AND all its contents
C:\> rmdir /s /q newfolder

REM Create an empty file
C:\> type nul > file.txt

REM Copy a file
C:\> copy file.txt D:\backup\file.txt

REM Copy a folder (with subfolders)
C:\> xcopy C:\source D:\dest /s /e

REM Move a file or folder
C:\> move file.txt D:\backup\

REM Rename a file or folder
C:\> ren oldname.txt newname.txt

REM Delete a file
C:\> del file.txt

REM Delete a file silently (no confirmation)
C:\> del /q file.txt

REM View contents of a text file
C:\> type file.txt

REM Search for text inside files
C:\> findstr "password" file.txt

REM Find files by name
C:\> dir /s /b *.txt
```

| Command | Fungsi |
|---------|--------|
| `mkdir` / `md` | Buat folder baru |
| `rmdir` / `rd` | Hapus folder |
| `copy` | Salin file |
| `xcopy` | Salin folder/file lanjutan |
| `move` | Pindah file/folder |
| `ren` | Ganti nama |
| `del` | Hapus file |
| `type` | Tampilkan isi file teks |
| `findstr` | Cari teks dalam file |

---

## 4. Informasi Sistem

Perintah-perintah ini digunakan untuk mendapatkan informasi tentang sistem, seperti versi OS, hardware, dan konfigurasi.

```cmd
REM Show detailed system info (OS, version, hotfixes, etc.)
C:\> systeminfo

REM Show OS version only
C:\> ver

REM Show environment variables
C:\> set

REM Show a specific environment variable
C:\> echo %USERNAME%
C:\> echo %COMPUTERNAME%
C:\> echo %PATH%

REM List installed hotfixes/patches
C:\> wmic qfe list

REM List installed software
C:\> wmic product get name,version

REM Show disk drive info
C:\> wmic logicaldisk get caption,description

REM Clear the screen
C:\> cls
```

| Command | Fungsi |
|---------|--------|
| `systeminfo` | Info sistem lengkap |
| `ver` | Versi OS |
| `set` | Tampilkan env variables |
| `wmic qfe list` | Daftar hotfix terinstal |
| `wmic product get name,version` | Daftar software terinstal |
| `cls` | Bersihkan layar |

Catatan pentesting: `systeminfo` dan `wmic qfe list` umum dipakai untuk mengecek patch yang belum terpasang, yang bisa menandakan sistem rentan dan berpotensi dieksploitasi.

---

## 5. Perintah Jaringan

Perintah jaringan digunakan untuk diagnosa konektivitas, melihat konfigurasi IP, dan troubleshooting jaringan.

```cmd
REM Show IP configuration
C:\> ipconfig

REM Show detailed IP configuration (DNS, MAC, etc.)
C:\> ipconfig /all

REM Release and renew DHCP lease
C:\> ipconfig /release
C:\> ipconfig /renew

REM Flush DNS cache
C:\> ipconfig /flushdns

REM Test connectivity to a host
C:\> ping google.com

REM Trace the route to a host
C:\> tracert google.com

REM Show active network connections
C:\> netstat -ano

REM Show ARP table
C:\> arp -a

REM DNS lookup
C:\> nslookup google.com

REM Show all network shares
C:\> net share

REM List computers on the domain/workgroup
C:\> net view

REM Show routing table
C:\> route print
```

| Command | Fungsi |
|---------|--------|
| `ipconfig` | Tampilkan konfigurasi IP |
| `ipconfig /all` | Konfigurasi IP detail |
| `ping` | Tes konektivitas |
| `tracert` | Lacak rute ke host |
| `netstat -ano` | Koneksi jaringan aktif + PID |
| `arp -a` | Tampilkan tabel ARP |
| `nslookup` | Lookup DNS |
| `net view` | Daftar komputer di network |

Catatan pentesting: `netstat -ano` dikombinasikan dengan `tasklist` membantu mengidentifikasi proses mana yang memiliki port terbuka yang mencurigakan.

---

## 6. User & Proses

Perintah-perintah ini digunakan untuk mengelola user account dan memonitor proses yang sedang berjalan di sistem.

```cmd
REM Show current logged-in user
C:\> whoami

REM Show current user's privileges
C:\> whoami /priv

REM Show current user's group memberships
C:\> whoami /groups

REM List all local user accounts
C:\> net user

REM Show details of a specific user
C:\> net user alex

REM Create a new local user
C:\> net user alex P@ssw0rd123 /add

REM Add user to local Administrators group
C:\> net localgroup administrators alex /add

REM Change a user's password
C:\> net user alex NewP@ssw0rd

REM Delete a user
C:\> net user alex /delete

REM List running processes
C:\> tasklist

REM Find a specific process
C:\> tasklist | findstr "chrome"

REM Kill a process by PID
C:\> taskkill /PID 1234 /F

REM Kill a process by name
C:\> taskkill /IM notepad.exe /F
```

| Command | Fungsi |
|---------|--------|
| `whoami` | Tampilkan user saat ini |
| `whoami /priv` | Tampilkan privilege user |
| `net user` | Daftar semua user lokal |
| `net user /add` | Buat user baru |
| `net localgroup administrators` | Kelola grup admin |
| `tasklist` | Daftar proses berjalan |
| `taskkill` | Hentikan proses |

Penting: selalu jalankan CMD sebagai Administrator saat menggunakan `net user /add` atau `net localgroup`, karena keduanya membutuhkan privilege elevated.

---

## 7. Enumerasi Host (Berizin)

Pada uji berizin atau lab sendiri, perintah berikut membantu inventaris host Windows dan audit konfigurasi. Ini bukan resep PrivEsc ofensif.

```cmd
REM ── Basic Recon ─────────────────────────────────────
whoami /all                        REM full identity, groups, privileges
hostname                           REM computer name
systeminfo                         REM OS, patches, architecture
echo %username% %computername%     REM quick context

REM ── User & Group Enumeration ────────────────────────
net user                           REM list local users
net localgroup administrators      REM who's in admin group
net accounts                       REM password policy

REM ── Network Enumeration ─────────────────────────────
ipconfig /all                      REM network interfaces
netstat -ano                       REM active connections
arp -a                             REM known hosts on LAN

REM ── Files & Credentials Hunting ─────────────────────
dir /s /b *password*               REM find files with "password" in name
findstr /si password *.txt *.ini *.cfg   REM search content for "password"
type C:\Users\*\Desktop\*.txt      REM check desktop notes

REM ── Scheduled Tasks & Services (priv-esc vectors) ───
schtasks /query /fo LIST /v        REM list scheduled tasks
sc query                           REM list services
sc qc <servicename>                REM service config (check binary path)

REM ── Installed Software & Patches ────────────────────
wmic product get name,version
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

Catatan: perintah-perintah ini ditujukan hanya untuk penetration testing berizin, audit defensif, dan lingkungan CTF/lab.

---

## 8. Catatan Keamanan: Hardening CMD, Audit & Kesadaran LOLBin

`cmd.exe` dan utilitas bawaan (living-off-the-land) sering dipakai penyerang maupun admin. Pertahanannya: kurangi privilege, aktifkan audit, dan monitor binary sah yang disalahgunakan.

```cmd
:: ── Privilege & session hygiene ─────────────────────────────
whoami /groups
:: Prefer standard user for daily work; elevate only when required
:: Disable local admin where possible; use LAPS for workstation admins

:: ── Command-line process auditing (defender-side) ───────────
:: Enable via GPO: Audit Process Creation + Include command line
:: Event ID 4688 (Security) — review suspicious cmd.exe /c chains
wevtutil qe Security /q:"*[System[(EventID=4688)]]" /c:5 /f:text

:: ── Soften attack surface ───────────────────────────────────
:: AppLocker/WDAC: restrict who can launch cmd.exe / scripting hosts
:: Remove unnecessary local admin; block interactive logon for service accounts
:: Prefer PowerShell with Script Block Logging for admin automation (auditable)
```

| Kontrol | Keterangan |
|---------|------------|
| Least privilege | Jangan run-as-admin harian |
| Process creation audit | Event 4688 + command line |
| WDAC / AppLocker | Batasi `cmd` / script hosts |
| LOLBAS monitoring | Alert pola anomali |
| Credential hygiene | Jangan `echo` password |

Prinsip defense-first: perlakukan rangkaian `cmd.exe /c` yang tak terduga, perubahan `sc`/`schtasks`, dan `findstr` massal di user profile sebagai sinyal untuk diburu (hunt signal), bukan sekadar noise.

---

## Tabel Ringkasan Perintah

| Command | Fungsi | Butuh Admin? |
|---------|--------|----------------|
| `dir` | Daftar isi folder | Tidak |
| `cd` | Pindah direktori | Tidak |
| `mkdir` / `rmdir` | Buat/hapus folder | Tidak (folder sistem: ya) |
| `copy` / `move` | Salin/pindah file | Tidak |
| `del` | Hapus file | Tidak |
| `systeminfo` | Info sistem | Tidak |
| `ipconfig` | Konfigurasi jaringan | Tidak |
| `ping` / `tracert` | Tes jaringan | Tidak |
| `netstat -ano` | Koneksi aktif | Tidak |
| `whoami` | User saat ini | Tidak |
| `net user /add` | Buat user | Ya |
| `net localgroup` | Kelola grup | Ya |
| `tasklist` / `taskkill` | Kelola proses | Tidak (sebagian proses: ya) |
| `sc query` | Daftar service | Tidak |
| `schtasks` | Scheduled tasks | Tidak (sebagian aksi: ya) |

---

## Contoh Alur Kerja Praktis

```cmd
REM ── SCENARIO: Quick Windows host enumeration ─────────

REM 1. Identify who and where you are
whoami /all
hostname
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

REM 2. Check network setup
ipconfig /all
netstat -ano

REM 3. Enumerate users and groups
net user
net localgroup administrators

REM 4. Look for interesting files
dir /s /b C:\Users\*password*
findstr /si password *.txt *.ini *.xml *.config

REM 5. Check scheduled tasks and services for priv-esc
schtasks /query /fo LIST /v
sc query

REM 6. Check running processes
tasklist /v
```

---

## Cheatsheet Referensi Cepat

```cmd
:: ── NAVIGATION ──────────────────────────────────────────────
cd <path>                      :: change directory
cd ..                          :: go up one level
dir                            :: list contents
dir /s /b *.txt                :: find files recursively

:: ── FILE / FOLDER ───────────────────────────────────────────
mkdir <name>                   :: create folder
rmdir /s /q <name>             :: delete folder + contents
copy <src> <dest>              :: copy file
xcopy <src> <dest> /s /e       :: copy folder recursively
move <src> <dest>              :: move file/folder
del <file>                     :: delete file
type <file>                    :: view file contents
findstr "<text>" <file>        :: search inside file

:: ── SYSTEM INFO ─────────────────────────────────────────────
systeminfo                     :: full system info
ver                             :: OS version
set                             :: environment variables
wmic qfe list                  :: installed hotfixes
cls                             :: clear screen

:: ── NETWORK ──────────────────────────────────────────────────
ipconfig /all                  :: network config
ping <host>                    :: connectivity test
tracert <host>                 :: trace route
netstat -ano                   :: active connections + PID
nslookup <domain>              :: DNS lookup
arp -a                         :: ARP table

:: ── USERS / PROCESSES ───────────────────────────────────────
whoami /all                    :: current user, groups, privileges
net user                       :: list local users
net user <name> <pw> /add      :: create user
net localgroup administrators <name> /add  :: add to admin group
tasklist                       :: list running processes
taskkill /PID <pid> /F         :: kill process by PID
taskkill /IM <name>.exe /F     :: kill process by name

:: ── DEFENSE / AUDIT CHECKS ──────────────────────────────────
whoami /priv                   :: review privileges (expect minimal daily)
net accounts                   :: password policy inventory
wevtutil qe Security /c:3 /f:text   :: sample recent Security events
:: Prefer AppLocker/WDAC + 4688 command-line auditing in production
```

## Latihan

Pakai Windows asli atau VM evaluasi Windows gratis dari Microsoft.

### Task 1: padanan Linux

| Linux | CMD |
|:---|:---|
| `ls -a` | |
| `cat file.txt` | |
| `grep "admin" file.txt` | |
| `ps aux` | |
| `kill -9 1234` | |
| `ip a` | |

<details><summary>Kunci jawaban</summary>

`dir /a` · `type file.txt` · `findstr "admin" file.txt` · `tasklist` · `taskkill /PID 1234 /F` · `ipconfig /all`

</details>

### Task 2: siapa yang membuka port?

```cmd
netstat -ano | findstr LISTENING
tasklist | findstr <PID dari baris di atas>
```

1. Pilih satu baris yang listening di port 135 atau 445. Berapa PID-nya?
2. Proses apa yang memiliki PID itu?
3. Kolom terakhir di `netstat -ano` berisi apa?

<details><summary>Kunci jawaban</summary>

1 dan 2 berbeda di tiap mesin. Port 135 biasanya milik `svchost.exe` (RPC), dan port 445 milik `System` (PID 4). Kolom terakhir adalah PID.

</details>

### Task 3: cari kesalahannya

Salah satu baris di bawah tidak melakukan apa yang tertulis di komentarnya. Yang mana, dan bagaimana yang benar?

```cmd
REM Hapus folder beserta isinya tanpa konfirmasi
rmdir /s /q temp
REM Ganti password user alex
net user alex PasswordBaru123 /add
REM Cari semua file .log di drive C
dir /s /b C:\*.log
```

<details><summary>Kunci jawaban</summary>

Baris kedua. `/add` dipakai untuk membuat user baru, jadi perintah itu gagal kalau `alex` sudah ada. Untuk mengganti password cukup `net user alex PasswordBaru123`, atau `net user alex *` supaya password diketik tanpa terlihat di layar dan tidak tersimpan di riwayat.

</details>

### Task 4: sisi blue team

1. Event ID apa yang mencatat setiap proses baru beserta command line-nya?
2. Di log kamu menemukan rangkaian ini dari satu akun dalam 30 detik: `whoami /all`, `net user`, `net localgroup administrators`, `findstr /si password *.txt`. Apa kemungkinan yang sedang terjadi?
3. Apa itu LOLBin, dan kenapa antivirus sering tidak memblokirnya?

<details><summary>Kunci jawaban</summary>

1. 4688, dengan opsi "Include command line in process creation events" diaktifkan lewat GPO.
2. Seseorang sedang melakukan enumerasi setelah masuk. Pengguna biasa jarang mengetik perintah-perintah ini berurutan secepat itu. Selidiki akun dan mesinnya.
3. LOLBin adalah program bawaan Windows yang sah (misalnya `certutil`, `bitsadmin`) tapi disalahgunakan penyerang. Antivirus jarang memblokirnya karena program itu bertanda tangan Microsoft dan dibutuhkan sistem.

</details>

### Lab gratis

| Tool | Yang bisa dilatih | Biaya |
|:---|:---|:---|
| Windows Evaluation VM (Microsoft) | Semua perintah di pelajaran ini | Gratis |
| LOLBAS Project (lolbas-project.github.io) | Daftar binary bawaan yang sering disalahgunakan, beserta cara mendeteksinya | Gratis |
| Sysinternals Suite | Process Explorer dan TCPView untuk melihat proses dan port secara visual | Gratis |

Kamu dianggap lulus pelajaran ini kalau bisa menemukan proses pemilik sebuah port hanya dengan `netstat` dan `tasklist`.

---

---

> **Referensi dan sumber buku:**
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`), konteks metodologi berizin
> - Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs, [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands), Audit Process Creation
> - [LOLBAS Project](https://lolbas-project.github.io), kesadaran defender terhadap living-off-the-land binaries
> - `help`, `<command> /?`

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
