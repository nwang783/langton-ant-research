#!/usr/bin/env python3
"""All160 raw local continuations for the bounded horizontal-jitter class."""
import itertools,json,hashlib,collections
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
targets=((2,5),(3,2),(-2,-5),(-3,-2))
def L(p):return -2*p[0]+3*p[1]
domains=[];maxima=[]
for target in targets:
 words=[];ceiling=0
 for first_axis in (0,1):
  for signs in itertools.product((0,1),repeat=9):
   w=tuple(((first_axis+j)%2+2*signs[j]) for j in range(9))
   p=(0,0);vals=[]
   for d in w:
    vals.append(L(p));p=(p[0]+D[d][0],p[1]+D[d][1])
   if p==target:words.append(w);ceiling=max(ceiling,max(vals))
 domains.append(words);maxima.append(ceiling)
assert list(map(len,domains))==[4,20,4,20]
assert maxima==[10,7,0,7]
assert all(w[-1]==0 for w in domains[0])
records=[];histograms={};survivors=[]
for choice in (1,3):
 hist=collections.Counter()
 for i,u in enumerate(domains[choice]):
  for j,v in enumerate(domains[2]):
   p=(0,0);h=0;initial={};parity={};last={}
   for t,d in enumerate(u+v):
    turn=(d-h)%4
    assert turn in(1,3)
    want=int(turn==3);required_initial=want^parity.get(p,0)
    known=initial.get(p,0 if L(p)>=0 else None)
    if known is not None and known!=required_initial:
     hist[t]+=1
     records.append(dict(horizontal=choice,first=i,second=j,read=t,cell=p,
      requested_initial=required_initial,available_initial=known,previous=last.get(p)))
     break
    initial[p]=required_initial;parity[p]=1^parity.get(p,0);last[p]=t
    p=(p[0]+D[d][0],p[1]+D[d][1]);h=d
   else:survivors.append([choice,i,j])
 histograms[str(choice)]=dict(hist)
assert len(records)==160 and not survivors
p=Path(__file__);raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n'
p.with_suffix('.records.json').write_bytes(raw)
out=dict(status='ALL160 LOCAL PAIRS CONFLICT',matrix=[[3,2],[2,5]],k=9,
 domain_counts=list(map(len,domains)),proper_prefix_maxima=maxima,histograms=histograms,
 latest=max(r['read'] for r in records),survivors=survivors,
 records_sha256=hashlib.sha256(raw).hexdigest())
p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
