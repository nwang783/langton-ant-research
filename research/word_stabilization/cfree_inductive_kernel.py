"""Descending exact-target abstraction kernel. Only a nonempty stable closure proves anything."""
from pathlib import Path
import subprocess,sys,json,os
ROOT=Path(__file__).parent
initial=json.load(open(ROOT/'cfree_first_reuse_targets.json'))
S={a:[z['site']for z in initial if z['macro']==a and 'EXCLUDED'in z['output']]for a in'UVQB'}
print('INITIAL',S,flush=True);rounds=[]
for i in range(1,42):
 sf=ROOT/'cfree_kernel_current_marks.json';sf.write_text(json.dumps(S));T={a:[]for a in S};results=[]
 for a in S:
  for p in S[a]:
   cmd=[sys.executable,str(ROOT/'cfree_first_reuse_patch.py'),a,'2','1000000',*map(str,p)]
   z=subprocess.run(cmd,text=True,capture_output=True,env={**os.environ,'CFREE_MARKS':str(sf)})
   ok=z.returncode==0 and 'EXCLUDED'in z.stdout
   if ok:T[a].append(p)
   results.append({'macro':a,'site':p,'excluded':ok,'stdout':z.stdout,'stderr':z.stderr})
   print('TARGET',i,a,p,'PASS'if ok else z.stdout.strip().splitlines()[-1],flush=True)
 rounds.append({'assumed':S,'surviving':T,'results':results});(ROOT/'cfree_kernel_rounds.json').write_text(json.dumps(rounds,indent=2))
 print('ROUND',i,'SIZE',sum(map(len,S.values())),'TO',sum(map(len,T.values())),flush=True)
 if T==S:print('STABLE',T,flush=True);break
 S=T
