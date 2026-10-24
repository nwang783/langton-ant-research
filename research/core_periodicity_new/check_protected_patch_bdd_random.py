import random,subprocess,re,json,collections
from pathlib import Path
P=Path('/workspace/shared/langton/core_periodicity_new');R=random.Random(193711);summary=[]
for trial in range(150):
 n=R.randint(1,8);np=R.randint(2,7);sp=R.randrange(np);sk=R.randrange(1<<n);sv=R.randrange(1<<n)&sk;T=[];out=[[]for _ in range(np)]
 for p in range(np-1):
  for a in range(R.randint(0,5)):
   k=R.randrange(1<<n);t=[p,R.randrange(np),k,R.randrange(1<<n)&k,R.randrange(1<<n),int(R.random()<.06),a];T.append(t);out[p].append(t)
 reentry=[p for p in range(np-1)if R.random()<.5]
 rows=[f'{n} {np} {len(T)} {len(reentry)}',f'{sp} {sk} {sv}']+[' '.join(map(str,t))for t in T]+[' '.join(map(str,reentry))]
 f=P/'bdd_random_control.dat';f.write_text('\n'.join(rows)+'\n');ret=subprocess.run([str(P/'protected_patch_bdd'),str(f),'100000'],capture_output=True,text=True,check=True).stdout
 seen={(sp,c)for c in range(1<<n)if(c&sk)==sv};front=set(seen);hit=False;depth=0
 while front and not hit:
  nex=set()
  for p,c in front:
   if p==np-1:nex|={(q,c)for q in reentry}
   else:
    for _,q,k,v,flip,goal,a in out[p]:
     if(c&k)!=v:continue
     if goal:hit=True;break
     nex.add((q,c^flip))
   if hit:break
  nex-=seen;seen|=nex;front=nex;depth+=1
 expected='ABSTRACT_WITNESS'if hit else'EXHAUSTED_NO_HIT'
 assert expected in ret,(trial,expected,ret)
 assert int(re.search(r'depth (\d+)',ret)[1])==depth,(trial,depth,ret)
 if not hit:assert int(re.search(r'states (\d+)',ret)[1])==len(seen),(trial,len(seen),ret)
 summary.append({'trial':trial,'n':n,'positions':np,'status':expected,'depth':depth,'explicit_states':len(seen)})
(P/'protected_patch_bdd_random_controls.json').write_text(json.dumps(summary,indent=2));print('passed',len(summary),'random guarded-XOR graphs with partial initialization')
