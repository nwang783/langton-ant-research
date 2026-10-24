"""Old-U THIRD source join: portable signed guards and exact direct before-state. No new prefix scan or postforeign maturity."""
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
AP=R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json';angles=[a for a in json.loads(AP.read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if a['old_source']=='U'];assert len(angles)==236
LEFT={(0,0),(0,1)};STAR=LEFT|{(1,0),(1,1)};INITIAL=STAR|{(1,3)}
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];facts=[]
for src in(7,8,9):
 tr=l.trace(G[src]['word']);outs=set(map(tuple,G[src]['outputs']));assert INITIAL<=outs
 facts.append(dict(actual_creating_full=G[src]['name'],source_full_entry_clock=0,actual_full_completion_clock=G[src]['name'].count('C'),all5_genuine_before_FOREIGN_current_tags=[dict(cell=p,source_actual_last_R_tick0=tr['last'][p][1],signed_current_rule='1918 all-age originalSTAR'if p in STAR else'adf3 source-exit bud minimum5 from same zeroC birth clock',own_C_tails_preserve_SAME_R_identity=True)for p in sorted(INITIAL)],true_preFOREIGN_age_upper_bound=4,only_actual_full_sources_completed_before_FOREIGN_are_admitted=True))
a,b=chord('U',(0,0,0));u=sub(b,a);geo={};boxes=[]
for angle in angles:
 target=angle['third'];K=angle['total_ordinary_C_before_third'];key=target,K
 if key in geo:continue
 h=angle['third_heading_relative_old'];c,d=chord(target,(0,0,h));v=sub(d,c);den=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(third=target,totalK=K,heading=h,closed_rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds));cases=[]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-K)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:
    s,t=Q(det(zz,v),den),Q(det(zz,u),den)
    if not(0<=s<1 and 0<t<=1):continue
    kind='nonparallel'
   else:
    assert target=='U'and K==2 and v==u
    if det(zz,u):continue
    source_start=Q(zz[1],u[1]);s,t=Q(0),-source_start
    if not(0<t<=1):continue
    kind='same-direction first positive collinear onset; entries already on old chord omitted by simple-prefix premise'
   tr=l.trace(W[target]+l.M);cuts=[]
   for cell in sorted(LEFT):
    loc=l.rot(sub(cell,(x,y)),-h);f=tr['first'].get(loc)
    if loc in l.K or f and f[0]=='R':cuts.append(dict(SAME_LEFT=cell,local=loc,in_ENTRY_core=loc in l.K,actual_first_read=None if f is None else o.describe(target,f[1])))
   p=(x,y,h);row=dict(third=target,totalK=K,third_pose=p,old_s=str(s),new_t=str(t),contact_kind=kind,SAME_LEFT_contradictions=cuts)
   if cuts:row['route']='SAME_LEFT_at_global_FIRST_contact_ENTRY'
   elif h==1:row['route']='signed_E_endpoint_guard_0e82a78e'
   elif(target,p)==('V',(0,4,2)):row['route']='S_pose_V_r_guard_277cedd1_or_CCv_direct'
   elif(target,p)in(('V',(0,3,3)),('U',(0,3,3))):row['route']='signed_W_arm_guard_bb6eb6b5'
   else:row['route']='direct_genuine_preFOREIGN_before_state'
   cases.append(row)
 geo[key]=cases
geometries=[r for v in geo.values()for r in v];assert len(boxes)==15 and len(geometries)==50
assert Counter(r['route']for r in geometries)=={'SAME_LEFT_at_global_FIRST_contact_ENTRY':37,'signed_E_endpoint_guard_0e82a78e':4,'S_pose_V_r_guard_277cedd1_or_CCv_direct':1,'signed_W_arm_guard_bb6eb6b5':2,'direct_genuine_preFOREIGN_before_state':6}
def raw(tokens):return ''.join(W[a]for a in tokens)
def owner(tokens,tick):
 t=0
 for i,a in enumerate(tokens):
  if tick<t+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,canonical=o.describe(a,tick-t))
  t+=len(W[a])
 return dict(actual_atom='next actual word',next_word_tick0=tick-t,next_word_read_number1=tick-t+1,turn=l.M[tick-t])
