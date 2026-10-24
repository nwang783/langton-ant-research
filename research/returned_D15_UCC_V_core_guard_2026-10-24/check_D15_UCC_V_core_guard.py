"""Genuine UCC,V boundary cannot repair a deleted core for the D15 reset.
No returned simplicity, postforeign age law, or generic prefix enumeration.
"""
from pathlib import Path
from collections import Counter
from itertools import permutations
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';XP=R/'returned_D_entry_controls_2026-10-24/D_entry_controls.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());X=json.loads(XP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));mp={a:i for i,a in enumerate('DCVUFQB')};b=(2,0);bp=(3,1);g=(0,0);g1=(0,1);gm=(-1,-1);young_deleted=(0,-1);previous_bud=(1,-1)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def derive(w,stop=False):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(w):
  initial=(ch=='L')^(p in par)
  if p in rq and rq[p]!=initial:
   if stop:return dict(tick=t,cell=p,first=first[p],required_initial=initial)
   raise AssertionError((t,p))
  if p not in rq:rq[p]=initial;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);ctx,_,_,_,_=derive(W[i]['word']+M);outs={q for q in rq if rq[q]^(q in par)}-{at(z,ep,dh)for z in K};assert all(q[1]>=0 and sum(q)>=0 for q in outs);AT.append(dict(name='DCVU'[i],endpoint=ep,turn=dh,outputs=outs,context=ctx))
def endpoints(identity,target,foreign,case):
 out=[]
 for gi in(0,4,7):
  for slot in map(tuple,G[gi]['inputs']):
   p=sub(identity,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);dx=target[0]-ep[0];down=ep[1]-target[1];sol=[];allowed=('V','U')if foreign in('F','Q')else('U',)
   for v in range(max(down+1,0)):
    d=down-v;rem=dx-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and a in allowed];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert ep!=target and all(not z['allowed_last']for z in sol),(identity,target,gi,slot,sol)
   out.append(dict(case=case,identity=identity,clearer=G[gi]['name'],input_slot=slot,entry=[*p,1],endpoint=ep,foreign_entry=target,all_E_run_counts=sol))
 return out

# Actual preceding UCC then plain V, in selected-D frame.
xp=(-2,2);xh=2;hp=(-1,-3);hh=0;dp=(0,0);foreign=(2,-5)
assert at(tuple(G[9]['endpoint'][:2]),xp,xh)==hp and (xh+G[9]['endpoint'][2])%4==0
assert at(tuple(G[4]['endpoint'][:2]),hp,hh)==dp
hole=(-2,-4);hr,_,_,_,hreads=derive(W[2]['word']);assert hreads[(-1,-1)]==[[2,'L']]
assert at((-1,-1),hp,hh)==hole
# All actual marked-cut BLACK births are included, not just residual outputs.
L={at(t,xp,xh) for t in ((0,0),(0,1),(1,0),(1,1))}
Hr=at((0,0),hp,hh);HB=at((1,0),hp,hh);Hb=at((2,0),hp,hh)
assert (Hr,HB,Hb)==((-1,-3),(0,-3),(1,-3))
held=L|{Hr,HB,Hb,previous_bud,b,bp}
assert len(held)==10
endpoint_rows=[]
for tag in (Hb,previous_bud,b,bp):endpoint_rows.extend(endpoints(tag,foreign,'F',15))
assert len(endpoint_rows)==32
# Last possible preforeign full packet is V or U. Both need hole BLACK in core.
last=[]
for gi in (4,7):
 en=tuple(G[gi]['endpoint'][:2]);p=sub(foreign,rot(en,1));local=rot(sub(hole,p),-1);rq,_,_,_,reads=derive(G[gi]['word'])
 assert local in K and rq[local] is True and reads[local][0][1]=='L'
 last.append(dict(packet=G[gi]['name'],entry=[*p,1],hole_local=local,first_hole_RAW_tick0=reads[local][0][0],first_hole_RAW_read_number1=reads[local][0][0]+1))
# H exits at D entry(0,0,N). N0 heads y>=0, W1 H>=1.
# Every actual final-R slot, including exit-core, has y>=0 and x+y>=0.
roles=[];raw=[]
for i in range(4):
 rq,par,en,turn,reads=derive(W[i]['word']);ctx=derive(W[i]['word']+M)[0];fresh={q for q,rr in reads.items() if rr[-1][1]=='R'};exitK={at(q,en,turn)for q in K}
 assert all(q[1]>=0 and sum(q)>=0 for q in fresh)
 raw.append(dict(name='DCVU'[i],endpoint=en,turn=turn,context=ctx,fresh=fresh,exitK=exitK,reads=reads))
