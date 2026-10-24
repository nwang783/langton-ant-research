"""Fixed whole component-type profile at cut173, all even spacings>=20.
The all-parameter proof is five separated affine x-intervals; named replays
only corroborate it. No new waiting-time or cap theorem is inferred by sampling.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,comp,step
G={(0,-1),(1,1),(2,2),(1,3)}
def profile(B):
 seen=set();types=[];sizes=[]
 for q in sorted(B):
  if q in seen:continue
  C=comp(B,0,ends(q,0)[0]);seen|=C;sizes.append(len(C));V={v for x in C for v in ends(x,0)};a=min(V)
  types.append(tuple(sorted(tuple(sorted((v[0]-a[0],v[1]-a[1])for v in ends(x,0)))for x in C)))
 return sorted(types),sorted(sizes)
B=set(G);p=(0,0);h=1;reads=[]
for t in range(173):reads.append(p);p,h=step(B,p,h)
L=set(B);assert len(L)==35 and(p,h)==((4,1),0)
assert(min(x for x,y in reads),max(x for x,y in reads),min(y for x,y in reads),max(y for x,y in reads))==(0,7,-2,7)
active=comp(L,0,cursor(p,h));assert len(active)==6
# Affine x intervals [a*n+b_lo,a*n+b_hi], ordered left to right.
intervals=[dict(group='port3',a=-5,lo=4,hi=8),dict(group='port4',a=-3,lo=0,hi=2),dict(group='port2',a=-1,lo=-2,hi=0),dict(group='local173',a=0,lo=0,hi=7),dict(group='port1',a=1,lo=-4,hi=0)]
gaps=[]
for x,y in zip(intervals,intervals[1:]):
 a=y['a']-x['a'];b=y['lo']-x['hi'];assert a>=0 and 20*a+b>=9
 gaps.append(dict(left=x['group'],right=y['group'],gap_a=a,gap_b=b,minimum_n20=20*a+b))
base=None;controls=[]
for n in(20,40,80):
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 BB=set()
 for q,hh in poses:BB|={(q[0]+v[0],q[1]+v[1])for z in G for v in[rot(z,(hh-1)%4)]}
 pp=(0,0);hh=1
 for t in range(173):pp,hh=step(BB,pp,hh)
 P,sz=profile(BB)
 if base is None:base=P
 assert P==base and(pp,hh)==(p,h)and comp(BB,0,cursor(pp,hh))==active
 assert len(BB)==51 and len(P)==18 and sz==[1]*10+[2]*5+[6,10,15]
 controls.append(dict(n=n,complete_mass=51,component_count=18,component_sizes=sz,component_types=P))
out=dict(status='AUTHOR all-parameter fixed complete component-type multiset at cut173',parameter='every even n>=20',local_read_box=[0,7,-2,7],local_field_173=sorted(L),local_mass=35,pose=[p,h],active_component=sorted(active),affine_x_intervals=intervals,adjacent_x_gaps=gaps,global_mass_173=51,component_count=18,global_component_sizes=[1]*10+[2]*5+[6,10,15],type_equivalence='Translation only on the embedded doubled w-edge graph; rotations need not be quotiented. Even n changes translate each future port by an even-checkerboard vector, preserving fixed sector0.',named_controls=controls,retained_dependency_sha256={'active_w_archive_itinerary_2026-10-23/TWENTY_CELL_SUSTAINED_CAP.md':hashlib.sha256((ROOT/'active_w_archive_itinerary_2026-10-23/TWENTY_CELL_SUSTAINED_CAP.md').read_bytes()).hexdigest()},scope='No new distance counterfamily: this freezes the exact full type-summary equality inside the already signed20-cell family. Its sustained cap501229, marked15-edge frozen archive and wait624n-1778 remain attributed dependencies.')
(OUT/'twenty_cell_type_profile_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='named_controls'},indent=2))
