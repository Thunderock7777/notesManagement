@echo off
setlocal enabledelayedexpansion

echo =========================================================================
echo INSTALLING ANTIGRAVITY AGENT SKILLS FROM md_skill/
echo =========================================================================

set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%.."
set "SKILLS_DIR=%ROOT_DIR%\.agent\skills"

echo Workspace Root: %ROOT_DIR%
echo Target Skills Directory: %SKILLS_DIR%

:: 1. Ensure target skill directories exist
if not exist "%SKILLS_DIR%\karpathy-guidelines" (
    mkdir "%SKILLS_DIR%\karpathy-guidelines"
)
if not exist "%SKILLS_DIR%\repository-management" (
    mkdir "%SKILLS_DIR%\repository-management"
)

:: 2. Deploy Karpathy Guidelines Skill
if exist "%SCRIPT_DIR%SKILL.md" (
    copy /Y "%SCRIPT_DIR%SKILL.md" "%SKILLS_DIR%\karpathy-guidelines\SKILL.md" >nul
    echo  [OK] Installed: .agent\skills\karpathy-guidelines\SKILL.md
) else (
    echo  [ERROR] Source SKILL.md not found in md_skill\
)

:: 3. Deploy Repository Management Skill
if exist "%SCRIPT_DIR%management_skill.md" (
    copy /Y "%SCRIPT_DIR%management_skill.md" "%SKILLS_DIR%\repository-management\SKILL.md" >nul
    copy /Y "%SCRIPT_DIR%management_skill.md" "%ROOT_DIR%\.agent\management_skill.md" >nul
    echo  [OK] Installed: .agent\skills\repository-management\SKILL.md
    echo  [OK] Installed: .agent\management_skill.md
) else (
    echo  [ERROR] Source management_skill.md not found in md_skill\
)

echo =========================================================================
echo All skills successfully deployed and active.
echo =========================================================================
