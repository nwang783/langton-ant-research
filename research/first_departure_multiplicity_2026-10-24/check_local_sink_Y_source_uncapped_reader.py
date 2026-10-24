"""All possible complete WHITE Q readers of the local sink/Y/source square.
The n<=2(I+J)+1 domain is derived from exact physical counts, not a cutoff.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rr(h,d,k):return[i for i in range(len(h))if(h[i]if k=='in'else out(h,i))==d]
pos={'F':(0,0),'L0':(0,1),'Q':(-1,1),'L2':(-1,0)};inv={p:u for u,p in pos.items()}
rows=[];good=[];counts=Counter()
for l0,l2 in product(['EEE','EEEE'],['WEW','WEWE']):
 I=len(l2);J=len(l0)
 for n in range(I,2*(I+J)+2):
  for np in combinations(range(n),I):
   nn=set(np);q=''.join('N'if i in nn else'S'for i in range(n))
   if len(rr(q,'E','out'))!=J:continue
   l=n//2;rn=sum(q[i]=='N'for i in range(0,n,2));rs=(n+1)//2-rn;assert I+J==2*rn+l
   hs=dict(F='NSSN',L0=l0,Q=q,L2=l2);succ={};edges=[]
   for u,h in hs.items():
    p=pos[u]
    for d in H:
     t=p[0]+V[d][0],p[1]+V[d][1]
     if t not in inv:continue
     v=inv[t];sr=rr(h,d,'out');tr=rr(hs[v],d,'in');assert len(sr)==len(tr)
     for j,(a,b)in enumerate(zip(sr,tr),1):succ[u,a]=(v,b);edges.append([u,a,v,b,d,j])
   witness=None
   for u in['F','L2','Q','L0']:
    for r in range(len(hs[u])):
     cur=(u,r);route=[cur]
     for _ in range(sum(map(len,hs.values()))+1):
      if cur not in succ:break
      cur=succ[cur];route.append(cur)
      if cur[0]==u:
       if cur[1]!=r+1:witness=route
       break
      if cur in route[:-1]:witness=route;break
     if witness:break
    if witness:break
   rec=dict(L0=l0,L2=l2,Q=q,derived_length_bound=2*(I+J)+1,N_in=I,E_out=J,R_N=rn,R_S=rs,opposite_C_raise=rs-rn,all_internal_edges=edges)
   if witness:counts['literal rank collision']+=1;rec['collision_route']=witness
   else:counts['necessary survivor']+=1;good.append(rec)
   rows.append(rec)
assert len(rows)==1014 and dict(counts)=={'literal rank collision':1010,'necessary survivor':4}
assert{r['Q']for r in good}=={'SSSSSSNNSN','SSSSSSNNSNS','SSSSSSNNSNSN','SSSSSSNNSNSNS'}
assert [r['opposite_C_raise']for r in good]==[3,4,4,5]
obj=dict(scope=__doc__,domain_identity='Nin+Eout=2 R_N+floor(n/2); n<=2(I+J)+1',counts=dict(counts),all_derived_reader_rows=rows,necessary_survivors=good,warning='Four survivors are only complete local port/rank controls, not actual exterior realizations. Every one forces a higher opposite C; global maximum excludes them without an outside multiplicity cap.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS1014 derived-domain readers:1010 literal collisions/4 higher-C controls')
