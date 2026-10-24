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
# Portable fresh C output reserve, with no full-eight producer age relation.
O={(2,0),(2,1),(1,2)};ct=l.trace(W['C']);cg=l.literal_geometry(W['C']);assert {tuple(x)for x in cg['outputs']}==O
births=[dict(tag=q,last_R_tick0=ct['last'][q][1],last_R_read_number1=ct['last'][q][1]+1)for q in sorted(O)];assert after(W['C'])==(0,1,3)
roles=[]
for tag in sorted(O):
 for a in'DVU':
  tr=l.trace(W[a]+l.M);I=[q for q,(c,t)in tr['first'].items()if c=='L'and q not in l.K]
  for slot in I:
   for h in range(4):
    p=(*sub(tag,l.rot(slot,h)),h);r=dict(SAME_output=tag,consumer=a,true_input_local=slot,pose=p,actual_input=tr['first'][slot],owner=o.describe(a,tr['first'][slot][1]),RAW_EXIT=after(W[a],p))
    if(sum(p[:2])+h)%2:r['route']='sector'
    else:
     bad=conflict(a,p,O)
     if bad:r.update(route='held_three_CURRENT_CORE_or_WHITE',held_conflicts=bad)
     elif h in(2,3):
      # The first W stage begins at0,1,W; its x never increases. The next
      # C moves x left once, so every S2 head has x<=-1.
      if h==2:assert p[0]>=0;r['route']='S2_head_x_positive_but_actual_heads_x_le_minus1'
      else:assert p[0]>0;r['route']='W1_head_x_positive_but_actual_heads_x_le0_or_W5_exit_y_ge2'
     elif h==1:
      co=contact(*chord('C',(0,0,0)),*chord(a,p));assert co;r.update(route='E3_actual_earlier_source_C_contact',actual_source_contact=co,not_actual_source_adjacency='source C EXIT has headingW and clock1; consumer has headingE and clock3')
     else:
      assert a=='U'and p in((2,-2,0),(3,-1,0))and r['RAW_EXIT'][1]>=2;r['route']='N4_loss_exits_y_ge2'
    roles.append(r)
assert len(roles)==96
assert Counter(r['route']for r in roles)=={'sector':48,'held_three_CURRENT_CORE_or_WHITE':28,'S2_head_x_positive_but_actual_heads_x_le_minus1':8,'W1_head_x_positive_but_actual_heads_x_le0_or_W5_exit_y_ge2':3,'E3_actual_earlier_source_C_contact':4,'N4_loss_exits_y_ge2':5}
W5=[r for r in roles if r['route'].startswith('W1_head')];assert all(r['consumer']=='U'and tuple(r['pose'])in((3,2,3),(2,3,3))and r['RAW_EXIT'][1]>=2 for r in W5)
reserve=dict(genuine_C_RAW_EXIT=(0,1,3),source_ENTRY_clock=0,source_RAW_EXIT_clock=1,all3_actual_output_births=births,all96_plain_true_input_first_loss_roles=roles,statement='In an ordinary-only suffix after a genuine fresh C, at a marked cut whose executed source-prefix is SIMPLE: all3 SAME outputs are CURRENT through source-entry K<=3. Also CURRENT at a prescribed N-facing K4 target with head y<=1, or W-facing K5 target with head y<=0, if the earlier prefix is simple and reaches that target. N4 first-loss U exits y2/3; reaching W5 requires another C raising y once. W5 first-loss U exits y2/3 and W never lowers y. No postforeign old-age or G8 producer law is used.',CURRENT_CORE_completion='All plain input slots include marker-only CORE capture. A first CURRENT loss must occur through these actual inputs. C has I0; no noninput/CORE-only export evades this cover. The conclusion stops at the target ENTRY, not through its RAW.')
# Young S2 repair guard: actual source-C hole0,-1 stays WHITE at higher S2
# readers. All actual final RAW R slots, including EXITCORE, are retained.
hole=(0,-1);assert ct['last'][hole]==('L',3)and hole not in O
exitK={add((0,1),l.rot(q,3))for q in l.K};assert hole not in exitK
writes=[]
for a in'DCVU':
 tr=l.trace(W[a]);ep=after(W[a])
 for q,(c,t)in sorted(tr['last'].items()):
  if c!='R':continue
  assert q[0]>=-1 and ep[1]>=q[1]if a in'DVU'else True
  writes.append(dict(atom=a,RAW_final_R_local=q,tick0=t,read_number1=t+1,RAW_EXIT=ep,in_actual_EXIT_CORE=rel(q,ep)in l.K))
