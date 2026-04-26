#!/usr/bin/env python3
import subprocess
import sys

BRIDGE_DIR = r"C:\Users\user\.qclaw\workspace\bridge"

def run(cmd, cwd=None):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return result.returncode, result.stdout, result.stderr

cmds = [
    ['git', 'init'],
    ['git', 'add', '.'],
    ['git', 'commit', '-m', 'Initial bridge - Evolution sync channel 2026-04-26'],
    ['git', 'branch', '-M', 'main'],
]

for cmd in cmds:
    code, out, err = run(cmd, cwd=BRIDGE_DIR)
    print(f"{' '.join(cmd)} -> {code}")
    if code != 0:
        print(f"  ERR: {err[:200]}")
        sys.exit(1)

print("Git init complete!")
