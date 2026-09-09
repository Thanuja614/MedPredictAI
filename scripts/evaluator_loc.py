"""
Script to simulate the automated evaluator's production LOC calculation.
Counts non-empty, non-comment lines in .py, .ts, .tsx, .js, .jsx files,
strictly excluding tests, node_modules, .git, dist, build, coverage, and generated artifacts.
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {
    'node_modules', '.git', 'dist', 'build', 'coverage', '.pytest_cache',
    'tests', 'test', 'generated', 'venv', '.venv', 'storage'
}

PROD_EXTENSIONS = {'.py', '.ts', '.tsx', '.js', '.jsx'}

def count_prod_loc():
    total_loc = 0
    by_lang = {'Python': 0, 'TypeScript': 0, 'JavaScript': 0}
    file_count = 0

    for root, dirs, files in os.walk(ROOT):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d.lower() not in EXCLUDE_DIRS and not d.startswith('.')]
        
        # Also check if any parent path is in excluded
        rel_root = Path(root).relative_to(ROOT)
        parts = set(p.lower() for p in rel_root.parts)
        if parts.intersection(EXCLUDE_DIRS):
            continue

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in PROD_EXTENSIONS:
                continue

            # Exclude test files
            if 'test' in file.lower() or 'conftest' in file.lower():
                continue

            filepath = Path(root) / file
            file_loc = 0
            is_in_multiline = False

            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        stripped = line.strip()
                        if not stripped:
                            continue
                        
                        # Python comments
                        if ext == '.py':
                            if stripped.startswith('"""') or stripped.startswith("'''"):
                                if stripped.count('"""') == 2 or stripped.count("'''") == 2:
                                    continue
                                is_in_multiline = not is_in_multiline
                                continue
                            if is_in_multiline:
                                if '"""' in stripped or "'''" in stripped:
                                    is_in_multiline = False
                                continue
                            if stripped.startswith('#'):
                                continue
                        else:
                            # JS/TS comments
                            if stripped.startswith('/*'):
                                if '*/' in stripped:
                                    continue
                                is_in_multiline = not is_in_multiline
                                continue
                            if is_in_multiline:
                                if '*/' in stripped:
                                    is_in_multiline = False
                                continue
                            if stripped.startswith('//'):
                                continue

                        file_loc += 1
            except Exception as e:
                pass

            if file_loc > 0:
                file_count += 1
                total_loc += file_loc
                if ext == '.py':
                    by_lang['Python'] += file_loc
                elif ext in ('.ts', '.tsx'):
                    by_lang['TypeScript'] += file_loc
                elif ext in ('.js', '.jsx'):
                    by_lang['JavaScript'] += file_loc

    print(f"Total Prod LOC: {total_loc} across {file_count} files.")
    for lang, count in by_lang.items():
        print(f"  {lang}: {count}")
    return total_loc

if __name__ == '__main__':
    count_prod_loc()
