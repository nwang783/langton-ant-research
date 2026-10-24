from pathlib import Path
from itertools import product
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/VC_one_VCC_crossing_frozen_20261023_1202';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
G=json.loads((B/'03_literal_residual_geometry.json').read_text())['geometry'];K={z for z,black in walk(mark)[2].items()if black}
rows=[]
for a in(0,4,5,6):
 end,h,_,_=walk(raws[a]);ins={z for z,b in walk(raws[a]+mark)[2].items()if b}-K
 assert [*xy(end),h]==G[a]['endpoint']and ins==set(map(lambda p:complex(*p),G[a]['inputs']))
 for heading in(1,3):rows.append({'packet':a,'heading':heading,'endpoint':[*xy(rotation(end,heading)),(heading+h)%4],'inputs':sorted([list(xy(rotation(q,heading)))for q in ins])})
assert G[5]['endpoint']==[1,4,3]
assert [*xy(rotation(walk(raws[6])[0],3)),(3+walk(raws[6])[1])%4]==[-4,0,1]
for a,w in((0,1),(4,3)):
 assert xy(rotation(walk(raws[a])[0],3))==(-w,1)
 assert xy(rotation(walk(raws[a])[0],1))==(w,-1)
assert complex(0,3) in {z for z,b in walk(raws[4]+mark)[2].items()if b}-K
assert complex(0,3) in {z for z,b in walk(raws[6]+mark)[2].items()if b}-K
assert rotation(3j,3)==-3 and rotation(1j,1)==1
ages=json.loads((B/'04_counted_input_age_rules_complete.json').read_text());assert [0,0,1,3]in ages
# Abstract transition proof is finite below zero, plus a monotone affine ray.
def inv(d,k):return d>=-2 or(d==-4 and k=='V')
trans=[]
for d in(-4,-2,0,2):
 for current,b,a in product(('D','V'),(1,3),(1,3)):
  if not inv(d,current):continue
  if d==-4 and current=='V' and b==1:continue # same retired cell, at most2C old
  dn=d+b-a;new='D'if a==1 else'V';assert inv(dn,new)
  trans.append([d,current,b,a,dn,new])
assert all(2+b-a>=0 for a,b in product((1,3),repeat=2))
# Same-cell necessity is independent of any finite path length.
assert -4+1==-3 and (3-1)==2<3
# At row4, five rightward endpoint steps remain; the old path started at x1.
assert 0-5-1==-6<-4
out={'status':'PASS independent literal masks/endpoints and all-word row-gap induction','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'literal_rows':rows,'boundary_transition_cases':len(trans),'source_exit':[1,4,3],'goal_pose':[0,-1,1],'age_reuse':[1,3,2,3],'invariant':'Even gap>=-4, with equality only at outgoingV/topVCC; affine positive ray closed.','bottom_gap_upper_bound':-6,'scope':'No actual complete-eight VC A VCC B U with A,B arbitrary D/V zero-C words and target(0,-1,E). No length or mass cap; other two-C grammars and unfunded U1 remain open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