assert len(writes)==36
# Generic S2 final-R endpoint inequality uses source normalizedN then rotateS:
# EXITy = heady - ep_y <= heady - local_qy = written_y.
assert all(after(W[a])[1]>=q[1]for a in'DVU'for q,(c,t)in l.trace(W[a])['last'].items()if c=='R')
young=[]
for p in[(-1,1,2),(-1,3,2)]:
 x=rel(hole,p);f=l.trace(W['U']+l.M)['first'][x];assert f[0]=='L'and p[1]>hole[1]
 young.append(dict(actor='U',pose=p,source_C_deleted_hole=hole,local=x,actual_first=f,owner=o.describe('U',f[1]),route='physical_WHITE_at_higher_S2_reader'))
white_guard=dict(actual_C_deletion=dict(cell=hole,tick0=3,read_number1=4,WHITE_outside_source_EXIT_CORE=True),all36_actual_RAW_final_R_slots_CORE_included=writes,all2_S2_U_guards=young,proof='After source C completes, W1 heads have x<=0,y>=1. Every final RAW R has local x>=-1, so a W1 write has y>=0 and cannot repair0,-1. S2 C cannot complete before a same-clock S2 reader; any completed S2 D/V/U last-R writer exits at/below the written hole y=-1, and zero-C S cannot rise to either reader y1/3. Source C itself lastL3-deleted the hole. Thus this is a real physical WHITE guard, not a residual-only origin or an assumption of permanent whiteness.')
# Q negative port lift: all ordinary targets at0,-1,W share actualM11.
qp=json.loads((R/'foreign_Q_W5_deleted_core_guard_2026-10-24/Q_W5_deleted_core_guard.json').read_text());qfive=[r for r in qp['all208_last_RAW_R_origin_deadline_and_hook_FOREIGN_constraints']if r.get('why')=='NECESSARY'];assert len(qfive)==5
qprev=qp['all3_actual_immediate_previous_RAW_BLACK_hole_obligations'];assert len(qprev)==3
qreader=[]
for a in'DCVU':
 assert(W[a]+l.M)[:11]==l.M
 target=(0,-1,3)
 for prev in'DCVU':
  h=0 if prev=='C'else 3;ep=after(W[prev],(0,0,h));p=(target[0]-ep[0],target[1]-ep[1],h);assert after(W[prev],p)==target
  if prev!='C':
   old=next(x for x in qprev if x['actual_previous_RAW']==prev);assert tuple(old['actual_previous_head'])==p
   cut='identical_signed_three_nonC_reader_funding_obligation_before_target_ENTRY'
  else:
   assert p==(0,-2,0)and z(p)==(-1,-5)
   cut='earlier_Q_genuine_F56_kink_ENTRY_repeat_at_clock4'
  qreader.append(dict(target_RAW=a,target_pose=target,target_entry_C_clock=5,actual_previous_RAW=prev,previous_pose=p,route=cut,target_and_old_U_same_actual_first_M11=True,old_Q_kink_is_actual_fine_cut_not_marked_CORE=True if prev=='C'else None))
assert len(qreader)==16
Qh=dict(statement='At GLOBAL-first-contact ENTRY5 pose0,-1,W after actual Q, physical h0,-2 is WHITE for ANY completed ordinary target D/C/V/U with actualM11. Every non-C preceding RAW is precisely the signed d3f96db6 three-reader funding obligation, whose proof precedes targetENTRY and uses only the shared actualM11, not targetU body/CU ban. A preceding C0,-2,N at clock4 repeats the genuine old Q kink(-1,-5) already at its ENTRY, hence earlier than the claimed contact. No marked CORE is assigned at that kink.',all16_target_by_actual_previous_RAW_interfaces=qreader,same5_CORE_inclusive_last_R_origins=qfive)
# Independent affine geometry universe for an ordinary source with no
# intervening foreign. K is sourceENTRY to candidateENTRY, not FORE clock.
V={'D':(1,1),'C':(1,1),'V':(1,3),'U':(0,4)};rank={'U':0,'V':1,'D':2,'C':2};CENTER=(F(-1,2),F(-1,2))
def generate(src):
 out=[]
 for K in range(2,7):
  h=(-K)%4;u=V[src]
  for a,bv in V.items():
   if K==2 and not rank[src]>rank[a]:continue
   if K==6 and not rank[src]<rank[a]:continue
   v=l.rot(bv,h);cor=sub(CENTER,l.rot(CENTER,h));corn=[add(cor,(s*u[0]-t*v[0],s*u[1]-t*v[1]))for s in(0,1)for t in(0,1)]
   from math import ceil,floor
   for x in range(ceil(min(p[0]for p in corn)),floor(max(p[0]for p in corn))+1):
    for y in range(ceil(min(p[1]for p in corn)),floor(max(p[1]for p in corn))+1):
     if(x+y+h)%2:continue
     w=sub(add((x,y),l.rot(CENTER,h)),CENTER);de=det(u,v)
     if de:
      s,t=F(det(w,v),de),F(det(w,u),de)
      if not(0<=s<1 and 0<t<=1):continue
     else:
      if det(w,u):continue
      k=0 if v[0]else 1;s=F(0);t=F(-w[k],v[k])
      if not(0<t<=1 and add(w,(t*v[0],t*v[1]))==(0,0)):continue
     out.append(dict(source=src,K=K,actor=a,pose=(x,y,h),old_s=str(s),new_t=str(t)))
 return out
