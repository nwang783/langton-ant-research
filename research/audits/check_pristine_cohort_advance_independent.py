from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=json.loads((P/'PRISTINE_COHORT_ADVANCE_MANIFEST.json').read_text())
for f,h in m.items():assert sha(P/f)==h
assert m['PRISTINE_COHORT_ADVANCE.md']=='b361f8d32db5005bf934519453bbf7d38d8aecf53410302ac3fb1efd34c04721'
ref=json.loads((P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').read_text());V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];dot=lambda p,n:int(p.real)*n[0]+int(p.imag)*n[1]
B=set();birth={};p=0j;h=0;events=[];words=[];norms=[(0,1),(1,1),(-1,1)];mx={n:-1 for n in norms};records={n:[]for n in norms};TB=None
for t in range(9977+104):
 if t==9977:TB=set(B);tp=p;th=h
 for n in norms:
  a=dot(p,n)
  if a>mx[n]:mx[n]=a;records[n].append(dict(time=t,head=xy(p),heading=h,height=a,preceding_event=events[-1]if events else None))
 c='L'if p in B else'R';ev=dict(time=t,cell=xy(p),incoming=h,turn=c,consumed_birth=birth.get(p));events.append(ev);words.append(c)
 if c=='L':B.remove(p);del birth[p]
 else:B.add(p);birth[p]=t
 h=(h+(1 if c=='R'else-1))%4;p+=V[h]
word=''.join(words);assert word[:9977]==ref['blank_prefix']and word[9977:]==ref['blank_tail_word'];assert events[:9977]==ref['full_blank_prefix_events'];assert TB=={complex(*z)for z in ref['blank_tail_state']['black']}and len(TB)==715 and(tp,th)==(-15+10j,3);H=word[9977:];d=p-tp;assert d==-2-2j and h==th
standard=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert any(H==standard[i:]+standard[:i]for i in range(104))
q=[complex(*e['cell'])for e in events[9977:]]
def multiple(z,d):
 a=F(z.real/d.real)if d.real else F(z.imag/d.imag)
 return int(a)if a.denominator==1 and int(a)*d==z else None
from fractions import Fraction as F
# Independent all-n phase/ray parity, every integer change point included.
cert=[]
for i,x in enumerate(q):
 old=set()
 for b in TB:
  n=multiple(b-x,d)
  if n is not None and n>=0:old.add(n)
 steps=[];const=0
 for j,y in enumerate(q):
  k=multiple(x-y,d)
  if k is None:continue
  if k<0:steps.append(-k)
  elif k==0 and j<i:const^=1
 tests={0,*steps,*old,*[n+1 for n in old]}
 for n in tests:
  color=((n in old)+const+sum(n>=s for s in steps))%2;assert color==(H[i]=='L'),(i,n,color,H[i])
 cert.append(dict(phase=i,initial_black_epochs=sorted(old),earlier_period_thresholds=sorted(steps),same_epoch_parity=const,checked_epochs=sorted(tests)))
bounds=[]
for n,want in zip(norms,(22,35,34)):
 pref=max(dot(complex(*e['cell']),n)for e in events[:9977]);tailmax=max(dot(x,n)for x in q);adv=dot(d,n);assert adv<=0 and max(pref,tailmax)==want
 rr=next(z for z in ref['bounds']if z['normal']==list(n));assert(pref,tailmax,adv)==(rr['prefix_maximum'],rr['tail_maximum'],rr['tail_projection_advance']);assert records[n]==rr['all_strict_blank_records'];bounds.append(dict(normal=n,prefix_maximum=pref,tail_maximum=tailmax,tail_projection=adv,exact_future_maximum=want,records=records[n]))
assert len(records[(0,1)])==23 and records[(0,1)][-1]['time']==9460
caps=[z for z in records[(1,1)]if z['height']%2==0];assert len(caps)==18;sponsors=[]
for z in caps[1:]:
 e=z['preceding_event'];b=e['consumed_birth'];assert e['turn']=='L'and b is not None and events[b]['turn']=='R'and events[b]['cell']==e['cell'];assert z['heading']==0 and sum(e['cell'])==z['height']-1>=1
 # The alleged birth-to-death interval is a genuine unchanged lifetime.
 assert all(a['cell']!=e['cell']for a in events[b+1:e['time']])
 row=dict(new_cap_first_level=z['height'],record_time=z['time'],record_pose=[z['head'],z['heading']],sponsor_cell=e['cell'],sponsor_birth=b,sponsor_consumption=e['time'],entire_lifetime_initially_in_virgin_halfplane=True);sponsors.append(row)
assert sponsors==ref['first_phase_diagonal_cap_sponsors']
def prep(B,p,h,w):
 B=set(B);positions=[p]
 for c in w:
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];positions.append(p)
 return B,p,h,positions
b,p,h,ps=prep({-1j},-1j,1,'L');assert not b and(p,h)==(0j,0)and max(x.imag for x in ps[:-1])<0
b,p,h,ps=prep({-1-1j,-1j},-1-1j,2,'LL');assert not b and(p,h)==(0j,0)and max(dot(x,(1,1))for x in ps[:-1])<0
out=dict(status='PASS unrestricted pristine entry-cohort advance22/35/34 with exact complete blank tail and scoped resource ledger',note_sha256=m['PRISTINE_COHORT_ADVANCE.md'],blank_prefix_reads=9977,tail_full_mass=715,tail_pose=[xy(tp),th],tail_drift=xy(d),all104_infinite_ray_certificates=cert,bounds=bounds,all17_fresh_side_sponsors=sponsors,analytic_review=[
'For any complete finite current black set B and WHITE head, couple to the blank ant at the same pose. Before the first actual read of any B cell, read positions/turns agree and the XOR field is exactly untouched B. At first contact the blank has never read that cell, hence expects R while actual L consumes the SAME entry-cohort lifetime. This covers all physical words, including self-written revisits, without a parser or age theorem.',
'Independent9977+104 physical replay agrees with every supplied event/birth. The complete715-cell state at(-15,10),W has exact infinite cyclic-standard104 continuation with drift(-2,-2), checked by per-phase integer-ray parity at every possible change point. The tail never raises the three indicated projections; exact global blank maxima are22,35,34, not a finite-scan inference.',
'At a pristine north record all old cohort lies y<0, so row23 requires a prior old-cohort L. The two normalized diagonal orientations similarly require old input before level36 or35. Proper rotations transfer directions. These are outward-advance bounds only, not elapsed-time, total-travel or old-substrate cardinality bounds.',
'The one-L and two-LL finite preparations reach a genuine pristine empty cut and establish sharp22/35 maxima. All17 later even-level NE cap sponsors are actual R-born lifetimes on initially virgin levels1..33; births, no intermediate reads and L consumption immediately before the new cap are checked. The two halves of one fresh pair are not distinct external fundings.',
'For unbounded north records, first-hit cuts at h0+23j are pristine and have incomingN. The bound forces an entry-present lifetime to die strictly before the next cut, so selections from disjoint blocks are distinct. Every selected noninitial identity was born in an earlier finite block; finite initial cohort and finite branching allow an infinite ancestry ray rather than a contradiction. Replenishment, capture and eventual standard motion remain compatible with this statement.',
'This unrestricted first-old-input coupling does not extend DCUV funding ages to arbitrary words, nor show a finite global record budget or attraction. Full old field and fresh outputs must remain after each contact.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('raytests',sum(len(z['checked_epochs'])for z in cert),'sponsors',len(sponsors))
