"""Old D age3: same common-R8 currentness and six incoming-bud guards.
Exact completed-context roles, actual next atom and final E endpoint counts.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util, json, hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py')
o=load('ownership',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
W=o.WORDS;GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);compact={a:i for i,a in enumerate(IDS)}
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,line.split()[:8])) for line in CP.read_text().splitlines()}

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(word,pose=(0,0,0)):
 p,h=pose[:2],pose[2]
 for turn in word:
  h=(h+(1 if turn=='R'else-1))%4;p=add(p,l.DIRS[h])
 return *p,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,pose):return z(pose),z(after(W[atom],pose))
def hit(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(q,v),den),Q(det(q,u),den)
  return(s,t) if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return('collinear',max(Q(0),lo),min(Q(1),hi)) if max(0,lo)<=min(1,hi)else None

def physical_owner(tokens,tick):
 lo=0
 for i,atom in enumerate(tokens):
  if tick<lo+len(W[atom]):return dict(actual_atom_index0=i,actual_atom=atom,canonical=o.describe(atom,tick-lo))
  lo+=len(W[atom])
 assert 0<=tick-lo<len(l.M)
 return dict(actual_atom='next actual word',next_word_tick0=tick-lo,next_word_read_number1=tick-lo+1,turn=l.M[tick-lo])

def raw(tokens):return ''.join(W[a]for a in tokens)
common=(2,0);beta=(1,-1);source_roles=[];queries=[];ports=[]
for source in(0,1):
 name=G[source]['name'];trace=l.trace(G[source]['word']);assert trace['last'][common]==('R',8)and list(common)in G[source]['outputs'];assert beta not in trace['first']
 # The genuine common identity is not recolored in an attached source C.
 pos=(0,0);h=0;rr=[]
 for tick,turn in enumerate(G[source]['word']):
  if pos==common:rr.append((tick,turn))
  h=(h+(1 if turn=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 assert rr==[(8,'R')]
 source_roles.append(dict(actual_full_source=name,source_full_entry_clock=0,source_full_completion_clock=name.count('C'),common_cell=common,common_birth_tick0=8,common_birth_read_number1=9,own_C_tail_preserves_SAME_common=True,source_RAW_misses_genuine_incoming_beta=True))
 for age in range(4):
  heading=(-age)%4
  for consumer in IDS:
   for slot,cell in enumerate(G[consumer]['inputs']):
    p=sub(common,l.rot(tuple(cell),heading));key=(compact[source],compact[consumer],*p,heading,*common,age)
    if age<name.count('C'):why='full_source_not_yet_completed'
    elif age+G[consumer]['name'].count('C')>3:why='consumer_full_tail_cannot_complete_before_foreign3'
    elif age<3:why='signed1344_common_atomic_ENTRY_minimum3'
    elif(sum(p)+heading)%2:why='sector'
    elif key in COUNT:why='signed_COUNT5'
    else:why='exact_E3_plain_port';ports.append(dict(actual_full_source=name,consumer=G[consumer]['name'],input_slot0=slot,input_cell=cell,pose=(*p,heading),key=key))
    queries.append(dict(actual_full_source=name,consumer=G[consumer]['name'],input_slot0=slot,input_cell=cell,pose=(*p,heading),true_full_source_ENTRY_age=age,key=key,reason=why))
assert len(queries)==184 and len(ports)==5
assert {(p['actual_full_source'],p['consumer'],p['pose'])for p in ports}=={('D','D',(1,0,1)),('D','V',(-1,0,1)),('D','V',(0,1,1)),('DC','V',(-1,0,1)),('DC','V',(0,1,1))}
old_start,old_exit=chord('D',(0,0,0));assert(old_start,old_exit)==((-1,-1),(1,1))
next_chords=[]
for atom in'DCVU':
 c,d=chord(atom,(1,1,0));contact=hit(*chord('V',(0,1,1)),c,d);assert contact and 0<contact[0]<1 and 0<contact[1]<1
 next_chords.append(dict(actual_next_N_atom=atom,actual_next_pose=(1,1,0),next_chord=[c,d],V_lower_E3_chord=list(chord('V',(0,1,1))),strict_intersection_new_V_parameter=str(contact[0]),strict_intersection_next_atom_parameter=str(contact[1])))
for p in ports:
 pc=p['pose'];new=chord(p['consumer'],pc)
 if p['consumer']=='D':
  assert z(pc)==old_exit
  p['causal_cut']='entry repeats genuine old D EXIT vertex at source clock3, not true adjacency'
 elif pc==(-1,0,1):
  ct=hit(old_start,old_exit,*new);assert ct==(Q(1,2),Q(1,2));p.update(causal_cut='strict source-D chord crossing',old_parameter='1/2',new_parameter='1/2')
 else:
  assert pc==(0,1,1);p.update(causal_cut='strict crossing of whichever actual next N D/C/V/U atom followed old D exit',actual_next_atom_cases=next_chords)
# Genuine incoming beta: retain every actual previous full EXIT, not its entry age.
prior=[]
for previous in('D','DC','V','VC','VCC','U','UC','UCC'):
 raw0=raw(previous);ep=after(raw0);slot=add(ep[:2],l.rot(beta,ep[2]));tr=l.trace(raw0);geo=l.literal_geometry(raw0);assert tr['last'][slot]==('R',len(raw0)-2)and list(slot)in geo['outputs']
 prior.append(dict(actual_previous_full=previous,actual_final_EXIT_clock=0,previous_full_ENTRY_clock=-previous.count('C'),full_ENTRY_age_at_foreign=3+previous.count('C'),true_post_EXIT_age_at_foreign=3,beta_in_actual_previous_full_frame=slot,birth_tick0=len(raw0)-2,birth_read_number1=len(raw0)-1,minimum_consumer_start_post_EXIT_age=3,own_following_D_DC_and_C_tails_preserve_until_a_real_input=True))
# Reconstruct precisely the signed12 angle cases,18 poses,54 foreign types.
AP=R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry.json';angles=[a for a in json.loads(AP.read_text())['conditional217_old_source_angle_interfaces']if a['old_source']=='D'and a['actual_old_source_to_FOREIGN_C_age']==3];assert len(angles)==12
boxes=[];poses=[];rows=[];a,b=old_start,old_exit;u=sub(b,a)
for angle in angles:
 b1,b2=angle['first_ordinary'],angle['second_ordinary'];N=3+int(b1=='C');h=angle['second_heading_relative_old_source'];assert b1!='C'and N==3 and h==3
 c,d=chord(b2,(0,0,h));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)];boxes.append(dict(angle=angle,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=Q(det(q,v),den),Q(det(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   p2=(x,y,h);poses.append(dict(first=b1,second=b2,second_pose=p2,old_s=str(s),new_t=str(t)))
   for A in'FQB':
    delta=after(W[A]+W[b1],(0,0,1));pa=(x-delta[0],y-delta[1],1);pe=after(W[A],pa);vertices=[z(pa),z(after(W['F'],pa))]
    if A!='F':vertices.append(z(pe))
    assert not any(hit(a,b,c0,d0)for c0,d0 in zip(vertices,vertices[1:]))and not hit(a,b,*chord(b1,pe))
    tr=l.trace(raw(A+b1+b2)+l.M);assert tr['feasible'];records=[]
    for label,cell in(('common',common),('incoming_beta',beta)):
     local=l.rot(sub(cell,pa[:2]),-pa[2]);first=tr['first'].get(local);rec=dict(tag=label,cell=cell,foreign_local=local,in_foreign_ENTRY_core=local in l.K,actual_first_read=first)
     if first:rec['actual_owner']=physical_owner(A+b1+b2,first[1])
     records.append(rec)
    rows.append(dict(foreign=A,first=b1,second=b2,foreign_pose=pa,second_pose=p2,old_s=str(s),new_t=str(t),tag_context=records))
assert len(boxes)==12 and len(poses)==18 and len(rows)==54
# The final E run is NOT a depth search. Counts solve exact displacement.
def endpoint_counts(start,end,consumer,A):
 dx,dy=end[0]-start[0],end[1]-start[1];solutions=[]
 if dx<0 or dy>0:return solutions
 total=-dy
 for vcount in range(total+1):
  dcount=total-vcount;rest=dx-dcount-3*vcount
  if rest<0 or rest%4:continue
  ucount=rest//4
  if dcount+vcount+ucount==0:
   if consumer=='U'or(consumer=='V'and A in'FQ'):solutions.append(dict(D=dcount,V=vcount,U=ucount,continuation='empty; consuming base is actual last V/U'))
  elif ucount or(vcount and A in'FQ'):solutions.append(dict(D=dcount,V=vcount,U=ucount,continuation='nonempty; some actual ordering ends allowed V/U'))
 return solutions
common_cut=[];beta_cut=[];open_rows=[];beta_endpoints=[]
for index,row in enumerate(rows):
 row['base_row_index0']=index;common_rec,beta_rec=row['tag_context']
 if common_rec['in_foreign_ENTRY_core']or(common_rec['actual_first_read']and common_rec['actual_first_read'][0]=='R'):
  row['classification']='excluded_by_same_original_common_CURRENT';common_cut.append(row);continue
 if beta_rec['in_foreign_ENTRY_core']or(beta_rec['actual_first_read']and beta_rec['actual_first_read'][0]=='R'):
  assert row['first']=='D'and row['second']in'DC'and row['second_pose']==(0,-1,3)
  local_rows=[]
  for consumer in('D','V','U'):
   gid={'D':0,'V':4,'U':7}[consumer]
   for slot,input_cell in enumerate(G[gid]['inputs']):
    pp=sub(beta,l.rot(tuple(input_cell),1));end=after(W[consumer],(*pp,1));wrong=(sum(pp)+1)%2
    possible=[]if wrong else endpoint_counts(end[:2],row['foreign_pose'][:2],consumer,row['foreign'])
    assert not possible
    local_rows.append(dict(base_row_index0=index,foreign=row['foreign'],foreign_pose=row['foreign_pose'],consumer=consumer,input_slot0=slot,input_cell=input_cell,consumer_pose=(*pp,1),consumer_RAW_exit=end,classification='wrong_sector'if wrong else'exact_E_count_equation_has_no_allowed_last_V_U_solution',count_solutions=possible))
  assert len(local_rows)==8;beta_endpoints.extend(local_rows);row['classification']='excluded_by_incoming_beta_min3_and_final_E_endpoint_guard';row['all8_beta_E3_endpoints']=local_rows;beta_cut.append(row)
 else:row['classification']='necessary_only_unresolved';open_rows.append(row)
assert(len(common_cut),len(beta_cut),len(open_rows))==(36,6,12)and len(beta_endpoints)==48
assert all(r['first']in'VU'and r['second']in'VU'and r['second_pose']==(1,0,3)for r in open_rows)
paths=[GP,CP,AP,R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',R/'audits/check_second_ordinary_small_interface_independent.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'audits/check_atomic_common_four_C_independent.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'audits/check_atomic_exit_bud_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'audits/check_first_foreign_returned_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_OLD_D_AGE3_COMMON_BETA_REDUCTION_PENDING_INDEPENDENT_AUDIT',scope='Old outgoing D base inside U-entry complete-eight prefix, true preforeign age3; chronological FIRST new SECOND ordinary RAW contact. Actual source D/DC both retained. Only42/54 excluded per source role here;12 necessary residues retained. No second simplicity or postforeign ages.',all2_genuine_common_source_roles=source_roles,all184_common_first_loss_full_role_queries=queries,query_classification=dict(Counter(q['reason']for q in queries)),all5_surviving_completed_E3_plain_common_ports=ports,all4_actual_next_N_atom_strict_crossing_interfaces=next_chords,common_conclusion='SAME original common(2,0) R8 remains CURRENT through foreign-entry clock3 under actual old-eight simple geometry. The three possible plain ports fail actual oldD exit/source/next-chord contacts; source DC removes one by COUNT5.',all8_actual_prior_full_EXIT_bud_roles=prior,beta_guard_clock_scope='Beta cannot first lose CURRENT before a full consumer starts at old clock3. Any consuming full packet must complete before the first foreign at clock3, so it is plain D/V/U E. All later old words are also plain E D/V/U; exact counts and actual last-V/U adjacency are exhaustive. No source full-entry age reset or postforeign age.',all12_signed_angle_boxes=boxes,all18_contact_poses=poses,all54_foreign_typed_masks=rows,all48_incoming_beta_endpoint_obligations=beta_endpoints,exact_disjoint_classification=dict(Counter(r['classification']for r in rows)),remaining12_necessary_states=open_rows,no_actual_genuine_countercontrol_or_global_closure_claimed=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'D_age3_common_beta.json').write_text(json.dumps(out,indent=2)+'\n');print('184 common roles -> five completed E3 ports, all old-prefix contacts;54 masks=36 same-common +6 incoming-beta endpoint exclusions +12 necessary V/U,V/U residues per source tail.')