old=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases']
for src in'DC':
 assert{(r['K'],r['actor'],tuple(r['pose']),r['old_s'],r['new_t'])for r in generate(src)}=={(r['entry_C_gap'],r['later_atom'],tuple(r['later_pose']),r['earlier_parameter'],r['later_parameter'])for r in old if r['earlier_atom']==src}
HOOK={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
closures=[]
for src in'DC':
 for g in generate(src):
  a=g['actor'];p=tuple(g['pose']);K=g['K']
  for A in'QB':
   r=dict(foreign=A,**g)
   if src=='D'and a in'DVU':
    signed=next(x for x in old if x['earlier_atom']=='D'and x['entry_C_gap']==K and x['later_atom']==a and tuple(x['later_pose'])==p)
    if not signed['surviving_allowed_first_full_packet_ids']:
     r.update(route='actual_BASE_cut_G8_parse_and_signed129_exclusion',signed129=signed);closures.append(r);continue
    assert a=='V'and p==(-1,0,1)and K==3
   black=set(HOOK[A]);white=set()
   if A=='B'and K<=5:black.add((-1,-2));white.add((0,-2))
   if src=='C':
    assert K<=3 or K==4 and p[1]<=1 or K==5 and p[1]<=0
    black|=O
   bad=conflict(a,p,black,white)
   if bad:r.update(route='actual_CURRENT_or_physical_WHITE_entry_context',guards=bad)
   elif src=='C'and K==2:
    assert a=='U'and p in[(-1,1,2),(-1,3,2)];r.update(route='source_C_actual_L3_hole_WHITE_at_S2_U',guard=next(x for x in young if tuple(x['pose'])==p))
   else:
    assert A=='Q'and K==5 and a in'DC'and p==(0,-1,3);bad=conflict(a,p,white={(0,-2)});assert bad;r.update(route='Q_hole_port_lift_to_same_pose_C5_reader',guards=bad)
   closures.append(r)
assert len(generate('D'))==20 and len(generate('C'))==20 and len(closures)==80
assert all(r['route']for r in closures)
# Real terminal exception regression remains, rather than falsely parsed.
reg=[]
for word in['UDCC','UQUDCC']:
 t=l.trace(''.join(W[a]for a in word)+l.M);assert t['feasible'];reg.append(dict(word=word,RAW_plus_actual_M11_complete=True,seed=sorted(p for p,(c,k)in t['first'].items()if c=='L'),not_called_G8_at_terminal_DCC=True))
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'audits/check_U_entry_simplicity_independent.json',R/'foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_hook_reserve_independent.json',R/'B_preU_WHITE_hole_shadow_reserve_2026-10-24/manifest.json',R/'audits/check_B_preU_hole_reserve_independent.json',R/'foreign_Q_W5_deleted_core_guard_2026-10-24/manifest.json',R/'audits/check_Q_W5_core_funding_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json']
# Some independent filenames are normalized separately from the manifest name.
D=[p for p in D if p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='An actual U-entry complete-eight prefix, its FIRST complete Q/B, and arbitrary following ordinary RAWs with actual finalM11. A GLOBAL first new proxy contact cannot have outgoing owner the FIRST postforeign ordinary D or C. F, later ordinary source owners, second foreign and arbitrary-tail simplicity remain separate. Terminal DCC is retained.',fresh_C_portable_coupled_reserve=reserve,fresh_C_S2_physical_WHITE_hole_guard=white_guard,Q_C5_negative_port_reader_lift=Qh,all40_source_D_C_geometry_rows={src:generate(src)for src in'DC'},all80_foreign_typed_contact_closures=closures,actual_terminal_DCC_regressions=reg,BASE_cut_only_scope='Only later D/V/U contact actors use actual RAW→G8 bridge. They end at genuine BASE with same actualM11, and the first D has actual preceding Q/B. Later C actors are treated from their own exact three-pose geometry; no terminal DCC is silently parsed.',C_reserve_stop='SAME C outputs CURRENT at contact ENTRY only. TRUE inputs during contact remain allowed; no through-contact or all-age seal.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'Q_B_DC_closure.json').write_text(json.dumps(out,indent=2)+'\n')
print('Fresh C96 first-loss roles; Q C5 reader16; Q/B D/C80 source contact labels all closed, terminal DCC retained.')
