#!/usr/bin/env python3
"""
bridge_sync.py - 同步 bridge 資料夾到 GitHub
讓 Hermes（任何環境）都能讀取通訊文件
"""
import subprocess
import sys
import json
from datetime import datetime

BRIDGE_DIR = r"C:\Users\user\.qclaw\workspace\bridge"
COMMIT_MSG = f"Bridge update - {datetime.now().strftime('%Y-%m-%d %H:%M BKK')}"

def run(cmd, cwd=None):
    result = subprocess.run(
        cmd, cwd=cwd or BRIDGE_DIR,
        capture_output=True, text=True,
        encoding='utf-8', errors='replace'
    )
    return result.returncode, result.stdout, result.stderr

def sync():
    # Git add
    code, out, err = run(['git', 'add', '.'], cwd=BRIDGE_DIR)
    if code != 0:
        print(f"git add failed: {err}")
        return False
    
    # Check if anything changed
    code, out, err = run(['git', 'status', '--porcelain'], cwd=BRIDGE_DIR)
    if not out.strip():
        print("No changes to sync")
        return True
    
    # Commit and push
    code, out, err = run(['git', 'commit', '-m', COMMIT_MSG], cwd=BRIDGE_DIR)
    if code != 0:
        print(f"git commit failed: {err}")
        return False
    
    code, out, err = run(['git', 'push'], cwd=BRIDGE_DIR)
    if code != 0:
        print(f"git push failed: {err}")
        return False
    
    print(f"Synced: {out}")
    return True

if __name__ == '__main__':
    success = sync()
    sys.exit(0 if success else 1)
