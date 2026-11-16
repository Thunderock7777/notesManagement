---
name: repository-management
description: Master operational management skill for the Study Knowledge Hub and automated PDF pipeline. Governs workspace discovery, three-tier note ingestion lifecycles (authentic notes, direct PDFs, and provisional surrogate Markdown), non-destructive source policies, tool immutability, mechanical automation boundaries, machine-readable control plane indexation, search isolation, and Option 1 virtual curriculum taxonomy.
---

# Repository Management Skill (Universal & Portable Edition)

This skill defines the operational laws, lifecycle state machines, directory governance, and automated pipeline rules for managing an automated **Study Knowledge Hub & Notes Management Repository**.

Any AI agent entering this workspace—whether pre-existing or initialized fresh in a brand-new directory on any machine—must execute strictly under this specification in coordination with the `karpathy-guidelines` skill.

---

## 1. Portable Workspace Architecture & Dynamic Root Resolution

### 1.1 Dynamic Root Resolution
The workspace root is defined dynamically as `<WORKSPACE_ROOT>` (the directory where `manage.py`, `manage.bat`, and `README.md` reside). **NEVER hardcode absolute machine paths** (such as specific drive letters `C:`, `D:`, or user profiles). All operational paths are resolved relative to `<WORKSPACE_ROOT>`.

### 1.2 Universal Directory Roles
```text
<WORKSPACE_ROOT>/
├── txt_md/     <-- INGESTION & TEXT: Authentic source notes & provisional search surrogates (both .md and .txt supported)
├── pdf/        <-- PUBLISHED OUTPUT: Final compiled XeLaTeX PDFs and verified digital PDF imports
├── scrap/      <-- UNIVERSAL DROPZONE & QUARANTINE: Dropzone for incoming notes (both .md and .txt) and PDFs; isolates non-text PDFs
├── index/      <-- CONTROL PLANE: Internal AI-only machine-readable indexation & relational graph
│   ├── README.md              <-- Master control plane index and quick entry
│   ├── 00_syllabus_taxonomy.md <-- Formal curriculum breakdown, sub-topic inventory & coverage matrix
│   ├── 01_tool_usage.md       <-- Compiler usage, execution flags & bypass commands
│   ├── 02_directory_management.md <-- Governance, naming SOP, deduplication & lifecycle rules
│   ├── 03_topic_index.md      <-- Master document catalog, coverage dashboard & detail blocks
│   ├── 04_interconnection_mindmap.md <-- Semantic YAML knowledge graph & relational triples
│   └── 05_contributing_and_versioning.md <-- Architecture, line-change budget & cumulative ledger
├── md_skill/   <-- REUSABLE SKILLS VAULT: Portable skill blueprints & automated installer driver
│   ├── README.md              <-- Skill deployment instructions
│   ├── install.bat            <-- 1-click deployment driver copying blueprints to .agent/skills/
│   ├── SKILL.md               <-- Karpathy Guidelines skill blueprint
│   └── management_skill.md    <-- Repository Management skill blueprint (authoritative source)
├── tool/       <-- COMPILER ENGINE: Pandoc + XeLaTeX publishing toolchain (STRICTLY IMMUTABLE)
│   ├── compile.bat            <-- Windows compilation driver
│   ├── setup.bat              <-- Environment verification script
│   ├── config/                <-- LaTeX templates, Lua filters, and normalizers
│   └── documentation/         <-- Architecture and rendering specifications
├── manage.bat  <-- One-click automation batch driver (scan, process, audit-duplicates, coverage)
├── manage.py   <-- Master automation engine (mechanical operations, deduplication & catalog reconciler)
└── README.md   <-- User manual and quick-start guide
```

### 1.3 Immutable Boundaries & Core Safeguards
1. **The `tool/` Directory is Read-Only, Strictly Immutable & Non-Recreatable**:
   - Never edit, modify, overwrite, append, or delete ANY file in `tool/` (`compile.bat`, `setup.bat`, Lua filters in `config/`, `custom.tex`, or documentation). Treat `tool/` as an external, frozen compiler engine.
   - **Missing Tool Invariant**: If the `tool/` folder does not exist in the workspace, **DO NOT attempt to remake or reconstruct it manually**. Instead, acquire the official tool automatically from its public repository:
     ```cmd
     git clone https://github.com/Thunderock7777/ai-ready-markdown-to-pdf tool
     ```
     *(Or if inside an existing Git repository with submodules: `git submodule update --init --recursive`).*
