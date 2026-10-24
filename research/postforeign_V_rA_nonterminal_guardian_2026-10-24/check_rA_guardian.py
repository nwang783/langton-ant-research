"""First postforeign V SAME r/A guardian for simple, nonterminal ordinary prefixes.
First loss may erode alive into CORE, but exact two-C loss endpoints are terminal.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
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
# Fresh ordinary RAW local survivor-edge proof: no old-eight authority is
# silently transported through the foreign. All later atoms are plain RAW
# with their ACTUAL next M11, and all CURRENT statuses are at real RAW cuts.
barriers=[]
for a in'DCVU':
 geo=l.literal_geometry(W[a]);tr=l.trace(W[a]+l.M);s,e=chord(a,(0,0,0));v=sub(e,s);k=0 if v[0]else 1
 box=[(Q(min(s[j],e[j])-1,2).__floor__(),Q(max(s[j],e[j])+1,2).__ceil__())for j in(0,1)];opened=[]
 for x in range(box[0][0],box[0][1]+1):
  for y in range(box[1][0],box[1][1]+1):
   q=(x,y);a0,b0=edge(q);h=contact(a0,b0,s,e)
   if not h:continue
   if 'new_t'in h:interior=0<Q(h['new_t'])<1
   else:
    lo,hi=sorted((Q(a0[k]-s[k],v[k]),Q(b0[k]-s[k],v[k])));interior=max(lo,Q(0))<min(hi,Q(1))or lo==hi and 0<lo<1
   if not interior:continue
   role='entry_CORE'if q in l.K else'TRUE_residual_input'if list(q)in geo['inputs']else'before_WHITE'if tr['first'][q][0]=='R'else'BAD';assert role!='BAD';opened.append(dict(cell=q,contact=h,actual_before_role=role))
 endpoints=[];ep=after(W[a]);Kexit={add(ep[:2],l.rot(q,ep[2]))for q in l.K}
 for center,K in((s,l.K),(e,Kexit)):
  incident=[]
  for x in range((center[0]-2)//2,(center[0]+2)//2+2):
   for y in range((center[1]-2)//2,(center[1]+2)//2+2):
    q=(x,y)
    if center in edge(q):incident.append(q);assert q in K
  assert len(incident)==4;endpoints.append(dict(actual_corrected_center=center,all4_incident_physical_cells=incident,inside_actual_transported_CORE=True))
 barriers.append(dict(ordinary_RAW=a,exact_expanded_rectangle=box,all_open_chord_edge_contacts=opened,actual_endpoint_incidence=endpoints,actual_residual_input_set=geo['inputs'],CORE_capture_covered_by_input_mask='Any old current identity at entry is outside entryK. Physical firstL, recycling, or RAWexit CORE absorption is therefore an I member of actual RAW+M11; C has I empty. Marker-only I counts CURRENT loss at this RAW EXIT, not later physical death.'))
assert [len(r['all_open_chord_edge_contacts'])for r in barriers]==[1,1,1,4]
# Sector covariance. Source-chart even-dual cells rotate correctly at exactly
# the actual ordinary reachable parity x+y+h even; no age is used.
for hd,p in((0,(0,0)),(1,(1,0)),(2,(0,0)),(3,(1,0))):
 for x in range(-2,4):
  for y in range(-2,4):
   q=(x,y);g=add(p,l.rot(q,hd));rotated={add((2*p[0],2*p[1]),l.rot(e,hd))for e in edge(q)};assert rotated==set(edge(g))
# Every possible earliest loss of SAME r/A, including simultaneous inputs
# and marker-owned EXIT CORE capture, is retained before filtering.
r=(0,0);A=(0,1);pair={r,A};source=l.trace(W['V']);sg=l.literal_geometry(W['V']);assert pair<=set(map(tuple,sg['outputs']))and source['last'][r]==('R',4)and source['last'][A]==('R',11)
old=chord('V',(0,0,0));roles=[]
for tag in sorted(pair):
 for a in'DCVU':
  geo=l.literal_geometry(W[a]);tr=l.trace(W[a]+l.M)
  for ii,slot in enumerate(map(tuple,geo['inputs'])):
   for hd in range(4):
    p=(*sub(tag,l.rot(slot,hd)),hd);rec=dict(SAME_lost_pair_identity_cell=tag,consumer_RAW=a,input_index0=ii,input_slot=slot,consumer_pose=p,actual_input_first_read=o.describe(a,tr['first'][slot][1]))
    if(sum(p[:2])+hd)%2:rec['classification']='unreachable_sector'
    else:
     bad=[]
     for held in sorted(pair):
      loc=l.rot(sub(held,p[:2]),-hd);f=tr['first'].get(loc)
      if loc in l.K or f and f[0]=='R':bad.append(dict(SAME_pair_cell=held,local=loc,reason='CURRENT_in_entry_CORE'if loc in l.K else'SAME_BLACK_vs_first_WHITE',first=f))
     if bad:rec.update(classification='initial_SAME_pair_CORE_or_WHITE_conflict',conflicts=bad)
     else:
      h=contact(*old,*chord(a,p));assert p!=(1,3,0)
      if h:rec.update(classification='actual_nonadjacent_source_V_proxy_contact',contact=h)
      else:rec['classification']='noncontact_A_loss_gate'
    roles.append(rec)
assert len(roles)==64 and Counter(q['classification']for q in roles)=={'unreachable_sector':32,'initial_SAME_pair_CORE_or_WHITE_conflict':18,'actual_nonadjacent_source_V_proxy_contact':12,'noncontact_A_loss_gate':2}
gates=[q for q in roles if q['classification']=='noncontact_A_loss_gate'];assert {(q['consumer_RAW'],tuple(q['consumer_pose']))for q in gates}=={('V',(0,4,2)),('U',(-1,5,2))}and all(q['SAME_lost_pair_identity_cell']==A for q in gates)
# Exact protected half-edge closure and both source/consumer interfaces.
P=(0,2);WW=(-1,3);L=(1,1);assert set(edge(A))=={WW,L};assert contact(*old,WW,L)==dict(old_s='1/2',new_t='1/2',point=['0','2'])
assert contact(P,old[1],WW,P)==dict(old_s='0',new_t='1',point=['0','2'])
interfaces=[];coneU=[]
for g in gates:
 a=g['consumer_RAW'];p=tuple(g['consumer_pose']);ep=after(W[a],p);assert ep==(-1,1,2)and z(ep)==WW;h=contact(*chord(a,p),WW,P);assert h and h['old_s']=='1'and h['new_t']=='0';tr=l.trace(W[a]+l.M);loc=l.rot(sub(A,p[:2]),2);assert loc not in l.trace(W[a])['first']and tr['first'][loc]==('L',len(W[a])+1);assert A in {add(ep[:2],l.rot(q,2))for q in l.K}
 beta_coeff=0 if a=='V'else 1
 interfaces.append(dict(consumer=a,pose=p,actual_RAW_EXIT=ep,corrected_EXIT=WW,SAME_A_actual_input_local=loc,actual_A_physical_L_owner=o.describe(a,len(W[a])+1),SAME_A_physically_alive_into_EXIT_CORE=True,source_partial_chord_only_bridge_contact=contact(P,old[1],WW,P),consumer_only_bridge_contact=h,angle_symbol_beta='atan(1/3)',ordinary_open_turn=dict(K_pi_over2_coefficient=1,beta_coefficient=beta_coeff),closing_at_W_then_P=dict(pi_coefficient=1,beta_coefficient=-beta_coeff),exact_total_turn='(K+2)*pi/2',Jordan_nonnegative_K_solutions=[2],bridge='SAME_CURRENT A edge half W(-1,3) to P(0,2), not a ghost connector',source_R_birth_tick0=11))
 # Generalize signed V endpoint cone to the upper-U helper, whose finalRAW
 # can have new writes in CORE. All actual reads still have y>=1.
 pose=(0,0,0)
 for t,c in enumerate(W[a]):
  q=pose[:2];glob=add(p[:2],l.rot(q,2));assert glob[1]>=1;coneU.append(dict(helper=a,tick0=t,read_number1=t+1,local=q,actual_helper_cell=glob));pose=after(c,pose)
# Same completed S-run EXIT support, now helper heady is four or five.
Ssupport=[]
for htag,heady in(('V',4),('U',5)):
 for a in'DVU':
  ep=after(W[a]);pose=(0,0,0)
  for t,c in enumerate(W[a]):
   lb=heady+ep[1]-pose[1];assert lb>=heady;Ssupport.append(dict(helper=htag,actual_preceding_RAW=a,tick0=t,minimum_cell_y_from_completed_S_EXIT_at_least_helper_y=lb));pose=after(c,pose)
CP=R/'postforeign_V_twoC_cleanup_cone_2026-10-24/cleanup_cone.json';cone=json.loads(CP.read_text());ports=cone['all21_terminal_guard_obligations'];assert len(ports)==21 and all(q['actual_first_V_chart_guard'][1]<=0 for q in ports)
for a,p in(('V',(0,4,2)),('U',(-1,5,2))):assert after(W[a],p)==(-1,1,2)
paths=[CP,R/'postforeign_V_twoC_cleanup_cone_2026-10-24/manifest.json',R/'audits/check_twoC_cleanup_cone_independent.json',R/'first_foreign_VCCV_terminal_ports_2026-10-24/manifest.json',R/'audits/check_VCCV_terminal_ports_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_POSTFOREIGN_FIRST_V_SAME_rA_NONTERMINAL_GUARDIAN_PENDING_REVIEW',scope='Actual complete8 interval then FIRSTFOREIGN then immediateV. Follow only ordinary RAW atoms. At any actual cut with executed proxy SIMPLE through that cut and an immediate next completeG7 RAW+actualM11, SAME firstV r/A are CURRENT outsideCORE. In particular they hold at ENTRY of a global-FIRST-contact atom if that complete next atom exists. No persistence through contact or arbitrary-tail simplicity.',fresh_plain_RAW_current_edge_barrier=barriers,SAME_first_V_pair_R_births=[dict(cell=r,tick0=4),dict(cell=A,tick0=11)],all64_plain_earliest_CURRENT_loss_roles=roles,both_exact_half_edge_Jordan_interfaces=interfaces,Jordan_statement='If the first pair-CURRENT-loss RAW completes while the executed proxy is still SIMPLE, it must be one of the two A gates. SAME A edge remains current until its endpoint CORE capture. Its half-edge closes the simple future subarc from sourceV midpointP to common EXITW; finite source/consumer interfaces touch bridge only at P/W. There is NO foreign between birth and loss. Exact ordinary lift plus closing turns gives(K+2)pi/2, so Jordan forces K2, not a postFOREIGN age law.',all46_helper_V_U_actual_RAW_support_records=coneU,all112_preceding_S_RAW_support_records=Ssupport,all21_inherited_common_EXIT_terminal_port_obligations=ports,terminal_cone_extension='For helperU(-1,5,S), preceding completed S atoms have EXITy>=5, hence RAWy>=5, and finalU RAWy>=1. N/W/C bounds are the signed V cone. SAME negative guards and mandatory U-before-firstB hole are unchanged; finalA is marker-only aliveCORE. Common helper EXIT is exactly the same as helperV, so all21 actual next contexts conflict.',proof_by_earliest_loss='Choose earliest loss before the stipulated simple cut. All CORE captures/recycled cells are included by actual I masks, and simultaneous pair inputs were not discarded. Loss must A->V/U atK2. Its helper EXIT has no possible next complete seven-atom RAW+actualM11. This contradicts the stipulated immediate next completed atom (or an already completed intervening ordinary word). Therefore no such earlier loss exists. The pair can erode in a finite terminal history, as the genuine UQ/UB controls demonstrate.',physical_and_CORE_qualifier='CURRENT loss is at RAW EXIT CORE absorption if marker-only. SAME A remains physically alive until the next actual word tick1/read2; the theorem does not call it dead at absorption. Real R repairs inside CORE are included by the RAW cones, not discarded as nonoutputs.',no_preFOREIGN_maturity_afterFOREIGN_or_cyclic_induction=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'rA_guardian.json').write_text(json.dumps(out,indent=2)+'\n');print('FirstpostFOREIGN V SAME r/A:64 earliest-loss roles=32sector+18field+12 sourcecontacts+2 A gates. Protected A half-edge gives K2. Both helperV/U common EXIT are terminal by all-length cones; pair CURRENT at every simple nonterminal cut. No arbitrary-tail simplicity.')
