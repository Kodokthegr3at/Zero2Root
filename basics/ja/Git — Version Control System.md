# Git: バージョン管理システム

> **Zero2Root** | 基礎シリーズ | kodoktheGr3at | 2026

---

<!-- LC-CURRICULUM-START -->
> **カリキュラムID:** `LC-002` | **フェーズ0:** 基礎
> **推定学習時間:** 3-4時間 | **レベル:** 初級
> **前提:** LC-001
> **書籍対応:** Shotts, The Linux Command Line 第17-18章（VCSの概念）
<!-- LC-CURRICULUM-END -->

## 目次

1. Gitとバージョン管理とは何か
2. Gitのインストールと設定
3. 基本概念
4. `git init` と `git clone`
5. ステージングとコミット
6. ブランチとマージ
7. リモートの操作
8. 履歴と取り消し
9. `.gitignore`
10. コラボレーションの流れ
11. セキュリティノート
12. 一通りの実践例

---

## 重要な用語

この教材でよく出てくる言葉である。

| 用語 | 意味 |
|:---|:---|
| リポジトリ(repo) | Gitが追跡するプロジェクトのフォルダ。全履歴を含む |
| コミット | ある時点での変更を保存したスナップショット |
| ブランチ | `main` に触れずに開発できる、独立した作業の線 |
| ステージングエリア | コミットする前に変更を並べておく待合室 |
| HEAD | 今いるコミット/ブランチを指すポインタ |
| リモート | GitHubなど、別のサーバー上にあるリポジトリのコピー |
| クローン | リモートリポジトリの完全なコピーをダウンロードすること |
| プッシュ / プル | 自分のコミットをリモートへ送る / リモートの分を取得してマージする |
| マージ | あるブランチの作業を別のブランチに取り込むこと |
| `.gitignore` | Gitが決して追跡すべきでないファイルの一覧(秘密情報、ビルド成果物) |

---

## 1. 概要: Gitとバージョン管理とは何か

Gitは、時間をかけてファイルの変更を追跡する分散型バージョン管理システムで、複数の人が同じプロジェクトで互いの作業を上書きせずに共同作業できるようにする。Linus Torvaldsが2005年、Linuxカーネルの開発を管理するために作った。

SVNのような集中型バージョン管理とは違い、Gitは分散型である。各コントリビューターは、最新のスナップショットだけでなく、リポジトリ全体の履歴の完全なコピーを自分のローカルマシンに持っている。わかりやすく言えば、コードのタイムマシンのようなものだ。いつでもプロジェクトの過去の任意のバージョンを表示、比較、復元できる。

Gitがセキュリティの仕事にとって重要なのは、いくつかの具体的な理由からだ。多くのセキュリティツールはGitHub経由で配布され、`git clone`でインストールされる。公開リポジトリには、うっかりコミットされた認証情報が含まれていることが少なくない。`.git`フォルダの仕組みを理解しておくと、ソースコードのフォレンジック調査や漏洩調査に役立つ。そしてGitの履歴は、作業ツリーから「削除」されたはずのデータでも、以前のコミットに残っていれば再び表に出てくる。

## 2. インストールと初期設定

Gitを使う前に、インストールを済ませ、作成するすべてのコミットに付けられる身元情報（名前とメールアドレス）を設定する。

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

| スコープ | 適用範囲 | 設定ファイルの場所 |
|---------|---------|-------------------|
| `--local` | 現在のリポジトリのみ | `.git/config` |
| `--global` | このユーザーの全リポジトリ | `~/.gitconfig` |
| `--system` | マシン上の全ユーザー | `/etc/gitconfig` |

## 3. 基本概念

コマンドに入る前に、基本用語を押さえておくとよい。