2. **Strict Ingestion Source Isolation**:
   - Only files placed inside `txt_md/` are eligible for note compilation.
   - Only pre-compiled PDFs placed inside `pdf/` are eligible for direct PDF ingestion.
   - Any `.txt`, `.md`, or `.pdf` file found outside these two folders (e.g. in root, `index/`, `tool/`) is **strictly ignored**—do NOT index, rename, or compile it.
3. **Non-Destructive Source Content Policy**:
   - Never alter, rewrite, edit, or summarize substantive conceptual content in `txt_md/`. Original equations, explanations, derivations, and statements must remain untouched.
   - *Exception*: Syntax-only fixes (closing broken fences, escaping invalid LaTeX tokens) are permitted ONLY when compilation fails with a fatal error or upon explicit user request.
4. **AI-Only Control Plane Mandate**:
   - The entire `index/` directory is an internal AI control plane designed for machine parsing, retrieval, and relational reasoning (not human visual presentation). Do not insert human diagrams or decorative charts into `03_topic_index.md` or `04_interconnection_mindmap.md`. When the user asks for relationships or summaries, query the control plane and respond in conversational markdown.
5. **Search Isolation Mandate**:
   - `manage.py` is a mechanical executor, NOT a search engine. When the user asks to search, find topics, or trace relationships, **`manage.py` must NEVER be used**. The AI agent performs all searching directly using native reading tools.
6. **Fundamental Architectural Prerequisite: Digital Text-Layer Mandate (Option C Gate)**:
   - The entire surrogate extraction pipeline (`pymupdf4llm`), full-text search across `txt_md/`, and relational mindmap strictly operate under the foundational requirement that **all imported PDFs must possess a clean, extractable digital text layer** (LaTeX-typeset or digital print).
   - Scanned image PDFs, photocopies, handwritten notebook pictures converted to PDF, camera snapshots, and files with missing or corrupted font encodings (`< 50` characters of extractable text) are **strictly prohibited from entering `pdf/`**.
   - If a non-text PDF is provided, the manager automatically quarantines it in `scrap/` (where it is preserved indefinitely and never deleted). To process its academic content, users must author an authentic text/markdown note in `txt_md/` (Lifecycle 1) to be compiled cleanly by XeLaTeX.

### 1.4 Universal Dropzone, File Sweeper & Quarantine Architecture (`scrap/`)
1. **Universal User Dropzone**:
   - The `scrap/` folder serves as a frictionless entry point. The user may paste any mixed collection of `.txt`, `.md`, or `.pdf` files directly into `scrap/` (or into workspace root) without worrying about folder conventions.
2. **Automated Misplaced File Sweeping (`manage.bat sweep` / `python manage.py sweep`)**:
   - When executed, the manager scans `scrap/`, workspace root, `index/`, `txt_md/`, and `pdf/`:
     - Text/Markdown notes (`.txt`, `.md`) are moved to their authoritative home in `txt_md/`.
     - Valid digital PDFs ($\ge 50$ clean characters) are moved to `pdf/`.
     - PDFs lacking extractable digital text ($< 50$ characters) are quarantined in `scrap/`.
3. **Quarantine Safety Policy (Zero Destruction)**:
   - Scanned, handwritten, or image-only PDFs quarantined in `scrap/` are preserved indefinitely.
   - The system **will never delete files in `scrap/` unless explicitly instructed by the user**.
4. **Dual Format Invariant (Both `.md` and `.txt` Supported)**:
   - Note files inside `txt_md/` and `scrap/` can freely be **both Markdown (`.md`) or raw plaintext (`.txt`)**.
   - Both formats are treated as first-class citizens throughout the entire pipeline.
   - The original extension (`.md` or `.txt`) is strictly preserved during semantic renaming and cataloging. Pandoc and Lua normalizers compile both seamlessly into XeLaTeX PDFs.

---

## 2. Systematic Order of Operations: The Complete Lifecycle

When operating in this repository—whether entering a fresh turn or processing incoming documents—the AI agent must follow this exact sequential lifecycle:

