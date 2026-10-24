"""Exact local arithmetic for a conditional complete-record-family theorem.
This script does NOT prove the missing V1/U1 record exclusions.
"""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent;gf=ROOT/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gf.read_text())['geometry'];A=[0,22,20,10];keep=[0,1,4,5,6,7,8,9]
def rot(q,h):
 x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
activation=[];prefix=[];packets=[]
for g in G:
 if g['packet']not in keep:continue
 for s in range(4):
  for q in g['inputs']:activation.append([2*sum(rot(q,s))-A[s],g['packet'],s,q])
 x=y=h=0
 for k,t in enumerate(g['word']):
  for s in range(4):prefix.append([2*sum(rot((x,y),s))-A[s],g['packet'],s,k,[x,y]])
  h=(h+(3 if t=='L'else 1))%4;dx,dy=rot((0,1),h);x+=dx;y+=dy
 assert[x,y,h]==g['endpoint']
 nm=g['name'];d=int(nm.startswith('D'));vv=int(nm.startswith('V'));u=int(nm.startswith('U'));c=nm.count('C')
 assert len(g['word'])==10*d+18*vv+28*u+15*c
 assert g['mass_change']==4*(vv+u)+3*c
 packets.append(dict(packet=g['packet'],name=nm,length=len(g['word']),D=d,V=vv,U=u,C=c,mass_change=g['mass_change']))
out={'status':'CONDITIONAL ARITHMETIC ONLY: requires all13 funding-aware strict record event exclusions, of which11 are signed at2026-10-23 04:59 UTC.','geometry_sha256':hashlib.sha256(gf.read_bytes()).hexdigest(),'core_offsets':A,'minimum_initial_weight':28,'activation_offset_max':max(activation),'shifted_raw_prefix_max':max(prefix),'packet_arithmetic':packets,'formulae':{'activation_jump':'K=I+6','raw_radius':'R=ceil(18+(I+6)*(m-5)/2)','non_D_macro_bound':'t=floor((2*R+1)^2/3)','raw_duration_bound':'20*R*(t+1)+28*t'},'example_only_I48':'R=18+27*(m-5), not asserted sufficient for currently open cases.'}
path=ROOT/'chronology_dcuv/record_conditional_constants.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='packet_arithmetic'},indent=2))
