"""EXPLORATORY bounded causal branching, NOT a complete pattern exhaustion or theorem.
Only cells actually exposed by a complete comparison are branched.
Stops UNKNOWN on guard exit, unsupported infinite input family, budget or node cap.
"""
from pathlib import Path
from collections import deque
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import H
P=Path(__file__).parent;D=json.loads((P/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text());W=D['base_word'];Q=[];p=(0,0);h=1
for c in W:Q.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
g=-150;M=set()
for i,q in enumerate(Q):
 r=(q[0]-Q[13][0],q[1]-Q[13][1]);lo=-((r[1]-g)//2);hi=0 if i<13 else-1
 for a in range(lo,hi+1):M.symmetric_difference_update({(r[0]+2*a,r[1]+2*a)})
PH={H[i:]+H[:i]for i in range(104)}
queue=deque([(frozenset({0,1}),frozenset(),-1)]);visited=set();results=[]
while queue and len(results)<32:
 S,F,last=queue.popleft();key=(S,F)
 if key in visited:continue
 visited.add(key);B={q:i for i,q in enumerate(M|{(2*a,2*a)for a in S})};p=(0,0);h=0;words=[];first={};box=[0,0,0,0];status='UNKNOWN step budget';tail=None
 for t in range(100000):
  if p[1]<g:status='EXPORTED below southern guard';break
  x,y=p;box=[min(box[0],x),max(box[1],x),min(box[2],y),max(box[3],y)]
  if x==y and x%2==0 and x>=4:first.setdefault(x//2,t)
  old=B.pop(p,None)
  if old is None:B[p]=t+10**6;h=(h+1)%4;c='R'
  else:h=(h-1)%4;c='L'
  words.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);N=t+1
  if N>=312 and N%104==0:
   w=''.join(words[-104:])
   if w in PH and ''.join(words[-312:])==w*3:
    try:fw,dr,dead,tests=future(B,p,h)
    except AssertionError:continue
    if fw not in PH:continue
    PP=[];pp=p;hh=h
    for cc in fw:PP.append(pp);hh=(hh+(1 if cc=='R'else-1))%4;pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
    tail=dict(word=fw,drift=dr,pose=[p,h],tests=tests)
    if dr[1]<0 or min(y for x,y in PP)<g:status='EXPORTED tail crosses southern guard';break
    infinite=[]
    for j,(x,y)in enumerate(PP):
     if dr==(2,2)and x==y and x%2==0:infinite.append((x//2,j));continue
     if dr==(-2,-2)and x==y and x%2==0:
      candidates=[(a,x//2-a)for a in range(2,x//2+1)]
     elif dr[0]+dr[1]==0 and(x+y)%4==0:
      a=(x+y)//4;dx=2*a-x
      candidates=[(a,dx//dr[0])]if dx%dr[0]==0 and y+(dx//dr[0])*dr[1]==2*a else[]
     else:candidates=[]
     for a,k in candidates:
      if a>=2 and k>=0:first[a]=min(first.get(a,10**99),N+104*k+j)
    if infinite:status='UNRESOLVED infinite next-ray family';tail['infinite_ray_classes']=infinite
    else:status='finite complete comparison'
    break
 queries=sorted((tt,a)for a,tt in first.items()if a not in S and a not in F)
 if status=='finite complete comparison':
  whites=set(F)
  for tt,a in queries:
   assert tt>last
   queue.append((S|{a},frozenset(whites),tt));whites.add(a)
 r=dict(index=len(results),black_indices=sorted(S),fixed_white_indices=sorted(F),last_branch_read=last,status=status,checked_reads=len(words),prefix_word_sha256=hashlib.sha256(''.join(words).encode()).hexdigest(),current_pose=[p,h],post_bbox=box,new_queries=queries,tail=tail)
 results.append(r);print(r['index'],r['black_indices'],'white',r['fixed_white_indices'],status,'reads',len(words),'box',box,'new',queries,flush=True)
out=dict(status='EXPLORATORY, universal closure UNKNOWN',limits=dict(node_cap=32,per_node_reads=100000,southern_guard=g),root_fixed_inputs=[0,1],mature_kernel_black_count=len(M),unprocessed_queue=len(queue),results=results)
(P/'PHASE13_CAUSAL_TREE_EXPLORATORY.json').write_text(json.dumps(out,indent=2)+'\n')
