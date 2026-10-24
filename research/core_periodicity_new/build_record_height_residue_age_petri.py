"""High residual height/transverse-residue/C-age multiset overapproximation.

CLI FULL_HEIGHT_PETRI.json PREFIX MODULUS [PLACES.json].
Every source residue is synchronized across all inputs, outputs and movement.
Unretained places are unlimited resources, never zero-count assumptions.
"""
from pathlib import Path
import sys,json,hashlib

src,out=map(Path,sys.argv[1:3]);mod=int(sys.argv[3]);assert mod>=2 and mod%2==0
J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text())
gp=Path('chronology_dcuv/literal_residual_geometry.json');G=json.loads(gp.read_text())['geometry']
rp=Path('chronology_dcuv/counted_input_age_rules_complete.json')
ages={(a,x,y):r for a,x,y,r in json.loads(rp.read_text())}
phase=S['phase'];F=J['initial_bound'];target=S['target']
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coords(p):
 x,y=rot(p,phase);return x+y,x-y
if len(sys.argv)>4:
 places=[tuple(v)for v in json.loads(Path(sys.argv[4]).read_text())]
else:
 places=sorted({(q,t%mod)for p in G[target]['inputs']for q,t in [coords(p)]if q>F})
assert len(set(places))==len(places)
assert all(F<q<=J['height_cap'] and 0<=t<mod for q,t in places)
idx={v:i for i,v in enumerate(places)};m=len(places)
positions=[]
for p,(pi,d)in enumerate(J['positions']):
 h,q=J['poses'][pi]
 for tr in range(h%2,mod,2):positions.append((p,tr))
pid={v:i for i,v in enumerate(positions)}
def op(pi,tr,a):
 h,q=J['poses'][pi];I=[0]*(5*m);O=[0]*m;c=G[a]['name'].count('C')
 if q is not None:
  for p in G[a]['inputs']:
   dq,dt=coords(rot(p,h));z=(q+dq,(tr+dt)%mod)
   if z in idx:
    k=idx[z];r=ages[a,*p]
    for j in range(r+1):I[5*k+j]+=1
  for p in G[a]['outputs']:
   dq,dt=coords(rot(p,h));z=(q+dq,(tr+dt)%mod)
   if z in idx:O[idx[z]]+=1
 return c,I,O
ops={};edges=[]
for p,q,a,_,_ in J['transitions']:
 pi=J['positions'][p][0];h=J['poses'][pi][0]
 dt=coords(rot(G[a]['endpoint'][:2],h))[1]
 for tr in range(h%2,mod,2):
  rr=(tr+dt)%mod;assert(q,rr)in pid
  c,I,O=ops.setdefault((pi,tr,a),op(pi,tr,a))
  edges.append((pid[p,tr],pid[q,rr],a,c,I,O))
goals=[]
for p,_ in J['goal_requirements']:
 pi=J['positions'][p][0];assert J['poses'][pi]==[0,0]
 c,I,O=ops.setdefault((pi,0,target),op(pi,0,target))
 goals.append((pid[p,0],I))
initial=[pp for pp,(p,tr)in enumerate(positions)if p in set(J['initial_controls'])]
N=dict(format='record_height_residue_age_petri_v1',source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),geometry_file=str(gp.resolve()),geometry_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),rules_file=str(rp.resolve()),rules_sha256=hashlib.sha256(rp.read_bytes()).hexdigest(),phase=phase,modulus=mod,places=places,age_cap=4,initial_controls=initial,goal_requirements=goals,positions=positions,base_positions=J['positions'],poses=J['poses'],operations=[[pi,tr,a,c,I,O]for(pi,tr,a),(c,I,O)in ops.items()],transitions=[[p,q,a]for p,q,a,_,_,_ in edges],scope='Current residual counts at selected exact heights above F and exact transverse residues modulo M, split by saturated C-age0..4. Tail counts use age>=j. One source residue synchronizes every input, output and head movement. Initial high counts are zero. Unselected places are unlimited, and white/core consistency is forgotten. Overapproximation only; no ant witness or exclusion without independent reconstruction and an exhaustive certificate.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{m} {len(positions)} {len(edges)} {len(initial)} {len(goals)}\n')
 f.write(' '.join(map(str,initial))+'\n')
 for p,r in goals:f.write(' '.join(map(str,[p]+r))+'\n')
 for p,q,a,c,I,O in edges:f.write(' '.join(map(str,[p,q,a,c]+I+O))+'\n')
print(dict(places=places,tail_coordinates=5*m,modulus=mod,controls=len(positions),edges=len(edges),initial=len(initial),goals=len(goals)))
