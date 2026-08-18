# 🔀 Git — Version Control System

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026

---


<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-002` | **Phase 0:** Foundations  
> **Est. study:** 3-4h | **Level:** Beginner  
> **Prerequisites:** LC-001  
> **Book map:** Shotts Â The Linux Command Line Ch.17-18 (VCS concepts)
<!-- LC-CURRICULUM-END -->
## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu Git & version control | What is Git & version control | Gitとバージョン管理とは |
| 2 | Instalasi | Install & konfigurasi awal | Install & initial config | インストールと初期設定 |
| 3 | Konsep Dasar | Repository, commit, branch | Repository, commit, branch | リポジトリ、コミット、ブランチ |
| 4 | `git init` & `clone` | Membuat & mengunduh repo | Creating & downloading repos | リポジトリの作成とダウンロード |
| 5 | Staging & Commit | Area staging dan commit | Staging area and commits | ステージングエリアとコミット |
| 6 | Branching | Cabang & penggabungan | Branches & merging | ブランチとマージ |
| 7 | Remote | Bekerja dengan remote repo | Working with remote repos | リモートリポジトリの操作 |
| 8 | History & Undo | Lihat riwayat & batalkan perubahan | View history & undo changes | 履歴の確認と変更の取り消し |
| 9 | `.gitignore` | Mengabaikan file tertentu | Ignoring certain files | 特定ファイルの無視 |
| 10 | Git Workflow | Alur kerja kolaborasi | Collaboration workflow | コラボレーションワークフロー |
| 11 | Security Note | Hygiene kredensial & secret scanning | Credential hygiene & secret scanning | 認証情報衛生とシークレットスキャン |
| 12 | Workflow | Contoh praktis lengkap | Full practical example | 実践的なワークフロー例 |

---

## 1. 🏢 Overview — What Is Git & Version Control

### 🇮🇩 Bahasa Indonesia
**Git** adalah **sistem kontrol versi terdistribusi (distributed version control system)** yang melacak perubahan pada file dari waktu ke waktu, memungkinkan banyak orang berkolaborasi pada proyek yang sama tanpa saling menimpa pekerjaan satu sama lain. Git dibuat oleh **Linus Torvalds** pada 2005 untuk mengelola pengembangan kernel Linux.

Berbeda dengan version control terpusat (seperti SVN), Git bersifat **terdistribusi** — setiap kontributor memiliki **kopi lengkap dari seluruh riwayat repository** di komputer lokal mereka, bukan hanya snapshot terbaru.

Analogi sederhana: Git seperti **mesin waktu untuk kode** — kamu bisa melihat, membandingkan, dan kembali ke versi mana pun dari proyekmu kapan saja.

**Mengapa penting untuk cybersecurity:**
- Banyak **tools pentesting didistribusikan via GitHub** dan diinstal dengan `git clone`
- Repository publik sering **mengandung credential yang ter-commit secara tidak sengaja**
- Memahami `.git` folder membantu **forensik kode dan source code leak**
- Git history bisa **mengungkap data sensitif** yang sudah "dihapus" tapi masih ada di riwayat

### 🇬🇧 English
**Git** is a **distributed version control system** that tracks changes to files over time, enabling multiple people to collaborate on the same project without overwriting each other's work. Git was created by **Linus Torvalds** in 2005 to manage Linux kernel development.

Unlike centralized version control (like SVN), Git is **distributed** — every contributor has a **complete copy of the entire repository history** on their local machine, not just the latest snapshot.

Simple analogy: Git is like a **time machine for code** — you can view, compare, and revert to any version of your project at any time.

**Why it matters for cybersecurity:**
- Many **pentesting tools are distributed via GitHub** and installed with `git clone`
- Public repositories often **contain accidentally committed credentials**
- Understanding the `.git` folder helps with **code forensics and source code leaks**
- Git history can **expose sensitive data** that was "deleted" but still exists in history

### 🇯🇵 日本語
**Git**は時間をかけてファイルの変更を追跡する**分散型バージョン管理システム**で、複数の人が同じプロジェクトで互いの作業を上書きせずにコラボレーションできるようにします。Gitは2005年に**Linus Torvalds**によってLinuxカーネル開発を管理するために作られました。

集中型バージョン管理（SVNなど）とは異なり、Gitは**分散型**です — 各コントリビューターは最新のスナップショットだけでなく、**リポジトリ全体の履歴の完全なコピー**をローカルマシンに持っています。

簡単な例え：Gitは**コードのタイムマシン**のようなもの — いつでもプロジェクトの任意のバージョンを表示、比較、復元できます。

**サイバーセキュリティにとって重要な理由：**
- 多くの**ペンテストツールがGitHubで配布され**、`git clone`でインストールされます
- 公開リポジトリには**誤ってコミットされた認証情報**が含まれることが多い
- `.git`フォルダの理解は**コードフォレンジクスとソースコード漏洩**に役立つ
- Git履歴は「削除された」が履歴にまだ存在する**機密データを露出させる**可能性がある

---

## 2. ⚙️ Instalasi — Install & Initial Configuration

### 🇮🇩 Bahasa Indonesia
Sebelum menggunakan Git, kita perlu **menginstal** dan **mengkonfigurasi identitas** (nama dan email) yang akan ditempelkan ke setiap commit yang kita buat.

### 🇬🇧 English
Before using Git, we need to **install** it and **configure an identity** (name and email) that will be attached to every commit we make.

### 🇯🇵 日本語
Gitを使う前に、**インストール**し、作成するすべてのコミットに付けられる**アイデンティティ（名前とメール）を設定**する必要があります。

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

| Scope | 🇮🇩 Berlaku untuk | 🇬🇧 Applies to | 🇯🇵 適用範囲 | Config Location |
|-------|-----------------|---------------|------------|-----------------|
| `--local` | Repository saat ini saja | Current repo only | 現在のリポジトリのみ | `.git/config` |
| `--global` | Semua repo milik user | All repos for user | ユーザーの全リポジトリ | `~/.gitconfig` |
| `--system` | Semua user di mesin | All users on machine | マシン上の全ユーザー | `/etc/gitconfig` |

---

## 3. 🧠 Konsep Dasar — Core Concepts

### 🇮🇩 Bahasa Indonesia
Sebelum masuk ke perintah, penting untuk memahami **istilah dasar** dalam Git:

- **Repository (repo)** — folder proyek yang dilacak oleh Git, berisi seluruh riwayat perubahan
- **Commit** — "snapshot" dari perubahan yang disimpan secara permanen ke riwayat
- **Branch** — cabang pengembangan independen dari proyek (default: `main` atau `master`)
- **Working Directory** — file yang sedang kamu edit di sistem
- **Staging Area (Index)** — area "ruang tunggu" sebelum perubahan benar-benar di-commit
- **HEAD** — pointer yang menunjukkan commit/branch yang sedang aktif
- **Remote** — kopi repository yang disimpan di server lain (misal: GitHub)

### 🇬🇧 English
Before diving into commands, it's important to understand the **core terminology** in Git:

- **Repository (repo)** — a project folder tracked by Git, containing the entire history of changes
- **Commit** — a "snapshot" of changes saved permanently to the history
- **Branch** — an independent line of development for the project (default: `main` or `master`)
- **Working Directory** — the files you are currently editing on disk
- **Staging Area (Index)** — a "waiting room" area before changes are actually committed
- **HEAD** — a pointer indicating the currently active commit/branch
- **Remote** — a copy of the repository stored on another server (e.g. GitHub)

### 🇯🇵 日本語
コマンドに入る前に、Gitの**基本用語**を理解することが重要です：

- **リポジトリ（repo）** — Gitによって追跡されるプロジェクトフォルダで、変更の全履歴を含む
- **コミット** — 履歴に永続的に保存される変更の「スナップショット」
- **ブランチ** — プロジェクトの独立した開発ライン（デフォルト：`main`または`master`）
- **作業ディレクトリ** — 現在編集しているディスク上のファイル
- **ステージングエリア（インデックス）** — 変更が実際にコミットされる前の「待合室」エリア
- **HEAD** — 現在アクティブなコミット/ブランチを示すポインタ
- **リモート** — 別のサーバー（例：GitHub）に保存されたリポジトリのコピー

### 📊 The Three States of a File

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository (.git)
   (modified)                     (staged)                       (committed)
```

