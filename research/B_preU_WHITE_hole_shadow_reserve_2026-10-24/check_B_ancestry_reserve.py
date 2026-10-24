"""Endpoint-conditioned physical WHITE reserve, then genuine pre-U ancestry
protects B g through C5 and prevents rebirth of B's deleted h. No global simplicity.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import importlib.util,json,hashlib
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
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None
# Physical last-R support. CORE writes are included, not only O exports.
support=[]
for atom in'DCVU':
 tr=l.trace(W[atom]);ep=after(W[atom]);zero=atom!='C'
 for q,(turn,tick)in tr['last'].items():
  if turn!='R':continue
  assert q[1]>=0 and q[0]>=-1
  if zero:assert q[1]<=ep[1]
  support.append(dict(atom=atom,actual_final_R_local=q,R_tick0=tick,R_read_number1=tick+1,initial_N0_write_y_lower_bound=q[1],initial_W1_write_y_lower_bound=1+q[0],S2_RAW_EXIT_minus_write_y= q[1]-ep[1]if zero else None,positive_C_atS2_cannot_complete_before_S2_reader=not zero,all_CORE_R_births_included=True))
assert len(support)==36 and sum(q['atom']!='C'for q in support)==28
zero=[]
for atom in'DVU':
 ep=after(W[atom]);assert ep[2]==0 and ep[1]>=1;zero.append(dict(atom=atom,N_zeroC_y_increment=ep[1],W_zeroC_y_increment=ep[0],S_zeroC_y_increment=-ep[1]));assert ep[0]>=0
assert after(W['C'])==(0,1,3)
# Generic endpoint lemma: initial h_y<=-1 is physically WHITE. Any lastR
# before S2 reader must be N0, W1 or non-C S2. N/W writes havey>=0;
# completed S writer exitsy<=h_y and remaining zero-C S cannot increasey.
GENERIC=dict(initial_actual_marked_cut=(0,0,0),initial_hole_condition='physically WHITE and h_y<=-1',reader_condition='actual S-facing ENTRY at exactC2 with head_y>h_y',conclusion='hole is still physically WHITE at that READER ENTRY',last_R_cases=['N0: all heads y>=0 and all finalR localy>=0, so cannot write negativey.','W1: all heads y>=1; finalR rotatedy=localx>=-1, so cannot write negativey.','S2 positiveC: cannot COMPLETE before the S2 reader because it would add C3.','S2 D/V/U: actual RAW EXITy minus written_cell_y<=0. After this completed writer noC remains; S zeroC motion never increasesy, so cannot reach reader head_y>h_y.'],no_age_U_ancestry_or_proxy_simplicity_needed=True,not_physical_WHITE_permanence='The hole may be restored at an S2 cut at/below its y, or after another C; this is only an endpoint-conditioned statement.')
# Actual firstB after complete8 has the necessary immediate plainU, not an
# invented shared CORE. Its own L1-deleted cell is missed by actual B RAW.
pre=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 tr=l.trace(raw(full+'B')+l.M);pre.append(dict(full=full,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
assert[q['full']for q in pre if q['feasible']]==['U']
ub=l.trace(raw('UB'));ubep=after(raw('UB'));old=(-1,0);P=l.rot(sub(old,ubep[:2]),-ubep[2]);assert P==(-2,-1)and ub['last'][old]==('L',1);bp=after(W['B']);inverse=add(bp[:2],l.rot(P,2));assert inverse not in l.trace(W['B'])['first']
S={(-2,-4),(-1,-4),(0,-4),(0,-3)};G=(-1,-2);gv=add(bp[:2],l.rot(G,2));assert l.trace(W['B'])['last'][gv]==('R',67)and list(gv)in l.literal_geometry(W['B'])['outputs'];fore=[((-5,-9),(1,-7)),((1,-7),(-1,-1))];loss=[]
for atom in'DCVU':
 geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
 for slot in map(tuple,geo['inputs']):
  for hd in range(4):
   p=(*sub(G,l.rot(slot,hd)),hd);q=dict(consumer=atom,input=slot,pose=p)
   if(sum(p[:2])+hd)%2:q['classification']='sector'
   elif any(l.rot(sub(tag,p[:2]),-hd)in tr['first']for tag in S):q['classification']='would_touch_original_CURRENT_B_hook_before_target'
   else:
    hits=[contact(a,b,*chord(atom,p))for a,b in fore]
    if any(hits):q.update(classification='earlier_B_proxy_contact',contacts=hits)
    else:q['classification']='S2_g_loss_helper_requires_old_U_hole_BLACK'
   loss.append(q)
keep=[q for q in loss if q['classification']=='S2_g_loss_helper_requires_old_U_hole_BLACK'];assert len(loss)==32 and {(q['consumer'],tuple(q['pose']))for q in keep}=={('V',(-1,1,2)),('U',(-2,2,2))}
helper=[]
for q in keep:
 atom=q['consumer'];p=tuple(q['pose']);assert p[2]==2 and p[1]>P[1];loc=l.rot(sub(P,p[:2]),-p[2]);first=l.trace(W[atom]+l.M)['first'][loc];assert first==('L',13 if atom=='V'else 23)
 helper.append(dict(g_loss_helper=q,clock_before_C5_target='S heading andK<=5 forceK2;K6 is beyond deadline.',old_preU_hole=P,reader_head_y=p[1],hole_y=P[1],WHITE_endpoint_reserve_applies=True,actual_first_BLACK_demand=o.describe(atom,first[1]),contradiction='WHITE at helperENTRY cannot satisfy its own firstL. HelperRAW cannot complete, before g EXITCORE absorption.'))
# Reuse the already independently checked full B h-origin cover unchanged,
# then add only the new g ENTRY field. All10 residues are direct initial
# conflicts: six BLACK firstR and four CURRENT-in-entryCORE.
EP=R/'Q_B_hook_MISS_first_contact_2026-10-24/five_MISS.json';ej=json.loads(EP.read_text());oldorig=ej['all208_B_CORE_inclusive_last_R_origins'];assert len(oldorig)==208
orig=[]
for atom in'DCVU':
 tr=l.trace(W[atom]+l.M);wt=l.trace(W[atom]);writes=[(q,t)for q,(cc,t)in wt['last'].items()if cc=='R']
 for clock in range(6):
  if atom=='C'and clock==5:continue
  hd=(-clock)%4
  for slot,tick in writes:
   pp=(*sub((0,-2),l.rot(slot,hd)),hd);row=dict(foreign='B',producer=atom,true_producer_ENTRY_C_clock=clock,true_producer_RAW_EXIT_C_clock=clock+int(atom=='C'),pose=pp,actual_final_R_local=slot,R_tick0=tick,R_read_number1=tick+1,RAW_EXIT=after(W[atom],pp),CORE_R_writes_included=True)
   if(sum(pp[:2])+hd)%2:why='sector'
   elif clock==0 and pp[1]<0:why='initial_N0_head_below0'
   elif clock==1 and pp[1]<1:why='initial_W1_head_below1'
   elif any(l.rot(sub(tag,pp[:2]),-hd)in tr['first']for tag in S):why='would_touch_CURRENT_original_hook_before_target'
   elif any(contact(a,b,*chord(atom,pp))for a,b in fore):why='earlier_actual_FOREIGN_proxy_contact'
   else:why='last_R_endpoint_obligation'
   row['classification']=why;orig.append(row)
assert len(orig)==208
def key(q):return(q['producer'],q['true_producer_ENTRY_C_clock'],tuple(q['pose']),tuple(q['actual_final_R_local']),q['R_tick0'],q['classification'])
assert set(map(key,orig))==set(map(key,oldorig))
res=[]
for q in orig:
 if q['classification']!='last_R_endpoint_obligation':continue
 atom=q['producer'];p=tuple(q['pose']);loc=l.rot(sub(G,p[:2]),-p[2]);tr=l.trace(W[atom]+l.M);fr=tr['first'].get(loc);assert loc in l.K or fr and fr[0]=='R'
 res.append(dict(original_CORE_inclusive_R_origin=q,SAME_B_g=G,producer_local_g=loc,actual_first=fr,actual_owner=None if fr is None else o.describe(atom,fr[1]),cut='CURRENT_g_in_producer_ENTRY_CORE'if loc in l.K else'SAME_BLACK_g_vs_producer_first_WHITE'))
assert len(res)==10 and Counter(q['cut']for q in res)=={'CURRENT_g_in_producer_ENTRY_CORE':4,'SAME_BLACK_g_vs_producer_first_WHITE':6}
h=(0,-2);hp=add(bp[:2],l.rot(h,2));assert l.trace(W['B'])['last'][hp]==('L',66)
# The entry state excludes each of the four proper B hook-MISS W5 targets.
TP=R/'Q_B_foreign_first_contact_hook_split_2026-10-24/hook_split.json';tj=json.loads(TP.read_text());targets=[t for t in tj['all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates']if t['foreign']=='B'];assert len(targets)==4;cuts=[]
for t in targets:
 p=(*t['head'],t['h']);atom=t['atom'];tr=l.trace(W[atom]+l.M);w=[]
 for cell,color in((G,True),(h,False)):
  loc=l.rot(sub(cell,p[:2]),-p[2]);f=tr['first'].get(loc)
  if loc in l.K and not color or f and(color!=(f[0]=='L')):w.append(dict(physical_guard=cell,actual_BLACK=color,local=loc,role='ENTRY_CORE_needsBLACK'if loc in l.K else'first_'+f[0],actual_owner=None if f is None else o.describe(atom,f[1])))
 assert w;cuts.append(dict(owner_aware_target=t,guard_contradictions=w,no_through_contact_persistence_assumed=True))
paths=[EP,R/'Q_B_hook_MISS_first_contact_2026-10-24/manifest.json',R/'audits/check_five_hook_MISS_independent.json',TP,R/'Q_B_foreign_first_contact_hook_split_2026-10-24/manifest.json',R/'foreign_Q_B_hook_contact_reserve_2026-10-24/manifest.json',R/'audits/check_foreign_hook_reserve_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_B_GENUINE_PREU_ANCESTRY_EARLY_SHADOW_HOLE_RESERVE_PENDING_REVIEW',generic36_physical_final_R_support_rows=support,all3_zeroC_head_displacements=zero,generic_negative_WHITE_S2_endpoint_reserve=GENERIC,all8_actual_complete8_to_B_predecessor_queries=pre,genuine_preU_hole=dict(actual_preU_cell=old,actual_U_last_L_tick0=1,actual_U_last_L_read_number1=2,post_B_cell=P,actual_B_RAW_MISS=True,physically_WHITE_at_B_EXIT=True),all32_B_original_g_first_CURRENT_loss_roles=loss,both_S2_g_helpers_blocked_by_WHITE_preU_hole=helper,g_guard_statement='After an actual complete8 interval and FIRSTB, SAME original B R67 g=(-1,-2) remains CURRENT at every ordinary cut before a nonadjacent B-proxy contact while Cclock<=5, and at ENTRY of a firstB-contact atom by that clock. Earlier ordinary-ordinary/preFORE selfcontacts need NOT be excluded. Before such contact, firstg loss either touches guardedhook, contactsB earlier, or uses an S2 helper requiring the oldU WHITEhole BLACK. The latter is impossible by genericR endpoint reserve. No claim through the firstB-contact atom.',all208_B_h_last_R_origins_freshly_reconstructed_without_simplicity=orig,all10_old_origin_residues_cut_by_new_g_field=res,h_WHITE_statement='At any same protected ENTRY/cut byC5, h=(0,-2), B L66-deleted, is physicallyWHITE. A BLACKvalue needs a laterlastR at a completed earlierRAW. The signed208-origin cover leaves10; every one conflicts with CURRENT g at its own ENTRY. AllCORE R births remain included. No freshdonor/simpleproxy law is used in this stronger B-only route.',all4_proper_B_hook_MISS_entry_cuts=cuts,scope='FIRSTB immediately after actual complete8, then ordinaryRAWs with actualmarkers, through C5 and before/atENTRY firstnonadjacent geometric contact with the CLOSED B proxy, including its terminal vertex. No earlier ordinary proxy simplicity assumed. No F/Q, laterforeign, physicalWHITE permanence, through-contact guard or capture theorem.',not_claimed='An S2 hole can be restored below its y, after anotherC, or during a contact. A currentg may retire during the firstB-contact atom; only its ENTRY is protected. No K6 attainability or indefinite shadow budget is inferred.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'B_ancestry_reserve.json').write_text(json.dumps(out,indent=2)+'\n');print('Generic negative WHITE hole S2 endpoint reserve from36 physicalR offsets. Genuine preU hole blocks2 earlyB-g losses; originalg CURRENT to firstBcontactENTRY throughC5. Newg cuts all10 oldhRfunders, hencehWHITE; fourB hookMISS cut. No global ordinary simplicity/freshdonor age.')
