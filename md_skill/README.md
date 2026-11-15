# Reusable Agent Skills Blueprint (`md_skill/`)

This directory serves as the **master reusable skill vault** for the Study Knowledge Hub. It stores the authoritative source definitions for all AI behavioral and operational skills, allowing you to deploy them to any fresh workspace, clone, or global Antigravity installation with a single command.

---

## 📦 Master Skill Inventory

| Skill Name | Blueprint Source | Installed Location | Core Purpose |
|---|---|---|---|
| **`karpathy-guidelines`** | [`SKILL.md`](file:///D:/STUDY/md_skill/SKILL.md) | `.agent/skills/karpathy-guidelines/SKILL.md` | Behavioral guidelines reducing common LLM coding pitfalls, forcing surgical changes, eliminating speculative code, and establishing verifiable completion criteria. |
| **`repository-management`** | [`management_skill.md`](file:///D:/STUDY/md_skill/management_skill.md) | `.agent/skills/repository-management/SKILL.md` | Master operational management skill governing three-tier note ingestion lifecycles (authentic notes, direct PDFs, and surrogate Markdown), compilation locks, tool immutability, and search isolation. |

---

## 🚀 First-Time Installation Instructions

### Option 1: One-Click Automatic Installer (Recommended)

Simply run the batch installer from the workspace root or inside `md_skill/`:

```cmd
cmd /c "D:\STUDY\md_skill\install.bat"
```
*(Or in Windows File Explorer, simply double-click `install.bat`).*

---

### Option 2: PowerShell One-Liner

Run the following command in PowerShell from the repository root:

```powershell
New-Item -ItemType Directory -Force -Path ".agent\skills\karpathy-guidelines", ".agent\skills\repository-management"; `
Copy-Item -Path "md_skill\SKILL.md" -Destination ".agent\skills\karpathy-guidelines\SKILL.md" -Force; `
Copy-Item -Path "md_skill\management_skill.md" -Destination ".agent\skills\repository-management\SKILL.md" -Force; `
Copy-Item -Path "md_skill\management_skill.md" -Destination ".agent\management_skill.md" -Force
```

---

### Option 3: Standard Windows Command Prompt (CMD)

```cmd
mkdir ".agent\skills\karpathy-guidelines" 2>nul
mkdir ".agent\skills\repository-management" 2>nul
copy /Y "md_skill\SKILL.md" ".agent\skills\karpathy-guidelines\SKILL.md"
copy /Y "md_skill\management_skill.md" ".agent\skills\repository-management\SKILL.md"
copy /Y "md_skill\management_skill.md" ".agent\management_skill.md"
```

---

### Option 4: Global Installation Across All Workspaces

If you want these skills automatically active in **every** project on your machine without copying them to each repository:

```powershell
$GlobalSkills = "$env:USERPROFILE\.gemini\antigravity\skills"
New-Item -ItemType Directory -Force -Path "$GlobalSkills\karpathy-guidelines", "$GlobalSkills\repository-management"
Copy-Item -Path "md_skill\SKILL.md" -Destination "$GlobalSkills\karpathy-guidelines\SKILL.md" -Force
Copy-Item -Path "md_skill\management_skill.md" -Destination "$GlobalSkills\repository-management\SKILL.md" -Force
```

---

## 🔍 How to Verify Installation

After running any of the above installation methods:
1. Check the `.agent` folder structure:
   ```text
   .agent/
   ├── management_skill.md
   └── skills/
       ├── karpathy-guidelines/
       │   └── SKILL.md
       └── repository-management/
           └── SKILL.md
   ```
2. When launching an Antigravity agent in this workspace, the agent will automatically discover and load both skills upon startup.
