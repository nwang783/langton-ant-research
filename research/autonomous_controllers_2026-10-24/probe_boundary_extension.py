#!/usr/bin/env python3
"""Unfrozen discovery; exact partial ordinal graph only."""
from itertools import combinations,product
from collections import Counter
from check_extremal_read_coupling import D,quotient
DRIFT=(2,-2)

def graph(H):
 pts=[(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)];ix={p:i for i,p in enumerate(pts)}
 nodes=[(i,j)for i,h in enumerate(H)for j in range(len(h))];out={};incoming={}
 for i,p in enumerate(pts):
  for h in range(4):
   src=[j for j,hi in enumerate(H[i])if(hi+(1 if j%2==0 else-1))%4==h]
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT)
   if q not in ix:continue
   ii=ix[q];dst=[j for j,hi in enumerate(H[ii])if hi==h]
   assert len(src)==len(dst),(i,h,src,ii,dst,H)
   for u,v in zip(src,dst):out[i,u]=((ii,v),k);incoming[ii,v]=((i,u),k)
 chains=[];seen=set()
 for start in nodes:
  if start in incoming:continue
  seq=[];at=start;k=0
  while True:
   assert at not in seen;seen.add(at);seq.append((at,k))
   if at not in out:break
   at,dk=out[at];k+=dk
  chains.append(seq)
 if len(seen)!=len(nodes):return 'closed',None
 for seq in chains:
  prev={}
  for z,((i,j),k)in enumerate(seq):
   p=(pts[i][0]+k*2,pts[i][1]-k*2)
   if p in prev and j!=prev[p]+1:return 'skip',None
   prev[p]=j
 return 'open',(pts,chains)

def relations(H,G):
 pts,chains=G;rel=[[],[]]
 for chain in chains:
  (i,j),k=chain[0];assert k==0;h=H[i][j];p=pts[i];sp=(p[0]-D[h][0],p[1]-D[h][1]);sr,sk=quotient(sp,DRIFT)
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;q=pts[ii];tp=(q[0]+kk*2+D[ho][0],q[1]-kk*2+D[ho][1]);tr,tk=quotient(tp,DRIFT)
  assert sum(sp)==sum(tp)==len(H)//2-1
  if sp==tp:
   a=[z for z,hh in enumerate(H[i])if hh==h].index(j)
   b=[z for z,hh in enumerate(H[ii])if(hh+(1 if z%2==0 else-1))%4==ho].index(jj)
   rel[sr[0]].append((a,b,len(chain)+1))
 return rel

def words(I,J,isC,rel):
 total=0;out=[]
 for n in range(0,2*(I+J)+2):
  if isC:
   z=I+J-n//2
   if z%2:continue
   X=z//2;Y=I-X;plus,minus,dep=1,3,2
  else:
   z=I+(n+1)//2-J
   if z%2:continue
   X=z//2;Y=I-X;plus,minus,dep=0,2,3
  if not 0<=X<=(n+1)//2 or not 0<=Y<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),Y)):
   nn=set(rr)|set(ll);hs=tuple(plus if k in nn else minus for k in range(n));pp=sorted(nn);dd=[k for k,h in enumerate(hs)if(h+(1 if k%2==0 else-1))%4==dep]
   if len(dd)!=J:continue
   total+=1
   if all(pp[b]==dd[a]+1 for a,b,L in rel):out.append(hs)
 return out,total

def extend(H):
 kind,G=graph(H)
 if kind!='open':return [],{'input_'+kind:1}
 rel=relations(H,G);nextT=len(H)//2-1;isC=nextT%2==1;aa,bb=H[-2:]
 def oc(hs,d):return sum((h+(1 if k%2==0 else-1))%4==d for k,h in enumerate(hs))
 if isC:
  I0=oc(bb,1);J0=aa.count(2);I1=oc(aa,1);J1=bb.count(2)
 else:
  I0=oc(aa,0);J0=bb.count(3);I1=oc(bb,0);J1=aa.count(3)
 q,nq=words(I0,J0,isC,rel[0]);r,nr=words(I1,J1,isC,rel[1]);stats=Counter({'raw_pairs':nq*nr,'filtered_pairs':len(q)*len(r)});surv=[]
 for a,b in product(q,r):
  HH=H+[a,b];odd=sum(len(h)%2 for h in HH)
  if odd>8:stats['odd_excess']+=1;continue
  # Positive signed residue deficits to mod4==2, in both x and y.
  pts=[(rr,t-rr)for t in range(-1,len(HH)//2-1)for rr in(0,1)]
  defects=[]
  for axis in(0,1):
   sums=[sum((-1)**sum(p)for p,h in zip(pts,HH)if len(h)%2 and p[axis]%2==rr)for rr in(0,1)]
   defects.append(sum(min((2-v)%4,(v-2)%4)for v in sums))
  if odd+max(defects)>8:stats['residue_odd_excess']+=1;continue
  kind,GG=graph(HH);stats[kind]+=1
  if kind=='open':surv.append(HH)
 return surv,dict(stats)

if __name__=='__main__':
 H=[(3,),(3,),(2,2,0,2),(2,2,0),(1,1,3,3,3,3),(1,1,1)]
 frontier=[H]
 for step in range(1,5):
  new=[];S=Counter()
  for H in frontier:
   out,stats=extend(H);new+=out;S.update(stats)
  print('step',step,'frontier',len(new),'stats',dict(S),flush=True)
  open('/tmp/boundary_step%d.json'%step,'w').write(__import__('json').dumps(new))
  frontier=new
  if len(new)>1000 or not new:break

def positive_clock_cycle(H,G):
 pts,chains=G;where={}
 for c,seq in enumerate(chains):
  for a,((i,j),k) in enumerate(seq):where[i,j]=(c,a,k)
 edges=[]
 for i,hs in enumerate(H):
  for j in range(len(hs)-1):
   u,a,ka=where[i,j];v,b,kb=where[i,j+1];C=4+a-b;K=kb-ka
   if u!=v:C=max(C,len(chains[u]))
   edges.append((u,v,C,K,i,j))
 N=sum(map(len,H));P=10*N+100;n=len(chains);dist=[0]*n;prev=[None]*n;last=None
 for _ in range(n):
  last=None
  for e in edges:
   u,v,C,K,*_=e;w=C+K*P
   if dist[v]<dist[u]+w:dist[v]=dist[u]+w;prev[v]=e;last=v
  if last is None:return None
 at=last
 for _ in range(n):at=prev[at][0]
 start=at;cy=[]
 while True:
  e=prev[at];cy.append(e);at=e[0]
  if at==start:break
 C=sum(e[2]for e in cy);K=sum(e[3]for e in cy)
 assert K>=0 and C+K*N>0,(C,K,N)
 return {'cycle':cy,'constant':C,'period_coefficient':K}
