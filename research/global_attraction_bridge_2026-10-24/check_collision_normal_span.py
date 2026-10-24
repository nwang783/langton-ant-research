"""Exact endpoint-normal span of completed empty-reference collision macros.
This is a finite certificate for an all-time geometric inequality, not a scan.
"""
import json, hashlib
from pathlib import Path
from blank_collision_operator import C,H,CP,HP,DR,CE,CH,geometry,rotate,D,next_collision,materialize
P=Path(__file__).parent
NORMALS=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

def dot(n,q): return n[0]*q[0]+n[1]*q[1]
def replay(B,p,h,w):
 B=set(B)
 for a in w:
  assert (p in B)==(a=='L'),(p,h,a)
  B.symmetric_difference_update([p]);h=(h+(1 if a=='R' else -1))%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 return B,p,h

# Physical prefix verification; the previously signed infinite tail is a dependency.
B,p,h=replay(set(),(0,0),0,C)
B2,p2,h2=replay(B,p,h,H)
assert p==CE and h==CH and tuple(p2[i]-p[i] for i in range(2))==DR and h2==h
rows=[]
for n in NORMALS:
 a=max(dot(n,q) for q in CP)
 high=max(dot(n,q) for q in HP)
 low=min(dot(n,q) for q in HP)
 delta=dot(n,DR)
 K=max(0,a,high) if delta<=0 else max(0,a,high-low)
 assert K>=1
 # Prefix endpoint proof is immediate from a. For a positive drift, the
 # difference of any two tail phases is bounded by high-low; at nonpositive
 # drift the whole tail stays below high. Enumerate exactly those finite
 # inequalities, not a finite range of periods.
 assert all(dot(n,q)<=K for q in CP)
 if delta<=0: assert all(dot(n,q)<=K for q in HP)
 else:
  assert all(dot(n,q)-dot(n,r)<=K for q in HP for r in HP)
 rows.append(dict(normal=n,prefix_max=a,tail_max=high,tail_min=low,
                  tail_drift_projection=delta,endpoint_span=K))
axis=max(r['endpoint_span'] for r in rows[:4]);diagonal=max(r['endpoint_span'] for r in rows[4:])
assert(axis,diagonal)==(29,48)
# Rotation closure: all proper rotated normals stay in their class.
for n in NORMALS:
 for r in range(4): assert rotate(n,r) in NORMALS
# Huge flights verify that the emitted full field, not merely the head word,
# participates. All endpoints use the exact first-collision operator.
controls=[]
for h in range(4):
 for t in (0,3,9976,9977,9977+104*10**9+45):
  if t<len(C):q=CP[t]
  else:
   k,r=divmod(t-len(C),104);q=(HP[r][0]+k*DR[0],HP[r][1]+k*DR[1])
  x=rotate(q,h);z=next_collision([(x,(0,0),1)],(0,0),h)
  assert z['kind']=='collision'
  # It can hit the same input earlier than the intended t; use the actual endpoint.
  x=tuple(z['consumed_cell']);duration=z['blank_duration']
  for n in NORMALS:
   K=axis if 0 in n else diagonal
   upper=max(0,dot(n,x))+K
   assert dot(n,tuple(z['new_pose'][0]))<=upper
   for b,v,L in z['emitted_terms']:
    end=(b[0]+(L-1)*v[0],b[1]+(L-1)*v[1])
    # Each syntactic segment endpoint obeys the bound, so its full support does.
    assert max(dot(n,b),dot(n,end))<=upper
  controls.append(dict(heading=h,requested_reference_time=t,actual_collision_time=duration,
                       consumed_cell=x,terms=len(z['emitted_terms'])))
report=dict(status='AUTHOR CHECKED; independent audit required',canonical_rows=rows,
 axis_uniform_span=axis,diagonal_uniform_span=diagonal,
 passive_axis_band_padding=axis+1,passive_diagonal_band_padding=diagonal+1,
 huge_and_prefix_controls=controls,
 semantics='Every completed macro includes its actual L successor; bound uses entry and selected FUTURE input, not only inputs already consumed.')
out=P/'COLLISION_NORMAL_SPAN_CHECKED.json';out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(axis_span=axis,diagonal_span=diagonal,controls=len(controls),output=str(out))))
