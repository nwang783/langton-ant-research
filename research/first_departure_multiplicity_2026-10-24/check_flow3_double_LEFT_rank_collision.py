"""All16 complete neighbor pairs of a constant3 LEFT-LEFT unit stencil.
Includes one-use entry/exit. Every accepted port row has a literal rank collision.
No front or period scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
pos={'A':(0,1),'Z':(0,0),'Y':(1,0),'B':(1,1)};inv={p:u for u,p in pos.items()}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
rows=[];counts=Counter()
for a,b in product(['EWE','EWWW','EEEW','EWEE'],['NNN','NNSN','NNNS','NSNN']):
 hs=dict(A=a,Z='NSSS',Y='WEEE',B=b);succ={};bad=None;edges=[]
 for u,h in hs.items():
  p=pos[u]
  for dr in H:
   q=p[0]+V[dr][0],p[1]+V[dr][1]
   if q not in inv:continue
   v=inv[q];sr=[i for i in range(len(h))if out(h,i)==dr];tr=[i for i,x in enumerate(hs[v])if x==dr]
   if len(sr)!=len(tr):bad=dict(source=u,target=v,heading=dr,departures=sr,arrivals=tr);break
   for j,(r,s)in enumerate(zip(sr,tr),1):succ[u,r]=(v,s);edges.append([u,r,v,s,dr,j])
  if bad:break
 if bad:counts['port mismatch']+=1;rows.append(dict(A=a,B=b,result='port mismatch',witness=bad));continue
 witness=None
 for r in range(4):
  cur=('Z',r);route=[cur]
  for _ in range(18):
   if cur not in succ:break
   cur=succ[cur];route.append(cur)
   if cur[0]=='Z':
    if cur[1]!=r+1:witness=route
    break
   if cur in route[:-1]:break
  if witness:break
 assert witness and len(witness)==5
 counts['literal rank collision']+=1;rows.append(dict(A=a,B=b,result='literal rank collision',all_internal_edges=edges,actual_return=witness))
assert dict(counts)=={'literal rank collision':10,'port mismatch':6}
obj=dict(scope=__doc__,complete_counts=dict(counts),rows=rows,nonmaximal_normal_form='R^a (LR)^(n-1) L R^b, n>=1, a,b in{1,2}; or RR.',locally_maximal_templates=['RR','RLR','RLRR','RRLR','RRLRR'],locally_maximal_max_edges=4)
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS16 pairs:6 port failures,10 literal4-step rank collisions')
