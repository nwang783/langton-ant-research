"""Exact terminal complete-marker interface of firstFOREIGN,V,C,C,V.
No general erosion terminality, age law afterFOREIGN or arbitrary-tail simplicity.
"""
from pathlib import Path
from fractions import Fraction as Q
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
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None

def owner(T,t):
 n=0
 for i,a in enumerate(T):
  if t<n+len(W[a]):return dict(actual_atom_index0=i,atom=a,canonical=o.describe(a,t-n))
  n+=len(W[a])
 return dict(atom='actual next word',tick0=t-n,read_number1=t-n+1,turn=l.M[t-n])
fields=[];rows=[]
for A in'FQB':
 prefix=A+'VCCV';pt=l.trace(raw(prefix));assert pt['feasible']and l.trace(raw(prefix)+l.M)['feasible'];vp=after(W[A]);holes=[]
 for q,t in(((-1,0),1),((-1,-1),2)):
  cell=add(vp[:2],l.rot(q,vp[2]));assert pt['last'][cell]==('L',len(W[A])+t);holes.append(dict(first_V_chart_cell=q,physical_cell=cell,actual_V_L_deletion_tick0=len(W[A])+t,deletion_read_number1=len(W[A])+t+1,physically_WHITE_at_next_atom_entry=True))
 A_cell=add(vp[:2],l.rot((0,1),vp[2]));ep=after(raw(prefix));K={add(ep[:2],l.rot(q,ep[2]))for q in l.K};assert pt['last'][A_cell]==('R',len(W[A])+11)and A_cell in K
 fields.append(dict(foreign=A,first_returned_V_pose=vp,next_atom_entry=ep,old_CORE_holes=holes,first_V_original_A_cell=A_cell,SAME_A_physically_alive_CORE_at_next_RAW_entry=True,A_not_current_residual_at_this_cut=True))
 for nxt in'DCVUFQB':
  T=prefix+nxt;tr=l.trace(raw(T)+l.M);rec=dict(foreign=A,next_atom=nxt,tokens=T,feasible=tr['feasible'])
  if tr['feasible']:assert(A,nxt)==('B','V');rec['classification']='prepared_B_V_escape_requires_actual_preFOREIGN_history'
  else:
   p,t=tuple(tr['cell']),tr['conflict_read'];old=tr['previous_read'];rec.update(literal_conflict=tr,required_read_owner=owner(T,t),actual_previous_read_owner=owner(T,old),physical_prior_turn=l.trace(raw(T)[:old+1])['last'][p][0])
   if nxt=='D':
    assert tr['turn']=='L'and old==len(W[A])+1;rec['classification']='first_V_L1_deleted_CORE_hole_vs_next_D_marker_L11';assert owner(T,t)['atom']=='actual next word'and owner(T,t)['tick0']==1
   elif nxt in'UFQB':
    assert tr['turn']=='L'and old==len(W[A])+2;rec['classification']='first_V_L2_deleted_CORE_hole_vs_next_own_RAW_L12';assert owner(T,t)['canonical']['context_tick0']==12
   else:
    assert tr['turn']=='R'and old<len(W[A]);rec['classification']='SAME_foreign_R_born_shadow_vs_actual_first_WHITE_demand';rec['SAME_foreign_original_R_tick0']=old;rec['actual_first_R_cell_in_postFOREIGN_chart']=l.rot(sub(p,vp[:2]),-vp[2])
  rows.append(rec)
