#!/usr/bin/env python3
"""
MedPredict AI — Lines of Code (LOC) Counter
Strictly counts genuine source code lines across modules.
Excludes node_modules, virtualenvs, build directories, and generated caches.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, Any, List

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "htmlcov",
    ".next",
    "storage",
    "artifacts"
}

EXTENSIONS_BY_CATEGORY = {
    "backend": {".py"},
    "frontend": {".ts", ".tsx", ".js", ".jsx", ".css", ".html"},
    "ml": {".py"},
    "tests": {".py", ".ts", ".tsx", ".js"},
    "scripts": {".py", ".sh", ".ps1"},
    "docs": {".md", ".rst"}
}

def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False

def count_file_lines(filepath: Path) -> Dict[str, int]:
    total_lines = 0
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                total_lines += 1
                stripped = line.strip()
                if not stripped:
                    blank_lines += 1
                elif stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
                    comment_lines += 1
                else:
                    code_lines += 1
    except Exception as e:
        return {"total": 0, "blank": 0, "comment": 0, "code": 0}

    return {"total": total_lines, "blank": blank_lines, "comment": comment_lines, "code": code_lines}

def categorize_path(rel_path: Path) -> str:
    parts = rel_path.parts
    if not parts:
        return "docs"
    
    first = parts[0].lower()
    if first == "backend":
        if len(parts) > 1 and parts[1].lower() == "tests":
            return "tests"
        if len(parts) > 2 and parts[2].lower() == "ml":
            return "ml"
        return "backend"
    elif first == "frontend":
        if "tests" in [p.lower() for p in parts]:
            return "tests"
        return "frontend"
    elif first == "scripts":
        return "scripts"
    elif first == "docs" or rel_path.suffix in {".md", ".rst"}:
        return "docs"
    elif first == "tests":
        return "tests"
    elif first == "data" and rel_path.suffix == ".json":
        return "backend"
    return "docs" if rel_path.suffix == ".md" else "scripts"

def run_loc_count() -> Dict[str, Any]:
    stats = {
        "backend": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
        "frontend": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
        "ml": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
        "tests": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
        "scripts": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
        "docs": {"files": 0, "total": 0, "blank": 0, "comment": 0, "code": 0},
    }

    all_allowed_exts = set().union(*EXTENSIONS_BY_CATEGORY.values())

    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            p = Path(root) / f
            if is_excluded(p):
                continue
            ext = p.suffix.lower()
            if ext not in all_allowed_exts and ext not in {".json", ".yaml", ".yml", ".toml", ".sql"}:
                continue

            rel = p.relative_to(ROOT_DIR)
            cat = categorize_path(rel)
            if cat not in stats:
                cat = "docs" if ext == ".md" else "backend"

            file_counts = count_file_lines(p)
            stats[cat]["files"] += 1
            stats[cat]["total"] += file_counts["total"]
            stats[cat]["blank"] += file_counts["blank"]
            stats[cat]["comment"] += file_counts["comment"]
            stats[cat]["code"] += file_counts["code"]

    grand_total_code = sum(s["code"] for s in stats.values())
    grand_total_all = sum(s["total"] for s in stats.values())
    grand_total_files = sum(s["files"] for s in stats.values())

    return {
        "breakdown": stats,
        "summary": {
            "total_files": grand_total_files,
            "total_code_lines": grand_total_code,
            "total_raw_lines": grand_total_all
        }
    }

def print_table(results: Dict[str, Any]):
    print("=" * 72)
    print(" MEDPREDICT AI -- GENUINE LINES OF CODE (LOC) AUDIT")
    print("=" * 72)
    print(f"{'Category':<15} | {'Files':>8} | {'Code Lines':>12} | {'Comments':>10} | {'Blank':>8}")
    print("-" * 72)
    for cat, s in results["breakdown"].items():
        print(f"{cat.capitalize():<15} | {s['files']:>8} | {s['code']:>12} | {s['comment']:>10} | {s['blank']:>8}")
    print("-" * 72)
    summary = results["summary"]
    print(f"{'TOTAL':<15} | {summary['total_files']:>8} | {summary['total_code_lines']:>12} | {'-':>10} | {'-':>8}")
    print("=" * 72)

if __name__ == "__main__":
    res = run_loc_count()
    if "--json" in sys.argv:
        print(json.dumps(res, indent=2))
    else:
        print_table(res)
