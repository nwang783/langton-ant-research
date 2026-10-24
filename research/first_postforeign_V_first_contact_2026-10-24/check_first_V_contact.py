"""Arbitrary-length FIRST contact with the first postforeign outgoing V source.
Signed SAME-pair guardian, coupled F reserve, B endpoint guard and whole-V bud reserve.
No prefix-depth enumeration, postforeign maturity or through-contact pair assumption.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(T):return ''.join(W[a]for a in T)
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def edge(q):
 x,y=q
 return((2*x-1,2*y-1),(2*x+1,2*y+1))if(x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None

def initial_hits(held,tr,p,all_touches=False):
 out=[]
 for tag in sorted(held):
  q=l.rot(sub(tag,p[:2]),-p[2]);f=tr['first'].get(q)
  if q in l.K or f and(all_touches or f[0]=='R'):out.append(dict(SAME_tag=tag,local=q,role='ENTRY_CORE'if q in l.K else f[0],first=f,actual_owner=None if f is None else o.describe('D',0)))
 return out
# Replace the placeholder owner with the actual RAW below when required.
def typed_hits(held,a,p,all_touches=False):
 tr=l.trace(W[a]+l.M);hits=initial_hits(held,tr,p,all_touches)
 for q in hits:
  if q['first']:q['actual_owner']=o.describe(a,q['first'][1])
 return hits
PAIR={(0,0),(0,1)};VO=set(map(tuple,l.literal_geometry(W['V'])['outputs']));OLD=chord('V',(0,0,0));FORE={'F':[((-7,-3),(-1,-1))],'Q':[((-7,-7),(-1,-5)),((-1,-5),(-1,-1))],'B':[((-5,-9),(1,-7)),((1,-7),(-1,-1))]}
V_BIRTHS=[]
for tag in sorted(VO):
 turn,tick=l.trace(W['V'])['last'][tag];assert turn=='R'
 V_BIRTHS.append(dict(SAME_first_V_output=tag,actual_last_R_tick0=tick,birth_read_number1=tick+1,outside_actual_source_RAW_EXIT_CORE=True))
# Exact postFOREIGN-source angle window. No fixed atom number is present.
WP=R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json';wj=json.loads(WP.read_text());win=[q for q in wj['all44_exact_source_target_C_window_rows']if q['source_class']=='postFOREIGN_ordinary'and q['source_atom']=='V'];assert len(win)==4
allowed={q['contact_atom']:q['allowed_C_counts_before_contact_ENTRY']for q in win};assert allowed=={'D':[3,4,5,6],'C':[3,4,5,6],'V':[3,4,5],'U':[2,3,4,5]}
a,b=OLD;u=sub(b,a);boxes=[];geos=[]
for atom in'DCVU':
 for K in allowed[atom]:
  hd=(-K)%4;c,d=chord(atom,(0,0,hd));v=sub(d,c);de=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];box=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(target=atom,K=K,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=box))
  for x in range(box[0][0],box[0][1]+1):
   for y in range(box[1][0],box[1][1]+1):
    if(x+y-K)%2:continue
    diff=sub(add(c,(2*x,2*y)),a)
    if de:
     s,t=Q(det(diff,v),de),Q(det(diff,u),de)
     if not(0<=s<1 and 0<t<=1):continue
     kind='nonparallel'
    else:
     if det(diff,u):continue
     assert atom=='V'and K==4 and v==u;s,t=Q(0),-Q(diff[0],u[0]);kind='same_direction_first_positive_onset'
     if not(0<t<=1):continue
    p=(x,y,hd);hits=typed_hits(PAIR,atom,p);tr=l.trace(W[atom]+l.M);trueinputs=[]
    for tag in sorted(PAIR):
     q=l.rot(sub(tag,p[:2]),-hd);f=tr['first'].get(q)
     if f and f[0]=='L'and q not in l.K:trueinputs.append(dict(SAME_tag=tag,local=q,actual_owner=o.describe(atom,f[1]),loss_during_contact_is_ALLOWED=True))
    geos.append(dict(target=atom,K=K,pose=p,old_s=str(s),new_t=str(t),kind=kind,pair_entry_conflicts=hits,pair_TRUE_inputs_during_contact=trueinputs,classification='pair_entry_cut'if hits else'necessary_after_pair_entry_guard'))
assert len(boxes)==15 and len(geos)==39 and Counter(q['classification']for q in geos)=={'pair_entry_cut':31,'necessary_after_pair_entry_guard':8}
# A coupled all-age F reserve, conditional on SAME first-V pair remaining
# current before the contact. TRUE pair inputs are forbidden here only because
# this is an EARLIER loss atom, not the contact atom itself.
FS={(-3,-1),(-2,-1)};ft=l.trace(W['F']);fep=after(W['F']);f_birth=[]
for tag in sorted(FS):
 physical=add(fep[:2],l.rot(tag,fep[2]));c,t=ft['last'][physical];assert c=='R'and t in(46,47)and list(physical)in l.literal_geometry(W['F'])['outputs'];assert tag not in l.trace(W['V']+l.M)['first'];f_birth.append(dict(postFOREIGN_cell=tag,actual_F_cell=physical,last_R_tick0=t,own_read_number1=t+1,firstV_COMPLETE_context_MISS=True))
froles=[]
for tag in sorted(FS):
 for atom in'DCVU':
  geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for slot in map(tuple,geo['inputs']):
   for hd in range(4):
    p=(*sub(tag,l.rot(slot,hd)),hd);q=dict(lost_SAME_F_tag=tag,consumer=atom,input_slot=slot,pose=p)
    if(sum(p[:2])+hd)%2:q['classification']='sector'
    else:
     ph=typed_hits(PAIR,atom,p,True);fh=typed_hits(FS,atom,p)
     hF=contact(*FORE['F'][0],*chord(atom,p));hV=contact(*OLD,*chord(atom,p))
     if ph:q.update(classification='would_change_guarded_V_pair_before_contact',pair_touches=ph)
     elif fh:q.update(classification='SAME_F_reserve_initial_CORE_or_WHITE',F_conflicts=fh)
     else:assert hF or hV;q.update(classification='actual_earlier_F_or_V_proxy_contact',F_contact=hF,V_contact=hV)
    froles.append(q)
assert len(froles)==64
# Any first physical R repair of h0 after sourceV L1 must be the FIRST local
# read of its RAW. Enumerate all such R reads, including writes into CORE.
HOLE=(-1,0);BLACK4=PAIR|FS;repair=[]
for atom in'DCVU':
 tr=l.trace(W[atom]);ctx=l.trace(W[atom]+l.M)
 for slot,(turn,tick)in tr['first'].items():
  if turn!='R':continue
  for hd in range(4):
   p=(*sub(HOLE,l.rot(slot,hd)),hd);q=dict(ordinary_RAW=atom,first_R_local=slot,first_R_tick0=tick,first_R_read_number1=tick+1,pose=p,includes_active_CORE_write=True)
   if(sum(p[:2])+hd)%2:q['classification']='sector'
   else:
    hits=typed_hits(BLACK4,atom,p,True);hf=contact(*FORE['F'][0],*chord(atom,p));hv=contact(*OLD,*chord(atom,p))
    if hits:q.update(classification='would_touch_SAME_guarded_BLACK_identity_before_contact',held_touches=hits)
    else:assert hf or hv;q.update(classification='actual_earlier_F_or_V_proxy_contact',F_contact=hf,V_contact=hv)
   repair.append(q)
assert len(repair)==104 and l.trace(W['V'])['last'][HOLE]==('L',1)
# F remaining clock3 D has an actual immediate ordinary predecessor. All four
# exact predecessor endpoints fail, independently of length of earlier rails.
fDprev=[];target=(-1,0,1)
for atom in'DCVU':
 hd=(target[2]+1)%4 if atom=='C'else target[2];ep=after(W[atom],(0,0,hd));p=(target[0]-ep[0],target[1]-ep[1],hd);hits=typed_hits(BLACK4,atom,p,True);assert hits
 if atom=='C':assert any(tuple(q['SAME_tag'])==(0,1)for q in hits)
 else:assert any(tuple(q['SAME_tag'])in FS and q['role']=='R'for q in hits)
 fDprev.append(dict(actual_previous_RAW=atom,pose=p,actual_EXIT=after(W[atom],p),preserved_guard_touches=hits,reason='PriorC violates currentA in CORE; priorD/V/U demandsWHITE at SAME F tag'))
# B's one remaining E3 target needs its g BLACK-to-WHITE demand. Classify every
# earlier possible CURRENT g loss, allowing CORE capture. Pair must MISS that
# earlier consumer; it may be consumed during the actual target, not before.
BG=(-1,-2);bep=after(W['B']);bgphysical=add(bep[:2],l.rot(BG,bep[2]));assert l.trace(W['B'])['last'][bgphysical]==('R',67)and BG not in l.trace(W['V']+l.M)['first'];bgloss=[]
for atom in'DCVU':
 geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
 for slot in map(tuple,geo['inputs']):
  for hd in range(4):
   p=(*sub(BG,l.rot(slot,hd)),hd);q=dict(consumer=atom,slot=slot,pose=p,RAW_EXIT=after(W[atom],p))
   if(sum(p[:2])+hd)%2:q['classification']='sector'
   else:
    ph=typed_hits(PAIR,atom,p,True);hs=[contact(*f,*chord(atom,p))for f in FORE['B']]+[contact(*OLD,*chord(atom,p))]
    if ph:q.update(classification='pair_must_MISS_before_target',pair_touches=ph)
    elif any(hs):q.update(classification='earlier_B_or_V_proxy_contact',contacts=hs)
    else:q['classification']='endpoint_obligation'
   bgloss.append(q)
bgkeep=[q for q in bgloss if q['classification']=='endpoint_obligation'];assert {(q['consumer'],tuple(q['pose']))for q in bgkeep}=={('D',(-1,-3,0)),('U',(-2,0,2)),('U',(-2,2,2))}
for q in bgkeep:
 if q['pose'][2]==0:q['causal_exclusion']='K<=3 and N implyK0. SourceV exitsy3; zero-C N never lowers y, so cannot reach heady-3.'
 else:
  assert q['RAW_EXIT'][1]in(-4,-2);q['causal_exclusion']='K<=3 and S implyK2. RAW_EXIT y<=-2, one remaining S->E C lowers y by1 and S/E zero-C motion never increasesy, so cannot reach target U(-2,-1,E).';q['max_reachable_E_y'] = q['RAW_EXIT'][1]-1;assert q['max_reachable_E_y']<-1
# Earliest loss of the ENTIRE six-output V cohort. No arbitrary selected-input
# age is imported: literal held-color masks, source contact and genuine bridge.
cohortroles=[]
for tag in sorted(VO):
 for atom in'DCVU':
  geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for slot in map(tuple,geo['inputs']):
   for hd in range(4):
    p=(*sub(tag,l.rot(slot,hd)),hd);q=dict(lost_SAME_V_output=tag,consumer=atom,slot=slot,pose=p)
    if(sum(p[:2])+hd)%2:q['classification']='sector'
    else:
     bad=typed_hits(VO,atom,p);hit=contact(*OLD,*chord(atom,p))
     if bad:q.update(classification='initial_SAME_cohort_CORE_or_WHITE',conflicts=bad)
     elif hit:q.update(classification='actual_earlier_source_V_proxy_contact',contact=hit)
     else:q['classification']='noncontact_first_loss_gate'
    cohortroles.append(q)
assert len(cohortroles)==192 and Counter(q['classification']for q in cohortroles)=={'sector':96,'initial_SAME_cohort_CORE_or_WHITE':86,'actual_earlier_source_V_proxy_contact':5,'noncontact_first_loss_gate':5}
ck=[q for q in cohortroles if q['classification']=='noncontact_first_loss_gate'];assert {(q['consumer'],tuple(q['pose']))for q in ck}=={('V',(0,4,2)),('U',(-1,5,2)),('D',(3,2,3)),('V',(5,2,3)),('U',(6,3,3))}
# Bud bridge: the SAME A half-edge, B, common, C and bud output edges.
P=(0,2);L=(1,1);Z=(3,-1);RR=(5,1);TT=(3,3);BB=(5,5);bridge=[BB,TT,RR,Z,L,P]
assert set(edge((0,1)))=={(-1,3),L};assert set(edge((1,0)))=={L,Z};assert set(edge((2,0)))=={Z,RR};assert set(edge((2,1)))=={RR,TT};assert set(edge((2,2)))=={TT,BB}
bridge_checks=[]
for j,(c,d)in enumerate(zip(bridge,bridge[1:])):
 for i,(a0,b0)in enumerate(list(zip(bridge,bridge[1:]))[:j]):
  hh=contact(a0,b0,c,d);adj=bool(hh and j==i+1 and b0==c and(hh.get('old_s')=='1'and hh.get('new_t')=='0'or hh.get('collinear_old_interval')==['1','1']))
  assert hh is None or adj;bridge_checks.append(dict(old_edge=i,new_edge=j,contact=hh,legitimate_adjacent_point_join=adj))
def cpow(z,n):
 if n<0:
  norm=z[0]*z[0]+z[1]*z[1];return cpow((Q(z[0],norm),Q(-z[1],norm)),-n)
 out=(Q(1),Q(0))
 for _ in range(n):out=(out[0]*z[0]-out[1]*z[1],out[0]*z[1]+out[1]*z[0])
 return out
def ray(coeff):
 a=cpow((1,1),coeff[0]);b=cpow((3,1),coeff[1]);return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def check_turn(u,v,coeff):
 dot=u[0]*v[0]+u[1]*v[1];dt=det(u,v);rr=ray(coeff);assert dot*rr[1]-dt*rr[0]==0 and dot*rr[0]+dt*rr[1]>0
 lo,hi=min(coeff[0],coeff[0]+coeff[1]),max(coeff[0],coeff[0]+coeff[1]);assert lo>-4 and hi<4
 return dict(incoming=u,outgoing=v,principal_pi_over4_beta=coeff,exact_dot_det=(dot,dt))
source_interfaces=[]
for c,d in zip(bridge,bridge[1:]):
 h=contact(P,OLD[1],c,d)
 if h:assert h.get('old_s')=='0'and h.get('point')==['0','2']
 source_interfaces.append(dict(bridge_edge=[c,d],source_partial_chord_contact=h))
budgates=[]
for atom,p in(('D',(3,2,3)),('V',(5,2,3)),('U',(6,3,3))):
 ep=after(W[atom],p);assert ep==(2,3,3)and z(ep)==BB;contacts=[]
 for i,(c,d)in enumerate(zip(bridge,bridge[1:])):
  h=contact(*chord(atom,p),c,d)
  if h:assert i==0 and h.get('old_s')=='1'and h.get('new_t')=='0'
  contacts.append(h)
 loc=l.rot(sub((2,2),p[:2]),-p[2]);tr=l.trace(W[atom]+l.M);assert loc not in l.trace(W[atom])['first']and tr['first'][loc]==('L',len(W[atom])+1)
 # alphaH-alphaV and closing expressed as pi/4 + beta coefficients.
 open_delta={'D':(-1,1),'V':(0,0),'U':(0,1)}[atom];closing={'D':(-1,-1),'V':(-2,0),'U':(-2,-1)}[atom];assert tuple(open_delta[k]+closing[k]for k in(0,1))==(-2,0)
 bd=[sub(d,c)for c,d in zip(bridge,bridge[1:])];sourcevec=sub(OLD[1],P);consumervec=sub(chord(atom,p)[1],chord(atom,p)[0]);coeffs=[{'D':(2,0),'V':(1,1),'U':(1,0)}[atom],(2,0),(-2,0),(-2,0),(0,0),(-1,-1)];vs=[consumervec]+bd+[sourcevec];exactjoins=[check_turn(x,y,cf)for x,y,cf in zip(vs,vs[1:],coeffs)];assert tuple(sum(cf[k]for cf in coeffs)for k in(0,1))==closing
 budgates.append(dict(exact_closing_principal_joins=exactjoins,consumer=atom,pose=p,actual_RAW_EXIT=ep,corrected_EXIT=BB,SAME_bud_input_local=loc,physical_L=o.describe(atom,len(W[atom])+1),bud_aliveCORE_at_RAW_EXIT=True,consumer_bridge_contacts=contacts,ordinary_open_delta_pi_over4_beta=open_delta,closing_pi_over4_beta=closing,total_turn='(K-1)*pi/2',Jordan_nonnegative_K=[5],post_loss_target_obstruction='At K5 no Cs remain before any K5 W contact. Zero-C W cannot lower y from actual EXITy3 to targety2 or1.'))
# Final disjoint route assignment. Q/B hook applies at ENTRY, never through a
# contact that consumes a TRUE hook input. The r/A true inputs are retained.
HOOKS={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}};joint=[]
for i,g in enumerate(geos):
 atom,p,K=g['target'],tuple(g['pose']),g['K']
 for fore in'FQB':
  row=dict(geometry_index0=i,foreign=fore,target=atom,K=K,pose=p,pair_TRUE_inputs_during_contact=g['pair_TRUE_inputs_during_contact'])
  if g['pair_entry_conflicts']:row.update(route='SAME_V_pair_entry_cut',conflicts=g['pair_entry_conflicts'])
  else:
   hh=typed_hits(HOOKS.get(fore,set()),atom,p)
   if hh:row.update(route='SAME_Q_B_hook_entry_cut',conflicts=hh)
   elif K==5:
    assert (atom,p)in{('V',(1,2,3)),('U',(1,2,3)),('U',(2,1,3))};hits=typed_hits(VO,atom,p);assert any(h['role']=='ENTRY_CORE'for h in hits);row.update(route='K5_full_V_cohort_bud_reserve_ENTRY_CORE_cut',conflicts=hits)
   elif fore=='F':
    fh=typed_hits(FS,atom,p)
    if fh:row.update(route='coupled_SAME_F_two_tag_entry_cut',conflicts=fh)
    elif K==3:
     assert(atom,p)==('D',(-1,0,1));row.update(route='coupled_F_actual_last_predecessor_cut',all4_predecessors=fDprev)
    else:
     assert(K,atom,p)==(4,'U',(0,-2,0));loc=l.rot(sub(HOLE,p[:2]),-p[2]);assert l.trace(W[atom]+l.M)['first'][loc]==('L',13);row.update(route='coupled_F_unrepaired_WHITE_core_hole_cut',hole=HOLE,actual_need=o.describe(atom,13))
   else:
    assert(fore,K,atom,p)==('B',3,'U',(-2,-1,1));loc=l.rot(sub(BG,p[:2]),-p[2]);assert l.trace(W[atom]+l.M)['first'][loc]==('R',6);row.update(route='B_g_first_loss_endpoint_guard_WHITE_cut',SAME_B_R67=BG,actual_need=o.describe(atom,6))
  joint.append(row)
assert len(joint)==117 and Counter(q['route']for q in joint)=={'SAME_V_pair_entry_cut':93,'SAME_Q_B_hook_entry_cut':9,'K5_full_V_cohort_bud_reserve_ENTRY_CORE_cut':9,'coupled_SAME_F_two_tag_entry_cut':3,'coupled_F_actual_last_predecessor_cut':1,'coupled_F_unrepaired_WHITE_core_hole_cut':1,'B_g_first_loss_endpoint_guard_WHITE_cut':1}
paths=[WP,R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/manifest.json',R/'audits/check_postforeign_V_pair_guardian_independent.json',R/'foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_hook_reserve_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FIRST_POSTFOREIGN_V_ARBITRARY_LENGTH_FIRST_CONTACT_CLOSURE_PENDING_REVIEW',scope='Actual U-entry complete8 prefix, FIRST completeFOREIGN, immediate ordinaryV, then arbitrary ordinary RAW suffix with actual markers. A GLOBAL FIRST new proxy contact by a completed ordinary RAW+actualM11 cannot have outgoing owner the FIRST postFOREIGN V chord. No fixed atom count, no later sourceV, other sources, through-contact pair persistence or arbitrary-tail simplicity.',all4_signed_sourceV_contact_C_windows=win,all15_exact_contact_boxes=boxes,all39_outgoing_owned_geometries=geos,SAME_F_tag_births=f_birth,all64_coupled_F_two_tag_first_loss_roles=froles,F_reserve_statement='At every entry before GLOBAL FIRST contact, SAME F tags(-3,-1),(-2,-1) stay CURRENT while firstV pair remains current. Firstloss either changes guardedpair, contradicts heldF initial colors/core, or causes an earlier F/V contact. Simultaneous F inputs are retained. This reserve is conditional on firstreturnedV and nonterminal simple history, not a universal F hook.',all104_physical_first_R_repair_roles_for_F_hole=repair,F_WHITE_hole_statement='SourceV L1 leaves(-1,0) WHITE. An earliest later physical R, including insideCORE, must be its RAW first local read R. All104 roles are excluded by sector, touching one of four SAME guardedBLACK identities before target, or an earlier F/V proxy contact. Thus no such repair precedes the candidate entry. No initial WHITE cell is treated as a residual identity.',all4_F_D_E3_actual_immediate_predecessor_guards=fDprev,all32_B_g_earlier_CURRENT_loss_roles=bgloss,all3_B_g_endpoint_obligations=bgkeep,B_g_statement='For sole remaining B E3 target U(-2,-1,E), any earlier g loss has N0 or S2 heading. N0 targetbelow sourceV exit is unreachable; both S2 U exits are y<=-2, and one remaining C plus S/E monotonicity cannot reach targety-1. SAME B R67 g is therefore still CURRENT/BLACK at targetENTRY, contradicting its R6 demand.',all192_entire_V_cohort_first_loss_roles=cohortroles,whole_cohort_K5_statement='Before K5 W candidates, pairguardian excludes earlier A/r loss. Firstloss of ANY of six genuine output identities must therefore be one of three bud gates. The SAME protected output-tree bridge closes the simple source-to-budloss subarc; exact turns give(K-1)pi/2 and K5. All three actual RAW exits are(2,3,W), too high to reach targety2/1 with zero Cs left. Therefore ALL six are still CURRENT at candidateENTRY, where C/bud/common ENTRY CORE overlap is impossible.',genuine_current_bud_bridge_reversed=bridge,all_exact_bud_bridge_pair_checks=bridge_checks,all6_actual_source_R_birth_facts=V_BIRTHS,source_partial_chord_bud_bridge_interfaces=source_interfaces,all3_bud_gate_Jordan_and_EXIT_interfaces=budgates,all117_FOREIGN_typed_disjoint_exclusion_routes=joint,conclusion='All39 first-postV source geometries, typed by all3 firstFOREIGN words, are excluded by genuine entry fields or causal endpoint reserves. Pair TRUE inputs during the contact remain explicitly allowed in the necessary stage; they are not erased using a through-contact persistence assumption. This closes ONLY the firstpostV outgoing source class for GLOBAL FIRST contacts.',no_word_depth_search_or_postFOREIGN_maturity_or_activeCORE_ghostwire=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'first_V_contact.json').write_text(json.dumps(out,indent=2)+'\n');print('FirstpostFOREIGN V firstcontact:15 windows/39 geometries/117 types all closed.31 pair cuts; exact F two-tag/WHITE-hole guard, B g endpoint guard and K5 six-output bud reserve. No atom-count cap or postA age; pair TRUE inputs during contact retained.')
