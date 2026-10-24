"""Independent literal enumeration of all residual origins at the DC core shadow."""
import json,hashlib,itertools,collections
from pathlib import Path
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/dc_core_shadow_frozen_20261023_1007'
m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
j=json.loads((B/'dc_core_shadow_obstruction.json').read_text())
ids=(0,1,4,5,6,7,8,9)
K={z for z,b in walk(mark)[2].items()if b}
g={}
for a in ids:
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b};postK={e+rotation(z,h)for z in K}
 I=black-K;O=(black^flip)-postK
 assert postK <= (black^flip) and I.isdisjoint(K) and O.isdisjoint(postK)
 g[a]=(I,O,req,postK)
P=sorted(g[1][1],key=xy);z=2+1j
assert list(map(xy,P))==[(2,0),(2,3),(3,1),(3,2)]
assert z in g[1][3] and z not in g[1][1]
rows={};profiles=collections.Counter()
for a,(I,O,req,postK) in g.items():
 for output in O:
  for h in range(4):
   p=z-rotation(output,h)
   if (sum(xy(p))+h)%2:continue
   hits=[]
   for i,q in enumerate(P):
    local=rotation(q-p,-h)
    if local in req:
     role='input'if local in I else 'core'if local in K else 'white'if not req[local] else 'other_black'
     assert role!='other_black'
     hits.append((i,xy(q),xy(local),role))
   key=(a,xy(p),h,xy(output));assert key not in rows
   rows[key]=hits;profiles[tuple(t[0]for t in hits)]+=1
assert len(rows)==136
for r in j['all_sector_output_producers']:
 key=(r['producer'],tuple(r['pose'][:2]),r['pose'][2],tuple(r['output_slot']))
 assert rows.pop(key)==[(x['source_output_index'],tuple(x['source_cell']),tuple(x['producer_local_cell']),x['role'])for x in r['protected_source_hits']]
assert not rows
covers=[]
for n in range(1,5):
 for s in itertools.combinations(range(4),n):
  if all(set(s)&set(t)for t in profiles)and not any(set(t)<=set(s)for t in covers):covers.append(s)
assert covers==[(0,2),(0,3)]==[tuple(s)for s in j['minimal_protected_source_output_index_covers']]
assert {str(t):v for t,v in profiles.items()}==j['coverage_hitset_profile']
spares=set(P[1:]);targets=[]
for a in(7,8,9):
 I=g[a][0];poses={(s-rotation(q,h),h)for s in spares for q in I for h in range(4)}
 for p,h in poses:
  inputs={p+rotation(q,h)for q in I}
  if spares<=inputs:
   assert(p,h)==(3-1j,0)and inputs==set(P)|{z}
   targets.append((a,*xy(p),h))
assert len(targets)==3
out={'status':'PASS independent literal geometry, all producer placements, exact hit roles and minimal covers',
 'producer_placements':136,'minimal_covers':covers,'coverage_hitset_profile':{str(t):v for t,v in sorted(profiles.items())},
 'all_spare_U_targets':targets,'source_exit_core':sorted(map(xy,g[1][3])),
 'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),
 'scope':'All-age ordered-identity obstruction within a complete recurrent-eight interval. No individual transfer/age rule or global U bound.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
