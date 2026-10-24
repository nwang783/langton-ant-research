"""Separate regression: RAW-complete C repairs an old CORE hole without contact,
then actual next-M11 g demand fails. Original signed port guard stays unchanged."""
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
def hit(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if not de:return None
 s,t=Q(det(q,v),de),Q(det(q,u),de)
 return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None

def owner(T,t):
 n=0
 for i,a in enumerate(T):
  if t<n+len(W[a]):return dict(actual_atom_index0=i,atom=a,canonical=o.describe(a,t-n))
  n+=len(W[a])
 return dict(atom='actual next word',tick0=t-n,read_number1=t-n+1,turn=l.M[t-n])
controls=[]
for pre in('','UQ','UB'):
 T=pre+'VCCVCD';body=raw(T);tr=l.trace(body+l.M);complete=tr['feasible'];assert complete==(pre=='');starts=[];pose=(0,0,0);n=0
 for a in T:starts.append((n,pose));n+=len(W[a]);pose=after(W[a],pose)
 vi=len(pre);source_start,sp=starts[vi];ci=vi+4;cstart,cp=starts[ci];dstart,dp=starts[ci+1];h=add(sp[:2],l.rot((-1,-1),sp[2]));g=add(sp[:2],l.rot((-1,-2),sp[2]));A=add(sp[:2],l.rot((0,1),sp[2]));assert after(raw('VCCV'))==(-1,1,2)
 if complete:executed=body+l.M
 else:
  assert tr['conflict_read']==dstart+8 and tuple(tr['cell'])==g and tr['turn']=='R';assert tr['previous_read']==28+(57 if pre=='UQ' else 67);assert l.trace(body[:dstart])['feasible'];executed=body[:tr['conflict_read']]
  # The C RAW is complete; C+actualM11 is NOT complete/feasible.
  mtest=l.trace(raw(T[:-1])+l.M);assert not mtest['feasible']and mtest['conflict_read']==dstart+8
 et=l.trace(executed);assert et['feasible'];seed={p for p,(c,t)in et['first'].items()if c=='L'};B=set(seed);labels={p:('initial',None)for p in seed};pose=(0,0,0);rr=[];snaps={}
 for t,c in enumerate(executed):
  p=pose[:2];assert(p in B)==(c=='L');old=labels.get(p)
  if c=='L':B.remove(p);labels.pop(p)
  else:B.add(p);labels[p]=('R',t)
  rr.append(dict(tick0=t,read_number1=t+1,cell=p,turn=c,before_identity=old,after_identity=labels.get(p),actual_owner=owner(T,t)));pose=after(c,pose)
  if t+1 in(cstart,cstart+13,dstart,dstart+6,len(executed)):
   K={add(pose[:2],l.rot(q,pose[2]))for q in l.K};snaps[str(t+1)]=dict(cut_before_tick0=t+1,pose=pose,hole_cell=h,hole_BLACK=h in B,hole_identity=labels.get(h),hole_CORE=h in K,original_A_alive=labels.get(A)==('R',source_start+11),shadow_cell=g,shadow_BLACK=g in B,shadow_identity=labels.get(g))
 assert not snaps[str(cstart)]['hole_BLACK'] and snaps[str(cstart)]['original_A_alive']
 assert snaps[str(cstart+13)]['hole_identity']==('R',cstart+12) and not snaps[str(cstart+13)]['original_A_alive']
 assert snaps[str(dstart)]['hole_identity']==('R',cstart+12) and snaps[str(dstart)]['hole_CORE']
 assert not snaps[str(dstart+6)]['hole_BLACK'];assert rr[dstart+5]['cell']==h and rr[dstart+5]['turn']=='L'and rr[dstart+5]['before_identity']==('R',cstart+12)
 c_hit=hit(*chord('V',sp),*chord('C',cp));d_hit=hit(*chord('V',sp),*chord('D',dp));assert c_hit is None and d_hit==dict(old_s='0',new_t='1',point=[str(q)for q in z(sp)])
 if pre:
  assert snaps[str(cstart)]['shadow_identity']==('R',tr['previous_read']) and snaps[str(dstart)]['shadow_identity']==('R',tr['previous_read']) and snaps[str(len(executed))]['shadow_identity']==('R',tr['previous_read'])
  assert pose[:2]==g and g in B
 else:assert len(seed)==8
 controls.append(dict(tokens=T,complete_RAW_and_actual_M11=complete,all_other_initial_cells_WHITE=True,complete_seed=sorted(seed),initial_black_mass=len(seed),executed_fine_reads=rr,source_V_pose=sp,source_V_hole=h,source_V_A=A,foreign_shadow=g,exact_cut_snapshots=snaps,C_RAW_completes=True,C_RAW_old_V_proxy_contact=c_hit,C_hole_repair=dict(tick0=cstart+12,read_number1=cstart+13,physical_owner=owner(T,cstart+12),into_C_EXIT_CORE=True),hole_new_R_deleted_again_by_D=dict(tick0=dstart+5,read_number1=dstart+6,physical_owner=owner(T,dstart+5)),intended_D_contact=d_hit,whole_word_failure=None if complete else tr,following_actual_M11_fails_if_genuine_UQ_UB=bool(pre),actual_next_turn_if_failure='L'if pre else None,full_D_proxy_executed=complete,no_U_ancestry_claim_for_prepared8=not bool(pre)))
paths=[H/'manifest.json',R/'audits/check_erosion_return_port_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_COMPLETED_RAW_C_HOLE_REPAIR_AND_SHADOW_HANDOFF_PENDING_REVIEW',scope='A genuine physical RAW-complete C can repair the old V entry CORE hole without proxy contact after real UQ/UB A erosion; the following actualM11 fails on a distinct untouched foreign shadow. Prepared8 VCCVCD attains endpoint return but lacks this foreign state. No arbitrary-tail simplicity/countercontrol or marked C continuation is claimed.',three_exact_prepared_or_genuine_controls=controls,necessary_restoration_interface='A returning modified history cannot be excluded solely because h was V L2-deleted: C R12 restores h into active EXIT K and completes RAW without oldV contact. It must ALSO remove the distinct genuine Q/B shadow g before next-word R8. Actual L removal and R restoration inside active CORE count, not only residual outputs.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'C_repair_shadow.json').write_text(json.dumps(out,indent=2)+'\n');print('Prepared8 VCCVCD endpoint loop, and genuine UQ/UB C-RAW repair: h R12 into EXITCORE, nextD L5 deletes repair, nextD R8 blocked by original FOREIGN shadow. C RAW completes; C+actualM11 fails.')
