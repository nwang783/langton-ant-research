"""Finite algebra controls, not a periodic-front classification."""
import importlib.util,sys,json,itertools
from collections import defaultdict,Counter
from pathlib import Path
path=Path(__file__).parent.parent/'sources/kehao95-core/wake_synthesis/verification/general_wake_parity/screen.py'
spec=importlib.util.spec_from_file_location('incoming_screen',path);screen=importlib.util.module_from_spec(spec);sys.modules[spec.name]=screen;spec.loader.exec_module(screen)
DIR=((0,1),(1,0),(0,-1),(-1,0))
def check(w):
 P=len(w);p=(0,0);h=0;reads=[]
 for a in w:
  reads.append(p);h=(h+(1 if a=='R' else -1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 if h or not p[0] or not p[1]:return None
 d=p
 if d[0]<0:d=(-d[0],-d[1]);reads=[(-x,-y)for x,y in reads]
 groups=defaultdict(list)
 for i,q in enumerate(reads):
  v=screen.canonical(q,d);k=(q[0]-v[0])//d[0];groups[v].append((i-P*k,w[i]))
 beta={};O=set()
 for v,g in groups.items():
  g.sort()
  if any(a[1]==b[1]for a,b in zip(g,g[1:])):return None
  beta[v]=g[0][1]=='L'
  if len(g)%2:O.add(v)
 runs=screen.runs_for(O,d);assert runs is not None
 positive=Counter()
 for r in runs:
  if r.positive:
   for u,v,_ in r.edges():positive[u]+=1;positive[v]+=1
 correction=sum(positive[v]for v,b in beta.items()if b)%2
 q=screen.compressed_signature(O,d)
 assert q==(1+d[0]+correction)%2,(w,d,beta,O,q,correction)
 omega=sum(y//abs(d[1])for x,y in O)%2;assert omega==1
 return {'word':w,'drift':d,'input_black_classes':sum(beta.values()),'odd_classes':len(O),'q':q,'correction':correction}
rows=[];examples=[]
for P in range(2,17,2):
 count=nonwhite=correction=0
 for z in itertools.product('RL',repeat=P):
  row=check(''.join(z))
  if row:
   count+=1;nonwhite+=row['input_black_classes']>0;correction+=row['correction']
   if row['correction']and len(examples)<8:examples.append(row)
 rows.append({'period':P,'legal_periodic_input_words':count,'nonwhite_input':nonwhite,'nonzero_correction':correction})
 print(rows[-1],flush=True)
for w in ['LLLLRLRRRR','RLRL']:
 row=check(w);assert row;examples.append(row)
out={'scope':'all raw binary words of even length<=16, stable class alternation, non-axis drift; arbitrary incoming periodic colors','counts':rows,'examples':examples}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
