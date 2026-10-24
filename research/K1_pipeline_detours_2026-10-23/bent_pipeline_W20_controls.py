"""Literal prepared alternating-bend K1 gate control, not a white-input front.
The word is algebraically prescribed by the signed local skeleton, not searched.
"""
from collections import defaultdict,Counter,deque
from pathlib import Path
import json
W='LRRRRLLLLRLLLLRLRRRR';D=(1j,1,-1j,-1)
def inv(z):return[int(z.real),int(z.imag)]
def literal(a):
 period=20*a;dy=2*a;drift=complex(0,dy);q=1+0j;h=1j;hist=defaultdict(list);flow=Counter()
 def canon(z):
  k=int(z.imag)//dy;return z-k*drift,k
 for t,c in enumerate(W*a):
  z,k=canon(q);hist[z].append((t-k*period,h,c));out=h*(-1j if c=='R'else 1j);flow[z,out]+=1;q+=out;h=out
 assert q==1+drift and h==1j
 hs=[]
 for z,es in sorted(hist.items(),key=lambda x:(x[0].real,x[0].imag)):
  es.sort();assert all(es[i][2]!=es[i-1][2]for i in range(1,len(es)))
  hs.append(dict(cell=inv(z),turns=''.join(c for t,h,c in es),incoming=[inv(h)for t,h,c in es],times=[t for t,h,c in es],input='white'if es[0][2]=='R'else'black'))
 assert Counter((int(x['cell'][0]),x['turns'])for x in hs)==Counter({(-1,'L'):2*a,(0,'RLRL'):2*a,(1,'RLRL'):2*a,(2,'R'):2*a})
 # Original physical stream; oriented positive drift is up, RIGHT=east.
 faces={(x,y)for x in range(-4,5)for y in range(dy)};adj=defaultdict(list)
 def face(x,y):return(x,y%dy)
 def edge(c,l,f):
  if c in faces and l in faces:adj[c].append((l,-f));adj[l].append((c,f))
 for x in range(-4,5):
  for y in range(dy):
   if (x+y)%2:src=complex(x,y);out=1;cf=face(x,y-1);lf=face(x,y)
   else:src=complex(x+1,y);out=-1;cf=face(x,y);lf=face(x,y-1)
   src,k=canon(src);edge(cf,lf,flow[src,out])
   if (x+y)%2==0:src=complex(x,y);out=1j;cf=face(x,y);lf=face(x-1,y)
   else:src=complex(x,y+1);out=-1j;cf=face(x-1,y);lf=face(x,y)
   src,k=canon(src);edge(cf,lf,flow[src,out])
 height={(4,0):0};todo=deque(height)
 while todo:
  u=todo.popleft()
  for v,k in adj[u]:
   val=height[u]+k
   if v in height:assert height[v]==val
   else:height[v]=val;todo.append(v)
 assert set(height)==faces
 maxc=max(v for (x,y),v in height.items()if(x+y)%2==0)
 assert {v for (x,y),v in height.items()if x==-4}=={-1};assert {v for(x,y),v in height.items()if x==4}=={0};assert maxc==1
 return dict(full_period=period,full_drift=inv(drift),histories=hs,stream=dict(c_left=-1,c_right=0,max_C=1,excess_K=1,scope='prepared front stream; no white-input maximum theorem imported',faces=[dict(face=[x,y],kind='C'if(x+y)%2==0 else'L',height=v)for(x,y),v in sorted(height.items())]))
profiles=[literal(a)for a in(1,2,3)]
controls=[]
for n in(1,2,3,10,100):
 seed={1+0j,0-1j,1-1j}|{complex(-1,y)for y in range(2*n)};black=set(seed);q=1+0j;h=1j
 for t,c in enumerate(W*n):
  actual='L'if q in black else'R';assert actual==c
  black.symmetric_difference_update({q});h*=(-1j if c=='R'else 1j);q+=h
 expected={1+2*n*1j,0+(2*n-1)*1j,1+(2*n-1)*1j}|{complex(2,y)for y in range(1,2*n+1)}
 assert black==expected and q==1+2*n*1j and h==1j
 mismatch=None
 for j,c in enumerate(W):
  actual='L'if q in black else'R'
  if actual!=c:mismatch=dict(offset=j,cell=inv(q),expected=c,actual=actual);break
  black.symmetric_difference_update({q});h*=(-1j if c=='R'else 1j);q+=h
 assert mismatch['offset']==11 and mismatch['cell']==[-1,2*n+1]
 controls.append(dict(stages=n,matched_steps=20*n,initial_black_count=len(seed),initial_black=[inv(z)for z in sorted(seed,key=lambda z:(z.real,z.imag))],first_missing_fuel=mismatch))
r=dict(status='PASS exact literal prepared controls; NOT a white-input front',scope=__doc__,word=W,profiles=profiles,finite_fuel_controls=controls)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(status=r['status'],word=W,full_periods=[x['full_period']for x in profiles],full_drifts=[x['full_drift']for x in profiles],stream=profiles[0]['stream']|{'faces':'omitted'},matched_prefixes=[x['matched_steps']for x in controls]),indent=2))
