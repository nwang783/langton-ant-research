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
from math import ceil,floor
M=(2,0);CO={(2,0),(2,1),(1,2)};FT={(-3,-1),(-2,-1)};FV=[(-7,-3),(-1,-1)]
# Exact all62 CLOSED F-piece heads. Owner of old s=1 is outgoing b1,
# which is separately signed and never assigned the foreign piece window.
def hit(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 assert den # No ordinary chord is parallel to this actual F3,1 chord.
 s,t=F(det(q,v),den),F(det(q,u),den)
 return(s,t)if 0<=s<=1 and 0<=t<=1 else None
windows=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
closed=[];proper=[];terminal=[];wrongwindow=[]
for a in'DCVU':
 for h in range(4):
  c,d=chord(a,(0,0,h));u=sub(FV[1],FV[0]);v=sub(d,c);corn=[tuple(F(FV[0][k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
  for x in range(floor(min(q[0]for q in corn)),ceil(max(q[0]for q in corn))+1):
   for y in range(floor(min(q[1]for q in corn)),ceil(max(q[1]for q in corn))+1):
    if(x+y+h)%2:continue
    co=hit(*FV,add(c,(2*x,2*y)),add(d,(2*x,2*y)))
    if not co or co[1]<=0:continue
    r=dict(actor=a,pose=(x,y,h),old_F_parameter=str(co[0]),new_parameter=str(co[1]));closed.append(r)
    if co[0]==1:r.update(route='FOREIGN_EXIT_has_outgoing_b1_owner');terminal.append(r);continue
    w=next(z for z in windows if z['source_class']=='Fprefix'and z['contact_atom']==a);K=[k for k in w['allowed_C_counts_before_contact_ENTRY']if(-k)%4==h]
    if not K:r.update(route='signed_piece_angle_window');wrongwindow.append(r);continue
    assert len(K)==1;r['K']=K[0];proper.append(r)
assert len(closed)==62 and len(proper)==42
assert all(r['K']in(2,3,4,5)and(r['pose'][0]<=1 if r['K']==4 else True)and(r['pose'][1]<=-1 if r['K']==5 else True)for r in proper)
# Fresh D common reserve at a simple ordinary-source prefix. Maturity is
# invoked on sourceD→hypothetical earlier BASE consumer only, never targetC.
oldcommon=json.loads((R/'old_D_second_age3_common_beta_2026-10-24/D_age3_common_beta.json').read_text());rows16=[r for r in oldcommon['all184_common_first_loss_full_role_queries']if r['true_full_source_ENTRY_age']==3 and r['consumer']in('D','V','U')];assert len(rows16)==16
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';counted={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()};common16=[]
for r in rows16:
 key=tuple(r['key']);a=r['consumer'];p=tuple(r['pose']);slot=tuple(r['input_cell']);assert p==(*sub(M,l.rot(slot,1)),1)
 if(sum(p[:2])+1)%2:why='sector'
 elif key in counted:why='signed_existing_COUNT5'
 else:
  assert r['reason']=='exact_E3_plain_port'and(a,p)in{('D',(1,0,1)),('V',(-1,0,1)),('V',(0,1,1))}
  if p==(1,0,1):assert z(p)==z(after(W['D']));why='actual_old_D_EXIT_entry_repeat'
  elif p==(-1,0,1):assert contact(*chord('D',(0,0,0)),*chord(a,p))=={'old_s':'1/2','new_t':'1/2'};why='strict_old_D_midpoint_contact'
  else:why='strict_contact_with_genuine_actual_NEXT_N_atom'
 common16.append(dict(original_signed_row=r,route=why))
assert Counter(r['route']for r in common16)=={'sector':4,'signed_existing_COUNT5':7,'actual_old_D_EXIT_entry_repeat':1,'strict_old_D_midpoint_contact':2,'strict_contact_with_genuine_actual_NEXT_N_atom':2}
nexts=[]
for a in'DCVU':
 co=contact(*chord(a,(1,1,0)),*chord('V',(0,1,1)));assert co and 0<F(co['old_s'])<1 and 0<F(co['new_t'])<1;nexts.append(dict(actual_next_atom=a,pose=(1,1,0),strict_chord_contact=co))
ends=[]
for a in'DVU':
 tr=l.trace(W[a]+l.M)
 for slot,(c,t)in tr['first'].items():
  if c!='L'or slot in l.K:continue
  for h in(0,3):
   p=(*sub(M,l.rot(slot,h)),h);ep=after(W[a],p)
   assert ep[1]>=0 and(h!=0 or ep[0]>=2)
   ends.append(dict(atom=a,input=slot,pose=p,RAW_EXIT=ep,actual_owner=o.describe(a,t)))
assert len(ends)==16
common=dict(all16_plain_E3_sourceD_DC_common_queries=common16,all4_genuine_NEXT_N_atom_strict_crossings=nexts,all16_N4_W5_plain_input_RAW_endpoint_inequalities=ends,statement='Fresh D with an ACTUAL preceding seven-atom RAW, followed only ordinary RAWs, and SIMPLE marked source-prefix: its SAME commonR8 is CURRENT through K3. Also CURRENT at an N4 target x<=1 or W5 target y<0 reached by that simple prefix. Apply minimum3 to the hypothetical earlier BASE consumer factor, genuinely G8 by base-cut grammar; no terminalC parsing. At E3 only5 plain ports survive and everyone contacts oldD/its real next atom. At N4 all loss RAW exits x>=2,y>=0; at W5 exits y>=0. Remaining N→W C raises yonce. No source identity is carried through an earlier foreign: D is freshly born after it.')
# Coupled F tags with source outputs ONLY, no beta assumption at new targets.
# A first pair loss that does not already contact oldF/source can only be
# one of three N4 RAWs exiting(-1,-1,N), too high for the true F targets.
pair=[]
for src,anchors in [('D',{M}),('C',CO)]:
 for tag in sorted(FT):
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for slot,(c,t)in tr['first'].items():
    if c!='L'or slot in l.K:continue
    for h in range(4):
     p=(*sub(tag,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(source=src,F_tag=tag,consumer=a,pose=p,RAW_EXIT=ep,input=slot,owner=o.describe(a,t))
     if(sum(p[:2])+h)%2:why='sector'
     else:
      touches=[q for q in sorted(anchors)if rel(q,p)in tr['first']]
      if touches:r['independently_CURRENT_source_outputs']=touches;why='touches_independent_source_CURRENT_identity_before_target'
      else:
       bad=conflict(a,p,FT)
       if bad:r['held_F_conflicts']=bad;why='other_held_F_tag_CORE_or_first_WHITE'
       else:
        co=contact(*FV,*chord(a,p));cs=contact(*chord(src,(0,0,0)),*chord(a,p))
        if co or cs:r.update(old_F_contact=co,ordinary_source_contact=cs);why='earlier_actual_F_or_ordinary_source_contact'
        else:
         assert h==0 and(a,p)in{('D',(-2,-2,0)),('V',(-2,-4,0)),('U',(-1,-5,0))}and ep==(-1,-1,0)
         why='N0_unreachable_or_N4_exit_y_minus1_cannot_reach_lower_N4_or_W5_target'
     r['route']=why;pair.append(r)
assert len(pair)==128
# Five unchanged actual negative-y F-output guards, newly bound without a
# first-V/U hypothesis via the universal input-to-RAW-exit inequalities.
oldF=json.loads((R/'firstpostV_F_piece_first_contact_2026-10-24/F_piece_contact.json').read_text());guards=oldF['all5_proper_Fsource_lower_output_guards'];assert len(guards)==5
negends=[]
for a in'DVU':
 for slot,(c,t)in l.trace(W[a]+l.M)['first'].items():
  if c!='L'or slot in l.K:continue
  assert slot[1]>=1 and slot[0]>=-1
  s=after(W[a],(*l.rot((-slot[0],-slot[1]),2),2));e=after(W[a],(*l.rot((-slot[0],-slot[1]),1),1));assert s[1]<=0 and e[1]<=0;negends.append(dict(atom=a,input=slot,S_RAW_exit_relative_tag=s,E_RAW_exit_relative_tag=e))
assert len(negends)==8
# The sole D-only N4 residue: no unsupported min5 shorthand. Older JO min4
# suffices after a physical-deletion + unbounded zero-C birth exclusion.
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);g=(-1,0);u=(-1,-3,0);loc=rel(g,u);assert loc==(0,3)
assert l.trace(W['D'])['last'][g]==('L',1)and l.trace(W['D']+W['C'])['last'][g]==('L',1)
assert l.trace(W['U']+l.M)['first'][loc]==('L',23)and loc not in l.K
JO=dict((tuple(x[:3]),x[3])for x in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text()));assert JO[7,0,3]>=4
zero=[]
for i in IDS:
 assert min(q[1]for q in G[i]['outputs'])>=0
 zero.append(dict(packet=G[i]['name'],minimum_full_output_y=min(q[1]for q in G[i]['outputs']),all_full_outputs=G[i]['outputs']))
assert all(g not in map(tuple,G[i]['outputs'])for i in(0,1))
N4=dict(actor='U',pose=u,sourceD_deleted_cell=g,D_last_L_tick0=1,D_last_L_read1=2,sourceDC_preserves_deletion=True,target_true_input_local=loc,target_first_read=o.describe('U',23),actual_produced_input_minimum=JO[7,0,3],all8_zero_clock_N_FULL_output_y_bounds=zero,proof='Actual BASE-cut sourceD→targetU factor parsesG8. Original g was deleted by sourceD L1; own D/DC O missesg. Every later clock0 full producer has N-head y>=1 and every genuine full output y>=0, so cannot installg at y0. Thus any real replacement producer starts clock>=1, produced age<=3 at target4, below actual JO minimum4. An EXITCORE R cannot silently supply this external true input: at target g is outside ENTRYCORE, so a surviving BLACK lifetime is an earlier actual fullO identity; original entry exception died atL1. No universal upper-minimum5 is asserted.')
# W5 actorU0,-1 uses exactly the same entry cut as signed8b58 beta targetC.
W5=dict(actor='U',pose=(0,-1,3),K=5,SAME_beta=(1,-1),local=rel((1,-1),(0,-1,3)),shared_actual_first_M11=True,scope_lift='All336 beta clauses in8b58 concern CURRENT at the stipulated target ENTRY pose0,-1,W. Target body is unused: earlier V/U exits repeat this ENTRY; the newU star lies in its universal ENTRYCORE; late helpers require mainWHITE and are treated in actual factor ending at their BASE, with SAME nextM11 supplied by U. Therefore replace targetC by actualU with identical firstM11, retaining mandatory5e24365a. No C→U prohibition or hypothetical complete terminalC is invoked.')
assert W5['local']in l.K and W['U'][:11]==W['C'][:11]==l.M
# All42 proper original-F owner labels × two first-source roles.
join=[]
for src,anchors in [('D',{M}),('C',CO)]:
 for r0 in proper:
  a=r0['actor'];p=tuple(r0['pose']);K=r0['K'];r=dict(first_post_RAW=src,**r0);bad=conflict(a,p,anchors|FT)
  if bad:r.update(route='CURRENT_source_outputs_and_coupled_F46_F47_CORE_or_WHITE',guards=bad)
  else:
   chosen=next((g for g in guards if g['atom']==a and tuple(g['head'])==p[:2]and g['h']==p[2]),None)
   if chosen:r.update(route='actual_negative_y_F_output_coordinate_reserve',signed_literal_guard=chosen)
   elif src=='D'and a=='U'and p==(-1,-3,0):r.update(route='actual_sourceD_L1_deleted_upper_input_no_clock0_rebirth_then_min4',guard=N4)
   else:
    assert a=='U'and p==(0,-1,3)and K==5;r.update(route='SAME_incoming_FOREIGN_beta_at_same_W5_ENTRY_CORE',guard=W5)
  join.append(r)
assert len(join)==84 and Counter(r['route']for r in join)=={'CURRENT_source_outputs_and_coupled_F46_F47_CORE_or_WHITE':71,'actual_negative_y_F_output_coordinate_reserve':10,'actual_sourceD_L1_deleted_upper_input_no_clock0_rebirth_then_min4':1,'SAME_incoming_FOREIGN_beta_at_same_W5_ENTRY_CORE':2}
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'first_post_F_DC_source_closure_2026-10-24/manifest.json',R/'first_post_F_DC_source_closure_2026-10-24/terminal_C_maturity_premise_qualifier_manifest.json',R/'audits/check_first_F_DC_source_independent.json',R/'audits/check_first_F_DC_terminal_C_qualification_independent.json',R/'first_post_Q_B_DC_source_closure_2026-10-24/manifest.json',R/'audits/check_first_Q_B_DC_source_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'old_D_second_age3_common_beta_2026-10-24/manifest.json',R/'audits/old_D_age3_common_beta_independent.json',R/'firstpostV_F_piece_first_contact_2026-10-24/manifest.json',R/'audits/check_F_piece_firstpostV_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',CP,R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json',R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry completeG8 prefix,FIRSTF,first ordinary RAW D orC,arbitrary ordinary suffix with actual finalM11. GLOBAL first new contact cannot be owned by original properF piece. Outgoing FOREEXIT belongs b1 and is separately signed; no later-owner/arbitrary-tail simplicity or secondFOREIGN conclusion.',all62_closed_F_contact_heads=closed,all_foreign_EXIT_owner_aliases=terminal,all_piece_angle_impossible_rows=wrongwindow,all42_genuine_proper_F_owned_angle_labels=proper,fresh_D_common_entry_reserve=common,all128_coupled_F46_F47_source_current_first_loss_rows=pair,all8_universal_negative_y_current_input_RAW_exit_bounds=negends,all5_reused_literal_F_negative_output_guards=guards,extra_N4_actual_sourceD_hole_guard=N4,extra_W5_beta_same_ENTRY_reader_lift=W5,all84_firstpostD_C_proper_F_contact_closures=join,not_a_terminal_DCC_ban=True,no_G8_maturity_for_FOREIGN_outputs=True,no_universal_upper_minimum5_assumption=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'F_piece_DC.json').write_text(json.dumps(out,indent=2)+'\n');print('Original properF after firstD/C:42×2=84 closed;71 current masks,10 lowerF guards,1 exact min4 repaired hole,2 same-entry beta.')
