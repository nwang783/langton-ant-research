"""Exact arithmetic/interface for atom-core enlarged historical records.
No finite-state reachability search and no funding case exclusion.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
YP=W/'chronology_dcuv/u_minimum_clock_cohort_by_phase.json'
AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json'
G=json.loads(GP.read_text())['geometry'];M=json.loads(RP.read_text());Y=json.loads(YP.read_text());AT=json.loads(AP.read_text())
A=M['core_offsets'];T={(a,h):v for a,h,v in M['created_peaks']};IDS=[0,1,4,5,6,7,8,9]
assert A==[0,22,20,10]
C=AT['C_word'];marker=G[0]['marker'];assert C.startswith(marker)
PP=Path(M['potential_file']);v=json.loads(PP.read_text())['values']
def rot(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def base(a):return 0 if a in[0,1]else 4 if a in[4,5,6]else 7
def atom_ends(a,h):
 p=(0,0);hh=h;rows=[]
 for k,word in enumerate([G[base(a)]['word']]+[C]*G[a]['name'].count('C')):
  for ch in word:
   hh=(hh+(-1 if ch=='L'else 1))%4;dx,dy=rot((0,1),hh);p=p[0]+dx,p[1]+dy
  rows.append(dict(atom_index=k,exit=[*p,hh],core_value=2*sum(p)+A[hh]))
 z=rot(G[a]['endpoint'][:2],h)
 assert p==z and hh==(h+G[a]['endpoint'][2])%4
 return rows
rows=[];new=[];old_danger=[];danger=[]
for a in IDS:
 assert G[a]['word']==G[base(a)]['word']+C*G[a]['name'].count('C')
 assert G[a]['inputs']==G[base(a)]['inputs']
 # A final truncated base has its ACTUAL following marker, including when tail C remains.
 assert (G[a]['word'][len(G[base(a)]['word']):]+marker).startswith(marker)
 for h in range(4):
  e=G[a]['endpoint'];z=rot(e[:2],h)
  literal_T=max([2*sum(z)+A[(h+e[2])%4]]+[
   2*sum(rot(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(G[a]['outputs'])])
  assert literal_T==T[a,h]
  atoms=atom_ends(a,h);peak=max([T[a,h]]+[r['core_value']for r in atoms]);r=dict(packet=a,name=G[a]['name'],global_phase=h,entry_core=A[h],old_peak=T[a,h],enlarged_peak=peak,atomic_exits=atoms)
  rows.append(r)
  if peak>T[a,h]:new.append([a,h,T[a,h],peak])
  if T[a,h]>A[h]:old_danger.append([a,h,T[a,h]])
  if peak>A[h]:danger.append([a,h,peak])
old_keys={tuple(r[:2])for r in old_danger};added=[r for r in danger if tuple(r[:2])not in old_keys]
assert len(old_danger)==13 and len(danger)==17
assert added==[[5,1,26],[6,1,26],[8,1,30],[9,1,30]]
reductions=[]
for a,h,peak in added:
 b=base(a);assert h==1 and peak==T[b,h]>A[h]
 reductions.append(dict(full_packet=a,base_goal=b,global_phase=h,threshold=peak,identical_residual_inputs=G[a]['inputs'],base_following_marker=marker))
activation=[dict(required_I=r['enlarged_peak']-2*sum(rot(q,r['global_phase'])),packet=r['packet'],phase=r['global_phase'],input=q)for r in rows for q in G[r['packet']]['inputs']]
assert max(z['required_I']for z in activation)==28
# In U0N coordinates the chosen diagonal is H=y-x; its global phase is h+1.
cohorts=[]
for ph in Y['U1_strict_record_phases']:
 for e in ph['completed_abstract_states']:
  p=e['last_producer'];a=p['packet'];x,y,h=p['head'];r=next(r for r in rows if r['packet']==a and r['global_phase']==(h+1)%4)
  peak=2*(y-x)+r['enlarged_peak'];b=base(a);dx,dy=rot(G[b]['endpoint'][:2],h);bh=(h+G[b]['endpoint'][2])%4
  bp=[x+dx,y+dy,bh];bc=2*(bp[1]-bp[0])+A[(bh+1)%4]
  cohorts.append(dict(source=a,pose=p['head'],C_age_residue=ph['heading'],youngest_input_mask=e['minimum_age_input_mask'],old_source_peak=p['U1_created_peak'],atomic_source_peak=peak,base_exit=bp,base_exit_core=bc,excluded_under_enlarged_history=peak>=30))
removed=[r for r in cohorts if r['excluded_under_enlarged_history']]
assert len(cohorts)==16 and len(removed)==4
assert all(r['C_age_residue']==0 and r['base_exit']==[-3,1,0]and r['base_exit_core']==30 for r in removed)
O=dict(status='AUTHOR_ATOMIC_CORE_RECORD_INTERFACE_ARITHMETIC_PASS',scope='Enlarged history includes actual atomic prefix cores, retaining original residual weights. Exact17-family interface and a conditional q-youngest residue-zero exclusion ONLY under the enlarged strict U1 premise. No original U1/V1 closure, no global funding theorem.',core_offsets=A,rows=rows,old_dangerous_cases=old_danger,enlarged_dangerous_cases=danger,new_dangerous_cases=added,base_prefix_reductions=reductions,raised_peaks=new,initial_activation_minimum_I=28,activation_requirements=activation,q_youngest_necessary_templates=cohorts,removed_q_youngest_templates=removed,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,YP,AP,PP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/atomic_core_record_interface.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(dict(rows=len(rows),old_danger=len(old_danger),enlarged_danger=len(danger),I=28,added=added,youngest_templates=len(cohorts),removed=len(removed)))
