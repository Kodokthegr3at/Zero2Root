# Sistem Berkas Windows

> **LearnCybersecurity** | Seri Dasar-Dasar | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-006` | **Fase 0:** Fondasi
> **Estimasi belajar:** 5-6 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Gray Hat Hacking (NTFS, Registry, ADS)
<!-- LC-CURRICULUM-END -->

## Daftar Isi

| # | Topik |
|---|-------|
| 1 | Apa itu sistem berkas Windows |
| 2 | Sistem huruf drive |
| 3 | Pohon direktori lengkap |
| 4 | `C:\Windows` |
| 5 | `C:\Windows\System32` |
| 6 | `C:\Users` |
| 7 | `C:\Program Files` |
| 8 | `C:\ProgramData` |
| 9 | `C:\Temp` dan `%TEMP%` |
| 10 | Registry |
| 11 | Variabel lingkungan |
| 12 | NTFS dan izin |
| 13 | File tersembunyi dan khusus |
| 14 | Lokasi sensitif dan hardening |
| 15 | Navigasi rekon praktis |

---

## 1. Overview: Apa Itu Sistem Berkas Windows

Sistem berkas Windows menggunakan struktur huruf drive (C:, D:, E:, dan seterusnya), berbeda dari Linux yang memakai satu pohon direktori berakar di `/`. Setiap drive punya hierarki direktorinya sendiri.

Windows modern berjalan di atas NTFS (New Technology File System), yang mendukung:
- Izin granular per file dan folder lewat ACL
- Alternate Data Streams (ADS), data tersembunyi yang menempel pada sebuah file
- Enkripsi file dan folder (EFS)
- Journaling, untuk pemulihan setelah kegagalan sistem
- Symbolic link dan junction

Ini penting untuk pekerjaan keamanan dalam beberapa hal konkret:
- Mengetahui lokasi kredensial dan file konfigurasi memberimu target rekognisi
- Memahami izin NTFS adalah prasyarat untuk privilege escalation
- Mengetahui lokasi log mendukung forensik dan incident response
- Memahami Registry penting untuk persistence dan analisis malware
- Mengetahui direktori mana yang writable penting untuk payload staging

---

## 2. Huruf Drive: Sistem Drive Windows

Windows menggunakan huruf drive untuk mengidentifikasi partisi dan perangkat penyimpanan. Secara default, drive utama tempat Windows terinstal adalah `C:\`. Drive lain (USB, CD, partisi tambahan) mendapat huruf berikutnya yang tersedia secara berurutan.

```cmd
:: List all drives
> wmic logicaldisk get name,description,size,freespace

:: Or in PowerShell
PS> Get-PSDrive -PSProvider FileSystem

Name  Used (GB)  Free (GB)  Provider   Root
----  ---------  ---------  --------   ----
C        85.2       14.8    FileSystem C:\
D         0.0       29.9    FileSystem D:\

