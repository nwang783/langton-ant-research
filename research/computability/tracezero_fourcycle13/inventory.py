#!/usr/bin/env python3
"""Exact independent-image inventory for the spectral theorem's four-cycle escape."""
import itertools,json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0));k=13
def check(w,h):
 p=(0,0);need={};last={}
 for d in w:
  bit=int((d-h)%4==3)
  if p in need and need[p]!=bit:return False
  need[p]=1-bit;p=(p[0]+D[d][0],p[1]+D[d][1]);h=d
 return True
base=[];raw=0
# Source N maps under A=3*counterclockwise rotation to W. F is that rotation.
for west in itertools.combinations(range(7),5):
 if 0 not in west:continue
 for north in itertools.combinations(range(6),3):
  w=tuple((3 if j//2 in west else 1) if j%2==0 else (0 if j//2 in north else 2) for j in range(k))
  raw+=1
  heads=[h for h in (0,2) if check(w,h)]
  if heads:base.append(dict(word=w,heads=heads))
assert raw==300
domains=[]
for d in range(4):
 domains.append([dict(word=[(z+d)%4 for z in r['word']],heads=[(h+d)%4 for h in r['heads']]) for r in base])
out=dict(matrix=[[0,-3],[3,0]],k=k,first_map=[3,0,1,2],root=0,
 raw_per_direction=raw,legal_per_direction=len(base),domains=domains,
 last_counts={str(d):sum(r['word'][-1]==d for r in base) for d in (1,3)})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='domains'}))
