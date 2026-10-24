"""Sanity control for the exact permutation conjugacy, not an ant/front search.
The proof is all-size. One16-event cycle has two interleaved source pairs;
their target pairs are EXACT successor images. No physical realization claimed.
"""
from pathlib import Path
import json
n=16;sigma=[(i+1)%n for i in range(n)];source=[(0,8),(4,12)];target=[(sigma[a],sigma[b])for a,b in source]
def trans(pairs):
 q=list(range(n))
 for a,b in pairs:q[a]=b;q[b]=a
 return q
def compose(p,q):return[p[q[i]]for i in range(n)]
def cycles(p):
 seen=set();out=[]
 for i in range(n):
  if i not in seen:
   c=[];j=i
   while j not in seen:seen.add(j);c.append(j);j=p[j]
   out.append(c)
 return out
S=trans(source);T=trans(target);partial=compose(compose(S,T),sigma);conjugate=compose(compose(S,sigma),S)
assert partial==conjugate and len(cycles(partial))==1
out=dict(scope=__doc__,sigma=sigma,source_pairs=source,target_pairs=target,S=S,T=T,partially_repaired=partial,conjugate=conjugate,cycles=cycles(partial))
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print('PASS exact all-pair conjugacy control, one event cycle retained')
