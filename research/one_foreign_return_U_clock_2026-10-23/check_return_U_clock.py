"""One first foreign, then returned U/UC(-1,5,S): exclude foreign clock4.
Finite atomic-output and actual C-tail interfaces only. No prefix enumeration.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def derive(w):
 p=(0,0);h=0;par=set();rq={};rd={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in rq or rq[p]==b;rq[p]=b;rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);cr,_,_,_,_=derive(W[i]['word']+M)
 outs={q for q in rq if rq[q]^(q in par)}-{at(q,ep,dh)for q in K}
 if i in(0,2,3):assert outs==set(map(tuple,G[{0:0,2:4,3:7}[i]]['outputs']))
 AT.append(dict(name='DCVU'[i],word=W[i]['word'],outputs=outs,endpoint=ep,turn=dh,context=cr,reads=rd))
assert sum(len(a['outputs'])for a in AT)==19
q0=(0,3);white0=(0,4);white1=(2,5);rp=(-1,5);rh=2;terminal=center(rp,rh);assert terminal==(-1,11)
# Genuine source history, not a prepared returned suffix.
ur,_,_,_,urd=derive(W[3]['word']);assert ur[white0]is False and urd[white0][0]==[24,'R'];assert white1 not in ur
first=[]
for a in AT:
 rd=a['reads'];assert rd[(0,-1)]==[[3,'L']];assert rd[(2,1)][0]==[7,'R']
 first.append(dict(atom=a['name'],actual_pose=[0,4,0],actual_C_clock=0,q0_deletion=[3,'L'],known_initial_white_cell_25_first_read=[7,'R']))
for gi in(7,8,9):assert q0 not in set(map(tuple,G[gi]['outputs']))and white0 not in set(map(tuple,G[gi]['outputs']))
cases=[];FOREIGN=[]
for j in(4,5,6):
 _,_,ep,dh,_=derive(W[j]['word']);assert dh==2;ap=sub(rp,ep);ar,_,_,_,ard=derive(W[j]['word']+M);ctx={at(q,ap,0)for q in ar};assert not L&ctx and q0 not in ctx and center(rp,rh)==terminal
 FOREIGN.append(dict(name='DCVUFQB'[j],pose=ap,allowed_last=('V','U')if j in(4,5)else('U',)))
 for gi in(7,8):
  pr,_,_,_,prd=derive(G[gi]['word']+M);assert at((-1,2),rp,rh)==q0 and pr[(-1,2)]is True and prd[(-1,2)][:2]==[[13,'L'],[21,'R']];assert at((-1,4),rp,rh)==(0,1)and prd[(-1,4)][0]==[29,'L']
  sols=[]
  for d in range(ap[0]+1):
   v=ap[0]-d;rem=ap[1]-4-d-3*v
   if rem<0 or rem%4:continue
   u=rem//4;allowed=[n for n,c in(('D',d),('V',v),('U',u))if c and n in FOREIGN[-1]['allowed_last']];sols.append(dict(d=d,v=v,u=u,allowed_last=allowed))
  # These four zero-clock solutions were separately replayed/excluded in the
  # signed original 72-row table; bind rather than reassert a head-only cut.
  cases.append(dict(foreign='DCVUFQB'[j],foreign_pose=[*ap,0],returned=G[gi]['name'],returned_pose=[*rp,rh],returned_lower_q=q0,returned_lower_q_reads=prd[(-1,2)],old_w_first_read=prd[(-1,4)][0],old_w_physical_owner='following RAW phase1; returned U exit-core absorption'if gi==7 else'returned UC C-tail RAW phase1',foreign_complete_context_misses_q0=True,zero_clock_head_solutions=sols,clock4_exclusion='all_q0_rebirth_origins_excluded',necessary_foreign_C_clock_at_least=8))
assert [f['pose']for f in FOREIGN]==[(3,7),(3,9),(2,10)]
# Clocks0/1: after the creating U base, N heads have y>=4 and W heads H=y-x>=5.
# Every actual atomic output has y>=0 and local x+y>=0; hence no q0 birth there.
assert q0[1]<4 and q0[1]-q0[0]<5
for a in AT:assert all(o[1]>=0 and sum(o)>=0 for o in a['outputs'])
# All later possible atomic output roles through clock4. A heading-S base starts
# at2, a heading-S C is C3(start2), heading-E base starts3, E C is C4(start3),
# and heading-N bases start4. N C5 is too late. Sector is sum(p)+h even.
roles=[];surv=[]
for h in(2,1,0):
 for a in AT:
  if h==0 and a['name']=='C':continue
  for o in sorted(a['outputs']):
   p=sub(q0,rot(o,h));hits=sorted({at(z,p,h)for z in a['context']}&L);ep=at(a['endpoint'],p,h)
   if(sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='held_original_U_star_in_actual_complete_context'
   else:
    if h==2:assert a['name']=='C'and(p,o)in(((1,5),(1,2)),((2,4),(2,1)));why='actual_C3_containing_full_packet_input_or_W_cone'
    elif h==1:
     if a['name']=='C':assert p==(0,5);why='C4_entry_center_equals_foreign_terminal'
     elif ep[0]>=3:why='mandatory_C4_adds_x_beyond_all_foreign_entries'
     elif a['name']=='D':assert p==(0,5);why='D_entry_center_equals_foreign_terminal'
     elif a['name']=='U':assert p==(-3,4);why='upper_d_initially_white_at_04_has_age_at_most3_below5'
     else:assert a['name']=='V'and p==(-2,5);why='lower_selected_initially_white_04_only_clock0_origins_are_guarded_V_r_or_U_star'
    else:why='N4_endpoint_zero_C_count_and_allowed_last_full_packet'
    surv.append((h,a['name'],o,p,ep,why))
   roles.append(dict(heading=h,atom=a['name'],output_slot=o,pose=[*p,h],atomic_endpoint=[*ep,(h+a['turn'])%4],held_star_hits=hits,reason=why))
assert len(roles)==54 and len(surv)==13
assert Counter(h for h,*_ in surv)=={2:2,1:7,0:4}
# Literal input and geometric obligations of the seven E roles.
E=[]
for h,name,o,p,ep,why in surv:
 if h!=1:continue
 if name=='C'or name=='D':assert center(p,h)==terminal
 if name=='U'and p==(-3,4):assert at((0,3),p,h)==white0;slot=(0,3);minimum=5
 elif name=='V'and p==(-2,5):assert at((1,2),p,h)==white0;slot=(1,2);minimum=3
 else:slot=None;minimum=None
 if ep[0]>=3:assert ep[0]+1>max(f['pose'][0]for f in FOREIGN)
 E.append(dict(atom=name,pose=[*p,h],endpoint=ep,reason=why,input_slot=slot,known_initial_white_input=white0 if slot else None,required_produced_minimum_age=minimum))
# Full-source clock0 origins of white0=(0,4), for the exceptional E3 V role.
# It is initially white (original creator U R24); source U/UC/UCC outputs miss it.
# At later clock0 N heads y>=5, all full outputs y>=0. At first head(0,4,N),
# only V-family or U-family may output it, as genuine local r=(0,0), born R4.
clock0=[]
for gi in(0,1,4,5,6,7,8,9):
 outs=set(map(tuple,G[gi]['outputs']));assert all(o[1]>=0 for o in outs)
 if(0,0)in outs:
  _,_,_,_,rd=derive(G[gi]['word']);assert rd[(0,0)][-1]==[4,'R'];assert gi in(4,5,6,7,8,9)
  why='V_family_genuine_r_first_retirement_age5'if gi in(4,5,6)else'U_family_genuine_permanent_left_star'
 else:assert gi in(0,1);why='D_family_does_not_output_local_00'
 clock0.append(dict(full_packet=G[gi]['name'],first_possible_entry=[0,4,0],candidate_cell=white0,reason=why))
# Actual C3 tail index. C3 starts at clock2 in heading S. Its containing full
# producer begins either at2 with C3 as first tail, or at1 with C3 second tail.
ctails=[]
for p in((1,5),(2,4)):
 # FIRST tail: DC, VC/VCC, UC/UCC. The second point needs immediately C4:
 # no intervening E base can fit x<=3, and only VCC/UCC supply adjacent CC.
 for base,gi in(('D',0),('V',4),('U',7)):
  bp=sub(p,rot(tuple(G[gi]['endpoint'][:2]),2));ep=at((0,1),p,2)
  if p==(1,5):
   slot={'D':(0,1),'V':(0,3),'U':(-1,4)}[base];assert at(slot,bp,2)==white1;why='known_initial_white_25_input_at_clock2_below_min3_or5'
  elif base=='D':slot=None;why='immediate_C4_needed_but_DCC_is_not_a_retained_full_packet'
  else:
   slot=(1,2)if base=='V'else(0,3);assert at(slot,bp,2)==white1;why='forced_VCC_or_UCC_has_known_initial_white_25_input_at_clock2'
  if slot:assert slot in set(map(tuple,G[gi]['inputs']))
  ctails.append(dict(C3_pose=[*p,2],tail_index=1,containing_base=base,full_entry=[*bp,2],full_entry_C_clock=2,input_slot=slot,initially_white_input=white1 if slot else None,required_produced_minimum_age=5 if base=='U' else 3,reason=why))
 # SECOND tail: VCC or UCC from heading W. Invert actual base + first C.
 for base,gi in(('V',4),('U',7)):
  c2entry=add(p,(1,0));bp=sub(c2entry,rot(tuple(G[gi]['endpoint'][:2]),3));H=bp[1]-bp[0];assert H<5
  ctails.append(dict(C3_pose=[*p,2],tail_index=2,containing_full_packet=base+'CC',full_entry=[*bp,3],full_entry_C_clock=1,W_entry_H=H,required_H_at_least=5,reason='clock1_W_head_halfplane'))
assert len(ctails)==10
# The (2,4,S) C3 endpoint is(2,3,E). Every E zero-C base adds >=1 x,
# while mandatory C4 adds1; foreign x<=3, so C4 must be the very next atom.
assert at((0,1),(2,4),2)==(2,3)
for gi in(0,4,7):assert G[gi]['endpoint'][1]>=1
# Four N4 endpoints versus three foreign entries: arbitrary zero-C lengths are
# solved by delta_x=d+v, delta_y=d+3v+4u, and the signed allowed last packet.
N=[]
for h,name,o,p,ep,why in surv:
 if h!=0:continue
 for f in FOREIGN:
  dx,dy=sub(f['pose'],ep);sol=[]
  for d in range(max(dx+1,0)):
   v=dx-d;rem=dy-d-3*v
   if rem<0 or rem%4:continue
   u=rem//4;last=[n for n,c in(('D',d),('V',v),('U',u))if c and n in f['allowed_last']];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
  assert all(not s['allowed_last']for s in sol)
  N.append(dict(N4_origin_atom=name,origin_pose=[*p,0],endpoint=ep,foreign=f['name'],foreign_entry=f['pose'],all_zero_C_count_solutions=sol,reason='no_solution_with_actual_allowed_last_full_packet'))
assert len(N)==12
D=[GP,QP,ROOT/'one_foreign_return_U_star_2026-10-23/manifest.json',ROOT/'one_foreign_return_U_star_2026-10-23/erratum_manifest.json',ROOT/'one_foreign_return_U_star_2026-10-23/ownership_erratum_manifest.json',ROOT/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json',ROOT/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',ROOT/'core_periodicity_new/genealogy_age5_speed_frozen_20261023_0827/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='A genuine creating U/UC/UCC, uninterrupted complete-eight interval, first foreign COMPLETE context missing original star, and immediately returned U/UC(-1,5,S) absorbing/retiring original w=(0,1), needs foreign source-entry C clock>=8. Clock0 is bound from the signed original72 ancestry table; only clock4 is newly excluded. No postforeign permanence/maturation, returned-atom simplicity, attainment at8 or further age iteration.',six_returned_U_UC_cases=cases,first_actual_atom_source_deletion_and_white_read=first,original_U_initial_white_04_read=urd[white0][0],all54_atomic_q0_output_alignments=roles,seven_E_origins=E,clock0_04_fullproducer_origin_interfaces=clock0,ten_actual_C3_fullproducer_tail_interfaces=ctails,twelve_N4_endpoint_count_obligations=N,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'return_U_clock.json').write_text(json.dumps(o,indent=2)+'\n');print('All6 returned U/UC cases need foreign clock>=8:54 q0 output roles,13 surviving interfaces,10 actual C3 tail-index cases,12 arbitrary-zero-C N4 endpoint equations.')
