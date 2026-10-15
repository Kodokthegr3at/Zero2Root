# Git: Version Control System

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-002` | **Phase 0:** Foundations
> **Est. study:** 3-4h | **Level:** Beginner
> **Prerequisites:** LC-001
> **Book map:** Shotts, The Linux Command Line Ch.17-18 (VCS concepts)
<!-- LC-CURRICULUM-END -->

## Table of Contents

1. What Git and version control are
2. Installing and configuring Git
3. Core concepts
4. `git init` and `git clone`
5. Staging and committing
6. Branching and merging
7. Working with remotes
8. History and undo
9. `.gitignore`
10. A collaboration workflow
11. Security notes
12. A full worked example

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Repository (repo) | A project folder that Git tracks, including its full history |
| Commit | A saved snapshot of your changes at one point in time |
| Branch | A separate line of work you can develop without touching `main` |
| Staging area | A waiting room where you line up changes before committing |
| HEAD | A pointer to the commit/branch you're currently on |
| Remote | A copy of the repo on another server, such as GitHub |
| Clone | Downloading a full copy of a remote repo |
| Push / pull | Sending your commits to a remote / fetching and merging theirs |
| Merge | Combining the work from one branch into another |
| `.gitignore` | A list of files Git should never track (secrets, build output) |

---

## 1. Overview: What Is Git and Version Control

Git is a distributed version control system that tracks changes to files over time, letting multiple people collaborate on the same project without overwriting each other's work. Linus Torvalds wrote it in 2005 to manage Linux kernel development.

Unlike centralized version control such as SVN, Git is distributed: every contributor holds a complete copy of the entire repository history on their local machine, not just the latest snapshot. A useful way to think about it is as a time machine for code. You can view, compare, and revert to any past version of a project at any point.

Git matters for security work in a few specific ways. Many security tools are distributed through GitHub and installed with `git clone`. Public repositories frequently contain credentials that were committed by accident. Understanding the `.git` folder helps with source code forensics and leak investigations, and Git history can resurface sensitive data that was "deleted" from the working tree but is still sitting in an earlier commit.

## 2. Installation and Initial Configuration

Before using Git, you install it and set an identity (name and email) that gets attached to every commit you make.

```bash
# ── INSTALL GIT ──────────────────────────────────────────────

# Debian/Ubuntu/Kali/Parrot
$ sudo apt install git -y

# RedHat/CentOS/Fedora
$ sudo yum install git -y
$ sudo dnf install git -y

# macOS (via Homebrew)
$ brew install git

# Verify installation
$ git --version
git version 2.43.0

# ── INITIAL CONFIGURATION ────────────────────────────────────

# Set your name (used in every commit)
$ git config --global user.name "kodoktheGr3at"

# Set your email
$ git config --global user.email "kodok@example.com"

# Set default branch name
$ git config --global init.defaultBranch main

# Set default editor (optional)
$ git config --global core.editor vim

# View all current config
$ git config --list

# View a specific config value
$ git config user.name

# Edit config file directly
$ git config --global --edit
```

| Scope | Applies to | Config location |
|-------|------------|------------------|
| `--local` | Current repo only | `.git/config` |
| `--global` | All repos for this user | `~/.gitconfig` |
| `--system` | All users on the machine | `/etc/gitconfig` |

## 3. Core Concepts

Before running commands, it helps to know the core terminology.

- Repository (repo): a project folder tracked by Git, containing the entire history of changes.
- Commit: a snapshot of changes saved permanently to the history.
- Branch: an independent line of development for the project (default: `main` or `master`).
- Working directory: the files you're currently editing on disk.
- Staging area (index): a waiting area for changes before they're actually committed.
- HEAD: a pointer to the currently active commit or branch.
- Remote: a copy of the repository stored on another server, such as GitHub.

### The Three States of a File

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository (.git)
   (modified)                     (staged)                       (committed)
```

| State | Meaning |
|-------|---------|
| Untracked | New file, not yet tracked by Git |
| Modified | File changed but not staged |
| Staged | File ready to be committed |
| Committed | File permanently saved to history |

## 4. `git init` and `git clone`: Creating and Downloading Repos

There are two ways to start working with a repository: create a new one from a local folder with `git init`, or download an existing one from a remote server with `git clone`.

