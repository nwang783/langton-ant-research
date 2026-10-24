"""Exact counterexample to a pointwise seed-to-lift lamp gauge.
No blankboard search is performed; both finite witness words are literal.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
LONG='RRRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRL'
SHORT='LLRLLRLLRL'
def mul(x,y):
 s=list(x)
 for a,e in y:
  if s and s[-1][0]==a:
   _,f=s.pop();e=(e+f)%4
   if e:s.append((a,e))
  else:s.append((a,e))
 return tuple(s)
def canon(x):
 while True:
  options=[x,mul(x,((0,1),(1,3))),mul(x,((1,1),(0,3)))];n=min(map(len,options));z=min(v for v in options if len(v)==n)
  if n==len(x):return z
  x=z

def replay(w):
 x=y=h=0;g=();last={};first={};counts={};cosets=[];d=[(0,1),(1,0),(0,-1),(-1,0)]
 for t,a in enumerate(w):
  p=x,y;c=canon(g);cosets.append(c)
  if p in last:assert last[p]!=a,(t,p,a)
  else:first[p]=a
  last[p]=a;counts[p]=counts.get(p,0)+1
  g=mul(g,((int(a=='L'),1),));h=(h+(1 if a=='R' else-1))%4;x+=d[h][0];y+=d[h][1]
 p=x,y;c=canon(g)
 assert c not in cosets
 assert first.get(p,'R')=='R'
 black=sorted(q for q,a in first.items() if a=='L')
 return {'word':w,'length':len(w),'pose':[x,y,h],'reduced_word':''.join('RL'[a]*e for a,e in g),'canonical_coset':c,'finite_seed_black':black,'endpoint_initial_color':'R','endpoint_prior_reads':counts.get(p,0),'endpoint_first_coset_read':'L' if counts.get(p,0)%2 else 'R'}
a,b=map(replay,(LONG,SHORT))
assert a['length']==50 and b['length']==10
assert a['pose']==b['pose']==[1,-1,0]
assert a['reduced_word']==b['reduced_word']==SHORT
assert a['canonical_coset']==b['canonical_coset']
assert a['finite_seed_black']==[]
assert a['endpoint_first_coset_read']=='L' and b['endpoint_first_coset_read']=='R'
out={'status':'PASS','long_blank_witness':a,'short_finite_seed_witness':b}
print(json.dumps(out,indent=2));(P/'static_lift_gauge_obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