:: Navigate drives in CMD
> C:         :: switch to C drive
> D:         :: switch to D drive
> cd C:\     :: go to root of C
```

| Huruf drive | Penggunaan umum |
|-------------|-------------------|
| `A:` / `B:` | Floppy disk (legacy) |
| `C:` | Drive sistem utama |
| `D:` | Drive sekunder / DVD |
| `E:` dan seterusnya | USB, partisi tambahan |

---

## 3. Pohon Berkas: Struktur Direktori Lengkap

```
C:\                                    ← Primary system drive (root)
│
├── Windows\                           ← Core OS files
│   ├── System32\                      ← 64-bit system binaries & DLLs
│   │   ├── cmd.exe                    ← Command Prompt
│   │   ├── powershell.exe             ← Windows PowerShell
│   │   ├── notepad.exe                ← Notepad
│   │   ├── calc.exe                   ← Calculator
│   │   ├── msiexec.exe                ← Windows Installer
│   │   ├── svchost.exe                ← Service host process
│   │   ├── lsass.exe                  ← Local Security Authority (credentials!)
│   │   ├── winlogon.exe               ← Windows logon process
│   │   ├── taskmgr.exe                ← Task Manager
│   │   ├── reg.exe                    ← Registry editor (CLI)
│   │   ├── net.exe                    ← Network commands
│   │   ├── netstat.exe                ← Network statistics
│   │   ├── ipconfig.exe               ← IP configuration
│   │   ├── whoami.exe                 ← Current user info
│   │   ├── runas.exe                  ← Run as different user
│   │   ├── sc.exe                     ← Service control
│   │   ├── cacls.exe                  ← File ACL editor
│   │   ├── icacls.exe                 ← Improved ACL editor
│   │   ├── drivers\                   ← Kernel drivers (.sys files)
│   │   ├── config\                    ← SAM, SYSTEM, SECURITY hives!
│   │   │   ├── SAM                    ← Security Account Manager (password hashes!)
│   │   │   ├── SYSTEM                 ← System configuration hive
│   │   │   ├── SECURITY               ← Security policy hive
│   │   │   ├── SOFTWARE               ← Installed software hive
│   │   │   └── DEFAULT                ← Default user hive
│   │   ├── winevt\                    ← Windows Event Logs
│   │   │   └── Logs\
│   │   │       ├── System.evtx        ← System events
│   │   │       ├── Security.evtx      ← Security/login events
│   │   │       ├── Application.evtx   ← Application events
│   │   │       └── Microsoft-Windows-PowerShell%4Operational.evtx
│   │   ├── spool\                     ← Print spooler
│   │   └── Tasks\                     ← Scheduled tasks
│   │
│   ├── SysWOW64\                      ← 32-bit system binaries (on 64-bit OS)
│   ├── Temp\                          ← Windows temp files
│   ├── Logs\                          ← Additional OS logs
│   ├── Prefetch\                      ← Program prefetch data (forensics!)
│   ├── ServiceProfiles\               ← Service account profiles
│   │   ├── LocalService\
│   │   ├── NetworkService\
│   │   └── LocalSystem\
│   └── inf\                           ← Driver information files
│
├── Users\                             ← All user profile directories
│   ├── Public\                        ← Shared between all users
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   └── Downloads\
│   │
│   ├── Administrator\                 ← Built-in admin account
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   ├── Downloads\
│   │   ├── AppData\                   ← Application data (hidden)
│   │   │   ├── Local\                 ← Local app data
│   │   │   │   ├── Temp\              ← User temp files
│   │   │   │   ├── Microsoft\         ← MS app data
│   │   │   │   │   ├── Windows\
│   │   │   │   │   │   └── PowerShell\
│   │   │   │   │   │       └── ConsoleHost_history.txt  ← PS history!
│   │   │   │   │   └── Credentials\   ← Stored credentials!
│   │   │   │   └── Google\Chrome\     ← Browser data
│   │   │   ├── LocalLow\              ← Low-integrity app data
│   │   │   └── Roaming\               ← Synced across domain
│   │   │       ├── Microsoft\
│   │   │       │   ├── Windows\
│   │   │       │   │   ├── Recent\    ← Recently opened files
│   │   │       │   │   └── PowerShell\
│   │   │       │   └── Credentials\   ← Cached domain credentials!
│   │   │       └── Mozilla\Firefox\   ← Firefox profile
│   │   ├── NTUSER.DAT                 ← User registry hive!
│   │   └── .ssh\                      ← SSH keys (if installed)
│   │
│   └── alice\                         ← Regular user
│       └── (same structure as above)
│
├── Program Files\                     ← 64-bit installed applications
│   ├── Google\
│   ├── Mozilla Firefox\
│   ├── Microsoft Office\
│   └── Common Files\
│
├── Program Files (x86)\               ← 32-bit installed applications
│   └── (legacy 32-bit software)
│
├── ProgramData\                       ← Global app data (hidden)
│   ├── Microsoft\
│   │   ├── Windows\
│   │   │   └── Start Menu\
│   │   └── Windows Defender\          ← AV definitions & logs
│   └── (other app data)
│
├── Temp\                              ← System-wide temp folder
│
├── inetpub\                           ← IIS web server root
│   ├── wwwroot\                       ← Default web files
│   └── logs\                          ← IIS logs
│
├── $Recycle.Bin\                      ← Recycle Bin (hidden)
│
├── System Volume Information\         ← VSS shadow copies (hidden)
│
├── pagefile.sys                       ← Virtual memory page file
├── hiberfil.sys                       ← Hibernation file (RAM dump!)
├── swapfile.sys                       ← Modern swap file
└── bootmgr                            ← Windows boot manager
```

---

## 4. `C:\Windows`: Direktori Sistem Utama

`C:\Windows` adalah direktori inti dari sistem operasi Windows, kurang lebih setara dengan `/` di Linux, meski cakupannya terbatas pada OS itu sendiri, bukan seluruh filesystem. Direktori ini berisi semua komponen OS kritis, driver, file konfigurasi sistem, dan log. Hanya akun Administrator dan SYSTEM yang seharusnya mengubah isinya.

```cmd
:: List Windows directory
> dir C:\Windows

