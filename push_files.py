import subprocess, os

os.environ['GH_TOKEN'] = 'YOUR_GH_PAT_HERE'
os.environ['GIT_TERMINAL_PROMPT'] = '0'

BRIDGE = r"C:\Users\user\.qclaw\workspace\bridge"
cmds = [
    ['git', 'add', '.'],
    ['git', 'commit', '-m', '小青上傳四個核心文件：SOUL,xos_evolution,MEMORY,xp_search'],
    ['git', 'push'],
]
for cmd in cmds:
    r = subprocess.run(cmd, cwd=BRIDGE, capture_output=True, text=True)
    print(f"{' '.join(cmd)} => {r.returncode}")
    if r.stdout:
        print(r.stdout[:300])
    if r.stderr:
        print(r.stderr[:300])
