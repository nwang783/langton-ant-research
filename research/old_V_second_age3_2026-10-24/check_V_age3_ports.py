"""Old V true preforeign age three: genuine C-port and A-cleanup branch.
Finite signed-role queries and exact contact masks, no trajectory-prefix scan.
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
# C=(2,1) is a genuine V RAW tick7/read8 R, preserved by both own tails.
C=(2,1);sources=[];query_rows=[]
for source in (4,5,6):
 name=G[source]['name'];tr=l.trace(G[source]['word']);assert tr['feasible'] and tr['last'][C]==('R',7)
 assert list(C)in G[source]['outputs']
 # The same cell is read once, not recolored by source C tails.
 p=(0,0);h=0;reads=[]
 for tick,turn in enumerate(G[source]['word']):
  if p==C:reads.append((tick,turn))
  h=(h+(1 if turn=='R'else-1))%4;p=add(p,l.DIRS[h])
 assert reads==[(7,'R')]
 sources.append(dict(actual_full_source=name,base_C_cell=C,birth_tick0=7,birth_read_number1=8,source_own_reads=reads,source_C_tail_count=name.count('C'),source_full_entry_clock=0,source_full_completion_clock=name.count('C')))
 for age in range(4):
  heading=(-age)%4
  for consumer in IDS:
   for slot,port in enumerate(G[consumer]['inputs']):
    pose=sub(C,l.rot(tuple(port),heading));key=(compact[source],compact[consumer],*pose,heading,*C,age)
    reason='sector' if(sum(pose)+heading)%2 else 'signed_COUNT5' if key in COUNT else 'UNEXCLUDED'
    assert reason!='UNEXCLUDED',(source,consumer,slot,pose,heading,age,key)
    query_rows.append(dict(actual_full_source=name,consumer=G[consumer]['name'],input_slot0=slot,input_cell=port,consumer_pose=(*pose,heading),true_full_source_ENTRY_C_age=age,key=key,reason=reason))
assert len(query_rows)==276 and Counter(r['reason']for r in query_rows)=={'sector':138,'signed_COUNT5':138}
# The geometry is reconstructed from precisely the signed 14 angle cases.
AP=R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry.json'
angles=[a for a in json.loads(AP.read_text())['conditional217_old_source_angle_interfaces']if a['old_source']=='V' and a['actual_old_source_to_FOREIGN_C_age']==3]
assert len(angles)==14
a,b=chord('V',(0,0,0));u=sub(b,a);boxes=[];poses=[];base_rows=[]
for angle in angles:
 b1,b2=angle['first_ordinary'],angle['second_ordinary'];N=3+int(b1=='C');heading=angle['second_heading_relative_old_source'];assert heading==(2-N)%4
 c,d=chord(b2,(0,0,heading));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
 bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
 boxes.append(dict(angle=angle,rational_corners=[[[v.numerator,v.denominator]for v in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=Q(det(q,v),den),Q(det(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   p2=(x,y,heading);poses.append(dict(first=b1,second=b2,second_pose=p2,old_s=str(s),new_t=str(t)))
   for A in'FQB':
    delta=after(W[A]+W[b1],(0,0,1));pa=(x-delta[0],y-delta[1],1);pe=after(W[A],pa);verts=[z(pa),z(after(W['F'],pa))]
    if A!='F':verts.append(z(pe))
    assert not any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:]))
    assert not hit(a,b,*chord(b1,pe))
    tr=l.trace(raw(A+b1+b2)+l.M);assert tr['feasible']
    base_rows.append(dict(foreign=A,first=b1,second=b2,foreign_pose=pa,second_pose=p2,old_s=str(s),new_t=str(t)))
assert len(boxes)==14 and len(poses)==47 and len(base_rows)==141
# Initial-BLACK / CURRENT-entry-core contradictions, no postforeign law.
def conflicts(row,cells):
 tokens=row['foreign']+row['first']+row['second'];tr=l.trace(raw(tokens)+l.M);pa=row['foreign_pose'];hits=[]
 for cell in cells:
  local=l.rot(sub(cell,pa[:2]),-pa[2]);first=tr['first'].get(local)
  if local in l.K:hits.append(dict(SAME_current_cell=cell,foreign_local=local,reason='CURRENT identity in foreign ENTRY core'))
  elif first and first[0]=='R':hits.append(dict(SAME_current_cell=cell,foreign_local=local,reason='first read requires WHITE',combined_tick0=first[1],actual_owner=physical_owner(tokens,first[1])))
 return hits
r=(0,0);Acell=(0,1);B=(1,0)
helper=[]
for cell in l.literal_geometry(W['V'])['outputs']:
 helper.append(add((0,4),l.rot(tuple(cell),2)))
assert set(helper)=={(0,4),(0,3),(-1,4),(-2,4),(-2,3),(-2,2)}
helper_tail=[]
for full in('V','VC'):
 tr=l.trace(raw(full));geo=l.literal_geometry(raw(full))
 assert set(map(tuple,l.literal_geometry(W['V'])['outputs']))<=set(map(tuple,geo['outputs']))
 assert all(tr['last'][tuple(q)]==l.trace(W['V'])['last'][tuple(q)]for q in l.literal_geometry(W['V'])['outputs'])
 helper_tail.append(dict(genuine_cleanup_full=full,entry_pose=(0,4,2),entry_clock=2,full_completion_clock=2+full.count('C'),true_age_at_foreign=1,six_base_outputs_SAME_and_preserved=True))
qmin=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(q['certified_minimum_C_age']>=2 for q in qmin['slots'].values())
results=[];priority=Counter();source_rows=[]
for row in base_rows:
 old_hits=conflicts(row,[r,B,Acell]);c_hits=conflicts(row,[C]);helper_hits=conflicts(row,[r,B]+helper)
 assert helper_hits and(old_hits or c_hits)
 why='r_or_B_or_original_A'if old_hits else'genuine_C_port_276_query_guard';priority[why]+=1
 rr=dict(**row,original_A_CURRENT_branch=dict(classification='excluded',priority_reason=why,existing_original_r_B_A_conflicts=old_hits,genuine_C_port_conflicts=c_hits),original_A_retired_branch=dict(classification='excluded',genuine_helper_current_conflicts=helper_hits))
 results.append(rr)
 for source in sources:source_rows.append(dict(actual_full_source=source['actual_full_source'],base_case=rr))
assert priority=={'r_or_B_or_original_A':114,'genuine_C_port_276_query_guard':27} and len(source_rows)==423
paths=[GP,CP,AP,R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',R/'audits/check_second_ordinary_small_interface_independent.json',R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/manifest.json',R/'audits/dcuv_count5_replay/queries.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'audits/check_V_parallel_reproductive_supply_independent.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'audits/check_V_C_same_heading_exclusion_independent.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'audits/check_first_foreign_returned_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_OLD_V_TRUE_AGE3_PORT_CLOSURE_PENDING_INDEPENDENT_AUDIT',scope='Only an outgoing old genuine V base at true V-base-entry-to-first-foreign C age three, for chronological FIRST new contact by SECOND ordinary RAW after the first foreign. Original U-entry complete-eight prefix and actual final M11. No other source or returned simplicity claimed.',all3_actual_containing_source_roles=sources,all276_original_C_port_age0_through3_queries=query_rows,exact_query_counts=dict(Counter(q['reason']for q in query_rows)),C_port_conclusion='SAME original C=(2,1), born actual V RAW tick7/read8, cannot first lose CURRENT status before foreign age3. All full-packet input roles, including marker-owned capture, are included. Own source C tails preserve it.',all14_signed_angle_boxes=boxes,all47_outgoing_owned_contact_poses=poses,all141_foreign_typed_two_branch_cases=results,all423_actual_source_typed_cases=source_rows,exact_original_A_current_priority_counts=dict(priority),genuine_A_cleanup_helper_branch=dict(signed_rule='2043: absent original A forces V/VC(0,4,S) at source clock2',all6_helper_base_outputs=helper,actual_source_tail_checks=helper_tail,all23_produced_input_minimum_at_least2=True,true_helper_age_before_first_foreign=1,no_postforeign_age_used=True),conclusion='Every old-V true-preforeign-age3 chronological FIRST SECOND-RAW source contact is excluded for V, VC and VCC. In the original-A-current branch,114 masks fail existing r/B/A and27 fail the new genuine C-port guard. In the original-A-retired branch every mask fails the genuine age-one cleanup-helper cohort. This is not second-step global simplicity or arbitrary-tail closure.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'V_age3_ports.json').write_text(json.dumps(out,indent=2)+'\n')
print('276 genuine C-port roles=138 sector+138 COUNT5;14 angles/47 poses/141 masks close both A branches, for all3 full source tails.')