:: Key subdirectories
> dir C:\Windows\System32
> dir C:\Windows\SysWOW64
> dir C:\Windows\Temp
> dir C:\Windows\Prefetch

:: Check Windows version
> winver
> ver

:: PowerShell
PS> [System.Environment]::OSVersion
PS> Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion
```

| Subdirektori | Isi |
|--------------|-----|
| `System32\` | Binary dan DLL sistem 64-bit |
| `SysWOW64\` | Binary sistem 32-bit |
| `Temp\` | File temp sistem |
| `Prefetch\` | Data prefetch program |
| `Logs\` | Log sistem tambahan |
| `inf\` | File informasi driver |
| `Fonts\` | File font sistem |

---

## 5. `C:\Windows\System32`: Jantung Windows

`System32` adalah direktori paling penting di Windows. Berisi binary sistem inti, DLL (Dynamic Link Library), driver, file konfigurasi registry, dan event log. Ini adalah target pentest utama karena berisi database SAM (hash password) dan event log.

Meski namanya "System32", di Windows 64-bit direktori ini berisi binary 64-bit. Binary 32-bit ada di `SysWOW64`.

```cmd
:: Navigate to System32
> cd C:\Windows\System32

:: Key executables
> cmd.exe              :: Command Prompt
> powershell.exe       :: PowerShell
> lsass.exe            :: Credential storage process
> svchost.exe          :: Service host
> taskmgr.exe          :: Task Manager
> msiexec.exe          :: Windows Installer
> reg.exe              :: Registry CLI tool
> sc.exe               :: Service Control
> net.exe              :: Network commands
> whoami.exe           :: Current user
> icacls.exe           :: File permissions
> runas.exe            :: Run as another user

:: Registry hives (locked while OS runs)
> dir C:\Windows\System32\config\
SAM       SYSTEM    SECURITY    SOFTWARE    DEFAULT
```

### File Kritis di `System32\config\`

| File | Isi | Nilai pentest |
|------|-----|-----------------|
| `SAM` | Hash password akun lokal | Kritis |
| `SYSTEM` | Konfigurasi sistem, boot key | Kritis |
| `SECURITY` | Kebijakan keamanan lokal | Tinggi |
| `SOFTWARE` | Software terinstal dan config | Sedang |
| `DEFAULT` | Profil user default | Rendah |

```cmd
:: SAM is locked while Windows runs — dump via shadow copy
:: Or use tools like: secretsdump.py, mimikatz

:: From attacker machine (via impacket):
$ python3 secretsdump.py -sam SAM -system SYSTEM LOCAL

:: Copy hives via shadow copy (requires admin):
> vssadmin create shadow /for=C:
> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM C:\temp\SAM
```

---

## 6. `C:\Users`: Direktori Pengguna

`C:\Users` menyimpan direktori profil untuk setiap user yang pernah login ke sistem. Setiap user mendapat direktori dengan tata letak yang sama, termasuk folder `AppData` tersembunyi yang menyimpan data aplikasi, kredensial tersimpan, dan riwayat.

```cmd
:: List all user profiles
> dir C:\Users
> net user

:: Navigate to a user profile
> cd C:\Users\alice

:: Show hidden AppData folder
> dir /a C:\Users\alice

:: PowerShell history (gold mine!)
> type C:\Users\alice\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

:: Stored Windows credentials
> cmdkey /list

:: Recent files
> dir C:\Users\alice\AppData\Roaming\Microsoft\Windows\Recent\

:: Check all users' PowerShell history
> foreach ($user in (Get-ChildItem C:\Users)) {
    $hist = "$($user.FullName)\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
    if (Test-Path $hist) { echo "=== $($user.Name) ==="; Get-Content $hist }
  }
