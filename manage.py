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

def classify_document(pdf_name, domain=""):
    """Classifies a document into a GATE 2027 PH section and syllabus topic."""
    name = pdf_name.lower()
    
    if "cauchy" in name or name.startswith("math-"):
        return ("SEC-02", "Mathematical Physics", "2.4: Complex Analysis, Cauchy-Riemann & Singularities")
    if "thermodynamics" in name or "statistical" in name or name.startswith("stat-"):
        return ("SEC-04", "Thermodynamics & Statistical Mechanics", "4.4: Classical and Quantum Statistics")
    if "zeeman" in name:
        return ("SEC-08", "Atomic & Molecular Physics", "8.4: External Field Effects (Zeeman, Paschen-Back, Stark)")
    if "electric-dipole" in name:
        return ("SEC-08", "Atomic & Molecular Physics", "8.5: Electric Dipole Transitions & Selection Rules")
    if name.startswith("nuc-") or "liquid-drop" in name or "shell-model" in name or "deuteron" in name:
        if "deuteron" in name or "nuclear-force" in name:
            return ("SEC-10", "Nuclear & Particle Physics", "10.4: Nuclear Force & Two-Nucleon Problem (Deuteron)")
        elif "shell-model" in name:
            return ("SEC-10", "Nuclear & Particle Physics", "10.3: Nuclear Shell Model & Magic Numbers")
        elif "liquid-drop" in name or "mass-formula" in name:
            return ("SEC-10", "Nuclear & Particle Physics", "10.2: Semi-Empirical Mass Formula & Liquid Drop Model")
        elif "radial-probability" in name:
            return ("SEC-07", "Quantum Mechanics", "7.6: Central Potentials & Hydrogen-like Atoms")
        else:
            return ("SEC-10", "Nuclear & Particle Physics", "10.1: Nuclear Properties & Models")
    if name.startswith("ssp-") or "brillouin" in name or "bravais" in name or "lattice" in name or "bloch" in name or "wigner-seitz" in name or "miller-indices" in name or "ewald" in name or "lau-condition" in name or "effective-mass" in name:
        if "wigner-seitz" in name or "bravais" in name or "lattice" in name or "miller-indices" in name:
            return ("SEC-09", "Solid State Physics", "9.1: Crystallography, Bravais Lattices, Miller Indices & Unit Cells")
        elif "ewald" in name or "lau" in name or "first-brillouin" in name or "reciprocal-lattice" in name or "g-hkl" in name:
            return ("SEC-09", "Solid State Physics", "9.2: Diffraction, Reciprocal Lattice, Ewald Sphere & Laue Condition")
        elif "einstein-temperature" in name or "oscillations" in name:
            return ("SEC-09", "Solid State Physics", "9.4: Lattice Vibrations, Phonons & Thermal Properties")
        elif "bloch" in name or "band" in name or "anisotropic-effective-mass" in name:
            return ("SEC-09", "Solid State Physics", "9.6: Band Theory of Solids, Bloch's Theorem & Effective Mass")
        elif "density-of-states" in name or "effective-mass" in name:
            return ("SEC-09", "Solid State Physics", "9.5: Free Electron Theory, Band Theory & Density of States")
        elif "dielectric" in name:
            return ("SEC-09", "Solid State Physics", "9.8: Dielectric Properties of Solids, Polarizability & Ferroelectricity")
        elif "potential-wells" in name:
            return ("SEC-07", "Quantum Mechanics", "7.3: One-Dimensional Potentials & Wells")
        elif "pauli" in name:
            return ("SEC-07", "Quantum Mechanics", "7.8: Identical Particles & Pauli Exclusion Principle")
        else:
            return ("SEC-09", "Solid State Physics", "9.1: Elements of Crystallography & Crystal Structures")
    if name.startswith("qm-") or "wavefunction" in name or "operator" in name or "perturbation" in name or "harmonic-oscillator" in name or "pauli" in name or "potential" in name or "commutator" in name:
        if "harmonic-oscillator" in name or "ladder-operators" in name or "truncated-half" in name or "2d-isotropic" in name or "3d-isotropic" in name:
            return ("SEC-07", "Quantum Mechanics", "7.5: Harmonic Oscillators (1D, 2D, 3D & Degeneracy)")
        elif "potential-well" in name or "potential" in name or "box" in name or "boundaries" in name or "attenuation" in name:
            return ("SEC-07", "Quantum Mechanics", "7.3: One-Dimensional Potentials (Step, Wells, Tunneling, Delta Functions)")
        elif "parity" in name or "operator" in name or "eigenvalue" in name or "eigenstate" in name or "hilbert" in name or "commutator" in name or "hermitian" in name or "phase" in name:
            return ("SEC-07", "Quantum Mechanics", "7.1: Foundations of QM, Uncertainty Principle & Hilbert Space Operators")
        elif "hydrogen" in name or "radial" in name or "bohr" in name:
            return ("SEC-07", "Quantum Mechanics", "7.6: Central Potentials & Hydrogen-like Atoms (Radial & Angular Wavefunctions)")
        elif "spin" in name or "pauli-spin" in name or "angular-momentum" in name:
            return ("SEC-07", "Quantum Mechanics", "7.7: Orbital and Spin Angular Momenta & Pauli Spin Matrices")
        elif "pauli-exclusion" in name or "identical" in name or "singlet" in name:
            return ("SEC-07", "Quantum Mechanics", "7.8: Identical Particles, Pauli Exclusion Principle & Fermions/Bosons")
        elif "perturbation" in name:
            return ("SEC-07", "Quantum Mechanics", "7.9: Approximation Methods (Variational Method & Perturbation Theory)")
        elif "time-evolved" in name or "wavefunction" in name:
            return ("SEC-07", "Quantum Mechanics", "7.2: Time-Independent & Time-Dependent Schrödinger Dynamics")
        else:
            return ("SEC-07", "Quantum Mechanics", "7.1: Foundations of Quantum Mechanics")
            
    return ("SEC-07", "Quantum Mechanics", "7.1: Foundations of Quantum Mechanics")

