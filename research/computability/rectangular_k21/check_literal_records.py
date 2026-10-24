#!/usr/bin/env python3
"""Different, recursive Python generation checks deterministic samples of records."""
from pathlib import Path
import array,hashlib,itertools,json,random,sys
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]/'causal_reduction'/'matrix_candidates'))
from search_rectangular_direction_morphisms import replay
inv=json.loads((HERE.parents[1]/'causal_reduction'/'matrix_candidates'/'rectangular_inventory_k21_3_7.json').read_text())
E=[r[0] for r in inv['E']];N=[r[0] for r in inv['N']]
rec=array.array('H')
for f in ['first10000.u16','remainder.u16']:rec.frombytes((HERE/f).read_bytes())
assert len(rec)==4*len(E)*len(N)==25616960
assert max(rec)==717 and 65535 not in rec
rng=random.Random(202610230026)
cases=set(rng.sample(range(len(rec)),10000))
cases.update(range(40));cases.update(range(39980,40020));cases.update(range(len(rec)-40,len(rec)))
cases.update(i for i,t in enumerate(rec) if t==717)
def letters(im,d,depth):
 if not depth:yield d
 else:
  for q in im[d]:yield from letters(im,q,depth-1)
for i in sorted(cases):
 p,case=divmod(i,4);ie,jn=divmod(p,len(N));root=1 if case<2 else 0
 h=(root+(3 if case%2==0 else 1))%4
 im={1:E[ie],0:N[jn],3:[(d+2)%4 for d in E[ie]],2:[(d+2)%4 for d in N[jn]]}
 r=replay(letters(im,root,4),h,10000)
 assert r['status']=='CONFLICT' and r['time']==rec[i],(i,r,rec[i])
hashes={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in HERE.iterdir() if f.suffix in ['.cpp','.txt','.u16','.jsonl','.json']}
out=dict(status='ALL CHECKED RECORDS MATCH',cases=len(rec),sampled=len(cases),maximum_conflict=717,byte_order=sys.byteorder,case_order='pair=east*north_count+north; root E headings N,S; root N headings W,E',hashes=hashes)
(HERE/'literal_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