```

### File Bernilai Tinggi di `C:\Users\<username>\`

| Path | Isi | Nilai pentest |
|------|-----|-----------------|
| `NTUSER.DAT` | Registry hive user | Tinggi |
| `AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt` | Riwayat PowerShell | Kritis |
| `AppData\Roaming\Microsoft\Credentials\` | Kredensial domain yang di-cache | Kritis |
| `AppData\Local\Microsoft\Credentials\` | Kredensial lokal yang di-cache | Tinggi |
| `AppData\Local\Google\Chrome\User Data\Default\Login Data` | Password browser Chrome | Tinggi |
| `AppData\Roaming\Mozilla\Firefox\Profiles\` | Profil Firefox | Tinggi |
| `.ssh\id_rsa` | SSH private key | Tinggi |
| `Desktop\` | File di desktop | Sedang |
| `Documents\` | Dokumen user | Sedang |

---

## 7. `C:\Program Files`: Aplikasi Terinstal

`C:\Program Files` adalah lokasi default untuk instalasi aplikasi 64-bit. `C:\Program Files (x86)` menyimpan aplikasi 32-bit di sistem 64-bit. Menulis ke salah satu direktori ini membutuhkan hak Administrator.

```cmd
:: List installed 64-bit programs
> dir "C:\Program Files"

:: List installed 32-bit programs
> dir "C:\Program Files (x86)"

:: PowerShell - list all installed programs
PS> Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Sort-Object DisplayName

:: Common pentesting-relevant software locations
> dir "C:\Program Files\OpenSSH-Win64\"         :: SSH client/server
> dir "C:\Program Files\Git\"                   :: Git
> dir "C:\Program Files\Python*\"               :: Python
> dir "C:\Program Files\Microsoft SQL Server\"  :: SQL Server
> dir "C:\Program Files\FileZilla Server\"      :: FTP server
```

Catatan pentest: aplikasi di `Program Files` yang datang dengan izin folder atau binary yang terlalu longgar bisa menjadi vektor privilege escalation lewat DLL hijacking atau binary planting.

---

## 8. `C:\ProgramData`: Data Aplikasi Global

`C:\ProgramData` adalah direktori tersembunyi yang menyimpan data aplikasi yang dibagikan di antara semua user. Berbeda dari `AppData` yang per-user, `ProgramData` bersifat global. Biasanya berisi file konfigurasi, database, dan log aplikasi.

```cmd
:: Show hidden ProgramData (requires /a flag or Show Hidden Files)
> dir /a C:\ProgramData

:: Common contents
> dir C:\ProgramData\Microsoft\Windows Defender\   :: AV logs & exclusions
> dir C:\ProgramData\Microsoft\Windows\Start Menu\ :: All-users start menu
> dir C:\ProgramData\ssh\                          :: SSH server config (if installed)
> type C:\ProgramData\ssh\sshd_config

:: Search for config files with credentials
PS> Get-ChildItem -Path "C:\ProgramData" -Recurse -Include "*.conf","*.config","*.ini","*.xml" -ErrorAction SilentlyContinue |
    Select-String -Pattern "password|passwd|pwd" -CaseSensitive:$false
```

---

## 9. `C:\Temp` dan `%TEMP%`: File Sementara

Windows menyimpan dua lokasi temp: `C:\Windows\Temp` (sistem-wide) dan `%TEMP%` (per user, biasanya `C:\Users\<user>\AppData\Local\Temp`). Keduanya bisa dipakai untuk payload staging, dan keduanya sering menyimpan artefak sementara yang berguna untuk forensik.

```cmd
:: View system temp
> dir C:\Windows\Temp

:: View current user temp (expand variable)
> echo %TEMP%
C:\Users\alice\AppData\Local\Temp
> dir %TEMP%

:: PowerShell
PS> $env:TEMP
PS> Get-ChildItem $env:TEMP

:: Clear temp files
> del /q /f /s %TEMP%\*

