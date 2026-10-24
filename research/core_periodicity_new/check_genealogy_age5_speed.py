"""Author exact arithmetic controls for the age-five genealogy speed corollary."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;gp=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];A={0:3,1:3,4:3,5:3,6:5,7:5,8:5,9:5};P={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)};phi=[0,5,6,3]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
rows=[]
for h in range(4):
 for hh in range(4):
  for a in A:
   n=A[a]+((h-hh-A[a])%4)
   for o in G[a]['outputs']:
    dx,dy=rot((o[0]-P[a][0],o[1]-P[a][1]),hh);margin=3*n+phi[h]-phi[hh]-4*dy;assert margin>=0
    for r in range(4):
     ddy=rot((dx,dy),r)[1];assert 4*ddy<=3*n+phi[(h+r)%4]-phi[(hh+r)%4]
    rows.append(dict(parent_heading=h,child_heading=hh,packet=a,output=o,minimum_admitted_gap=n,dy=dy,margin=margin))
roots=[]
for hi in range(4):
 mx=-999;att=[]
 for hh in range(4):
  b=(hi-hh)%4
  for a,p in P.items():
   for o in G[a]['outputs']:
    dx,dy=rot((o[0]-p[0],o[1]-p[1]),hh);v=4*dy-3*b+phi[hh]
    if v>mx:mx=v;att=[]
    if v==mx:att.append([hh,b,a,o])
 roots.append(dict(entry_heading=hi,K=mx,attaining_cases=att));assert mx<=18
qsum=0
for k in range(10001):
 R=(3*k+18)//4;assert R<=k+4
 qsum+=2*R+2
 q,s=divmod(k+1,4);formula=12*q*q+38*q+6*q*s+[0,10,22,36][s];assert formula==qsum
O=dict(status='AUTHOR_EXACT_ARITHMETIC_PASS_NOT_INDEPENDENT',scope='Complete recurrent-eight factors; JO minima3 plus independently signed KV age5 for VCC and upperU*. No age4 monotonicity inference for D/V. No confinement.',geometry_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),chosen_inputs={str(a):p for a,p in P.items()},required_minimum_ages=A,potential=phi,produced_edge_cases=len(rows),all_four_rotations_checked=4*len(rows),rows=rows,initial_root_constants=roots,uniform_root_radius='floor((3*k+18)/4)',epoch_packet_count='(m-5)*(2*floor((3*j+18)/4)+2)',duration='28*(m-5)*(12*q^2+38*q+6*q*s+[0,10,22,36][s])+15*k; q=floor((k+1)/4), s=(k+1) mod4',coarse_duration='7*(m-5)*(k+1)*(3*k+44)+15*k',checked_duration_k=10001)
(W/'chronology_dcuv/genealogy_age5_speed.json').write_text(json.dumps(O,indent=2)+'\n');print({k:v for k,v in O.items()if k not in ['rows','initial_root_constants']})
