# Study Knowledge Hub & Automated PDF Pipeline

Welcome to your study repository! This directory is an automated knowledge base designed to catalog your technical notes, convert raw Markdown/Text notes (such as AI chat exports) into publication-quality LaTeX PDFs, and maintain an interconnected conceptual knowledge graph.

---

## 📁 Directory Structure at a Glance

```text
D:\STUDY\
├── txt_md/     <-- INPUT & SURROGATES: Authoritative notes & search surrogates (both .md & .txt supported)
├── pdf/        <-- OUTPUT & STORAGE: All compiled and imported PDFs live here
├── scrap/      <-- UNIVERSAL DROPZONE: Drop raw notes (both .md & .txt) & PDFs here; isolates non-text PDFs
├── index/      <-- CONTROL PLANE: Master topic catalog, mindmap, governance & version ledger
│   ├── 00_syllabus_taxonomy.md <-- GATE 2027 PH Physics curriculum & coverage matrix
│   ├── 01_tool_usage.md       <-- Compiler usage & CLI automation
│   ├── 02_directory_management.md <-- Governance, naming SOP & rules
│   ├── 03_topic_index.md      <-- Master document catalog & coverage dashboard
│   ├── 04_interconnection_mindmap.md <-- Knowledge graph & relational triples
│   └── 05_contributing_and_versioning.md <-- Architecture & version ledger
├── md_skill/   <-- REUSABLE SKILLS VAULT: Skill blueprints & 1-click installer (install.bat)
├── tool/       <-- COMPILER: Pandoc + XeLaTeX publishing engine (STRICTLY IMMUTABLE)
├── manage.bat  <-- One-click automation runner (scan, process, sweep, audit-duplicates, coverage)
├── manage.py   <-- Master automation engine
└── README.md   <-- User manual (this file)
```

---

## 🚀 How to Use This Directory Efficiently

### 1. Converting Raw Notes to Stunning PDFs

You don't need to manually rename files or run complex command-line scripts. The AI acts as your directory manager.