:: Common attacker artifacts in temp:
:: - Downloaded payloads
:: - Extracted archives
:: - Compiled exploit binaries
:: - Credential dumps
```

---

## 10. Registry: Windows Registry

Windows Registry adalah database hierarkis terpusat yang menyimpan konfigurasi sistem, pengaturan aplikasi, dan informasi user. Ini adalah komponen paling penting untuk dipahami dalam pentest Windows: lokasi utama untuk persistence, penyimpanan kredensial, dan konfigurasi sistem.

Registry diorganisasi ke dalam hive utama (root key):

| Hive | Singkatan | Isi |
|------|-----------|-----|
| `HKEY_LOCAL_MACHINE` | `HKLM` | Konfigurasi mesin lokal |
| `HKEY_CURRENT_USER` | `HKCU` | Konfigurasi user saat ini |
| `HKEY_USERS` | `HKU` | Semua profil user |
| `HKEY_CLASSES_ROOT` | `HKCR` | Asosiasi file dan objek COM |
| `HKEY_CURRENT_CONFIG` | `HKCC` | Profil hardware saat ini |

```cmd
:: Open Registry Editor (GUI)
> regedit

:: Registry CLI — reg.exe
> reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run   :: startup programs
> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run   :: user startup

:: ── PERSISTENCE LOCATIONS IN REGISTRY ─────────────────────
:: Auto-run on startup (all users)
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

:: Auto-run on startup (current user)
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce

:: ── CREDENTIAL-RELATED REGISTRY KEYS ───────────────────────
:: Windows autologon (may contain cleartext password!)
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

:: Stored VNC passwords
> reg query HKCU\Software\ORL\WinVNC3\Password
> reg query HKCU\Software\TightVNC\Server

:: PuTTY stored sessions
> reg query HKCU\Software\SimonTatham\PuTTY\Sessions

:: ── SYSTEM INFO VIA REGISTRY ────────────────────────────────
:: OS version
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName

:: Installed software
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

:: PowerShell
PS> Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" |
    Select-Object DefaultUserName, DefaultPassword, AutoAdminLogon
```

### Registry Key Kritis untuk Pentest

| Registry Key | Isi | Nilai pentest |
|---------------|-----|-----------------|
| `HKLM\SAM` | Hash password lokal | Kritis |
| `HKLM\SYSTEM\CurrentControlSet\Services` | Daftar service | Tinggi |
| `HKLM\SOFTWARE\...\Winlogon` | Kredensial auto-logon | Kritis |
| `HKCU\...\Run` | Program startup user | Tinggi |
| `HKLM\...\Run` | Program startup sistem | Tinggi |
| `HKCU\Software\SimonTatham\PuTTY` | Sesi/password PuTTY | Tinggi |

---

## 11. Variabel Lingkungan: Env Var Windows

Variabel lingkungan menyimpan informasi tentang lingkungan sistem. Di Windows, kamu mengaksesnya dengan tanda `%` di CMD atau `$env:` di PowerShell. Berguna untuk navigasi karena menunjuk ke direktori penting tanpa perlu path lengkap.

```cmd
:: List all environment variables
> set
> set | findstr /i "path"

:: PowerShell
PS> Get-ChildItem Env:
PS> $env:PATH

:: ── KEY ENVIRONMENT VARIABLES ────────────────────────────────
%SYSTEMROOT%        :: C:\Windows
%SYSTEMDRIVE%       :: C:
%WINDIR%            :: C:\Windows
%PROGRAMFILES%      :: C:\Program Files
%PROGRAMFILES(X86)% :: C:\Program Files (x86)
%PROGRAMDATA%       :: C:\ProgramData
%USERPROFILE%       :: C:\Users\alice
%APPDATA%           :: C:\Users\alice\AppData\Roaming
%LOCALAPPDATA%      :: C:\Users\alice\AppData\Local
%TEMP%              :: C:\Users\alice\AppData\Local\Temp
%TMP%               :: Same as %TEMP%
%USERNAME%          :: alice
%USERDOMAIN%        :: WORKGROUP or DOMAIN_NAME
%COMPUTERNAME%      :: PC hostname
%PATH%              :: Directories searched for executables
%PATHEXT%           :: Executable file extensions

:: Use variables for navigation
> cd %USERPROFILE%
> cd %APPDATA%\Microsoft\Windows\PowerShell
> dir %SYSTEMROOT%\System32\config
```

| Variabel | Menunjuk ke |
|----------|--------------|
| `%SYSTEMROOT%` | Direktori Windows |
| `%USERPROFILE%` | Direktori home user |
| `%APPDATA%` | AppData Roaming |
| `%TEMP%` | Folder temp user |
| `%PROGRAMFILES%` | Program Files 64-bit |
| `%COMPUTERNAME%` | Nama komputer |
| `%USERNAME%` | Username saat ini |

---

## 12. NTFS dan Izin: Keamanan Sistem Berkas

NTFS menggunakan sistem ACL (Access Control List) untuk mengontrol izin akses. Setiap file dan folder punya DACL (Discretionary ACL) yang menentukan siapa boleh melakukan apa. Memahami izin NTFS penting baik untuk privilege escalation maupun forensik.

```cmd
:: View file/folder permissions
> icacls C:\Windows\System32
> icacls C:\Users\alice\Desktop

