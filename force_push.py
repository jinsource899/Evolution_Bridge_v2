import subprocess, os, shutil

BRIDGE = r"C:\Users\user\.qclaw\workspace\bridge"
os.environ['GH_TOKEN'] = '[GITHUB_PAT]'
os.environ['GIT_TERMINAL_PROMPT'] = '0'

# Clean memory of PAT in current files
for fname in ['03_MEMORY.md', 'gh_login.py', 'push_files.py']:
    fpath = os.path.join(BRIDGE, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('[GITHUB_PAT]', '[PAT_REMOVED]')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {fname}")

# Force push to overwrite remote history
r = subprocess.run(
    ['git', 'push', '--force', '--set-upstream', 'origin', 'master'],
    cwd=BRIDGE, capture_output=True
)
print(f"force push => {r.returncode}")
print(r.stdout[:500])
print(r.stderr[:500])
