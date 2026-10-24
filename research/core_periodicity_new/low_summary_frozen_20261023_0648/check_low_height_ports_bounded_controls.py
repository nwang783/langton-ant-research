"""Direct bounded-stack control against the unbounded exact summary prototype."""
from pathlib import Path
from collections import deque
import sys,json,random
unit,pre=map(Path,sys.argv[1:3]);nd=int(sys.argv[3]);B=int(sys.argv[4]);samples=int(sys.argv[5])if len(sys.argv)>5 else 0
z=list(map(int,unit.read_text().split()));n,m=z[:2];adj=[[]for _ in range(n)]
for k in range(m):
 u,v,dd,c=z[2+4*k:6+4*k];adj[u].append((v,dd,c))
with pre.with_suffix('.ports').open()as f:
 np,ne,ni=map(int,next(f).split());initial=set(map(int,next(f).split()));ports=[tuple(map(int,next(f).split()))for _ in range(np)];expected={}
 for _ in range(ne):
  u,v,c=map(int,next(f).split());expected[u,v]=c
starts=list(range(np));rng=random.Random(1984)
if samples and samples<np:starts=rng.sample(starts,samples)
def search(starts):
 V=[-1]*(n*(B+1));q=deque()
 for u,d in starts:
  p=u*(B+1)+d;V[p]=0;q.append((u,d))
 while q:
  u,d=q.popleft();c=V[u*(B+1)+d]
  for v,dd,cc in adj[u]:
   e=d+dd
   if not 0<=e<=B:continue
   p=v*(B+1)+e;w=min(4,c+cc)
   if w>V[p]:V[p]=w;q.append((v,e))
 return V
same=0;below=0
for ii,p in enumerate(starts):
 h,d,z=ports[p];V=search([(h*nd+d,z)])
 for j,(hh,dd,zz)in enumerate(ports):
  observed=V[(hh*nd+dd)*(B+1)+zz];target=expected.get((p,j),-1);assert observed<=target,(p,j,observed,target)
  same+=observed==target;below+=observed<target
 if(ii+1)%50==0:print({'ports_checked':ii+1,'matched_pairs':same,'strict_lower':below},flush=True)
# Check initial-low port existence with every bounded possible physical depth.
V=search([(h*nd,d)for h in range(4)for d in range(B+1)if(d-h)%2==0]);boundedinitial={p for p,(h,d,z)in enumerate(ports)if V[(h*nd+d)*(B+1)+z]>=0};assert boundedinitial<=initial
R={'status':'PASS_BOUNDED_STACK_CONTROLS','stack_cap_for_control_only':B,'source_ports':len(starts),'target_pairs_checked':len(starts)*np,'exact_profile_matches':same,'summary_strictly_stronger_than_bounded_control':below,'bounded_initial_ports':len(boundedinitial),'exact_initial_ports':len(initial),'scope':'Direct finite-stack replay is a control only. The unbounded weighted summary is certified separately by finite derivations and complete grammar closure.'};pre.with_suffix('.ports.bounded_check.json').write_text(json.dumps(R,indent=2)+'\n');print(R)
