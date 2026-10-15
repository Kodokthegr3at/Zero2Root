# Windows File System

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-006` | **Phase 0:** Foundations
> **Est. study:** 5-6h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Gray Hat Hacking (NTFS, Registry, ADS)
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic |
|---|-------|
| 1 | What is the Windows File System |
| 2 | Drive letter system |
| 3 | Full directory tree |
| 4 | `C:\Windows` |
| 5 | `C:\Windows\System32` |
| 6 | `C:\Users` |
| 7 | `C:\Program Files` |
| 8 | `C:\ProgramData` |
| 9 | `C:\Temp` & `%TEMP%` |
| 10 | Registry |
| 11 | Environment variables |
| 12 | NTFS & permissions |
| 13 | Hidden & special files |
| 14 | Sensitive locations & hardening |
| 15 | Practical recon navigation |

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Drive letter | Windows gives each volume a letter (`C:`, `D:`) instead of one root |
| NTFS | The modern Windows file system (permissions, journaling, encryption) |
| Path | A file's location; Windows uses backslashes (`C:\Users\alex`) |
| Environment variable | A named shortcut for a path, like `%APPDATA%` or `%SystemRoot%` |
| Registry | Windows' central settings database, separate from the file tree |
| ACL | Access Control List: the per-file rules for who may read/write/execute |
| ADS | Alternate Data Stream: hidden data NTFS can attach to a file |
| Hidden / system file | Files flagged so they don't show by default |

---

## 1. Overview: What Is the Windows File System

The Windows file system uses a drive letter structure (C:, D:, E:, and so on), unlike Linux, which uses one directory tree rooted at `/`. Each drive carries its own directory hierarchy.

Modern Windows runs on NTFS (New Technology File System), which supports:
- Granular per file and folder permissions through ACLs
- Alternate Data Streams (ADS), hidden data attached to a file
- File and folder encryption (EFS)
- Journaling, for recovery after a system failure
- Symbolic links and junctions

This matters for cybersecurity work in a few concrete ways:
- Knowing where credentials and config files sit gives you reconnaissance targets
- Understanding NTFS permissions is a prerequisite for privilege escalation
- Knowing where logs live supports forensics and incident response
- Understanding the Registry matters for persistence and malware analysis
- Knowing which directories are writable matters for payload staging

---

## 2. Drive Letters: The Windows Drive System

Windows uses drive letters to identify partitions and storage devices. By default, the primary drive where Windows is installed is `C:\`. Other drives (USB, CD, additional partitions) get the next available letter in sequence.

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

| Drive Letter | Common Use |
|-------------|------------|
| `A:` / `B:` | Floppy disk (legacy) |
| `C:` | Primary system drive |
| `D:` | Secondary drive / DVD |
| `E:` onward | USB, extra partitions |

---

## 3. File Tree: Full Directory Structure

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

## 4. `C:\Windows`: Main System Directory

`C:\Windows` is the core directory of the Windows operating system, roughly analogous to `/` in Linux, though scoped to the OS itself rather than the whole filesystem. It holds all critical OS components, drivers, system config files, and logs. Only Administrator and SYSTEM accounts should modify its contents.

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

| Subdirectory | Contents |
|-------------|----------|
| `System32\` | 64-bit system binaries & DLLs |
| `SysWOW64\` | 32-bit system binaries |
| `Temp\` | System temp files |
| `Prefetch\` | Program prefetch data |
| `Logs\` | Additional system logs |
| `inf\` | Driver information files |
| `Fonts\` | System font files |

---

## 5. `C:\Windows\System32`: Heart of Windows

`System32` is the single most important directory in Windows. It holds the core system binaries, DLLs (Dynamic Link Libraries), drivers, registry config files, and event logs. It is a primary pentesting target because it contains the SAM database (password hashes) and the event logs.

> Despite the name "System32", on 64-bit Windows this directory contains 64-bit binaries. 32-bit binaries live in `SysWOW64`.

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

### Critical Files in `System32\config\`

| File | Contents | Pentest Value |
|------|----------|----------------|
| `SAM` | Local account password hashes | Critical |
| `SYSTEM` | System config, boot key | Critical |
| `SECURITY` | Local security policies | High |
| `SOFTWARE` | Installed software & config | Medium |
| `DEFAULT` | Default user profile | Low |

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

## 6. `C:\Users`: User Directories

`C:\Users` holds a profile directory for every user who has ever logged into the system. Each user gets a directory with the same layout, including the hidden `AppData` folder, which stores application data, saved credentials, and history.

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

### High-Value Files in `C:\Users\<username>\`

| Path | Contents | Pentest Value |
|------|----------|----------------|
| `NTUSER.DAT` | User registry hive | High |
| `AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt` | PowerShell history | Critical |
| `AppData\Roaming\Microsoft\Credentials\` | Cached domain credentials | Critical |
| `AppData\Local\Microsoft\Credentials\` | Cached local credentials | High |
| `AppData\Local\Google\Chrome\User Data\Default\Login Data` | Chrome browser passwords | High |
| `AppData\Roaming\Mozilla\Firefox\Profiles\` | Firefox profile | High |
| `.ssh\id_rsa` | SSH private key | High |
| `Desktop\` | Files on desktop | Medium |
| `Documents\` | User documents | Medium |

---

## 7. `C:\Program Files`: Installed Applications

`C:\Program Files` is the default location for 64-bit application installs. `C:\Program Files (x86)` holds 32-bit applications on 64-bit systems. Writing to either directory requires Administrator rights.

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

> Pentesting note: an application in `Program Files` that ships with overly permissive folder or binary permissions can become a privilege escalation vector through DLL hijacking or binary planting.

---

## 8. `C:\ProgramData`: Global Application Data

`C:\ProgramData` is a hidden directory that stores application data shared across all users. Unlike `AppData`, which is per user, `ProgramData` is global. It usually holds config files, databases, and application logs.

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

## 9. `C:\Temp` & `%TEMP%`: Temporary Files

Windows keeps two temp locations: `C:\Windows\Temp` (system-wide) and `%TEMP%` (per user, typically `C:\Users\<user>\AppData\Local\Temp`). Both can be used for payload staging, and both often hold temporary artifacts that are useful for forensics.

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

The Windows Registry is a centralized, hierarchical database that stores system configuration, application settings, and user information. It is the single most important component to understand for Windows pentesting: it is the primary location for persistence, credential storage, and system configuration.

The Registry is organized into main hives (root keys):

| Hive | Abbreviation | Contents |
|------|---------------|----------|
| `HKEY_LOCAL_MACHINE` | `HKLM` | Local machine configuration |
| `HKEY_CURRENT_USER` | `HKCU` | Current user configuration |
| `HKEY_USERS` | `HKU` | All user profiles |
| `HKEY_CLASSES_ROOT` | `HKCR` | File associations & COM objects |
| `HKEY_CURRENT_CONFIG` | `HKCC` | Current hardware profile |

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

### Critical Registry Keys for Pentesting

| Registry Key | Contents | Pentest Value |
|-------------|----------|----------------|
| `HKLM\SAM` | Local password hashes | Critical |
| `HKLM\SYSTEM\CurrentControlSet\Services` | Service list | High |
| `HKLM\SOFTWARE\...\Winlogon` | Auto-logon credentials | Critical |
| `HKCU\...\Run` | User startup programs | High |
| `HKLM\...\Run` | System startup programs | High |
| `HKCU\Software\SimonTatham\PuTTY` | PuTTY sessions/passwords | High |

---

## 11. Environment Variables: Windows Env Vars

Environment variables store information about the system environment. On Windows, you reach them with `%` signs in CMD or `$env:` in PowerShell. They are useful for navigation because they point to important directories without requiring the full path.

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

| Variable | Points to |
|----------|-----------|
| `%SYSTEMROOT%` | Windows directory |
| `%USERPROFILE%` | User home directory |
| `%APPDATA%` | AppData Roaming |
| `%TEMP%` | User temp folder |
| `%PROGRAMFILES%` | Program Files 64-bit |
| `%COMPUTERNAME%` | Computer name |
| `%USERNAME%` | Current username |

---

## 12. NTFS & Permissions: File System Security

NTFS uses an ACL (Access Control List) system to control access permissions. Every file and folder carries a DACL (Discretionary ACL) that determines who can do what. Understanding NTFS permissions matters for both privilege escalation and forensics.

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

### NTFS Permission Types

| Permission | Symbol | Meaning |
|-----------|--------|---------|
| Full Control | `F` | All rights |
| Modify | `M` | Read, write, delete |
| Read & Execute | `RX` | Read & run |
| Read | `R` | Read only |
| Write | `W` | Write only |

---

## 13. Special & Hidden Files

Windows hides various files and directories from normal view. A file can be "hidden" in several ways: the hidden attribute, the system attribute, or simply by sitting in a non-indexed location. Some of these files matter a great deal for forensics and pentesting.

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

### Important Hidden Files

| File/Directory | Contents | Pentest Value |
|---------------|----------|----------------|
| `C:\pagefile.sys` | Virtual memory | High |
| `C:\hiberfil.sys` | RAM dump at hibernate | Critical |
| `C:\$Recycle.Bin` | Deleted files | Medium |
| `C:\System Volume Information` | Shadow copies | High |
| `NTUSER.DAT` | User registry hive | High |
| `C:\Windows\Prefetch\*.pf` | Program execution evidence | High |
| `winevt\Logs\Security.evtx` | Security/login logs | High |

---

## 14. Security Note: Sensitive Locations & Defensive Hardening

These locations are high-value to attackers and defenders alike. Use them for permission audits, monitoring, and hardening on hosts you manage, not as an offensive credential-dumping recipe.

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

### Defensive Hardening Focus

| Control | Notes |
|---------|-------|
| BitLocker / encryption | Protect against offline SAM theft |
| No AutoLogon secrets | Remove cleartext AutoLogon |
| AlwaysInstallElevated | Ensure it is disabled |
| Service ACLs | No user-writable binary paths |
| Autoruns inventory | Baseline Run keys & scheduled tasks |
| Unattend cleanup | Strip from golden images |
| Event forwarding | WEF / SIEM |

> Defense-first: treat cleartext Winlogon passwords, leftover Unattend.xml files, and user-writable service binaries as critical hardening findings. Remediate them before entertaining any red team narrative.

### Windows Security Priority Table

| Location | Risk Level | Reason |
|----------|--------------|--------|
| `System32\config\SAM` | Critical | Password hashes |
| `Winlogon registry key` | Critical | Cleartext password |
| `PSReadline history` | Critical | Command history + passwords |
| `hiberfil.sys` | Critical | Full RAM dump |
| `AppData\Credentials` | High | Cached credentials |
| `NTUSER.DAT` | High | User registry hive |
| `Security.evtx` | High | Login events |
| `Unattend.xml` | Critical | Admin password in plaintext |
| `Prefetch files` | Medium | Execution history |
| `$Recycle.Bin` | Medium | Deleted files |

---

## Complete Directory Reference Table

| Directory | Function |
|-----------|----------|
| `C:\` | Primary system drive |
| `C:\Windows` | Core OS files |
| `C:\Windows\System32` | 64-bit system binaries |
| `C:\Windows\SysWOW64` | 32-bit system binaries |
| `C:\Windows\System32\config` | Registry hives + SAM |
| `C:\Windows\System32\winevt` | Windows Event Logs |
| `C:\Windows\Temp` | System temp |
| `C:\Windows\Prefetch` | Prefetch data |
| `C:\Users` | All user profiles |
| `C:\Users\<user>\AppData` | User app data |
| `C:\Program Files` | 64-bit applications |
| `C:\Program Files (x86)` | 32-bit applications |
| `C:\ProgramData` | Global app data |
| `C:\Temp` | Alternate system temp |
| `C:\inetpub` | IIS web server root |
| `C:\$Recycle.Bin` | Deleted files |

---

## Practical Workflow Example

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

## Quick Reference Cheatsheet

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

> **References & Book Sources:**
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`), authorized methodology context
> - Georgia Weidman, *Penetration Testing* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - [Microsoft Docs — Windows File Systems](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)
> - [HackTheBox Academy - Windows Fundamentals](https://academy.hackthebox.com)
> - [LOLBAS Project](https://lolbas-project.github.io), for defender awareness

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026
