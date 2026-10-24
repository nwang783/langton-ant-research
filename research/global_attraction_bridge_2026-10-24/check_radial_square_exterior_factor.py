"""Literal eleven-cell full-board realization of the first radial port cycle."""
from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__).parent
D=[(0,1),(1,0),(0,-1),(-1,0)];Q=[(0,0),(1,0),(1,1),(0,1)];QS=set(Q)
seed={(-2,0),(-2,1),(-1,2),(0,2),(2,2),(2,1),(2,-1),(1,-2),(0,-3),(-1,-3),(-2,-2)}
assert len(seed)==11 and not(seed&QS)
B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=0;events=[];snap={};first={};death={};cuts={0,2,4,5,7,9,22,28,37,39,60,66,185}
for t in range(186):
 if t in cuts:snap[t]=dict(pose=[p,h],full_field=[[q,i]for q,i in sorted(B.items())],patch={Q.index(q):i for q,i in B.items()if q in QS})
 if t==185:break
 old=B.pop(p,None);ch='R'if old is None else'L';first.setdefault(p,t);events.append(dict(time=t,cell=p,heading=h,turn=ch,consumed_lifetime=old))
 if old is None:B[p]=t;h=(h+1)%4
 else:death[old]=t;h=(h-1)%4
 p=(p[0]+D[h][0],p[1]+D[h][1])
eps=[(0,2,0,'RR'),(4,5,0,'L'),(7,9,3,'RR'),(22,28,2,'RLLLLR'),(37,39,1,'RR'),(60,66,0,'RLLLLR')]
connectors=[(2,4),(5,7),(9,22),(28,37),(39,60)]
for s,t,v,w in eps:
 assert tuple(snap[s]['pose'][0])==Q[v] and snap[s]['pose'][1]==[0,3,2,1][v]
 assert ''.join(e['turn']for e in events[s:t])==w and all(tuple(e['cell'])in QS for e in events[s:t])
 assert tuple(snap[t]['pose'][0])not in QS
for s,t in connectors:assert all(tuple(e['cell'])not in QS for e in events[s:t])
assert all(tuple(e['cell'])not in QS for e in events[66:185])
assert snap[185]['pose']==[(1,0),3] and set(snap[185]['patch'])=={1}
assert[s[2]for s in eps]==[0,0,3,2,1,0]
protocol=json.loads((P/'RADIAL_SQUARE_ORDERED_PORTS_CHECKED.json').read_text());assert protocol['entry_ports'][:6]==[0,0,3,2,1,0]and protocol['entry_ports'][6]==3
assert snap[5]['patch']=={1:1}and snap[66]['patch']=={1:65}
assert death[1]==25 and all(i in death and death[i]==first[q]for q,i in((q,-i-1)for i,q in enumerate(sorted(seed))))
assert max(death[i]for i in range(-11,0))==52
counts=Counter()
for s,t,v,w in eps[2:]:
 for k,e in enumerate(events[s:t]):
  typ=('inner_L'if k else'outer_L')if e['turn']=='L'else('entry_R'if not k else'exit_R');counts[Q.index(tuple(e['cell'])),typ]+=1
for v in range(4):assert {z:counts[v,z]for z in['inner_L','outer_L','entry_R','exit_R']}==dict(inner_L=2,outer_L=0,entry_R=1,exit_R=1)
S={tuple(q):i for q,i in snap[5]['full_field']};E={tuple(q):i for q,i in snap[66]['full_field']};assert len(S)==14 and len(E)==25
outside=[e for e in events[5:66]if tuple(e['cell'])not in QS];assert len(outside)==45 and sum(e['turn']=='R'for e in outside)==28
# All added BLACK cells were untouched before their displayed first-L use.
guide=[dict(cell=q,initial_identity=-i-1,first_read=first[q],turn=events[first[q]]['turn'])for i,q in enumerate(sorted(seed))];assert all(g['turn']=='L'for g in guide)
fs=['RADIAL_SQUARE_ORDERED_PORTS_MANIFEST.json','RADIAL_SQUARE_PORT_TERMINOLOGY_ADDENDUM.json','../audits/check_radial_square_ordered_ports_independent.json','ORDERED_SQUARE_CIRCULATION_MANIFEST.json','../audits/check_ordered_square_circulation_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR literal finite exterior factor; independent audit pending',seed=sorted(seed),initial_pose=[[0,0],0],physical_updates=185,events=events,full_snapshots={str(t):snap[t]for t in sorted(snap)},complete_factor_end=66,patch=Q,patch_episodes=[dict(start=s,end=t,entry=v,word=w,entry_pose=snap[s]['pose'],exit_pose=snap[t]['pose'])for s,t,v,w in eps],connectors=[dict(start=s,end=t,length=t-s,word=''.join(e['turn']for e in events[s:t]),read_cells=[e['cell']for e in events[s:t]])for s,t in connectors],all_initial_first_reads=guide,guide_final_colors=[dict(cell=q,BLACK=q in E,lifetime=E.get(q))for q in sorted(seed)],all_original_consumed_by=52,inner_cycle=dict(start=5,end=66,old_root_birth=1,old_root_death=25,new_root_birth=65,full_mass_before=14,full_mass_after=25,full_field_xor=sorted(set(S)^set(E)),outside_reads=45,outside_R=28,outside_L=17),next_actual_entry=dict(cut=185,vertex=1,pose=snap[185]['pose'],next_turn='L',required_next_vertex=3),dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='One actual finite protected-patch factor with11 charged original exterior bits. It does not execute the next protocol entry, and no full96-entry, arbitrary repetition or infinite future claim is made.')
(P/'RADIAL_SQUARE_EXTERIOR_FACTOR_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('11 initial cells;66-read factor; first next actual entry185 vertex1 versus required3; XOR',len(out['inner_cycle']['full_field_xor']))
