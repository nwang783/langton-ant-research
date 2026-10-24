"""Independent literal replay and complete finite-board periodic-tail arithmetic.
No author simulator, geometry, or tail checker is imported.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'causal_reduction/unit_scale'
A=json.loads((P/'prepared1564_router_crossing.json').read_text());Z=json.loads((P/'prepared1564_router_second_contact.json').read_text());V=((0,1),(1,0),(0,-1),(-1,0))
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H'];assert len(H)==104
seed=set(map(tuple,A['seed']));assert len(seed)==A['initial_mass']==56
B=set(seed);p=(-15,10);h=3;last={};history=[];snap={};snap_times={A['time'],Z['time']};cuts={94896,205680,260802};events={}
for t in range(Z['time']+1):
 if t in snap_times:snap[t]=(set(B),p,h)
 if t==Z['time']:break
 c='L' if p in B else 'R'
 if t in cuts:events[t]=dict(cell=p,heading=h,turn=c,previous=last.get(p))
 last[p]=(t,c);history.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
for a in (A,Z):
 b,q,g=snap[a['time']];assert b==set(map(tuple,a['black'])) and [list(q),g]==a['pose']
assert ''.join(history[A['first_conflict_time']:A['time']])==A['word_from_first_conflict']
assert ''.join(history[Z['contact_time']:Z['time']])==Z['word_from_contact']
assert events[205680]['cell']==(383,380) and events[205680]['turn']=='L' and events[205680]['previous']==(94896,'R')

def periodic(B,p,h,w):
 """Return EXACT earliest mismatch, or None, for w repeated from finite B."""
 start=p;heading=h;reads=[]
 for i,c in enumerate(w):
  reads.append((p,i,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 assert h==heading
 d=p[0]-start[0],p[1]-start[1];assert d!=(0,0);n=len(w)
 def orbit(q):
  axis=0 if d[0] else 1;a=q[axis]%abs(d[axis]);k=(q[axis]-a)//d[axis]
  return (q[0]-k*d[0],q[1]-k*d[1]),k
 groups=defaultdict(list);blacks=defaultdict(set)
 for q,i,c in reads:
  a,k=orbit(q);groups[a].append((i-n*k,k,c))
 for q in B:
  a,k=orbit(q);blacks[a].add(k)
 earliest=None;critical=0
 for a,slots in groups.items():
  slots.sort();lo=min(k for _,k,_ in slots);hi=max(k for _,k,_ in slots)
  levels=set(range(lo,hi+1))|{k for k in blacks[a] if k>=lo}
  free=hi+1
  while free in blacks[a]:free+=1
  levels.add(free)
  for m in levels:
   seq=[(offset+n*m,c)for offset,k,c in slots if k<=m];assert seq
   actual='L' if m in blacks[a] else 'R'
   for time,c in seq:
    if c!=actual:earliest=time if earliest is None else min(earliest,time);break
    actual='R' if actual=='L' else 'L'
   critical+=1
  # Outside the finitely checked eligibility levels and black exceptions,
  # every full slot list starts on white and has precisely the same chronology.
  seq=[c for _,_,c in slots]
  if seq[0]!='R' or any(x==y for x,y in zip(seq,seq[1:])):
   assert earliest is not None
 return earliest,d,groups,critical
reports=[]
for a in (A,Z):
 b,q,g=snap[a['time']];w=a['period_word'];assert w in {H[i:]+H[:i]for i in range(104)}
 mismatch,d,groups,num=periodic(b,q,g,w)
 assert list(d)==a['drift'] and mismatch==a['next_mismatch']
 reports.append(dict(time=a['time'],pose=a['pose'],mass=len(b),drift=d,next_mismatch=mismatch,orbits=len(groups),critical_levels=num))
 if mismatch is not None:
  actual=''.join(history[a['time']:a['time']+mismatch+1]);expected=(w*((mismatch+104)//104))[:mismatch+1]
  assert actual[:-1]==expected[:-1] and actual[-1]!=expected[-1]
# A remote perturbation in every final read orbit must be detected, not missed
# because the certificate tested only a finite number of periods.
b,q,g=snap[Z['time']];w=Z['period_word'];_,d,groups,_=periodic(b,q,g,w);rejected=0
for a in groups:
 cell=(a[0]+1000000*d[0],a[1]+1000000*d[1]);bb=b^{cell};assert periodic(bb,q,g,w)[0] is not None;rejected+=1
out=dict(status='PASS independent complete56-cell trajectory and all-future NW104 capture',source_hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest()for n in ('prepared1564_router_crossing.json','prepared1564_router_second_contact.json')},initial_pose=[[-15,10],3],initial_mass=56,literal_updates=Z['time'],selected_events=events,tail_checks=reports,far_flip_controls=rejected,scope='One supplied finite seed. First desired crossing fails at205680, later NE flight has an exact finite next contact at260802, and NW standard capture is certified from276536. No all-parameter itinerary or finite preparation of the1564 wave is inferred.')
Q=Path(__file__).with_suffix('.json');Q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
