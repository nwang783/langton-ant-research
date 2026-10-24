"""Actual C-source first-foreign contact reduction with full-producer roles.
Finite signed catalogue join, exact endpoint cones, four forced word controls.
No arbitrary standalone-C language or prefix-tree search.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';WP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];G7=json.loads(WP.read_text())['macro_words'];M=G[0]['marker'];VEC=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
W={a:G7[i]['word']for i,a in enumerate('DCVUFQB')}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def derive(word):
 p=(0,0);h=0;req={};par=set();reads={}
 for t,ch in enumerate(word):
  bit=(ch=='L')^(p in par);assert p not in req or req[p]==bit
  req[p]=bit;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])
 return req,p,h,reads
# Literal C has only the canonical core as black requirements, no residual
# input, and three fresh outputs. Its entry/exit markers are supplied below
# by the actual containing full packet, not assumed as a free C language.
c_req,cep,ceh,c_reads=derive(W['C']+M)
assert {q for q,b in c_req.items()if b}==K
_,cep,ceh,c_raw_reads=derive(W['C']);odd={q for q,ts in c_raw_reads.items()if len(ts)%2}
exit_core={add(cep,rot(q,ceh))for q in K}
assert (K^odd)-exit_core=={(1,2),(2,0),(2,1)}
for full,base in((0,0),(1,0),(4,4),(5,4),(6,4),(7,7),(8,7),(9,7)):
 assert G[full]['inputs']==G[base]['inputs']
# Every C here is a real tail of one of these seven full-source roles.
producer_roles=[]
for a,base,number in((1,'D',1),(5,'V',1),(6,'V',2),(8,'U',1),(9,'U',2)):
 for j in range(1,number+1):
  prefix=W[base]+(j-1)*W['C'];_,cp,ch,_=derive(prefix)
  source_word=G[a]['word'];_,_,_,rr=derive(source_word)
  actual_context=source_word+M;assert actual_context[len(prefix):len(prefix)+11]==M
  assert actual_context[len(prefix)+15:len(prefix)+26]==M
  slots={name:add(cp,rot(q,ch))for name,q in {'C_common':(2,0),'C_exit_bud':(1,2),'incoming_exit_bud':(1,-1)}.items()}
  details={}
  for name,q in slots.items():
   ts=rr[q];assert ts[-1][1]=='R'
   if name=='C_common':assert ts[-1][0]==len(prefix)+8
   elif name=='C_exit_bud':assert ts[-1][0]==len(prefix)+13
   else:assert ts[-1][0]<len(prefix)
   assert q in set(map(tuple,G[a]['outputs']))
   details[name]=dict(full_output_slot=q,physical_reads_in_full_source=ts)
  reqC,_,_,rC=derive(W['C']+M);assert all(q not in rC for q in[(1,-1)])
  producer_roles.append(dict(full_packet=G[a]['name'],C_index=j,C_atomic_entry_clock_offset=j-1,C_atomic_exit_clock_offset=j,atomic_to_full_consumer_age_shift=j-1,C_pose_in_full_source=(*cp,ch),full_producer_pose_in_C_chart=(*rot((-cp[0],-cp[1]),-ch),(-ch)%4),full_output_roles=details,remaining_C_tails=number-j,actual_C_entry_marker_supply='inside_the_actual_C_RAW_word',actual_C_exit_marker_supply='following_actual_C_tail'if j<number else'actual_full_packet_marker'))
assert len(producer_roles)==7
# These exact shifts are the signed 1325/1344 scope, not a naive JO relabel.
assert producer_roles[-1]['full_packet']=='UCC'and producer_roles[-1]['C_index']==2
assert producer_roles[-1]['full_output_roles']['C_common']['full_output_slot']==(0,7)
assert next(r for r in producer_roles if r['full_packet']=='VCC'and r['C_index']==2)['full_output_roles']['C_common']['full_output_slot']==(1,6)
P=json.loads((H/'foreign_first_contact_interface.json').read_text());T=json.loads((H/'foreign_tail_first_contact.json').read_text());cases=[]
for r in P['rows']:
 if r['source_atom']=='C':
  for foreign in'FQB':cases.append(dict(foreign=foreign,piece='F_prefix',pose=r['foreign_pose'],C_age=r['permitted_C_ages'][0]))
for foreign,rows in T['rows'].items():
 for r in rows:
  if r['source_atom']=='C'and 0 in r['preceding_C_bits']:
   i=r['preceding_C_bits'].index(0);cases.append(dict(foreign=foreign,piece=foreign+'_tail',pose=r['foreign_pose'],C_age=r['permitted_C_ages'][i]))
assert len(cases)==25
# Full source completion is explicit for every catalogue role.
embedding_times=[]
for ci,c in enumerate(cases):
 for role in producer_roles:
  relative_full_exit=role['C_atomic_exit_clock_offset']+role['remaining_C_tails']-role['C_atomic_entry_clock_offset']
  embedding_times.append(dict(case=ci,full_packet=role['full_packet'],C_index=role['C_index'],full_consumer_age=c['C_age']+role['atomic_to_full_consumer_age_shift'],source_completed=relative_full_exit<=c['C_age']))
assert len(embedding_times)==175 and sum(not r['source_completed']for r in embedding_times)==16

def protected(age):
 out=[]
 if age<=3:out.append(dict(cell=(1,2),name='C_exit_bud',earliest_atomic_consumer_age=4))
 if age<=2:out.append(dict(cell=(2,0),name='C_common',earliest_atomic_consumer_age=3))
 return out

def context(p,h,word):
 req,_,_,reads=derive(word+M)
 return {add(p,rot(q,h)):dict(required_black=b,local=q,reads=reads[q])for q,b in req.items()}, {add(p,rot(q,h))for q in K}
predecessors=[];target_rows=[];survivors=[]
for ci,c in enumerate(cases):
 x,y,h=c['pose'];p=x,y;age=c['C_age'];ctx,core=context(p,h,W[c['foreign']]);hits=[]
 for tag in protected(age):
  q=tag['cell']
  if q in core:hits.append(dict(**tag,reason='current_residual_in_foreign_entry_core'))
  elif q in ctx and not ctx[q]['required_black']:hits.append(dict(**tag,reason='foreign_before_white'))
 target_rows.append(dict(case=ci,case_data=c,protected_conflicts=hits))
 for a in('V','U')if c['foreign']!='B'else('U',):
  if hits:predecessors.append(dict(case=ci,base=a,reason='target_protected_guard'));continue
  _,ep,_,_=derive(W[a]);pp=sub(p,rot(ep,h));pc,pk=context(pp,h,W[a]);ph=[]
  for tag in protected(age):
   q=tag['cell']
   if q not in pc:continue
   reason='current_residual_in_old_entry_core'if q in pk else'old_before_white'if not pc[q]['required_black']else'old_residual_input_before_signed_maturity'
   ph.append(dict(**tag,reason=reason,context=pc[q]))
  row=dict(case=ci,case_data=c,base=a,pose=(*pp,h),protected_conflicts=ph,reason='protected_old_predecessor_context'if ph else'remaining_exact_obligation')
  predecessors.append(row)
  if not ph:survivors.append(row)
assert len(predecessors)==40
assert Counter(r['reason']for r in predecessors)=={'target_protected_guard':8,'protected_old_predecessor_context':11,'remaining_exact_obligation':21}
# Exact nonnegative transport solutions at atomic ages one and two.
# After source C exit(0,1,W), age1 predecessor target(-1,2,W)
# forces one D: y=d+v=1, -x=d+3v+4u=1.
one_solutions=[]
for d in range(2):
 for v in range(2):
  if d+v!=1:continue
  rest=1-d-3*v
  if rest>=0 and rest%4==0:one_solutions.append(dict(D=d,V=v,U=rest//4))
assert one_solutions==[dict(D=1,V=0,U=0)]
# Age2 U predecessor(-4,2,S). W counts(d,v,u), then S(e,f,g):
# d+3v+4u+e+f=3, d+v-e-3f-4g=1.
# The first equation bounds d,v,u,e,f; second bounds g, no arbitrary cap.
two_solutions=[]
for d in range(4):
 for v in range(2):
  for u in range(1):
   for e in range(4):
    for f in range(4):
     if d+3*v+4*u+e+f!=3:continue
     rem=d+v-e-3*f-1
     if rem>=0 and rem%4==0:two_solutions.append(dict(W_D=d,W_V=v,W_U=u,S_D=e,S_V=f,S_U=rem//4))
assert two_solutions==[dict(W_D=0,W_V=1,W_U=0,S_D=0,S_V=0,S_U=0),dict(W_D=2,W_V=0,W_U=0,S_D=1,S_V=0,S_U=0)]
forced=[]
for labels in(['C','D','V','Q'],['C','D','U','B'],['C','D','D','C','D','U','B'],['C','V','C','U','B']):
 p=(0,0);h=0;req={};par=set();rr={};tick=0;failure=None;poses=[]
 for a in labels:
  poses.append(dict(atom=a,tick=tick,pose=(*p,h)))
  for phase,ch in enumerate(W[a]):
   bit=(ch=='L')^(p in par)
   if p in req and req[p]!=bit:
    failure=dict(atom=a,phase=phase,tick=tick,cell=p,proposed_turn=ch,forced_turn='L'if req[p]^(p in par)else'R',previous_reads=rr[p]);break
   req[p]=bit;rr.setdefault(p,[]).append((tick,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h]);tick+=1
  if failure:break
 assert failure
 forced.append(dict(word=labels,poses=poses,immutable_conflict=failure))
assert [(r['immutable_conflict']['atom'],r['immutable_conflict']['phase'])for r in forced]==[('Q',59),('B',69),('B',42),('U',14)]
# All eight actual residual-input roles, at each needed heading.
inputs=[(a,tuple(q))for a,gi in(('D',0),('V',4),('U',7))for q in G[gi]['inputs']]
assert len(inputs)==8
endpoints=[]
for guardian in((2,0),(1,-1)):
 for age,h in((3,1),(4,0)):
  for a,slot in inputs:
   pp=sub(guardian,rot(slot,h));_,ep,_,_=derive(W[a]);end=add(pp,rot(ep,h));endpoints.append(dict(guardian=guardian,age=age,base=a,input=slot,pose=(*pp,h),endpoint=(*end,h)))

def cone_solutions(delta,h):
 dx,dy=rot(delta,-h)
 if dx<0:return[]
 out=[]
 for v in range(dx+1):
  d=dx-v;rem=dy-d-3*v
  if rem>=0 and rem%4==0:out.append(dict(D=d,V=v,U=rem//4))
 return out
# Exact age4 common-bud guard to target(3,1,N).
age4=[]
for r in endpoints:
 if r['guardian']!=(2,0):continue
 ex,ey,h=r['endpoint']
 if r['age']==3:
  if ex>2:proof='after_remaining_C_x_at_least_four'
  else:
   assert(ex,ey)==(2,-1)
   assert cone_solutions(sub((3,1),(3,-1)),0)==[]
   proof='x_budget_forces_no_E_base_then_zero_x_N_U_steps_of_four_cannot_raise_y_by_two'
 else:
  assert cone_solutions(sub((3,1),(ex,ey)),0)==[]
  proof='exact_N_nonnegative_base_cone_has_no_solution'
 age4.append(dict(**r,proof=proof))
assert len(age4)==16
# Tail age3: guardian g=(1,-1) for Q target(3,-4,E), or
# common t=(2,0) for B target(4,-3,E). Both target=guardian+(2,-3).
tail3=[]
for guardian,target in(((1,-1),(3,-4)),((2,0),(4,-3))):
 for r in endpoints:
  if r['guardian']!=guardian or r['age']!=3:continue
  ex,ey,h=r['endpoint'];ss=cone_solutions(sub(target,(ex,ey)),1)
  assert ss==[]or ss==[dict(D=2,V=0,U=0)]
  if ss:assert(ex,ey)==add(guardian,(0,-1))
  tail3.append(dict(**r,target=target,foreign_before_white_local_slot=(-3,-2),remaining_E_transport_solutions=ss,exclusion='no_E_transport'if not ss else'forced_terminal_D_D_contradicts_signed_D_to_foreign_pair'))
assert len(tail3)==16 and sum(bool(r['remaining_E_transport_solutions'])for r in tail3)==6
# Classify every remaining predecessor branch using the finite derived proofs.
classified=[]
for row in predecessors:
 if row['reason']!='remaining_exact_obligation':why=row['reason']
 else:
  c=row['case_data'];age=c['C_age'];part=c['piece']
  if age==1:why='unique_D_transport_then_one_of_two_immutable_forced_words'
  elif age==2:why='two_exact_W_S_transport_solutions_both_immutable_forced_words'
  elif age==3 and part=='F_prefix':
   assert c['pose'][0]==1;why='common_bud_cannot_retire_age3_before_target_x_one_and_foreign_requires_white'
  elif age==3:why='young_guardian_cleanup_forces_terminal_D_D_before_foreign'
  else:assert age==4 and part=='F_prefix';why='common_bud_cannot_retire_before_target_3_1_N_then_foreign_core_conflict'
 classified.append(dict(**row,exclusion=why))
assert Counter(r['exclusion']for r in classified)=={'target_protected_guard':8,'protected_old_predecessor_context':11,'unique_D_transport_then_one_of_two_immutable_forced_words':2,'two_exact_W_S_transport_solutions_both_immutable_forced_words':1,'common_bud_cannot_retire_age3_before_target_x_one_and_foreign_requires_white':10,'young_guardian_cleanup_forces_terminal_D_D_before_foreign':3,'common_bud_cannot_retire_before_target_3_1_N_then_foreign_core_conflict':5}
for foreign in('Q','B'):
 req,_,_,reads=derive(W[foreign]+M);assert req[(-3,-2)]is False and reads[(-3,-2)][0]==(57,'R')
D=[GP,WP,H/'foreign_first_contact_manifest.json',H/'foreign_tail_first_contact_manifest.json',H/'complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
def enc(x):
 if isinstance(x,F):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return[enc(v)for v in x]
 return x
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='Chronological first new contact of first foreign repaired proxy after an actual complete-eight U-entry factor cannot have outgoing earlier C source. Every C is an actual tail in one of seven containing full-producer roles, with clock shifts recorded; no arbitrary standalone-C language, internal marker or global proxy simplicity.',C_full_producer_roles=producer_roles,first_contact_cases=cases,full_source_completion_timing=embedding_times,target_protected_guards=target_rows,classified_predecessor_assignments=classified,one_C_transport_solutions=one_solutions,two_C_transport_solutions=two_solutions,forced_RAW_word_conflicts=forced,all_guardian_endpoint_rows=endpoints,age4_common_guard=age4,age3_tail_guardians=tail3,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'first_foreign_C_source_exclusion.json').write_text(json.dumps(enc(o),indent=2)+'\n')
print('C source: seven actual full-producer roles;25 b0 contact cases;all40 immediate-predecessor assignments excluded. Atomic/full clock shifts and all16 age4 endpoint rows retained.')
