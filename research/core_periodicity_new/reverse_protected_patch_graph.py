"""Reverse the entire finite guarded-XOR graph for exact backward reachability."""
from pathlib import Path
import sys,json
p=Path(sys.argv[1]);o=Path(sys.argv[2]);it=iter(map(int,p.read_text().split()));n,np,nt,nr=[next(it)for _ in range(4)];sp,sk,sv=[next(it)for _ in range(3)];T=[[next(it)for _ in range(7)]for _ in range(nt)];RE=[next(it)for _ in range(nr)];assert not list(it);G=[t for t in T if t[5]];assert len(G)==1;goal=G[0];R=[]
for f,t,k,v,x,g,a in T:
 if not g:R.append([t,f,k,v^(x&k),x,0,a])
for r in RE:R.append([r,np-1,0,0,0,0,99])
R.append([sp,sp,sk,sv,0,1,100])
# A new, unreachable dummy OUT position makes every original position ordinary.
with o.open('w')as f:
 f.write(f'{n} {np+1} {len(R)} 0\n');f.write(f'{goal[0]} {goal[2]} {goal[3]}\n')
 for t in R:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'source':str(p),'reverse':str(o),'n':n,'positions':np+1,'transitions':len(R)}))
