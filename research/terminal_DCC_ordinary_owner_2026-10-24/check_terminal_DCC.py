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
T=['D','C','C'];TAIL=''.join(W[a]for a in T);assert len(TAIL)==40

def owner_tail(t):
 off=0
 for i,a in enumerate(T):
  if t<off+len(W[a]):return dict(actual_tail_RAW_index0=i,actual_RAW=a,actual_C_ordinal_after_last_D=i if i else None,RAW_tick0=t-off,RAW_read_number1=t-off+1,canonical_RAW_ownership=o.describe(a,t-off),terminal_C2_not_a_retained_G8_C2=i==2)
  off+=len(W[a])
 return dict(actual_marker_after_terminal_C2_tick0=t-off,actual_marker_read_number1=t-off+1,next_completed_G7_RAW_NOT_assumed=True)
# Universe comes from the signed arbitrary ordinary SOURCE window, not
# from a theorem that incorrectly calls the terminal C2 a G8 packet.
win=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];V={'D':(1,1),'C':(1,1),'V':(1,3),'U':(0,4)};CC=(F(-1,2),F(-1,2));geo=[]
for src,u in V.items():
 Ks=next(r['allowed_C_counts_before_contact_ENTRY']for r in win if r['source_class']=='postFOREIGN_ordinary'and r['source_atom']==src and r['contact_atom']=='C')
 for K in Ks:
  h=(-K)%4;v=l.rot((1,1),h);cor=sub(CC,l.rot(CC,h));corn=[add(cor,(s*u[0]-t*v[0],s*u[1]-t*v[1]))for s in(0,1)for t in(0,1)]
  for x in range(ceil(min(p[0]for p in corn)),floor(max(p[0]for p in corn))+1):
   for y in range(ceil(min(p[1]for p in corn)),floor(max(p[1]for p in corn))+1):
    if(x+y+h)%2:continue
    w=sub(add((x,y),l.rot(CC,h)),CC);de=det(u,v)
    if de:
     s,t=F(det(w,v),de),F(det(w,u),de)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if det(w,u):continue
     k=0 if v[0]else 1;s=F(0);t=F(-w[k],v[k])
     if not(0<t<=1 and add(w,(t*v[0],t*v[1]))==(0,0)):continue
    c2=(x,y,h);hp=(h+1)%4;p=(*sub(c2[:2],l.rot((1,2),hp)),hp);c1=after(W['D'],p);assert after(W['C'],c1)==c2
    geo.append(dict(source_RAW=src,SOURCE_ENTRY_to_terminal_C2_ENTRY_C_clock=K,terminal_C2_ENTRY=c2,old_source_parameter=str(s),new_C2_parameter=str(t),actual_last_D_ENTRY=p,actual_C1_ENTRY=c1,last_D_ENTRY_C_clock=K-1,actual_source_D_contact_with_last_D=contact(*chord(src,(0,0,0)),*chord('D',p)),actual_source_contact_with_C1=contact(*chord(src,(0,0,0)),*chord('C',c1))))
