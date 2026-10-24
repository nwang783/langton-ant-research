"""One exact six-contact/no-flow2-crossing mixed candidate, full d=(-3,-3).
Finite first-reader layer only; unknown P symbolic and farther fields open.
Not a bounded period/drift/width search or a completed front.
"""
from itertools import product
from collections import defaultdict,deque,Counter
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)};d=(-3,-3)
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def key(p):return(p[0]-p[1],p[0]%3)
def rep(k):n,r=k;return(r,r-n)
def shift(p,k):q=rep(k);v=(q[0]-p[0])//3;assert(q[0]-p[0])%3==0 and(p[0],p[1])==(q[0]-3*v,q[1]-3*v);return v
def add(p,h,s=1):return(p[0]+s*V[h][0],p[1]+s*V[h][1])
def rr(h,dr,kind):return[i for i in range(len(h))if(h[i]if kind=='in'else out(h,i))==dr]
def fp(p,h):
 x,y=p;return{'E':((x,y-1),(x,y)),'W':((x-1,y),(x-1,y-1)),'N':((x,y),(x-1,y)),'S':((x-1,y-1),(x,y-1))}[h]
def check(hs):
 succ={};eq={};edges=[];open_ports=[]
 for k,h in hs.items():
  p=rep(k);ia='NS'if k[0]%2==0 else'EW';oa='EW'if k[0]%2==0 else'NS'
  for dr in oa:
   n=len(rr(h,dr,'out'));ek=(k,dr)
   if ek in eq and eq[ek]!=n:return'port',None
   eq[ek]=n
  for dr in ia:
   p0=add(p,dr,-1);sk=key(p0);ek=(sk,dr);n=len(rr(h,dr,'in'))
   if ek in eq and eq[ek]!=n:return'port',None
   eq[ek]=n
  for dr in H:
   q=add(p,dr);v=key(q);sr=rr(h,dr,'out')
   if v not in hs:
    open_ports.extend((k,r,v,dr)for r in sr);continue
   tr=rr(hs[v],dr,'in')
   if len(sr)!=len(tr):return'port',None
   z=shift(q,v)
   for a,b in zip(sr,tr):succ[k,a]=(v,b,z);edges.append(((k,a),(v,b),-z,1))
 nodes=[(k,r)for k,h in hs.items()for r in range(len(h))]
 for s in nodes:
  cur=s;vol=0;seen={s};route=[(s,0)]
  while cur in succ:
   k,r,z=succ[cur];cur=(k,r);vol+=z;route.append((cur,vol))
   if cur[0]==s[0]and vol==0:
    if cur[1]!=s[1]+1:return'physical rank skip',route
    break
   if cur in seen:return'known quotient event cycle',route
   seen.add(cur)
 adj=defaultdict(list)
 for(k,dr),f in eq.items():
  c,l=map(key,fp(rep(k),dr));adj[l].append((c,f));adj[c].append((l,-f))
 anchor=key((0,-1));val={anchor:0};queue=deque([anchor])
 while queue:
  u=queue.popleft()
  for v,w in adj[u]:
   if v in val:
    if val[v]!=val[u]+w:return'face inconsistency',None
   else:val[v]=val[u]+w;queue.append(v)
 if len(val)!=len(adj):return'disconnected face graph',None
 if any(z>0 for (n,r),z in val.items()if n%2):return'GLOBAL C excess',None
 return'open symbolic clocks',dict(edges=edges,faces=val,nodes=nodes,succ=succ,open_ports=open_ports)
base={(0,0):'NSSN',(0,1):'NSN',(0,2):'NNN',(1,0):'WWEE',(1,1):'WWEE',(1,2):'WEEE'}
counts=Counter();rows=[]
for l0,l1,l2,r0,r1 in product(['EEE','EEEE'],['WEE','EEW','WEEE','EEWE'],['WEW','WEWE'],['SS','SSN'],['NNSS','NSSN','SNNS','SSNN']):
 hs=base|{(-1,0):l0,(-1,1):l1,(-1,2):l2,(2,0):r0,(2,1):r1,(2,2):'NNS'}
 ans,data=check(hs);counts[ans]+=1
 if ans=='open symbolic clocks':rows.append((dict(L0=l0,L1=l1,L2=l2,R0=r0,R1=r1),hs,data))
print('128 first-layer assignments',dict(counts),'remaining',len(rows))
for r,_,_ in rows:print(r)
# Propagated NEXT physical reader row; counts alone force L0=EEE,L2=WEW.
# This is a fixed necessary port interface, not a variable-width solve.
second=Counter();rr2=[]
for l1,r0 in product(['WEE','EEW','WEEE','EEWE'],['SS','SSN']):
 q0s=['NS','NSS','SSN']if len(l1)==3 else['NSSS','SSNS']
 q1s=['NN','NNS','SNN']if len(l1)==3 else['NNSN','SNNN']
 for q0,q1,q2 in product(q0s,q1s,['NNNS','NSNN']):
  hs=base|{(-1,0):'EEE',(-1,1):l1,(-1,2):'WEW',(2,0):r0,(2,1):'SSNN',(2,2):'NNS',(-2,0):q0,(-2,1):q1,(-2,2):q2}
  ans,data=check(hs);second[ans]+=1
  if ans=='open symbolic clocks':rr2.append((dict(L1=l1,R0=r0,Q0=q0,Q1=q1,Q2=q2),hs,data))
print('104 exact next-reader completions',dict(second),'remaining',len(rr2))
for r,_,_ in rr2:print(r)
