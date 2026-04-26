import subprocess
import os

# GitHub PAT from TOOLS.md
GH_PAT = os.environ.get('GH_TOKEN', '')
if not GH_PAT:
    print('[ERROR] GH_TOKEN not set')
    exit(1)
os.environ['GH_TOKEN'] = GH_PAT

# Auth with token
r = subprocess.run(['gh', 'auth', 'login', '--with-token'], 
                   input=GH_PAT, capture_output=True, text=True)
print(f"Auth: {r.returncode}")
print(r.stdout[:200])
print(r.stderr[:200])

# Create repo
BRIDGE_DIR = r"C:\Users\user\.qclaw\workspace\bridge"
r = subprocess.run(['gh', 'repo', 'create', 'Evolution_Bridge', '--public', 
                    '--source', BRIDGE_DIR, '--push'],
                   capture_output=True, text=True)
print(f"Create repo: {r.returncode}")
print(r.stdout[:300])
print(r.stderr[:300])
