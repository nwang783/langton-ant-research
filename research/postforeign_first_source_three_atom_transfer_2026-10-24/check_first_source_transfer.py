"""Direct local first-source transfer through two later ordinary RAW atoms.
No old-eight maturity is applied after a foreign. Includes genuine U-entry
fourth-atom erosion controls with explicit original physical/CORE lifetime.
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
def raw(tokens):return ''.join(W[a]for a in tokens)
def after(word,pose=(0,0,0)):
 p,h=pose[:2],pose[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
 return*p,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,p):return z(p),z(after(W[atom],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(q,v),den),Q(det(q,u),den)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1
 lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None

def physical_owner(tokens,tick):
 start=0
 for i,a in enumerate(tokens):
  if tick<start+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,atom_start_tick0=start,canonical=o.describe(a,tick-start))
  start+=len(W[a])
 assert 0<=tick-start<len(l.M)
 return dict(actual_atom='next actual word',next_word_tick0=tick-start,next_word_read_number1=tick-start+1,turn=l.M[tick-start])
# Actual atomic residual output births, no full-G8 producer relabeling.
sources={}
for a in'DCVU':
 geo=l.literal_geometry(W[a]);trace=l.trace(W[a]);records=[]
 for cell in map(tuple,geo['outputs']):
  turn,tick=trace['last'][cell];assert turn=='R'
  records.append(dict(source_atomic_RAW=a,source_output_cell=cell,last_R_birth_tick0=tick,last_R_birth_read_number1=tick+1,birth_identity='THIS actual R, never an initial identity or recolored replacement',outside_source_RAW_EXIT_core=True))
 sources[a]=records
assert {a:len(v)for a,v in sources.items()}=={'D':1,'C':3,'V':6,'U':9}
triples=[];geometry_contacts=[];transfer=[]
for b1 in'DCVU':
 p2=after(W[b1]);old=chord(b1,(0,0,0))
 for b2 in'DCVU':
  p3=after(W[b1]+W[b2]);b2_context=l.trace(W[b2]+l.M);K2={add(p2[:2],l.rot(q,p2[2]))for q in l.K};K3={add(p3[:2],l.rot(q,p3[2]))for q in l.K}
  for b3 in'DCVU':
   tokens=b1+b2+b3;tr=l.trace(raw(tokens)+l.M);p4=after(raw(tokens));hit=contact(*old,*chord(b3,p3));row=dict(ordinary_atoms=tokens,first_source_pose=(0,0,0),second_entry=p2,third_entry=p3,fourth_entry=p4,third_chord_vs_first_source=hit,complete_triple_feasible=tr['feasible'])
   if hit:geometry_contacts.append(row)
   if not tr['feasible']:row['literal_conflict']=tr
   else:
    third_context=l.trace(W[b3]+l.M);K4={add(p4[:2],l.rot(q,p4[2]))for q in l.K};held=[]
    for fact in sources[b1]:
     cell=tuple(fact['source_output_cell']);local2=l.rot(sub(cell,p2[:2]),-p2[2]);local3=l.rot(sub(cell,p3[:2]),-p3[2]);assert local2 not in b2_context['first']and local3 not in third_context['first'];assert cell not in K2|K3|K4
     rec=dict(ordinary_atoms=tokens,original_source_R_fact=fact,b2_local_cell=local2,b3_local_cell=local3,b2_entire_RAW_plus_future_M11_misses=True,b3_entire_RAW_plus_future_M11_misses=True,SAME_identity_physically_alive_at_third_and_fourth_RAW_entries=True,SAME_identity_CURRENT_outside_core_at_third_and_fourth_RAW_entries=True,future_M11_reads_not_assumed_executed=True)
     transfer.append(rec);held.append(rec)
    row['all_first_source_output_identities_survive']=held
   triples.append(row)
assert len(triples)==64 and Counter(r['complete_triple_feasible']for r in triples)=={True:55,False:9}
assert len(geometry_contacts)==1 and geometry_contacts[0]['ordinary_atoms']=='CCU'and geometry_contacts[0]['third_chord_vs_first_source']==dict(old_s='0',new_t='1/2',point=['-1','-1'])
assert not geometry_contacts[0]['complete_triple_feasible']and geometry_contacts[0]['literal_conflict']['conflict_read']==42
assert len(transfer)==270
# Full physical labeled-board replay for a prescribed erosion beyond the bound.
def proxy(tokens):
 pose=(0,0,0);pieces=[]
 for i,a in enumerate(tokens):
  if a in'FQB':
   mid=after(W['F'],pose);pieces.append(dict(actual_atom_index0=i,label=a+' actualF56prefix',start=z(pose),end=z(mid)))
   if a!='F':pieces.append(dict(actual_atom_index0=i,label=a+' actualtail',start=z(mid),end=z(after(W[a],pose))))
  else:pieces.append(dict(actual_atom_index0=i,label=a,start=z(pose),end=z(after(W[a],pose))))
  pose=after(W[a],pose)
 checks=[]
 for i,new in enumerate(pieces):
  for j,old in enumerate(pieces[:i]):
   hit=contact(old['start'],old['end'],new['start'],new['end'])
   allowed=(i==j+1 and old['end']==new['start']and hit is not None and hit.get('old_s')=='1'and hit.get('new_t')=='0')
   assert hit is None or allowed,(tokens,i,j,hit)
   checks.append(dict(old_piece=j,new_piece=i,contact=hit,allowed_true_adjacency=allowed))
 return dict(pieces=pieces,all_pair_checks=checks,simple_through_all_executed_RAWs=True)

def erosion_control(tokens):
 body=raw(tokens);tr=l.trace(body+l.M);assert tr['feasible'];seed={p for p,(c,t)in tr['first'].items()if c=='L'};board=set(seed);labels={p:('initial',None)for p in seed};pose=(0,0,0);reads=[];snapshots={};starts=[];t0=0
 for a in tokens:starts.append((a,t0,pose));pose=after(W[a],pose);t0+=len(W[a])
 v1=next((i,x)for i,x in enumerate(starts)if x[0]=='V');i1,(_,start1,entry1)=v1;v4_index=i1+3;assert ''.join(tokens[i1:v4_index+1])=='VCCV';_,start4,entry4=starts[v4_index]
 original=add(entry1[:2],l.rot((0,1),entry1[2]));birth=start1+11;cut4=start4;exit4=start4+len(W['V']);death=start4+19
 local=l.rot(sub(original,entry4[:2]),-entry4[2]);assert local==(0,3)
 assert l.trace(W['V']+l.M)['first'][local]==('L',19)
 pose=((0,0),0);original_alive=False
 for tick,turn in enumerate(body+l.M):
  p,h=pose;black=p in board;assert black==(turn=='L');before=labels.get(p)
  if turn=='L':board.remove(p);labels.pop(p)
  else:board.add(p);labels[p]=('R',tick)
  if tick==birth:assert p==original and turn=='R';original_alive=True
  if tick==death:assert p==original and turn=='L'and before==('R',birth);original_alive=False
  h=(h+(1 if turn=='R'else-1))%4;pose=(add(p,l.DIRS[h]),h)
  reads.append(dict(tick0=tick,read_number1=tick+1,cell=p,turn=turn,before_BLACK=black,before_identity=before,after_identity=labels.get(p),actual_owner=physical_owner(tokens,tick)))
  if tick+1 in(cut4,exit4):
   Kcut={add(pose[0],l.rot(q,pose[1]))for q in l.K};same=labels.get(original)==('R',birth);snapshots[str(tick+1)]=dict(cut_before_next_tick0=tick+1,head=pose[0],heading=pose[1],original_A_cell=original,SAME_original_physically_alive=same,inside_actual_active_core=original in Kcut,CURRENT_same_original_residual=same and original not in Kcut)
 assert snapshots[str(cut4)]['CURRENT_same_original_residual']
 assert snapshots[str(exit4)]['SAME_original_physically_alive']and snapshots[str(exit4)]['inside_actual_active_core']and not snapshots[str(exit4)]['CURRENT_same_original_residual']
 assert labels.get(original)!=('R',birth)and not original_alive
 return dict(tokens=tokens,all_other_initial_cells_WHITE=True,complete_seed=sorted(seed),initial_black_mass=len(seed),RAW_length=len(body),RAW_plus_actual_M11_reads=len(reads),all_actual_fine_reads=reads,first_returned_V_source_pose=entry1,first_V_genuine_A_cell=original,first_V_A_birth_tick0=birth,first_V_A_birth_read_number1=birth+1,fourth_ordinary_V_entry=entry4,fourth_V_start_tick0=start4,original_A_fourth_V_local=local,exact_cut_states=snapshots,original_A_actual_death_global_tick0=death,original_A_death_owner=physical_owner(tokens,death),no_recolored_replacement_counted_as_original=True,complete_corrected_proxy=proxy(tokens),genuine_U_entry_prefix=(tokens[0]=='U'),scope='Actual complete finite-board control. It erodes a NEW postforeign first-V A identity at the FOURTH ordinary atom, without any proxy self-contact; not a THIRD-contact countercontrol or old-U-star loss.')
controls=[]
for A in'FQB':controls.append(erosion_control(list(A+'VCCV')))
for A in'QB':controls.append(erosion_control(list('U'+A+'VCCV')))
assert [r['initial_black_mass']for r in controls]==[22,23,26,28,31]
assert [r['RAW_plus_actual_M11_reads']for r in controls]==[133,141,151,169,179]
failed=l.trace(raw('UFVCCV')+l.M);assert not failed['feasible']and(failed['conflict_read'],failed['previous_read'],tuple(failed['cell']))==(157,21,(-1,2))
paths=[R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py',R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_LOCAL_FIRST_SOURCE_THREE_ATOM_TRANSFER_AND_GENUINE_FOURTH_EROSION_PENDING_REVIEW',scope='Direct literal local theorem for any actual ordinary triple b1,b2,b3 in D/C/V/U with actual final M11, including immediately after first foreign. No old-eight maturation, full-producer assumption, arbitrary-tail closure or THIRD global simplicity.',all4_actual_atomic_sources_and_fresh_R_output_identities=sources,all64_ordinary_triple_geometry_and_literal_rows=triples,unique_geometric_contact_is_literal_impossible_CCU=geometry_contacts,all270_SAME_original_output_transfer_rows=transfer,conclusion='For every legal triple, all original b1 residual-output identities miss b2/b3 COMPLETE contexts and remain SAME physical/current identities at both b3 and b4 entry. Third chord cannot touch b1 chord: sole64-case geometry CCU is literally impossible. No claim after b4 is made.',five_complete_prepared_fourth_erosion_controls=controls,failed_immediate_U_F_lift=dict(tokens='UFVCCV',literal_conflict=failed,no_finite_board_claimed=True),induction_warning='Actual U,Q,V,C,C,V and U,B,V,C,C,V controls have genuine initial U ancestry and a wholly simple expanded proxy, yet the NEW first returned V A identity becomes alive-CORE at the fourth V RAW exit and physically dies at the next actual word tick1/read2. Erosion is not a proxy contact and not loss of the original creating-U star.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'first_source_transfer.json').write_text(json.dumps(out,indent=2)+'\n');print('64 triples:55 legal, sole b3/b1 geometry CCU impossible;270 SAME first-output tags miss both complete later contexts. Five full-board fourth-erosion controls22/23/26/28/31; genuine UQ/UB, simple proxies, exact A alive-CORE then next read2 death.')
