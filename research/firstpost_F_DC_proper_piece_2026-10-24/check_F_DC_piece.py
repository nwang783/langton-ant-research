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
# Exact OLD F segment in actual postEXIT0N frame. Do not assign F's EXIT
# terminal to its incoming segment; that vertex belongs to outgoing b1D/C.
A0=(-7,-3);A1=(-1,-1);M=(2,0);CO={(2,0),(2,1),(1,2)};FT={(-3,-1),(-2,-1)}

def hit(a,b,c,d):
 u,v,w=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(w,v),den),F(det(w,u),den);return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(w,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((F(a[k]-c[k],v[k]),F(b[k]-c[k],v[k])));lo,hi=max(F(0),lo),min(F(1),hi)
 if lo>hi:return None
 p=(c[0]+lo*v[0],c[1]+lo*v[1]);j=0 if u[0]else 1;return(F(p[j]-a[j],u[j]),lo,hi)
from math import ceil,floor
win=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
allclosed=[];proper=[];terminal=[]
for a in'DCVU':
 for h in range(4):
  c,d=chord(a,(0,0,h));u,v=sub(A1,A0),sub(d,c);corn=[tuple(F(A0[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
  for x in range(floor(min(q[0]for q in corn)),ceil(max(q[0]for q in corn))+1):
   for y in range(floor(min(q[1]for q in corn)),ceil(max(q[1]for q in corn))+1):
    if(x+y+h)%2:continue
    co=hit(A0,A1,add(c,(2*x,2*y)),add(d,(2*x,2*y)))
    if not co or co[1]<=0:continue
    r=dict(actor=a,pose=(x,y,h),actual_old_s=str(co[0]),actual_new_t=str(co[1]),same_direction_parallel_interval=[str(q)for q in co[1:]]if len(co)==3 else None)
    allclosed.append(r)
    if co[0]==1:r.update(outgoing_owner='first_postforeign_ordinary_b1',not_incoming_F=True);terminal.append(r);continue
    w=next(z for z in win if z['source_class']=='Fprefix'and z['contact_atom']==a);K=[k for k in w['allowed_C_counts_before_contact_ENTRY']if(-k)%4==h];assert len(K)==1
    r.update(outgoing_owner='Fprefix',actual_post_FOREIGN_C_clock=K[0]);proper.append(r)
assert len(allclosed)==62 and len(proper)==42 and len(terminal)==20
assert all(r['actual_post_FOREIGN_C_clock']in(2,3,4,5)for r in proper)
assert all(r['pose'][0]<=1 for r in proper if r['actual_post_FOREIGN_C_clock']==4)
assert all(r['pose'][1]<=-1 for r in proper if r['actual_post_FOREIGN_C_clock']==5)
assert all(r['pose'][1]<=1 for r in proper if r['actual_post_FOREIGN_C_clock']==4)
# Portable source-D common projection. Every hypothetical first consumer is
# itself an actual BASE endpoint, even if its later C tail is not executed
# or is terminalDCC; the real next RAW supplies the same actualM11.
d3=json.loads((R/'old_D_second_age3_common_beta_2026-10-24/D_age3_common_beta.json').read_text());q64=[q for q in d3['all184_common_first_loss_full_role_queries']if q['consumer']in'DVU'];assert len(q64)==64
open5=[q for q in q64 if q['reason']=='NECESSARY'];print('q64 reasons',Counter(q['reason']for q in q64))
if len(open5)!=5:
 open5=[q for q in q64 if q['reason'].startswith('surviving')or'NECESSARY'in q['reason']or q['reason']=='OPEN']
# The signed exact5 list is also independently bound by its own dedicated key.
open5=d3['all5_surviving_completed_E3_plain_common_ports'];assert len(open5)==5
assert not any(q['reason']=='consumer_full_tail_cannot_complete_before_foreign3'for q in q64)
source_next=d3['all4_actual_next_N_atom_strict_crossing_interfaces'];assert len(source_next)==4
Mnormal=[]
for a in'DVU':
 for slot,(c,t)in l.trace(W[a]+l.M)['first'].items():
  if c!='L'or slot in l.K:continue
  for h in(0,3):
   p=(*sub(M,l.rot(slot,h)),h);ep=after(W[a],p)
   if h==0:assert ep[0]>=2 and ep[1]>=0
   else:assert ep[1]>=0
   Mnormal.append(dict(atom=a,input=slot,h=h,pose=p,RAW_EXIT=ep,N4_exit_x_ge2_and_y_ge0=h==0,W5_exit_y_ge0=h==3))
assert len(Mnormal)==16
Mreserve=dict(all64_source_D_DC_to_plain_BASE_common_queries=q64,all5_E3_base_ports_and_past_source_contacts=open5,all4_genuine_next_N_atom_crossings=source_next,all16_N4_W5_common_input_RAW_normal_bounds=Mnormal,scope='Any genuine selected RAW D with ACTUAL preceding seven-atom RAW, followed only ordinary RAWs. At SIMPLE source-prefix cuts: SAME common2,0 CURRENT through K3, at N4 targets x<=1, and W5 targets y<0. Earlier foreign allowed before selectedD; none after it. Every hypothetical earlier first-loss BASE is independently a valid G8 endpoint under the signed grammar. No G8 parse of terminal C/DCC is needed.',projection='Truncate the factor at the hypothetical earlier D/V/U consumer BASE, with actual next RAW supplyingM11. The consumer is genuinely plain D/V/U as END packet of this chosen factor even when actual later C tails continue outside it. Thus the64 plain BASE source/age queries are valid; no completion-before-FORE3 condition is reused for positive-C consumers. All5 E3 surviving BASE poses contact actual sourceD/its genuine actual next N atom. N4/W5 endpoint normals give the stated later target halfplanes.')
# SAME F46/F47 pair with NO incoming-beta anchor. Three extra N-facing
# losses are retained and blocked by actual RAW-exit normal ordering.
fpair=[]
for src,anchors in [('D',{M}),('C',CO)]:
 for tag in sorted(FT):
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for slot,(c,tick)in tr['first'].items():
    if c!='L'or slot in l.K:continue
    for h in range(4):
     p=(*sub(tag,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(source=src,SAME_F_tag=tag,consumer=a,pose=p,input=slot,owner=o.describe(a,tick),RAW_EXIT=ep)
     if(sum(p[:2])+h)%2:why='sector'
     else:
      touches=[dict(anchor=q,local=rel(q,p),first=tr['first'][rel(q,p)])for q in anchors if rel(q,p)in tr['first']]
      if touches:r['independently_CURRENT_anchor_touches']=touches;why='would_touch_independent_same_source_reserve_before_target'
      else:
       bad=conflict(a,p,FT)
       if bad:r['SAME_F_colour_conflicts']=bad;why='SAME_other_F_tag_ENTRY_CORE_or_first_WHITE'
       else:
        fc=contact(A0,A1,*chord(a,p));sc=contact(*chord(src,(0,0,0)),*chord(a,p))
        if fc or sc:r.update(actual_FOREIGN_contact=fc,actual_source_contact=sc);why='earlier_actual_F_or_source_proxy_contact'
        else:
         assert h==0 and p in[(-2,-2,0),(-2,-4,0),(-1,-5,0)]and ep==(-1,-1,0)
         why='N0_unreachable_or_N4_exit_y_minus1_cannot_reach_negative_y_N4_W5_target'
     r['route']=why;fpair.append(r)
assert len(fpair)==128
# All actual negative-y ports and final WHITE readers are literally the
# signed archive5. No firstpostV/U premise enters the coordinate lemma.
oldF=json.loads((R/'firstpostV_F_piece_first_contact_2026-10-24/F_piece_contact.json').read_text());negative=oldF['all5_proper_Fsource_lower_output_guards'];assert len(negative)==5
assert{(q['atom'],tuple(q['head']),q['h'])for q in negative}=={('D',(-4,-1),1),('V',(-6,-1),1),('U',(-7,-2),1),('U',(-4,0),2),('U',(-3,1),2)}
for q in negative:
 g=tuple(q['initial_SAME_FOREIGN_output_reserve']['postforeign_cell']);p=(*q['head'],q['h']);assert g[1]<=-1 and p[1]>g[1];x=rel(g,p);f=l.trace(W[q['atom']]+l.M)['first'][x];assert f[0]=='R'and f[1]<len(W[q['atom']])
# The source-D-only N4 U needs an actual source-CORE deleted cell as a true
# upper input of produced age<=4. Any old entry exemption died at sourceL1.
target=(-1,-3,0);g=(-1,0);assert l.trace(W['D'])['last'][g]==('L',1)and rel(g,target)==(0,3)
for src in['D','DC']:
 t=l.trace(''.join(W[a]for a in src));assert t['last'][g]==('L',1)and list(g)not in l.literal_geometry(''.join(W[a]for a in src))['outputs']
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);NEW={a:i for i,a in enumerate(IDS)}
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HP=R/'core_periodicity_new/chronology_dcuv/protected_patch2.tsv';COUNTED={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()};HB={tuple(map(int,line.split()[:7]))for line in HP.read_text().splitlines()}
upper_queries=[]
for producer in IDS:
 for out in G[producer]['outputs']:
  for age in range(5):
   h=(-age)%4;p=(*sub(out,l.rot((0,3),h)),h);key=(NEW[producer],NEW[7],*p,*out,age);hb=(producer,7,*p,*out)
   if age<G[producer]['name'].count('C'):why='producer_not_completed_before_TRUE_input'
   elif(sum(p[:2])+h)%2:why='sector'
   elif hb in HB:why='signed_HB'
   else:assert key in COUNTED;why='signed_COUNT5'
   upper_queries.append(dict(actual_full_producer=G[producer]['name'],output=out,true_full_source_ENTRY_age=age,full_U_pose=p,actual_U_TRUE_input=(0,3),counted_key=key,HB_key=hb,route=why))
assert len(upper_queries)==340
upper=dict(actor='U',pose=target,source_D_cell=g,actual_source_last_L_tick0=1,source_last_L_read1=2,actual_goal_TRUE_input=(0,3),actual_goal_first=l.trace(W['U']+l.M)['first'][(0,3)],owner=o.describe('U',l.trace(W['U']+l.M)['first'][(0,3)][1]),all340_existing_producer_specific_upper_age0_to4_exclusions=upper_queries,maximum_new_full_source_age=4,proof='Select actual sourceD-to-goalU BASE factor; signed grammar makes realG8. Cellg is actual source entryCORE then physically deletedL1, absent both actual initial D/DC output sets, hence no old entry ID can fund it. At goal it is outside entryCORE and has actual firstL23; any genuine BLACK must be a new residual output born inside the selected G8 factor. Its sourceENTRY clock>=0 gives age<=4, excluded by the explicit eight-producer HB/COUNT5 inventory through age4. CORE-only funding cannot occupy a TRUE external input outside goalENTRYK.')
# Existing beta W5 proof is entry-pose/first-M11 only. The new U reader has
# exactly the same actual K and M11 as C at0,-1,W; no targetC body was used.
pbeta=(1,-1);ureader=(0,-1,3);assert rel(pbeta,ureader)in l.K and W['U'][:11]==W['C'][:11]==l.M
beta_lift=dict(actor='U',pose=ureader,actual_C_clock=5,SAME_original_FOREIGN_EXIT_beta=pbeta,beta_local=rel(pbeta,ureader),beta_in_actual_ENTRY_CORE=True,premise_lift='Signed8b58+5e243 beta interface targets W5 pose0,-1 and uses only actual target ENTRY/core and firstM11, not C body. Earlier source-consumer contacts, nonadjacent entry repeat, freshU star in universalK and late BASE-helper main guard are identical for this U reader. The helper BASE is a real endpoint with actualM11 supplied by U; terminalC/DCC is never parsed. Original beta is CURRENT at this ENTRY, conflicting with the same actualK.')
closures=[]
for src,held in [('D',{M}|FT),('C',CO|FT)]:
 for q in proper:
  a=q['actor'];p=tuple(q['pose']);K=q['actual_post_FOREIGN_C_clock'];r=dict(first_ordinary_source=src,**q);bad=conflict(a,p,held)
  if bad:r.update(route='independent_source_reserve_and_SAME_F46_F47_CURRENT_colour',guards=bad)
  else:
   ng=next((x for x in negative if x['atom']==a and tuple(x['head'])==p[:2]and x['h']==p[2]),None)
   if ng:r.update(route='existing_genuine_negative_y_FOREIGN_output_coordinate_guard',guard=ng)
   elif src=='D'and a=='U'and p==target and K==4:r.update(route='source_D_L1_deleted_CORE_upper_input_max_age4_below5',guard=upper)
   else:assert a=='U'and p==ureader and K==5;r.update(route='same_pose_reader_independent_CURRENT_beta_inside_U_ENTRY_CORE',guard=beta_lift)
  closures.append(r)
assert len(closures)==84
assert Counter(r['route']for r in closures)=={'independent_source_reserve_and_SAME_F46_F47_CURRENT_colour':71,'existing_genuine_negative_y_FOREIGN_output_coordinate_guard':10,'source_D_L1_deleted_CORE_upper_input_max_age4_below5':1,'same_pose_reader_independent_CURRENT_beta_inside_U_ENTRY_CORE':2}
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'first_post_F_DC_source_closure_2026-10-24/manifest.json',R/'first_post_F_DC_source_closure_2026-10-24/terminal_C_maturity_premise_qualifier_manifest.json',R/'audits/check_first_F_DC_source_independent.json',R/'first_post_Q_B_DC_source_closure_2026-10-24/manifest.json',R/'audits/check_first_Q_B_DC_source_independent.json',R/'old_D_second_age3_common_beta_2026-10-24/manifest.json',R/'audits/old_D_age3_common_beta_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'firstpostV_F_piece_first_contact_2026-10-24/manifest.json',CP,HP];D=[p for p in D if p.exists()]
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry G8 prefix, FIRST F, first ordinaryD/C, arbitrary ordinary RAW suffix and actual finalM11. GLOBAL first new proxy contact cannot be owned by proper F piece. Actual FOREEXIT terminal returns are routed to outgoing b1D/C via separately signed source theorem. No other old/later ordinary source, second foreign or arbitrary-tail simplicity.',all62_closed_F_contact_geometries=allclosed,all20_FORE_EXIT_owned_by_outgoing_b1_D_C=terminal,all42_proper_F_owned_angle_geometries=proper,fresh_D_common_normal_reserve=Mreserve,all128_coupled_F46_F47_roles_with_NO_beta_anchor=fpair,F_pair_statement='At all proper F contact targets: sourceD common is CURRENT by its BASE-projection/normal reserve; fresh sourceC O3 by its separately signed reserve. Earliest F46/F47 loss is an anchor touch, held-F colour conflict, earlier actualF/source contact, or N0/N4 D/V/U exiting at-1,-1,N. N0 is unreachable after either selected source. At N4 the candidate F contact has y<=-2; at W5 anotherC raises y to0, while candidates have y<=-1. Neither endpoint can be reached. No incoming-beta anchor or postforeign age is assumed for this pair.',all5_existing_negative_y_FOREIGN_output_guards=negative,source_D_four_C_deleted_CORE_upper_guard=upper,W5_same_ENTRY_U_reader_beta_lift=beta_lift,all84_first_D_C_proper_F_contact_exclusions=closures,terminal_DCC_scope='Only hypothetical earlier loss BASE, actual late helperBASE, or actual U goalBASE is parsed into G8. A terminal C/DCC target is never parsed by assumption. Foreforeign terminal vertex sourceowner is explicitly outgoingb1D/C, not Fpiece.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'F_DC_piece.json').write_text(json.dumps(out,indent=2)+'\n');print('Proper F source84=71current+10negative-coordinate+1actualG8 upper+2entry-beta.20FOREterminal aliases routed to signedb1source theorem.')