#### Step 1: Drop Raw Notes in `txt_md/` or `scrap/`
- Paste any copied response from ChatGPT, Gemini, Claude, NotebookLM, or your own raw `.txt` / `.md` notes directly into [txt_md/](file:///D:/STUDY/txt_md/) or [scrap/](file:///D:/STUDY/scrap/).
- **Both `.md` and `.txt` files are fully supported**: Notes can use either `.md` or `.txt` extension seamlessly.
- Don't worry about the filename (e.g. `notes.txt`, `chat.md`, `download.txt` is fine).

#### Step 2: Tell the AI to Process
- In the chat, simply say:
  > *"Scan and process the notes in txt_md."*
- **What happens automatically**:
  1. The AI reads and analyzes the technical content.
  2. The file is renamed to a clean, semantic identifier in `kebab-case` (e.g., `ssp-bloch-theorem-and-band-structure.txt`).
  3. The note is cataloged in [index/03_topic_index.md](file:///D:/STUDY/index/03_topic_index.md).
  4. Its concepts and prerequisites are linked in [index/04_interconnection_mindmap.md](file:///D:/STUDY/index/04_interconnection_mindmap.md).
  5. The compiler compiles it using Pandoc + XeLaTeX, and moves the final PDF to [pdf/](file:///D:/STUDY/pdf/) with a matching name.

---

### 2. Direct PDF Imports & Provisional Surrogate Markdown

If you already have well-compiled LaTeX PDFs or digital documents with clear text layers (e.g. from Zotero, research papers, or prior exports):

1. **Paste them directly into [pdf/](file:///D:/STUDY/pdf/)**.
2. Tell the AI:
   > *"Scan pdf folder and index the new PDFs."*
3. **What happens automatically**:
   - The AI verifies the text layer, derives the core domain and concepts, and renames messy filenames to clean `kebab-case`.
   - **Provisional Surrogate Extraction (`pymupdf4llm`)**: The system automatically extracts a clean Markdown companion file into [txt_md/](file:///D:/STUDY/txt_md/) bearing a strict `DO NOT RECOMPILE` safety banner.
   - **Full-Text Search & Git Backup**: The surrogate Markdown allows instantaneous full-text search across your entire library without re-scanning binary PDFs, while backing up note text on GitHub (where binary PDFs are excluded).
   - **Seamless Replacement**: When you later paste an authentic `.txt` or `.md` source note, it automatically replaces the provisional surrogate, lifts the compilation lock, and compiles the definitive PDF.

---

## 📖 How to Access & Use the Catalog

Your knowledge base has two companion indexing files inside [index/](file:///D:/STUDY/index/):

### 1. Master Topic Index ([index/03_topic_index.md](file:///D:/STUDY/index/03_topic_index.md))
- **What it is**: Your master inventory of every document in the repository.
- **How to use it**:
  - Open the file to see the **Master Table** (tracking Document ID `DOC-XXX`, Semantic Name, Original Filename, Domain, and direct clickable PDF links).
  - Use `Ctrl + F` in VS Code or your editor to search for any keyword (e.g., `Harmonic Oscillator`, `Brillouin Zone`, `Liquid Drop`, or your original Zotero folder ID).
  - Detailed sections provide dense summaries and concept tags for every document.

### 2. Interconnected Knowledge Mindmap ([index/04_interconnection_mindmap.md](file:///D:/STUDY/index/04_interconnection_mindmap.md))
- **What it is**: A machine-readable knowledge graph (YAML + relational triples) mapping how topics connect, which concepts depend on each other, and shared themes.
- **How to use it (Interactive AI Queries)**:
  Because the mindmap is structured for AI reasoning, you can ask the AI questions directly in chat:
  - *"What notes do I have on 1D harmonic oscillators and ladder operators?"*
  - *"What are the prerequisite notes I should read before studying Bloch's theorem?"*
  - *"Find all documents related to Nuclear Shell Models."*
  - *"Give me a recommended reading roadmap for Quantum Mechanics based on my notes."*

The AI queries the mindmap graph and provides instant, contextual answers with direct links to the relevant PDFs.

### 3. GATE 2027 PH Physics Syllabus Taxonomy & Coverage Matrix ([index/00_syllabus_taxonomy.md](file:///D:/STUDY/index/00_syllabus_taxonomy.md))
- **What it is**: Complete curriculum breakdown of the official IIT Madras GATE 2027 PH Physics syllabus across 11 sections and 78 sub-topics, linking notes assigned to each unit and tracking real-time preparation progress.
- **How to check preparation metrics**:
  - Run `cmd /c "D:\STUDY\manage.bat coverage"` in the terminal or ask in chat: *"Check syllabus coverage"* or *"Show GATE preparation gaps"*.

### 4. Architecture, Contributing & Version Ledger ([index/05_contributing_and_versioning.md](file:///D:/STUDY/index/05_contributing_and_versioning.md))
- **What it is**: Complete developer and system documentation tracking repository working rules, lifecycle specifications, cumulative line-budget versioning, and change ledgers.

---

## ⚡ Master Chat Commands Directory

Because the AI is the cognitive brain of this repository, you do not need to memorize rigid CLI arguments or manual batch syntax. You can command the entire repository through natural conversation.

Here is the exhaustive, categorized master list of chat prompts for every operational possibility:

### 1. 📥 Dropzone & Universal Ingestion (`scrap/` & `txt_md/`)

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Process Universal Dropzone** | `"Check the scrap and do the rest"`<br>`"Sweep scrap and process everything"` | Runs `manage.bat sweep`, routes `.txt`/`.md` to `txt_md/`, routes valid digital PDFs to `pdf/`, isolates non-text PDFs in `scrap/`, extracts surrogates, and updates indexes. |
| **Ingest Raw Notes (Markdown & Text)** | `"Scan and process new notes in txt_md"`<br>`"Compile my new note on Debye Model"` | Analyzes technical content, deduplicates via MD5, renames to semantic `kebab-case`, compiles via XeLaTeX to `pdf/`, and catalogs in `03_topic_index.md`. |
| **Import Direct Digital PDFs** | `"Scan pdf/ and index new textbooks"`<br>`"Process the new PDF in pdf/"` | Verifies digital text layer ($\ge 50$ chars), extracts companion surrogate markdown via `pymupdf4llm` to `txt_md/` with `DO NOT RECOMPILE` lock, and maps in mindmap. |
| **Promote Note to Authoritative (Lifecycle 3)** | `"I wrote an authentic note for DOC-070 to replace the surrogate"` | Detects matching base name, deletes provisional surrogate markdown, releases compilation lock, compiles definitive XeLaTeX PDF, and promotes status to `Compiled from Source`. |
| **Inspect Quarantined Files** | `"Check quarantined files in scrap"`<br>`"Why was this PDF quarantined in scrap?"` | Audits files in `scrap/`, inspects font encoding and text layer density, reports why they were quarantined (< 50 chars / scanned image), preserving files indefinitely. |
| **Clean Up Misplaced Files** | `"Sweep repository and collect misplaced files"` | Searches root, `index/`, and extraneous paths for misplaced `.txt`, `.md`, or `.pdf` files and moves them to their authoritative directories. |

### 2. 🔍 Topic Search, Deep Derivations & Academic Problem Solving

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Search by Concept or Topic** | `"What notes do I have on Debye Model?"`<br>`"Do I have any notes on Perturbation Theory?"` | Performs Stage 1 control plane lookup in `00_syllabus_taxonomy.md` and `03_topic_index.md`, locates matching `DOC-XXX` records, and presents dense summaries with clickable PDF links. |
| **Detailed Proof & Derivation Walkthrough** | `"Explain the derivation of Bloch's Theorem from my notes"`<br>`"Derive the Debye $T^3$ law using DOC-070"` | Performs line-sliced reading of the focal note in `txt_md/`, extracts exact mathematical steps, and delivers a rigorous derivation rendered in LaTeX / KaTeX. |
| **Comparative Concept Analysis** | `"Compare the Einstein and Debye heat capacity models using my notes"` | Slices relevant sections across multiple notes (e.g. DOC-070 and DOC-139), contrasting physical assumptions, high/low-temperature limits, and formulas. |
| **Inspect Equations & Formulations** | `"Read DOC-015 and summarize its key equations"`<br>`"What are the boundary conditions in DOC-042?"` | Directly inspects the note, extracts foundational mathematical identities, Hamiltonian expressions, and boundary equations without full-book context dumps. |
| **Solve PYQs & Exercises** | `"How many questions in quantum mechanics PYQ are left to solve?"`<br>`"Solve question 14 from DOC-002"` | Evaluates unsolved problem blocks inside indexed notes, provides step-by-step mathematical solutions, and verifies units and dimensional consistency. |
| **Generate Study Practice Questions** | `"Generate 5 GATE practice problems on Solid State Physics from my notes"` | Synthesizes custom practice questions adhering to GATE standards directly derived from the equations and concepts in your cataloged notes. |

### 3. 🧠 Knowledge Graph, Mindmap & Relational Reasoning

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Trace Prerequisites** | `"What do I need to know before reading DOC-023?"`<br>`"What are the prerequisites for Superconductivity?"` | Queries incoming edges and `prerequisites` in `index/04_interconnection_mindmap.md` and returns a prerequisite tree with direct links to foundational notes. |
| **Explore Conceptual Bridges** | `"How do my notes on <Topic A> connect to <Topic B>?"`<br>`"How does DOC-001 connect to DOC-007?"` | Traverses relational triples (`shares Hamiltonian`, `prerequisite for`, `analogous to`) to explain the exact mathematical and physical bridge between documents. |
| **Domain-Wide Knowledge Exploration** | `"Show all notes related to Hamiltonian dynamics"`<br>`"Find all documents discussing Brillouin zones"` | Traverses YAML nodes sharing specific concept tags in `04_interconnection_mindmap.md` and generates an interconnected cluster summary. |
| **Sequential Reading Roadmaps** | `"Give me a recommended reading roadmap for Quantum Mechanics based on my notes"` | Analyzes prerequisite chains and syllabus sequence in `00_syllabus_taxonomy.md` to construct an optimal step-by-step curriculum reading path. |

### 4. 📊 GATE 2027 Syllabus & Curriculum Gap Auditing

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Comprehensive Syllabus Audit** | `"Check syllabus coverage"`<br>`"Show GATE 2027 preparation metrics"` | Queries `index/00_syllabus_taxonomy.md` (or runs `manage.bat coverage`) and reports active sections, total notes, sub-topic coverage percentages, and active document IDs. |
| **Curriculum Blind-Spot Detection** | `"Show curriculum gaps"`<br>`"Which GATE physics sections need more notes?"` | Identifies sections or sub-topics with 0 active notes, alerting you to unrepresented areas so you can source or author missing material. |
| **Section Deep Dive** | `"Show all notes under SEC-07 (Quantum Mechanics)"`<br>`"List all sub-topics under SEC-09 (Solid State Physics)"` | Filters `00_syllabus_taxonomy.md` and `03_topic_index.md` for specific GATE sections, listing all covered and pending syllabus units. |
| **Bootstrap or Synthesize Syllabus** | `"Synthesize curriculum for <subject>"`<br>`"Bootstrap syllabus taxonomy"` | If `00_syllabus_taxonomy.md` is absent and no syllabus is provided, the AI uses autonomous academic reasoning to construct a structured section breakdown (`SEC-01` to `SEC-XX`) and sub-topics. |

### 5. 🛡️ Repository Health, Deduplication & Maintenance

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Proactive Repository Audit** | `"Scan directory for any changes"`<br>`"Reconcile disk files against catalog"` | Executes `manage.bat scan`, comparing physical files in `txt_md/` and `pdf/` against `03_topic_index.md`, reporting any untracked or orphaned files. |
| **Detect Exact & Semantic Duplicates** | `"Check if there are any duplicate notes"`<br>`"Audit duplicates by MD5 hash"` | Executes `manage.bat audit-duplicates` to detect exact hash collisions and normalized text overlap across `txt_md/` and `pdf/`. |
| **Remove or Consolidate Notes** | `"Remove DOC-045 and clean up catalog and mindmap"`<br>`"Consolidate duplicate DOC-110 into DOC-002"` | Atomically removes specified files, strips the table row and detail block from `03_topic_index.md`, and prunes nodes and edges from `04_interconnection_mindmap.md`. |
| **Verify Toolchain & Compiler Status** | `"Check if LaTeX compiler and tools are working"` | Verifies environment prerequisites (Python 3.10+, Pandoc, XeLaTeX) and checks `tool/compile.bat` responsiveness. |

### 6. ⚡ Token Efficiency, Context Hygiene & Slash Commands

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Compact Conversation Context** | `"/compact"` or `"Compact our context to save tokens"` | Condenses long turn history, prunes ephemeral compiler output logs, and frees 80–90% of active tokens while keeping all repository state safe in `index/`. |
| **Audit Session Token Burn** | `"Is my workflow token efficient?"`<br>`"What is burning tokens in our current session?"` | Analyzes conversation logs and prompt patterns against the 5 Token-Conservation Laws, pointing out large reads vs surgical practices. |
| **CPU-Local Scratch Data Analysis** | `"Run a scratch filter to find all mentions of <concept> across all 140 notes"` | Authors an ephemeral Python script in `<scratch>`, runs it locally on CPU, and prints a compact 10-line summary into context (saving ~50,000 tokens). |
| **Long-Running Autonomous Goal** | `"/goal"` | Runs an extensive multi-step workflow (e.g. processing large batches or deep audits) thoroughly until completion without stopping early. |
| **Interactive Step-by-Step Planning** | `"/plan"` or `"/grill-me"` | Engages in strategic alignment before large repository refactorings or curriculum reorganizations. |

### 7. ⚙️ Portable Skills Deployment & Administration

| Goal / Operational Task | What to say in chat | What the AI does automatically |
|---|---|---|
| **Deploy Agent Skills** | `"Deploy skills from md_skill/"`<br>`"Install repository management skill"` | Runs `md_skill/install.bat` to deploy `karpathy-guidelines` and `repository-management` blueprints into `.agent/skills/`. |
| **Verify Skill Integrity** | `"Verify SHA256 checksums of installed skills"` | Computes and compares SHA256 hashes of `md_skill/` blueprints against `.agent/skills/` to guarantee synchronization. |
| **Inspect Release History & Ledger** | `"Show recent entries in the version ledger"`<br>`"What was added in Version 1.5.1?"` | Queries `index/05_contributing_and_versioning.md` and displays cycle dates, line budgets, and architectural change entries. |

---

## 🛠️ First-Time Agent Skills Installation (`md_skill/`)

The [`md_skill/`](file:///D:/STUDY/md_skill/) folder contains reusable blueprints for the two core agent skills:
1. **`karpathy-guidelines`** ([`md_skill/SKILL.md`](file:///D:/STUDY/md_skill/SKILL.md)): Behavioral safeguards against overcomplication, unrequested abstractions, and unsurgical edits.
2. **`repository-management`** ([`md_skill/management_skill.md`](file:///D:/STUDY/md_skill/management_skill.md)): Master rules for three-tier ingestion lifecycles, non-destructive note safety, and compilation interlocks.

### Quick 1-Click Installation
Whenever setting up this repository in a fresh environment or cloning to another machine, deploy both skills with one command:
```cmd
cmd /c "D:\STUDY\md_skill\install.bat"
```
*(Or simply double-click `md_skill\install.bat` in Windows File Explorer).*

### Manual PowerShell One-Liner
```powershell
New-Item -ItemType Directory -Force -Path ".agent\skills\karpathy-guidelines", ".agent\skills\repository-management"; `
Copy-Item "md_skill\SKILL.md" ".agent\skills\karpathy-guidelines\SKILL.md" -Force; `
Copy-Item "md_skill\management_skill.md" ".agent\skills\repository-management\SKILL.md" -Force
```

---

## ⚠️ Important Rules to Keep in Mind

1. **Leave `tool/` untouched (Do Not Recreate)**: The `tool/` directory is strictly read-only. It contains the compilation scripts and LaTeX templates. Never edit or delete files in `tool/`. If missing, do not attempt to recreate it manually; clone it from [https://github.com/Thunderock7777/ai-ready-markdown-to-pdf](https://github.com/Thunderock7777/ai-ready-markdown-to-pdf) (`git submodule update --init --recursive` or `git clone https://github.com/Thunderock7777/ai-ready-markdown-to-pdf tool`).
2. **Source notes stay safe**: The AI will never alter the conceptual text of your notes in `txt_md/`.
3. **Keep inputs in `txt_md/`**: Always drop your text/markdown files inside `txt_md/` (files placed in root or `index/` are ignored by design).
4. **Automatic Deduplication**: If you accidentally paste a note or PDF that already exists, the AI detects the duplicate (via content hash, file size, and topic comparison) to prevent redundant catalog entries or duplicate PDFs.
5. **Missing Syllabus Fallback**: If no syllabus file is present, the AI will ask you for one. If you don't provide one, the AI will automatically synthesize a complete academic curriculum taxonomy for your domain using its own reasoning.
6. **Fresh Start Auto-Sanitation**: On a brand-new setup (when the 3 index files do not exist), the AI automatically purges `txt_md/` to ensure a completely clean start, and configures `manage.bat` to bind to your local Python path.