```bash
# ── GIT INIT — create a new repository ──────────────────────

# Create and initialize a new repo
$ mkdir myproject && cd myproject
$ git init

Initialized empty Git repository in /home/user/myproject/.git/

# This creates a hidden .git/ folder containing all Git metadata
$ ls -la
.git/   ← all version history lives here

# ── GIT CLONE — download an existing repository ─────────────

# Clone a repository into a new directory
$ git clone https://github.com/samratashok/nishang.git

Cloning into 'nishang'...
remote: Enumerating objects: 1691, done.
Receiving objects: 100% (1691/1691), 7.84 MiB | 4.86 MiB/s, done.

# Clone into a specific directory name
$ git clone https://github.com/samratashok/nishang.git ~/tools/nishang

# Clone a specific branch only
$ git clone -b develop https://github.com/username/repo.git

# Clone with limited history (faster, smaller download)
$ git clone --depth 1 https://github.com/username/repo.git

# Clone via SSH (requires SSH key set up)
$ git clone git@github.com:username/repo.git
```

| Command | Function |
|---------|----------|
| `git init` | Create a new repo in a local folder |
| `git clone <url>` | Download a repo from a remote |
| `git clone -b <branch>` | Clone only a specific branch |
| `git clone --depth N` | Clone with limited history |

## 5. Staging and Commit: Saving Your Changes

Git saves changes in two steps: you stage the files you want to save with `git add`, then commit to save them permanently to history with `git commit`.

```bash
# ── CHECK STATUS ─────────────────────────────────────────────
$ git status

On branch main
Changes not staged for commit:
  modified:   index.html
Untracked files:
  new_script.sh

# ── STAGING (git add) ────────────────────────────────────────

# Stage a specific file
$ git add index.html

# Stage multiple files
$ git add file1.txt file2.txt

# Stage all changed files in current directory
$ git add .

# Stage all changes in the entire repo
$ git add -A

# Unstage a file (remove from staging area)
$ git restore --staged index.html

# ── COMMITTING (git commit) ──────────────────────────────────

# Commit with an inline message
$ git commit -m "Add login validation script"

# Commit with both subject and detailed body
$ git commit -m "Fix SQL injection vulnerability" -m "Sanitized user input on login form to prevent SQLi attacks"

# Stage AND commit tracked files in one step
$ git commit -am "Quick fix for typo"

# Amend the previous commit (e.g. fix a typo in message)
$ git commit --amend -m "Corrected commit message"

# View the diff of staged changes before committing
$ git diff --staged
```

| Command | Function |
|---------|----------|
| `git status` | Check file status |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all files in this folder |
| `git commit -m "msg"` | Commit with a message |
| `git commit -am "msg"` | Stage and commit in one step |
| `git diff` | View unstaged changes |
| `git diff --staged` | View staged changes |

## 6. Branching: Branches and Merging

Branches let you develop features, fix bugs, or experiment in isolation from the main codebase (`main`). Once you're done, a branch can be merged back into the main branch.

```bash
# ── CREATE & SWITCH BRANCHES ─────────────────────────────────

# List all branches (current marked with *)
$ git branch
* main
  feature-login

# Create a new branch (without switching to it)
$ git branch feature-payment

# Create AND switch to a new branch in one step
$ git checkout -b feature-payment
$ git switch -c feature-payment    # modern alternative

# Switch to an existing branch
$ git checkout main
$ git switch main                  # modern alternative

# Rename current branch
$ git branch -m old-name new-name

# Delete a branch (after merging)
$ git branch -d feature-payment

# Force delete a branch (even if not merged)
$ git branch -D feature-payment

# ── MERGING ───────────────────────────────────────────────────

# Switch to the branch you want to merge INTO (e.g. main)
$ git checkout main

# Merge another branch into the current branch
$ git merge feature-payment

# ── HANDLING MERGE CONFLICTS ─────────────────────────────────
# When Git can't auto-merge, it marks conflicts in the file:
<<<<<<< HEAD
your current code
=======
incoming code from merged branch
>>>>>>> feature-payment

# After manually resolving conflicts:
$ git add <resolved-file>
$ git commit -m "Resolve merge conflict"

# ── REBASING (alternative to merge, cleaner history) ─────────
$ git checkout feature-payment
$ git rebase main
```

