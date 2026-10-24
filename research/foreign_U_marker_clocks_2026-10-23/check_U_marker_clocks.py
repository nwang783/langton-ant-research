"""Exact minimum clocks for the two remaining original-U marker-only mechanisms.
No age iteration, new prefix enumeration, or attainment assertion.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};V=((0,1),(1,0),(0,-1),(-1,0))
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
# Bind exactly the surviving marker-only mechanisms in the independently signed
# 138-row predecessor interface. Repeated predecessor rows are deduplicated.
P=R/'foreign_U_star_predecessors_2026-10-23/foreign_U_star_predecessors.json';D0=json.loads(P.read_text());mk={}
for r in D0['rows']:
 if r['reason']=='necessary_interface_not_asserted_attained'and r['marker_spillover']:mk[(r['foreign'],*r['foreign_pose'])]=r
assert set(mk)=={('F',3,3,0),('F',3,-2,1),('Q',3,5,0)}
# F(3,3,N) is removed by the separately signed actual age-four right-renewal
# reduction plus universal common-bud obstruction. Do not restate it as a local
# prepared-mask impossibility.
markers=[]
for name,p,h,tag in [('F',(3,-2),1,(1,1)),('Q',(3,5),0,(0,1))]:
 j='DCVUFQB'.index(name);rq,_,_,_,rd=derive(W[j]['word']+M);loc=rot(sub(tag,p),-h);assert rq[loc]and rd[loc][0]==(len(W[j]['word'])+1,'L');assert all(t>=len(W[j]['word'])for t,ch in rd[loc])
 _,_,ep,dh,_=derive(W[j]['word']);exitcore={at(c,at(ep,p,h),(h+dh)%4)for c in K};assert tag in exitcore
 markers.append(dict(foreign=name,pose=[*p,h],original_tag=tag,marker_only_local_slot=loc,first_full_context_read=rd[loc][0],physical_owner='successor RAW phase1, not foreign RAW',source_entry_C_residue=(-h)%4))
# F's before-WHITE requirement concerns the genuine creating U exit bud.
freq,_,_,_,frd=derive(W[4]['word']+M);s=(1,3);fl=rot(sub(s,(3,-2)),-1);assert fl==(-5,-2)and freq[fl]is False and frd[fl][0]==(53,'R')
_,_,_,_,ur=derive(W[3]['word']);assert ur[s][-1]==(26,'R')
for i in(7,8,9):assert s in set(map(tuple,G[i]['outputs']))
# The signed actual source-bud no-retirement-through4 law excludes age3;
# E-heading means ages3 mod4, so the next permitted lower bound is7.
Fbound=dict(foreign_pose=[3,-2,1],same_original_U_exit_bud=s,last_source_R=ur[s][-1],foreign_before_white_local=fl,first_foreign_read=frd[fl][0],signed_no_retirement_through_age=4,excluded_C_ages=[3],necessary_C_age_at_least=7)
# Q's actual immediate predecessor must be plain U(3,1,N); plain V's complete
# context meets held original L. The U itself requires common bud b WHITE.
qp=(3,5);qr,_,_,_,qrd=derive(W[5]['word']+M);b=(2,4);ql=sub(b,qp);assert ql==(-1,-1)and ql in K and qr[ql]
predecessors=[]
for i in(4,7):
 ep=tuple(G[i]['endpoint'][:2]);p=sub(qp,ep);rq,_,_,_,rd=derive(G[i]['word']+M);hits=sorted({at(c,p,0)for c in rq}&L)
 predecessors.append(dict(type=G[i]['name'],pose=[*p,0],held_original_L_context_hits=hits))
 if i==4:assert hits
 else:
  assert p==(3,1)and not hits;bl=sub(b,p);assert bl==(-1,3)and rq[bl]is False and rd[bl][0]==(22,'R')
# The first actual atom after creating-U base starts at(0,4,N), source clock0,
# whether it is a D/V/U base or internal C1 in UC/UCC. All four genuinely birth b.
common=[]
for i in range(4):
 rq,_,_,_,rd=derive(W[i]['word']);assert rd[(2,0)][-1]==(8,'R');common.append(dict(atom='DCVU'[i],start=[0,4,0],C_birth_clock=0,local_bud=[2,0],R_birth_phase=8,global_bud=b))
# Exhaust all genuine residual-input roles of a first bud consumer at ages3/4.
# A positive-C tail must finish before target U entry4; tails overshooting4 are
# not an alternative. C itself has no external residual inputs.
roles=[]
for age,h in((3,1),(4,0)):
 for i in(0,4,7):
  ep=tuple(G[i]['endpoint'][:2])
  for slot in map(tuple,G[i]['inputs']):
   p=sub(b,rot(slot,h));out=at(ep,p,h)
   if age==3:
    assert out[0]>=2
    if out[0]>2:why='remaining_C4_forces_x_above_target3';bound=dict(minimum_later_x=out[0]+1)
    else:
     assert out==(2,3);why='exact_x_budget_forces_after_C4_y3_above_target1';bound=dict(after_only_C4=[3,3,0],minimum_later_y=3)
   else:
    assert out[1]>=4;why='N_zero_C_motion_cannot_lower_y_to_target1';bound=dict(minimum_later_y=out[1])
   roles.append(dict(C_age=age,consumer=G[i]['name'],input_slot=slot,pose=[*p,h],base_endpoint=[*out,h],exclusion=why,**bound))
assert len(roles)==16 and sum(r['C_age']==3 and r['base_endpoint']==[2,3,1]for r in roles)==3
# Age0 has only N zero-C motion from U exit y4, so neither target U y1 nor
# Q's exact cone condition y-4>=x (here1>=3) can hold.
assert qp[1]-4<qp[0]
Qbound=dict(foreign_pose=[3,5,0],only_predecessor=[3,1,0],same_first_successor_common_bud=b,Q_core_local_slot=ql,target_U_before_white_local_slot=[-1,3],target_U_first_read=[22,'R'],excluded_C_ages=[0,4],necessary_C_age_at_least=8)
D=[GP,QP,P,R/'foreign_U_star_predecessors_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'seven_word_spatial_return_2026-10-23/foreign_U_age4_renewal_branch_manifest.json',R/'foreign_renewal_bud_obstruction_2026-10-23/manifest.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Necessary lower clocks for marker-only first-foreign absorption of genuine original U-star tags: only F(3,-2,E) at C age>=7 or Q(3,5,N) at C age>=8 remain. The other residual marker port F(3,3,N) is already excluded by signed actual renewal/bud history. Original tags stay physically black through foreign RAW; successor owns phase1. No attainment at7/8, physical erosion, postforeign permanence, or all-age exclusion is claimed.',remaining_marker_mechanisms=markers,F_clock_bound=Fbound,Q_actual_predecessor_rows=predecessors,first_post_U_common_bud_rows=common,Q_bud_first_consumer_endpoint_rows=roles,Q_clock_bound=Qbound,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'U_marker_clocks.json').write_text(json.dumps(o,indent=2)+'\n');print('Only original-U marker mechanisms: F(3,-2,E) needs>=7Cs; Q(3,5,N) needs>=8Cs. Necessary, not attained.')
