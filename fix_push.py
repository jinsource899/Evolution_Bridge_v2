import subprocess, os

BRIDGE = r"C:\Users\user\.qclaw\workspace\bridge"

# 1. Reset to before the bad commit
r = subprocess.run(['git', 'reset', '--soft', 'HEAD~1'], cwd=BRIDGE, capture_output=True)
print(f"reset => {r.returncode} {r.stderr[:100]}")

# 2. Update files to remove PAT
os.environ['GH_TOKEN'] = 'REMOVED_FAKE_TOKEN_FOR_CLEANUP'

# Rewrite 03_MEMORY.md to remove PAT
with open(os.path.join(BRIDGE, '03_MEMORY.md'), 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('[GITHUB_PAT]', '[PAT_REMOVED]')
with open(os.path.join(BRIDGE, '03_MEMORY.md'), 'w', encoding='utf-8') as f:
    f.write(content)
print("03_MEMORY.md cleaned")

# Rewrite gh_login.py to not have PAT inline
with open(os.path.join(BRIDGE, 'gh_login.py'), 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('GH_PAT = \'[GITHUB_PAT]\'', 'GH_PAT = os.environ.get("GH_TOKEN", "")')
with open(os.path.join(BRIDGE, 'gh_login.py'), 'w', encoding='utf-8') as f:
    f.write(content)
print("gh_login.py cleaned")

# Rewrite push_files.py to not have PAT inline
with open(os.path.join(BRIDGE, 'push_files.py'), 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('\'[GITHUB_PAT]\'', '\'YOUR_GH_PAT_HERE\'')
with open(os.path.join(BRIDGE, 'push_files.py'), 'w', encoding='utf-8') as f:
    f.write(content)
print("push_files.py cleaned")

# 3. Commit with clean files
msg = "小青上傳四個核心文件（無敏感資訊）"
r = subprocess.run(['git', 'add', '.'], cwd=BRIDGE, capture_output=True)
r = subprocess.run(['git', 'commit', '-m', msg], cwd=BRIDGE, capture_output=True)
print(f"commit => {r.returncode} {r.stderr[:200]}")

# 4. Push
r = subprocess.run(['git', 'push'], cwd=BRIDGE, capture_output=True)
print(f"push => {r.returncode}")
print(r.stdout[:200])
print(r.stderr[:200])
