# Git: Sistem Kontrol Versi

> **Zero2Root** | Seri Dasar-Dasar | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **ID Kurikulum:** `LC-002` | **Fase 0:** Fondasi
> **Estimasi belajar:** 3-4 jam | **Level:** Pemula
> **Prasyarat:** LC-001
> **Peta buku:** Shotts, The Linux Command Line Bab 17-18 (konsep VCS)
<!-- LC-CURRICULUM-END -->

## Daftar Isi

1. Apa itu Git dan version control
2. Instal dan konfigurasi Git
3. Konsep dasar
4. `git init` dan `git clone`
5. Staging dan commit
6. Branching dan merging
7. Bekerja dengan remote
8. History dan undo
9. `.gitignore`
10. Alur kerja kolaborasi
11. Catatan keamanan
12. Contoh lengkap dari awal sampai akhir

---

## Istilah penting

Istilah-istilah ini akan sering muncul di materi.

| Istilah | Artinya |
|:---|:---|
| Repository (repo) | Folder proyek yang dilacak Git, beserta seluruh riwayatnya |
| Commit | Snapshot perubahanmu yang tersimpan pada satu titik waktu |
| Branch (cabang) | Jalur kerja terpisah yang bisa kamu kembangkan tanpa menyentuh `main` |
| Staging area | Ruang tunggu tempat kamu menyusun perubahan sebelum di-commit |
| HEAD | Penunjuk ke commit/branch yang sedang kamu tempati |
| Remote | Kopi repo di server lain, seperti GitHub |
| Clone | Mengunduh kopi lengkap sebuah repo remote |
| Push / pull | Mengirim commit-mu ke remote / mengambil dan menggabungkan milik remote |
| Merge | Menggabungkan pekerjaan dari satu branch ke branch lain |
| `.gitignore` | Daftar file yang tidak boleh dilacak Git (rahasia, output build) |

---

## 1. Overview: Apa Itu Git dan Version Control

Git adalah sistem kontrol versi terdistribusi yang melacak perubahan pada file dari waktu ke waktu, sehingga banyak orang bisa berkolaborasi di proyek yang sama tanpa saling menimpa pekerjaan. Linus Torvalds menulisnya pada 2005 untuk mengelola pengembangan kernel Linux.

Berbeda dari version control terpusat seperti SVN, Git bersifat terdistribusi: setiap kontributor menyimpan kopi lengkap dari seluruh riwayat repository di komputer lokalnya, bukan sekadar snapshot terbaru. Cara sederhana membayangkannya adalah sebagai mesin waktu untuk kode. Kamu bisa melihat, membandingkan, dan kembali ke versi mana pun dari proyek kapan saja.

Git penting untuk pekerjaan keamanan dalam beberapa hal spesifik. Banyak tool keamanan didistribusikan lewat GitHub dan diinstal dengan `git clone`. Repository publik sering mengandung kredensial yang ter-commit secara tidak sengaja. Memahami folder `.git` membantu forensik kode dan investigasi kebocoran, dan riwayat Git bisa memunculkan kembali data sensitif yang sudah "dihapus" dari working tree tapi masih tersimpan di commit sebelumnya.

## 2. Instalasi dan Konfigurasi Awal

Sebelum menggunakan Git, kamu menginstalnya dan mengatur identitas (nama dan email) yang akan ditempelkan ke setiap commit yang kamu buat.

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

| Scope | Berlaku untuk | Lokasi konfigurasi |
|-------|----------------|----------------------|
| `--local` | Repository saat ini saja | `.git/config` |
| `--global` | Semua repo milik user ini | `~/.gitconfig` |
| `--system` | Semua user di mesin | `/etc/gitconfig` |

## 3. Konsep Dasar

Sebelum menjalankan perintah, ada baiknya paham dulu istilah-istilah intinya.

