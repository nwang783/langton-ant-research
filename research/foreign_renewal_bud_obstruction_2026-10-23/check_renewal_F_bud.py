"""All-history obstruction to age-four U renewal immediately followed by F.
Finite literal16-input endpoint table plus signed atomic common-bud maturity.
No prefix enumeration or source-tail restriction.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(QP.read_text())['macro_words'];G8=json.loads(GP.read_text())['geometry'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};V=((0,1),(1,0),(0,-1),(-1,0))
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
start=(0,4);bud=(2,4);renew=(3,-1);foreign=(3,3)
assert derive(G[3]['word'])[2:4]==((0,4),0)
common=[]
for i in(0,1,2,3):
 w=G[i]['word'];req,_,_,_,reads=derive(w+M);_,par,p,h,_=derive(w);board={q for q,b in req.items()if b}^par;outputs=board-{place(q,p,h)for q in K}
 assert(2,0)in outputs and reads[(2,0)]==[(8,'R')]
 common.append(dict(atom='DCVU'[i],local_fresh_common_bud=(2,0),fresh_R_phase=8,global_first_post_U_bud=bud))
for b,fs in ((0,(0,1)),(4,(4,5,6)),(7,(7,8,9))):
 for f in fs:assert G8[f]['inputs']==G8[b]['inputs']
rows=[]
for age,h in((3,1),(4,0)):
 for a in(0,4,7):
  dx,dy,dh=G8[a]['endpoint'];assert dh==0
  for slot in G8[a]['inputs']:
   p=sub(bud,rot(slot,h));end=place((dx,dy),p,h)
   row=dict(C_age=age,consumer=G8[a]['name'],input_slot=slot,pose=[*p,h],base_endpoint=[*end,h])
   if age==3:
    assert end[0]>=2
    if end[0]>2:
     row.update(reason='one_remaining_E_to_N_C_forces_x_above_renewal',minimum_later_x=end[0]+1);assert end[0]+1>renew[0]
    else:
     assert end==(2,3)
     row.update(reason='exact_x_budget_leaves_y_at_least3',after_only_possible_C4=[3,3,0],minimum_later_y=3);assert 3>renew[1]
   else:
    assert end[1]>=4
    row.update(reason='zero_C_N_cannot_decrease_y_to_renewal',minimum_later_y=end[1]);assert end[1]>renew[1]
   rows.append(row)
assert len(rows)==16
# Literal endpoint-cone facts used after an early first retirement.
kinematics=[]
for a in(0,4,7):
 x,y,dh=G8[a]['endpoint'];assert dh==0 and x>=0 and y>0
 ex,ey=rot((x,y),1);assert ex>0
 kinematics.append(dict(atom=G8[a]['name'],N_step=[x,y],E_step=[ex,ey]))
assert place((0,1),(0,0),1)==(1,0) # the only remaining C adds1 inx
renew_inputs={place(q,renew,0)for q in G8[7]['inputs']};assert bud not in renew_inputs
renew_req=derive(G[3]['word']+M)[0];local=sub(bud,renew);assert local not in renew_req
assert place(tuple(G8[7]['endpoint'][:2]),renew,0)==foreign
freq,_,_,_,freads=derive(G[4]['word']+M);flocal=sub(bud,foreign)
assert flocal==(-1,1)and freq[flocal]is False and freads[flocal][0]==(14,'R')
# The original star marker-only identity is the intended, now blocked reset.
oldtag=(0,1);tlocal=sub(oldtag,foreign);assert tlocal==(-3,-2)and freads[tlocal][0]==(57,'L')
DP=R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json'
D=[QP,GP,DP,R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',Path(__file__).resolve()]
out=dict(status='AUTHOR_ALL_HISTORY_AGE4_RENEWAL_F_OBSTRUCTION_PENDING_INDEPENDENT_AUDIT',scope='Any actual retained-eight history from genuine creating Ubase through age4 renewing plainU(3,-1,N) cannot continue with immediate F at3,3,N and actual marker. ALLcreating U/UC/UCC tail variants and arbitrary intervening zero-C lengths covered. Does not exclude other foreign poses,6C contact branches, or prove seven-word termination.',creator_U_exit=[0,4,0],first_post_U_atomic_common_bud=bud,atomic_source_clock=0,signed_minimum_first_retirement_age=3,literal_common_bud_rows=common,endpoint_rows=rows,zero_C_kinematics=kinematics,renewing_U_pose=[3,-1,0],renewing_U_input_cells=sorted(renew_inputs),foreign_pose=[3,3,0],foreign_conflicting_cell=bud,foreign_local_conflicting_cell=flocal,foreign_first_read=[14,'R'],blocked_original_star_marker_tag=oldtag,blocked_tag_successor_raw_phase=1,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'renewal_F_bud_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print('Universalage4 U-renewal→F blocked by genuine commonbud(2,4);16 endpoint rows')
