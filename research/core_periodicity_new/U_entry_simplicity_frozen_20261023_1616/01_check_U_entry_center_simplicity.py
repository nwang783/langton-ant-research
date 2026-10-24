"""Dependency-bound COMPLETE first-contact assembly, including all129 cases."""
from collections import Counter
from fractions import Fraction as F
from math import ceil,floor
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
DEPS={
 'horizon':'first_center_contact_frozen_20261023_1412',
 'proper_catalogue':'atomic_crossing_contexts_frozen_20261023_1414',
 'proper_VU':'atomic_crossing_retirement_frozen_20261023_1429',
 'two':'two_C_first_contact_frozen_20261023_1436',
 'three_nonproper':'three_C_center_touch_frozen_20261023_1533',
 'atomic_left_pose':'atomic_three_C_pose_boundary_frozen_20261023_1607',
 'four':'four_C_contact_gate_frozen_20261023_1455',
 'four_boundary':'atomic_predecessor_halfplanes_frozen_20261023_1505',
 'C_W5':'C_first_W_crossing_frozen_20261023_1424',
 'D_W5_gate':'D_first_W5_gate_frozen_20261023_1437',
 'D_W5_helpers':'D_W5_helper_history_frozen_20261023_1548',
 'five_nonproper':'five_C_center_touch_frozen_20261023_1550',
 'five_boundary':'five_C_endpoint_boundary_frozen_20261023_1557',
 'six':'six_C_contact_frozen_20261023_1454',
 'six_successor_geometry':'six_C_successor_frozen_20261023_1505',
 'six_successor_cohort':'six_C_successor_cohort_frozen_20261023_1538',
 'read_cap':'simple_center_read_cap_frozen_20261023_1612',
}
V={'D':(1,1),'C':(1,1),'V':(1,3),'U':(0,4)}
RANK={'U':0,'V':1,'D':2,'C':2}
CENTER=(F(-1,2),F(-1,2))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def frac(x):return F(*x) if isinstance(x,list) else F(x)
def key(n,a,b,p,s,t):return n,a,b,*p,frac(s),frac(t)
def data(name):
 directory=ROOT/DEPS[name]
 return json.loads(next(directory.glob('02_*json')).read_text())

def generate():
 rows=[]
 for n in range(2,7):
  h=(-n)%4
  for a,u in V.items():
   for b,bv in V.items():
    if n==2 and not RANK[a]>RANK[b]:continue
    if n==6 and not RANK[a]<RANK[b]:continue
    v=rot(bv,h);correction=sub(CENTER,rot(CENTER,h))
    corners=[add(correction,(s*u[0]-t*v[0],s*u[1]-t*v[1])) for s in (0,1) for t in (0,1)]
    bounds=[(ceil(min(p[k] for p in corners)),floor(max(p[k] for p in corners))) for k in (0,1)]
    for x in range(bounds[0][0],bounds[0][1]+1):
     for y in range(bounds[1][0],bounds[1][1]+1):
      if (x+y+h)%2:continue
      w=sub(add((x,y),rot(CENTER,h)),CENTER);den=det(u,v)
      if den:
       s,t=F(det(w,v),den),F(det(w,u),den)
       if not(0<=s<1 and 0<t<=1):continue
      else:
       if det(w,u):continue
       k=0 if v[0] else 1;t=F(-w[k],v[k]);s=F(0)
       if not(0<t<=1 and add(w,(t*v[0],t*v[1]))==(0,0)):continue
      rows.append(key(n,a,b,(x,y,h),s,t))
 return set(rows)
