"""Literal arithmetic for the boundary-origin height guard; no state search."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];keep=[0,1,4,5,6,7,8,9]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def H(z):return z[1]-z[0]
rows=[]
for a in keep:
 delta=[max(H(rot(z,h))for z in G[a]['outputs'])-max(H(rot(z,h))for z in G[a]['inputs'])for h in range(4)]
 rows.append(dict(packet=a,name=G[a]['name'],max_output_minus_max_input_height=delta));assert max(delta)<=4
kappa=[];sources=[]
for h in range(4):
 hs=(h+3)%4;offset=rot((-1,0),h);pofs=H(offset);vals=[]
 for a in[4,5,6]:
  assert G[a]['inputs']==[[0,3],[1,2]] and [1,0]in G[a]['outputs']and [2,0]in G[a]['outputs']
  u=[pofs+H(rot(z,hs))for z in G[a]['inputs']];vals.append(max(u));sources.append(dict(consumer_heading=h,source=a,source_head_offset=offset,source_heading=hs,source_input_height_offsets=u))
  # The literal source outputs are exactly target lower a/q at these relative poses.
  for o,z in[([1,0],[-1,1]),([2,0],[-1,2])]:
   q=rot(o,hs);assert(offset[0]+q[0],offset[1]+q[1])==rot(z,h)
 assert len(set(vals))==1;kappa.append(vals[0])
assert kappa==[4,4,-4,-2]
J=dict(status='AUTHOR_BOUNDARY_ORIGIN_HEIGHT_GUARD_ARITHMETIC_PASS',scope='Analytic corollary of independently signed first-producer q3 boundary theorem plus lower-pair equivalence. Bounds only initial identities actually consumed in the factor, not unused initial black cells. No new U1/V1 exclusion or model closure.',all_first_packet_output_deltas=rows,U_young3_initial_input_offsets=sources,kappa=kappa,U1_F_minus10_young3_head_height_caps=[-10-z for z in kappa],dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,W/'U_young3_boundary_frozen_20261023_1230/manifest.json',W/'u_lower_pair_equivalence_frozen_20261023_1146/manifest.json',Path(__file__).resolve()]})
(W/'chronology_dcuv/boundary_origin_height_guard.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(dict(first_output_delta_max=4,kappa=kappa,Fminus10_caps=J['U1_F_minus10_young3_head_height_caps']),indent=2))
