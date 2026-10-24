"""One exact mixed reset geometry; symbolic full-drift quotient, no period scan.
Turn word RRLRLL, b displacement(3,-1), actual d=(-3,1).
Open outer normal rows remain unfilled; necessary models are not fronts.
"""
from itertools import product
from collections import defaultdict,deque
H='NESW';dn={'E':1,'W':-1,'N':3,'S':-3};vlt={'E':0,'W':0,'N':1,'S':-1}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
for middle,root in product(['EEWW','EWWE'],['NSS','NSSN']):
 hs={-4:root,-3:'WWEE',-2:'NNSS',-1:'EWWE',0:'NNSS',1:middle}
 edges=[];ports=[];bad=None
 for n,h in hs.items():
  for dr in H:
   sr=[r for r in range(len(h))if out(h,r)==dr];m=n+dn[dr]
   if m not in hs:
    ports.extend((n,r,dr)for r in sr);continue
   tr=[r for r,x in enumerate(hs[m])if x==dr]
   if len(sr)!=len(tr):bad=('port',n,dr,sr,m,tr);break
   for a,b in zip(sr,tr):edges.append(((n,a),(m,b),-vlt[dr],1))
  if bad:break
 if bad:print(middle,root,bad);continue
 adj=defaultdict(list)
 for s,t,p,c in edges:adj[s].append((t,p,c));adj[t].append((s,-p,-c))
 vals={};requirements=[];components=[]
 for s in [(n,r)for n,h in hs.items()for r in range(len(h))]:
  if s in vals:continue
  j=len(components);cc=[];vals[s]=(j,0,0);q=deque([s])
  while q:
   u=q.popleft();cc.append(u);_,p,c=vals[u]
   for v,pp,cc0 in adj[u]:
    want=(j,p+pp,c+cc0)
    if v in vals:
     _,p0,c0=vals[v]
     if (p0,c0)!=want[1:]:requirements.append((p0-want[1],want[2]-c0))
    else:vals[v]=want;q.append(v)
  components.append(cc)
 print('case',middle,root,'components',len(components),'requirements',set(requirements),'open ports',ports)
 print('affine clocks',dict(sorted(vals.items())))