| Command | Function |
|---------|----------|
| `git branch` | List all branches |
| `git branch <name>` | Create a new branch |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git checkout <name>` | Switch to a branch |
| `git merge <name>` | Merge a branch into the current one |
| `git branch -d <name>` | Delete a branch |
| `git rebase <name>` | Re-apply commits on top of another base |

## 7. Remote: Working with Remote Repositories

A remote is a copy of the repository stored on another server, such as GitHub, GitLab, or Bitbucket. You interact with remotes using `git push` to send changes and `git pull` to fetch them.

```bash
# ── MANAGING REMOTES ─────────────────────────────────────────

# View configured remotes
$ git remote -v
origin  https://github.com/username/repo.git (fetch)
origin  https://github.com/username/repo.git (push)

# Add a new remote
$ git remote add origin https://github.com/username/repo.git

# Change a remote's URL
$ git remote set-url origin git@github.com:username/repo.git

# Remove a remote
$ git remote remove origin

# ── PUSHING & PULLING ────────────────────────────────────────

# Push current branch to remote
$ git push origin main

# Push and set upstream tracking (first push of a new branch)
$ git push -u origin feature-payment

# Pull latest changes from remote (fetch + merge)
$ git pull origin main

# Fetch changes without merging (review first)
$ git fetch origin
$ git log origin/main

# Force push (DANGEROUS — overwrites remote history)
$ git push --force origin main
```

| Command | Function |
|---------|----------|
| `git remote -v` | View connected remotes |
| `git remote add <name> <url>` | Add a new remote |
| `git push origin <branch>` | Push commits to a remote |
| `git pull origin <branch>` | Fetch and merge from a remote |
| `git fetch` | Fetch without merging |

`git push --force` is a dangerous operation: it overwrites history on the remote and can wipe out a teammate's work. Use `--force-with-lease` instead, which refuses to overwrite commits you haven't seen yet.

## 8. History and Undo: Viewing History and Reverting Changes

Git keeps the entire history of a project's changes and gives you plenty of ways to view that history or undo changes when you need to.

```bash
# ── VIEWING HISTORY ──────────────────────────────────────────

# View commit history
$ git log

commit a1b2c3d4e5f6...
Author: kodoktheGr3at <kodok@example.com>
Date:   Mon Jun 23 10:00:00 2026 +0900
    Add login validation script

# Compact one-line log
$ git log --oneline

a1b2c3d Add login validation script
f6e5d4c Initial commit

# Visual graph of branches
$ git log --oneline --graph --all

# Show changes in each commit
$ git log -p

# Show commits by a specific author
$ git log --author="kodoktheGr3at"

# Show who changed each line of a file
$ git blame index.html

# ── UNDOING CHANGES ──────────────────────────────────────────

# Discard changes in working directory (unstaged)
$ git restore index.html

# Unstage a file (keep changes, remove from staging)
$ git restore --staged index.html

# Revert a specific commit (creates a new "undo" commit)
$ git revert a1b2c3d

# Reset to a previous commit, KEEPING changes unstaged
$ git reset a1b2c3d

# Reset to a previous commit, DISCARDING all changes (DANGEROUS)
$ git reset --hard a1b2c3d

# Temporarily save uncommitted changes without committing
$ git stash

# List stashed changes
$ git stash list

# Reapply the most recent stash
$ git stash pop
```

| Command | Function |
|---------|----------|
| `git log` | View commit history |
| `git log --oneline` | Compact one-line history |
| `git blame <file>` | See who changed each line |
| `git restore <file>` | Discard unstaged changes |
| `git revert <commit>` | Undo a commit by creating a new one |
| `git reset --hard <commit>` | Go back and discard all changes |
| `git stash` | Temporarily save changes |

`git reset --hard` is destructive: any uncommitted changes are lost permanently. Make sure you actually want to throw the changes away before running it.

## 9. `.gitignore`: Ignoring Files

A `.gitignore` file tells Git which files or folders to ignore and never track. It matters for keeping sensitive files (credentials, API keys), build artifacts, and temporary files out of the repository.

```bash
# Create a .gitignore file in the repo root
$ vim .gitignore
```

```gitignore
# ── EXAMPLE .gitignore ──────────────────────────────────────

