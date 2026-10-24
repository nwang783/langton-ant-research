"""Research full-five simultaneous first-reuse kernel using backward 14-cell patches."""
from pathlib import Path
import subprocess,sys,json,os
from verify_macro_word import D
ROOT=Path(__file__).parent;seam={(0,0),(-1,-1),(0,-1),(1,0)}
S={}
for a in'UVQB':
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 S[a]=[p for p,c in first.items()if c=='L'and p not in seam]
rounds=[]
for i in range(1,42):
 sf=ROOT/'full_kernel_current_marks.json';sf.write_text(json.dumps(S));T={a:[]for a in S};results=[]
 for a in S:
  for p in S[a]:
   cmd=[sys.executable,str(ROOT/'backward_first_reuse_grammar_patch.py'),a,'2','1000000',*map(str,p)]
   z=subprocess.run(cmd,text=True,capture_output=True,env={**os.environ,'FRESH_MARKS':str(sf),'PATCH_MODE':'vshape'})
   ok=z.returncode==0 and 'EXCLUDED'in z.stdout
   if ok:T[a].append(p)
   results.append({'macro':a,'site':p,'excluded':ok,'stdout':z.stdout,'stderr':z.stderr})
   print('TARGET',i,a,p,'PASS '+z.stdout.strip().splitlines()[-1]if ok else z.stdout.strip().splitlines()[-1]if z.stdout else z.stderr,flush=True)
 rounds.append({'assumed':S,'surviving':T,'results':results});(ROOT/'full_kernel_rounds.json').write_text(json.dumps(rounds,indent=2))
 print('ROUND',i,'SIZE',sum(map(len,S.values())),'TO',sum(map(len,T.values())),flush=True)
 if T==S:print('STABLE',T,flush=True);break
 S=T
