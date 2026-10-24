"""Exact first-foreign U-star erosion ports with actual plain V/U predecessors.
Finite 69-port interface and forced genuine renewal guard; no prefix enumeration.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
G=json.load(open('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'))['geometry']
RAW=json.load(open('/workspace/shared/langton/word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'))['macro_words']
M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};Z={(1,0),(1,1),(2,0),(2,1)}
V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads

P=R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json'
ports=json.loads(P.read_text())['interfaces']['star']['gates']
assert len(ports)==69
E={(2,0),(2,1)};bp=(3,-1);BL={place(q,bp,0)for q in L}
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(z,v),den),F(det(z,u),den)
  return dict(kind='point',s=s,t=t)if 0<=s<=1 and 0<=t<=1 else None
 if det(z,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])));lo=max(F(0),lo);hi=min(F(1),hi)
 return dict(kind='collinear',lo=lo,hi=hi)if lo<=hi else None
def chord(p,h,kind):
 a=add((2*p[0],2*p[1]),rot((-1,-1),h));return a,add(a,rot((2,6)if kind=='V'else(0,8),h))
rows=[]
for gate in ports:
 j='DCVUFQB'.index(gate['foreign']);p=tuple(gate['pose'][:2]);h=gate['pose'][2]
 fr,_,_,_,_=derive(RAW[j]['word']+M);core={place(q,p,h)for q in K};white={place(q,p,h)for q,b in fr.items()if not b}
 force_east_absence=sorted((core|white)&E)
 guardian_conflict=sorted((core|white)&BL)
 for i,name in((2,'V'),(3,'U')):
  pr,_,ep,dh,_=derive(RAW[i]['word']);sp=sub(p,rot(ep,h));sh=h
  assert not(name=='U'and sp==(0,0)and sh==0), 'No gate is the immediate creating-U adjacency'
  req,_,_,_,_=derive(RAW[i]['word']+M);ctx={place(q,sp,sh)for q in req};held_hits=sorted(ctx&L)
  a,b=chord(sp,sh,name);oldhit=hit((-1,-1),(-1,7),a,b)
  legal_adjacent=oldhit==dict(kind='point',s=F(1),t=F(0))and sp==(0,4)and sh==0
  if gate['foreign']=='B'and name=='V':why='literal_V_B_adjacency_conflict_RAW59'
  elif held_hits:why='old_permanent_U_star_in_predecessor_complete_context'
  elif oldhit and not legal_adjacent:why='predecessor_chord_contacts_creating_U_chord'
  elif force_east_absence and guardian_conflict:why='forced_genuine_right_breaker_fresh_star_in_foreign_core_or_before_white'
  else:why='necessary_interface_not_asserted_attained'
  rows.append(dict(foreign=gate['foreign'],foreign_pose=gate['pose'],predecessor=name,predecessor_pose=[*sp,sh],reason=why,held_star_predecessor_context_hits=held_hits,old_U_chord_contact=oldhit,legal_source_endpoint_adjacency=legal_adjacent,original_east_absence_forcing_cells=force_east_absence,forced_breaker_star_core_or_before_white_hits=guardian_conflict,raw_retirements=gate['raw_retirements'],marker_spillover=gate['marker_spillover']))
counts=dict(Counter(r['reason']for r in rows));assert counts=={'old_permanent_U_star_in_predecessor_complete_context':12,'necessary_interface_not_asserted_attained':81,'predecessor_chord_contacts_creating_U_chord':2,'forced_genuine_right_breaker_fresh_star_in_foreign_core_or_before_white':20,'literal_V_B_adjacency_conflict_RAW59':23},counts
surv=[r for r in rows if r['reason']=='necessary_interface_not_asserted_attained'];survkeys={(r['foreign'],*r['foreign_pose'])for r in surv};assert len(survkeys)==50
newguards=sorted({(r['foreign'],*r['foreign_pose'])for r in rows if r['reason']=='forced_genuine_right_breaker_fresh_star_in_foreign_core_or_before_white'});assert len(newguards)==13
# The forced guardian is a real output star of every possible right-breaker tail.
assert BL=={(3,-1),(3,0),(4,-1),(4,0)}
for i in(7,8,9):assert BL<={place(q,bp,0)for q in map(tuple,G[i]['outputs'])}
# Bind the actual V->B conflict, not a guessed family ban.
w=RAW[2]['word']+RAW[6]['word']+M;p0=(0,0);h0=0;par=set();rq={};bad=None
for t,ch in enumerate(w):
 need=(ch=='L')^(p0 in par)
 if p0 in rq and rq[p0]!=need:bad=t-len(RAW[2]['word']);break
 rq[p0]=need;par.symmetric_difference_update({p0});h0=(h0+(-1 if ch=='L'else 1))%4;p0=add(p0,V[h0])
assert bad==59
D=[R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',P,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
def enc(z):
 if isinstance(z,F):return int(z)if z.denominator==1 else str(z)
 if isinstance(z,dict):return{k:enc(v)for k,v in z.items()}
 if isinstance(z,(tuple,list)):return[enc(v)for v in z]
 return z
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Necessary original-U-star first-foreign erosion interfaces, after a genuine creating U/UC/UCC and an uninterrupted complete-eight interval. No first-center-contact condition is imposed on the foreign proxy; predecessor chords lie strictly inside the preforeign simple interval. All old-star and forced-breaker-star permanence is used only before foreign entry. No remaining gate is asserted attained and no permanence crosses foreign RAW.',counts=counts,remaining_predecessor_assignments=len(surv),remaining_foreign_poses=len(survkeys),new_forced_renewal_guard_poses=newguards,rows=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_U_star_predecessors.json').write_text(json.dumps(enc(o),indent=2)+'\n');print(counts);print('81 necessary assignments at50 poses;13 foreign poses excluded by actual renewal guardian')
