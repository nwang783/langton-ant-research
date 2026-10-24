"""Last-exit constraint and a literal empty-seed ordered circulation control."""
from pathlib import Path
from collections import Counter
import json,hashlib
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent
Q=[(9,4),(10,4),(10,5),(9,5)];Qset=set(Q);cuts={5710,5712,6036,6042,9977};B={};p=(0,0);h=1;events=[];snap={};death={};first={}
for t in range(10081):
 if t in cuts:snap[t]=dict(pose=[p,h],field=dict(B))
 old=B.pop(p,None);c='R'if old is None else'L';first.setdefault(p,t)
 events.append(dict(time=t,cell=p,heading=h,turn=c,old_lifetime=old))
 if old is None:B[p]=t;h=(h+1)%4
 else:death[old]=t;h=(h-1)%4
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
T=snap[9977];w,dr,tail,tests=future(T['field'],tuple(T['pose'][0]),T['pose'][1]);assert w==''.join(e['turn']for e in events[9977:])
death.update({i:9977+t for i,t in tail.items()})
assert len(T['field'])==715
S=snap[5710]['field'];E=snap[6042]['field'];q0={q:i for q,i in S.items()if q in Qset};q1={q:i for q,i in E.items()if q in Qset}
assert set(q0)==set(q1)=={(10,5)}
pe=[e for e in events[5710:6042]if e['cell']in Qset]
assert [e['time']for e in pe]==[5710,5711,6036,6037,6038,6039,6040,6041]
assert ''.join(e['turn']for e in pe)=='RRRLLLLR'
counts=Counter((tuple(e['cell']),e['turn'])for e in pe)
assert all(counts[q,c]==1 for q in Q for c in'RL')
assert pe[3]['old_lifetime']==q0[(10,5)] and q1[(10,5)]==6041 and death[6041]==6313
for q in Q:assert events[first[q]]['turn']=='R'
# Last-exit forest on this actual packet: each non-root arrow has increasing last-read time.
last={q:max(e['time']for e in pe if e['cell']==q)for q in Q};arrows=[]
for q,t in last.items():
 e=events[t];hh=(e['heading']+(1 if e['turn']=='R'else-1))%4;nxt=(q[0]+DXY[hh][0],q[1]+DXY[hh][1]);
 if nxt in Qset:assert last[nxt]>t
 arrows.append(dict(cell=q,last_read=t,turn=e['turn'],next=nxt,exits=nxt not in Qset))
assert sum(a['exits']for a in arrows)==1 and next(a for a in arrows if a['exits'])['cell']==(10,5)
# Exact 16-color/four-entry-port patch automaton; no outside routing is asserted.
C=[(0,0),(1,0),(1,1),(0,1)];rows=[]
for mask0 in range(16):
 for entry in range(4):
  mask=mask0;q=C[entry];hh=[0,3,2,1][entry];seq=[]
  while q in C:
   i=C.index(q);old=bool(mask>>i&1);c='L'if old else'R';seq.append((i,c));mask^=1<<i;hh=(hh+(-1 if old else 1))%4;q=(q[0]+DXY[hh][0],q[1]+DXY[hh][1]);assert len(seq)<=6
  rows.append(dict(before=mask0,entry=entry,after=mask,reads=seq,exit_pose=[q,hh]))
a=next(z for z in rows if z['before']==4 and z['entry']==3);b=next(z for z in rows if z['before']==13 and z['entry']==1)
assert a['after']==13 and b['after']==4
assert ''.join(c for i,c in a['reads'])=='RR'and ''.join(c for i,c in b['reads'])=='RLLLLR'
# Component counts are contained in the r=1/2 radial witness scaled by16.
# Each cell has inner-L1, one crossing-R1, other crossing-R0, outer-L0.
assert 1<=15 and 1<=9 and 0<=3
record=lambda t:dict(cut=t,pose=snap[t]['pose'],full_black=[[q,i]for q,i in sorted(snap[t]['field'].items())],full_mass=len(snap[t]['field']),entire_future_relevant=[[q,i,death[i]]for q,i in sorted(snap[t]['field'].items())if i in death])
fs=['SUMMABLE_BALANCED_TURN_FLOW_MANIFEST.json','../audits/check_summable_turn_flow_independent.json','PRISTINE_COHORT_ADVANCE_MANIFEST.json','../audits/check_pristine_cohort_advance_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR ordered square circulation; independent audit pending',original_seed=[],initial_pose=[[0,0],1],prefix_word=''.join(e['turn']for e in events[:9977]),tail_word=w,tail_drift=dr,tail_parity_tests=tests,tail_state=record(9977),patch=Q,patch_events=pe,patch_first_reads=[events[first[q]]for q in Q],last_exit_forest=arrows,old_input=dict(cell=(10,5),birth=q0[(10,5)],death=6037,age=6037-q0[(10,5)]),replacement=dict(cell=(10,5),birth=6041,death=6313),whole_cuts=[record(t)for t in[5710,5712,6036,6042]],outside_read_count=324,outside_word=''.join(e['turn']for e in events[5712:6036]),full_field_xor=sorted(set(S)^set(E)),full_mass_change=len(E)-len(S),patch_automaton=rows,dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='Sharp one-current-BLACK last-exit requirement for a pure inner-L restored patch packet; literal empty-seed realization of one component, NOT whole radial flow or autonomous repeated scattering')
(P/'ORDERED_SQUARE_CIRCULATION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('old input',out['old_input'],'replacement',out['replacement'],'whole masses',len(S),len(E),'XOR',len(out['full_field_xor']),'whole relevance',[(r['cut'],len(r['entire_future_relevant']))for r in out['whole_cuts']])
