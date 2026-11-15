# Study Knowledge Hub & Automated PDF Pipeline

Welcome to your study repository! This directory is an automated knowledge base designed to catalog your technical notes, convert raw Markdown/Text notes (such as AI chat exports) into publication-quality LaTeX PDFs, and maintain an interconnected conceptual knowledge graph.

---

## 📁 Directory Structure at a Glance

```text
D:\STUDY\
├── txt_md/     <-- INPUT: Paste your raw .txt or .md notes here
├── pdf/        <-- OUTPUT & STORAGE: All compiled and imported PDFs live here
├── index/      <-- CONTROL PLANE: Master topic catalog and AI knowledge mindmap
├── tool/       <-- COMPILER: Pandoc + XeLaTeX publishing engine (DO NOT EDIT)
├── manage.bat  <-- One-click automation script (ingest, compile, index)
├── manage.py   <-- Master automation engine
├── README.md   <-- User manual (this file)
└── SKILL.md    <-- Active AI behavioral guidelines (Karpathy Guidelines)
```

---

## 🚀 How to Use This Directory Efficiently

### 1. Converting Raw Notes to Stunning PDFs

You don't need to manually rename files or run complex command-line scripts. The AI acts as your directory manager.

#### Step 1: Drop Raw Notes in `txt_md/`
- Paste any copied response from ChatGPT, Gemini, Claude, NotebookLM, or your own raw `.txt` / `.md` notes directly into [txt_md/](file:///D:/STUDY/txt_md/).
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

### 2. Direct PDF Imports (No Source Text Needed)

If you already have well-compiled LaTeX PDFs or digital documents with clear text layers (e.g. from Zotero, research papers, or prior exports):

1. **Paste them directly into [pdf/](file:///D:/STUDY/pdf/)**.
2. Tell the AI:
   > *"Scan pdf folder and index the new PDFs."*
3. The AI verifies the text layer, derives the core domain and concepts, renames messy filenames to clean `kebab-case`, and updates the catalog and relational mindmap.

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

---

## ⚡ Useful Chat Commands

Here are quick prompts you can give the AI at any time:

| What you want to do | What to say in chat |
|---|---|
| Ingest new notes in `txt_md/` | `"Scan and process new notes"` |
| Check for any new PDFs or changes | `"Scan directory for any changes"` |
| Query a topic | `"What notes do I have on <topic>?"` |
| Explore connections | `"How do my notes on <Topic A> connect to <Topic B>?"` |
| Find prerequisites | `"What do I need to know before reading DOC-023?"` |
| Inspect a specific PDF | `"Read DOC-015 and summarize its key equations"` |

---

## ⚠️ Important Rules to Keep in Mind

1. **Leave `tool/` untouched**: The `tool/` directory is strictly read-only. It contains the compilation scripts and LaTeX templates. Never edit or delete files in `tool/`.
2. **Source notes stay safe**: The AI will never alter the conceptual text of your notes in `txt_md/`.
3. **Keep inputs in `txt_md/`**: Always drop your text/markdown files inside `txt_md/` (files placed in root or `index/` are ignored by design).
4. **Automatic Deduplication**: If you accidentally paste a note or PDF that already exists, the AI detects the duplicate (via content hash, file size, and topic comparison) to prevent redundant catalog entries or duplicate PDFs.
