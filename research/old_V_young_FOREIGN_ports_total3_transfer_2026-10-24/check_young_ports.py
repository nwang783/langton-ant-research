"""Young V-to-foreign port exclusions and portable TOTAL3 coupled transfer.
No trajectory depth cap, no generic CURRENT field across a reading foreign.
"""
from pathlib import Path
from fractions import Fraction as F
from math import floor,ceil
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('l','word_stabilization/check_foreign_return_interfaces.py');o=ld('o','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(A,p):return z(p),z(after(W[A],p))
def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def curcuts(A,p,tags):
 tr=l.trace(W[A]+l.M);out=[]
 for tag in sorted(tags):
  loc=rel(tag,p);f=tr['first'].get(loc)
  if loc in l.K or f and f[0]=='R':out.append(dict(SAME_CURRENT_tag=tag,local=loc,ENTRY_CORE=loc in l.K,actual_first=f,actual_owner=o.describe(A,f[1])if f else None))
 return out
from itertools import permutations,product
RES={(0,0),(1,0),(2,1),(2,2)}
# Finite count universes are forced by each exact FOREIGN input pose.
def Nmodels(p):
 X=p[0]-1;Y=p[1]-3;out=[]
 if min(X,Y)<0:return out
 for un in range(Y//4+1):
  if(Y-X-4*un)%2:continue
  vn=(Y-X-4*un)//2;dn=X-vn
  if min(dn,vn)>=0:out.append(dict(N_D=dn,N_V=vn,N_U=un))
 return out
def NWmodels(p):
 Y=p[1]-4;out=[]
 if Y<0:return out
 for un in range(Y//4+1):
  for vn in range(Y//3+1):
   for dn in range(Y+1):
    rem=Y-dn-3*vn-4*un
    if rem<0:continue
    for vw in range(rem+1):
     dw=rem-vw;num=1+dn+vn-dw-3*vw-p[0]
     if num>=0 and num%4==0:out.append(dict(N_D=dn,N_V=vn,N_U=un,W_D=dw,W_V=vw,W_U=num//4))
 return out
rows=[];wordrefs={0:{},1:{}};countmods=Counter()
for n in[0,1]:
 hd=(-n)%4
 for tag in sorted(RES):
  for A in'FQB':
   ctx=l.trace(W[A]+l.M)
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,hd)),hd);rec=dict(SAME_original_V_tag=tag,true_source_V_ENTRY_to_FOREIGN_ENTRY_age=n,FOREIGN=A,ENTRY=p,true_input=slot,owner=o.describe(A,ctx['first'][slot][1]))
    if(sum(p[:2])+hd)%2:rec['route']='sector';rec['all_exact_count_models']=[]
    else:
     ms=Nmodels(p)if n==0 else NWmodels(p);rec['all_exact_count_models']=ms;rec['route']='all_endpoint_forced_whole_RAW_words_conflict'if ms else'no_nonnegative_endpoint_count_solution'
     for m in ms:
      countmods[n]+=1;nn=set(permutations('D'*m['N_D']+'V'*m['N_V']+'U'*m['N_U']));ww=[()]if n==0 else set(permutations('D'*m['W_D']+'V'*m['W_V']+'U'*m['W_U']))
      for ns,ws in product(nn,ww):
       ts=('V',)+ns+(()if n==0 else('C',))+ws+(A,);wordrefs[n].setdefault(ts,[]).append(dict(source_tag=tag,actual_FOREIGN_ENTRY=p,true_input=slot,exact_model=m))
    rows.append(rec)
assert len(rows)==376 and countmods=={0:2,1:37}and len(wordrefs[0])==2 and len(wordrefs[1])==25
words=[]
for n in[0,1]:
 for ts,refs in wordrefs[n].items():
  raw=''.join(W[a]for a in ts);tr=l.trace(raw+l.M);assert not tr['feasible'];words.append(dict(true_FOREIGN_age=n,actual_entire_source_V_to_FOREIGN_RAW_word=ts,all_endpoint_model_backreferences=refs,actual_immutable_literal_conflict=tr,no_initial_board_can_repair_repeated_same_turn_conflict=True))
assert len(words)==27
# New full four-heading transfer: do NOT reuse the n2 certificate's
# structural rejection of S/E stages at earlier foreign ages. Rebuild all
#128 actual firstloss roles with only sector/heldtag/sourcecontact cuts.
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=F(det(q,v),de),F(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t))if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(F(0),lo)),str(min(F(1),hi))])if max(0,lo)<=min(1,hi)else None
joint=[];keep=[]
for tag in sorted(RES):
 for A in'DVU':
  ctx=l.trace(W[A]+l.M)
  for hd in range(4):
   for slot in map(tuple,l.literal_geometry(W[A])['inputs']):
    p=(*sub(tag,l.rot(slot,hd)),hd);ex=after(W[A],p);rec=dict(first_lost_tag=tag,consumer=A,ENTRY=p,true_input=slot,owner=o.describe(A,ctx['first'][slot][1]),RAW_EXIT=ex)
    if(sum(p[:2])+hd)%2:why='sector'
    else:
     cuts=curcuts(A,p,RES-{tag})
     if cuts:rec['other_held_tag_CORE_or_FIRST_WHITE']=cuts;why='other_SOURCE_reserve_ENTRYCORE_or_actual_firstWHITE'
     else:
      cc=contact(*chord('V',(0,0,0)),*chord(A,p))
      if cc:rec['actual_earlier_old_V_contact']=cc;why='earlier_GLOBAL_contact_not_actual_source_adjacency_since_FOREIGN_intervenes'
      else:keep.append(rec);why='same8_firstloss_ports_as_independently_signed_age2_coupled_proof'
    rec['route']=why;joint.append(rec)