```mermaid
stateDiagram-v2
    [*] --> Phase0_Discovery

    state Phase0_Discovery {
        [*] --> CheckRoot
        CheckRoot --> GitStatusCheck: Verify clean workspace
        GitStatusCheck --> RunScan: manage.bat scan (Reconcile disk vs catalog)
        RunScan --> AuditDedup: manage.bat audit-duplicates
    }

    Phase0_Discovery --> IngestionRouter: Files pending ingestion
    Phase0_Discovery --> SearchMode: User asks search/query

    state IngestionRouter {
        [*] --> CheckLocation
        CheckLocation --> Lifecycle1: Placed in txt_md/
        CheckLocation --> Lifecycle2: Placed in pdf/
        CheckLocation --> Reject: Outside authorized paths
    }

    state "Lifecycle 1: Authentic Source Note" as Lifecycle1 {
        [*] --> DedupL1: MD5 & Text Dedup Check
        DedupL1 --> TaxonomyL1: Map to Virtual Section & Topic
        TaxonomyL1 --> RenameL1: kebab-case Rename ([domain]-[topic].[ext])
        RenameL1 --> CompileXeLaTeX: Non-interactive tool/compile.bat
        CompileXeLaTeX --> RoutePDF: Move PDF to pdf/
        RoutePDF --> CatalogL1: Register in 03_topic_index.md (Compiled from Source)
        CatalogL1 --> MindmapL1: Insert Node in 04_interconnection_mindmap.md (source_type: txt_md)
    }

    state "Lifecycle 2: Direct Digital PDF" as Lifecycle2 {
        [*] --> TextLayerGate: Text Layer Gate (len >= 50 clean chars)
        TextLayerGate --> RejectScanned: < 50 chars (Rejected Option C)
        TextLayerGate --> DedupL2: MD5 Content Dedup Check
        DedupL2 --> TaxonomyL2: Map to Virtual Section & Topic
        TaxonomyL2 --> RenamePDF: kebab-case Rename ([domain]-[topic].pdf)
        RenamePDF --> ExtractSurrogate: pymupdf4llm Parallel Extraction
        ExtractSurrogate --> ApplyBanner: Prepend DO NOT RECOMPILE Header
        ApplyBanner --> SaveSurrogate: Save to txt_md/<name>.md
        SaveSurrogate --> LockCompile: Strict Compilation Lock Activated
        LockCompile --> CatalogL2: Register in 03_topic_index.md (Provisional Source)
        CatalogL2 --> MindmapL2: Insert Node in 04_interconnection_mindmap.md (source_type: surrogate_md)
    }

    state "Lifecycle 3: Surrogate-to-Authoritative Promotion" as Lifecycle3 {
        SaveSurrogate --> UserDropsNote: User provides authentic note
        UserDropsNote --> DetectSurrogate: Match Base Name
        DetectSurrogate --> RemoveSurrogate: Cleanly remove provisional .md
        RemoveSurrogate --> ReleaseLock: Compilation Lock Released
        ReleaseLock --> CompileXeLaTeX
    }
```

### Phase 0: Discovery & Onboarding Protocol (On Session Startup)
Before touching any files or executing commands:
1. **Locate Workspace Root**: Identify the directory containing `manage.py` and `manage.bat`.
2. **Inspect Git Status**: Run `git status` to verify clean state, check for uncommitted changes or untracked user inputs.
3. **Verify Prerequisites**: Confirm that Python 3.10+, Pandoc, and XeLaTeX (`xelatex`) are accessible.
4. **Proactive Repository Audit (`manage.bat scan` / `python manage.py scan`)**:
   - Reconciles physical files in `txt_md/` and `pdf/` against `index/03_topic_index.md`.
   - Counts authentic source notes vs provisional surrogates and flags any unindexed files.
5. **Deduplication Audit (`manage.bat audit-duplicates`)**:
   - Verifies zero duplicate content hashes or identical body texts exist across the library.

---

### Phase 1: Ingestion Lifecycles & State Machine

#### Lifecycle 1: Processing Authentic Source Notes (`txt_md/` -> `pdf/`)
1. **Analyze Content**: Read the note to determine Domain, Core Concepts, Prerequisites, and dense Summary.
2. **Deduplication Check**: Compare MD5 hash and normalized body text against all files in `txt_md/`. If identical, halt and inform user.
3. **Taxonomy Classification**: Map document to its formal curriculum section (`SEC-XX`) and sub-topic unit based on `index/00_syllabus_taxonomy.md`.
4. **Semantic Renaming**: Rename to `kebab-case` (`[domain]-[topic].[ext]`). Notes can be **either `.md` or `.txt`**, and the original extension is strictly preserved throughout compilation.
5. **Headless Compilation**:
   - Run via `(echo Y & echo.) | tool\compile.bat txt_md\<filename>.md` (or through `manage.bat process`) with `BypassSandbox: true`.
   - Verify that `<filename>.pdf` was successfully created.