universe=generate()
assert Counter(r[0] for r in universe)=={2:8,3:45,4:23,5:45,6:8}
assert len(universe)==129
catalogues={}
D=data('two');catalogues['two']={key(2,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_chord_parameter'],r['later_chord_parameter']) for r in D['all_eight_canonical_two_C_contact_geometries']}
D=data('proper_catalogue');catalogues['proper_catalogue']={key(3 if r['later_pose'][2]==1 else 5,r['first_atom'],r['later_atom'],r['later_pose'],r['first_parameter'],r['later_parameter']) for r in D['crossings']}
D=data('three_nonproper');catalogues['three_nonproper']={key(3,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']) for r in D['all_24_canonical_nonproper_geometries']}
D=data('four');catalogues['four']={key(4,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']) for r in D['all_23_canonical_geometries']}
D=data('five_nonproper');catalogues['five_nonproper']={key(5,r['a'],r['b'],[*r['p'],r['h']],r['s'],r['t']) for r in D['all_24_geometries']}
D=data('six');catalogues['six']={key(6,r['first_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']) for r in D['geometries']}
assert set.union(*catalogues.values())==universe
assert sum(map(len,catalogues.values()))==129
assembly=[]
for k in sorted(universe):
 n,a,b,x,y,h,s,t=k;p=(x,y,h);proper=0<s<1 and 0<t<1
 entry_ids=[]
 if n==2:
  refs=['two'];reason='EXCLUDED_TWO_C_FIRST_CONTACT'
 elif n==6:
  refs=['six','six_successor_geometry','six_successor_cohort'];reason='EXCLUDED_SIX_C_FIRST_CONTACT'
 elif n==3:
  if proper:
   if a in ('V','U'):
    refs=['proper_catalogue','proper_VU'];reason='EXCLUDED_V_OR_U_PROPER_FIRST_CONTACT'
   else:
    assert a in ('D','C') and b=='V' and p==(-1,0,1)
    refs=['proper_catalogue','atomic_left_pose'];reason='THREE_C_LEFT_POSE_ENTRY_ALTERNATIVES'
    entry_ids=[0,1] if a=='D' else [1]
  elif a=='V' and b=='D' and p==(-1,0,1):
   refs=['three_nonproper','atomic_left_pose'];reason='THREE_C_LEFT_POSE_ENTRY_ALTERNATIVES'
   entry_ids=[0,4,5,6]
  else:
   refs=['three_nonproper'];reason='EXCLUDED_THREE_C_NONPROPER_CONTACT'
 elif n==4:
  if a=='D' and b=='C' and p==(-1,-1,0):
   refs=['four','four_boundary'];reason='FACTOR_FIRST_D_BASE_REQUIRED';entry_ids=[0,1]
  else:
   refs=['four','four_boundary'];reason='EXCLUDED_FOUR_C_OTHER_OR_NONINITIAL_C'
 else:
  assert n==5
  if proper:
   if a in ('V','U'):refs=['proper_catalogue','proper_VU']
   elif a=='C':refs=['proper_catalogue','C_W5']
   else:refs=['proper_catalogue','D_W5_gate','D_W5_helpers']
   reason='EXCLUDED_FIVE_C_PROPER_FIRST_CONTACT'
  elif a=='D' and b=='C' and p==(0,-1,3):
   refs=['five_nonproper','five_boundary'];reason='FACTOR_FIRST_D_BASE_REQUIRED';entry_ids=[0,1]
  else:
   refs=['five_nonproper','D_W5_helpers'];reason='EXCLUDED_FIVE_C_NONPROPER_OTHER_CASE'
 assert not set(entry_ids)&{7,8,9}
 assembly.append({'entry_C_gap':n,'earlier_atom':a,'later_atom':b,'later_pose':p,'earlier_parameter':str(s),'later_parameter':str(t),'kind':'PROPER' if proper else 'NONPROPER','reason':reason,'signed_dependency_modules':refs,'surviving_allowed_first_full_packet_ids':entry_ids,'surviving_source_entry_C_clock':0 if entry_ids else None})
assert sum(bool(r['surviving_allowed_first_full_packet_ids']) for r in assembly)==5
assert {r['entry_C_gap'] for r in assembly if r['surviving_allowed_first_full_packet_ids']}=={3,4,5}
cap=data('read_cap');assert cap['physical_read_cap_raw']==104 and cap['raw_plus_terminal_marker_per_cell_cap']==106
result={'status':'AUTHOR_COMPLETE_U_FAMILY_ENTRY_CENTER_SIMPLICITY_ASSEMBLY',
 'scope':'Every actual complete recurrent-eight factor beginning U/UC/UCC has an injective corrected-center atomic polygonal path. This is auxiliary center simplicity, not microscopic self-avoidance, incidence beta0, renewal, a C bound, or capture.',
 'all129_canonical_first_contact_cases':assembly,'case_counts_by_entry_gap':dict(Counter(r['entry_C_gap'] for r in assembly)),
 'case_counts_by_conclusion':dict(Counter(r['reason'] for r in assembly)),
 'all_surviving_initial_packet_ids':sorted(set.union(*(set(r['surviving_allowed_first_full_packet_ids']) for r in assembly))),
 'U_family_first_packet_ids':[7,8,9],'raw_physical_read_cap':104,'with_terminal_marker_physical_read_cap':106,
 'finite_and_infinite_prefix_scope':'Any hypothetical first contact lies in a finite complete prefix, so the finite result implies the corresponding statement for an infinite complete factor starting U-family.',
 'dependency_manifest_hashes':{name:{'path':str(Path(directory)/'manifest.json'),'sha256':hashlib.sha256((ROOT/directory/'manifest.json').read_bytes()).hexdigest()} for name,directory in DEPS.items()},
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'chronology_dcuv/U_entry_center_simplicity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'canonical_contact_cases':len(assembly),'case_counts':dict(Counter(r['entry_C_gap'] for r in assembly)),'surviving_boundary_cases':sum(bool(r['surviving_allowed_first_full_packet_ids']) for r in assembly),'surviving_initial_packet_ids':result['all_surviving_initial_packet_ids'],'U_entry_raw_read_cap':104,'with_terminal_M11_cap':106}))
