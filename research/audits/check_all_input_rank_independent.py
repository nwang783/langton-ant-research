"""Independent literal input counts, historical graph identities, and abstract cactus control."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
F=ROOT/'cut_order_obstruction_2026-10-23/mass_sensitive/all_input';M=json.loads((F/'manifest.json').read_text())
for name,digest in M['files'].items():assert hashlib.sha256((F/name).read_bytes()).hexdigest()==digest
K={z for z,b in walk(mark)[2].items()if b};counts={}
for a in(0,1,4,5,6,7,8,9):
 B={z for z,b in walk(raws[a]+mark)[2].items()if b};e,h,_,fl=walk(raws[a]);O=(B^fl)-{e+rotation(z,h)for z in K};counts[a]=(len(B-K),len(O))
assert counts=={0:(1,1),1:(1,4),4:(2,6),5:(2,9),6:(2,12),7:(5,9),8:(5,12),9:(5,15)}
# Exact role counts are used here only as an explicitly nonphysical resource model.
N=768;live={complex(0,10*r):r for r in range(8)};adj={r:set()for r in range(8)};owner={r:r for r in range(8)};born={r:None for r in range(8)};serial=8;E=0;ops=0;age_inputs=0;multi=0
for clock in range(N):
 r=clock%8;n=clock//8;x=4*n;y=10*r
 actions=[]
 if n:
  b=x-4;actions=[(4,[complex(b,y+1),complex(b+1,y+1)],[complex(b,y),complex(b+1,y),complex(b+2,y),complex(b+3,y),complex(b,y+2),complex(b+1,y+2)]),(0,[complex(b+2,y+1)],[complex(b+2,y+2)])]
 actions.append((1,[complex(x,y)],[complex(x+4,y),complex(x,y+1),complex(x+1,y+1),complex(x+2,y+1)]))
 for a,I,O in actions:
  assert tuple(map(len,(I,O)))==counts[a];iv=[live.pop(q)for q in I];assert{owner[v]for v in iv}=={r}
  for q,v in zip(I,iv):
   if born[v]is not None:assert clock-born[v]==8;age_inputs+=1
   assert all(max(abs((z-q).real),abs((z-q).imag))<=4 for z in O)
  pn=serial;serial+=1;adj[pn]=set(iv)
  for v in iv:adj[v].add(pn)
  for q in O:
   assert q not in live;v=serial;serial+=1;live[q]=v;adj[v]={pn};adj[pn].add(v);owner[v]=r;born[v]=clock
  E+=len(I)+len(O);ops+=1;multi+=a==4
 assert len(live)==8+3*(clock+1)+4*max(clock+1-8,0)
 # Full-current radius, including every dormant output.
 bound=(2*(clock+1)+13)//3
 for q,v in live.items():assert max(abs(q.real),abs(q.imag-10*owner[v]))<=bound
seen=set();components=[]
for v in adj:
 if v in seen:continue
 stack=[v];seen.add(v);vs=[];degree=0
 while stack:
  u=stack.pop();vs.append(u);degree+=len(adj[u])
  for z in adj[u]:
   if z not in seen:seen.add(z);stack.append(z)
 components.append(dict(vertices=len(vs),edges=degree//2,beta=degree//2-len(vs)+1))
assert len(components)==8 and E-len(adj)+8==multi==N-8
# Arithmetic shortcut, checked on a grid as a guard on constants; monotonicity
# and the incidence identity provide the all-integer argument in the note.
for m in range(6,55):
 for B in range(50):
  u=(B+m-6)//4;b=57+38*(m-5)+60*u;assert b<=53*m+15*B-223
out=dict(status='PASS literal input multiplicities, exact historical graph identity and abstract aged cactus construction',manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),literal_counts=counts,abstract_rounds=N,abstract_packets=ops,age8_inputs=age_inputs,components=components,beta=multi,scope='Bounded historical beta implies a cubic duration/confinement bound via signed HS in ACTUAL complete recurrent-eight factors. No beta bound proved. The fixed-eight-root cactus is only an abstract resource model, not literal masks/head transport.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
