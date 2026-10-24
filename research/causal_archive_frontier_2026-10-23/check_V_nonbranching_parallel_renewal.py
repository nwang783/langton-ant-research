"""Literal selected C-port rail algebra and exact renewal constants."""
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
roles={4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def mu(p,h):return sum(p)+(3 if h==0 else -3)
C=(2,1);rows=[]
for a,i in roles.items():
 assert i in set(map(tuple,G[a]['inputs'])) and sum(i)==3
 for h in(0,2):
  p=sub(C,rot(i,h));assert mu((0,0),0)==mu(p,h)==sum(C)
  b=4 if a in(4,5,6) else 7
  delta=(1,3)if b==4 else(0,4)
  # Corrected center in doubled coordinates and base increment.
  entry=add((2*p[0],2*p[1]),rot((-1,-1),h))
  out=add(entry,rot((2*delta[0],2*delta[1]),h))
  assert sum(out)==2*mu(p,h)
  assert(out[0]-out[1])%4==0
  rows.append(dict(consumer=G[a]['name'],selected=i,head=[*p,h],head_sum=sum(p),mu=mu(p,h),base_exit_doubled=out))
# Rotation of an arbitrary axis gives the same chart calculation. Coordinate
# sum of each physical support cell is odd in the chart (h N/S has even sum).
for h in(0,2):
 p=(4,2)if h==0 else(2,10)
 assert sum(p)%2==0
 q=add(p,rot(C,h));assert sum(q)==mu(p,h)and sum(q)%2
E=list(range(2,295,2));A=4851+3*len(E)
assert len(E)==147 and A==5292 and 2*A==10584
assert len(E)+1+len(E)==295
for m in range(1,200):
 assert 4851*m+3*(m+292)==4854*m+876
for L in range(1,100):
 assert 294*(L-1)+1>0
# Distinct even normal coordinates of L actual base exits force span2(L-1).
for L in range(1,100):
 ts=list(range(0,2*L,2));assert ts[-1]-ts[0]==2*(L-1)
D=[ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',HERE/'U_sink_V_renewal_manifest.json',HERE/'parallel_transport_manifest.json',HERE/'perpendicular_manifest.json',HERE/'manifest.json']
out=dict(status='AUTHOR_NONBRANCHING_V_RAILS_PENDING_INDEPENDENT_AUDIT',scope='Actual U-entry complete-eight selected production graph. Candidate transfer poses are not reachability assertions.',rows=rows,even_ages=E,constant=A,
 reproduction='v_j+u_j<=5292+sum_even2..294 v_(j-e)',total='N_j<=5292+sum_even2..294 v_(j-e)+v_(j-4)+u_(j-6)',
 bounded_V='v<=M eventually implies N<=10584+295M eventually',block='sum(v+u)<=4854m+876+sum_padded_source v',
 conserved_rail='mu=x+y+3s; all support cells and actual V/U base-exit centers lie on x+y=mu',
 bounded_V_depth='if each parallel path has at most L V vertices, v_j<=r0+5292[294(L-1)+1]',
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'V_nonbranching_parallel_renewal_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','constant','bounded_V','conserved_rail')},indent=2))
