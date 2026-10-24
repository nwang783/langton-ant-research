"""Exact physical port restoration obstructions, not arbitrary-tail simplicity."""
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
def raw(tokens):return ''.join(W[a]for a in tokens)
def after(word,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if not den:return None
 s,t=Q(det(q,v),den),Q(det(q,u),den)
 return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None

def owner(tokens,t):
 n=0
 for i,a in enumerate(tokens):
  if t<n+len(W[a]):return dict(actual_atom_index0=i,atom=a,canonical=o.describe(a,t-n))
  n+=len(W[a])
 return dict(atom='actual next word',tick0=t-n,read_number1=t-n+1,turn=l.M[t-n])
# A physical atomic EXIT port at every real boundary, no residual maturity.
beta=(1,-1);exitfacts=[]
for a in'DCVUFQB':
 tr=l.trace(W[a]);ep=after(W[a]);cell=add(ep[:2],l.rot(beta,ep[2]));assert tr['last'][cell]==('R',len(W[a])-2);assert cell not in {add(ep[:2],l.rot(q,ep[2]))for q in l.K}
 exitfacts.append(dict(actual_previous_atom=a,EXIT_pose=ep,physical_beta_slot_in_previous_chart=cell,SAME_last_R_birth_tick0=len(W[a])-2,birth_read_number1=len(W[a])-1,following_entry_local=beta,outside_active_core=True,BLACK_at_next_RAW_entry=True,no_age_law_or_full_G8_assumption=True))
T='DCVCCVV';tr=l.trace(raw(T)+l.M);assert tr['feasible']and tr['first'][beta]==('R',98);g=l.literal_geometry(W['D']);assert after(raw(T))==(3,0,1)
queries=[]
for a in'DCVUFQB':
 q=l.trace(raw(a+T)+l.M);assert not q['feasible'];queries.append(dict(previous_atom=a,literal=q))
# A complete nine-black prepared loop control. Incoming beta is WHITE here,
# exactly the boundary condition that no real immediately previous atom permits.
seed={p for p,(c,t)in tr['first'].items()if c=='L'};assert len(seed)==9 and beta not in seed;B=set(seed);reads=[];pose=(0,0,0)
for t,c in enumerate(raw(T)+l.M):
 p=pose[:2];assert(p in B)==(c=='L');B.symmetric_difference_update({p});reads.append(dict(tick0=t,read_number1=t+1,cell=p,turn=c,actual_owner=owner(T,t)));pose=after(c,pose)
oldC=chord('C',after(W['D']));lastV=chord('V',after(raw(T[:-1])));contact=hit(*oldC,*lastV);assert contact==dict(old_s='1/2',new_t='1/2',point=['2','2'])
loop=dict(tokens=T,complete_seed=sorted(seed),all_other_initial_cells_WHITE=True,initial_black_mass=9,all_RAW_plus_actual_M11_reads=reads,incoming_beta_initially_WHITE=True,incoming_beta_first_read=dict(tick0=98,read_number1=99,turn='R',physical_owner=owner(T,98)),actual_proxy_recontact=contact,outgoing_old_source='own C of initial DC, not its creating D',all7_real_atomic_predecessors_impossible=queries,necessary_boundary_rewrite='A genuine predecessor leaves SAME beta BLACK at this boundary. To attain this exact loop after any previous actual atom, an actual L removal of that beta is necessary before its R98 read. The displayed word has no earlier beta read, hence cannot attain that repair. An R into CORE at another cell is not a beta removal.')
# Genuine UQ/UB positive regressions from the signed erosion controls. Their
# next-U attempt has a concrete old CORE hole, even though old output A dies.
controls=[]
for A in'QB':
 prefix='U'+A+'VCCV';attempt=prefix+'U';pt=l.trace(raw(prefix)+l.M);qt=l.trace(raw(attempt)+l.M);assert pt['feasible']and not qt['feasible'];starts=[];pose=(0,0,0);n=0
 for a in attempt:starts.append((n,pose));n+=len(W[a]);pose=after(W[a],pose)
 vi=2;vstart,vpose=starts[vi];fourth_start,fourth_pose=starts[5];next_start,next_pose=starts[6];hole=add(vpose[:2],l.rot((-1,-1),vpose[2]));originalA=add(vpose[:2],l.rot((0,1),vpose[2]));assert qt['conflict_read']==next_start+12 and qt['previous_read']==vstart+2 and tuple(qt['cell'])==hole and qt['turn']=='L';assert l.trace(raw('VCCV'))['last'][(-1,-1)]==('L',2)
 assert l.rot(sub(hole,next_pose[:2]),-next_pose[2])==(0,2);assert l.trace(W['U']+l.M)['first'][(0,2)]==('L',12)
 cutbody=raw(attempt)[:qt['conflict_read']];ct=l.trace(cutbody);assert ct['feasible'];seed={p for p,(c,t)in ct['first'].items()if c=='L'};B=set(seed);labels={p:('initial',None)for p in seed};pose=(0,0,0);rr=[];snaps={};birth=vstart+11;death=next_start+1
 for t,c in enumerate(cutbody):
  p=pose[:2];assert(p in B)==(c=='L');prior=labels.get(p)
  if c=='L':B.remove(p);labels.pop(p)
  else:B.add(p);labels[p]=('R',t)
  if t==birth:assert p==originalA and c=='R'
  if t==death:assert p==originalA and c=='L'and prior==('R',birth)
  rr.append(dict(tick0=t,read_number1=t+1,cell=p,turn=c,before_identity=prior,after_identity=labels.get(p),actual_owner=owner(attempt,t)));pose=after(c,pose)
  if t+1 in(next_start,death+1,len(cutbody)):
   K={add(pose[:2],l.rot(q,pose[2]))for q in l.K};snaps[str(t+1)]=dict(cut_before_tick0=t+1,head=pose[:2],heading=pose[2],original_A_physically_alive=labels.get(originalA)==('R',birth),original_A_CORE=originalA in K,original_A_CURRENT=labels.get(originalA)==('R',birth)and originalA not in K,hole_WHITE=hole not in B)
 assert snaps[str(next_start)]['original_A_physically_alive']and snaps[str(next_start)]['original_A_CORE'];assert not snaps[str(death+1)]['original_A_physically_alive']and hole not in B
 assert pose[:2]==hole and cutbody==raw(attempt)[:next_start+12]
 # The actual physical ant reads WHITE here and takes R, not the intended U's L.
 divergent_actual_pose=after('R',pose);assert hit(*chord('V',(0,0,0)),*chord('U',(-1,1,2)))==dict(old_s='0',new_t='1/2',point=['-1','-1'])
 controls.append(dict(genuine_U_entry_prefix=prefix,positive_complete_RAW_plus_M11_literal=True,selected_first_returned_V_pose=vpose,selected_V_hole_cell=hole,hole_actual_L_deletion_tick0=vstart+2,hole_deletion_read_number1=vstart+3,selected_V_original_A_cell=originalA,original_A_R_birth_tick0=birth,original_A_physical_death_tick0=death,original_A_death_owner=owner(attempt,death),attempted_next_word='U',attempt_U_old_source_proxy_contact=dict(old_s='0',new_t='1/2',point=['-1','-1']),complete_finite_seed_for_actual_valid_partial_run=sorted(seed),all_other_initial_cells_WHITE=True,executed_actual_fine_reads_before_divergence=rr,exact_physical_snapshots=snaps,intended_U_first_failure=qt,actual_next_turn='R',actual_next_pose=divergent_actual_pose,necessary_restoration='Any modified history retaining this marked next-U target must actually restore hole BLACK before U tick12/read13. The SAME old A output can be dead already; its erosion does not restore the source entry-core hole. Repairs inside active K count as real R writes and are not excluded by this statement.',no_complete_U_or_actual_U_proxy_claim=True))
# Arbitrary zero-C S rail after VCCV: D/V strictly lower x; U keeps it.
# The old V segment occupies x in[-1,1]; run starts corrected(-1,3).
# Before any D/V, immediate U is the sole possible contact with that old V.
# Its deleted-hole conflict above blocks it. Once D/V occurs, every later
# S corrected point is strictly x<-1, forever disjoint from that old segment.
railfacts=[]
for a in'DVU':
 ep=after(W[a],(-1,1,2));seg=chord(a,(-1,1,2));railfacts.append(dict(actual_zero_C_S_atom=a,entry=(-1,1,2),exit=ep,corrected_segment=seg,old_V_contact=hit(*chord('V',(0,0,0)),*seg)))
assert railfacts[0]['old_V_contact']is None and railfacts[1]['old_V_contact']is None and railfacts[2]['old_V_contact']['new_t']=='1/2'
paths=[R/'postforeign_first_source_three_atom_transfer_2026-10-24/manifest.json',R/'audits/third_source_transfer_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_POSTFOREIGN_EROSION_RETURN_PORT_RESTORATION_PENDING_REVIEW',scope='Exact physical incoming beta and deleted CORE-hole obstructions for prescribed proper proxy recontacts. Genuine UQ/UB erosion regressions retained. Not arbitrary-tail simplicity, not a global no-return theorem and no postforeign maturity.',all7_atomic_real_EXIT_beta_birth_facts=exitfacts,complete9_black_prepared_loop_and_boundary_obstruction=loop,two_genuine_U_entry_output_erosion_but_hole_not_restored_controls=controls,all3_zero_C_S_rail_generator_facts=railfacts,portable_zero_C_lane_conclusion='For any actual ordinary zero-C S run immediately after a V,C,C,V pattern, a FIRST contact with that first V segment can only be its immediate U. D/V move strictly left of the whole old V chord and subsequent zero-C motion cannot return. Immediate U is impossible because V L2 deleted its required input (0,2) cell and C,C,V never reread it. This excludes only this old-V/zero-C lane, not other proxy sources or any later C turn.',CORE_rule='CURRENT-to-CORE is not physical death. Actual next-word R/L writes inside CORE are fully included in restoration/removal obligations; no output-only origin enumeration is claimed.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'return_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('Seven actual EXIT beta R births; nine-black DCVCCVV recontact cannot follow any real atom. Genuine UQ/UB VCCV A erodes, but next-U recontact needs actual repair of V L2-deleted CORE hole. Arbitrary zero-C S rail lane closed, no arbitrary-tail simplicity.')
