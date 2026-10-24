"""All-tail old-U N-heading first-contact; earliest physical BLACK-cut restoration.
Same genuine LEFT, true preforeign funding clock, no postforeign maturation.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('ownership',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,p):return z(p),z(after(W[atom],p))
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];ar=[]
for atom in'DCVU':
 r=next(r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='U'and r['contact_atom']==atom);assert[k for k in r['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==0]==[2];ar.append(r)
a,b=chord('U',(0,0,0));u=sub(b,a);LEFT={(0,0),(0,1)};geo=[]
for atom in'DCVU':
 c,d=chord(atom,(0,0,0));v=sub(d,c);den=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y)%2:continue
   q=sub(add(c,(2*x,2*y)),a)
   if den:
    s,t=Q(det(q,v),den),Q(det(q,u),den)
    if not(0<=s<1 and 0<t<=1):continue
   else:
    if det(q,u):continue
    k=0 if v[0]else 1;s=Q(0);t=Q(-q[k],v[k])
    if not(0<t<=1 and add(q,(t*v[0],t*v[1]))==(0,0)):continue
   bad=[];tr=l.trace(W[atom]+l.M)
   for tag in sorted(LEFT):
    local=sub(tag,(x,y));fr=tr['first'].get(local)
    if local in l.K or fr and fr[0]=='R':bad.append(dict(SAME_LEFT=tag,local=local,role='ENTRY_CORE'if local in l.K else'first_WHITE',first=fr,owner=o.describe(atom,fr[1])if fr else None))
   geo.append(dict(actor=atom,ENTRY=(x,y,0),total_ordinary_C_before_actor_ENTRY=2,old_U_first_contact_parameter=str(s),new_positive_first_contact_parameter=str(t),SAME_LEFT_contradictions=bad))
assert len(geo)==8;keep=[r for r in geo if not r['SAME_LEFT_contradictions']];assert len(keep)==1 and keep[0]['actor']=='U'and keep[0]['ENTRY']==(0,-2,0)
target=(0,-2,0);g=(-1,0);assert l.trace(W['U'])['last'][g]==('L',1);assert sub(g,target[:2])==(-1,2);assert l.trace(W['U']+l.M)['first'][(-1,2)]==('L',13)
# Every physical final-R slot, CORE included; no residual-only rebirth
# assumption. Earliest actual RAW-END BLACK cut starts after sourceU's
# real WHITE RAW-exit cut. If a writer first reads g L, its entry already
# needs BLACK, contradicting the earliest-cut choice.
RR={a:[dict(slot=q,last_R_tick0=t,last_R_read1=t+1,first_physical_read=l.trace(W[a])['first'][q],actual_RAW_EXIT_CORE=l.rot(sub(q,after(W[a])[:2]),-after(W[a])[2])in l.K)for q,(c,t)in l.trace(W[a])['last'].items()if c=='R']for a in'DCVUFQB'}
rows=[];surv={h:[]for h in range(4)}
for h in range(4):
 for atom in'DCVU':
  raw=l.trace(W[atom]);ctx=l.trace(W[atom]+l.M)
  for rr in RR[atom]:
   q=tuple(rr['slot']);p=(*sub(g,l.rot(q,h)),h);ep=after(W[atom],p);r=dict(hypothetical_STRICTLY_EARLIER_writer_RAW=atom,writer_ENTRY=p,physical_final_R=rr,writer_RAW_EXIT=ep)
   if(sum(p[:2])+h)%2:why='wrong_actual_marked_sector'
   elif raw['first'][q][0]=='L':why='first_hole_read_L_requires_BLACK_at_an_earlier_actual_RAW_cut'
   else:
    touched=[]
    for tag in sorted(LEFT):
     local=l.rot(sub(tag,p[:2]),-h);fr=ctx['first'].get(local)
     if local in l.K or fr:
      if local in l.K:how='CURRENT_anchor_cannot_be_in_writer_ENTRY_CORE'
      elif fr[0]=='R':how='SAME_BLACK_anchor_conflicts_with_first_WHITE'
      else:how='TRUE_anchor_input_would_lose_CURRENT_by_writer_RAW_EXIT_including_marker_CORE_capture'
      touched.append(dict(SAME_LEFT_anchor=tag,local=local,actual_first=fr,owner=o.describe(atom,fr[1])if fr else None,exact_contradiction=how))
    if touched:r['independently_CURRENT_before_and_after_earlier_writer_LEFT_contacts']=touched;why='earlier_writer_touches_independently_CURRENT_SAME_LEFT'
    else:why='necessary_earliest_BLACK_cut_origin_after_sector_and_LEFT_and_priorBLACK_filters';surv[h].append(r)
   r['route']=why;rows.append(r)
assert len(rows)==144
assert not surv[2]
assert{(r['hypothetical_STRICTLY_EARLIER_writer_RAW'],tuple(r['writer_ENTRY']))for r in surv[3]}=={(a,(-1,-2,3))for a in'DCVU'}
assert{(r['hypothetical_STRICTLY_EARLIER_writer_RAW'],tuple(r['writer_ENTRY']))for r in surv[1]}=={('D',(-2,1,1)),('V',(-4,1,1)),('U',(-5,0,1))}
assert len(surv[0])==5 and all(r['writer_ENTRY'][1]<4 for r in surv[0])
assert all(tuple(r['writer_RAW_EXIT'])==(-1,0,1)for r in surv[1])
# PreFOREIGN genuineG8 region: N0 headsy>=4, W1 headsy>=5, S2 hasno
# surviving firstBLACK writer. All actual creator C tails are included as
# realC RAWs; no fictitious internal-C marker is introduced.
pre=[]
for h in[0,3,2]:
 for r in surv[h]:
  p=tuple(r['writer_ENTRY'])
  if h==0:assert p[1]<4;route='N0_writer_below_actual_sourceU_RAW_EXIT_y4'
  else:assert h==3 and p[1]==-2;route='W1_writer_below_actual_first_W_y5'
  pre.append(dict(necessary_origin=r,route=route))
assert len(pre)==9
# PostFOREIGN ordinary phases for true preFOREIGN n0/1/2 are respectively
# S0,E1,N2 / E1,N2 / N2, in TOTAL-source C clocks. There is no W phase.
post=[]
for h in[2,1,0]:
 for r in surv[h]:
  atom=r['hypothetical_STRICTLY_EARLIER_writer_RAW'];ep=tuple(r['writer_RAW_EXIT'])
  if h==1:
   assert ep==(-1,0,1);route='one_E_to_N_C_adds_x1_no_E_base_can_intervene_then_N_start0,0_cannot_reach0,minus2'
  elif atom=='C':route='N2_C_writer_would_complete_C3_after_target_ENTRY_clock2'
  else:
   assert ep[1]>=2>target[1];route='N2_BASE_writer_RAW_EXIT_y_ge2_cannot_reach_target_y_minus2_by_zeroN'
  post.append(dict(necessary_origin=r,route=route))
assert len(post)==8
# FOREIGN itself may repair activeCORE. At n0 exact N counts have no
# physical finalR model. At n1 old fullU/UC height yields all writesy>=1.
# At n2 FOREIGN entersS and exitsN; any finalR atg has RAWEXIT_y>=g_y0,
# so no later zeroN rail reaches the stipulated target y=-2.
fore0=[];fore2=[]
for A in'FQB':
 ep=after(W[A]);assert ep[2]==2
 for rr in RR[A]:
  q=tuple(rr['slot']);X=g[0]-q[0];Y=g[1]-q[1]-4;models=[]
  if min(X,Y)>=0:
   for nu in range(Y//4+1):
    if(Y-X-4*nu)%2:continue
    nv=(Y-X-4*nu)//2;nd=X-nv
    if min(nd,nv)>=0:models.append(dict(D=nd,V=nv,U=nu))
  assert not models;fore0.append(dict(FOREIGN=A,physical_final_R=rr,exact_N_zero_run_X=X,exact_N_zero_run_Y=Y,all_nonnegative_N_count_models=models))
  ep2=add(g,sub(q,ep[:2]));assert ep2[1]>=0>target[1];fore2.append(dict(FOREIGN=A,physical_final_R=rr,actual_S_FOREIGN_ENTRY=add(g,q),actual_N_FOREIGN_RAW_EXIT=(*ep2,0),route='all_ZERO_C_N_continuations_raise_y_from_ge0_not_to_minus2'))
 assert min(r['slot'][0]for r in RR[A])>=-5
assert len(fore0)==len(fore2)==73
# Genuine creator completion/height facts. CU is tested literally; the
# complete8-toFORE pair table forces a nonempty W run and final plainV/U.
cu=l.trace(W['C']+W['U']+l.M);assert not cu['feasible']
heights=dict(true_preFOREIGN_n1_plain_creator_U='Actual firstC belongs a later full producer because creator is plainU, so W beginsy>=6; first W base mustD/V (CU impossible), and foreign cannot follow a completeC-tail directly, hence FORE entryy>=7.',true_preFOREIGN_n1_creator_UC='Own C RAW ends0,5,W; W run is nonempty by actual complete8-toFORE pairs and its first baseD/V raisesy, hence FORE entryy>=6.',true_preFOREIGN_n1_creator_UCC='Full source completion2>FOREIGNclock1, impossible.',all_FOREIGN_physical_R_local_x_ge_minus5=True,consequence='Any n1 W-oriented FOREIGN finalR writes globaly>=1, strictly above deleted g_y0.',actual_CU_literal_conflict=cu)
# Exact old two-track controls are regressions only. The new proof does
# not assume no earlier N/W source rails or restrict S/N rails to D/V.
tw=R/'two_track_UCC_F_return_2026-10-24/foreign_covariance_manifest.json';assert tw.exists()
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',tw,R/'audits/check_two_track_foreign_covariance_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual preFOREIGN genuineU-family creator in U-entry completeG8, FIRST completeF/Q/B, then arbitrary ordinary-only RAW suffix with actual finalM11. At GLOBAL first positive contact old-owned by its outgoingU-base chord, no N-facing actor is possible. TotalC2 slice only, no arbitrary-tail simplicity.',all4_signed_angle_rows_forcing_total_C2=ar,all8_exact_outgoing_owned_N_geometries=geo,sole_SAME_LEFT_compatible_actor=keep[0],actual_source_U_deleted_hole=dict(cell=g,source_last_L_tick0=1,source_last_L_read1=2,physical_WHITE_at_actual_source_U_RAW_EXIT=True,target_TRUE_lower_q_local=(-1,2),target_own_first_L_tick0=13,target_own_first_L_read1=14),all_physical_RAW_final_R_slots_including_CORE=RR,all144_earlier_ordinary_first_BLACK_cut_writer_roles=rows,exact_surviving_first_BLACK_origin_counts={str(h):len(v)for h,v in surv.items()},all9_preFOREIGN_ordinary_origin_height_cuts=pre,no_S_heading_ordinary_first_BLACK_origin=True,all8_postFOREIGN_ordinary_origin_deadline_endpoint_cuts=post,all73_n0_FOREIGN_physical_CORE_inclusive_R_origin_queries=fore0,n1_FOREIGN_height_and_source_completion_guards=heights,all73_n2_FOREIGN_physical_CORE_inclusive_R_endpoint_cuts=fore2,earliest_BLACK_cut_logic='Start at actual sourceU RAWEXIT whereg isWHITE. Ifg BLACK at targetENTRY, choose EARLIEST subsequent actual RAWEXIT BLACK cut, including CORE. Ifg unread in thatRAW, priorCUT alreadyBLACK; if firstg readL, priorCUT alreadyBLACK. Otherwise its actual RAWfinalreadR slot appears in144 or the completeFOREIGN table. Prior ordinary writers are STRICTLY before target, so independently SAMELEFT CURRENT at theirENTRY andEXIT excludes ANY anchor touch: literalWHITE/CORE conflict or TRUEinput CURRENTloss including aliveCORE atEXIT. No physical death is substituted for CURRENTloss. The surviving origin endpoints are impossible in an actual path reaching the stipulated target.',LEFT_scope='Signed preFOREIGN star permanence plus firstFOREIGN effect ages<=2 gives COMPLETE contextMISS of four SAME originals. GLOBAL-first stopping and bf1018 give SAME LEFT CURRENT at every relevant simple marked prefix cut through targetENTRY, not through targetRAW. Complete actual contexts are available from actual followingRAW or given finalM11.',no_G8_age_law_across_FOREIGN=True,no_residual_only_rebirth_or_CORE_escape_assumption=True,no_finite_tail_length_or_zero_rail_cap=True,conclusion='Old outgoing preFOREIGN U cannot be source of a N-facing GLOBAL FIRST ordinary proxy contact at ANY tail index after one firstFOREIGN. Only true preFOREIGN n0/1/2, not an age reset, is used.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'N_hole.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU all-tailN:8 heads→7 SAMELEFT+soleU0,-2. Deleted lowerq firstBLACK cut:144 ordinaryCORE-inclusive roles,73+73 FORE queries, all endpoint/height impossible; no age acrossFORE.')
