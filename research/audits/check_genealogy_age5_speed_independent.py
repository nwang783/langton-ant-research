"""Independent exact literal genealogy inequalities, root boundary, floor sums."""
from pathlib import Path
import json,hashlib
from fractions import Fraction
from check_dcuv_producer_model_independent import ROOT,geometry,rotation,xy
F=ROOT/'core_periodicity_new/genealogy_age5_speed_frozen_20261023_0827';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
A=json.loads((F/'genealogy_age5_speed.json').read_text());Q=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())
anchors={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};phi=(0,5,6,3);rows=[];checks=0
for h in range(4):
 for hh in range(4):
  for a,q in anchors.items():
   age=Q['slots'][f'{a}:{xy(q)}']['certified_minimum_C_age'];assert age==(3 if a in(0,1,4,5)else 5)
   n=next(t for t in range(age,age+4)if(t+hh-h)%4==0)
   for z in geometry[a]['outputs']:
    d=rotation(z-q,hh);dy=int(d.imag);margin=3*n+phi[h]-phi[hh]-4*dy;assert margin>=0
    for r in range(4):assert 4*int(rotation(d,r).imag)<=3*n+phi[(h+r)%4]-phi[(hh+r)%4];checks+=1
    rows.append({'parent_heading':h,'child_heading':hh,'packet':a,'output':list(xy(z)),'minimum_admitted_gap':n,'dy':dy,'margin':margin})
assert rows==A['rows'];constants=[]
for h0 in range(4):
 vals=[]
 for a,q in anchors.items():
  for h in range(4):
   b=(h0-h)%4
   vals.extend(4*int(rotation(z-q,h).imag)-3*b+phi[h]for z in geometry[a]['outputs'])
 constants.append(max(vals))
assert constants==[16,13,18,15]==[x['K']for x in A['initial_root_constants']]
# Exact floor arithmetic is reduced to the four residues, not sample extrapolation.
base=[2*((3*j+18)//4)+2 for j in range(4)];assert base==[10,12,14,14]
# Translation j->j+4 increases each summand by6. A q-block sum is
# 50q+24*q(q-1)/2 =12q²+38q, with 6q added for each residual entry.
assert sum(base)==50 and [0,base[0],sum(base[:2]),sum(base[:3])]==[0,10,22,36]
for r in range(4):
 assert (3*r+18)//4<=r+4
 assert (3*(r+4)+18)//4==((3*r+18)//4)+3
 # The difference j+4 minus R_(j+4) increases by one, proving radius dominance.
# Abstract speed cycle is explicitly checked for physical output/input sector only.
cycle=[(7,0j,0,2,6),(1,3+1j,2,3,3),(5,2+5j,3,0,3)];totaln=totaldy=0
for i,(a,z,h,hh,n) in enumerate(cycle):
 previous_output=cycle[(i-1)%len(cycle)][1];relative=(hh-h)%4;pose=previous_output-rotation(anchors[a],relative)
 assert (sum(xy(pose))+relative)%2==0
 assert z in geometry[a]['outputs']
 d=rotation(z-anchors[a],hh);assert int(d.imag)==3
 assert n>=Q['slots'][f'{a}:{xy(anchors[a])}']['certified_minimum_C_age']and(n+hh-h)%4==0
 totaln+=n;totaldy+=int(d.imag)
assert(totaln,totaldy)==(12,9)
out={'status':'PASS independent literal three-quarter ancestry speed and separate initial-root bound','produced_edges':len(rows),'rotated_inequalities':checks,'root_constants':constants,'root_radius':'floor((3*j+18)/4)','floor_block_weights':base,'exact_sum':'12*q^2+38*q+6*q*s+[0,10,22,36][s]','manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'scope':'Complete recurrent-eight factors. Initial identity edges handled separately, not assigned produced-age premises. No C upper bound, confinement or global capture.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
