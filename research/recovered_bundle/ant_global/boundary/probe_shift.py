import random,json
from collections import Counter
from pathlib import Path
rng=random.Random(7744)
dirs=((1,0),(0,-1),(-1,0),(0,1));best=None
for trial in range(50000):
 seed={(r,s-r) for r in range(-8,9) for s in range(-2,-9,-1) if rng.random()<.25}
 b=set(seed);x,y,d=0,-4,2;N=Counter();Q=KC=EB=0;ev=[]
 for t in range(2000):
  s=x+y
  if s>0:break
  c=int((x,y) in b);out=(d+1-2*c)%4
  if s>=-3:
   N[s]+=1
   if s==-1 and c:Q+=1
   if s==-2 and not c and d==2 and out==3:EB+=1
   if s==-3 and c and d==1 and out==0:KC+=1
  ev.append((x,y,d,c,out))
  if c:b.remove((x,y))
  else:b.add((x,y))
  dx,dy=dirs[out];x+=dx;y+=dy;d=out
  if s==-3 and x+y==-4:
   M=N[0];D=EB-M;Z=KC+2*D-Q;S=N[-1]-N[-3]-8*D-4*Z
   if best is None or S>best['S']:
    best=dict(S=S,seed=sorted(seed),steps=t+1,N=dict(N),Q=Q,KC=KC,EB=EB,D=D,Z=Z,events=ev.copy())
   if S>0:
    Path('ant_global/boundary/shift_counterexample.json').write_text(json.dumps(best,indent=2));print('FAIL', {k:v for k,v in best.items() if k not in ('events','seed')});print(best['seed']);raise SystemExit
Path('ant_global/boundary/shift_probe.json').write_text(json.dumps(best,indent=2));print('BEST', {k:v for k,v in best.items() if k not in ('events','seed')})
