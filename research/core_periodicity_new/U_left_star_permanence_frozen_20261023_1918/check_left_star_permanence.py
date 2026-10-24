"""Exact first-retirement table for a time-descending U core-port invariant.
No path search, chain-length assumption, or cycle-to-root funding inference.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent;W=R.parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
L={(0,0),(0,1),(1,0),(1,1)};Z={(1,0),(1,1),(2,0),(2,1)}
MARK=G[0]['marker'];VEC=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def place(q,p,h):return add(p,rot(q,h))
def reconstruct(word):
 p=(0,0);h=0;par=set();req={}
 for ch in word:
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b
  req[p]=b;par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])
 return req,par,p,h
for a in IDS:
 req,_,_,_=reconstruct(G[a]['word']+MARK)
 assert req=={(x,y):bool(b)for x,y,b,*_ in G[a]['requirements']}
 _,odd,p,h=reconstruct(G[a]['word'])
 O=(K|set(map(tuple,G[a]['inputs'])))^odd
 core={place(q,p,h)for q in K};assert O-core==set(map(tuple,G[a]['outputs']))
for a in(7,8,9):
 assert L<=set(map(tuple,G[a]['outputs']))
 p=(0,0);h=0
 for tick,ch in enumerate(G[a]['word']):
  if tick>=len(G[7]['word']):assert p not in L
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])

def chord(p,h,a):
 start=add((2*p[0],2*p[1]),rot((-1,-1),h))
 step=rot((2,2)if a in(0,1)else(2,6)if a in(4,5,6)else(0,8),h)
 return start,add(start,step)
def hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(z,v),den),F(det(z,u),den)
  return dict(kind='point',past_parameter=s,consumer_parameter=t)if 0<=s<=1 and 0<=t<=1 else None
 if det(z,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])));lo=max(F(0),lo);hi=min(F(1),hi)
 return dict(kind='collinear',past_interval=(lo,hi))if lo<=hi else None
A=chord((0,0),0,7);B=chord((3,-1),0,7);rB=(3,-1)
rows=[];candidates={}
for a in IDS:
 for target in sorted(L):
  for slot in G[a]['inputs']:
   for h in range(4):
    p=sub(target,rot(slot,h))
    I={place(q,p,h)for q in G[a]['inputs']}
    core={place(q,p,h)for q in K}
    white={place(q[:2],p,h)for q in G[a]['requirements']if not q[2]}
    why='sector'if(sum(p)+h)%2 else'star_core'if L&core else'star_before_white'if L&white else'candidate'
    row=dict(packet=a,name=G[a]['name'],pose=(*p,h),aligned_star_cell=target,input_slot=slot,reason=why,star_inputs=sorted(I&L),star_core_hits=sorted(L&core),star_white_hits=sorted(L&white))
    rows.append(row)
    if why=='candidate':
     row['source_chord_hit']=hit(*A,*chord(p,h,a))
     row['right_breaker_chord_hit']=hit(*B,*chord(p,h,a))
     row['right_breaker_fresh_r_before_white']=rB in white
     row['rB_source_B_local_coordinate']=(0,0)
     row['before_white_consumer_local_coordinate']=rot(sub(rB,p),-h)if rB in white else None
     candidates[a,*p,h]=row
assert len(rows)==368 and len(candidates)==24
assert Counter(r['reason']for r in rows)==dict(sector=184,star_core=20,star_before_white=140,candidate=24)
for key,row in candidates.items():
 I=set(map(tuple,row['star_inputs']));assert len(I)==1
 if I&{(0,0),(0,1)}:
  hh=row['source_chord_hit'];assert hh
  if hh['kind']=='point':assert hh['past_parameter']in(F(0),F(1,2))
  else:assert hh['past_interval'][0]<1 and hh['past_interval'][1]>=0
  row['classification']='FORBIDDEN_CREATING_U_CHORD_CONTACT'
 elif I=={(1,1)}:
  hh=row['right_breaker_chord_hit'];assert hh and hh['kind']=='point'and 0<hh['past_parameter']<1
  row['classification']='FORBIDDEN_EARLIER_RIGHT_BREAKER_U_CHORD_CONTACT'
 elif I=={(1,0)}:
  assert row['source_chord_hit']is None and row['right_breaker_chord_hit']is None
  assert row['right_breaker_fresh_r_before_white']
  assert row['before_white_consumer_local_coordinate']in ((2,0),(2,2),(1,3))
  row['classification']='REQUIRES_EARLIER_RETIREMENT_OF_RIGHT_BREAKER_LEFT_STAR_ID'
 else:assert False
assert Counter(r['classification']for r in candidates.values())==dict(FORBIDDEN_CREATING_U_CHORD_CONTACT=12,FORBIDDEN_EARLIER_RIGHT_BREAKER_U_CHORD_CONTACT=6,REQUIRES_EARLIER_RETIREMENT_OF_RIGHT_BREAKER_LEFT_STAR_ID=6)
# The signed right breaker retires east Z identities, never one of old L.
for b in(7,8,9):
 I={place(q,(3,-1),0)for q in G[b]['inputs']}
 assert not I&L
 assert rB in {place(q,(3,-1),0)for q in G[b]['outputs']}
 assert rB==place((0,0),(3,-1),0)
# Bind exact scope/dependencies, leaving the analytic minimum-time induction
# to the readable theorem rather than disguising it as a finite search.
DP=W/'causal_cycle_renewal_20261023_1841/manifest.json'
SP=W/'U_entry_simplicity_frozen_20261023_1616/manifest.json'
assert hashlib.sha256(DP.read_bytes()).hexdigest()=='27db0bc457534074587a988c16bbf57c994464656df7c9aa06427ab23203d7d4'
assert hashlib.sha256(SP.read_bytes()).hexdigest()=='127a00884b4a06af35a807ab76f6f6499b9427d56350a931c03cc0e8de65524d'
out=dict(status='AUTHOR_EXACT_U_LEFT_STAR_PERMANENCE_PENDING_INDEPENDENT_REVIEW',scope='Actual complete recurrent-eight factor, tracking only fresh residual IDs produced by U/UC/UCC inside that factor. Each source U-entry suffix supplies simple atomic centers. No arbitrary precolored roots, fine-R-walk simplicity, or infinite-chain assumption.',star_cells=sorted(L),right_breaker_pose=(3,-1,0),right_breaker_fresh_r_global=rB,right_breaker_fresh_r_local=(0,0),all_alignment_count=len(rows),counts=dict(Counter(r['reason']for r in rows)),all_alignments=rows,surviving_placements=list(candidates.values()),classification_counts=dict(Counter(r['classification']for r in candidates.values())),theorem='Every U/UC/UCC freshly produces four left-star IDs at(0,0),(0,1),(1,0),(1,1), which remain current until the end of the same retained-eight factor. A first retirement of any such star would require a strictly earlier retirement of the right first-breaker\'s own fresh star member r, contradicting chronological minimality.',consequence='Distinct U-born left stars are cell-disjoint. At full boundaries, if u U-family packets have occurred, at least4u residual cells are permanently reserved for the remainder of the factor.',not_claimed='No new-chain count, historical-component merger, finite U budget, confinement, or capture theorem follows merely from the locked mass.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,DP,SP,Path(__file__).resolve())})
def enc(x):
 if isinstance(x,F):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,(tuple,list)):return[enc(v)for v in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
(R/'left_star_permanence.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print(json.dumps(dict(status=out['status'],counts=out['counts'],classification_counts=out['classification_counts']),indent=2))
