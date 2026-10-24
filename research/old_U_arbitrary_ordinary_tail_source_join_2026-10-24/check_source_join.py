"""Dependency-only all-tail old U source join, not all-source simplicity.
Rational head boxes are exact finite geometry, not a trajectory depth scan.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import floor,ceil
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('literal','word_stabilization/check_foreign_return_interfaces.py');o=ld('owner','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(A,p):return z(p),z(after(W[A],p))
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];Uangles=[a for a in angles if a['source_class']=='preFOREIGN_ordinary'and a['source_atom']=='U'];assert len(Uangles)==4
E=json.loads((R/'old_U_all_tail_E_hole_guard_2026-10-24/E_holes.json').read_text());N=json.loads((R/'old_U_all_tail_N_hole_guard_2026-10-24/N_hole.json').read_text());WW=json.loads((R/'old_U_all_tail_W_pair_hole_2026-10-24/W_pair_hole.json').read_text())
oldsets={1:{(r['actor'],tuple(r['ENTRY']))for r in E['all18_exact_outgoing_owned_E_geometries']},2:{(r['actor'],tuple(r['ENTRY']))for r in N['all8_exact_outgoing_owned_N_geometries']},3:{(r['actor'],tuple(r['ENTRY']))for r in WW['all18_exact_outgoing_owned_W_geometries']}}
a,b=chord('U',(0,0,0));u=sub(b,a);LEFT={(0,0),(0,1)};boxes=[];allgeo=[]
for ar in Uangles:
 A=ar['contact_atom']
 for K in ar['allowed_C_counts_before_contact_ENTRY']:
  h=(2-K)%4;c,d=chord(A,(0,0,h));v=sub(d,c);de=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bd=[(floor(min(q[k]for q in corners)),ceil(max(q[k]for q in corners)))for k in(0,1)]
  boxes.append(dict(actor=A,total_ordinary_C_before_actor_ENTRY=K,heading=h,exact_rational_parallelogram_corners=[[[x.numerator,x.denominator]for x in p]for p in corners],integer_bounds=bd,parallel=not bool(de)))
  for x in range(bd[0][0],bd[0][1]+1):
   for y in range(bd[1][0],bd[1][1]+1):
    if(x+y+h)%2:continue
    q=sub(add(c,(2*x,2*y)),a)
    if de:
     s,t=Q(det(q,v),de),Q(det(q,u),de)
     if not(0<=s<1 and 0<t<=1):continue
     onset='transverse_outgoing_old_s_lt1_positive_new_t'
    else:
     if det(q,u):continue
     kk=0 if v[0]else 1;s=Q(0);t=Q(-q[kk],v[kk])
     if not(0<t<=1 and add(q,(t*v[0],t*v[1]))==(0,0)):continue
     onset='codirected_parallel_first_onset_at_old_start; earlier_overlap_would_already_be_a_contact'
    p=(x,y,h);ctx=l.trace(W[A]+l.M);cuts=[]
    for tag in sorted(LEFT):
     loc=l.rot(sub(tag,p[:2]),-h);fr=ctx['first'].get(loc)
     if loc in l.K or fr and fr[0]=='R':cuts.append(dict(SAME_original_LEFT=tag,target_local=loc,ENTRY_CORE=loc in l.K,first=fr,actual_owner=o.describe(A,fr[1])if fr else None))
    if cuts:route='direct_SAME_LEFT_at_GLOBAL_first_contact_ENTRY'
    elif K==1:assert(A,p)in{('D',(-1,0,1)),('V',(-3,0,1)),('U',(-4,-1,1)),('U',(-2,-1,1))};route='signed_e366_E1_physical_holes_CORE_inclusive'
    elif K==2:assert(A,p)==('U',(0,-2,0));route='signed_2df_N2_physical_deleted_hole_CORE_inclusive'
    elif K==3:route='signed_75c9_W3_PAIR_and_physical_hole_NEW_donor'
    elif A=='V':assert p==(0,4,2);route='conditional_0aad_S4V_plus_MANDATORY_1d47_immediate_FOREIGN_adjacency_repair'
    else:assert K==4 and A=='D'and p==(0,2,2);route='b224_S4D_coupled_d_arm_bud_reserve'
    allgeo.append(dict(actor=A,ENTRY=p,total_ordinary_C_before_actor_ENTRY=K,old_source_outgoing_s=str(s),new_positive_t=str(t),contact_kind=onset,SAME_LEFT_ENTRY_contradictions=cuts,route=route))
assert len(boxes)==15 and len(allgeo)==50
assert Counter(r['total_ordinary_C_before_actor_ENTRY']for r in allgeo)=={1:18,2:8,3:18,4:6}
assert Counter(r['route']for r in allgeo)=={'direct_SAME_LEFT_at_GLOBAL_first_contact_ENTRY':37,'signed_e366_E1_physical_holes_CORE_inclusive':4,'signed_2df_N2_physical_deleted_hole_CORE_inclusive':1,'signed_75c9_W3_PAIR_and_physical_hole_NEW_donor':6,'conditional_0aad_S4V_plus_MANDATORY_1d47_immediate_FOREIGN_adjacency_repair':1,'b224_S4D_coupled_d_arm_bud_reserve':1}
for K in[1,2,3]:assert{(r['actor'],tuple(r['ENTRY']))for r in allgeo if r['total_ordinary_C_before_actor_ENTRY']==K}==oldsets[K]
leftscope='Actual preFOREIGN true creator age n is a subcount of TOTAL K<=4, not a reset postFOREIGN age. Signed first-effect>=5 excludes any actual firstFOREIGN star retirement or markerCORE capture; actual CURRENT BLACK already excludes ENTRYCORE/firstWHITE. Therefore COMPLETEFOREIGN contextMISS all4 SAME originals. Stop at GLOBAL-first actorENTRY; earlier expandedprefix is simple, so signedbf1018 gives SAME LEFT CURRENT here. No persistence through actor or originalRIGHT/q/shadow seal is claimed.'
# All source routes have independently passed, including the explicit
# S4V adjacency repair and S4D CORE bookkeeping/wording qualifiers. This
# source-level set join still needs its own independent binding.
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_SOURCE_JOIN_REVIEW',scope='Only preFOREIGN genuine outgoing U-base old source at GLOBAL first ordinary proxy contact after FIRSTF/Q/B and arbitrary ordinary-only RAW tail plus actual finalM11. Actor index unrestricted. Other oldD/C/V source classes remain open and no arbitrarytail simplicity follows.',all4_signed_arbitrary_tail_old_U_angle_rows=Uangles,actual_total_clock_and_LEFT_scope=leftscope,all15_exact_contact_head_boxes=boxes,all50_outgoing_owned_old_U_contact_geometries_and_routes=allgeo,route_counts=dict(Counter(r['route']for r in allgeo)),old_SOURCE_own_UC_UCC_tails_are_not_new_G8_reset='Selected outgoingU is actual U-base of a genuine preFOREIGN U/UC/UCC fullpacket. Each source-family branch and actual ownC shift remains in its independently checked package; TOTALclock begins at its U-base/fullpacket ENTRY.',outgoing_owner_convention='Old s=1 belongs to actual outgoing next source, not incomingU. New t=0 is an earlier vertex return already present at actorENTRY, not a fresh positive onset. ParallelN2 actorU retains exact first overlap onset at old s=0, new t>0. Actual GLOBAL earliest contact supplies simple prefix, not a prior arbitrary-tail simplicity theorem.',mandatory_corrections='Original0aad omitted immediateUFOREIGN adjacency and remains incomplete alone; its conditional finite/analytic report plus separate1d47 repairs compose here. Rejected143d universalFpair/full84 remains rejected. Only45abc strict-lowerN4 field is used by1d47, leaving genuine y=-1 CORE controls valid.',no_post_FOREIGN_maturity_or_original_STAR_permanence=True,no_all_source_or_second_FOREIGN_closure=True)
D=[R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'old_U_all_tail_E_hole_guard_2026-10-24/manifest.json',R/'audits/check_old_U_all_tail_E_holes_independent.json',R/'old_U_all_tail_N_hole_guard_2026-10-24/manifest.json',R/'audits/check_old_U_all_tail_N_hole_independent.json',R/'old_U_all_tail_W_pair_hole_2026-10-24/manifest.json',R/'audits/check_old_U_all_tail_W_independent.json',R/'old_U_all_tail_S_V_foreign_effect_2026-10-24/manifest.json',R/'audits/check_old_U_all_tail_S_V_independent.json',R/'old_U_S4_V_immediate_FOREIGN_2026-10-24/manifest.json',R/'audits/check_old_U_S4_V_adjacency_independent.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out['explicit_S4V_composition']='The original0aad is independently checked CONDITIONAL on a real next ordinary full base beforeFOREIGN, not a standalone complete proof. Separate signed1d47 excludes the actual immediateU-F/Q/B adjacency. Together the next-base funnel is exhaustive. No original file or failed claim is overwritten.'
out['mandatory_S4D_current_CORE_qualifications']='Use b224 only with8d68 internal-RAW identity lift and f393 C exitCORE wording precision. Three external C capture sites are first-WHITE; two are already ENTRYCORE first-L. Do not conflate CURRENT loss into CORE with physical death.'
out['dependencies']={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D}
(H/'source_join.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU all-tail source join:50 exact geometry=37 LEFT+4 E+1 N+6 W+1 correctedV+1 qualifiedD; source-level independent review remains.')
