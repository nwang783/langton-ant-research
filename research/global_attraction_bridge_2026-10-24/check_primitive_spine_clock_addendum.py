"""Bind the signed full-field layering; check every new finite clock identity."""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent
J=json.loads((P/'CHRONOLOGICAL_SPINE_ORIENTATION_CHECKED.json').read_text());A=J['MT_all_n'];D=((0,1),(1,0),(0,-1),(-1,0))
parent={tuple(q):tuple(p)for q,p in A['base_complete_tree']};time={tuple(q):t for typ,q,t,p,h,src in A['cap_last_parent_records']};root=(-2,372);time[root]=69097
rows={tuple(z['representative']):z for z in A['phase_rows']};jumps=[]
for q,r in parent.items():
 jump=time[r]-time[q];assert jump>0;jumps.append((jump,q,r,time[q],time[r]))
assert max(jumps)==(29865,(210,186),(210,187),29029,58894)
bulk=[]
for r,z in rows.items():
 rp=tuple(z['parent_representative']);tau=z['last_time_constant'];taurp=rows[rp]['last_time_constant'];delta=z['parent_layer_shift']
 assert time[r]==tau and time[(r[0]+2,r[1]+2)]==tau-104
 jump=taurp-tau-104*delta;assert jump>0;bulk.append(dict(cell=r,parent_class=rp,layer_shift=delta,jump=jump))
assert max(z['jump']for z in bulk)==125
S=list(map(tuple,A['spine_base']));anchor=S[300];period=[time[S[i+1]]-time[S[i]]for i in range(300,304)];assert period==[1,1,5,97]
checks=[]
for c in J['MT_controls']:
 n=c['n'];K=n-100;start=tuple(c['start_pose'][0]);h=c['start_pose'][1];pos=[]
 w=c['complete_prefix_word'][c['start']:c['end']];p=start;last={}
 for i,ch in enumerate(w):
  pos.append(p);last[p]=i;h=(h+(1 if ch=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 last[p]=len(w);assert p==root
 actual_parent={tuple(q):tuple(p)for q,p in c['full_interval_tree']}
 actualmax=max((last[r]-last[q],q,r)for q,r in actual_parent.items());assert actualmax==(29865,(210,186),(210,187))
 for q in actual_parent:
  if q[0]<=364:pred=time[q]+104*K
  elif q[0]>=365+2*K:pred=time[(q[0]-2*K,q[1]-2*K)]
  else:
   x=363 if q[0]%2 else 364;r=(x,x-(q[0]-q[1]));k=(q[0]-x)//2;pred=rows[r]['last_time_constant']+104*(K-k)
  assert pred==last[q]
 old=(206,229);B0={tuple(q):i for q,i in c['full_start_field']};assert B0[old]==20165
 death=31805+208*n;first=pos.index(old);assert c['start']+first==death and w[first]=='L'
 checks.append(dict(n=n,actual_max_edge_jump=actualmax,old_input_cell=old,birth=20165,death=death,age=death-20165,all_time_labels_checked=len(actual_parent)))
assert all(c['layer_shift']==1 and c['turn_sum']==0 for c in J['canonical_quotient']['cycles'])
fs=['CHRONOLOGICAL_SPINE_ORIENTATION_MANIFEST.json','../audits/check_chronological_spine_independent.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR addendum; independent audit pending',baseline_edge_count=len(parent),maximum=max(jumps),bulk_jumps=bulk,inserted_spine_jumps=period,controls=checks,
 canonical_literal_cycles_primitive_and_zero_turn=True,universal_primitive_and_zero_turn_proof='Geometric proof in PRIMITIVE_SPINES_AND_LAST_PARENT_CLOCK.md, not inferred from finite cases.',
 dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='Primitive embedded quotient cycles and all-n fixed-family last-parent jump bound. Not bounded lifetime ages or a universal record-clock occurrence theorem.')
(P/'PRIMITIVE_SPINE_CLOCK_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('AUTHOR checked',len(parent),'baseline edges, all22 clocks, all',sum(c['all_time_labels_checked']for c in checks),'literal parameter labels')