6. **PDF Routing**: Move `<filename>.pdf` from `txt_md/` to `pdf/`.
7. **Control Plane Registration**:
   - In `index/03_topic_index.md`: Add/update table row with `Section`, `Syllabus Topic`, and status `Compiled from Source`. Add detail history block.
   - In `index/04_interconnection_mindmap.md`: Insert node with `section:`, `syllabus_topic:`, `source_type: txt_md`, `source_note: <filename>.<ext>`, and connect relational edges.

#### Lifecycle 2: Ingesting Direct Pre-Compiled PDFs (`pdf/` -> `txt_md/`)
1. **Text Layer Quality Gate (Strict Rejection)**:
   - Verify digital text layer density ($\ge 50$ clean characters) via PyMuPDF.
   - Halt with exit code 1 if the PDF is an image-only scan, bitmap photocopy, or corrupted stream. Strictly reject non-digital PDFs.
2. **Deduplication Check**: Compare MD5 hash against existing PDFs in `pdf/`.
3. **Taxonomy Classification**: Determine primary curriculum section and sub-topic unit.
4. **Semantic Renaming**: Rename PDF in `pdf/` to semantic `kebab-case`.
5. **Surrogate Extraction (`pymupdf4llm`)**:
   - Extract structured Markdown into `txt_md/<basename>.md`.
   - Prepend mandatory safety banner:
     ```markdown
     <!-- ===================================================================== -->
     <!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
     <!-- Source PDF: <basename>.pdf                                            -->
     <!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
     <!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
     <!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
     <!-- ===================================================================== -->
     ```
6. **Strict Compilation Lock**: `manage.py` and compilation drivers must halt with exit code 1 if asked to compile a surrogate note.
7. **Control Plane Registration**:
   - `03_topic_index.md`: Register with status `Provisional Source (Auto-extracted)`.
   - `04_interconnection_mindmap.md`: Insert node with `source_type: surrogate_md`, `source_note: <basename>.md`.

#### Lifecycle 3: Promoting Surrogate to Authoritative Source
1. **Detect Trigger**: User drops an authentic `.txt` or `.md` note matching an existing surrogate base name.
2. **Remove Surrogate**: Safely delete the provisional `<basename>.md` file.
3. **Ingest Authentic Note**: Ingest, rename, and release the compilation lock.
4. **Compile Definitive PDF**: Compile via `tool/compile.bat` and overwrite `pdf/<basename>.pdf`.
5. **Promote Control Plane Status**:
   - `03_topic_index.md`: Promote status to `Compiled from Source`.
   - `04_interconnection_mindmap.md`: Promote node to `source_type: txt_md`.

---

## 3. Option 1: Virtual Curriculum Taxonomy Architecture

1. **Physical Storage Invariance**:
   - The physical directories `txt_md/` and `pdf/` **MUST ALWAYS REMAIN FLAT**.
   - **Never create physical section sub-directories** (e.g. `txt_md/SEC-07/` or `pdf/SEC-01/`). Physical sub-directories break relative Pandoc compilation paths, LaTeX font/filter loaders, and Git history.
2. **Virtual Control Plane Mapping**:
   - All hierarchical taxonomy (Sections, Topics, Units) is maintained virtually inside the `index/` control plane:
     - `index/00_syllabus_taxonomy.md`: Defines curriculum sections, lists all sub-topic units, and tracks coverage percentages.
     - `index/03_topic_index.md`: Master table columns `Section` (`SEC-01` to `SEC-XX`) and `Syllabus Topic`, plus detail blocks.
     - `index/04_interconnection_mindmap.md`: YAML node fields `section:` and `syllabus_topic:`.
3. **Real-Time Coverage Auditing**:
   - Run `cmd /c "manage.bat coverage"` (or `python manage.py coverage`) to generate a complete syllabus coverage audit, note counts, and curriculum gap alerts.

---

## 4. Automation Engine CLI Reference & Zero-Permission Pipeline

