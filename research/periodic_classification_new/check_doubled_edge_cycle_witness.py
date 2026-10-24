#!/usr/bin/env python3
"""Exact replay of one finite counterexample; no exhaustive exclusion claim."""
from collections import defaultdict
import json
seed={(-2,0),(-2,1),(-2,3),(-1,3)}
word='RRRRLRRRRLRRLRRLRRLLRRRRLLRRLRRLRRLRRRRLRRRRLLL'
cycle=[(0,2),(-1,2),(-1,1),(0,1)]
D=((0,1),(1,0),(0,-1),(-1,0))
black=set(seed); reads=defaultdict(list); edges=defaultdict(list); p=(0,0); h=0
for t,c in enumerate(word):
    assert c==('L' if p in black else 'R'),(t,p,c)
    reads[p].append((t,c,'NESW'[h])); assert len(reads[p])<=3,(t,p)
    black.symmetric_difference_update({p})
    h=(h+(1 if c=='R' else -1))%4; dx,dy=D[h]; q=(p[0]+dx,p[1]+dy)
    edges[p,q].append(t); p=q
assert len(word)==47 and p==(0,3) and len(reads[p])==3
assert not (set(cycle)&seed)
rows=[]
for v,q in zip(cycle,cycle[1:]+cycle[:1]):
    assert ''.join(e[1] for e in reads[v])=='RLR'
    assert reads[v][0][2]!=reads[v][2][2]
    assert len(edges[v,q])==2
    rows.append(dict(cell=v,reads=reads[v],next=q,crossings=edges[v,q]))
out=dict(verified=True,scope='one finite 47-read prefix, not an infinite or periodic front',seed=sorted(seed),word=word,cycle=rows,next_read_would_be_fourth=dict(position=p,turn='L' if p in black else 'R'))
print(json.dumps(out,indent=2))
