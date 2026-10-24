"""Fresh C coupled reserve; outgoing first post-Q/B D/C first-contact closure.
No terminal DCC parsing assumption. Every clock below is actual ordinary C.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(q,v),den),F(det(q,u),den)
  return dict(old_s=str(s),new_t=str(t))if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(F(0),lo)),str(min(F(1),hi))])if max(0,lo)<=min(1,hi)else None

def rel(q,p):return l.rot(sub(q,p[:2]),-p[2])
def conflict(a,p,black=(),white=()):
 tr=l.trace(W[a]+l.M);bad=[]
 for q in sorted(black):
  x=rel(q,p);f=tr['first'].get(x)
  if x in l.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT_BLACK=q,local=x,role='ENTRY_CORE'if x in l.K else'first_WHITE',actual_first=f,owner=o.describe(a,f[1])if f else None))
 for q in sorted(white):
  x=rel(q,p);f=tr['first'].get(x)
  if x in l.K or f and f[0]=='L':bad.append(dict(physical_WHITE=q,local=x,role='ENTRY_CORE_requires_BLACK'if x in l.K else'first_BLACK',actual_first=f,owner=o.describe(a,f[1])if f else None))
 return bad
# The selected D/C is actual first post-F, entry0N. beta is a GENUINE
# foreign R-born identity, not a G8-age-tagged source output.
beta=(1,-1);M=(2,0);CO={(2,0),(2,1),(1,2)};FT={(-3,-1),(-2,-1)};FV=[(-7,-3),(-1,-1)]
fbirth=[]
for tag in sorted(FT|{beta}):
 ep=after(W['F']);cell=add(ep[:2],l.rot(tag,ep[2]));f=l.trace(W['F'])['last'][cell];assert f[0]=='R';fbirth.append(dict(post_F_EXIT_tag=tag,actual_F_cell=cell,R_tick0=f[1],R_read_number1=f[1]+1,genuine_external_output=list(cell)in l.literal_geometry(W['F'])['outputs']))
assert{q['R_tick0']for q in fbirth}=={46,47,54}
for src in'DC':assert beta not in l.trace(W[src]+l.M)['first']and beta not in{add(after(W[src])[:2],l.rot(q,after(W[src])[2]))for q in l.K}
# The old helper-main subtable is SOURCE-D/late-reader only: no preceding
# packet or incoming beta's producer-age hypothesis appears in its552 rows.
old5=json.loads((R/'core_periodicity_new/five_C_endpoint_boundary_frozen_20261023_1557/02_five_C_endpoint_boundary.json').read_text());tabs=old5['last_clock_helper_main_retirement_tables'];assert len(tabs)==2 and sum(len(t['rows'])for t in tabs)==552
main_lift=[]
for t in tabs:
 assert tuple(t['main_output'])==M and len(t['rows'])==276
 leftovers=[r for r in t['rows']if r['reason']=='FRESH_V_EXIT_BUD_STILL_CURRENT_WHITE_OR_TOO_YOUNG_AT_HELPER'];assert len(leftovers)==4
 for r in leftovers:assert r['full_source']in(0,1)and r['consumer']in(4,5)and tuple(r['consumer_pose'])==(0,1,1)and r['atomic_entry_C_gap']==3
 p=tuple(t['helper_pose']);tr=l.trace(W[t['helper_atom']]+l.M);assert tr['first'][rel(M,p)][0]=='R'
 main_lift.append(dict(actual_late_helper=t['helper_atom'],pose=p,requires_original_D_common_WHITE=dict(local=rel(M,p),actual_first=tr['first'][rel(M,p)]),all276_reader_specific_main_first_retirement_rows=t['rows'],premise_lift='Selected sourceD to this BASE helper is an ACTUAL G8 factor by signed RAW base-cut grammar, with actual precedingF and SAME finalM supplied by targetC. Source is real D/DC; every earlier main-consuming complete packet finishes before helperBASE. The552-row proof refers only to these actual source/reader data and GLOBAL first-contact simplicity. It uses no G8 age for foreign beta and no hypothetical previous G8 packet. Four residues are genuine V/VC0,1E atclock3; their fresh EXIT bud2,-1 is too young/current atlatehelper5 INSIDE this actual G8 factor.'))
# Fresh C reserve is independently signed, including its deadline-conditioned
# CURRENT guarantee at every source-C contact target used below.
cp=json.loads((R/'first_post_Q_B_DC_source_closure_2026-10-24/Q_B_DC_closure.json').read_text());assert len(cp['fresh_C_portable_coupled_reserve']['all96_plain_true_input_first_loss_roles'])==96
# Incoming beta first-loss interface. A sourceD E3 target needs common M
# CURRENT to ENTRY by legitimate G8 atomic-min3 + all E input exits x>=2.
common_E=[]
for a in'DVU':
 for slot,(c,tick)in l.trace(W[a]+l.M)['first'].items():
  if c!='L'or slot in l.K:continue
  p=(*sub(M,l.rot(slot,1)),1);ep=after(W[a],p);assert ep[0]>=2
  common_E.append(dict(atom=a,input=slot,pose=p,RAW_EXIT=ep,exit_x_ge2=True))
assert len(common_E)==8
# Only these cutoff targets are needed. E3 x may be more negative for sourceC.
T={'D':[(3,(-1,0,1))], 'C':[(3,(-1,0,1)),(3,(-3,0,1)),(3,(-4,-1,1)),(3,(-2,-1,1))]}
for src in'DC':T[src]+=[(4,(-1,-1,0)),(5,(0,-1,3))]
betarows=[]
for src in'DC':
 for deadline,target in T[src]:
  for K in range(deadline+1):
   h=(-K)%4
   for a in'DVU':
    tr=l.trace(W[a]+l.M)
    for slot,(c,tick)in tr['first'].items():
     if c!='L'or slot in l.K:continue
     p=(*sub(beta,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(source=src,target_pose=target,target_C_clock=deadline,consumer=a,consumer_ENTRY_C_clock=K,pose=p,input=slot,actual_input=tr['first'][slot],owner=o.describe(a,tick),RAW_EXIT=ep)
     if(sum(p[:2])+h)%2:why='sector'
     elif src=='C'and K==0:why='before_selected_C_RAW_completes_at1'
     elif K==0:
      assert p[1]<1;why='initial_N0_head_below_actual_sourceD_EXIT_y1'
     elif K==1:
      assert p[1]<1;why='initial_W1_head_below_sourceC_y1_or_sourceD_y2'
     elif K==2:
      co=contact(*chord(src,(0,0,0)),*chord(a,p))
      if co:r['actual_old_source_contact']=co;why='earlier_actual_source_EXIT_vertex_repeat'
      else:
       assert a=='U'and p==(1,1,2);assert M in[add(p[:2],l.rot(q,h))for q,(c0,t0)in tr['first'].items()if c0=='L'and q not in l.K]
       why='young_D_common_atomic_min3_inside_actual_G8'if src=='D'else'sourceC_genuine_O3_reserve_CURRENT_through_target'
     elif K==3:
      co=contact(*chord(src,(0,0,0)),*chord(a,p))
      if co:r['actual_old_source_contact']=co;why='earlier_actual_source_contact_or_repeated_entry'
      elif deadline==3:
       assert ep[0]>=1>target[0];why='same_E3_remaining_zeroC_cannot_move_left_to_target'
      elif deadline==4:
       assert ep[0]>=1;why='one_E_to_N_C_adds_x1_then_N_cannot_move_left_to_target_x_minus1'
      elif p==(-1,-2,1):
       assert a=='U';fresh=add(p[:2],l.rot((0,1),h));assert fresh==(0,-2)and rel(fresh,target)in l.K;r['genuine_fresh_U_STAR']=fresh;why='new_U_permanent_RAW_star_inside_final_C5_ENTRY_CORE'
      else:
       assert(a=='V'and p==(-2,-1,1))or(a=='U'and p==(-3,-2,1));assert z(ep)==z(target);why='earlier_consumer_RAW_EXIT_is_the_final_C5_ENTRY_vertex'
     elif K==4:
      if deadline==4:
       assert ep[0]>=1>target[0];why='N4_RAW_exit_x_ge1_cannot_move_left_to_target'
      else:
       assert ep[1]>=-1;why='one_N_to_W_C_raises_y_to_ge0_then_W_cannot_lower_to_minus1'
     else:
      assert K==5 and deadline==5
      if ep[1]>target[1]:why='same_W5_RAW_exit_y_above_target'
      elif ep[0]<target[0]:why='same_W5_RAW_exit_x_left_of_target_and_W_cannot_move_right'
      else:
       assert ep==target and((a=='V'and p==(3,-2,3))or(a=='U'and p==(4,-1,3)))
       assert tr['first'][rel(M,p)][0]=='R';r['main_WHITE_requirement']=dict(cell=M,local=rel(M,p),first=tr['first'][rel(M,p)])
       why='sourceD_reader_independent_552_main_guard_in_actual_G8'if src=='D'else'sourceC_genuine_O3_CURRENT_reserve_at_final_W5_y_minus1'
     r['route']=why;betarows.append(r)
assert len(betarows)==336
# Coupled F46/F47 first-loss cover. Source-D anchors apply only to E3
# V(-1,0,E); fresh-sourceC anchors apply to every E3 contact target.
fpair=[]
for src,anchors in [('D',{M,beta}),('C',CO|{beta})]:
 for tag in sorted(FT):
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for slot,(c,tick)in tr['first'].items():
    if c!='L'or slot in l.K:continue
    for h in range(4):
     p=(*sub(tag,l.rot(slot,h)),h);r=dict(source=src,SAME_F_tag=tag,consumer=a,pose=p,input=slot,owner=o.describe(a,tick),RAW_EXIT=after(W[a],p))
     if(sum(p[:2])+h)%2:why='sector'
     else:
      touches=[dict(anchor=q,local=rel(q,p),actual_first=tr['first'][rel(q,p)],owner=o.describe(a,tr['first'][rel(q,p)][1]))for q in sorted(anchors)if rel(q,p)in tr['first']]
      if touches:r['independently_CURRENT_to_target_anchor_touches']=touches;why='would_lose_or_violate_independent_CURRENT_anchor_before_target'
      else:
       bad=conflict(a,p,FT)
       if bad:r['held_F_conflicts']=bad;why='other_SAME_held_F_tag_ENTRY_CORE_or_first_WHITE'
       else:
        co=contact(*FV,*chord(a,p));cs=contact(*chord(src,(0,0,0)),*chord(a,p));assert co or cs;r.update(actual_FOREIGN_contact=co,actual_ordinary_source_contact=cs);why='earlier_actual_FOREIGN_or_source_proxy_contact'
     r['route']=why;fpair.append(r)
assert len(fpair)==128
# All4 actual predecessors of the common E3 negative-x0 target need F47
# WHITE before they can supply that target. Each has actual SAME M11.
PRE=[];target=(-1,0,1);g=(-2,-1)
for a in'DCVU':
 h=2 if a=='C'else 1;ep=after(W[a],(0,0,h));p=(target[0]-ep[0],target[1]-ep[1],h);x=rel(g,p);f=l.trace(W[a]+l.M)['first'][x];assert f[0]=='R';PRE.append(dict(actual_previous_RAW=a,pose=p,SAME_F47=g,local=x,actual_first=f,owner=o.describe(a,f[1]),requires_WHITE_before_reaching_target=True))
# Bind exact source universes and assemble F D/C first-contact exclusions.
olds=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];geo=cp['all40_source_D_C_geometry_rows'];closures=[]
for src in'DC':
 for q in geo[src]:
  K=q['K'];a=q['actor'];p=tuple(q['pose']);r=dict(foreign='F',**q)
  if src=='D'and a in'DVU':
   old=next(x for x in olds if x['earlier_atom']=='D'and x['entry_C_gap']==K and x['later_atom']==a and tuple(x['later_pose'])==p)
   if not old['surviving_allowed_first_full_packet_ids']:r.update(route='actual_BASE_cut_G8_and_signed129',signed129=old);closures.append(r);continue
   assert a=='V'and K==3 and p==(-1,0,1)
  if src=='C':
   bad=conflict(a,p,CO)
   if bad:r.update(route='fresh_C_O3_CURRENT_CORE_or_WHITE',guards=bad);closures.append(r);continue
   if K==2:
    assert a=='U'and p in[(-1,1,2),(-1,3,2)];r.update(route='fresh_C_L3_hole_WHITE_at_higher_S2_U');closures.append(r);continue
  if K in(4,5):
   assert a in'DC'and p==((-1,-1,0)if K==4 else(0,-1,3));bad=conflict(a,p,{beta});assert bad;r.update(route='genuine_FOREIGN_beta_CURRENT_until_terminal_C4_or_C5_ENTRY',guards=bad)
  elif p==(-1,0,1):
   assert K==3;r.update(route='coupled_F46_F47_CURRENT_and_all4_actual_previous_RAW_require_F47_WHITE',actual_previous_RAWs=PRE)
  else:
   assert src=='C'and K==3;bad=conflict(a,p,FT);assert bad;r.update(route='coupled_F46_F47_CURRENT_direct_CORE_or_WHITE',guards=bad)
  closures.append(r)
assert len(closures)==40 and all(r['route']for r in closures)
# Retain the structurally selected sharp G8 boundary lift attempts, not a
# prefix-depth scan or a positive history. They show actual F rewrites matter.
reg=[]
for T in ['DDDCVCVCDV','DCDVCVCVCC']:
 for pre in['','U','V']:
  word=pre+'F'+T;t=l.trace(''.join(W[a]for a in word)+l.M);assert not t['feasible'];reg.append(dict(prescribed_word=word,reason_for_choice='Exact retained three-C bud sharpness or four-C boundary control after selectedF, not a generic corpus scan.',literal_conflict=t))
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'first_post_Q_B_DC_source_closure_2026-10-24/manifest.json',R/'audits/check_first_Q_B_DC_source_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'audits/check_U_entry_simplicity_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json',R/'core_periodicity_new/five_C_endpoint_boundary_frozen_20261023_1557/manifest.json',R/'audits/check_five_C_endpoint_boundary_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json'];D=[p for p in D if p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry G8 prefix, FIRST F, arbitrary ordinary RAW suffix with actual finalM11. Its GLOBAL first new proxy contact cannot be owned by outgoing first post-F D/C. Terminal DCC is retained; no general arbitrary-tail or other-source simplicity.',genuine_FOREIGN_R_births=fbirth,all8_E3_common_input_RAW_endpoints=common_E,common_E3_entry_guard='For sourceD, selectedD-to-targetBASE is actualG8. Atomic common minimum3 excludes earlier ages; every E3 input RAW exits x>=2 and zeroE cannot return to targetx=-1. For sourceC use separately signed fresh O3 reserve, not JO afterF.',all336_beta_first_loss_target_source_interfaces=betarows,beta_CURRENT_statement='Genuine incoming FOREIGN EXIT beta remains SAME CURRENT at each stipulated E3/N4/W5 contact ENTRY, never through its contact actor. Plain-input/CORE capture cover is independent of a foreign producer-age law. Terminal-C5 U helper creates an actual permanently current freshU star. LateW5 sourceD helpers are blocked by the legitimately parsed G8 552-row main-output guard; sourceC helpers by its independently proved O3 endpoint reserve.',all552_reader_specific_sourceD_main_guard_lift=main_lift,all128_coupled_F46_F47_first_loss_roles=fpair,F_pair_statement='Under the separately proved independently CURRENT source anchors to the candidate E3 ENTRY, choose earliest F46/F47 CURRENT loss before it. Every128 role hits an anchor, conflicts with held otherF tag, or already contacts the actual F/source proxy. This keeps SAME original F46/F47 until candidateENTRY, no through-contact assertion.',all4_actual_previous_RAW_F47_WHITE_obligations=PRE,all40_F_sourceD_C_contact_closures=closures,all6_prescribed_boundary_lift_failures=reg,terminal_DCC_scope='The actual base-cut G8 bridge is used only when the selected factor ends at a genuine BASE (or at the late BASE helper). Target C and terminal DCC are NOT parsed away; C4/C5 use the separate beta currentness interface.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'F_DC_closure.json').write_text(json.dumps(out,indent=2)+'\n');print('F D/C40 closed: beta336 source/target roles, coupledF128; real BASE-cut G8 used only at BASE endpoints.')
