from pathlib import Path
from itertools import product
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in (D/'DRIFT31_MOD4_WINDING_SHA256SUMS').read_text().splitlines():
 h,f=line.split();assert sha(D/f)==h
J=json.loads((D/'drift31_mod4_winding_cocycle_certificate.json').read_text());weight=(0,1,3,1,2,2,2,3,1,3,0,0);table=[(0,0),(2,0),(3,1),(2,0),(0,0),(2,2),(0,0),(0,2),(3,1),(0,2),(0,0),(0,0)]
psi={(t,h):table[t][i] for t in range(12) for i,h in enumerate((0,2) if t%2==0 else (1,3))};v=(1j,1,-1j,-1);T=lambda z:int(3*z.imag-z.real)
assert list(weight)==J['weight_by_T_mod12'] and {tuple(r['state']):r['value'] for r in J['potential24_states']}==psi
for t in range(-36,37):assert ((-(-t//3))+2*int(t%6==2))%4==weight[t%12]
trans=[]
for (t,h),val in sorted(psi.items()):
 for sig in (-1,1):
  hh=(h+sig)%4;dy=int(v[hh].imag);tt=(t+T(v[hh]))%12;lhs=(psi[tt,hh]-val)%4;rhs=(weight[t]*sig-dy)%4;assert lhs==rhs
  trans.append(dict(source=[t,h],turn_sign=sig,target=[tt,hh],dy=dy,potential_difference=lhs,weighted_turn_minus_dy=rhs))
assert trans==J['all48_transition_checks']
def trace(w,p=0j,h=0):
 start=p;h0=h;ev=[];total=0
 for t,ch in enumerate(w):
  sig=1 if ch=='R' else -1;before=h;total+=weight[T(p)%12]*sig;h=(h+sig)%4
  ev.append(dict(t=t,p=[int(p.real),int(p.imag)],hi=before,ho=h,c=ch));p+=v[h]
 assert (total-(p-start).imag-psi[T(p)%12,h]+psi[T(start)%12,h0])%4==0
 return ev,p-start,h,total%4
counts={}
for length in (6,10,14):
 count=0
 for chars in product('RL',repeat=length):
  _,d,h,total=trace(''.join(chars))
  if d==3+1j and h==0:assert total==1;count+=1
 counts[str(length)]=count
assert counts==J['literal_geometric_controls']=={'6':2,'10':30,'14':420}
stdpath=R/'recovered_bundle/ant_global/root/standard.json';std=json.loads(stdpath.read_text());assert sha(stdpath)==J['actual_standard312_control']['source_sha256']
ev,d,h,total=trace(std['word']*3,1+0j,std['heading']);assert(d,h,total)==(-6-6j,std['heading'],2)
groups=defaultdict(list)
for e in ev:
 x,y=e['p'];k=-(x//6);rep=(x+6*k,y+6*k);groups[rep].append((e['t']-312*k,e))
odd=[]
for q,es in groups.items():
 es.sort();assert [e['c'] for t,e in es]==['R' if i%2==0 else 'L' for i in range(len(es))]
 if len(es)%2:odd.append(q)
assert len(odd)==36 and set(odd)==set(map(tuple,J['actual_standard312_control']['all_odd_class_representatives']))
assert sum(weight[(3*y-x)%12] for x,y in odd)%4==2
# Complete physical prepared6 control, including BLACK-first sign caveat.
r=J['prepared_six_read_control'];ev,d,h,total=trace(r['word']);B={complex(*q) for q in r['initial_black']};p=0j;hh=0
for e in ev:
 assert e['p']==[int(p.real),int(p.imag)] and hh==e['hi'];black=p in B;assert e['c']==('L' if black else 'R')
 if black:B.remove(p)
 else:B.add(p)
 hh=e['ho'];p+=v[hh]
assert ev==r['events'] and sorted((int(q.real),int(q.imag)) for q in B)==list(map(tuple,r['complete_final_black']))
assert (p,hh,d,total)==(3+1j,0,3+1j,1)
wrong=sum(weight[T(complex(*e['p']))%12] for e in ev)%4;assert wrong==r['incorrect_all_WHITE_odd_sum'] and wrong!=total
# Full family algebra follows only from periodic weights, all integer a,c.
for acase in J['parameter_controls']:
 a,c=acase['a'],acase['c'];O=[0,1,2,6,7,6*c+1,6*a+2,6*a+4]
 assert O==acase['full_odd_levels'];z=sum(weight[t%12] for t in O)%4
 assert z==(15+2*c+4*a)%4==(3+2*c)%4==acase['weighted_sum_mod4']
 assert(z==1)==bool(c%2)==acase['passes_necessary_winding']
report=dict(status='PASS all-cap mod4 kinematic cocycle and complete-WHITE FULL-odd winding restriction; middle-short c must be odd',proof_sha256=sha(D/'DRIFT31_MOD4_WINDING_ODD_INVENTORY.md'),author_checker_sha256=sha(D/'certify_drift31_mod4_winding_cocycle.py'),certificate_sha256=sha(D/'drift31_mod4_winding_cocycle_certificate.json'),independent_checker_sha256=sha(S),all48_transitions=trans,geometric_path_counts=counts,standard312=dict(full_drift=[-6,-6],odd_classes=36,odd_weight=2),prepared6=dict(signed_weight=total,incorrect_WHITE_weight=wrong,initial=r['initial_black'],final=r['complete_final_black']),analytic_scope=['All24 physical sector states and both turns exhaust the exact kinematic cocycle; potential telescopes with delta_y. No board legality, period or multiplicity bound enters this identity.','In complete WHITE full-drift histories, alternating R/L startsR and each odd class contributes+1. When3dy-dx=0mod12, w is constant under actual FULL drift; hence the entire odd inventory weighted sum equalsdy mod4. BLACK-first odd classes require minus signs. Primitive drift substitution and cropped odd support are not permitted.','Signed middle-short ownershipO is the FULL8class set. Baseweights9 plus(2c+1)+(2a+3)+(2a+2) give3+2cmod4, so d3,1 forces c odd>=3, witha>=c still unrestricted. No odd-c exclusion, singleusedcircle existence or new controller follows.','Prepared6 is an actual finite factor, not complete WHITE or a finite-seed repeated controller. Standard312 is repeated certified standard with drift-6,-6, not a new primitive or3,1 front.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