assert len(geo)==20
old=json.loads((R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json').read_text())['all129_canonical_first_contact_cases'];assert{(r['source_RAW'],r['SOURCE_ENTRY_to_terminal_C2_ENTRY_C_clock'],tuple(r['terminal_C2_ENTRY']),r['old_source_parameter'],r['new_C2_parameter'])for r in geo}=={(r['earlier_atom'],r['entry_C_gap'],tuple(r['later_pose']),r['earlier_parameter'],r['later_parameter'])for r in old if r['later_atom']=='C'}
# Seven genuine preceding RAW penultimate-R births. D/C source itself
# misses beta, and beta is outside its RAW EXIT core.
beta=(1,-1);M=(2,0);birth=[]
for a in'DCVUFQB':
 ep=after(W[a]);cell=add(ep[:2],l.rot(beta,ep[2]));tr=l.trace(W[a]);assert tr['last'][cell]==('R',len(W[a])-2)and list(cell)in l.literal_geometry(W[a])['outputs']
 birth.append(dict(actual_previous_RAW=a,actual_RAW_EXIT=ep,actual_beta_cell=cell,last_R_tick0=len(W[a])-2,last_R_read_number1=len(W[a])-1,genuine_external_output=True))
for src in'DC':
 ep=after(W[src]);assert beta not in l.trace(W[src]+l.M)['first']and rel(beta,ep)not in l.K
# Ordinary D/C-source beta needs to survive only to the REAL last-D ENTRY,
# not through a fictitious completed DCC or beyond the terminal RAW.
betarows=[];bclosures=[]
for g in geo:
 src=g['source_RAW'];K=g['SOURCE_ENTRY_to_terminal_C2_ENTRY_C_clock'];P=tuple(g['actual_last_D_ENTRY'])
 if src not in'DC':continue
 assert(K,tuple(g['terminal_C2_ENTRY']))in{(3,(-1,0,1)),(4,(-1,-1,0)),(5,(0,-1,3))}
 rows=[]
 for n in range(K):
  h=(-n)%4
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for slot,(c,t)in tr['first'].items():
    if c!='L'or slot in l.K:continue
    p=(*sub(beta,l.rot(slot,h)),h);ep=after(W[a],p);r=dict(source_RAW=src,candidate_K=K,actual_last_D_ENTRY=P,consumer=a,consumer_ENTRY_C_clock=n,pose=p,input=slot,owner=o.describe(a,t),RAW_EXIT=ep)
    if(sum(p[:2])+h)%2:why='sector'
    elif src=='C'and n==0:why='before_actual_SOURCE_C_RAW_completion_at1'
    elif n==0:
     assert p[1]<1;why='N0_head_below_actual_SOURCE_D_EXIT_y1'
    elif n==1:
     assert p[1]<1;why='W1_head_below_SOURCE_C_y1_or_SOURCE_D_y2'
    elif n==2:
     if src=='C':
      assert a=='U'and p[0]>=0;why='SOURCE_C_S2_heads_x_le_minus1_but_beta_ports_x_ge0'
     else:
      co=contact(*chord('D',(0,0,0)),*chord(a,p))
      if co:assert a=='U'and p==(0,0,2);r['actual_source_contact']=co;why='earlier_nonadjacent_SOURCE_D_EXIT_ENTRY_repeat'
      else:
       assert a=='U'and p==(1,1,2)and rel(M,p)in[tuple(q)for q in l.literal_geometry(W[a])['inputs']];why='fresh_SOURCE_D_common_minimum3_in_actual_BASE_ending_G8_factor'
    elif n==3:
     co=contact(*chord(src,(0,0,0)),*chord(a,p))
     if co:r['actual_source_contact']=co;why='earlier_actual_SOURCE_chord_contact'
     elif K==4:
      assert ep[0]>=1>P[0];why='zeroC_E_after_loss_cannot_reach_last_D_x_minus3'
     else:
      assert K==5 and ep[0]>=1 and P[0]==-1;why='remaining_E_to_N_C_adds_x1_then_N_cannot_reach_last_D_x_minus1'
    else:
     assert n==4 and K==5 and ep[0]>=1>P[0];why='N4_loss_RAW_exit_x_ge1_cannot_reach_last_D_x_minus1'
    r['route']=why;rows.append(r)
 assert len(rows)==8*K;betarows+=rows
 local=rel(beta,P);f=l.trace(TAIL+l.M)['first'][local];assert f[0]=='R'and f[1]in{3:38,4:33,5:16}.values()and f[1]<len(TAIL)
 assert f[1]=={3:38,4:33,5:16}[K]
 bclosures.append(dict(geometry=g,SAME_beta_CURRENT_at_real_last_D_ENTRY=True,last_D_local_beta=local,first_physical_beta_request_in_actual_DCC_tail=f,actual_tail_owner=owner_tail(f[1]),FIRST_WHITE_contradicts_original_BLACK_without_any_earlier_tail_read=True,no_claim_beta_CURRENT_after_the_contact_or_after_an_infeasible_tail=True))
assert len(betarows)==192 and len(bclosures)==6
# U sources: signed all-ordinary-RAW SAME STAR supplies CURRENT at exact
# C2 ENTRY (actual preceding C1 has real C2 marker; no next G7 afterC2).
STAR={(0,0),(0,1),(1,0),(1,1)};ust=[]
for g in geo:
 if g['source_RAW']!='U':continue
 bad=conflict('C',tuple(g['terminal_C2_ENTRY']),STAR);assert bad and any(b['role']=='ENTRY_CORE'or b['actual_first'][1]<len(W['C'])for b in bad)
 ust.append(dict(geometry=g,SAME_U_STAR_CURRENT_at_actual_terminal_C2_ENTRY=True,actual_CORE_or_first_WHITE_conflicts=bad,source_FOREIGN_before_fresh_U_is_outside_its_guard_interval=True,no_FOREIGN_after_fresh_U=True))
assert len(ust)==8
# V sources: min5 is enough at lastBASE clocks3/4; atclock5 only exact
# first-loss gates ending0,1,W can occur, unable to reach real lastD2,-1,W.
vr=json.loads((R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/fresh_r.json').read_text());gates=vr['all3_marker_loss_Jordan_interfaces'];assert len(gates)==3 and all(tuple(r['actual_RAW_EXIT'])==(0,1,3)for r in gates)
vc=[]
for g in geo:
 if g['source_RAW']!='V'or g['actual_source_D_contact_with_last_D']or g['actual_source_contact_with_C1']:continue
 K=g['SOURCE_ENTRY_to_terminal_C2_ENTRY_C_clock'];P=tuple(g['actual_last_D_ENTRY']);assert K in(4,5,6)
 if K<6:route='fresh_RAW_V_r_min5_excludes_all_BASE_losses_before_last_D_at3_or4'
 else:
  assert P==(2,-1,3)
  for loss in gates:
   ep=tuple(loss['actual_RAW_EXIT']);assert ep[0]<P[0]and ep[1]>P[1]
  route='any_first_r_loss_is_exact5_and_its_W_RAW_exit0,1_cannot_reach_last_D2,-1_with_zeroC'
 loc=rel((0,0),P);f=l.trace(TAIL+l.M)['first'][loc];assert f[0]=='R'and f[1]=={4:31,5:22,6:21}[K]
 vc.append(dict(geometry=g,actual_r_current_before_last_D_route=route,SAME_r=(0,0),last_D_local_r=loc,actual_tail_first_WHITE=f,actual_tail_owner=owner_tail(f[1]),all3_possible_exact_K5_loss_interfaces=gates if K==6 else None,original_r_aliveCORE_after_an_earlier_loss_is_NOT_mistaken_for_CURRENT=True))
assert len(vc)==3
# Exact disjoint20 source ledger, geometric precursor contacts first.
ledger=[]
for g in geo:
 src=g['source_RAW'];co=g['actual_source_D_contact_with_last_D']or g['actual_source_contact_with_C1']
 if co:
  assert g['last_D_ENTRY_C_clock']>=2;r='earlier_actual_last_D_or_C1_contact_already_breaks_GLOBAL_first_prefix';proof={'earlier_D_contact':g['actual_source_D_contact_with_last_D'],'earlier_C1_contact':g['actual_source_contact_with_C1'],'not_legitimate_source_adjacency':'Atleast2 actualCs separate sourceENTRY from lastD; an old end/new entry repeat is already a nonadjacent return at the previous incoming RAW endpoint.'}
 elif src=='U':r='SAME_fresh_U_STAR_CURRENT_before_terminal_C2';proof=next(x for x in ust if x['geometry']==g)
 elif src in'DC':r='genuine_preceding_beta_FIRST_WHITE_in_real_DCC_tail';proof=next(x for x in bclosures if x['geometry']==g)
 else:r='fresh_V_r_FIRST_WHITE_in_real_DCC_tail';proof=next(x for x in vc if x['geometry']==g)
 ledger.append(dict(geometry=g,route=r,proof=proof))
assert Counter(r['route']for r in ledger)=={'earlier_actual_last_D_or_C1_contact_already_breaks_GLOBAL_first_prefix':6,'SAME_fresh_U_STAR_CURRENT_before_terminal_C2':5,'genuine_preceding_beta_FIRST_WHITE_in_real_DCC_tail':6,'fresh_V_r_FIRST_WHITE_in_real_DCC_tail':3}
# The finalD/C1 own local geometry is adjacent-only; no missing source
# with gap0/1 is called a new contact by the20-row window.
local=dict(vertices=[chord('D',(0,0,0))[0],chord('D',(0,0,0))[1],chord('C',(1,1,0))[1],chord('C',(1,2,3))[1]],old_last_D_vs_C2=contact(*chord('D',(0,0,0)),*chord('C',(1,2,3))),old_C1_vs_C2=contact(*chord('C',(1,1,0)),*chord('C',(1,2,3))))
assert local['old_last_D_vs_C2']is None and local['old_C1_vs_C2']=={'old_s':'1','new_t':'0'}
# Actual positive terminal words; complete whole boards and repaired proxy
# (M11 fine reads NOT appended as a fictitious complete next G7 atom).
def proxy(word):
 p=(0,0,0);out=[]
 for i,a in enumerate(word):
  cuts=[p]
  if a in'QB':cuts.append(after(W['F'],p))
  ep=after(W[a],p);cuts.append(ep)
  for j,(u,v)in enumerate(zip(cuts,cuts[1:])):out.append(dict(atom_index0=i,atom=a,piece_index0=j,start=z(u),end=z(v)))
  p=ep
 return out
reg=[]
for word in['UDCC','UQUDCC']:
 raw=''.join(W[a]for a in word);t=l.trace(raw+l.M);assert t['feasible'];seed={q for q,(c,k)in t['first'].items()if c=='L'};B=set(seed);p=(0,0,0);reads=[]
 for tick,c in enumerate(raw+l.M):
  assert(p[:2]in B)==(c=='L');reads.append(dict(tick0=tick,read_number1=tick+1,cell=p[:2],turn=c))
  if c=='L':B.remove(p[:2])
  else:B.add(p[:2])
  p=after(c,p)
 pp=proxy(word);contacts=[]
 for i,u in enumerate(pp):
  for j in range(i+1,len(pp)):
   v=pp[j];co=contact(tuple(u['start']),tuple(u['end']),tuple(v['start']),tuple(v['end']))
   if not co:continue
   if j==i+1:
    assert u['end']==v['start']and(co=={'old_s':'1','new_t':'0'}or co.get('collinear_old_interval')==['1','1'])
   else:contacts.append(dict(old_piece=i,new_piece=j,intersection=co))
 assert not contacts;reg.append(dict(word=word,complete_black_seed=sorted(seed),all_RAW_plus_given_M11_physical_reads=reads,proxy_pieces=pp,repaired_proxy_simple=True,all_nonadjacent_contacts=contacts,proxy_stops_last_RAW_and_does_NOT_append_marker_D_as_valid_G7=True,terminal_DCC_real_and_NOT_excluded=True))
# Exact marker boundary, not an extra completed word assumption.
given=l.trace(TAIL+l.M);assert given['feasible']and len(TAIL+l.M)==51;ep=after(TAIL+l.M);assert ep[:2]==(0,1)and given['last'][(0,1)]==('L',11)
nextD=l.trace(TAIL+W['D']+l.M);assert not nextD['feasible']and nextD['conflict_read']==51 and nextD['previous_read']==11
marker=dict(actual_known_tail= 'DCC+M11',actual_fine_read_count=51,given_marker_contains_D10_body_plus_only_one_following_L=True,head_at_first_ungiven_read=ep,known_cell_last_L=given['last'][(0,1)],forced_actual_next_fine_turn='R',attempted_next_D_plus_M11_conflict=nextD,next_completed_G7_NOT_ASSUMED=True,not_used_to_exclude_the_terminal_C2=True)
D=[R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/02_U_entry_center_simplicity.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json',R/'audits/check_RAW_G8_base_cut_bridge_independent.json',R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24/U_star_RAW_lift_manifest.json',R/'audits/check_fresh_U_star_RAW_lift_independent.json',R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/manifest.json',R/'audits/check_fresh_RAW_donors_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json'];assert all(p.exists()for p in D)
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual U-entry G8 prefix,FIRSTF/Q/B,ordinary-only RAW suffix with an actual terminal DCC and given actual finalM11. If GLOBAL first new proxy contact occurs in terminal secondC, its outgoing old owner cannot be ANY postFOREIGN ordinary D/C/V/U, including a leadingC. Original FOREIGN/preFOREIGN owners remain separate; no next completedG7 assumption.',all20_exact_ordinary_source_terminal_C2_geometry_rows=geo,all7_genuine_previous_RAW_beta_births=birth,all192_D_C_source_beta_first_loss_before_actual_last_D_roles=betarows,all6_D_C_source_actual_tail_FIRST_WHITE_beta_guards=bclosures,all8_U_source_STAR_entry_guards=ust,all3_V_source_actual_tail_FIRST_WHITE_r_guards=vc,all20_disjoint_source_owner_exclusions=ledger,actual_lastD_C1_C2_local_adjacent_only_geometry=local,all2_actual_prepared_positive_terminal_words=reg,actual_given_marker_boundary=marker,no_fictitious_completed_terminal_DCC_G8_packet=True,no_completed_next_G7_assumption=True,real_UDCC_and_UQUDCC_controls_preserved=True,no_preFOREIGN_or_original_FOREIGN_owner_closure_or_arbitrary_tail_simplicity=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'terminal_DCC.json').write_text(json.dumps(out,indent=2)+'\n');print('TerminalDCC ordinaryowner20 closed:6 earlierprecursor+5 USTAR+6 beta tailWHITE+3 Vr tailWHITE. UDCC/UQUDCC complete simple positives retained; no nextG7.')
