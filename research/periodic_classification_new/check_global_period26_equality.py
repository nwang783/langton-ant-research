#!/usr/bin/env python3
"""Author complete equality cases for a putative P26 white front.
The separate structural reduction restricts full drift to3,+/-1 or3,3,
and a complete class to five occurrences. This is not a general front scan.
"""
from itertools import product,combinations
from pathlib import Path
import json,time
D=[(0,1),(1,0),(0,-1),(-1,0)]

def run(b):
 drift=(3,b);mac={};st=time.time()
 for h0 in range(4):
  for k,L in ((0,4),(0,8),(-1,6),(1,6)):
   arr=[]
   for cs in product((1,-1),repeat=L):
    p=(0,0);h=h0;tr=[];valid=True
    for t,c in enumerate(cs):
     tr.append((p,h,c));h=(h+c)%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
     if t<L-1 and p[0]%3==0 and p[1]==(p[0]//3)*b:valid=False;break
    if valid and p==(3*k,b*k):arr.append((h,cs,tr))
   mac[h0,k,L]=arr
 counts={};total=cyclic=central=white=0;accepted=[];bytype={}
 def extend(h0,blocks,layout,hs,turns,trace,p,kind):
  nonlocal total,cyclic,central,white
  if not blocks:
   total+=1;bytype[kind]=bytype.get(kind,0)+1
   if hs!=h0:counts['heading']=counts.get('heading',0)+1;return
   cyclic+=1;groups={}
   for t,(q,h,c) in enumerate(trace):
    x,y=q;k=x//3;r=x%3;groups.setdefault((r,y-k*b),[]).append((t-k*26,c))
   cs=sorted(groups[(0,0)]);assert len(cs)==5
   if any(c!=(1 if j%2==0 else -1) for j,(_,c) in enumerate(cs)):
    counts['center_white']=counts.get('center_white',0)+1;return
   central+=1
   for q,ls in groups.items():
    ls.sort()
    if any(c!=(1 if j%2==0 else -1) for j,(_,c) in enumerate(ls)):
     counts['other_white']=counts.get('other_white',0)+1;return
   white+=1;accepted.append(dict(type=kind,incoming=h0,layout=layout,word=''.join('R' if c==1 else'L' for c in turns)));return
  k,L=blocks[0]
  for h,cs,tr in mac[hs,k,L]:
   ntr=trace+[((p[0]+q[0],p[1]+q[1]),hh,c) for q,hh,c in tr]
   extend(h0,blocks[1:],layout,h,turns+cs,ntr,(p[0]+3*k,p[1]+b*k),kind)
 for long in range(4):
  blocks=((1,6),)+tuple((0,8 if i==long else 4) for i in range(4))
  for h in range(4):extend(h,blocks,blocks,h,(),[],(0,0),'one_winding')
 for positives in combinations(range(1,5),2):
  blocks=((-1,6),)+tuple((1,6) if i in positives else(0,4) for i in range(1,5))
  for h in range(4):extend(h,blocks,blocks,h,(),[],(0,0),'three_windings')
 return dict(full_drift=drift,macro_counts={str(k):len(a) for k,a in mac.items()},program_sequences=total,by_type=bytype,heading_restoring=cyclic,center_white_legal=central,all_classes_white_legal=white,rejections=counts,accepted=accepted,seconds=time.time()-st)
result=dict(scope='AUTHOR COMPLETE STRUCTURALLY REDUCED P26 EQUALITY CASES ONLY; global reduction separately required.',cases=[run(b) for b in(1,-1,3)])
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