### 4.1 CLI Command Reference
The automation script (`manage.bat` on Windows, or `python manage.py` universally) provides the mechanical execution engine:

| Command | Arguments / Flags | Core Responsibility |
|---|---|---|
| `scan` | *(none)* | Audits physical files vs index, counts authentic notes vs surrogates, reports uncataloged files. |
| `sweep` | *(none)* | Sweeps `scrap/`, root, and misplaced directories; auto-routes notes to `txt_md/`, digital PDFs to `pdf/`, and quarantines non-text PDFs into `scrap/`. |
| `process` | *(reads `.pending.json`)* | Executes staged ingestion without interactive permission prompts. |
| `ingest-note` | `--file <path> --name <kebab> --domain <str> --concepts <csv> --summary <str> [--prerequisites <csv>]` | Renames note, compiles XeLaTeX PDF, routes PDF to `pdf/`, and registers in catalog & mindmap. |
| `ingest-pdf` | `--file <path> --name <kebab> --domain <str> --concepts <csv> --summary <str>` | Verifies text layer ($\ge 50$ chars), extracts surrogate `.md`, locks compilation, and catalogs. |
| `audit-duplicates`| *(none)* | Detects exact MD5 hash collisions and normalized body text duplicates across the repository. |
| `remove-doc` | `--doc-id <DOC-XXX> [--consolidate-into <DOC-YYY>]` | Atomically deletes files, cleans catalog row, removes detail block, and strips mindmap node/edges. |
| `coverage` | *(none)* | Displays curriculum coverage audit dashboard across all sections and sub-topic units. |

### 4.2 Zero-Permission Protocol (`.pending.json` Schema)
To prevent agent environments from prompting for permissions on every dynamic command invocation, the AI stages instructions into `.pending.json` in the workspace root, then invokes the static command:
```cmd
cmd /c "manage.bat process"
```
*(or `python manage.py process`).*

**`.pending.json` Schema**:
```json
{
  "action": "ingest-note",
  "file": "txt_md/raw_input.txt",
  "name": "ssp-bloch-wavefunction-and-theorem",
  "domain": "Solid State Physics",
  "concepts": "Bloch Theorem, Periodic Potential, Crystal Momentum",
  "summary": "Detailed derivation of Bloch theorem and periodic wavefunctions in periodic lattices.",
  "prerequisites": "DOC-001, DOC-018"
}
```
*(For direct PDF ingestion, set `"action": "ingest-pdf"` and point `"file"` to the PDF in `pdf/`).*

---

## 5. Control Plane Data Formats & Schemas

### 5.1 Catalog Schema (`index/03_topic_index.md`)
1. **Master Table Layout (8 Columns)**:
   ```markdown
   | ID | Section | Syllabus Topic | Semantic Filename | Original Filename | Generated PDF | Status | Last Updated |
   |---|---|---|---|---|---|---|---|
   | DOC-001 | **SEC-07** | `7.2` Schrödinger Dynamics | `qm-two-state.pdf` | `QM.pdf` | [qm-two-state.pdf](file:///.../pdf/qm-two-state.pdf) | Provisional Source (Auto-extracted) | 2026-11-15 |
   ```
2. **Document Detail Block Layout**:
   ```markdown
   ### [DOC-001] qm-two-state.pdf
   - **Source File**: [qm-two-state.md](file:///.../txt_md/qm-two-state.md) (Provisional Surrogate)
   - **Compiled PDF**: [qm-two-state.pdf](file:///.../pdf/qm-two-state.pdf)
   - **Original Filename**: `QM.pdf`
   - **GATE Section**: `SEC-07` (Quantum Mechanics)
   - **Syllabus Topic**: `7.2: Time-Independent & Time-Dependent Schrödinger Dynamics`
   - **Domain**: `Quantum Mechanics`
   - **Core Concepts**:
     - Wavefunction
     - Eigenstates
   - **Text Layer Quality**: Verified (LaTeX Typeset)
   - **Summary**: Concise technical summary...
   - **Processing Log**:
     - `2026-11-15`: Initial ingestion...
   ```

### 5.2 Mindmap YAML Knowledge Graph Schema (`index/04_interconnection_mindmap.md`)
```yaml
version: '1.3'
total_nodes: 131
total_edges: 150
nodes:
  - id: DOC-001
    file: qm-two-state.pdf
    source_type: surrogate_md # or txt_md, pdf_direct
    domain: Quantum Mechanics
    core_concepts:
      - Wavefunction
      - Eigenstates
    summary: Concise technical summary...
    source_note: qm-two-state.md
    section: SEC-07
    syllabus_topic: '`7.2` Schrödinger Dynamics'
edges:
  - from: DOC-001
    to: DOC-007
    relation: shares Eigenstates
```

