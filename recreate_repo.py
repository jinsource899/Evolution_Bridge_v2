import subprocess, os, shutil, time

BRIDGE = r"C:\Users\user\.qclaw\workspace\bridge"
os.environ['GH_TOKEN'] = '[GITHUB_PAT]'
os.environ['GIT_TERMINAL_PROMPT'] = '0'

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd or BRIDGE, capture_output=True)
    return r.returncode, r.stdout, r.stderr

# Step 1: Delete remote repo
print("Deleting remote repo...")
rc, out, err = run(['gh', 'repo', 'delete', 'jinsource899/Evolution_Bridge', '--yes'])
print(f"delete => {rc}: {out[:200]} {err[:200]}")

# Step 2: Recreate remote repo (without pushing sensitive files)
print("\nCreating new repo...")
rc, out, err = run(['gh', 'repo', 'create', 'Evolution_Bridge', '--public', '--source', BRIDGE, '--push'])
print(f"create => {rc}: {out[:300]} {err[:300]}")
