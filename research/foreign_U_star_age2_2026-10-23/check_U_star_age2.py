"""Four genuine source-deletion guards for first-foreign star effects at age two.
Finite fresh-output roles and exact head cones, not a path-prefix scan.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};E={(2,0),(2,1)};V=((0,1),(1,0),(0,-1),(-1,0));GUARDS={(-1,-1),(-1,1),(0,-1),(0,2)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
u,_,_,_,ur=derive(W[3]['word']);births=[]
for q in sorted(GUARDS):
 assert ur[q][-1][1]=='L';assert q[1]<4 and q[1]-q[0]<5
 births.append(dict(cell=q,last_creating_U_read=ur[q][-1],N_bound_y=4,W_bound_H=5))
# Literal outputs for all four atomic types. C has no external residual inputs;
# C15, not a fictitious five-turn suffix, is used here.
_,_,_,_,_=derive(W[1]['word'])
_,cpar,cep,ch,_=derive(W[1]['word']);assert cep==(0,1)and ch==3
craw,_,_,_,_=derive(W[1]['word']+M);cI={q for q,b in craw.items()if b}-K;assert not cI
Cout={at(q,cep,ch)for q in K}^cpar^K;assert Cout=={(1,2),(2,0),(2,1)}
for os in[set(map(tuple,G[i]['outputs']))for i in(0,4,7)]+[Cout]:
 assert all(q[1]>=0 and sum(q)>=0 for q in os)
# North zero-C base endpoints increase y; first C changes y to >=5 and W
# zero-C endpoints increase H=y-x. A second C preserves that W-born output bound.
for i in(0,4,7):
 ep=G[i]['endpoint'];assert ep[2]==0 and ep[1]>=0 and sum(ep[:2])>=0
roles=[]
for q in sorted(GUARDS):
 for i in(0,4,7):
  rq,_,_,_,_=derive(G[i]['word']+M)
  for z in map(tuple,G[i]['outputs']):
   p=sub(q,rot(z,2));hits=sorted({at(c,p,2)for c in rq}&L)
   why='wrong_active_sector'if(sum(p)+2)%2 else'held_original_L_in_complete_context'
   if why!='wrong_active_sector':assert hits
   roles.append(dict(cell=q,producer=G[i]['name'],output_slot=z,producer_pose=[*p,2],held_star_context_hits=hits,reason=why))
assert len(roles)==64 and Counter(r['reason']for r in roles)=={'wrong_active_sector':32,'held_original_L_in_complete_context':32}
P=R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json';ports=json.loads(P.read_text())['interfaces']['star']['gates'];rows=[]
for g in ports:
 if g['pose'][2]!=2:continue
 p=tuple(g['pose'][:2]);h=2;j='DCVUFQB'.index(g['foreign']);rq,_,_,_,rd=derive(W[j]['word']+M);core={at(q,p,h)for q in K};I={at(q,p,h)for q,b in rq.items()if b}-core;white={at(q,p,h)for q,b in rq.items()if not b};guardhits=sorted(I&GUARDS)
 if guardhits:
  why='black_foreign_residual_input_has_no_possible_fresh_identity_by_clock_two'
 elif g['foreign']=='Q':
  assert g['pose']==[-2,-4,2]and(core|white)&E;why='original_east_absence_requires_first_right_renewal_at_clock_four'
 else:
  assert g['foreign']=='B'and g['pose']==[-1,-5,2]
  # Only plain U is allowed before B by signed complete-eight adjacency.
  ep=tuple(G[7]['endpoint'][:2]);pred=sub(p,rot(ep,2));pr,_,_,_,_=derive(G[7]['word']+M);hits={at(q,pred,2)for q in pr}&L;assert hits
  why='only_plain_U_predecessor_has_held_original_L_in_complete_context'
 rows.append(dict(foreign=g['foreign'],pose=g['pose'],guard_black_residual_inputs=[dict(cell=q,foreign_local=rot(sub(q,p),-h),first_foreign_read=rd[rot(sub(q,p),-h)][0])for q in guardhits],original_east_core_or_white_hits=sorted((core|white)&E),reason=why,raw_retirements=g['raw_retirements'],marker_spillover=g['marker_spillover']))
assert len(rows)==15
assert Counter(r['reason']for r in rows)=={'black_foreign_residual_input_has_no_possible_fresh_identity_by_clock_two':13,'original_east_absence_requires_first_right_renewal_at_clock_four':1,'only_plain_U_predecessor_has_held_original_L_in_complete_context':1}
D=[GP,QP,P,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'seven_word_spatial_return_2026-10-23/foreign_U_early_star_exclusion_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='A genuine U/UC/UCC followed by uninterrupted complete eight cannot have its first foreign RAW retirement or marker-only absorption of an original four-star identity at source-entry C age two. Combined with signed ages zero/one, such an effect requires age at least three. Four source-deleted cells lack black residual identities outside the current core, not a claim of fine-time physical whiteness. No foreign persistence or attainment claim.',source_deletion_guards=births,S_fresh_output_alignment_rows=roles,foreign_S_heading_gates=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'U_star_age2.json').write_text(json.dumps(o,indent=2)+'\n');print('64 fresh-output roles:32 sector+32 held-star;15 S gates:13 source-deletion guards+1 renewal-age+1 predecessor. First foreign star effect requires >=3Cs.')
