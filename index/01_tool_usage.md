# 01 - Tool Usage & Execution Guide

> [!IMPORTANT]
> **SKILL ADHERENCE MANDATE:**
> Every compilation or tool action must strictly adhere to [.agent/skills/karpathy-guidelines/SKILL.md](file:///D:/STUDY/.agent/skills/karpathy-guidelines/SKILL.md).
> Verify prerequisites first, execute surgically, do not speculate on file contents, and verify that the output PDF was successfully generated.

## Overview

The `tool/` directory contains **Markdown to PDF (v1.3.7)**, a specialized compiler pipeline that transforms raw text and Markdown notes (especially direct AI chat exports) into publication-grade PDFs.

The core pipeline:
1. **Pandoc AST Processing**: Reads the input Markdown/TXT.
2. **`markdown-normalizer.lua`**: Normalizes bare math (`\begin{align}` outside math blocks), standardizes Unicode subscripts, preserves HTML tags (`<sub>`, `<sup>`), wraps theorem environments, and standardizes code spans.
3. **`code-fence-runner.lua`**: Evaluates and caches executable code blocks (`python`, `c`, `cpp`, `java`) or renders LaTeX snippets cleanly.
4. **`custom.tex` & XeLaTeX**: Compiles the normalized document using TeX Live / MiKTeX with full multilingual support (Latin, Bengali, Hindi, CJK) and error recovery annotations (`[!!!]`).

---

## Strict Permission & Tool Safety

> [!CAUTION]
> **READ-ONLY MANDATE:**
> The entire `tool/` folder is **strictly read-only**.
> **NEVER** edit, delete, or append to any file in `tool/` (`compile.bat`, `setup.bat`, Lua scripts in `config/`, `custom.tex`, or documentation).
> It exists solely for execution.

### Execution Permissions (Windows Sandbox)
- On Windows, `pandoc.exe` (located at `%LOCALAPPDATA%\Pandoc\pandoc.exe`) and `xelatex.exe` (located at `C:\texlive\2026\bin\windows\xelatex.exe`) require access to local directories outside the sandbox.
- **Rule**: Whenever you invoke `compile.bat` or the compilation command from the agent environment, **always use `BypassSandbox: true`**. Do not hesitate or stall asking repeatedly about sandbox permissions—ask or execute with bypass directly to avoid permission denials.

---

## Running the Compiler

### Recommended Automation: `manage.bat` (Single Fast Ingestion)

The automation script `D:\STUDY\manage.py` (wrapped by `manage.bat`) acts as the mechanical engine for the AI.

#### Standard Zero-Permission Ingestion (Recommended)
To prevent Antigravity permission prompts on every file, stage the AI metadata into `.pending.json` in the workspace root, then run the static command:
```cmd
cmd /c "D:\STUDY\manage.bat process"
```
*(Once approved with "Always allow", this command shape is auto-approved forever with zero permission popups).*

#### Alternative CLI Flags:
- Ingest source note: `cmd /c "D:\STUDY\manage.bat ingest-note --file ... --name ... --domain ... --concepts ... --summary ..."`
- Ingest direct PDF: `cmd /c "D:\STUDY\manage.bat ingest-pdf --file ... --name ... --domain ... --concepts ... --summary ..."`
- Proactive scan: `cmd /c "D:\STUDY\manage.bat scan"` (audits repository and counts authentic source notes vs provisional surrogates)
- Syllabus coverage audit: `cmd /c "D:\STUDY\manage.bat coverage"` (computes and displays the complete GATE 2027 PH Physics syllabus preparation & coverage audit across all 11 sections, note counts, coverage levels, and curriculum gap alerts)
- Surrogate extraction: batch extracts companion Markdown approximations for all sourceless PDFs via `pymupdf4llm`.

---

## Strict Rules: When `manage.py` Can and Cannot Be Used

> [!IMPORTANT]
> **STRICT USAGE BOUNDARIES FOR `manage.py` & `manage.bat`**

### ✅ WHERE `manage.py` MUST BE USED:
1. **Mechanical File Operations in Authorized Folders**:
   - Renaming incoming raw notes inside `D:\STUDY\txt_md/` to semantic `kebab-case`.
   - Renaming incoming pre-compiled PDFs inside `D:\STUDY\pdf/` to semantic `kebab-case`.
   - Moving compiled PDFs from `txt_md/` to `pdf/`.
2. **Headless Compilation Driver & Interlock**:
   - Running `tool\compile.bat` non-interactively using piped stdin to handle pauses and uncached code execution prompts without freezing.
   - **Strict Compilation Lock**: Refusing to compile any provisional surrogate file bearing `DO NOT RECOMPILE` / `AUTO-GENERATED SURROGATE`, protecting XeLaTeX PDFs from being overwritten.
   - **Automatic Replacement**: Removing prior provisional surrogates when an authentic source note of the same base name is ingested.
3. **Atomic Catalog & Mindmap Updates**:
   - Safely appending or updating table rows and detailed history blocks in `index/03_topic_index.md`.
   - Safely inserting nodes and relational edges in `index/04_interconnection_mindmap.md`.
4. **Automated Deduplication & Repository Scanning**:
   - Checking MD5 content hashes against existing files in `txt_md/` and `pdf/` to prevent duplicate notes or PDFs.
   - Performing proactive scans (`manage.bat scan`) on session startup.
5. **Syllabus Coverage Auditing & Automatic Classification**:
   - Running `manage.bat coverage` to audit preparation progress across all 11 sections of the GATE 2027 PH Physics curriculum.
   - Automatically assigning GATE section (`SEC-01` to `SEC-11`) and syllabus sub-topics when generating new index entries in `03_topic_index.md` and `04_interconnection_mindmap.md`.

---

### ❌ WHERE `manage.py` IS STRICTLY FORBIDDEN:
1. **NEVER Touch the `tool/` Folder**:
   - `manage.py` is strictly forbidden from editing, modifying, overwriting, creating, or deleting ANY file inside `D:\STUDY\tool\` (`compile.bat`, `setup.bat`, `config/*`, `documentation/*`). The `tool/` directory is 100% read-only and immutable.
2. **NEVER Alter Substantive Content of Source Notes**:
   - `manage.py` must never modify, rephrase, rewrite, or trim the conceptual prose, mathematical formulas, or explanations inside notes in `D:\STUDY\txt_md/`.
3. **NEVER Replace AI Semantic Reasoning**:
   - `manage.py` is a mechanical executor, NOT a thinker. It must never use naive regex to invent titles or topic relationships autonomously. The AI model must ALWAYS read and analyze the note first, formulate the domain/concepts, and pass them to the script.
4. **NEVER Ingest Files Outside `txt_md/` and `pdf/`**:
   - `manage.py` must never touch or index `.txt`, `.md`, or `.pdf` files located in the root directory, `index/`, `tool/`, or external paths.
5. **NEVER Edit Root Instruction Files Directly via Script**:
   - `manage.py` only updates `03_topic_index.md` and `04_interconnection_mindmap.md`. It must never overwrite `index/README.md`, `index/01_tool_usage.md`, `index/02_directory_management.md`, or the root `README.md`.
6. **NEVER Use `manage.py` for Searching or Answering User Queries**:
   - When the user asks to search, find topics, trace concepts, or check relationships in the knowledge base, **`manage.py` must NEVER be invoked**.
   - The AI agent must perform all searching and retrieval **by itself**: directly inspecting `index/03_topic_index.md`, querying `index/04_interconnection_mindmap.md`, and reading documents directly with native file-reading tools to provide deep, contextual explanations with clickable links.

---

### Low-Level Compiler Direct Invocations
The compiler driver is located at `D:\STUDY\tool\compile.bat`. It accepts one or more quoted file paths:

```cmd
D:\STUDY\tool\compile.bat "D:\STUDY\txt_md\<filename>.md"
```

### Non-Interactive & Automated Execution (Bypassing Prompts)
`compile.bat` contains a terminal `pause` statement at the end and prompts for approval (`Y/N`) when uncached code fences run for the first time.

To execute the tool non-interactively without freezing on background pauses:

#### Method 1: Using PowerShell with Stdin Pipe
```powershell
cmd /c '(echo Y & echo.) | "D:\STUDY\tool\compile.bat" "D:\STUDY\txt_md\<filename>.md"'
```
- The first `echo Y` approves any executable code blocks.
- The second `echo.` sends an Enter key to satisfy the final `pause` command.

#### Method 2: Direct Command Line Invocation
If compiling multiple files into a single unified PDF:
```powershell
cmd /c '(echo Y & echo.) | "D:\STUDY\tool\compile.bat" "D:\STUDY\txt_md\part1.md" "D:\STUDY\txt_md\part2.md"'
```

---

## Output Management (Routing PDF to `pdf/`)

`compile.bat` automatically produces `<filename>.pdf` **in the same directory as the first input file** (`D:\STUDY\txt_md\`).

**Post-Compilation Step (Mandatory):**
Immediately upon successful compilation, move or copy the newly created PDF to the `D:\STUDY\pdf\` folder:

```powershell
Move-Item -Path "D:\STUDY\txt_md\<filename>.pdf" -Destination "D:\STUDY\pdf\<filename>.pdf" -Force
```

This guarantees:
- `D:\STUDY\txt_md\` contains **only** clean source text/markdown notes.
- `D:\STUDY\pdf\` contains **all** publication-ready PDFs with matching names.

---

## Supported Syntax & AI Export Guidelines

### 1. Direct AI Responses
You can paste raw responses from ChatGPT, Gemini, Claude, or NotebookLM directly. The normalizer handles:
- **Bare AMS Math**: Environments like `\begin{align}...\end{align}` or `\begin{equation}` in prose are automatically hoisted and wrapped in display math delimiters (`$$...$$`).
- **Inline Math**: Standard `$a^2 + b^2 = c^2$` and `\(...\)` work seamlessly.
- **Display Math**: `$$...$$` or `\[...\]` are standard.

### 2. Document Metadata
Metadata must be declared inside a fenced `yaml` block at the beginning of the file (traditional `---` front matter lines are treated as horizontal dividing rules):

````markdown
```yaml
title: "Body-Centered Cubic and Wigner-Seitz Cells"
author: "Antigravity Research Notes"
date: "2026-11-15"
page-layout: default # or "presentation" for 16:9 widescreen
title-rule: true     # set false to hide divider rule under title
```
````

### 3. Code Fences & Execution Attributes
- **Python**: ```` ```python ```` executes and embeds printed outputs / matplotlib plots automatically.
- **C / C++**: ```` ```c ```` or ```` ```cpp ```` compiles via GCC/G++ and executes.
- **Java**: ```` ```java ```` executes single-file Java programs.
- **LaTeX**: ```` ```latex ```` or ```` ```{.latex} ```` renders TikZ diagrams and formulas without attempting execution.

Key attributes (added inside fence header, e.g., ```` ```{.python trusted=true} ````):
- `trusted=true`: Skips confirmation prompts for fresh runs.
- `run=false`: Skips execution entirely, rendering the block as syntax-highlighted code.
- `output=false`: Executes the code but suppresses standard output from appearing in the PDF.
- `figures=false`: Python only; suppresses automatic embedding of generated plots.

---

## Troubleshooting & Build Diagnostics

- **`[!!!]` Badges in PDF**: If localized LaTeX syntax errors occur in prose, the Lua error annotator catches them and highlights the offending section with a red `[!!!]` badge in the PDF rather than failing the build. Check the console log or temporary `.tex` for the specific line.
- **Missing Characters**: If non-standard Unicode glyphs are missing from the default font, check the console output for `Missing character: There is no <char> in font ...`.
- **Cache Invalidation**: Build artifacts and cache hashes reside in `D:\STUDY\tool\md2pdf_cache\`. If cache corruption occurs, deleting that directory is safe; it will regenerate automatically.