- リポジトリ（repo）: Gitが追跡するプロジェクトフォルダで、変更の全履歴を含む。
- コミット: 履歴に永続的に保存される変更のスナップショット。
- ブランチ: プロジェクトの独立した開発ライン（デフォルトは`main`または`master`）。
- 作業ディレクトリ: 現在ディスク上で編集しているファイル群。
- ステージングエリア（インデックス）: 変更が実際にコミットされる前の待機場所。
- HEAD: 現在アクティブなコミットまたはブランチを指すポインタ。
- リモート: GitHubなど別のサーバーに保存されたリポジトリのコピー。

### ファイルの3つの状態

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository (.git)
   (modified)                     (staged)                       (committed)
```

| 状態 | 意味 |
|------|------|
| Untracked | 新規ファイルで、まだGitに追跡されていない |
| Modified | ファイルは変更されたがステージされていない |
| Staged | コミット準備が整ったファイル |
| Committed | 履歴に永続的に保存されたファイル |

## 4. `git init` と `git clone`: リポジトリの作成とダウンロード

リポジトリでの作業を始める方法は2つある。ローカルフォルダから`git init`で新規作成するか、`git clone`でリモートサーバーから既存のリポジトリをダウンロードするかだ。

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

| コマンド | 機能 |
|---------|------|
| `git init` | ローカルフォルダに新規リポジトリを作成 |
| `git clone <url>` | リモートからリポジトリをダウンロード |
| `git clone -b <branch>` | 特定のブランチのみクローン |
| `git clone --depth N` | 履歴を制限してクローン |

## 5. ステージングとコミット: 変更の保存

Gitは2段階で変更を保存する。まず`git add`で保存したいファイルをステージし、次に`git commit`で履歴に永続的に保存する。

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

| コマンド | 機能 |
|---------|------|
| `git status` | ファイルの状態を確認 |
| `git add <file>` | 特定のファイルをステージ |
| `git add .` | このフォルダの全ファイルをステージ |
| `git commit -m "msg"` | メッセージ付きでコミット |
| `git commit -am "msg"` | ステージとコミットを同時に |
| `git diff` | 未ステージの変更を表示 |
| `git diff --staged` | ステージ済みの変更を表示 |

## 6. ブランチ操作: ブランチとマージ

ブランチを使うと、メインのコードベース（`main`）から分離した状態で機能開発、バグ修正、実験ができる。作業が終わったら、ブランチをメインブランチにマージし直せる。

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

| コマンド | 機能 |
|---------|------|
| `git branch` | 全ブランチを一覧表示 |
| `git branch <name>` | 新しいブランチを作成 |
| `git checkout -b <name>` | 新規ブランチの作成と切り替えを同時に |
| `git checkout <name>` | ブランチに切り替え |
| `git merge <name>` | ブランチを現在のブランチにマージ |
| `git branch -d <name>` | ブランチを削除 |
| `git rebase <name>` | コミットを別のベースの上に再適用 |

## 7. リモート: リモートリポジトリの操作

リモートとは、GitHub、GitLab、Bitbucketなど別のサーバーに保存されたリポジトリのコピーである。変更を送るには`git push`、取得するには`git pull`を使ってリモートとやり取りする。

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

| コマンド | 機能 |
|---------|------|
| `git remote -v` | 接続されたリモートを表示 |
| `git remote add <name> <url>` | 新しいリモートを追加 |
| `git push origin <branch>` | コミットをリモートに送信 |
| `git pull origin <branch>` | リモートから取得してマージ |
| `git fetch` | マージせずに取得のみ |

`git push --force`は危険な操作である。リモート側の履歴を上書きし、チームメイトの作業を消してしまうことがある。代わりに、自分がまだ見ていないコミットの上書きを拒否する`--force-with-lease`を使うとよい。

## 8. 履歴と取り消し: 履歴の確認と変更の取り消し

Gitはプロジェクトの変更履歴をすべて保持し、その履歴を確認したり、必要に応じて変更を取り消したりする手段を多数提供している。

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

| コマンド | 機能 |
|---------|------|
| `git log` | コミット履歴を表示 |
| `git log --oneline` | 1行の簡潔な履歴を表示 |
| `git blame <file>` | 各行の変更者を確認 |
| `git restore <file>` | 未ステージの変更を取り消す |
| `git revert <commit>` | 新規コミットを作ってコミットを取り消す |
| `git reset --hard <commit>` | 過去のコミットに戻り、変更をすべて破棄 |
| `git stash` | 変更を一時的に退避 |

`git reset --hard`は破壊的な操作である。コミットしていない変更はすべて永久に失われる。実行する前に、本当に変更を捨ててよいか確認すること。

## 9. `.gitignore`: ファイルの無視設定

`.gitignore`ファイルは、Gitにどのファイルやフォルダを無視して決して追跡しないかを伝える。認証情報やAPIキーといった機密ファイル、ビルド成果物、一時ファイルをリポジトリから除外するために重要だ。

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

`.gitignore`にファイルを追加しても、すでに一度コミットされていたファイルは履歴から消えない。履歴を書き換えて完全に取り除くには、`git filter-repo`かBFG Repo-Cleanerが必要になる。

## 10. Gitワークフロー: コラボレーションの型

GitとGitHubのようなプラットフォームでの一般的なコラボレーションの流れは、フォークまたはクローン、ブランチ作成、コミット、プッシュ、プルリクエストという標準的な形をとる。

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

### よく使われるワークフロー戦略

| 戦略 | 向いている場面 |
|------|----------------|
| Git Flow | スケジュールされたリリースのある大規模プロジェクト |
| GitHub Flow | 継続的デプロイ、シンプルさ重視 |
| トランクベース | 小規模チーム、高速な統合 |
| フォーク＋PR | オープンソース、外部コントリビューター |

## 11. セキュリティノート: 認証情報の衛生管理とシークレットスキャン

Gitの履歴は、一度コミットされたものを永久に保持する。この節の焦点は、自分が所有・管理するリポジトリにおいて認証情報の漏洩を防ぎ、プッシュ前にシークレットを検知することであり、他人の履歴からクレデンシャルを探し出すことではない。

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

### 防御コントロールのチェックリスト

| コントロール | 対応 |
|-------------|------|
| `.gitignore`テンプレート | `.env`、鍵、PEMをデフォルトでブロック |
| Pre-commit / CIスキャナー | プッシュ時に`gitleaks`やTruffleHogでゲート |
| 短寿命トークン | 長期トークンよりOIDCや短寿命PATを優先 |
| シークレットマネージャー | リポジトリではなくVaultやクラウドのシークレットマネージャー |
| ローテーションのランブック | 先に失効させ、その後に履歴を掃除 |
| 保護ブランチ＋CODEOWNERS | マージ前のレビューを必須化 |
| Webルートに`.git`を置かない | `.git`を本番環境にデプロイしない |

シークレットが誤ってコミットされたら、そのシークレットは確実に漏洩したものとして扱う。履歴の書き換えより、ローテーションのほうが確実だ。CIでスキャナーを走らせておけば、人が気づくかどうかに依存しなくて済む。

## 12. 一通りの実践例

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

### コマンドまとめ

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

> **参考文献:**
> - Scott Chacon & Ben Straub, *Pro Git (2nd Edition)* (`https://git-scm.com/book/en/v2`)
> - William Shotts, *The Linux Command Line (2nd Edition)*, 第17-18章 (`~/Documents/Books/Linux/`)
> - `man git`, `git help <command>`
> - [TruffleHog secret scanner](https://github.com/trufflesecurity/trufflehog)
> - [Gitleaks secret scanner](https://github.com/gitleaks/gitleaks)

> **Zero2Root** | 基礎シリーズ | kodoktheGr3at | 2026
> **リポジトリ:** [Zero2Root](https://github.com/Kodokthegr3at/Zero2Root)
> **フィードバックと貢献を歓迎します。** 誤りを見つけたらissueかPRを開いてください。
