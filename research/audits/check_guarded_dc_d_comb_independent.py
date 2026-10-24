"""Independent symbolic-index and literal-guard control of FREE core relocation.
This does not join actual packet endpoints and is intentionally not an ant.
"""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
F=ROOT/'core_periodicity_new/dc_d_guarded_comb_frozen_20261023_0935';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
K={z for z,b in walk(mark)[2].items()if b};G={}
for a in(0,1):
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b};post={e+rotation(z,h)for z in K};G[a]=(e,h,req,flip,black-K,(black^flip)-post,post)
assert G[1][5]=={2+0j,2+3j,3+1j,3+2j}and G[0][5]=={2+0j}
buds={2+3j,3+1j,3+2j}
# Exact formal all-integer index intersections, not a depth cutoff.
for a,head,h in[(1,0j,0),(0,1+0j,1)]:
 ctx={head+rotation(z,h):b for z,b in G[a][2].items()};hits=[]
 for z in ctx:
  for b in buds:
   t=int((z-b).real)
   if(z-b)==t*(1-3j):hits.append((z,b,t));assert a==1 and t==0 and not ctx[z]
 assert len(hits)==(3 if a==1 else 0)
assert min(3*z.real+z.imag for a,p,h in[(1,0j,0),(0,1+0j,1)]for z in[p+rotation(q,h)for q in G[a][2]])==-4
assert max(3*z.real+z.imag for a,p,h in[(1,0j,0),(0,1+0j,1)]for z in[p+rotation(q,h)for q in G[a][2]])==11
roots=[rotation(complex(100+10*(r//4),-100+((-r)%4)%2),(-r)%4)for r in range(12)]
res={p+rotation(1j,(-r)%4):(None,r)for r,p in enumerate(roots)};previous=None;events=0;Dages=[];DCages=[]
for clock in range(1500):
 actions=[]
 if clock>=7:actions.append((0,(clock-7)%12,(clock-7)//12))
 actions.append((1,clock%12,clock//12))
 for a,r,generation in actions:
  baseh=(-r)%4;base=roots[r]+rotation(generation*(1-3j),baseh);p=base+(rotation(1,baseh)if a==0 else 0);h=(baseh+int(a==0))%4
  assert h==(-clock)%4 and(sum(xy(p))+h)%2==0
  if previous is not None:assert(p,h)!=previous
  e,dh,req,flip,I,O,post=G[a];core={p+rotation(z,h)for z in K};assert core.isdisjoint(res)
  board=set(res)|core
  for z,b in req.items():assert((p+rotation(z,h))in board)==b
  for z in I:
   born,owner=res.pop(p+rotation(z,h));assert owner==r
   if born is not None:
    age=clock-born;assert age==(7 if a==0 else 5);(Dages if a==0 else DCages).append(age)
  for z in O:
   q=p+rotation(z,h);assert q not in res;res[q]=(clock,r)
  after=board^{p+rotation(z,h)for z in flip};postcore={p+rotation(z,h)for z in post}
  assert postcore.isdisjoint(res)and after==set(res)|postcore
  previous=(p+rotation(e,h),(h+dh)%4);events+=1
 assert len(res)==12+3*(clock+1)
# Marginal transfers checked against our separately reconstructed full role graph.
import check_genealogy_saturation_roles_independent as R
for h in range(4):
 u=R.index[1,2+0j,h];v=R.index[0,2+0j,(h+1)%4];assert any(a==u and b==v and n==7 for a,b,n,d in R.fundamental)
 u=R.index[0,2+0j,(h+1)%4];v=R.index[1,2+0j,h];assert any(a==u and b==v and n==5 for a,b,n,d in R.fundamental)
out=dict(status='PASS symbolic-index and literal guarded FREE-CORE-RELOCATION control',manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),checked_DC_events=1500,checked_packets=events,current_residuals=len(res),DC_to_D_age=7,D_to_DC_age=5,scope='Every packet individually obeys full raw+marker guards and exact XOR, both core boundaries avoid all current residuals. All junctions deliberately violate actual endpoint continuity. NOT a physical word, full trajectory, DCV counterexample, or global seed construction.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
