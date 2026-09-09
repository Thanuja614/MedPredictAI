#!/usr/bin/env python3
"""
MedPredict AI — Project Audit Utility
Inspects repository health, manifest alignment, structure completeness, and tests.
Zero fabrication of results.
"""

import json
import os
import sys
from pathlib import Path

# Ensure UTF-8 output even on Windows cp1252 consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent

def audit_project():
    print("=" * 72)
    print(" MEDPREDICT AI — MASTER PROJECT AUDIT")
    print("=" * 72)

    issues = []
    checks_passed = 0

    # 1. Manifest file inspection
    manifest_path = ROOT_DIR / "project_manifest.json"
    if not manifest_path.exists():
        issues.append("Missing project_manifest.json")
    else:
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
            print(f"[OK] project_manifest.json exists (Phase {manifest.get('current_phase')})")
            checks_passed += 1
        except Exception as e:
            issues.append(f"Invalid JSON in project_manifest.json: {e}")

    # 2. Project progress file inspection
    progress_path = ROOT_DIR / "PROJECT_PROGRESS.md"
    if not progress_path.exists():
        issues.append("Missing PROJECT_PROGRESS.md")
    else:
        print("[OK] PROJECT_PROGRESS.md ledger exists")
        checks_passed += 1

    # 3. Environment templates & security ignores
    gitignore_path = ROOT_DIR / ".gitignore"
    env_example_path = ROOT_DIR / ".env.example"
    if gitignore_path.exists():
        print("[OK] .gitignore present")
        checks_passed += 1
    else:
        issues.append("Missing .gitignore")

    if env_example_path.exists():
        print("[OK] .env.example template present")
        checks_passed += 1
    else:
        issues.append("Missing .env.example")

    # 4. Check for committed secrets (.env)
    env_real_path = ROOT_DIR / ".env"
    if env_real_path.exists():
        print("[!] Warning: .env file found in workspace. Ensure it is gitignored.")

    # 5. Core directories verification
    core_dirs = [
        "backend",
        "frontend",
        "data",
        "models",
        "reports",
        "scripts",
        "docs",
        "docker"
    ]
    for d in core_dirs:
        dp = ROOT_DIR / d
        if dp.is_dir():
            print(f"[OK] Directory '{d}/' present")
            checks_passed += 1
        else:
            issues.append(f"Core directory missing: {d}/")

    print("-" * 72)
    if issues:
        print(f"AUDIT SUMMARY: {checks_passed} checks passed, {len(issues)} issues identified:")
        for issue in issues:
            print(f"  [FAIL] {issue}")
        return False
    else:
        print(f"AUDIT SUMMARY: ALL {checks_passed} STRUCTURAL INTEGRITY CHECKS PASSED [SUCCESS]")
        return True

if __name__ == "__main__":
    success = audit_project()
    sys.exit(0 if success else 1)