# Sensitive files — NEVER commit these!
.env
*.pem
*.key
secrets.yaml
config/credentials.json

# Dependency directories
node_modules/
venv/
__pycache__/

# Build output
dist/
build/
*.exe
*.o

# OS-specific files
.DS_Store
Thumbs.db

# IDE/editor files
.vscode/
.idea/
*.swp

# Logs
*.log
logs/
```

```bash
# Check if a file is ignored
$ git check-ignore -v config/credentials.json

# Remove a file that's already tracked, then ignore it
$ git rm --cached secrets.yaml
$ echo "secrets.yaml" >> .gitignore
$ git commit -m "Remove secrets file and add to gitignore"
```

Adding a file to `.gitignore` does not remove it from history if it was already committed before. For that you need `git filter-repo` or the BFG Repo-Cleaner to rewrite history and strip it out permanently.

## 10. Git Workflow: A Collaboration Pattern

A common workflow for collaborating on Git and platforms like GitHub follows a standard shape: fork or clone, branch, commit, push, pull request.

```bash
# ── STANDARD COLLABORATION WORKFLOW ──────────────────────────

# 1. Fork the repo on GitHub (via web UI), then clone your fork
$ git clone https://github.com/yourusername/repo.git
$ cd repo

# 2. Add the original repo as "upstream" to stay in sync
$ git remote add upstream https://github.com/original-owner/repo.git

# 3. Create a feature branch
$ git checkout -b fix-xss-vulnerability

# 4. Make changes and commit
$ git add .
$ git commit -m "Fix XSS vulnerability in comment form"

# 5. Keep your branch up to date with upstream
$ git fetch upstream
$ git rebase upstream/main

# 6. Push your branch to your fork
$ git push origin fix-xss-vulnerability

# 7. Open a Pull Request on GitHub (via web UI)

# 8. After PR is merged, clean up
$ git checkout main
$ git pull upstream main
$ git branch -d fix-xss-vulnerability
```

### Common Workflow Strategies

| Strategy | Best for |
|----------|----------|
| Git Flow | Large projects with scheduled releases |
| GitHub Flow | Continuous deployment, kept simple |
| Trunk-Based | Small teams, fast integration |
| Fork and PR | Open source, external contributors |

## 11. Security Note: Credential Hygiene and Secret Scanning

Git history keeps forever anything that was once committed. The point of this section is preventing credential leaks and catching secrets before they get pushed, in repositories you own or maintain, not hunting for credentials in someone else's history.

```bash
# ── PREVENT: stop secrets from entering commits ──────────────
# Strong .gitignore patterns (always review before first push)
echo -e '.env\n.env.*\n*.pem\n*.key\nid_rsa\nid_ed25519\n*.p12\ncredentials.json' >> .gitignore

# Pre-commit secret scanning (developer workstation / CI)
# Install gitleaks or trufflehog as a pre-commit / CI gate
gitleaks detect --source . --verbose
# Or: pre-commit hook running gitleaks protect --staged

# Block common patterns in CI (fail the pipeline on findings)
gitleaks detect --source . --report-path gitleaks-report.json --exit-code 1

# ── DETECT: audit repositories you own or maintain ───────────
# Scan local clone history for accidentally committed secrets
gitleaks detect --source . --log-opts="--all"
trufflehog git file://. --only-verified   # prefer verified findings

# Search your own history for known secret markers (ops hygiene)
git log --all -p -S 'AKIA' -- '*.env' '*.yml' '*.json' 2>/dev/null | head

# ── RESPOND: if a secret was committed ───────────────────────
# 1) Rotate/revoke the credential immediately (primary control)
# 2) Remove from future commits (.gitignore + rewrite only if policy allows)
# 3) Treat old history as compromised until rotation completes
# 4) Use BFG/filter-repo only on repos you control, then re-sync with team policy
```

### Defensive Controls Checklist

| Control | Action |
|---------|--------|
| `.gitignore` templates | Block `.env`, keys, PEMs by default |
| Pre-commit / CI scanners | `gitleaks` or TruffleHog gate on push |
| Short-lived tokens | Prefer OIDC or short-lived PATs |
| Secret managers | Vault or cloud secret manager, not the repo |
| Rotation runbook | Revoke first, clean history second |
| Protected branches + CODEOWNERS | Require review before merge |
| No `.git` on web roots | Never deploy `.git` to production |

Treat any accidental commit of a secret as a confirmed compromise of that secret. Rotation beats history rewriting, and running scanners in CI means the check doesn't depend on a human catching it.

## 12. Practical Workflow Example

```bash
# ── SCENARIO: Start a new project and push to GitHub ─────────