def update_topic_index_file(doc_id, semantic_name, orig_name, domain, concepts, pdf_name, summary, source_type="txt_md", revision_info=None, section=None, topic=None):
    """Safely updates or appends to 03_topic_index.md."""
    if not os.path.exists(TOPIC_INDEX_FILE):
        print(f"Error: {TOPIC_INDEX_FILE} not found.")
        return False
        
    with open(TOPIC_INDEX_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    sec_code, sec_title, unit = classify_document(pdf_name, domain)
    if section:
        sec_code = section
    if topic:
        unit = topic
    unit_code = unit.split(":")[0].strip()
    unit_short = unit.split(":")[1].strip() if ":" in unit else unit
    
    status_str = "Compiled from Source" if source_type == "txt_md" else "Indexed (Direct PDF Import)"
    if "surrogate" in source_type:
        status_str = "Provisional Source (Auto-extracted)"
    today = "2026-11-15"
    
    table_row = f"| {doc_id} | **{sec_code}** | `{unit_code}` {unit_short[:25]} | `{pdf_name}` | `{orig_name}` | [{pdf_name}](file:///D:/STUDY/pdf/{pdf_name}) | {status_str} | {today} |\n"
    source_file_entry = f"[{semantic_name}](file:///D:/STUDY/txt_md/{semantic_name})" if source_type == "txt_md" else f"`N/A - Direct PDF Import`"
    
    concepts_list_str = "\n".join([f"  - {c}" for c in concepts])
    log_entry = f"  - `{today}`: {revision_info}" if revision_info else f"  - `{today}`: Ingested, semantically renamed to `{semantic_name}`, and cataloged."
    
    detail_block = f"""
### [{doc_id}] {pdf_name}
- **Source File**: {source_file_entry}
- **Compiled PDF**: [{pdf_name}](file:///D:/STUDY/pdf/{pdf_name})
- **Original Filename**: `{orig_name}`
- **GATE Section**: `{sec_code}` ({sec_title})
- **Syllabus Topic**: `{unit}`
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
        new_lines = []
        for line in lines:
            if line.strip().startswith(f"| {doc_id} |"):
                new_lines.append(table_row)
            else:
                new_lines.append(line)
        full_content = "".join(new_lines)
        pattern = rf"### \[{doc_id}\][\s\S]*?(?=\n### \[|\n---|\Z)"
        full_content = re.sub(pattern, detail_block.strip() + "\n", full_content)
    else:
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

def update_mindmap_file(doc_id, pdf_name, source_type, domain, concepts, summary, source_note=None, prerequisites=None, section=None, topic=None):
    """Safely updates or appends node to 04_interconnection_mindmap.md."""
    if not os.path.exists(MINDMAP_FILE):
        return False
        
    with open(MINDMAP_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    sec_code, sec_title, unit = classify_document(pdf_name, domain)
    if section:
        sec_code = section
    if topic:
        unit = topic
        
    node_dict = {
        "id": doc_id,
        "file": pdf_name,
        "source_type": source_type,
        "domain": domain,
        "core_concepts": concepts,
        "summary": summary,
        "section": sec_code,
        "syllabus_topic": unit
    }
    if source_note:
        node_dict["source_note"] = source_note
    if prerequisites:
        node_dict["prerequisites"] = prerequisites
        
    yaml_node = yaml.dump([node_dict], sort_keys=False, indent=2)
    node_str = "  " + yaml_node.strip().replace("\n", "\n  ") + "\n"
    
    if f"id: {doc_id}" in content:
        pattern = rf"- id: {doc_id}[\s\S]*?(?=\n- id:|\nedges:)"
        content = re.sub(pattern, yaml.dump(node_dict, sort_keys=False).strip(), content)
    else:
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
    txt_files = [f for f in os.listdir(TXT_MD_DIR) if os.path.isfile(os.path.join(TXT_MD_DIR, f)) and f.endswith(('.txt', '.md'))]
    pdf_files = [f for f in os.listdir(PDF_DIR) if os.path.isfile(os.path.join(PDF_DIR, f)) and f.endswith('.pdf')]
    
    surrogate_count = 0
    authentic_count = 0
    for f in txt_files:
        fpath = os.path.join(TXT_MD_DIR, f)
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as sf:
                if "AUTO-GENERATED SURROGATE" in sf.read(500):
                    surrogate_count += 1
                else:
                    authentic_count += 1
        except Exception:
            authentic_count += 1

    print(f"Notes in txt_md/: {len(txt_files)} ({authentic_count} authentic source notes, {surrogate_count} provisional surrogates)")
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
    
    # 0. Provisional Surrogate Check (Strict Compilation Block)
    with open(src_file, "r", encoding="utf-8", errors="ignore") as sf:
        head = sf.read(500)
        if "DO NOT RECOMPILE" in head or "AUTO-GENERATED SURROGATE" in head:
            print(f"[COMPILATION BLOCKED] {orig_name} is an auto-generated provisional surrogate Markdown file. It cannot be compiled to PDF.")
            sys.exit(1)

    # 1. Deduplication Check
    dup_txt = check_duplicate_content(src_file, TXT_MD_DIR)
    if dup_txt and dup_txt != orig_name:
        dup_path = os.path.join(TXT_MD_DIR, dup_txt)
        with open(dup_path, "r", encoding="utf-8", errors="ignore") as df:
            if "AUTO-GENERATED SURROGATE" not in df.read(500):
                print(f"[DEDUPLICATION STOP] Exact duplicate note content already exists as: {dup_txt}. Aborting ingestion to prevent duplicate catalog entries.")
                sys.exit(0)
        
    # Clean up prior provisional surrogate if it exists
    prior_surrogate = os.path.join(TXT_MD_DIR, f"{target_base}.md")
    if os.path.exists(prior_surrogate) and prior_surrogate != src_file:
        try:
            with open(prior_surrogate, "r", encoding="utf-8", errors="ignore") as ps:
                if "AUTO-GENERATED SURROGATE" in ps.read(500):
                    os.remove(prior_surrogate)
                    print(f"[REPLACE] Removed provisional surrogate {target_base}.md to make way for authentic note.")
        except Exception:
            pass

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

def cmd_audit_duplicates():
    """Runs repository-wide exact and normalized-text duplicate detection."""
    from collections import defaultdict
    print("=== REPOSITORY DUPLICATE AUDIT ===")
    
    # Check PDFs
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    pdf_hashes = defaultdict(list)
    for f in pdf_files:
        pdf_hashes[get_file_hash(os.path.join(PDF_DIR, f))].append(f)
        
    pdf_dups = {h: files for h, files in pdf_hashes.items() if len(files) > 1}
    if pdf_dups:
        print(f" [!] Exact duplicate PDFs detected by MD5 hash:")
        for h, files in pdf_dups.items():
            print(f"     - Hash {h}: {files}")
    else:
        print(f" [OK] Zero exact duplicate PDFs across {len(pdf_files)} files.")
        
    # Check Notes
    txt_files = [f for f in os.listdir(TXT_MD_DIR) if f.endswith((".txt", ".md"))]
    txt_hashes = defaultdict(list)
    for f in txt_files:
        txt_hashes[get_file_hash(os.path.join(TXT_MD_DIR, f))].append(f)
        
    txt_dups = {h: files for h, files in txt_hashes.items() if len(files) > 1}
    if txt_dups:
        print(f" [!] Exact duplicate notes detected by MD5 hash:")
        for h, files in txt_dups.items():
            print(f"     - Hash {h}: {files}")
    else:
        print(f" [OK] Zero exact duplicate notes across {len(txt_files)} files.")
        
    # Normalized body text
    body_hashes = defaultdict(list)
    for f in txt_files:
        with open(os.path.join(TXT_MD_DIR, f), "r", encoding="utf-8", errors="ignore") as fp:
            text = fp.read()
        text = re.sub(r'<!--[\s\S]*?-->', '', text)
        norm = re.sub(r'\s+', ' ', text).strip()
        if len(norm) > 50:
            h = hashlib.md5(norm.encode('utf-8')).hexdigest()
            body_hashes[h].append(f)
            
    body_dups = {h: files for h, files in body_hashes.items() if len(files) > 1}
    if body_dups:
        print(f" [!] Identical normalized body text detected across notes:")
        for h, files in body_dups.items():
            print(f"     - {files}")
    else:
        print(f" [OK] Zero duplicate notes by normalized body text.")

def cmd_remove_doc(args):
    """Safely removes or consolidates a document from the catalog, mindmap, and filesystem."""
    doc_id = args.doc_id
    consolidate_into = getattr(args, "consolidate_into", "")
    print(f"=== REMOVING DOCUMENT [{doc_id}] ===")
    
    # 1. Parse 03_topic_index.md to find filenames
    with open(TOPIC_INDEX_FILE, "r", encoding="utf-8") as f:
        catalog_text = f.read()
        
    pdf_match = re.search(rf'\| {doc_id} \| `([^`]+)`', catalog_text)
    pdf_name = pdf_match.group(1) if pdf_match else None
    base_name = pdf_name.replace(".pdf", "") if pdf_name else None
    
    # 2. Remove files from filesystem
    if pdf_name:
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
            print(f" [FS] Removed {pdf_path}")
            
    if base_name:
        for ext in [".txt", ".md"]:
            txt_path = os.path.join(TXT_MD_DIR, f"{base_name}{ext}")
            if os.path.exists(txt_path):
                os.remove(txt_path)
                print(f" [FS] Removed {txt_path}")
                
    # 3. Update 03_topic_index.md
    lines = catalog_text.splitlines(keepends=True)
    new_lines = []
    skip_detail = False
    
    for line in lines:
        if line.strip().startswith(f"| {doc_id} |"):
            continue
        if line.strip().startswith(f"### [{doc_id}]"):
            skip_detail = True
            continue
        if skip_detail:
            if line.strip().startswith("### [") or line.strip() == "---":
                skip_detail = False
            else:
                continue
        new_lines.append(line)
        
    catalog_updated = "".join(new_lines)
    
    if consolidate_into:
        log_pattern = rf"(### \[{consolidate_into}\][\s\S]*?- \*\*Processing Log\*\*:\n)([\s\S]*?)(?=\n### \[|\n---|\Z)"
        m = re.search(log_pattern, catalog_updated)
        if m:
            logs = m.group(2)
            new_log = f"  - `2026-11-15`: Consolidated duplicate entry {doc_id} ({pdf_name}) into {consolidate_into}.\n"
            catalog_updated = catalog_updated[:m.start(2)] + logs + new_log + catalog_updated[m.end(2):]
            print(f" [CATALOG] Added consolidation log to [{consolidate_into}]")
            
    with open(TOPIC_INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(catalog_updated)
    print(f" [CATALOG] Removed [{doc_id}] from 03_topic_index.md")
    
    # 4. Update 04_interconnection_mindmap.md
    with open(MINDMAP_FILE, "r", encoding="utf-8") as f:
        mindmap_text = f.read()
        
    yaml_match = re.search(r"```yaml\n(.*?)\n```", mindmap_text, re.DOTALL)
    if yaml_match:
        data = yaml.safe_load(yaml_match.group(1))
        data["nodes"] = [n for n in data.get("nodes", []) if n.get("id") != doc_id]
        new_edges = []
        for e in data.get("edges", []):
            if e.get("from") == doc_id or e.get("to") == doc_id:
                if consolidate_into:
                    new_from = consolidate_into if e.get("from") == doc_id else e.get("from")
                    new_to = consolidate_into if e.get("to") == doc_id else e.get("to")
                    if new_from != new_to:
                        e["from"] = new_from
                        e["to"] = new_to
                        new_edges.append(e)
            else:
                new_edges.append(e)
        data["edges"] = new_edges
        data["total_nodes"] = len(data["nodes"])
        data["total_edges"] = len(data["edges"])
        
        new_yaml = yaml.dump(data, sort_keys=False, indent=2, width=1000)
        mindmap_updated = mindmap_text[:yaml_match.start(1)] + new_yaml + mindmap_text[yaml_match.end(1):]
        with open(MINDMAP_FILE, "w", encoding="utf-8") as f:
            f.write(mindmap_updated)
        print(f" [MINDMAP] Removed [{doc_id}] from 04_interconnection_mindmap.md (new total_nodes: {len(data['nodes'])})")
    
    print(f"[DONE] Successfully removed {doc_id} and consolidated into {consolidate_into or 'None'}.")

def cmd_coverage():
    """Calculates and prints the real-time GATE 2027 PH Physics syllabus coverage metrics."""
    taxonomy_file = os.path.join(INDEX_DIR, "00_syllabus_taxonomy.md")
    if not os.path.exists(taxonomy_file):
        print("Error: 00_syllabus_taxonomy.md not found.")
        return
        
    with open(taxonomy_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("==========================================================================")
    print("      GATE 2027 PH PHYSICS: SYLLABUS PREPARATION & COVERAGE AUDIT        ")
    print("==========================================================================")
    
    matrix_match = re.search(r"## 📊 Real-Time Syllabus Coverage Matrix\n\n(.*?)\n---", content, re.DOTALL)
    if matrix_match:
        table_text = matrix_match.group(1).strip()
        lines = table_text.splitlines()
        for l in lines:
            if l.startswith("| **SEC-") or l.startswith("| **TOTAL"):
                parts = [p.strip() for p in l.split("|")[1:-1]]
                sec = parts[0].replace("*", "")
                title = parts[1][:30]
                notes = parts[2].replace("*", "")
                status = parts[5]
                print(f" {sec:7} | {title:30} | {notes:10} | {status}")
    print("==========================================================================")
    print(" Detailed section breakdown available at: index/00_syllabus_taxonomy.md")
    print("==========================================================================")

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
    args.consolidate_into = data.get("consolidate_into", "")
    
    try:
        if action == "ingest-note":
            cmd_ingest_note(args)
        elif action == "ingest-pdf":
            cmd_ingest_pdf(args)
        elif action == "remove-doc":
            cmd_remove_doc(args)
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
    subparsers.add_parser("coverage", help="Display GATE 2027 Physics syllabus coverage metrics")
    
    # audit-duplicates
    subparsers.add_parser("audit-duplicates", help="Audit repository for exact and normalized duplicate notes/PDFs")
    
    # remove-doc
    p_rem = subparsers.add_parser("remove-doc", help="Consolidate/remove a duplicate document entry")
    p_rem.add_argument("--doc-id", required=True, help="DOC-XXX to remove")
    p_rem.add_argument("--consolidate-into", default="", help="DOC-XXX to consolidate into (optional)")
    
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
    elif args.command == "coverage":
        cmd_coverage()
    elif args.command == "audit-duplicates":
        cmd_audit_duplicates()
    elif args.command == "remove-doc":
        cmd_remove_doc(args)
    elif args.command == "ingest-note":
        cmd_ingest_note(args)
    elif args.command == "ingest-pdf":
        cmd_ingest_pdf(args)

if __name__ == "__main__":
    main()