---

## 6. Three-Stage Search & Retrieval Protocol (AI Execution Only)

When the user asks to search, find topics, explore conceptual connections, or review notes:
1. **Never Invoke `manage.py` for Search**: Searching is purely an AI reading, reasoning, and synthesis task.
2. **Sequential Search Execution**:
   - **Stage 1 (Control Plane Lookup)**: Query `index/03_topic_index.md` (Master Table + detail blocks) and `index/04_interconnection_mindmap.md` (YAML nodes and relational triples) to identify candidate `DOC-XXX` IDs, domains, syllabus topics, and prerequisites.
   - **Stage 2 (Full-Text Scan across `txt_md/`)**: Search across the plaintext `.md`/`.txt` files in `txt_md/` (covering 100% of notes thanks to surrogate extraction).
   - **Stage 3 (Deep Read & Synthesis)**: Use `read_file` on focal notes to inspect exact equations, proofs, and definitions. Deliver a synthesized answer with KaTeX math and clickable links to both source note (`[note.md](file:///.../txt_md/note.md)`) and published PDF (`[note.pdf](file:///.../pdf/note.pdf)`).

---

## 7. Proactive Maintenance, Git Standards & 8-Document Audit Checklist

1. **Session Entry Check**: Proactively run `manage.bat scan` on session startup.
2. **Zero Redundancy**: If duplicates are detected, consolidate into a single document ID immediately via `manage.bat remove-doc`.
3. **Git Hygiene**:
   - `.gitignore` must ignore `pdf/*` (except `pdf/.gitkeep`). Binary PDFs are never pushed.
   - All note text in `txt_md/` (authentic + surrogate) and index files in `index/` are tracked and pushed.
   - Never commit `.pending.json`, `tool/md2pdf_cache/`, `__pycache__/`, or scratch files.
4. **Mandated 8-Document Audit Checklist**:
   After any structural, workflow, or engine modification, audit and synchronize all 8 core documents:
   - `README.md` (Root user manual, quick start, workflow descriptions)
   - `index/README.md` (Master AI instructions, folder structure tree, operational rules)
   - `index/00_syllabus_taxonomy.md` (Curriculum breakdown, sub-topic inventory & coverage matrix)
   - `index/01_tool_usage.md` (Compiler flags, `manage.bat` command shapes, execution permissions)
   - `index/02_directory_management.md` (Taxonomic rules, kebab-case schemas, deduplication checks)
   - `index/03_topic_index.md` (Machine-readable inventory, coverage dashboard, detail history blocks)
   - `index/04_interconnection_mindmap.md` (YAML knowledge graph, total_nodes, total_edges, triples)
   - `index/05_contributing_and_versioning.md` (Working rules, lifecycle state machine, change ledger)

---

## 8. Portable Bootstrapping Guide: Deploying in a Fresh Directory

If this skill is introduced into a new, uninitialized folder:
1. **Initialize Directory Skeleton**: Create `txt_md/`, `pdf/`, `scrap/`, `index/`, `md_skill/`, and place `manage.py` and `manage.bat` in the root.
2. **Install Skills**: Run `md_skill/install.bat` (or manually copy blueprints) to deploy into `.agent/skills/`.
3. **Acquire Compiler Tool (Do Not Recreate)**:
   - If `tool/` is not present, **NEVER attempt to remake or re-code it manually**. Automatically download/clone it from its official public repository:
     ```cmd
     git clone https://github.com/Thunderock7777/ai-ready-markdown-to-pdf tool
     ```
     *(Or if in an existing repository with submodules: `git submodule update --init --recursive`).*
4. **Initialize Control Plane**:
   - Create `index/00_syllabus_taxonomy.md` defining the subject curriculum sections and sub-topics.
   - Create `index/03_topic_index.md` with the 8-column Master Table header.
   - Create `index/04_interconnection_mindmap.md` with baseline YAML header (`total_nodes: 0`, `total_edges: 0`).
5. **Run Baseline Scan**: Execute `manage.bat scan` (or `python manage.py scan`) to verify clean initialization.