# 1. Configure identity (once per machine)
$ git config --global user.name "kodoktheGr3at"
$ git config --global user.email "kodok@example.com"

# 2. Create project folder and initialize repo
$ mkdir security-notes && cd security-notes

# 3. Create initial files
$ echo "# Security Notes" > README.md
$ echo "*.log" > .gitignore
$ echo ".env" >> .gitignore

# 4. Stage and commit
$ git add .
$ git commit -m "Initial commit"

# 5. Create a feature branch
$ git checkout -b add-recon-notes

# 6. Add new files and commit
$ echo "notes on recon methodology" > recon.md
$ git add recon.md
$ git commit -m "Add recon methodology notes"

# 7. Switch back to main and merge
$ git checkout main
$ git merge add-recon-notes

# 8. Connect to GitHub remote
$ git remote add origin https://github.com/kodoktheGr3at/security-notes.git

# 9. Push to GitHub
$ git push -u origin main

# 10. Clone the repo on another machine later
$ git clone https://github.com/kodoktheGr3at/security-notes.git

# 11. Pull latest updates
$ cd security-notes && git pull origin main
```

### Command Summary

```bash
# ── SETUP ────────────────────────────────────────────────────
git config --global user.name "Name"     # set username
git config --global user.email "email"   # set email
git --version                             # check version

# ── CREATE / CLONE ───────────────────────────────────────────
git init                                  # create new repo
git clone <url>                           # clone existing repo
git clone <url> <dir>                     # clone into specific dir
git clone -b <branch> <url>               # clone specific branch

# ── BASIC WORKFLOW ───────────────────────────────────────────
git status                                # check status
git add <file>                            # stage a file
git add .                                 # stage everything
git commit -m "message"                   # commit staged changes
git commit -am "message"                  # stage + commit (tracked files)
git push origin <branch>                  # push to remote
git pull origin <branch>                  # pull from remote

# ── BRANCHING ────────────────────────────────────────────────
git branch                                # list branches
git checkout -b <name>                    # create + switch branch
git checkout <name>                       # switch branch
git merge <name>                          # merge branch into current
git branch -d <name>                      # delete branch

# ── HISTORY ──────────────────────────────────────────────────
git log                                   # view history
git log --oneline --graph --all           # visual history
git diff                                  # unstaged changes
git diff --staged                         # staged changes
git blame <file>                          # who changed each line

# ── UNDO ─────────────────────────────────────────────────────
git restore <file>                        # discard unstaged changes
git restore --staged <file>               # unstage a file
git revert <commit>                       # undo commit (safe)
git reset --hard <commit>                 # discard everything (danger!)
git stash                                 # temporarily save changes
git stash pop                             # reapply stashed changes

# ── REMOTE ───────────────────────────────────────────────────
git remote -v                             # list remotes
git remote add origin <url>               # add remote
git fetch origin                          # fetch without merging

# ── SECRET HYGIENE (repos you own) ─────────────────────────
gitleaks detect --source .                # scan working tree
gitleaks detect --source . --log-opts="--all"  # include history
trufflehog git file://. --only-verified   # verified secret findings
# Ensure .env, *.pem, id_rsa are in .gitignore before first push
```

---

> **References and Book Sources:**
> - Scott Chacon & Ben Straub, *Pro Git (2nd Edition)* (`https://git-scm.com/book/en/v2`)
> - William Shotts, *The Linux Command Line (2nd Edition)*, Ch.17-18 (`~/Documents/Books/Linux/`)
> - `man git`, `git help <command>`
> - [TruffleHog secret scanner](https://github.com/trufflesecurity/trufflehog)
> - [Gitleaks secret scanner](https://github.com/gitleaks/gitleaks)

> **Zero2Root** | Basics Series | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Feedback and contributions welcome.** Open an issue or PR if you spot any errors.
