"""Translation-invariant local interfaces for a zero-output ancestry rail.
Only enumerates the complete seven even flag-one canonical-face profiles.
The global periodicity contradiction is analytic, not a front scan.
"""
from pathlib import Path
from itertools import product
import ast,json
root=Path(__file__).parent
H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0))
cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
t=ast.parse((root/'canonical_three_child_square_closure.py').read_text())
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows']
even=[r for r in base if r['headings']['A']=='NNSN'and all(len(h)%2==0 for h in r['headings'].values())]
upper=[]
for r,q in product(even,(2,3)):
 hh,fs,e,bd=pose(r,(-1,1),q)
 if hh.get((0,1))!='SSNS':continue
 if hh.get((0,2)) not in ('EEEW','EWEE'):continue
 if fs.get((0,2))!=-2:continue
 if outs(hh[(0,2)]).count('S')!=3:continue
 # Retain both known k/j histories on the left child of the current D.
 hh[(1,1)]='EEWE';hh[(1,2)]='NNNS'
 ns=[(p,a)for p,h in hh.items()for a in range(len(h))];es=[]
 for p,h in hh.items():
  for a in range(len(h)-1):es.append(((p,a),(p,a+1),4))
  for o in 'NESW':
   dx,dy=V[o];v=(p[0]+dx,p[1]+dy)
   if v not in hh:continue
   aa=[(p,a)for a,x in enumerate(outs(h))if x==o];bb=[(v,a)for a,x in enumerate(hh[v])if x==o]
   assert len(aa)==len(bb)
   for a,b in zip(aa,bb):es.extend([(a,b,1),(b,a,-1)])
 d={n:0 for n in ns};cyclic=False
 for _ in ns:
  change=False
  for a,b,k in es:
   if d[b]<d[a]+k:d[b]=d[a]+k;change=True
  if not change:break
 else:cyclic=True
 upper.append(dict(profile=r['headings'],rotation=q,physical={str(p):h for p,h in hh.items()},heights={str(p):h for p,h in fs.items()},ordinal_time_cycle=cyclic))
R=[]
for r in even:
 hh,fs,e,bd=pose(r,(-1,-1),1)
 if hh.get((0,0))!='WWEW':continue
 if outs(hh[(0,-1)]).count('E')!=1 or hh[(-1,0)].count('S')!=1:continue
 if fs.get((-2,0))!=0:continue
 R.append(r)
pairs=[]
for r,d,q in product(R,even,(0,2,3)):
 rh,rf,re,rb=pose(r,(-1,-1),1);dh,df,de,db=pose(d,(-2,0),q)
 if dh.get((-1,1))!='EEWE'or dh.get((-1,0))!=rh[(-1,0)]:continue
 cyclic=q==0
 positive=(d['headings']==dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'))
 pairs.append(dict(R=r['headings'],R_physical={str(p):h for p,h in rh.items()},D=d['headings'],D_rotation=q,canonical_cycle=cyclic,positive_duplicator_profile=positive,survives=not cyclic and positive))
out=dict(scope=__doc__,even_canonical_profiles=len(even),upper_candidates=upper,upper_survivors=[r for r in upper if not r['ordinal_time_cycle']],R_profiles=len(R),candidate_pairs=len(pairs),cycle_rejections=sum(x['canonical_cycle']for x in pairs),nonduplicator_leaf_rejections=sum(not x['canonical_cycle']and not x['positive_duplicator_profile']for x in pairs),survivors=[x for x in pairs if x['survives']],pairs=pairs)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='pairs'},indent=2))
