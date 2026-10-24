"""Old-V THIRD true age2: genuine before-FOREIGN base field, incoming bud, and actual A-or-helper branch. No age after A."""
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
from collections import Counter
RBASE={(0,0),(1,0),(2,0),(2,1),(2,2)};Acell=(0,1);beta=(1,-1);GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];sourcefacts=[]
for src in(4,5,6):
 tr=l.trace(G[src]['word']);assert RBASE|{Acell}<=set(map(tuple,G[src]['outputs']));assert beta not in tr['first']
 facts=[]
 for cell,tick in(((0,0),4),((1,0),9),((2,0),8),((2,1),7),((2,2),16),((0,1),11)):
  assert tr['last'][cell]==('R',tick);proof='original-A-current branch only'if cell==Acell else'signed2036 first loss5'if cell==(0,0)else'signed2043 first loss4'if cell==(1,0)else'signed1344 atomic common minimum3'if cell==(2,0)else'signed358 exact source-tail output queries ages0..3'
  facts.append(dict(SAME_base_output_cell=cell,birth_tick0=tick,birth_read_number1=tick+1,own_C_tails_preserve_source_R=True,preFOREIGN_current_rule=proof))
 sourcefacts.append(dict(actual_full_source=G[src]['name'],actual_SOURCE_ENTRY_clock=0,actual_SOURCE_completion_clock=G[src]['name'].count('C'),true_FOREIGN_clock=2,all_base_current_or_original_A_branch_facts=facts))
# Every actual previous FULL packet contributes its genuine final atomic
# EXIT bud at the selected old-V ENTRY, not at its older full ENTRY clock.
prior=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 word=''.join(W[x]for x in full);ep=after(word);slot=add(ep[:2],l.rot(beta,ep[2]));tr=l.trace(word);geo=l.literal_geometry(word);assert tr['last'][slot]==('R',len(word)-2)and list(slot)in geo['outputs'];prior.append(dict(actual_previous_full=full,previous_full_ENTRY_clock=-full.count('C'),actual_final_atomic_EXIT_clock=0,true_post_EXIT_age_at_FOREIGN=2,actual_full_ENTRY_age_at_FOREIGN=2+full.count('C'),SAME_incoming_beta_in_old_V_chart=beta,actual_previous_full_output_slot=slot,actual_last_R_tick0=len(word)-2,birth_read_number1=len(word)-1,proof='signed1325 postEXIT consumer-start minimum3; own old-V/C tails preserve this old current residual'))
# If original A is absent before Aclock2, signed2043 forces real V/VC
# H0,4S atclock2. Full H must COMPLETE before Aclock2, hence only plain V.
helper=[];hgeo=l.literal_geometry(W['V']);htr=l.trace(W['V'])
for q in map(tuple,hgeo['outputs']):
 cell=add((0,4),l.rot(q,2));turn,tick=htr['last'][q];assert turn=='R';helper.append(dict(SAME_genuine_helper_output_cell=cell,helper_base_output_slot=q,helper_R_tick0=tick,helper_R_read_number1=tick+1,actual_helper_full='V',actual_helper_ENTRY_pose=(0,4,2),actual_helper_ENTRY_clock=2,completion_clock=2,true_helper_age_at_FOREIGN=0,current_rule='all23 produced inputs minimum>=2, used only within old complete8 before FORE entry'))
assert len(helper)==6 and set(r['SAME_genuine_helper_output_cell']for r in helper)=={(0,4),(0,3),(-1,4),(-2,4),(-2,3),(-2,2)}
qmin=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(q['certified_minimum_C_age']>=2 for q in qmin['slots'].values())
AP=R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json';angles=[q for q in json.loads(AP.read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if q['old_source']=='V'and q['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']==2];assert len(angles)==62
a,b=chord('V',(0,0,0));u=sub(b,a);boxes=[];poses=[];rows=[]
def raw(tokens):return ''.join(W[a]for a in tokens)
def physical_owner(tokens,tick):
 t=0
 for i,a in enumerate(tokens):
  if tick<t+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,canonical=o.describe(a,tick-t))
  t+=len(W[a])
 return dict(actual_atom='next actual word',tick0=tick-t,read_number1=tick-t+1,turn=l.M[tick-t])
def conflicts(cells,tr,pa,tokens):
 hits=[]
 for cell in sorted(cells):
  loc=l.rot(sub(cell,pa[:2]),-pa[2]);f=tr['first'].get(loc)
  if loc in l.K:hits.append(dict(SAME_CURRENT_cell=cell,foreign_local=loc,contradiction='outside-core current identity in FOREIGN ENTRY core'))
  elif f and f[0]=='R':hits.append(dict(SAME_preFOREIGN_BLACK_cell=cell,foreign_local=loc,contradiction='actual first combined read requires WHITE',combined_tick0=f[1],actual_owner=physical_owner(tokens,f[1])))
 return hits
