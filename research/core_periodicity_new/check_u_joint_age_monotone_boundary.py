"""Finite arithmetic controls for an explicitly relaxed monotone-guard claim.
The all-age assertion is analytic; this enumeration is not its proof.
"""
from pathlib import Path
import hashlib, itertools, json

W=Path(__file__).resolve().parent
P=W/'chronology_dcuv/literal_residual_geometry.json'
G=json.loads(P.read_text())['geometry']
slots=[(-1,1),(-1,2),(-1,4),(0,2),(0,3)]
assert set(slots)==set(map(tuple,G[7]['inputs']))
minimum=(3,3,5,5,5)
def law(t):
 a,q,b,c,d=t
 return q>=min(a,c) and q>=min(a,d)
assert law(minimum)
def tail(ages,places,K):
 return tuple(sum(age>=j for age,z in zip(ages,places) if z==place)
              for place in sorted(set(places)) for j in range(K+1))
controls=[]
for h in range(4):
 def rot(p):
  x,y=p
  return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
 places=[rot(p)[1]-rot(p)[0] for p in slots]
 I=tail(minimum,places,12)
 checked=joint=0
 for ages in itertools.product(*[range(a,10) for a in minimum]):
  T=tail(ages,places,12)
  assert all(x>=y for x,y in zip(T,I))
  checked+=1
  joint+=law(ages)
 controls.append(dict(heading=h,slot_heights=places,minimal_tail=I,
                      tested_JO_KV_profiles=checked,joint_profiles=joint))
places=[y-x for x,y in slots]
bad=(18,14,6,18,14)
assert not law(bad)
assert all(x>=y for x,y in zip(tail(bad,places,20),tail(minimum,places,20)))
assert places==[2,3,5,2,3]
O=dict(status='AUTHOR_RELAXED_GUARD_ARITHMETIC_PASS',
       scope='Only the JO/KV/LN input-age ansatz, not exact physical attainability.',
       slot_order=slots,minimum=minimum,minimum_satisfies_joint_law=True,
       rotated_geometry_controls=controls,nonmonotone_counterinventory=bad,
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [P,Path(__file__).resolve()]})
T=W/'chronology_dcuv/u_joint_age_monotone_boundary.json'
T.write_text(json.dumps(O,indent=2)+'\n')
print({'status':O['status'],'profiles':sum(r['tested_JO_KV_profiles'] for r in controls),
       'minimum':minimum,'counterinventory':bad})
