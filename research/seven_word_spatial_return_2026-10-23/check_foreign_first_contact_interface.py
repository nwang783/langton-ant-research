"""Exact geometric obligations at the first foreign F-prefix contact.
No prefix search, actual-history attainment claim, or global proxy simplicity.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib, json
ROOT=Path('/workspace/shared/langton'); HERE=Path(__file__).resolve().parent
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry']; ALLWORDS=json.loads(WP.read_text())['macro_words']; FWORD=ALLWORDS[4]['word']
M=G[0]['marker']; VEC=((0,1),(1,0),(0,-1),(-1,0))
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
L={(0,0),(0,1),(1,0),(1,1)}
def rot(q,h):
 x,y=q; return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[0],a[1]-b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def derive(w):
 p=(0,0);h=0;req={};par=set();reads={}
 for t,ch in enumerate(w):
  bit=(ch=='L')^(p in par)
  assert p not in req or req[p]==bit
  req[p]=bit;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p})
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])
 return req,p,h,reads
WORDS={'D':G[0]['word'],'C':G[1]['word'][len(G[0]['word']):], 'V':G[4]['word'],'U':G[7]['word']}
STEPS={'D':(2,2),'C':(2,2),'V':(2,6),'U':(0,8)}
def chord(a,p=(0,0),h=0):
 c=add((2*p[0],2*p[1]),rot((-1,-1),h))
 return c,add(c,rot(STEPS[a],h))
def foreign_chord(p,h):
 c=add((2*p[0],2*p[1]),rot((-1,-1),h))
 return c,add(c,rot((-6,-2),h))
def intersection(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 assert den, 'The F-prefix chord is never parallel to an old atomic chord.'
 s,t=Q(det(z,v),den),Q(det(z,u),den)
 return (s,t) if 0<=s<1 and 0<t<=1 else None

def enc(x):
 if isinstance(x,Q):return int(x) if x.denominator==1 else str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
rows=[]
for n in range(1,5):
 h=(-n)%4
 for a in WORDS:
  start,end=chord(a);u=sub(end,start);base=rot((-1,-1),h);fv=rot((-6,-2),h)
  # 2p = start + s*u - base - t*fv, 0<=s,t<=1.
  corners=[sub(add(start,(s*u[0],s*u[1])),add(base,(t*fv[0],t*fv[1]))) for s in (0,1) for t in (0,1)]
  bounds=[((min(q[i] for q in corners)+1)//2, max(q[i] for q in corners)//2) for i in range(2)]
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if (x+y+h)%2:continue
    p=x,y;hit=intersection(start,end,*foreign_chord(p,h))
    if hit is None:continue
    rows.append(dict(source_atom=a,foreign_pose=(*p,h),source_parameter=hit[0],foreign_parameter=hit[1],permitted_C_ages=[n,n+4],preceding_C_bits=[0,1],exact_candidate_bounds=bounds))
assert len(rows)==42
assert Counter(r['permitted_C_ages'][0] for r in rows)=={1:9,2:12,3:9,4:12}
assert Counter(r['source_atom'] for r in rows)=={'D':6,'C':6,'V':14,'U':16}
# Full foreign F context necessary conditions when the earlier atom is itself
# a genuine U source. Its four original fresh L tags are still current at F entry.
Ufilters={}
for foreign_index,foreign_name in ((4,'F'),(5,'Q'),(6,'B')):
 req,_,_,_=derive(ALLWORDS[foreign_index]['word']+M)
 Urows=[]
 for r in rows:
  if r['source_atom']!='U':continue
  x,y,h=r['foreign_pose'];p=x,y
  core={add(p,rot(q,h)) for q in K}
  white={add(p,rot(q,h)) for q,b in req.items() if not b}
  inputs={add(p,rot(q,h)) for q,b in req.items() if b}-core
  reason='held_star_in_core' if L&core else 'held_star_before_white' if L&white else 'unexcluded_necessary_interface'
  Urows.append(dict(**r,foreign=foreign_name,reason=reason,star_input_hits=sorted(L&inputs)))
 Ufilters[foreign_name]=Urows
assert Counter(r['reason'] for r in Ufilters['F'])=={'held_star_in_core':2,'held_star_before_white':10,'unexcluded_necessary_interface':4}
assert Counter(r['reason'] for r in Ufilters['Q'])=={'held_star_in_core':2,'held_star_before_white':12,'unexcluded_necessary_interface':2}
assert Counter(r['reason'] for r in Ufilters['B'])=={'held_star_in_core':2,'held_star_before_white':13,'unexcluded_necessary_interface':1}
assert [r['foreign_pose'] for r in Ufilters['F'] if r['reason']=='unexcluded_necessary_interface']==[(-2,3,3),(1,3,0),(2,4,0),(3,3,0)]
assert [r['foreign_pose'] for r in Ufilters['Q'] if r['reason']=='unexcluded_necessary_interface']==[(1,3,0),(2,4,0)]
assert [r['foreign_pose'] for r in Ufilters['B'] if r['reason']=='unexcluded_necessary_interface']==[(1,3,0)]
# Smallest prepared U-star return gate, normalized to the actual creating U.
FPOSE=(-3,-3,2);DPOSE=(1,-1,0)
assert derive(WORDS['U'])[1:3]==((0,4),0)
freq,fp,fh,fr=derive(FWORD)
assert add(FPOSE[:2],rot(fp,FPOSE[2]))==DPOSE[:2]
assert (FPOSE[2]+fh)%4==0
_,dp,dh,dr=derive(WORDS['D']);assert add(DPOSE[:2],dp)==(2,0) and dh==0
full_freq,_,_,full_fr=derive(FWORD+M)
assert not L&{add(FPOSE[:2],rot(q,FPOSE[2])) for q in full_fr}
assert not L&{add(DPOSE[:2],q) for q in dr}
creq,_,_,cr=derive(WORDS['C']);assert add((2,0),next(q for q,ts in cr.items() if ts[0][0]==1))==(1,0)
assert cr[(-1,0)][0]==(1,'L')
closure=[(-5,-5),(1,-3),(3,-1),(1,1),(-1,-1)]
assert foreign_chord(FPOSE[:2],FPOSE[2])==tuple(closure[:2])
assert chord('D',DPOSE[:2],0)==tuple(closure[1:3])
# Remaining bridge turns, in units pi/4: D->B = +2, B->r = +2,
# r->source U = -3. Total +1 cancels alpha_D-alpha_U=-pi/4.
bridge_turn_quarters=[2,2,-3];assert sum(bridge_turn_quarters)==1
branches=[dict(preceding_C_bit=b,C_count=n,closed_turn_quarters=2*(n+2-4*b)) for b in(0,1) for n in range(2,15,4) if abs(2*(n+2-4*b))==8]
assert branches==[dict(preceding_C_bit=0,C_count=2,closed_turn_quarters=8),dict(preceding_C_bit=1,C_count=6,closed_turn_quarters=8)]
D=[GP,WP,ROOT/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',ROOT/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',HERE/'foreign_kinked_barrier_manifest.json',Path(__file__).resolve()]
out=dict(status='AUTHOR_EXACT_FIRST_FOREIGN_INTERFACE_PENDING_INDEPENDENT_AUDIT',scope='Necessary geometry for the chronological first center contact in the common F-prefix chord, following an actual simple retained-eight atomic path. No first-contact exclusion, actual ancestry control, Q/B-tail classification, or global proxy simplicity is claimed.',geometric_count=len(rows),age_label_count=2*len(rows),rows=rows,U_source_star_filters=Ufilters,smallest_return_gate=dict(source_U_pose=(0,0,0),foreign_F_pose=FPOSE,returned_D_pose=DPOSE,retired_tag=(1,0),retirement_owner='returned C RAW phase 1',closure_vertices_after_old_path=closure,bridge_turn_quarters=bridge_turn_quarters,conditional_Jordan_branches=branches),dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D})
(HERE/'foreign_first_contact_interface.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print('42 geometric cases / 84 clock labels; seven U-source F/Q/B necessary interfaces; conditional Jordan branches (2,0), (6,1).')
