from pathlib import Path
import hashlib,json
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_core_record_interface_frozen_20261023_1359';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_core_record_interface.json').read_text());Y=json.loads((B/'05_u_minimum_clock_cohort_by_phase.json').read_text())
for p,h in J['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/p).read_bytes()).hexdigest()==h
old={};new={};rows=[];raises=[];activation=[]
for a in ids:
 assert raws[a]==raws[base[a]]+C*counts[a] and G[a][3]==G[base[a]][3]
 assert(raws[a][len(raws[base[a]]):]+mark).startswith(mark)
 for h in range(4):
  e=rotation(G[a][0],h);eh=(h+G[a][1])%4
  t=max(2*H(e)+A[eh],*(2*H(rotation(o,h))+w[f'w_{a}_{i}_{h}']for i,o in enumerate(sorted(G[a][4],key=xy))))
  old[a,h]=t;z=0j;hh=h;atoms=[]
  for j,word in enumerate([raws[base[a]]]+[C]*counts[a]):
   for c in word:hh=(hh+(1 if c=='R'else-1))%4;z+=(1j,1,-1j,-1)[hh]
   atoms.append(dict(atom_index=j,exit=[*xy(z),hh],core_value=2*H(z)+A[hh]))
  assert(z,hh)==(e,eh);peak=max(t,*(r['core_value']for r in atoms));new[a,h]=peak
  names={0:'D',1:'DC',4:'V',5:'VC',6:'VCC',7:'U',8:'UC',9:'UCC'}
  rows.append(dict(packet=a,name=names[a],global_phase=h,entry_core=A[h],old_peak=t,enlarged_peak=peak,atomic_exits=atoms))
  if t<peak:raises.append([a,h,t,peak])
  for q in G[a][3]:activation.append((a,h,xy(q),peak-2*H(rotation(q,h))))
assert rows==J['rows']and raises==J['raised_peaks']and len(raises)==7
old_danger=[[a,h,old[a,h]]for a in ids for h in range(4)if old[a,h]>A[h]]
new_danger=[[a,h,new[a,h]]for a in ids for h in range(4)if new[a,h]>A[h]]
assert old_danger==J['old_dangerous_cases']and len(old_danger)==13
assert new_danger==J['enlarged_dangerous_cases']and len(new_danger)==17
add=[r for r in new_danger if r[:2]not in[r[:2]for r in old_danger]]
assert add==[[5,1,26],[6,1,26],[8,1,30],[9,1,30]]
for a,h,t in add:assert t==old[base[a],h]and G[a][3]==G[base[a]][3]
assert max(r[-1]for r in activation)==28
assert set(activation)=={(r['packet'],r['phase'],tuple(r['input']),r['required_I'])for r in J['activation_requirements']}
cohorts=[]
for phase in Y['U1_strict_record_phases']:
 for e in phase['completed_abstract_states']:
  p=e['last_producer'];a=p['packet'];x,y,h=p['head'];z=complex(x,y);ph=(h+1)%4
  peak=2*(y-x)+new[a,ph];end=z+rotation(G[base[a]][0],h);eh=(h+G[base[a]][1])%4;core=2*int(end.imag-end.real)+A[(eh+1)%4]
  cohorts.append(dict(source=a,pose=p['head'],C_age_residue=phase['heading'],youngest_input_mask=e['minimum_age_input_mask'],old_source_peak=p['U1_created_peak'],atomic_source_peak=peak,base_exit=[*xy(end),eh],base_exit_core=core,excluded_under_enlarged_history=peak>=30))
assert cohorts==J['q_youngest_necessary_templates']and len(cohorts)==16
removed=[r for r in cohorts if r['excluded_under_enlarged_history']];assert removed==J['removed_q_youngest_templates']and len(removed)==4
assert all(r['C_age_residue']==0 and r['base_exit']==[-3,1,0]and r['base_exit_core']==30 for r in removed)
out=dict(status='PASS independent enlarged atomic-core historical-observable interface',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),literal_rows=32,raised_peaks=raises,old_dangerous=13,new_dangerous=17,added_rows=add,activation_weight_minimum=28,removed_q_youngest_templates=removed,scope='New stronger history only. Four added goal rows reduce by true-marker truncation to base V1/U1; eleven existing exclusions restrict unchanged. Conditional confinement can use this new17-row reduction. Four q-youngest positive-age residue0 templates tie earlier observed atomic core30 and fail ONLY this enlarged U1 premise; twelve templates and q-older remain. Original11of13 ledger and global conjecture remain open.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='removed_q_youngest_templates'})