| State | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 |
|-------|---------|------------|---------|
| Untracked | File baru, belum dilacak Git | New file, not yet tracked by Git | 新規ファイル、まだGitに追跡されていない |
| Modified | File sudah diubah tapi belum di-stage | File changed but not staged | ファイルが変更されたがステージされていない |
| Staged | File siap untuk di-commit | File ready to be committed | コミット準備が完了したファイル |
| Committed | File tersimpan permanen di riwayat | File permanently saved to history | 履歴に永続的に保存されたファイル |

---

## 4. 🆕 `git init` & `git clone` — Creating & Downloading Repos

### 🇮🇩 Bahasa Indonesia
Ada dua cara untuk mulai bekerja dengan repository: **membuat repo baru** dari folder lokal (`git init`) atau **mengunduh repo yang sudah ada** dari remote server (`git clone`).

### 🇬🇧 English
There are two ways to start working with a repository: **creating a new repo** from a local folder (`git init`) or **downloading an existing repo** from a remote server (`git clone`).

### 🇯🇵 日本語
リポジトリで作業を開始する方法は2つあります：ローカルフォルダから**新しいリポジトリを作成する**（`git init`）か、リモートサーバーから**既存のリポジトリをダウンロードする**（`git clone`）かです。

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

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git init` | Buat repo baru di folder lokal | Create new repo in local folder | ローカルフォルダに新規リポジトリ作成 |
| `git clone <url>` | Unduh repo dari remote | Download repo from remote | リモートからリポジトリをダウンロード |
| `git clone -b <branch>` | Clone branch tertentu saja | Clone only a specific branch | 特定のブランチのみクローン |
| `git clone --depth N` | Clone dengan riwayat terbatas | Clone with limited history | 履歴を制限してクローン |

---

## 5. 📝 Staging & Commit — Saving Your Changes

### 🇮🇩 Bahasa Indonesia
Git menggunakan proses **dua langkah** untuk menyimpan perubahan: pertama kamu **stage** file yang ingin disimpan (`git add`), lalu **commit** untuk menyimpannya secara permanen ke riwayat (`git commit`).

### 🇬🇧 English
Git uses a **two-step process** to save changes: first you **stage** the files you want to save (`git add`), then **commit** to permanently save them to history (`git commit`).

### 🇯🇵 日本語
Gitは変更を保存するために**2段階のプロセス**を使います：まず保存したいファイルを**ステージ**し（`git add`）、次に**コミット**して履歴に永続的に保存します（`git commit`）。

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

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git status` | Lihat status file | Check file status | ファイルの状態を確認 |
| `git add <file>` | Stage file tertentu | Stage a specific file | 特定のファイルをステージ |
| `git add .` | Stage semua file di folder ini | Stage all files in this folder | このフォルダの全ファイルをステージ |
| `git commit -m "msg"` | Commit dengan pesan | Commit with a message | メッセージ付きでコミット |
| `git commit -am "msg"` | Stage + commit sekaligus | Stage + commit in one step | ステージとコミットを同時に |
| `git diff` | Lihat perubahan belum di-stage | View unstaged changes | 未ステージの変更を表示 |
| `git diff --staged` | Lihat perubahan sudah di-stage | View staged changes | ステージされた変更を表示 |

