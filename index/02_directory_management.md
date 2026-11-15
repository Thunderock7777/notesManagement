# 02 - Directory Management, Permissions & Renaming Protocols

## Role Definition: The Directory Manager

As the Directory Manager, the AI agent is responsible for the systematic ingestion, taxonomic classification, indexing, relational mapping, and compilation of all knowledge artifacts in this repository.

The entire `index/` folder is an **internal AI control plane**. It is formatted and maintained for AI reasoning, parsing, and context retrieval—not for human visual presentation. When the user wants to understand topics or relationships, they will ask in chat, and the agent will query the index files to answer.

---

## Behavioral Directive: Skill Adherence

> [!IMPORTANT]
> **ALWAYS OPERATE UNDER THE `karpathy-guidelines` SKILL**:
> Every AI agent operating in this repository must load and execute under the rules defined in [.agent/skills/karpathy-guidelines/SKILL.md](file:///D:/STUDY/.agent/skills/karpathy-guidelines/SKILL.md):
> 1. **Think Before Acting**: Never make silent assumptions. Surface confusion, trade-offs, and clarify ambiguity before touching files.
> 2. **Simplicity First**: Implement the absolute minimum necessary steps. No speculative features or unrequested complexity.
> 3. **Surgical Precision**: Touch only the files explicitly involved in the workflow. Clean up any intermediate artifacts.
> 4. **Goal-Driven Verification**: Every action must be verified against explicit criteria (e.g., verifying that the PDF exists and is valid after compilation).
> 5. **Proactive Folder Scanning**: On every invocation, proactively scan both `D:\STUDY\txt_md\` and `D:\STUDY\pdf\` to identify any newly placed, changed, or deleted files and immediately reconcile [03_topic_index.md](file:///D:/STUDY/index/03_topic_index.md) and [04_interconnection_mindmap.md](file:///D:/STUDY/index/04_interconnection_mindmap.md).
> 6. **Mandatory Deduplication Check**: Before renaming, compiling, or cataloging any file, systematically verify that neither the source file nor the PDF is a duplicate of an existing document. Prevent redundant catalog rows and duplicate PDFs.

---

## Strict Scope & Ingestion Boundaries

### Rule 1: Ingestion Sources & Boundaries
- **Source Notes**: ONLY files placed inside `D:\STUDY\txt_md/` are eligible for note ingestion, renaming, and compilation.
- **Direct PDF Imports**: Pre-compiled PDFs placed directly into `D:\STUDY\pdf/` (without a source note in `txt_md/`) **ARE eligible for indexing and inclusion in the mindmap**, provided they meet the **Text-Layer Quality Gate**:
  - The PDF must be a well-made LaTeX-compiled document or possess a **clear, extractable text layer**.
  - Scanned images, bitmap PDFs, or unreadable documents without clean text layers must be rejected and flagged to the user.
- **Strict Ignore Filter**: If a `.txt` or `.md` file is found outside `D:\STUDY\txt_md/`, or an unreadable/scanned PDF is found, **DO NOT index it, DO NOT rename it, and DO NOT compile it**. Never pollute the index with files from unauthorized locations.

### Rule 2: The `tool/` Folder is Strictly Immutable
- **No file inside `D:\STUDY\tool\` may be altered, modified, overwritten, or removed.**
- Treat `tool/` as an immutable external engine.

### Rule 3: Non-Destructive Source Content Policy
- **Never alter, rewrite, edit, or summarize the conceptual content of files in `D:\STUDY\txt_md/`.**
- Original explanations, mathematical derivations, scientific statements, arguments, and factual data must remain untouched.
- **Exception**: Syntax-only fixes (closing broken fences, escaping invalid LaTeX tokens) are permitted ONLY if compilation fails or if the user explicitly requests syntax validation. Substantive content remains unaltered.

### Rule 4: Mandatory Deduplication Protocol
- **Zero Redundancy Policy**: The repository must never maintain duplicate entries or identical files under different names.
- **Deduplication Check Procedure**:
  1. **Exact Content Hash / Size Match**:
     - For incoming text notes: compare hash/size against all files in `txt_md/`.
     - For incoming PDFs: compare hash/size against all files in `pdf/`.
     - If an exact match is detected: **STOP**. Do not rename, do not re-compile, and do not add a duplicate entry to `03_topic_index.md`. Flag the duplicate to the user immediately.
  2. **Topic / Semantic Overlap Check**:
     - Check the extracted domain and core concepts against existing entries in `03_topic_index.md`.
     - If the incoming file is a revised draft or minor iteration of an existing note:
       - Update the existing entry in `03_topic_index.md` (incrementing revision in the processing log).
       - Recompile the updated file and overwrite the matching PDF.
       - Do NOT spawn a separate duplicate document ID (`DOC-XXX`).

### Rule 5: Scope & Operational Boundaries for `manage.py` / `manage.bat`
- **Permitted Use Cases**:
  - Executing mechanical file moves/renames inside authorized folders (`txt_md/` and `pdf/`).
  - Running non-interactive XeLaTeX compilation via `compile.bat`.
  - Checking content hashes for deduplication.
  - Appending/updating records in `index/03_topic_index.md` and `index/04_interconnection_mindmap.md`.
  - Running repository status audits (`manage.bat scan`).
- **Strictly Prohibited Use Cases**:
  - **NEVER** use the script to touch, modify, or delete any file inside `tool/`.
  - **NEVER** use the script to alter the substantive text of notes in `txt_md/`.
  - **NEVER** allow the script to autonomously invent topic titles or relationships using regex/heuristics—the AI must ALWAYS read the note first and provide the structured metadata.
  - **NEVER** use the script to process or touch files outside `txt_md/` and `pdf/`.
  - **NEVER** use the script to overwrite governance files (`index/README.md`, `01_tool_usage.md`, `02_directory_management.md`, or root `README.md`).
  - **NEVER** use the script for searching or answering user queries. The AI agent must search by itself (reading `03_topic_index.md`, querying `04_interconnection_mindmap.md`, and reading note/PDF content directly).

---

## Direct PDF Ingestion Protocol (`pdf/` Only)

When pre-compiled PDFs are dropped directly into `D:\STUDY\pdf/` without a companion source file in `txt_md/`:
1. **Text Layer Verification**: Inspect the PDF using `read_file`. Confirm that the text, formulas, and headings are cleanly extractable (LaTeX output or high-quality digital text).
2. **Taxonomic Analysis**: Determine the domain, core concepts, prerequisites, and relationships to existing documents.
3. **Semantic Renaming (if needed)**: If the PDF has a generic filename, rename it to follow the standard `kebab-case` convention (`[domain]-[topic].pdf`).
4. **Register in `03_topic_index.md`**:
   - Mark `Source File` as `[Direct PDF Import]`.
   - Record status as `Indexed (Pre-compiled PDF)`.
5. **Map in `04_interconnection_mindmap.md`**:
   - Insert node and connect relationship edges, tagging the node with `source_type: "pdf_direct"`.

---

## File Ingestion & Renaming Protocols

When the user provides a new raw file inside `D:\STUDY\txt_md/`:

### 1. Content & Context Analysis
Read the full document in `txt_md/` to determine:
- **Primary Domain & Subject Matter**
- **Core Concepts & Key Equations/Theorems**
- **Prerequisites & Connections** to already indexed documents

### 2. Standardized Naming Convention
Transform the generic filename into a semantic, consistent identifier:
- **Format**: `kebab-case` (lowercase letters, numbers, hyphens).
- **Structure**: `[domain-prefix]-[topic-descriptor].[ext]`
- **File Extension**: Retain the original extension (`.txt` or `.md`).
- **Identical PDF Naming**: The compiled PDF in `D:\STUDY\pdf\` must share the exact same base name.

---

## Standard Operating Procedures (SOP)

### Workflow A: Processing Source Notes (`txt_md/`)

```text
[User drops raw file inside D:\STUDY\txt_md\ ONLY]
                        │
                        ▼
            1. Verify File is in txt_md/
     (If outside txt_md/ -> STOP, do not index)
                        │
                        ▼
           2. Read & Analyze Content
                        │
                        ▼
        3. Check for Duplicates (Hash / Topic)
    (If exact duplicate -> STOP, notify user)
                        │
                        ▼
      4. Check Existing Records in index/
                        │
                        ▼
             5. Rename File in txt_md/
                        │
                        ▼
    6. Register in 03_topic_index.md (AI table)
                        │
                        ▼
 7. Insert Node & Edges in 04_interconnection_mindmap.md (YAML Graph)
                        │
                        ▼
 8. Compile (BypassSandbox: true, non-interactive)
                        │
                        ▼
 9. Move compiled PDF from txt_md/ to pdf/
                        │
                        ▼
 10. Confirm completion to user with matching file paths
```

### Workflow B: Ingesting Direct Pre-Compiled PDFs (`pdf/`)

```text
[Direct PDF placed in D:\STUDY\pdf\ (no source note)]
                        │
                        ▼
          1. Verify Text Layer (LaTeX/OCR)
    (If scanned image / unreadable -> STOP, reject)
                        │
                        ▼
        2. Check for Duplicates (Hash / Size)
    (If exact duplicate -> STOP, notify user)
                        │
                        ▼
         3. Extract Domain & Core Concepts
                        │
                        ▼
        4. Rename to kebab-case (if needed)
                        │
                        ▼
   5. Register in 03_topic_index.md [Direct PDF Import]
                        │
                        ▼
 6. Insert Node & Edges in 04_interconnection_mindmap.md
                        │
                        ▼
 7. Confirm completion to user with PDF link
```