- Repository (repo): folder proyek yang dilacak Git, berisi seluruh riwayat perubahan.
- Commit: snapshot dari perubahan yang disimpan permanen ke riwayat.
- Branch: jalur pengembangan independen dari proyek (default: `main` atau `master`).
- Working directory: file yang sedang kamu edit di disk.
- Staging area (index): area tunggu untuk perubahan sebelum benar-benar di-commit.
- HEAD: pointer ke commit atau branch yang sedang aktif.
- Remote: kopi repository yang disimpan di server lain, misalnya GitHub.

### Tiga Status File

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository (.git)
   (modified)                     (staged)                       (committed)
```

| Status | Arti |
|--------|------|
| Untracked | File baru, belum dilacak Git |
| Modified | File sudah diubah tapi belum di-stage |
| Staged | File siap untuk di-commit |
| Committed | File tersimpan permanen di riwayat |

## 4. `git init` dan `git clone`: Membuat dan Mengunduh Repo

Ada dua cara memulai bekerja dengan repository: membuat repo baru dari folder lokal dengan `git init`, atau mengunduh repo yang sudah ada dari remote server dengan `git clone`.

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

| Perintah | Fungsi |
|----------|--------|
| `git init` | Buat repo baru di folder lokal |
| `git clone <url>` | Unduh repo dari remote |
| `git clone -b <branch>` | Clone branch tertentu saja |
| `git clone --depth N` | Clone dengan riwayat terbatas |

## 5. Staging dan Commit: Menyimpan Perubahan

Git menyimpan perubahan lewat dua langkah: kamu stage file yang ingin disimpan dengan `git add`, lalu commit untuk menyimpannya permanen ke riwayat dengan `git commit`.

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

| Perintah | Fungsi |
|----------|--------|
| `git status` | Cek status file |
| `git add <file>` | Stage file tertentu |
| `git add .` | Stage semua file di folder ini |
| `git commit -m "msg"` | Commit dengan pesan |
| `git commit -am "msg"` | Stage dan commit sekaligus |
| `git diff` | Lihat perubahan yang belum di-stage |
| `git diff --staged` | Lihat perubahan yang sudah di-stage |

## 6. Branching: Cabang dan Penggabungan

Branch memungkinkanmu mengembangkan fitur, memperbaiki bug, atau bereksperimen secara terisolasi dari kode utama (`main`). Setelah selesai, branch bisa digabungkan kembali ke branch utama.

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

| Perintah | Fungsi |
|----------|--------|
| `git branch` | Daftar semua branch |
| `git branch <name>` | Buat branch baru |
| `git checkout -b <name>` | Buat sekaligus pindah ke branch baru |
| `git checkout <name>` | Pindah ke branch |
| `git merge <name>` | Gabungkan branch ke branch aktif |
| `git branch -d <name>` | Hapus branch |
| `git rebase <name>` | Susun ulang commit di atas base lain |

## 7. Remote: Bekerja dengan Remote Repository

Remote adalah kopi repository yang disimpan di server lain, seperti GitHub, GitLab, atau Bitbucket. Kamu berinteraksi dengan remote memakai `git push` untuk mengirim perubahan dan `git pull` untuk mengambilnya.

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

| Perintah | Fungsi |
|----------|--------|
| `git remote -v` | Lihat remote yang terhubung |
| `git remote add <name> <url>` | Tambah remote baru |
| `git push origin <branch>` | Kirim commit ke remote |
| `git pull origin <branch>` | Ambil dan gabungkan dari remote |
| `git fetch` | Ambil tanpa menggabungkan |

`git push --force` adalah operasi berbahaya: ini menimpa riwayat di remote dan bisa menghapus pekerjaan rekan tim. Pakai `--force-with-lease` sebagai gantinya, yang menolak menimpa commit yang belum pernah kamu lihat.

## 8. History dan Undo: Melihat Riwayat dan Membatalkan Perubahan

Git menyimpan seluruh riwayat perubahan proyek dan menyediakan banyak cara untuk melihat riwayat itu atau membatalkan perubahan saat dibutuhkan.

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

| Perintah | Fungsi |
|----------|--------|
| `git log` | Lihat riwayat commit |
| `git log --oneline` | Riwayat ringkas satu baris |
| `git blame <file>` | Lihat siapa mengubah tiap baris |
| `git restore <file>` | Batalkan perubahan yang belum di-stage |
| `git revert <commit>` | Batalkan commit dengan membuat commit baru |
| `git reset --hard <commit>` | Kembali dan buang semua perubahan |
| `git stash` | Simpan perubahan sementara |

`git reset --hard` bersifat destruktif: semua perubahan yang belum di-commit akan hilang permanen. Pastikan kamu memang ingin membuang perubahan itu sebelum menjalankan perintah ini.

## 9. `.gitignore`: Mengabaikan File

File `.gitignore` memberi tahu Git file atau folder mana yang harus diabaikan dan tidak pernah dilacak. Ini penting untuk menjaga file sensitif (kredensial, API key), artefak build, dan file sementara agar tidak masuk ke repository.

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

Menambahkan file ke `.gitignore` tidak menghapusnya dari riwayat kalau file itu sudah pernah di-commit sebelumnya. Untuk itu kamu butuh `git filter-repo` atau BFG Repo-Cleaner untuk menulis ulang riwayat dan membuangnya secara permanen.

## 10. Git Workflow: Pola Kolaborasi

Alur kerja umum untuk berkolaborasi di Git dan platform seperti GitHub mengikuti pola standar: fork atau clone, branch, commit, push, pull request.

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

### Strategi Workflow Umum

| Strategi | Cocok untuk |
|----------|-------------|
| Git Flow | Proyek besar dengan rilis terjadwal |
| GitHub Flow | Deployment berkelanjutan, dijaga tetap sederhana |
| Trunk-Based | Tim kecil, integrasi cepat |
| Fork dan PR | Open source, kontributor eksternal |

## 11. Catatan Keamanan: Hygiene Kredensial dan Secret Scanning

Riwayat Git menyimpan selamanya apa pun yang pernah di-commit. Fokus bagian ini adalah mencegah kebocoran kredensial dan menangkap secret sebelum ter-push, di repository yang kamu miliki atau kelola sendiri, bukan berburu kredensial di riwayat milik orang lain.

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

### Checklist Kontrol Defensif

| Kontrol | Tindakan |
|---------|----------|
| Template `.gitignore` | Blokir `.env`, key, PEM secara default |
| Scanner pre-commit / CI | Gate `gitleaks` atau TruffleHog saat push |
| Token berumur pendek | Utamakan OIDC atau PAT berumur pendek |
| Secret manager | Vault atau secret manager cloud, bukan repo |
| Runbook rotasi | Revoke dulu, baru bersihkan riwayat |
| Protected branch + CODEOWNERS | Wajib review sebelum merge |
| Tidak ada `.git` di web root | Jangan pernah deploy `.git` ke produksi |

Perlakukan setiap commit secret yang tidak sengaja sebagai kompromi yang terkonfirmasi atas secret itu. Rotasi lebih baik daripada menulis ulang riwayat, dan menjalankan scanner di CI berarti pengecekan itu tidak bergantung pada manusia yang kebetulan menyadarinya.

## 12. Contoh Praktis dari Awal Sampai Akhir

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

### Ringkasan Perintah

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

> **Referensi dan Sumber Buku:**
> - Scott Chacon & Ben Straub, *Pro Git (2nd Edition)* (`https://git-scm.com/book/en/v2`)
> - William Shotts, *The Linux Command Line (2nd Edition)*, Bab 17-18 (`~/Documents/Books/Linux/`)
> - `man git`, `git help <command>`
> - [TruffleHog secret scanner](https://github.com/trufflesecurity/trufflehog)
> - [Gitleaks secret scanner](https://github.com/gitleaks/gitleaks)

> **Zero2Root** | Seri Dasar-Dasar | kodoktheGr3at | 2026
> **Repository:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **Masukan dan kontribusi diterima.** Buka issue atau PR kalau menemukan kesalahan.
