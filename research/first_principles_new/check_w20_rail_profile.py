#!/usr/bin/env python3
"""Exact all-epoch chronology for one westbound solid-rail rewrite."""
import json
from collections import defaultdict
from pathlib import Path
W='LLRLRRRRLRRRRLLLLRLL'
D=[(0,1),(1,0),(0,-1),(-1,0)]
x,y,h=1,0,1
reads=[]
for i,a in enumerate(W):
    reads.append((i,x,y,a))
    h=(h+(1 if a=='R' else -1))%4
    dx,dy=D[h]; x+=dx; y+=dy
assert (x,y,h)==(-1,0,1)
# At a fixed physical cell, period index is (x_i-X)/2, so
# chronological order is 20*(x_i-X)/2+i, hence 10*x_i+i.
classes=defaultdict(list)
for i,x,y,a in reads:
    classes[(x%2,y)].append((10*x+i,i,x,a))
out=[]
for (r,y),entries in sorted(classes.items()):
    entries.sort()
    word=''.join(e[3] for e in entries)
    assert all(a!=b for a,b in zip(word,word[1:]))
    expected={0:'L',1:'RLRL',2:'RLRL',3:'R'}[y]
    assert word==expected
    before=int(word[0]=='L'); after=before^(len(word)%2)
    out.append({'x_mod_2':r,'row':y,'ordered_reads':word,
                'input_black':before,'output_black':after,
                'ordering_keys':[e[0] for e in entries]})
assert len(out)==8
result={'word':W,'period':len(W),'entry_pose':[1,0,1],
        'heading_convention':['N','E','S','W'],'drift':[-2,0],
        'pose_sector':0,'classes':out,'pass':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