for angle in angles:
 b1,b2,b3=angle['first'],angle['second'],angle['third'];K=angle['total_ordinary_C_before_third'];h=angle['third_heading_relative_old'];hA=angle['true_FOREIGN_heading_relative_old'];c,d=chord(b3,(0,0,h));v=sub(d,c);den=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(angle=angle,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-K)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:
    s,t=Q(det(zz,v),den),Q(det(zz,u),den)
    if not(0<=s<1 and 0<t<=1):continue
    kind='nonparallel'
   else:
    assert b3=='V'and K==2 and v==u
    if det(zz,u):continue
    start=Q(zz[0],u[0]);s,t=Q(0),-start
    if not(0<t<=1):continue
    kind='same-direction first positive collinear onset'
   p3=(x,y,h);poses.append(dict(angle=angle,third_pose=p3,old_s=str(s),third_t=str(t),contact_kind=kind))
   for A in'FQB':
    de=after(raw(A+b1+b2),(0,0,hA));pa=(x-de[0],y-de[1],hA);tokens=A+b1+b2+b3;tr=l.trace(raw(tokens)+l.M);row=dict(foreign=A,first=b1,second=b2,third=b3,true_preFOREIGN_age=2,totalK=K,foreign_pose=pa,third_pose=p3,old_s=str(s),third_t=str(t))
    if not tr['feasible']:row.update(classification='immutable_local_literal_conflict',conflict=tr)
    else:
     fixed=RBASE|{beta};stateA=conflicts(fixed|{Acell},tr,pa,tokens);stateH=conflicts(fixed|{tuple(z['SAME_genuine_helper_output_cell'])for z in helper},tr,pa,tokens);assert stateA and stateH
     row.update(classification='both_genuine_before_FOREIGN_A_states_excluded',original_A_CURRENT_branch=stateA,original_A_absent_FORCED_genuine_plainV_helper_branch=stateH,original_A_not_assumed_physically_WHITE_in_absent_branch=True)
    rows.append(row)
assert len(boxes)==62 and len(poses)==137 and len(rows)==411
assert Counter(r['classification']for r in rows)=={'immutable_local_literal_conflict':105,'both_genuine_before_FOREIGN_A_states_excluded':306}
paths=[GP,AP,R/'third_ordinary_local_interface_2026-10-24/manifest.json',R/'audits/third_local_interface_independent.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'audits/check_V_parallel_reproductive_supply_independent.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'audits/check_V_C_same_heading_exclusion_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'audits/check_atomic_exit_bud_independent.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/manifest.json',R/'V_postforeign_pair_rail_reserve_2026-10-24/simultaneous_input_qualification_manifest.json',R/'audits/check_V_pair_rail_independent.json',R/'audits/check_V_pair_simultaneous_qualification_independent.json',R/'audits/dcuv_count5_replay/queries.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_OLD_V_THIRD_TRUE_AGE2_GENUINE_FIELD_CLOSURE_PENDING_REVIEW',scope='Only global FIRST contact by THIRD ordinary RAW with outgoing oldV source at true preFOREIGN age2, actual source fullV/VC/VCC completed. Actual firstforeign and finalM11. No postFOREIGN age, endpoint word search or other source/age closure.',all3_actual_source_full_base_R_facts=sourcefacts,all8_genuine_previous_full_final_EXIT_bud_roles=prior,absent_original_A_branch='Signed2043 requires genuine helperV/VC0,4S at sourceclock2 beforeFOREclock2. Completion beforeFORE forces helperplainV. Its six new R-born outputs are CURRENT untilFORE entry by old minimum2 at actual helperage0. No old A physical WHITE value is assumed; it may be aliveCORE if helper is immediately before A.',all6_genuine_helper_R_output_facts=helper,all62_signed_angle_contact_boxes=boxes,all137_outgoing_owned_contact_pose_labels=poses,all411_FOREIGN_typed_two_branch_before_mask_cases=rows,all_actual_source_full_types_are_covered_by_same_base_field=True,conclusion='All411 necessary oldV true-preFOREIGN-age2 THIRD labels fail:105 local complete literal conflicts and306 contradictory genuine fields in BOTH A-current and A-absent/helper states. Source fullV/VC/VCC each retained with actual clocks and same base R births; these are not counts of attained executions. No input age is used afterFOREIGN.',no_original_A_alive_CORE_identified_with_death_or_replacement=True,no_unexecuted_helper_C_tail_or_arbitrary_field_reset=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'age2_field.json').write_text(json.dumps(out,indent=2)+'\n');print('OldV THIRD trueage2:62 angles/137 poses/411 types=105 local conflicts+306 BOTH genuine A/helper field contradictions, all3 actual source tails; no postA age or history search.')
