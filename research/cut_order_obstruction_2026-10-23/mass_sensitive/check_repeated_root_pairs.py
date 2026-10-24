from pathlib import Path
from collections import Counter
from itertools import combinations
import json
ROOT=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
W=(ROOT.parents[1]/'word_stabilization/standard_word.txt').read_text().strip()
F={(W*2)[i:i+10]for i in range(104)}
SIX={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
z='LRRLLRRLLRR';assert z[:10]not in F and z[1:]not in F and z not in SIX
out={'status':'PASS','parameters':0,'literal_updates':0,'selected_residual_windows':0,'eleven_owner_checks':0}
for n in range(4,66):
 w=''.join('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L'for j in range(n,0,-1))
 p=(0,0);h=0;first={};seed=set();reads=[];poses=[]
 for a in w:
  if p not in first and a=='L':seed.add(p)
  elif p in first:assert first[p]!=a
  first[p]=a;reads.append(p);poses.append((p,h));h=(h+(1 if a=='R'else-1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
 assert len(seed)==11*n+2
 owner={p:p for p in seed};active=None;labels=[]
 for p,a in zip(reads,w):
  labels.append(active)
  if a=='R':assert p not in owner;owner[p]=active
  else:active=owner.pop(p)
 pairs=set();count=0
 for k in range(1,n-2):
  j=n-k;tk=k*(16*n+6)-8*k*(k-1)
  for l in range(n-k-2):
   start=tk+4*j+3+4*l;end=start+10
   roots=[(-2*(l+s),2*n+1)for s in [1,2,3]]
   assert w[start:end+1]==z
   assert labels[start:end+1]==[roots[0]]*4+[roots[1]]*4+[roots[2]]*3
   assert poses[end]==((-k-2*l-7,2*n-k),3)
   pairs.update(combinations(roots,2));count+=1
 assert count==(n-3)*(n-2)//2
 expected={((-2*s,2*n+1),(-2*(s+1),2*n+1))for s in range(1,n-1)}
 expected|={((-2*s,2*n+1),(-2*(s+2),2*n+1))for s in range(1,n-2)}
 assert pairs==expected and len(pairs)==2*n-5
 out['parameters']+=1;out['literal_updates']+=len(w);out['selected_residual_windows']+=count;out['eleven_owner_checks']+=11*count
(ROOT/'check_repeated_root_pairs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
