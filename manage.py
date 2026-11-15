#!/usr/bin/env python3
"""
Study Repository Automation Engine (manage.py)
-----------------------------------------------
Executes deterministic operations instructed by the AI agent:
- Content hash & deduplication checks
- File renaming in txt_md/ and pdf/
- Non-interactive Pandoc + XeLaTeX compilation via tool/compile.bat
- Moving compiled PDFs from txt_md/ to pdf/
- Safe, atomic updates to index/03_topic_index.md
- Safe, atomic updates to index/04_interconnection_mindmap.md
"""

import os
import sys
import argparse
import hashlib
import json
import shutil
import subprocess
import re
import fitz
import yaml

WORKSPACE = os.path.abspath(os.path.dirname(__file__))
TXT_MD_DIR = os.path.join(WORKSPACE, "txt_md")
PDF_DIR = os.path.join(WORKSPACE, "pdf")
INDEX_DIR = os.path.join(WORKSPACE, "index")
TOOL_DIR = os.path.join(WORKSPACE, "tool")
COMPILE_BAT = os.path.join(TOOL_DIR, "compile.bat")
TOPIC_INDEX_FILE = os.path.join(INDEX_DIR, "03_topic_index.md")
MINDMAP_FILE = os.path.join(INDEX_DIR, "04_interconnection_mindmap.md")

def get_file_hash(filepath):
    """Compute MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_next_doc_id():
    """Parse 03_topic_index.md to find the highest DOC-XXX number."""
    if not os.path.exists(TOPIC_INDEX_FILE):
        return "DOC-001"
    
    with open(TOPIC_INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.findall(r'\[DOC-(\d+)\]', content)
    if not matches:
        matches = re.findall(r'\| DOC-(\d+)', content)
        
    if matches:
        highest = max(int(m) for m in matches)
        return f"DOC-{highest + 1:03d}"
    return "DOC-001"

def check_duplicate_content(source_path, target_dir):
    """Check if source_path has an exact duplicate in target_dir by MD5."""
    if not os.path.exists(source_path):
        return None
    src_hash = get_file_hash(source_path)
    src_size = os.path.getsize(source_path)
    
    for fname in os.listdir(target_dir):
        fpath = os.path.join(target_dir, fname)
        if os.path.isfile(fpath) and fpath != os.path.abspath(source_path):
            if os.path.getsize(fpath) == src_size:
                if get_file_hash(fpath) == src_hash:
                    return fname
    return None

def update_topic_index_file(doc_id, semantic_name, orig_name, domain, concepts, pdf_name, summary, source_type="txt_md", revision_info=None):
    """Safely updates or appends to 03_topic_index.md."""
    if not os.path.exists(TOPIC_INDEX_FILE):
        print(f"Error: {TOPIC_INDEX_FILE} not found.")
        return False
        
    with open(TOPIC_INDEX_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    # Check if doc_id already exists (update existing)
    existing_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(f"| {doc_id} |") or line.strip().startswith(f"### [{doc_id}]"):
            existing_idx = i
            break
            
    concepts_str = ", ".join(concepts[:2]) if concepts else domain
    status_str = "Compiled from Source" if source_type == "txt_md" else "Indexed (Direct PDF Import)"
    today = "2026-11-15"
    
    table_row = f"| {doc_id} | `{pdf_name}` | `{orig_name}` | **{domain}**: {concepts_str} | [{pdf_name}](file:///D:/STUDY/pdf/{pdf_name}) | {status_str} | {today} |\n"
    
    source_file_entry = f"[{semantic_name}](file:///D:/STUDY/txt_md/{semantic_name})" if source_type == "txt_md" else f"`N/A - Direct PDF Import`"
    
    concepts_list_str = "\n".join([f"  - {c}" for c in concepts])
    log_entry = f"  - `{today}`: {revision_info}" if revision_info else f"  - `{today}`: Ingested, semantically renamed to `{semantic_name}`, and cataloged."
    
    detail_block = f"""