assert len(rows)==21 and sum(r['feasible']for r in rows)==1
# Actual eight-to-FIRSTforeign restriction is a signed exact literal pair
# theorem. For B only plain U can immediately precede. All eight verified.
predecessors=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 tr=l.trace(raw(full+'B')+l.M);predecessors.append(dict(actual_full_G8=full,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
assert [r['actual_full_G8']for r in predecessors if r['feasible']]==['U']
T='UBVCCVV';tr=l.trace(raw(T)+l.M);assert not tr['feasible']and(tr['conflict_read'],tr['previous_read'],tuple(tr['cell']),tr['turn'])==(181,1,(-1,0),'L')
block=dict(mandatory_actual_preFOREIGN_full='U',tokens=T,literal_conflict=tr,old_U_ENTRY_CORE_hole=(-1,0),actual_U_L_deletion_tick0=1,deletion_read_number1=2,required_next_V_owner=owner(T,181),reason='The TRUE B->V escape would require BLACK at an earlier creating-U entry CORE cell physically deleted by U L1. No intervening read in the fixed UBVCCV prefix repairs it; complete old history cannot change the repeated-L conflict.',no_age_or_U_output_permanence_assumption=True)
# Prepared B escape shows that the true earlier source hypothesis matters.
T='BVCCVV';body=raw(T);tr=l.trace(body+l.M);assert tr['feasible'];seed={p for p,(c,t)in tr['first'].items()if c=='L'};B=set(seed);labels={p:('initial',None)for p in seed};pose=(0,0,0);g=(-2,-3);birth=67;death=len(body)+1;reads=[];snaps={}
for t,c in enumerate(body+l.M):
 p=pose[:2];assert(p in B)==(c=='L');old=labels.get(p)
 if c=='L':B.remove(p);labels.pop(p)
 else:B.add(p);labels[p]=('R',t)
 if t==birth:assert p==g and c=='R'
 if t==death:assert p==g and c=='L'and old==('R',birth)
 reads.append(dict(tick0=t,read_number1=t+1,cell=p,turn=c,before_identity=old,after_identity=labels.get(p),physical_owner=owner(T,t)));pose=after(c,pose)
 if t+1 in(len(body),death+1):
  K={add(pose[:2],l.rot(q,pose[2]))for q in l.K};snaps[str(t+1)]=dict(cut_before_tick0=t+1,pose=pose,SAME_B_R67_alive=labels.get(g)==('R',67),inside_active_core=g in K,CURRENT_same_B_R67=labels.get(g)==('R',67)and g not in K)
assert snaps[str(len(body))]['SAME_B_R67_alive']and snaps[str(len(body))]['inside_active_core'];assert not snaps[str(death+1)]['SAME_B_R67_alive']
pieces=[];pose=(0,0,0)
for i,a in enumerate(T):
 if a=='B':
  mid=after(W['F'],pose);pieces.append(dict(atom=i,label='B actualF56',a=z(pose),b=z(mid)));pieces.append(dict(atom=i,label='B actualtail',a=z(mid),b=z(after(W[a],pose))))
 else:pieces.append(dict(atom=i,label=a,a=z(pose),b=z(after(W[a],pose))))
 pose=after(W[a],pose)
checks=[]
for k,q in enumerate(pieces):
 for i,p in enumerate(pieces[:k]):
  h=contact(p['a'],p['b'],q['a'],q['b']);adj=bool(h and k==i+1 and p['b']==q['a']and(h.get('old_s')=='1'and h.get('new_t')=='0'or h.get('collinear_old_interval')==['1','1']));assert h is None or adj;checks.append(dict(old_piece=i,new_piece=k,contact=h,true_adjacent_join=adj))
escape=dict(tokens=T,complete_finite_seed=sorted(seed),all_other_initial_cells_WHITE=True,initial_black_mass=len(seed),all_RAW_plus_actual_M11_reads=reads,SAME_B_shadow_R67_cell=g,SAME_B_shadow_birth_tick0=birth,SAME_shadow_actual_physical_death_tick0=death,physical_death_owner=owner(T,death),exact_cut_snapshots=snaps,repaired_proxy_pieces=pieces,all_exact_piece_checks=checks,proxy_simple=True,genuine_U_entry_before_B=False,not_erosion_of_four_tag_B_hook=True)
paths=[R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'postforeign_first_source_three_atom_transfer_2026-10-24/manifest.json',R/'audits/third_source_transfer_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FIRST_FOREIGN_VCCV_TERMINAL_MARKED_INTERFACE_PENDING_REVIEW',scope='An actual complete-eight prefix then its FIRSTcompleteF/Q/B then V,C,C,V with actual nextM11 cannot extend by any NEXT complete seven-atom RAW+actualM11. Only this exact erosion morphology, not arbitrary erosion or arbitrary-tail simplicity. RAW-only completion is not called marked completion.',all3_actual_postFOREIGN_current_COLOR_CORE_fields=fields,all21_exact_next_seven_atom_cases=rows,all8_actual_G8_to_B_immediate_predecessor_queries=predecessors,unique_B_V_escape_killed_by_true_preFOREIGN_U=block,complete_prepared_B_shadow_erosion_regression=escape,conclusion='F/Q have no prepared next seven-atom marked continuation. B has one prepared V escape, but every actual firstB after a complete8 interval must immediately follow plainU, and UBVCCVV has an immutable U-L1 / next-V-L13 repeated-L conflict. Therefore this source-identity erosion mechanism is terminal under the stipulated actual complete histories. Genuine UQ/UB A erosion is real but cannot seed an unbounded seven-atom continuation.',CORE_and_marker_qualification='A is aliveCORE before next RAW and can physically die at next tick1/read2. D and C RAW may complete; their actual followingM11 is what fails in some rows. Every R repair inside CORE remains a valid physical operation. No unexecuted marker is treated as already read, and no old input-age law is used afterFOREIGN.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'terminal_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('FirstFOREIGN,VCCV terminal:21 next cases, only preparedB->V; all8 actualG8 predecessors forceU and UBVCCVV is impossible. Prepared B shadow erodes aliveCORE then next-read2, simple proxy; no genuine U ancestry or general erosion terminality.')
