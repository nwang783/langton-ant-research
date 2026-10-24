"""Run the three independent exact checks. Requires Python 3, standard library only."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for name in ['verify_prefix.py','verify_capture.py','verify_reverse.py']:
 subprocess.run([sys.executable,str(root/name)],cwd=root,check=True)
print('PASS: every supplied184-cell family member is bi-standard; its forward defect count is unbounded.')