assert len(joint)==128 and len(keep)==8
old=json.loads((R/'old_V_all_tail_foreign_age2_coupled_ports_2026-10-24/V_n2.json').read_text());oldkeep=old['all8_only_ordinary_firstloss_ports'];k=lambda r,tagf,pf:(tuple(r[tagf]),r['consumer'],tuple(r[pf]))
assert{k(r,'first_lost_tag','ENTRY')for r in keep}=={k(r,'first_lost_SOURCE_reserve_tag','ENTRY')for r in oldkeep}
assert all(r['ENTRY'][2]in[0,3]for r in keep)
# The genuine K2/N and K3/W loss exits, same held-C read and exact future
#models in old20 obligations do not depend on foreign age2: they begin at
#the FIRSTLOSS's actual RAW exit and use TOTAL3 plus actual reader only.
future=old['all20_exact_post_firstloss_future_obligations'];assert len(future)==20
oldgeo=old['all15_exact_total3_geometries_with_TRUE_age2_not_copied_age3'];geokeys=[dict(actor=g['actor'],ENTRY=g['ENTRY'],TOTAL_C=3,true_FOREIGN_age_corollaries=[0,1],source_geometry_only_from_old15=True)for g in oldgeo];assert len(geokeys)==15
D=[R/'old_V_all_tail_foreign_age2_coupled_ports_2026-10-24/manifest.json',R/'audits/check_old_V_age2_coupled_independent.json',R/'old_V_all_tail_foreign_age3_pair_horizon_2026-10-24/manifest.json',R/'audits/check_old_V_age3_horizon_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'full_packet_CURRENT_internal_RAW_lift_2026-10-24/manifest.json',R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24/C_CORE_wording_manifest.json',R/'audits/check_old_U_S4_D_coupled_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in D),[str(p)for p in D if not p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',port_lemma_scope='Genuine RAW V source0N, followed only ordinary RAWs with exactly0or1 C, then a complete F/Q/B+actualM11. For coordinate tags r0,0/B1,0/C2,1/bud2,2, no actual nextFOREIGN TRUE input can occur there. This TRUEinput portion is literal/endpoint only, no U ancestry/simple/globalfirst/age. If the SAME tags are independently CURRENT beforeFOREIGN, ENTRYCORE/firstWHITE is also impossible, hence COMPLETEcontextMISS.',all376_actual_young_FOREIGN_source_tag_TRUEinput_roles=rows,all27_endpoint_exhaustive_whole_words_and_literal_failures=words,all0_and1_C_count_model_counts=dict(countmods),actual_source_full_word_completion='For oldV corollary, sourceV eligible at0; sourceV/VC eligible at1; sourceVCC needs2 and is not silently completed earlier. Whole words start at actual Vbase and retain any ownC or later containingC, so no rawC_FOREIGN ban is assumed.',portable_transfer_scope='Conditional four-tag reserve: genuine past Vbase and one interveningFOREIGN, all4 SAME tags CURRENT before it and completeFOREIGNMISS. Ordinary suffix only; at TOTALC3 outgoing-old-V GLOBALfirstcontact (15 exact W heads), earlier prefix simple. All128 fourheading firstloss roles are sector/current-other-tag/sourcecontact except8 N2/W3 ports. Their20 exact postloss endpoint/read obligations from signed0af do not depend on trueFOREIGNage2. Hence15 targets excluded, for trueFOREIGNages0/1 as well as the original2. No produced age is used afterFOREIGN.',all128_full_four_heading_first_CURRENT_loss_roles=joint,all8_firstloss_ports_set_equal_signed0af=keep,all20_signed_postloss_obligations_copied_without_foreign_age_assumption=future,all15_target_geometries_for_oldV_n0_n1_TOTAL3_corollary=geokeys,actual_new_young_corollary_current_funding='For oldV beforeFIRSTFOREIGN, r5/B4/Cbud-through3 supply the SAME4 CURRENT beforefore0/1. Actual own tails preserve births and completion clocks. The young literal port lemma therefore supplies genuine COMPLETEFOREIGNMISS4; the conditional transfer then closes TOTAL3 trueages0/1 at arbitrary suffix index.',scope_limits=['No tag is inferred CURRENT from black color alone','No fourtag reserve is carried through a foreign that consumes one','The n2 firstloss S/E heading exclusions are NOT reused; new128 table reconstructs those headings directly','No n>=3 pair-clock impossibility is imported','No general all-clock V or arbitrarytail simplicity statement','No generic prefix search: only endpoint-exhaustive integer count models and all permutations of their exact bounded multisets'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'young_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('Young V ports:376 roles=>2+37 exact count models=>27 immutable failed words. Fresh full128 transfer=>same8 ports and20 signed age-independent futures; closes oldV TOTAL3 n0/1 conditionally on genuine funding.')
