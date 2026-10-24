#!/usr/bin/env python3
"""Author exact equality-case control, not an all-period front exclusion.
Given the separate n6/P36 packing reduction, enumerate its only remaining
three winding gaps (+1,+1,-1), three physical four-step returns.
"""
from itertools import product,combinations
from pathlib import Path
import json,time
D=[(0,1),(1,0),(0,-1),(-1,0)];mac={}
for h0 in range(4):
 for k,L in ((0,4),(-1,8),(1,8)):
  arr=[]
  for cs in product((1,-1),repeat=L):
   p=(0,0);h=h0;tr=[];valid=True
   for t,c in enumerate(cs):
    tr.append((p,h,c));h=(h+c)%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
    if t<L-1 and p[1]==0 and p[0]%4==0:valid=False;break
   if valid and p==(4*k,0):arr.append((h,cs,tr))
  mac[h0,k]=arr
counts={};total=0;cyclic=0;central=0;firstwhite=0;accepted=[];st=time.time()
def check(h0,ks,choice,hs,turns,trace,p):
 global total,cyclic,central,firstwhite
 if not ks:
  total+=1
  if hs!=h0:counts['heading'] =counts.get('heading',0)+1;return
  cyclic+=1
  groups={}
  for t,(q,h,c) in enumerate(trace):
   x,y=q;k=x//4;r=x%4;groups.setdefault((r,y),[]).append((t-k*36,c))
  # Center is the class whose complete multiplicity six was assumed.
  cs=sorted(groups[(0,0)])
  assert len(cs)==6
  if any(c!=(1 if j%2==0 else -1) for j,(_,c) in enumerate(cs)):
   counts['center_white']=counts.get('center_white',0)+1;return
  central+=1
  for q,ls in groups.items():
   ls.sort()
   if any(c!=(1 if j%2==0 else -1) for j,(_,c) in enumerate(ls)):
    counts['other_white']=counts.get('other_white',0)+1;return
  firstwhite+=1
  accepted.append(dict(incoming=h0,windings=choice,word=''.join('R' if c==1 else'L' for c in turns),multiplicities={str(q):len(a) for q,a in groups.items()}));return
 k=ks[0]
 for h,cs,tr in mac[hs,k]:
  ntr=trace+[((p[0]+q[0],p[1]+q[1]),hh,c) for q,hh,c in tr]
  check(h0,ks[1:],choice,h,turns+cs,ntr,(p[0]+4*k,p[1]))
for positives in combinations(range(1,6),2):
 ks=(-1,)+tuple(1 if i in positives else 0 for i in range(1,6))
 for h in range(4):check(h,ks,ks,h,(),[],(0,0))
result=dict(scope='AUTHOR COMPLETE n6/P36 THREE-WINDING EQUALITY-CASE ENUMERATION ONLY; the separate packing reduction is required.',macro_counts={str(k):len(a) for k,a in mac.items()},layouts=10,initial_headings=4,program_sequences=total,heading_restoring=cyclic,center_white_legal=central,all_classes_white_legal=firstwhite,rejections=counts,accepted=accepted,seconds=time.time()-st)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