:: Example output:
C:\Users\alice\Desktop
  BUILTIN\Administrators:(I)(F)     :: Full control
  NT AUTHORITY\SYSTEM:(I)(F)        :: Full control
  alice:(I)(OI)(CI)(F)              :: Full control (owner)
  BUILTIN\Users:(I)(RX)             :: Read & Execute

:: Check permissions on a specific file
> icacls C:\Windows\System32\config\SAM

:: Find writable directories (privilege escalation!)
PS> Get-ChildItem "C:\Program Files\" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.PSIsContainer } |
    ForEach-Object {
        $acl = Get-Acl $_.FullName
        if ($acl.Access | Where-Object { $_.IdentityReference -match "Everyone|Users" -and $_.FileSystemRights -match "Write|FullControl" }) {
            $_.FullName
        }
    }

:: Alternate Data Streams (ADS) — hide data in files
:: Create ADS
> echo "hidden data" > normal.txt:hidden_stream
:: Read ADS
> more < normal.txt:hidden_stream
:: List ADS
> dir /r normal.txt
> Get-Item normal.txt -Stream *
```

### Jenis Izin NTFS

| Izin | Simbol | Arti |
|------|--------|------|
| Full Control | `F` | Semua hak |
| Modify | `M` | Baca, tulis, hapus |
| Read & Execute | `RX` | Baca dan jalankan |
| Read | `R` | Baca saja |
| Write | `W` | Tulis saja |

---

## 13. File Khusus dan Tersembunyi

Windows menyembunyikan berbagai file dan direktori dari tampilan normal. Sebuah file bisa "tersembunyi" dengan beberapa cara: atribut hidden, atribut system, atau sekadar berada di lokasi yang tidak diindeks. Beberapa file ini sangat berarti untuk forensik dan pentest.

```cmd
:: Show hidden files in CMD
> dir /a C:\
> dir /a /s C:\Users\alice

:: Show hidden files in PowerShell
PS> Get-ChildItem -Force C:\Users\alice
PS> Get-ChildItem -Force -Hidden C:\

:: ── IMPORTANT HIDDEN FILES ───────────────────────────────────

:: Page file (virtual memory — may contain sensitive data!)
> dir /a C:\pagefile.sys

:: Hibernation file (complete RAM dump at hibernate time!)
> dir /a C:\hiberfil.sys
:: Extract from hiberfil.sys (Volatility/Hibernation tools)
$ python3 volatility3 -f hiberfil.sys windows.info

:: Recycle Bin
> dir /a C:\$Recycle.Bin\

:: System Volume Information (VSS shadow copies)
> dir /a "C:\System Volume Information\"

:: NTUSER.DAT (user registry hive — hidden in user profile)
> dir /a C:\Users\alice\NTUSER.DAT

:: Prefetch files (program execution evidence)
> dir C:\Windows\Prefetch\
> dir C:\Windows\Prefetch\ | findstr .pf

:: Windows Event Logs
> dir C:\Windows\System32\winevt\Logs\

:: View Windows Event Log
PS> Get-WinEvent -LogName Security -MaxEvents 50 |
    Where-Object { $_.Id -in 4624,4625,4648 } |
    Select-Object TimeCreated, Id, Message