---

## 6. 🌿 Branching — Branches & Merging

### 🇮🇩 Bahasa Indonesia
**Branch** memungkinkan kamu mengembangkan fitur, memperbaiki bug, atau eksperimen secara **terisolasi** dari kode utama (`main`). Setelah selesai, branch bisa **digabungkan (merge)** kembali ke branch utama.

### 🇬🇧 English
**Branches** let you develop features, fix bugs, or experiment **in isolation** from the main codebase (`main`). Once finished, a branch can be **merged** back into the main branch.

### 🇯🇵 日本語
**ブランチ**を使うと、メインコードベース（`main`）から**分離して**機能開発、バグ修正、実験ができます。完了したら、ブランチをメインブランチに**マージ**できます。

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

# ── REBASING (alternative to merge — cleaner history) ────────
$ git checkout feature-payment
$ git rebase main
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git branch` | Daftar semua branch | List all branches | 全ブランチを一覧表示 |
| `git branch <name>` | Buat branch baru | Create a new branch | 新しいブランチを作成 |
| `git checkout -b <name>` | Buat + pindah ke branch baru | Create + switch to new branch | 新ブランチ作成+切り替え |
| `git checkout <name>` | Pindah ke branch | Switch to a branch | ブランチに切り替え |
| `git merge <name>` | Gabungkan branch ke branch aktif | Merge branch into current | 現在のブランチにマージ |
| `git branch -d <name>` | Hapus branch | Delete a branch | ブランチを削除 |
| `git rebase <name>` | Susun ulang riwayat commit | Re-apply commits on top of another base | コミットを別ベースの上に再適用 |

---

## 7. 🌐 Remote — Working with Remote Repositories

### 🇮🇩 Bahasa Indonesia
**Remote** adalah kopi repository yang disimpan di server lain (seperti GitHub, GitLab, Bitbucket). Kita berinteraksi dengan remote menggunakan `git push` (kirim perubahan) dan `git pull` (ambil perubahan).

### 🇬🇧 English
A **remote** is a copy of the repository stored on another server (such as GitHub, GitLab, Bitbucket). We interact with remotes using `git push` (send changes) and `git pull` (fetch changes).

### 🇯🇵 日本語
**リモート**は別のサーバー（GitHub、GitLab、Bitbucketなど）に保存されたリポジトリのコピーです。リモートとのやり取りには`git push`（変更を送信）と`git pull`（変更を取得）を使います。

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

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git remote -v` | Lihat remote yang terhubung | View connected remotes | 接続されたリモートを表示 |
| `git remote add <name> <url>` | Tambah remote baru | Add a new remote | 新しいリモートを追加 |
| `git push origin <branch>` | Kirim commit ke remote | Push commits to remote | コミットをリモートに送信 |
| `git pull origin <branch>` | Ambil + gabungkan dari remote | Fetch + merge from remote | リモートから取得+マージ |
| `git fetch` | Ambil tanpa menggabungkan | Fetch without merging | マージせずに取得 |

