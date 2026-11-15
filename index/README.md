# Master Directory Index & Instructions

> [!IMPORTANT]
> **MANDATORY INSTRUCTIONS FOR ALL AI MODELS AND AGENTS:**
> 1. **READ THIS `index/` FOLDER FIRST**: Before performing any action in this workspace, you must read the instruction files in this directory.
> 2. **ALWAYS USE THE INSTALLED SKILL**: You must strictly apply and follow the `karpathy-guidelines` skill ([SKILL.md](file:///D:/STUDY/.agent/skills/karpathy-guidelines/SKILL.md)) for every operation:
>    - **Think Before Acting**: State assumptions explicitly. If uncertain or ambiguous, ask. Never guess silently.
>    - **Simplicity First**: Minimum necessary actions only. No speculative features or unrequested complexity.
>    - **Surgical Changes**: Touch only what you must. Never alter unrelated code or files.
>    - **Goal-Driven Execution**: Define clear success criteria and verify completion step-by-step.
> 3. **PROACTIVE SCAN ON EVERY INVOCATION**: Every time you enter or begin a session in this repository, you must immediately scan both `D:\STUDY\txt_md\` and `D:\STUDY\pdf\` to detect any changes (newly added files, renames, or modifications) and reconcile [03_topic_index.md](file:///D:/STUDY/index/03_topic_index.md) and [04_interconnection_mindmap.md](file:///D:/STUDY/index/04_interconnection_mindmap.md).
> 4. **MANDATORY DEDUPLICATION CHECK**: Always verify whether any newly detected `.txt`, `.md`, or `.pdf` file is a duplicate (by content hash, size, or topic match) before proceeding. Never create duplicate catalog entries or duplicate PDFs.
> 5. **AI-ONLY CONTROL PLANE**: The `index/` directory is an internal AI control plane designed for machine parsing, retrieval, and relational reasoning (not human visualization).

---

## Workspace Structure Overview

```text
D:\STUDY\
├── index/                     <-- INTERNAL AI CONTROL PLANE (Machine-readable)
│   ├── README.md              <-- Master entry point (this file)
│   ├── 01_tool_usage.md       <-- Compiler usage, execution flags & bypass commands
│   ├── 02_directory_management.md <-- Governance, strict txt_md isolation & renaming SOP
│   ├── 03_topic_index.md      <-- Machine-readable document inventory & metadata
│   ├── 04_interconnection_mindmap.md <-- Semantic YAML knowledge graph & relational triples
│   └── 05_contributing_and_versioning.md <-- Working rules, lifecycle specs, ledger & version policy
│
├── tool/                      <-- STRICTLY IMMUTABLE COMPILER ENGINE
│   ├── compile.bat            <-- Windows compilation driver
│   ├── setup.bat              <-- Environment verification script
│   ├── config/                <-- LaTeX templates and Lua filters
│   └── documentation/         <-- Architecture and rendering specifications
│
├── txt_md/                    <-- EXCLUSIVE INGESTION SOURCE (User puts raw files here)
├── pdf/                       <-- FINAL PUBLISHED PDFS (Compiled outputs saved here)
├── manage.bat                 <-- One-click automation runner
└── manage.py                  <-- Master automation engine (renaming, compiling, indexing)
```

---

## Core Operational Rules

1. **Strict Ingestion Source Isolation & Three-Tier Ingestion**:
   - **Authentic Source Notes**: ONLY authentic source files placed directly inside `D:\STUDY\txt_md\` are eligible to be compiled from source into `pdf/`.
   - **Direct PDF Imports & Provisional Surrogates**: Pre-compiled PDFs placed directly into `D:\STUDY\pdf\` without source notes are indexed and companion surrogate Markdown files are extracted via `pymupdf4llm` into `txt_md/<basename>.md` carrying the `DO NOT RECOMPILE` safeguard banner. This enables instant full-text search, token-efficient context retrieval, and Git backup without compiling.
   - **Authoritative Replacement**: When the user provides an authentic `.txt` or `.md` note, it automatically supersedes and deletes the provisional surrogate, unlocks compilation, and compiles the definitive XeLaTeX PDF into `pdf/`.
   - If a `.txt` or `.md` file exists anywhere else (e.g. mistakenly placed in `index/`, `tool/`, or workspace root), **DO NOT index it**.
2. **`tool/` is Strictly Immutable**:
   - No AI model may edit, modify, overwrite, or delete files inside `tool/`.
3. **No Content Alteration**:
   - Never modify or summarize substantive content in `txt_md/`. Only syntax fixes are permitted when explicitly requested or required to resolve fatal build crashes.
4. **Machine-Oriented Mindmap**:
   - The knowledge graph in [04_interconnection_mindmap.md](file:///D:/STUDY/index/04_interconnection_mindmap.md) is structured in dense YAML and semantic triples for AI traversal. The user will ask the AI directly for insights, connections, and summaries.
5. **Deduplication Check (Zero Redundancy)**:
   - Systematically verify if any incoming `.txt`, `.md`, or `.pdf` file is a duplicate before indexing or compiling:
     - **Exact Duplicates**: Check content hash / file size against existing files in `txt_md/` and `pdf/`. If identical, do not re-compile or create duplicate catalog rows. Flag to user.
     - **Revisions / Updated Drafts**: If a file is an updated version of an existing note, update the existing entry in `03_topic_index.md` and recompile instead of creating redundant duplicate entries.
6. **Strict Scope for Automation Script (`manage.py` / `manage.bat`)**:
   - **Permitted**: Mechanical file renaming in `txt_md/` and `pdf/`, headless XeLaTeX compilation, routing PDFs, deduplication checks, and updating `03_topic_index.md` & `04_interconnection_mindmap.md`.
   - **Strictly Prohibited**: Never touch or modify `tool/`, never alter substantive note content in `txt_md/`, never replace AI semantic reasoning with script heuristics, never touch files outside `txt_md/` and `pdf/`, and **never use the script for searching** (the AI must always search and answer queries by itself).
   - **Compilation Interlock**: `manage.py` strictly refuses to compile any file marked with the provisional surrogate header (`DO NOT RECOMPILE`).
7. **Execution Permissions**:
   - Run compilation and ingestion via `cmd /c "D:\STUDY\manage.bat process"` with `BypassSandbox: true` (auto-approvable static command shape).