all_rows=[];direct=[]
for idx,angle in enumerate(angles):
 b1,b2,b3=angle['first'],angle['second'],angle['third'];K=angle['total_ordinary_C_before_third'];n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];hA=angle['true_FOREIGN_heading_relative_old'];assert 0<=n<=K<=4
 for geometry in geo[b3,K]:
  p3=geometry['third_pose']
  for A in'FQB':
   de=after(raw(A+b1+b2),(0,0,hA));pa=(p3[0]-de[0],p3[1]-de[1],hA);route=geometry['route'];row=dict(signed_angle_index0=idx,foreign=A,first=b1,second=b2,third=b3,true_preFOREIGN_age=n,totalK=K,foreign_pose=pa,third_pose=p3,route=route)
   if route=='S_pose_V_r_guard_277cedd1_or_CCv_direct':
    if n in(3,4):row['route']='signed_S_pose_V_r_guard_277cedd1'
    else:assert n==2 and b1==b2=='C';row['route']='direct_genuine_preFOREIGN_before_state'
   if row['route']=='direct_genuine_preFOREIGN_before_state':
    tokens=A+b1+b2+b3;tr=l.trace(raw(tokens)+l.M);atr=l.trace(W[A]+l.M);rr=dict(**row)
    if not tr['feasible']:rr.update(classification='immutable_complete_local_literal_conflict',literal_conflict=tr)
    else:
     touches=[]
     for cell in sorted(STAR):
      loc=l.rot(sub(cell,pa[:2]),-hA);f=atr['first'].get(loc)
      if f:touches.append(dict(SAME_old_star_cell=cell,foreign_local=loc,actual_FOREIGN_context_first_read=o.describe(A,f[1]),foreign_ENTRY_core=loc in l.K))
     if touches:rr.update(classification='forbidden_firstFOREIGN_young_STAR_context_touch',exact_touches=touches,true_preFOREIGN_age_at_most4=True)
     else:
      cuts=[]
      for cell in sorted(INITIAL):
       loc=l.rot(sub(cell,pa[:2]),-hA);f=tr['first'].get(loc)
       if loc in l.K:cuts.append(dict(SAME_preFOREIGN_current_cell=cell,foreign_local=loc,contradiction='CURRENT beforeFOREIGN but in FOREIGN ENTRY core'))
       elif f and f[0]=='R':cuts.append(dict(SAME_preFOREIGN_BLACK_cell=cell,foreign_local=loc,contradiction='first actual combined read requires WHITE',combined_tick0=f[1],actual_owner=owner(tokens,f[1])))
      assert cuts,row
      rr.update(classification='genuine_preFOREIGN_current_or_BLACK_before_state_contradiction',exact_current_or_BLACK_conflicts=cuts)
    direct.append(rr);row['direct_classification']=rr['classification']
   all_rows.append(row)
assert len(all_rows)==2346 and len(direct)==291
assert Counter(r['classification']for r in direct)=={'immutable_complete_local_literal_conflict':73,'forbidden_firstFOREIGN_young_STAR_context_touch':13,'genuine_preFOREIGN_current_or_BLACK_before_state_contradiction':205}
paths=[AP,R/'third_ordinary_local_interface_2026-10-24/manifest.json',R/'audits/third_local_interface_independent.json',GP,R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json',R/'audits/check_U_foreign_prefix_buds_independent.json',R/'old_U_third_E_endpoint_guard_2026-10-24/manifest.json',R/'audits/check_U_third_E_endpoint_independent.json',R/'V_r_postforeign_contact_clock_2026-10-24/manifest.json',R/'audits/check_V_r_postforeign_clock_independent.json',R/'U_arm_W_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_U_arm_W_guard_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_COMPLETE_OLD_U_THIRD_SOURCE_JOIN_PENDING_INDEPENDENT_REVIEW',scope='Only global FIRST new proxy contact by THIRD ordinary RAW, old outgoing source a genuine preFOREIGN U-base inside actual U-entry complete8 prefix then FIRSTforeign and two ordinary RAWs; actual finalM11. No other old source/full third simplicity or arbitrary-tail extension.',all236_signed_old_U_angle_rows=angles,all15_exact_contact_parallelograms=boxes,all50_unique_outgoing_owned_contact_geometries=geometries,all3_actual_U_source_before_FOREIGN_tag_births=facts,all2346_necessary_FOREIGN_typed_contact_labels_and_exhaustive_routes=all_rows,all291_direct_preFOREIGN_before_state_cases=direct,exact_direct_disjoint_classification=dict(Counter(r['classification']for r in direct)),conclusion='All old-U THIRD source contacts excluded. Fifty unique geometries:37 SAME LEFT current/core or WHITE cuts;4 E endpoint guards;1 S-V pose via signed V-r clock for45 n3/4 labels plus3 direct n2CCV cases;2 W arm guards;6 direct genuine initial-star/bud mask geometries. Direct291 labels split73 local conflicts,13 forbidden young FOREIGN-star touches,205 true preFOREIGN current/BLACK first-read contradictions. No q/shadow or other identity permanence is assumed across A.',no_postFOREIGN_age_or_unproved_RIGHT_physical_survival_or_fixed_nine_mask_reuse=True,no_generic_prefix_scan_or_overall_third_simplicity_claim=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'U_third_join.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU THIRD:236 angles/50 unique geometries/2346 foreign labels exhaust via37LEFT+4E+1S+2W+6direct.291 direct masks=73literal+13youngSTAR+205 genuine preA before-state contradictions.')