:: Event IDs for pentesting
:: 4624 = Successful logon
:: 4625 = Failed logon
:: 4648 = Logon with explicit credentials
:: 4672 = Special privileges assigned (admin logon)
:: 4688 = Process creation
:: 4698 = Scheduled task created
```

### File Tersembunyi Penting

| File/Direktori | Isi | Nilai pentest |
|-----------------|-----|-----------------|
| `C:\pagefile.sys` | Memori virtual | Tinggi |
| `C:\hiberfil.sys` | Dump RAM saat hibernate | Kritis |
| `C:\$Recycle.Bin` | File terhapus | Sedang |
| `C:\System Volume Information` | Shadow copy | Tinggi |
| `NTUSER.DAT` | Registry hive user | Tinggi |
| `C:\Windows\Prefetch\*.pf` | Bukti eksekusi program | Tinggi |
| `winevt\Logs\Security.evtx` | Log keamanan/login | Tinggi |

---

## 14. Catatan Keamanan: Lokasi Sensitif dan Hardening Defensif

Lokasi berikut bernilai tinggi bagi penyerang maupun defender. Gunakan untuk audit izin, monitoring, dan hardening pada host yang kamu kelola, bukan sebagai resep penggalian kredensial ofensif.

```cmd
:: ── HIGH-VALUE PATHS (defender inventory) ────────────────────
C:\Windows\System32\config\SAM
C:\Windows\System32\config\SYSTEM
:: Protect with disk encryption, ACL lockdown, backup hygiene

HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
:: Disable AutoLogon cleartext; audit DefaultPassword presence

%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
:: Avoid secrets on CLI; enable PS logging instead of relying on history

C:\Windows\Panther\Unattend.xml
C:\Windows\system32\sysprep\sysprep.xml
:: Remove leftover unattend files from images

C:\inetpub\wwwroot\web.config
:: Secrets → vault / DPAPI / KeyVault, not plaintext in web.config

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
C:\Windows\System32\Tasks\
:: Inventory autoruns; alert on unexpected changes

C:\Windows\System32\winevt\Logs\Security.evtx
:: Forward to SIEM; protect local log tampering
```

### Fokus Hardening Defensif

| Kontrol | Catatan |
|---------|---------|
| BitLocker / enkripsi | Lindungi dari pencurian SAM secara offline |
| Tanpa secret AutoLogon | Hapus password AutoLogon cleartext |
| AlwaysInstallElevated | Pastikan dinonaktifkan |
| ACL service | Tidak ada path binary yang writable oleh user |
| Inventaris autorun | Baseline key Run dan scheduled task |
| Pembersihan Unattend | Buang dari golden image |
| Forwarding event | WEF / SIEM |

Password Winlogon dalam cleartext, file Unattend.xml yang tertinggal, dan binary service yang writable oleh user adalah temuan hardening kritis. Perbaiki dulu sebelum mempertimbangkan skenario red team apa pun.

### Tabel Prioritas Keamanan Windows

| Lokasi | Level risiko | Alasan |
|--------|---------------|--------|
| `System32\config\SAM` | Kritis | Hash password |
| `Winlogon registry key` | Kritis | Password cleartext |
| `PSReadline history` | Kritis | Riwayat perintah plus password |
| `hiberfil.sys` | Kritis | Dump RAM lengkap |
| `AppData\Credentials` | Tinggi | Kredensial yang di-cache |
| `NTUSER.DAT` | Tinggi | Registry hive user |
| `Security.evtx` | Tinggi | Event login |
| `Unattend.xml` | Kritis | Password admin dalam plaintext |
| `Prefetch files` | Sedang | Riwayat eksekusi |
| `$Recycle.Bin` | Sedang | File terhapus |

---

## Tabel Referensi Direktori Lengkap

| Direktori | Fungsi |
|-----------|--------|
| `C:\` | Drive sistem utama |
| `C:\Windows` | File inti OS |
| `C:\Windows\System32` | Binary sistem 64-bit |
| `C:\Windows\SysWOW64` | Binary sistem 32-bit |
| `C:\Windows\System32\config` | Registry hive plus SAM |
| `C:\Windows\System32\winevt` | Windows Event Logs |
| `C:\Windows\Temp` | Temp sistem |
| `C:\Windows\Prefetch` | Data prefetch |
| `C:\Users` | Semua profil user |
| `C:\Users\<user>\AppData` | Data aplikasi user |
| `C:\Program Files` | Aplikasi 64-bit |
| `C:\Program Files (x86)` | Aplikasi 32-bit |
| `C:\ProgramData` | Data aplikasi global |
| `C:\Temp` | Temp sistem alternatif |
| `C:\inetpub` | Root web server IIS |
| `C:\$Recycle.Bin` | File terhapus |

---

## Contoh Workflow Praktis

```cmd
:: ── SCENARIO: Windows post-exploitation filesystem recon ────

:: 1. Who am I and what privileges do I have?
> whoami
> whoami /priv
> whoami /groups
> net user %USERNAME%

