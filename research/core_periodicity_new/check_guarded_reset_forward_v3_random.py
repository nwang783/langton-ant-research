import random,subprocess,re,json,collections
from pathlib import Path
P=Path('/workspace/shared/langton/core_periodicity_new');C=P/'chronology_dcuv/forward_v3_controls';C.mkdir(exist_ok=True);gc_count=0;R=random.Random(193711);summary=[]
for trial in range(250):
 n=R.randint(1,8);np=R.randint(2,7);sp=R.randrange(np);sk=R.randrange(1<<n);sv=R.randrange(1<<n)&sk;T=[];out=[[]for _ in range(np)]
 for p in range(np-1):
  for a in range(R.randint(0,5)):
   k=R.randrange(1<<n);t=[p,R.randrange(np),k,R.randrange(1<<n)&k,R.randrange(1<<n),R.randrange(1<<n),R.randrange(1<<n),int(R.random()<.06),a];T.append(t);out[p].append(t)
 reentry=[p for p in range(np-1)if R.random()<.5]
 rows=[f'{n} {np} {len(T)} {len(reentry)}',f'{sp} {sk} {sv}']+[' '.join(map(str,t))for t in T]+[' '.join(map(str,reentry))]
 f=C/'control.dat';f.write_text('\n'.join(rows)+'\n');ret=subprocess.run([str(P/'guarded_reset_bdd_forward_v3'),str(f),'100000',str(C/'control.bdd'),'10','0'],capture_output=True,text=True,check=True);gc_count+=ret.stderr.count('midgc ');ret=ret.stdout
 seen={(sp,c)for c in range(1<<n)if(c&sk)==sv};front=set(seen);hit=False;depth=0
 while front and not hit:
  nex=set()
  for p,c in front:
   if p==np-1:nex|={(q,c)for q in reentry}
   else:
    for _,q,k,v,flip,clear,reset,goal,a in out[p]:
     if(c&k)!=v:continue
     if goal:hit=True;break
     nex.add((q,((c^flip)&~clear)|(reset&clear)))
   if hit:break
  nex-=seen;seen|=nex;front=nex;depth+=1
 expected='ABSTRACT_WITNESS'if hit else'EXHAUSTED_NO_HIT'
 assert expected in ret,(trial,expected,ret)
 assert int(re.search(r'depth (\d+)',ret)[1])==depth,(trial,depth,ret)
 if not hit:
  assert int(re.search(r'states (\d+)',ret)[1])==len(seen),(trial,len(seen),ret)
  subprocess.run(['python',str(P/'verify_protected_patch_bdd_labels.py'),str(f),str(C/'control.bdd')],check=True,capture_output=True,text=True)
 summary.append({'trial':trial,'n':n,'positions':np,'status':expected,'depth':depth,'explicit_states':len(seen)})
(C/'summary.json').write_text(json.dumps({'controls':summary,'forced_collections':gc_count},indent=2));print('passed',len(summary),'random guarded-XOR-reset graphs with partial initialization')
