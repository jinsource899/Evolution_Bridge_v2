import subprocess
# Set git identity
subprocess.run(['git', 'config', '--global', 'user.email', 'xos-evolution@spiritflow.ai'])
subprocess.run(['git', 'config', '--global', 'user.name', 'XOS-Evolution-Bridge'])
# Commit
BRIDGE_DIR = r"C:\Users\user\.qclaw\workspace\bridge"
code = subprocess.run(['git', 'commit', '-m', 'Initial bridge - Evolution sync channel 2026-04-26'], 
                      cwd=BRIDGE_DIR, capture_output=True, text=True).returncode
print(f"Commit: {code}")
# Set remote (need to create the repo on GitHub first)
# For now, just mark complete
print("Bridge folder ready for GitHub push")
print(f"Files in bridge/:")
import os
for f in os.listdir(BRIDGE_DIR):
    print(f"  {f}")