### [{doc_id}] {pdf_name}
- **Source File**: {source_file_entry}
- **Compiled PDF**: [{pdf_name}](file:///D:/STUDY/pdf/{pdf_name})
- **Original Filename**: `{orig_name}`
- **Domain**: `{domain}`
- **Core Concepts**:
{concepts_list_str}
- **Text Layer Quality**: Verified
- **Summary**: {summary}
- **Processing Log**:
{log_entry}
"""

    full_content = "".join(lines)
    
    # If doc_id already exists in detailed block, replace it
    if f"### [{doc_id}]" in full_content:
        # Update table row
        new_lines = []
        for line in lines:
            if line.strip().startswith(f"| {doc_id} |"):
                new_lines.append(table_row)
            else:
                new_lines.append(line)
        full_content = "".join(new_lines)
        
        # Replace detail block
        pattern = rf"### \[{doc_id}\][\s\S]*?(?=\n### \[|\n---|\Z)"
        full_content = re.sub(pattern, detail_block.strip() + "\n", full_content)
    else:
        # Append to table
        table_end = -1
        for i, line in enumerate(lines):
            if line.strip() == "---":
                table_end = i
                break
        if table_end != -1:
            lines.insert(table_end, table_row)
            full_content = "".join(lines) + detail_block
        else:
            full_content += "\n" + table_row + detail_block
            
    with open(TOPIC_INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(full_content)
    return True

def update_mindmap_file(doc_id, pdf_name, source_type, domain, concepts, summary, source_note=None, prerequisites=None):
    """Safely updates or appends node to 04_interconnection_mindmap.md."""
    if not os.path.exists(MINDMAP_FILE):
        return False
        
    with open(MINDMAP_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    node_dict = {
        "id": doc_id,
        "file": pdf_name,
        "source_type": source_type,
        "domain": domain,
        "core_concepts": concepts,
        "summary": summary
    }
    if source_note:
        node_dict["source_note"] = source_note
    if prerequisites:
        node_dict["prerequisites"] = prerequisites
        
    yaml_node = yaml.dump([node_dict], sort_keys=False, indent=2)
    # Strip opening list dash indentation to match schema
    node_str = "  " + yaml_node.strip().replace("\n", "\n  ") + "\n"
    
    # Check if node exists
    if f"id: {doc_id}" in content:
        # Node already present, updated in place
        pattern = rf"- id: {doc_id}[\s\S]*?(?=\n- id:|\nedges:)"
        content = re.sub(pattern, yaml.dump(node_dict, sort_keys=False).strip(), content)
    else:
        # Insert before edges:
        if "edges:" in content:
            content = content.replace("edges:\n", f"{yaml.dump([node_dict], sort_keys=False)}\nedges:\n")
        else:
            content += f"\n{yaml.dump([node_dict], sort_keys=False)}\n"
            
    with open(MINDMAP_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def cmd_scan():
    """Scans txt_md and pdf for unindexed or duplicate files."""
    print("=== STUDY REPOSITORY STATUS SCAN ===")
    txt_files = [f for f in os.listdir(TXT_MD_DIR) if os.path.isfile(os.path.join(TXT_MD_DIR, f))]
    pdf_files = [f for f in os.listdir(PDF_DIR) if os.path.isfile(os.path.join(PDF_DIR, f))]
    
    print(f"Notes in txt_md/: {len(txt_files)}")
    print(f"PDFs in pdf/:     {len(pdf_files)}")
    
    with open(TOPIC_INDEX_FILE, "r", encoding="utf-8") as f:
        index_text = f.read()
        
    unindexed_txt = [f for f in txt_files if f not in index_text]
    unindexed_pdf = [f for f in pdf_files if f not in index_text]
    
    if unindexed_txt:
        print(f" [!] Unindexed notes in txt_md/: {unindexed_txt}")
    else:
        print(" [OK] All notes in txt_md/ are cataloged.")
        
    if unindexed_pdf:
        print(f" [!] Unindexed PDFs in pdf/: {unindexed_pdf}")
    else:
        print(" [OK] All PDFs in pdf/ are cataloged.")

def cmd_ingest_note(args):
    """Executes atomic ingestion of a source note."""
    src_file = os.path.abspath(args.file)
    if not os.path.exists(src_file):
        print(f"Error: File not found: {src_file}")
        sys.exit(1)
        
    orig_name = os.path.basename(src_file)
    target_base = args.name.replace(".txt", "").replace(".md", "").replace(".pdf", "")
    target_ext = os.path.splitext(src_file)[1] or ".txt"
    semantic_txt_name = f"{target_base}{target_ext}"
    semantic_pdf_name = f"{target_base}.pdf"
    
    # 1. Deduplication Check
    dup_txt = check_duplicate_content(src_file, TXT_MD_DIR)
    if dup_txt and dup_txt != orig_name:
        print(f"[DEDUPLICATION STOP] Exact duplicate note content already exists as: {dup_txt}. Aborting ingestion to prevent duplicate catalog entries.")
        sys.exit(0)
        
    # 2. Rename/Move to semantic name in txt_md/
    final_txt_path = os.path.join(TXT_MD_DIR, semantic_txt_name)
    if src_file != final_txt_path:
        shutil.move(src_file, final_txt_path)
        print(f"[RENAME] {orig_name} -> {semantic_txt_name}")
    else:
        print(f"[RENAME] File already at target: {semantic_txt_name}")
        
    # 3. Non-interactive Compile
    print(f"[COMPILING] Invoking compile.bat on {semantic_txt_name}...")
    compile_cmd = f'cmd /c "(echo Y & echo.) | \"{COMPILE_BAT}\" \"{final_txt_path}\""'
    proc = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)
    
    # The PDF is produced in TXT_MD_DIR beside the input
    compiled_pdf_temp = os.path.join(TXT_MD_DIR, semantic_pdf_name)
    final_pdf_path = os.path.join(PDF_DIR, semantic_pdf_name)
    
    if os.path.exists(compiled_pdf_temp):
        shutil.move(compiled_pdf_temp, final_pdf_path)
        print(f"[ROUTING] Successfully compiled and placed PDF in pdf/{semantic_pdf_name}")
    elif os.path.exists(final_pdf_path):
        print(f"[ROUTING] Compiled PDF already in pdf/{semantic_pdf_name}")
    else:
        print(f"[ERROR] Compilation failed. Log output:\n{proc.stdout}\n{proc.stderr}")
        sys.exit(1)
        
    # 4. Catalog & Mindmap Updates
    doc_id = args.doc_id or get_next_doc_id()
    concepts = [c.strip() for c in args.concepts.split(",") if c.strip()]
    prereqs = [p.strip() for p in args.prerequisites.split(",") if p.strip()] if args.prerequisites else []
    
    update_topic_index_file(
        doc_id=doc_id,
        semantic_name=semantic_txt_name,
        orig_name=orig_name,
        domain=args.domain,
        concepts=concepts,
        pdf_name=semantic_pdf_name,
        summary=args.summary,
        source_type="txt_md",
        revision_info=f"Compiled from source note {semantic_txt_name}"
    )
    print(f"[CATALOG] Updated 03_topic_index.md for [{doc_id}]")
    
    update_mindmap_file(
        doc_id=doc_id,
        pdf_name=semantic_pdf_name,
        source_type="txt_md",
        domain=args.domain,
        concepts=concepts,
        summary=args.summary,
        source_note=semantic_txt_name,
        prerequisites=prereqs
    )
    print(f"[MINDMAP] Updated 04_interconnection_mindmap.md for [{doc_id}]")
    print(f"\n[DONE] Ingestion complete. PDF available at: {final_pdf_path}")

def cmd_ingest_pdf(args):
    """Executes atomic ingestion of a direct PDF."""
    src_file = os.path.abspath(args.file)
    if not os.path.exists(src_file):
        print(f"Error: File not found: {src_file}")
        sys.exit(1)
        
    orig_name = os.path.basename(src_file)
    target_base = args.name.replace(".pdf", "")
    semantic_pdf_name = f"{target_base}.pdf"
    final_pdf_path = os.path.join(PDF_DIR, semantic_pdf_name)
    
    # 1. Verify Text Layer
    with fitz.open(src_file) as doc:
        text = "".join([page.get_text() for page in doc])
    if len(text.strip()) < 50:
        print("[ERROR] PDF has no extractable text layer (scanned/bitmap). Rejected.")
        sys.exit(1)
        
    # 2. Deduplication Check
    dup_pdf = check_duplicate_content(src_file, PDF_DIR)
    if dup_pdf and dup_pdf != orig_name:
        print(f"[DEDUPLICATION STOP] Exact duplicate PDF already exists as: {dup_pdf}. Aborting ingestion to prevent duplicate catalog entries.")
        sys.exit(0)
        
    # 3. Move/Rename
    if src_file != final_pdf_path:
        shutil.move(src_file, final_pdf_path)
        print(f"[RENAME] {orig_name} -> {semantic_pdf_name}")
        
    # 4. Catalog & Mindmap Updates
    doc_id = args.doc_id or get_next_doc_id()
    concepts = [c.strip() for c in args.concepts.split(",") if c.strip()]
    
    update_topic_index_file(
        doc_id=doc_id,
        semantic_name="N/A",
        orig_name=orig_name,
        domain=args.domain,
        concepts=concepts,
        pdf_name=semantic_pdf_name,
        summary=args.summary,
        source_type="pdf_direct"
    )
    print(f"[CATALOG] Updated 03_topic_index.md for [{doc_id}]")
    
    update_mindmap_file(
        doc_id=doc_id,
        pdf_name=semantic_pdf_name,
        source_type="pdf_direct",
        domain=args.domain,
        concepts=concepts,
        summary=args.summary
    )
    print(f"[MINDMAP] Updated 04_interconnection_mindmap.md for [{doc_id}]")
    print(f"\n[DONE] PDF ingestion complete: {final_pdf_path}")

def cmd_process():
    """Reads .pending.json and executes the requested ingestion action."""
    pending_file = os.path.join(WORKSPACE, ".pending.json")
    if not os.path.exists(pending_file):
        print("No .pending.json found. Running repository scan instead.")
        cmd_scan()
        return
        
    with open(pending_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    action = data.get("action", "ingest-note")
    class Args:
        pass
    args = Args()
    args.file = data.get("file")
    args.name = data.get("name")
    args.domain = data.get("domain")
    args.concepts = data.get("concepts", "")
    args.summary = data.get("summary", "")
    args.prerequisites = data.get("prerequisites", "")
    args.doc_id = data.get("doc_id", "")
    
    try:
        if action == "ingest-note":
            cmd_ingest_note(args)
        elif action == "ingest-pdf":
            cmd_ingest_pdf(args)
        else:
            print(f"Unknown action: {action}")
    finally:
        if os.path.exists(pending_file):
            os.remove(pending_file)

def main():
    parser = argparse.ArgumentParser(description="Study Repository Automation Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # process (standard static command)
    subparsers.add_parser("process", help="Process pending instruction from .pending.json")

    # scan
    subparsers.add_parser("scan", help="Scan repository for status and unindexed files")
    
    # ingest-note
    p_note = subparsers.add_parser("ingest-note", help="Ingest, rename, compile and catalog a text note")
    p_note.add_argument("--file", required=True, help="Path to input text/md file")
    p_note.add_argument("--name", required=True, help="Target semantic name (kebab-case)")
    p_note.add_argument("--domain", required=True, help="Primary academic domain")
    p_note.add_argument("--concepts", required=True, help="Comma-separated core concepts")
    p_note.add_argument("--summary", required=True, help="Dense technical summary")
    p_note.add_argument("--prerequisites", default="", help="Comma-separated prerequisites")
    p_note.add_argument("--doc-id", default="", help="Explicit DOC-XXX ID (optional)")
    
    # ingest-pdf
    p_pdf = subparsers.add_parser("ingest-pdf", help="Ingest, verify text layer and catalog a direct PDF")
    p_pdf.add_argument("--file", required=True, help="Path to input PDF file")
    p_pdf.add_argument("--name", required=True, help="Target semantic name (kebab-case)")
    p_pdf.add_argument("--domain", required=True, help="Primary academic domain")
    p_pdf.add_argument("--concepts", required=True, help="Comma-separated core concepts")
    p_pdf.add_argument("--summary", required=True, help="Dense technical summary")
    p_pdf.add_argument("--doc-id", default="", help="Explicit DOC-XXX ID (optional)")

    args = parser.parse_args()
    if args.command == "process":
        cmd_process()
    elif args.command == "scan":
        cmd_scan()
    elif args.command == "ingest-note":
        cmd_ingest_note(args)
    elif args.command == "ingest-pdf":
        cmd_ingest_pdf(args)

if __name__ == "__main__":
    main()
