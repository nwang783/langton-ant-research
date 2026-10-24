from verify_macro_word import D,rot
import json
from pathlib import Path
marks={a:set(map(tuple,v))for a,v in json.load(open(Path(__file__).with_name('cfree_spatial_kernel_fresh_sites.json'))).items()}
seam={(0,0),(-1,-1),(0,-1),(1,0)}
for a in'UVQBC':
 first={}
 for z in D[a]['trace']:first.setdefault(tuple(z['p']),z['c'])
 assert{q for q,c in first.items()if c=='L'}==seam|marks[a]
 assert not(seam&marks[a])
 if a!='C':
  p=D[a]['end_pose'];last={tuple(z['p']):z['c']for z in D[a]['trace']}
  for q in seam:
   x,y=rot(q,p[2]);assert last[(p[0]+x,p[1]+y)]=='R'
 print(a,'nonseam first-L count',len(marks[a]))
print('Exact fuel accounting passed.')