> ⚠️ **`git push --force` adalah operasi berbahaya** — ini menimpa riwayat di remote dan bisa menghapus pekerjaan rekan tim. Gunakan `--force-with-lease` sebagai alternatif yang lebih aman.

---

## 8. ⏪ History & Undo — Viewing History & Reverting Changes

### 🇮🇩 Bahasa Indonesia
Git menyimpan **seluruh riwayat perubahan** proyek, dan menyediakan banyak cara untuk melihat riwayat tersebut atau membatalkan perubahan jika diperlukan.

### 🇬🇧 English
Git keeps the **entire history of changes** to a project, and provides many ways to view that history or undo changes when needed.

### 🇯🇵 日本語
Gitはプロジェクトの**変更の全履歴**を保持し、その履歴を表示したり必要に応じて変更を取り消したりする多くの方法を提供します。

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

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git log` | Lihat riwayat commit | View commit history | コミット履歴を表示 |
| `git log --oneline` | Riwayat singkat 1 baris | Compact one-line history | 簡潔な1行履歴 |
| `git blame <file>` | Lihat siapa mengubah tiap baris | See who changed each line | 各行の変更者を確認 |
| `git restore <file>` | Batalkan perubahan belum di-stage | Discard unstaged changes | 未ステージの変更を取り消し |
| `git revert <commit>` | Batalkan commit (commit baru) | Undo a commit (new commit) | コミットを取り消す（新規コミット） |
| `git reset --hard <commit>` | Kembali & hapus semua perubahan | Go back & discard all changes | 戻って全変更を破棄 |
| `git stash` | Simpan sementara perubahan | Temporarily save changes | 変更を一時保存 |

> ⚠️ **`git reset --hard` bersifat destruktif** — semua perubahan yang belum di-commit akan hilang permanen. Selalu pastikan kamu benar-benar ingin membuang perubahan sebelum menjalankan perintah ini.

---

## 9. 🚫 `.gitignore` — Ignoring Files

### 🇮🇩 Bahasa Indonesia
File `.gitignore` memberi tahu Git **file atau folder mana yang harus diabaikan** dan tidak pernah dilacak. Sangat penting untuk mengecualikan file sensitif (credential, API keys), file build, dan file sementara dari repository.

### 🇬🇧 English
The `.gitignore` file tells Git **which files or folders to ignore** and never track. Critical for excluding sensitive files (credentials, API keys), build artifacts, and temporary files from the repository.

### 🇯🇵 日本語
`.gitignore` ファイルはGitに**どのファイルやフォルダを無視するか**を伝え、決して追跡しないようにします。機密ファイル（認証情報、APIキー）、ビルド成果物、一時ファイルをリポジトリから除外するために重要です。

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

> 🔴 **Penting:** Menambahkan file ke `.gitignore` **TIDAK menghapusnya dari riwayat** jika sudah pernah di-commit sebelumnya! Gunakan `git filter-repo` atau BFG Repo-Cleaner untuk membersihkan riwayat secara permanen.

---

## 10. 🔄 Git Workflow — Collaboration Workflow

### 🇮🇩 Bahasa Indonesia
Workflow umum saat berkolaborasi menggunakan Git dan platform seperti GitHub mengikuti pola standar: **fork/clone → branch → commit → push → pull request**.

### 🇬🇧 English
A common workflow when collaborating with Git and platforms like GitHub follows a standard pattern: **fork/clone → branch → commit → push → pull request**.

### 🇯🇵 日本語
GitとGitHubなどのプラットフォームでコラボレーションする際の一般的なワークフローは、標準的なパターンに従います：**フォーク/クローン → ブランチ → コミット → プッシュ → プルリクエスト**。

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

### 📊 Common Workflow Strategies

| Strategy | 🇮🇩 Cocok untuk | 🇬🇧 Best for | 🇯🇵 適している場面 |
|----------|----------------|-------------|------------------|
| **Git Flow** | Proyek besar dgn rilis terjadwal | Large projects with scheduled releases | スケジュールされたリリースのある大規模プロジェクト |
| **GitHub Flow** | Deployment berkelanjutan, sederhana | Continuous deployment, simple | 継続的デプロイ、シンプル |
| **Trunk-Based** | Tim kecil, integrasi cepat | Small teams, fast integration | 小規模チーム、高速統合 |
| **Fork & PR** | Open source, kontributor eksternal | Open source, external contributors | オープンソース、外部コントリビューター |

---

## 11. 🔐 Security Note — Credential Hygiene & Secret Scanning (Defense)

### 🇮🇩 Bahasa Indonesia
Riwayat Git **menyimpan selamanya** apa yang pernah di-commit. Fokus keamanan di sini adalah **mencegah kebocoran kredensial** dan **mendeteksi secret sebelum push** — bukan panduan berburu kredensial pada target.

### 🇬🇧 English
Git history **retains forever** anything once committed. Security focus here is **preventing credential leaks** and **detecting secrets before push** — not a guide to hunting credentials on third-party targets.

### 🇯🇵 日本語
Gitの履歴は一度コミットした内容を**永続保持**します。ここでの重点は**認証情報漏洩の防止**と**push前のシークレット検知**であり、第三者ターゲットへのクレデンシャル探索ガイドではありません。

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

# ── DETECT: audit YOUR repositories you own/maintain ─────────
# Scan local clone history for accidentally committed secrets
gitleaks detect --source . --log-opts="--all"
trufflehog git file://. --only-verified   # prefer verified findings

# Search YOUR history for known secret markers (ops hygiene)
git log --all -p -S 'AKIA' -- '*.env' '*.yml' '*.json' 2>/dev/null | head

# ── RESPOND: if a secret was committed ───────────────────────
# 1) Rotate/revoke the credential immediately (primary control)
# 2) Remove from future commits (.gitignore + rewrite only if policy allows)
# 3) Treat old history as compromised until rotation completes
# 4) Prefer BFG/filter-repo ONLY on repos you control, then force-sync with team policy
```

