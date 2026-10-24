from pathlib import Path
import json
from collections import defaultdict
D=((0,1),(1,0),(0,-1),(-1,0))
out={'status':'PASS','cases':0,'literal_steps':0,'largest_N':0}
for N in range(4,130,2):
 H={(x,y) for y in range(N-1) for x in range(1,y+2)}
 rho=defaultdict(int)
 for x,y in H:
  for dx,dy,v in [(0,0,1),(1,0,-1),(0,1,-1),(1,1,1)]:rho[x+dx,y+dy]+=v
 rho={q:v for q,v in rho.items() if v}
 assert all(v==(-1 if sum(q)%2==0 else 1) for q,v in rho.items())
 B=set(rho)
 explicit={(n+1,n) for n in range(N)}|{(n+2,n) for n in range(N-1)}|{(1,N-1)}
 assert B==explicit and len(B)==2*N
 rows=defaultdict(int);cols=defaultdict(int)
 for x,y in B:
  rows[y]+=(-1 if x%2 else 1);cols[x]+=(-1 if y%2 else 1)
 assert all(v==0 for v in list(rows.values())+list(cols.values()))
 p=(0,0);h=0
 for t in range(2*N):
  assert p==((t+1)//2,t//2) and (p in B)==(t%2==1)
  black=p in B;h=(h+(-1 if black else 1))%4
  if black:B.remove(p)
  else:B.add(p)
  p=(p[0]+D[h][0],p[1]+D[h][1])
 out['cases']+=1;out['literal_steps']+=2*N;out['largest_N']=N
root=Path(__file__).resolve().parent
(root/'check_optimal_staircase.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
