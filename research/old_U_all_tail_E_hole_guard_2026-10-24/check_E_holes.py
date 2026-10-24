"""All-tail old-U E-heading first-contact; physical restoration/CORE included.
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
 r=next(r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='U'and r['contact_atom']==atom);kk=[k for k in r['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==1];assert kk==[1];ar.append(r)
a,b=chord('U',(0,0,0));u=sub(b,a);LEFT={(0,0),(0,1)};geo=[]
for atom in'DCVU':
 c,d=chord(atom,(0,0,1));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y+1)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=Q(det(q,v),den),Q(det(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   bad=[];tr=l.trace(W[atom]+l.M)
   for tag in sorted(LEFT):
    local=l.rot(sub(tag,(x,y)),-1);f=tr['first'].get(local)
    if local in l.K or f and f[0]=='R':bad.append(dict(SAME_LEFT=tag,local=local,role='ENTRY_CORE'if local in l.K else'first_WHITE',first=f,owner=o.describe(atom,f[1])if f else None))
   geo.append(dict(actor=atom,ENTRY=(x,y,1),old_U_parameter=str(s),new_positive_parameter=str(t),total_ordinary_C_before_actor_ENTRY=1,SAME_LEFT_contradictions=bad))
assert len(geo)==18;surv=[r for r in geo if not r['SAME_LEFT_contradictions']];assert{(r['actor'],tuple(r['ENTRY']))for r in surv}=={('D',(-1,0,1)),('V',(-3,0,1)),('U',(-4,-1,1)),('U',(-2,-1,1))}
# Fresh physical WHITE holes, not surviving output identities. Their actual
# source U lastL resets every older BLACK lifetime; replacements are allowed
# and classified by actual finalR, including all EXIT CORE writes.
lastU=l.trace(W['U'])['last'];holemap={('D',(-1,0,1)):(-1,1),('V',(-3,0,1)):(-1,-1),('U',(-4,-1,1)):(-1,-1),('U',(-2,-1,1)):(0,-1)};targets=[]
for r in surv:
 p=tuple(r['ENTRY']);g=holemap[r['actor'],p];fr=l.trace(W[r['actor']]+l.M)['first'][l.rot(sub(g,p[:2]),-1)];assert lastU[g][0]=='L'and fr[0]=='L'and fr[1]<len(W[r['actor']]);targets.append(dict(geometry=r,actual_source_U_hole=g,actual_source_last_L_tick0=lastU[g][1],actual_source_last_L_read1=lastU[g][1]+1,target_local=l.rot(sub(g,p[:2]),-1),actual_target_first_BLACK=fr,actual_target_owner=o.describe(r['actor'],fr[1])))
# Genuine physical RAW-final R slots, not merely residual O. This explicitly
# includes every actual CORE R origin that might repair a deleted hole.
RR={a:[dict(slot=q,actual_RAW_last_R_tick0=t,actual_RAW_last_R_read1=t+1,in_RAW_EXIT_CORE=l.rot(sub(q,after(W[a])[:2]),-after(W[a])[2])in l.K)for q,(c,t)in l.trace(W[a])['last'].items()if c=='R']for a in'DCVUFQB'}
# Old source-toFOREIGN C clock n is0/1, not totalK used as a new age.
# Before firstFOREIGN, genuine completed creator is U(n0), U/UC(n1);
# UCC has already used2. All later N heads y>=4; every W head y>=5.
# All raw finalR minimum local y>=0, minimum local x>=-1, including CORE.
prebounds=[]
for atom in'DCVU':
 assert min(r['slot'][1]for r in RR[atom])>=0 and min(r['slot'][0]for r in RR[atom])>=-1
 prebounds.append(dict(RAW=atom,all_physical_last_R_slots=RR[atom],N_head_y_ge4_implies_write_y_ge4=True,W_head_y_ge5_implies_write_y_ge4=True))
# All possible FOREIGN finalR funders for all3 holes at n0. N zero-run
# counts solve exact source-U-EXIT endpoint equations; y bounds make this
# an exact arithmetic classification, not a rail/depth cap.
holes=sorted(set(holemap.values()));foreN=[];Nmodels=[]
for A in'FQB':
 for r in RR[A]:
  q=tuple(r['slot'])
  for g in holes:
   X=g[0]-q[0];Y=g[1]-q[1]-4;models=[]
   if min(X,Y)>=0:
    for nu in range(Y//4+1):
     if(Y-X-4*nu)%2:continue
     nv=(Y-X-4*nu)//2;nd=X-nv
     if min(nd,nv)<0:continue
     assert A=='B'and g==(-1,1)and nv==nu==0 and nd in(1,2);m=dict(N_D_count=nd,N_V_count=nv,N_U_count=nu,forced_old_zeroC_run='D'*nd,actual_FOREIGN_predecessor='D',route='signed_full_D_to_B_literal_pair_impossible');models.append(m);Nmodels.append(dict(foreign=A,hole=g,slot=q,actual_R=r,model=m))
   foreN.append(dict(foreign=A,hole=g,physical_final_R=r,exact_N_endpoint_X=X,exact_N_endpoint_Y=Y,all_nonnegative_integer_count_models=models))
assert len(Nmodels)==2
# n1 plain-U creator has its first C in a later producer: W beginsy>=6;
# nonempty W firstD/V is mandatory (CU and C->FORE are literal-impossible),
# so actualFOREIGN W entryy>=7. Its physical R localx>=-5 gives writey>=2.
assert all(min(r['slot'][0]for r in RR[A])>=-5 for A in'FQB')
# n1 UC creator W starts0,5. First W baseD/V forces d+v>=1. Exact W
# head=(-d-3v-4u,5+d+v), then rotatedFORE physical finalR. Four models.
foreW=[];Wmodels=[]
for A in'FQB':
 for r in RR[A]:
  q=tuple(r['slot'])
  for g in holes:
   S=g[1]-q[0]-5;T=-g[0]-q[1];models=[]
   if S>=1 and T>=0:
    for nu in range(T//4+1):
     if(T-S-4*nu)%2:continue
     nv=(T-S-4*nu)//2;nd=S-nv
     if min(nd,nv)<0:continue
     assert g==(-1,1)
     if(nd,nv,nu)==(0,1,0):
      assert A in'FQB';word='UCV'+A;route='signed_plain_V_to_B_pair_impossible'if A=='B'else'exact_UCV_FOREIGN_RAW_R52_conflicts_with_source_U_R21'
     else:
      assert A=='Q'and(nd,nv,nu)==(1,0,1);word='UCDUQ';route='CU_forces_firstD_thenU_and_exact_UCDUQ_RAW_R52_conflicts_with_source_U_R21'
     tt=l.trace(''.join(W[a]for a in word)+l.M);assert not tt['feasible'];m=dict(W_D_count=nd,W_V_count=nv,W_U_count=nu,forced_actual_whole_subword=word,route=route,actual_literal_conflict=tt);models.append(m);Wmodels.append(dict(foreign=A,hole=g,physical_final_R=r,model=m))
   foreW.append(dict(foreign=A,hole=g,physical_final_R=r,exact_W_d_plus_v=S,exact_W_d_plus3v_plus4u=T,all_integer_count_models_with_d_plus_v_ge1=models))
assert len(Wmodels)==4
# General exact zero-C E endpoint semigroup. This certifies unlimited
# ordinary length by nonnegative counts, not a fixed number of atoms.
def Ecounts(ep,p):
 dx=p[0]-ep[0];drop=ep[1]-p[1];out=[]
 if dx<0 or drop<0:return out
 for nv in range(drop+1):
  nd=drop-nv;rem=dx-nd-3*nv
  if rem>=0 and rem%4==0:out.append(dict(D=nd,V=nv,U=rem//4))
 return out
postE=[];postS=[];postC=[];Crepairs=[]
for tar in targets:
 p=tuple(tar['geometry']['ENTRY']);g=tuple(tar['actual_source_U_hole'])
 for atom in'DVU':
  ee=after(W[atom])
  for rr in RR[atom]:
   off=l.rot(sub(ee[:2],rr['slot']),1);ep=add(g,off);assert off[0]>=0
   models=Ecounts(ep,p);assert not models
   postE.append(dict(target=tar['geometry'],hole=g,writer_RAW=atom,physical_final_R=rr,actual_writer_heading='E',writer_RAW_EXIT=(*ep,1),all_zeroC_E_endpoint_count_models=models,route='physical_R_exit_cannot_reach_actual_target_by_E_semigroup'))
   offS=l.rot(sub(ee[:2],rr['slot']),2);assert offS[1]<=0;epS=add(g,offS)
   if offS[1]==0:assert offS[0]in(0,1)
   if p[1]>=g[1]:why='S_RAW_exit_y_le_hole_y_then_actual_S_to_E_C_lowers_once_below_target'
   else:
    assert tar['geometry']['actor']=='D'and g==(-1,1)and p==(-1,0,1)
    if offS[1]<0:why='S_RAW_exit_y_le0_then_required_C_lowers_below_target_y0'
    elif offS[0]==1:
     assert epS==(0,1);why='S_equal_y_forces_no_S_base_beforeC_then_E_starts_x0_right_of_target_x_minus1'
    else:
     assert epS==g==(-1,1)and z((*epS,2))==(-1,3);why='S_equal_y_RAW_EXIT_is_earlier_old_U_midpoint_return_before_C_or_target'
   postS.append(dict(target=tar['geometry'],hole=g,writer_RAW=atom,physical_final_R=rr,actual_writer_heading='S',writer_RAW_EXIT=(*epS,2),route=why,one_remaining_C_after_S_writer_is_actual_S_to_E=True))
 # Exactly the one postFOREIGN C, if it is the finalR writer. It startsS,
 # endsE; CORE R4 is explicitly retained rather than discarded as O-only.
 ec=after(W['C'])
 for rr in RR['C']:
  off=l.rot(sub(ec[:2],rr['slot']),2);ep=add(g,off);models=Ecounts(ep,p);x=dict(target=tar['geometry'],hole=g,physical_C_final_R=rr,actual_writer_heading='S',writer_RAW_EXIT=(*ep,1),all_E_continuation_count_models=models)
  if models:
   assert tar['geometry']['actor']=='D'and rr['slot']==(0,0)and rr['actual_RAW_last_R_tick0']==4 and models==[dict(D=0,V=0,U=0)]
   hp=add(g,l.rot(rr['slot'],0)); # slot0,0: actual C head is g
   assert hp==(-1,1);cp=(*hp,2);assert z(cp)==(-1,3)
   w=(0,1);loc=l.rot(sub(w,hp),-2);assert loc in l.K
   x.update(route='real_C_RAW_R4_CORE_repair_but_its_ENTRY_is_earlier_source_U_midpoint_return',actual_C_ENTRY=cp,old_U_contact_parameter='1/2',actual_source_U_chord_start=a,actual_C_ENTRY_center=z(cp),SAME_original_LEFT_w_in_C_ENTRY_CORE=dict(cell=w,local=loc),no_FALSE_physical_CORE_write_exclusion=True);Crepairs.append(x)
  else:x['route']='all_physical_C_R_exit_endpoints_fail_exact_zeroC_E_semigroup'
  postC.append(x)
assert len(Crepairs)==1
# The structurally matched W/E U-rail regressions are preserved as real
# negatives, not a finite approximation to the all-length proof.
reg=[]
for word in['UCDUFDDD','UCDUUFUDDD','UCDUUFDUDD','UCDUUFDDUD','UCVUFDVD','UCVUFVDD']:
 tt=l.trace(''.join(W[a]for a in word)+l.M);assert not tt['feasible']and tuple(tt['cell'])==(-1,1)and tt['previous_read']==14;reg.append(dict(word=word,why_chosen='Matched W/E U or D/V endpoint rails to targetD(-1,0,E), not a generic prefix search.',immutable_literal_conflict=tt))
# A real complete prepared CORE rewrite regression, not a U-ancestry
# counterexample. C local0,0 L0/R4 then actual next D ownL1.
cd=l.trace(W['C']+W['D']+l.M);assert cd['feasible'];seed={q for q,(c,t)in cd['first'].items()if c=='L'};black=set(seed);p=(0,0,0);reads=[];life=None;cut=None;death=None
for tick,c in enumerate(W['C']+W['D']+l.M):
 assert(p[:2]in black)==(c=='L');reads.append(dict(tick0=tick,read_number1=tick+1,cell=p[:2],turn=c))
 if c=='L':
  black.remove(p[:2])
  if life is not None and p[:2]==(0,0):death=tick;life=None
 else:
  black.add(p[:2])
  if tick==4:assert p[:2]==(0,0);life=('C',4)
 p=after(c,p)
 if tick+1==len(W['C']):
  assert life==('C',4)and l.rot(sub((0,0),p[:2]),-p[2])in l.K;cut=dict(actual_C_RAW_EXIT=p,SAME_C_R4_alive_CORE=True,not_CURRENT=True)
assert death==16
prepared_core=dict(actual_word='CD+actualM11',complete_finite_black_seed=sorted(seed),all36_actual_fine_reads=reads,C_RAW_R4_birth=dict(cell=(0,0),RAW_tick0=4,RAW_read1=5),actual_C_RAW_EXIT_cut=cut,physical_death_combined_tick0=16,physical_death_owner=o.describe('D',1),no_genuine_old_U_ancestry_or_global_proxy_control_claim=True)
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/check_complete8_foreign_adjacency_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual genuine preFOREIGN U/UC/UCC creator in U-entryG8 before FIRSTF/Q/B, then arbitrary ordinary-only RAW tail with actualfinalM11. At GLOBAL first positive proxy contact old-owned by that outgoing U-base chord, contact actor cannot faceE. All-tail totalC1 slice only; other headings/sourcefamilies and arbitrarytail simplicity remain separate.',all4_signed_angle_rows_forcing_total_C1=ar,true_preFOREIGN_C_age='n is0or1, a genuine subcount of totalK1. UCC completion2 impossible; n0 creator plainU; n1 creator plainU orUC. No postFOREIGN age law.',all18_exact_outgoing_owned_E_geometries=geo,all4_SAME_LEFT_compatible_targets_and_source_deleted_holes=targets,all_physical_RAW_final_R_slots_including_EXIT_CORE=RR,all4_old_N_W_physical_R_coordinate_bounds=prebounds,all_FOREIGN_n0_physical_R_funding_roles=foreN,all2_n0_FOREIGN_funding_count_models=Nmodels,all_FOREIGN_n1_UC_physical_R_funding_roles=foreW,all4_n1_UC_FOREIGN_funding_count_models=Wmodels,plain_creator_U_n1_FOREIGN_funding_guard='FirstC belongs a LATER complete producer: W startsy>=6, nonemptyW beginsD/V becauseCU and C-toFORE forbidden, soFORE heady>=7. EveryFORE finalR localx>=-5 writesphysicaly>=2, above all three holes. This is a physical CORE-inclusive bound, not residualO-only.',all_postFOREIGN_E_physical_R_endpoint_obligations=postE,all_postFOREIGN_S_physical_R_endpoint_obligations=postS,all_postFOREIGN_C_physical_R_endpoint_obligations=postC,sole_real_C_R4_CORE_repair_branch_and_earlier_proxy_return=Crepairs,all6_structurally_matched_rail_negative_regressions=reg,real_prepared_C_R4_alive_CORE_repair_regression=prepared_core,physical_last_R_completeness='Each chosen hole has lastL in genuine sourceU RAW, so every older BLACK lifetime is erased. A target firstL requiresBLACK already at actorENTRY. Select the LAST actual R funding it: if in an earlier RAW its FINAL read there isR. Every physical finalR includingCORE appears. Earlier G8 N/W cannot reach lowhole; FORE funding models are exhausted exactly; postFORE phases S/C/E for n0 or E for n1 are covered by endpoint cones/semigroup. No CORE-only origin is silently dropped.',SAME_LEFT_scope='Signed ages n<=1 give completeFOREIGN context MISS of original4STAR. GLOBAL-first stopping and bf1018 then give SAME LEFT CURRENT at candidateENTRY. Fourteen of18 masks close directly. No RIGHT/q/currentness through contact or postFORE maturation is used.',conclusion='No E-facing GLOBAL-first ordinary contact with an outgoing preFOREIGN genuine U-base source at ANY tail index. In particular all four uncut D/V/U actors are blocked by exact physical last-R restoration obligations.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'E_holes.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU all-tail E:18 geometry→14 SAMELEFT+4 sourceholes. FORE origin219-class exact2+4 models; all S/C/E finalR/CORE origins cut, one actualC-R4 repair returns oldU midpoint before target.')