### 🛡️ Defensive Controls Checklist

| Control | 🇮🇩 Tindakan | 🇬🇧 Action | 🇯🇵 アクション |
|---------|-------------|-----------|----------------|
| `.gitignore` + templates | Blokir `.env`, key, PEM | Block `.env`, keys, PEMs | `.env`・鍵・PEMを除外 |
| Pre-commit / CI scanners | `gitleaks` / TruffleHog gate | Fail build on secrets | シークレット検知でCI失敗 |
| Short-lived tokens | PAT/OIDC, bukan long-lived | Prefer OIDC / short PATs | 短寿命トークン・OIDC |
| Secret managers | Vault / cloud SM, bukan repo | Vault/cloud SM, not git | Vault等、リポジトリ外 |
| Rotation runbook | Segera revoke jika bocor | Revoke first, then cleanup | 漏洩時は先に失効 |
| Protected branches + CODEOWNERS | Review wajib sebelum merge | Require review before merge | マージ前レビュー必須 |
| No `.git` on web roots | Pastikan deploy tanpa `.git` | Never deploy `.git` to prod | 本番に `.git` を置かない |

> 🛡️ **Defense-first:** Treat every accidental commit of a secret as a **confirmed compromise of that secret**. Rotation beats history rewriting. Use scanners in CI so humans are not the only control.

