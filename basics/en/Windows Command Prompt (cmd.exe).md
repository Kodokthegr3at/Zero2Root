# Windows Command Prompt (cmd.exe)

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-004` | **Phase 0:** Foundations
> **Est. study:** 3-4h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Gray Hat Hacking, Windows enumeration chapters
<!-- LC-CURRICULUM-END -->

## Table of Contents

1. What Command Prompt is
2. Navigating directories
3. File & folder management
4. System information
5. Network commands
6. Users & processes
7. Authorized host enumeration
8. Security notes: audit logging & LOLBin defense
9. Quick reference cheatsheet

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Command Prompt (CMD) | Windows' classic text command interpreter (`cmd.exe`) |
| Shell | A program that runs typed commands |
| Working directory | The folder your commands act on right now |
| Environment variable | A named value the system stores, like `%USERPROFILE%` |
| Pipe (`\|`) | Sending one command's output into another |
| Built-in vs external | Some commands live inside CMD; others are separate `.exe` programs |
| LOLBin | A "living off the land binary": a legitimate built-in tool an attacker reuses for malicious ends |
| Enumeration | Gathering facts about a host (users, shares, services) you're authorized to inspect |

---

## 1. Overview: What is Command Prompt

**Command Prompt** (`cmd.exe`) is Windows' built-in command-line interpreter that lets users interact with the operating system through text commands, without needing a graphical interface (GUI). cmd.exe has existed since the MS-DOS era and is still widely used today.

From a cybersecurity perspective, understanding CMD is useful for:
- System enumeration after gaining access (post-exploitation)
- Scripting and automation using batch files (`.bat`)
- Network and system troubleshooting

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

## 2. Directory Navigation

Navigation commands are used to move between directories and view folder contents, equivalent to `cd` and `ls` on Linux.

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

| Command | Function |
|---------|----------|
| `cd` | Show/change directory |
| `cd ..` | Go up one level |
| `cd \` | Go to drive root |
| `dir` | List folder contents |
| `dir /a` | Include hidden files |
| `dir /s` | Recursive (all subfolders) |
| `tree` | Display folder structure |

---

## 3. File & Folder Management

These commands are used to create, copy, move, and delete files and folders.

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

| Command | Function |
|---------|----------|
| `mkdir` / `md` | Create new folder |
| `rmdir` / `rd` | Remove folder |
| `copy` | Copy file |
| `xcopy` | Advanced copy for folders/files |
| `move` | Move file/folder |
| `ren` | Rename |
| `del` | Delete file |
| `type` | Display text file contents |
| `findstr` | Search text within files |

---

## 4. System Information

These commands are used to retrieve system information such as OS version, hardware, and configuration.

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

| Command | Function |
|---------|----------|
| `systeminfo` | Full system information |
| `ver` | OS version |
| `set` | Show environment variables |
| `wmic qfe list` | List installed hotfixes |
| `wmic product get name,version` | List installed software |
| `cls` | Clear screen |

Pentesting note: `systeminfo` and `wmic qfe list` are commonly used to check for missing patches that may indicate vulnerable, exploitable systems.

---

## 5. Network Commands

Network commands are used for connectivity diagnostics, viewing IP configuration, and network troubleshooting.

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

| Command | Function |
|---------|----------|
| `ipconfig` | Show IP configuration |
| `ipconfig /all` | Detailed IP configuration |
| `ping` | Test connectivity |
| `tracert` | Trace route to host |
| `netstat -ano` | Active connections + PID |
| `arp -a` | Show ARP table |
| `nslookup` | DNS lookup |
| `net view` | List computers on network |

Pentesting note: `netstat -ano` combined with `tasklist` helps identify which process owns a suspicious open port.

---

## 6. Users & Processes

These commands are used to manage user accounts and monitor running processes on the system.

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

| Command | Function |
|---------|----------|
| `whoami` | Show current user |
| `whoami /priv` | Show user privileges |
| `net user` | List all local users |
| `net user /add` | Create new user |
| `net localgroup administrators` | Manage administrators group |
| `tasklist` | List running processes |
| `taskkill` | Terminate a process |

Important: always run CMD as Administrator when using `net user /add` or `net localgroup`, since these require elevated privileges.

---

## 7. Authorized Host Enumeration

On authorized engagements or your own lab, the following commands help inventory a Windows host and audit its configuration. This is not an offensive PrivEsc recipe.

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

Note: these commands are intended for authorized penetration testing, defensive audits, and CTF/lab environments only.

---

## 8. Security Note: CMD Hardening, Audit & LOLBin Awareness

`cmd.exe` and its built-in utilities (living-off-the-land binaries) are used by attackers and admins alike. Defense means reducing privilege, enabling audit, and monitoring abuse of legitimate binaries.

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

| Control | Description |
|---------|--------------|
| Least privilege | No daily admin shell |
| Process creation audit | 4688 + command line |
| WDAC / AppLocker | Restrict `cmd` / script hosts |
| LOLBAS monitoring | Alert on anomalous LOLBin use |
| Credential hygiene | Never echo passwords |

Defense-first: treat unexpected `cmd.exe /c` chains, `sc`/`schtasks` changes, and mass `findstr` scans over user profiles as hunt signals, not just noise.

---

## Command Summary Table

| Command | Function | Admin needed? |
|---------|----------|----------------|
| `dir` | List folder contents | No |
| `cd` | Change directory | No |
| `mkdir` / `rmdir` | Create/remove folder | No (system folders: Yes) |
| `copy` / `move` | Copy/move file | No |
| `del` | Delete file | No |
| `systeminfo` | System info | No |
| `ipconfig` | Network configuration | No |
| `ping` / `tracert` | Network testing | No |
| `netstat -ano` | Active connections | No |
| `whoami` | Current user | No |
| `net user /add` | Create user | Yes |
| `net localgroup` | Manage groups | Yes |
| `tasklist` / `taskkill` | Manage processes | No (some processes: Yes) |
| `sc query` | List services | No |
| `schtasks` | Scheduled tasks | No (some actions: Yes) |

---

## Practical Workflow Example

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

## Quick Reference Cheatsheet

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

---

> **References & Book Sources:**
> - Peter Kim, *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`), authorized methodology context
> - Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking* (`~/Documents/Books/CyberSec/Ethical Hacking/`)
> - Allen Harper et al., *Gray Hat Hacking* (`~/Documents/Books/CyberSec/Handbook/`)
> - Microsoft Docs, [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands), Audit Process Creation
> - [LOLBAS Project](https://lolbas-project.github.io), defender awareness of living-off-the-land binaries
> - `help`, `<command> /?`

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
