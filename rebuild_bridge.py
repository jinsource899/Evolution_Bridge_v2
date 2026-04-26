import subprocess, os, shutil

BRIDGE = r"C:\Users\user\.qclaw\workspace\bridge"
PAT = '[GITHUB_PAT]'
os.environ['GH_TOKEN'] = PAT
os.environ['GIT_TERMINAL_PROMPT'] = '0'

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd or BRIDGE, capture_output=True)
    return r.returncode, r.stdout[:400], r.stderr[:400]

# Step 1: Clean ALL files of PAT
print("Cleaning PAT from all files...")
for fname in os.listdir(BRIDGE):
    fpath = os.path.join(BRIDGE, fname)
    if os.path.isfile(fpath):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if PAT in content:
                content = content.replace(PAT, '[GITHUB_PAT]')
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Cleaned: {fname}")
        except Exception as e:
            print(f"  Skip {fname}: {e}")

# Step 2: Delete .git to start fresh
print("\nRemoving old git history...")
shutil.rmtree(os.path.join(BRIDGE, '.git'), ignore_errors=True)

# Step 3: Init new git
print("Init new git...")
rc, out, err = run(['git', 'init'])
rc, out, err = run(['git', 'add', '.'])
rc, out, err = run(['git', 'commit', '-m', 'Evolution Bridge v2 — clean start'])
print(f"commit => {rc}")

# Step 4: Create new CLEAN repo (different name)
print("\nCreating new CLEAN repo 'Evolution_Bridge_v2'...")
rc, out, err = run(['gh', 'repo', 'create', 'Evolution_Bridge_v2', '--public'])
print(f"create => {rc}: {out[:300]}")
if err:
    print(f"  err: {err[:300]}")

# Step 5: Push to new repo
print("\nPushing to new repo...")
rc, out, err = run(['git', 'remote', 'add', 'origin', 'https://github.com/jinsource899/Evolution_Bridge_v2.git'])
rc, out, err = run(['git', 'push', '-u', 'origin', 'master'])
print(f"push => {rc}: {out[:300]}")
if err:
    print(f"  err: {err[:300]}")