---

## 📊 Command Summary Table

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `git init` | Buat repo baru | Create new repo | 新規リポジトリ作成 |
| `git clone <url>` | Unduh repo | Download repo | リポジトリをダウンロード |
| `git status` | Cek status file | Check file status | ファイル状態を確認 |
| `git add <file>` | Stage file | Stage file | ファイルをステージ |
| `git commit -m "msg"` | Commit perubahan | Commit changes | 変更をコミット |
| `git push` | Kirim ke remote | Push to remote | リモートに送信 |
| `git pull` | Ambil dari remote | Pull from remote | リモートから取得 |
| `git branch` | Daftar/buat branch | List/create branches | ブランチ一覧/作成 |
| `git checkout -b <name>` | Buat & pindah branch | Create & switch branch | ブランチ作成と切り替え |
| `git merge <branch>` | Gabungkan branch | Merge branch | ブランチをマージ |
| `git log` | Lihat riwayat | View history | 履歴を表示 |
| `git diff` | Lihat perbedaan | View differences | 差分を表示 |
| `git stash` | Simpan sementara | Temporarily stash | 一時保存 |
| `git revert <commit>` | Batalkan commit | Undo a commit | コミットを取り消し |
| `git reset --hard` | Reset paksa | Force reset | 強制リセット |

---

## 🔗 Practical Workflow Example

```bash
# ── SCENARIO: Start a new project and push to GitHub ─────────

# 1. Configure identity (once per machine)
$ git config --global user.name "kodoktheGr3at"
$ git config --global user.email "kodok@example.com"

# 2. Create project folder and initialize repo
$ mkdir pentest-toolkit && cd pentest-toolkit
$ git init

# 3. Create initial files
$ echo "# Pentest Toolkit" > README.md
$ echo "*.log" > .gitignore
$ echo ".env" >> .gitignore

# 4. Stage and commit
$ git add .
$ git commit -m "Initial commit"

# 5. Create a feature branch
$ git checkout -b add-recon-scripts

# 6. Add new files and commit
$ echo "echo 'recon script'" > recon.sh
$ git add recon.sh
$ git commit -m "Add basic recon script"

# 7. Switch back to main and merge
$ git checkout main
$ git merge add-recon-scripts

# 8. Connect to GitHub remote
$ git remote add origin https://github.com/kodoktheGr3at/pentest-toolkit.git

# 9. Push to GitHub
$ git push -u origin main

# 10. Clone the tool on another machine later
$ git clone https://github.com/kodoktheGr3at/pentest-toolkit.git

# 11. Pull latest updates
$ cd pentest-toolkit && git pull origin main
```

---

## 🧠 Quick Reference Cheatsheet

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

# ── SECURITY / SECRET HYGIENE (YOUR REPOS) ────────────────
gitleaks detect --source .                # scan working tree
gitleaks detect --source . --log-opts="--all"  # include history
trufflehog git file://. --only-verified   # verified secret findings
# Ensure .env, *.pem, id_rsa are in .gitignore before first push
```

---

> 📚 **References & Book Sources:**
> - Scott Chacon & Ben Straub — *Pro Git (2nd Edition)* (`https://git-scm.com/book/en/v2`)
> - Peter Kim — *The Hacker Playbook 3* (`~/Documents/Books/CyberSec/Ethical Hacking/`) — authorized testing methodology context
> - Dafydd Stuttard & Marcus Pinto — *The Web Application Hacker's Handbook (2nd Edition)* (`~/Documents/Books/CyberSec/Web App/`)
> - [HackTheBox Academy - Linux Fundamentals](https://academy.hackthebox.com)
> - `man git`, `git help <command>`
> - [TruffleHog — Secret Scanner](https://github.com/trufflesecurity/trufflehog)
> - [Gitleaks — Secret Scanner](https://github.com/gitleaks/gitleaks)

> **LearnCybersecurity** | Basics Series | kodoktheGr3at | 2026  
> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.