assert hole[1]<0 and hole[1]-hole[0]<1
for h in (2,1):
 for a in raw:
  for slot in sorted(a['fresh']):
   p=sub(hole,rot(slot,h));en=at(a['endpoint'],p,h);hits=sorted(held&{at(q,p,h)for q in a['context']});core=slot in a['exitK']
   if (sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='genuine_held_UCC_or_V_or_D_bud_complete_context_contact'
   elif h==2 and a['name']=='C':
    assert slot==(0,2) and p==(-2,-2) and en==(-2,-3) and core;why='C3_core_repair_forces_E_endpoint_minus2_minus3'
   elif h==2:
    assert (a['name'],slot,p,en) in (('V',(0,2),(-2,-2),(-3,-5)),('U',(-1,3),(-3,-1),(-3,-5))) and core
    why='S2_core_repair_exits_y_minus5_then_C3_below_foreign'
   elif a['name']=='C':why='E_C4_completion_after_foreign_clock3'
   elif a['name']=='V' and slot==(0,1):
    assert p==(-3,-4) and en==(0,-5) and not core;why='E3_residual_origin_cannot_cover_horizontal_gap2_at_same_y'
   elif a['name']=='U' and slot==(-1,2):
    assert p==(-4,-5) and en==(0,-5) and not core and a['reads'][slot]==[[13,'L'],[21,'R']]
    why='not_earliest_BLACK_cut_same_true_input_needs_earlier_BLACK_cut'
   else:
    assert (a['name'],slot,p,en) in (('D',(2,1),(-3,-2),(-2,-3)),('V',(2,3),(-5,-2),(-2,-3)),('U',(1,4),(-6,-3),(-2,-3))) and core
    why='E3_core_repair_forces_E_endpoint_minus2_minus3'
   roles.append(dict(heading=h,atom=a['name'],last_R_local=slot,last_R_tick0=a['reads'][slot][-1][0],last_R_read_number1=a['reads'][slot][-1][0]+1,birth_is_exit_core=core,pose=[*p,h],endpoint=en,held_tag_contacts=hits,reason=why))
assert len(roles)==72
# From E endpoint(-2,-3), foreign(2,-5) forces exactly D,V or V,D.
# V,D has forbidden lastD. D,V first consumes original H r at(-1,-3).
firstD=(-2,-3);assert at((0,1),firstD,1)==Hr
solutions=[]
for v in range(3):
 d=2-v;rem=4-d-3*v
 if rem<0 or rem%4:continue
 solutions.append(dict(d=d,v=v,u=rem//4))
assert solutions==[dict(d=1,v=1,u=0)]
# The residual-origin endpoint(0,-5) cannot reach F2,-5: only U preserve y,
# but their horizontal displacement is a multiple of4, not2.
assert (foreign[0]-0)%4!=0
from collections import Counter
D=[GP,QP,R/'returned_D_Jordan_ancestry_horizon_2026-10-24/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Excludes ONLY D15 finite-horizon boundary UCC,plainV,selectedD(D/DC), for arbitrary genuine earlier history and arbitrary later old-eight connector to F2,-5E returnedC. Uses genuine source UCC leftstar/V cohort and actual deleted CORE BLACK repair. All72 final-R roles include active-core writes; no postforeign maturity or residual-only rebirth shortcut.',actual_boundary=dict(UCC=[*xp,xh],V=[*hp,hh],selected_D=[0,0,0],UCC_entry_C_clock=-2,V_D_entry_C_clock=0,first_foreign_C_clock=3),deleted_core_cell=hole,actual_H_deletion=dict(local_cell=[-1,-1],RAW_tick0=2,RAW_read_number1=3),held_current_tags=sorted(held),all32_target_specific_bud_clearer_endpoint_obligations=endpoint_rows,two_possible_last_foreign_predecessors=last,all72_S_E_final_R_BLACK_cut_birth_roles=roles,role_counts=dict(Counter(x['reason']for x in roles)),sole_core_repair_E_run_counts=solutions,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D15_UCC_V_core_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('D15 UCC,V boundary blocked:72 last-R roles (including core),32 held-bud endpoints, all actual last packet core requirements.')