:: 2. System information
> systeminfo
> hostname
> echo %COMPUTERNAME%
> echo %USERDOMAIN%

:: 3. List all local users
> net user
> net localgroup administrators

:: 4. Hunt for AutoLogon credentials (cleartext!)
> reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

:: 5. Check PowerShell history
> type "%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"

:: 6. List stored credentials
> cmdkey /list

:: 7. Find unattended install files
> dir /s /b C:\*.xml | findstr /i "unattend sysprep"
> type C:\Windows\Panther\Unattend.xml

:: 8. Check scheduled tasks for persistence
> schtasks /query /fo LIST /v | findstr /i "task\|run\|status"

:: 9. Check startup programs (persistence)
> reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
> dir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
> dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\"

:: 10. Find services with unquoted paths (privesc)
> wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """"

:: 11. Check AlwaysInstallElevated (privesc if both = 1)
> reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
> reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

:: 12. Find recent security events
PS> Get-WinEvent -LogName Security -MaxEvents 100 |
    Where-Object { $_.Id -in 4624,4625,4648,4672 } |
    Select-Object TimeCreated,Id,@{n='Message';e={$_.Message.Substring(0,100)}}

:: 13. Search for config files with passwords
PS> Get-ChildItem -Path C:\ -Recurse -Include "*.config","*.xml","*.ini","*.txt" -ErrorAction SilentlyContinue |
    Select-String -Pattern "password|passwd|pwd|secret|credential" -CaseSensitive:$false |
    Select-Object Path, LineNumber, Line | Select-Object -First 20
```

---

## Referensi Cepat

```cmd
:: ── NAVIGATION ───────────────────────────────────────────────
cd C:\                              :: go to C drive root
dir /a                              :: list all including hidden
dir /s /b *.txt                     :: recursive search
tree C:\ /f /a                      :: show full file tree

:: ── KEY ENVIRONMENT VARIABLES ────────────────────────────────
%SYSTEMROOT%    → C:\Windows
%USERPROFILE%   → C:\Users\alice
%APPDATA%       → C:\Users\alice\AppData\Roaming
%LOCALAPPDATA%  → C:\Users\alice\AppData\Local
%TEMP%          → C:\Users\alice\AppData\Local\Temp
%PROGRAMFILES%  → C:\Program Files
%PROGRAMDATA%   → C:\ProgramData

:: ── CREDENTIAL HUNTING ───────────────────────────────────────
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
cmdkey /list
type "%APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
dir /s /b C:\*pass* C:\*cred* C:\*vnc* C:\*.config 2>nul

:: ── REGISTRY (PERSISTENCE & PRIVESC) ─────────────────────────
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

:: ── SERVICES & TASKS ─────────────────────────────────────────
sc query type= all state= all
schtasks /query /fo LIST /v
wmic service get name,pathname,startmode | findstr /i "auto" | findstr /i /v "C:\Windows"

:: ── NETWORK INFO ─────────────────────────────────────────────
ipconfig /all
netstat -ano
arp -a
route print
net share
net use

:: ── USER & GROUPS ────────────────────────────────────────────
net user
net localgroup
net localgroup administrators
whoami /all
whoami /priv

:: ── SYSTEM INFO ──────────────────────────────────────────────
systeminfo
wmic os get Caption,Version,BuildNumber
wmic computersystem get Name,Domain,Manufacturer
ver

:: ── POWERSHELL EQUIVALENTS ───────────────────────────────────
PS> Get-ChildItem -Force -Recurse          :: dir /a /s
PS> Get-ItemProperty HKLM:\...\Run         :: reg query
PS> Get-WinEvent -LogName Security         :: Event logs
PS> Get-Service                            :: sc query
PS> Get-ScheduledTask                      :: schtasks
PS> Get-NetIPAddress                       :: ipconfig
PS> Get-NetTCPConnection                   :: netstat
PS> Get-LocalUser                          :: net user
PS> Get-LocalGroupMember Administrators    :: net localgroup administrators
```

---

> **Referensi dan Sumber Buku:**
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`), konteks metodologi berizin
> - Georgia Weidman, *Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - [Microsoft Docs — Windows File Systems](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - [LOLBAS Project](https://lolbas-project.github.io), untuk kesadaran defender

> **LearnCybersecurity** | Seri Dasar-Dasar | kodoktheGr3at | 2026
