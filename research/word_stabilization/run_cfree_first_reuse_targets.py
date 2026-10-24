from pathlib import Path
import subprocess,sys,json,time
from verify_macro_word import D
ROOT=Path(__file__).parent;seam={(0,0),(-1,-1),(0,-1),(1,0)};results=[]
for a in'VUQB':
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 for p,c in first.items():
  if c!='L'or p in seam:continue
  cmd=[sys.executable,str(ROOT/'cfree_first_reuse_patch.py'),a,'2','1000000',*map(str,p)]
  r=subprocess.run(cmd,text=True,capture_output=True)
  row={'macro':a,'site':p,'returncode':r.returncode,'output':r.stdout,'stderr':r.stderr};results.append(row)
  print(a,p,r.stdout.strip().replace('\n',' | '),r.stderr.strip(),flush=True)
  (ROOT/'cfree_first_reuse_targets.json').write_text(json.dumps(results,indent=2))
