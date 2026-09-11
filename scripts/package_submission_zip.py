"""
MedPredict AI — Compliant Archive Packaging Script
Creates the production submission ZIP archive containing:
  - Full Git history (.git directory included)
  - All source code, clinical modules, tests, docs, scripts, and example.env
  - Strictly EXCLUDES:
      - .env (ZERO sensitive files)
      - venv/, .venv/
      - node_modules/
      - dist/, build/
      - .pytest_cache/, __pycache__, *.pyc
      - storage/
      - existing *.zip, *.tar.gz archives
"""

import os
import zipfile
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Detect user desktop
desktop_candidate = Path.home() / "OneDrive" / "Desktop"
if not desktop_candidate.exists():
    desktop_candidate = Path.home() / "Desktop"

OUTPUT_ZIP = desktop_candidate / "MedPredictAI_v2.0.0.zip"
DOWNLOADS_ZIP = Path.home() / "Downloads" / "MedPredictAI_v2.0.0.zip"
LOCAL_ZIP = ROOT / "MedPredictAI_v2.0.0.zip"

EXCLUDED_DIR_NAMES = {
    'venv', '.venv', 'node_modules', 'dist', 'build',
    '.pytest_cache', '__pycache__', 'storage'
}

EXCLUDED_FILES = {
    '.env', '.ds_store', 'thumbs.db'
}

EXCLUDED_EXTENSIONS = {
    '.pyc', '.pyo', '.pyd', '.zip', '.tar.gz', '.tgz'
}

def should_exclude(rel_path: Path) -> bool:
    parts = [p.lower() for p in rel_path.parts]
    
    # Check if any component directory should be excluded
    for part in parts[:-1]:
        if part in EXCLUDED_DIR_NAMES:
            return True
            
    # Check file name and extension
    filename = rel_path.name.lower()
    if filename in EXCLUDED_FILES:
        return True
        
    for ext in EXCLUDED_EXTENSIONS:
        if filename.endswith(ext):
            return True
            
    return False

def create_archive():
    print(f"[*] Packaging MedPredict AI into: {OUTPUT_ZIP}")
    start_time = time.time()
    
    OUTPUT_ZIP.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT_ZIP.exists():
        print(f"[*] Removing existing archive {OUTPUT_ZIP}...")
        OUTPUT_ZIP.unlink()
        
    total_files = 0
    total_bytes = 0
    git_files_count = 0
    
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(ROOT):
            # Do not traverse into excluded directories
            dirs[:] = [d for d in dirs if d.lower() not in EXCLUDED_DIR_NAMES]
            
            for file in files:
                full_path = Path(root) / file
                rel_path = full_path.relative_to(ROOT)
                
                if should_exclude(rel_path):
                    continue
                    
                arcname = str(rel_path).replace("\\", "/")
                zf.write(full_path, arcname)
                total_files += 1
                total_bytes += full_path.stat().st_size
                
                if ".git/" in arcname or arcname.startswith(".git/"):
                    git_files_count += 1

    elapsed = time.time() - start_time
    zip_size_mb = OUTPUT_ZIP.stat().st_size / (1024 * 1024)
    raw_size_mb = total_bytes / (1024 * 1024)
    
    print("\n" + "="*60)
    print("ARCHIVE GENERATION COMPLETE")
    print("="*60)
    print(f"Primary Desktop Path:  {OUTPUT_ZIP}")
    print(f"Compressed Size:       {zip_size_mb:.2f} MB")
    print(f"Uncompressed Size:     {raw_size_mb:.2f} MB")
    print(f"Total Files Archived:  {total_files}")
    print(f"Git Objects Archived:  {git_files_count}")
    print(f"Time Taken:            {elapsed:.2f} seconds")
    print("="*60)

    # Replicate copy to Downloads and Workspace
    try:
        shutil.copy2(OUTPUT_ZIP, DOWNLOADS_ZIP)
        print(f"[*] Copy created at Downloads: {DOWNLOADS_ZIP}")
    except Exception as e:
        print(f"[!] Warning copying to Downloads: {e}")

    try:
        shutil.copy2(OUTPUT_ZIP, LOCAL_ZIP)
        print(f"[*] Copy created at Workspace: {LOCAL_ZIP}")
    except Exception as e:
        print(f"[!] Warning copying to Workspace: {e}")

def verify_archive():
    print("\n[*] Verifying archive compliance against evaluator criteria...")
    has_git = False
    has_env = False
    has_example_env = False
    prod_files = 0
    
    with zipfile.ZipFile(OUTPUT_ZIP, 'r') as zf:
        namelist = zf.namelist()
        for name in namelist:
            name_lower = name.lower()
            if name.startswith(".git/") or "/.git/" in name:
                has_git = True
            if name_lower == ".env" or name_lower.endswith("/.env"):
                has_env = True
                print(f"  [!] FORBIDDEN FILE FOUND: {name}")
            if "example.env" in name_lower:
                has_example_env = True
            if any(name_lower.endswith(ext) for ext in ('.py', '.ts', '.tsx', '.js', '.jsx')):
                if not any(ex in name_lower for ex in ('tests/', 'test/', 'node_modules/', '.git/')):
                    prod_files += 1

    print(f"  - Git directory included:     {'YES (PASS)' if has_git else 'NO (FAIL)'}")
    print(f"  - Sensitive .env excluded:    {'YES (PASS)' if not has_env else 'NO (FAIL)'}")
    print(f"  - example.env included:       {'YES (PASS)' if has_example_env else 'NO (FAIL)'}")
    print(f"  - Production source files:    {prod_files} files")

    assert has_git, "FAILED: .git directory not found in archive!"
    assert not has_env, "FAILED: .env file found in archive!"
    assert has_example_env, "FAILED: example.env not found in archive!"
    print("\n[SUCCESS] ALL EVALUATION CRITERIA VERIFIED AND PASSED!")

if __name__ == '__main__':
    create_archive()
    verify_archive()
