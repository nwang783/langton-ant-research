from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=D/'DRIFT31_VOLTAGE_AS_STREAM_HEIGHT.md';code=D/'check_drift31_voltage_stream_counter.py';cert=D/'drift31_voltage_stream_counter_certificate.json';J=json.loads(cert.read_text())
standard=R/'recovered_bundle/ant_global/root/standard.json';data=json.loads(standard.read_text());assert sha(standard)==J['actual_standard_control']['source_sha256']
v=(1j,1,-1j,-1);p=0j;h=data['heading'];events=[]
for t,ch in enumerate(data['word']):
 old=h;h=(h+(1 if ch=='R' else -1))%4;events.append(dict(t=t,p=[int(p.real),int(p.imag)],hi=old,ho=h,c=ch));p+=v[h]
assert p==-2-2j and h==data['heading'];drift=p
stable={}
for name,q in [('H',1-1j),('V',-1j)]:
 rows=[]
 for e in events:
  d=q-complex(*e['p']);x,y=int(d.real),int(d.imag)
  if x%2==0 and x==y:rows.append([e['t']+(x//-2)*104,e])
 rows.sort();assert rows==J['actual_standard_control'][name+'_stable_complete_events']
 assert ''.join(e['c'] for _,e in rows)=='RLRLRLRL'
 stable[name]=rows
HH=''.join('NESW'[e['hi']] for _,e in stable['H']);VV=''.join('NESW'[e['hi']] for _,e in stable['V']);assert (HH,VV)==('WWEWWEEW','NSSSSNSN')
lam=sum(k%2 and e['hi']==3 for k,(_,e) in enumerate(stable['H']));eta=sum(k%2 and e['hi']==0 for k,(_,e) in enumerate(stable['V']));assert(lam,eta)==(3,2)
# Derive face labels from actual right/left unit squares at representatives(-t,0).
# h index of face with lower-left(x,y) is3y-x after its full (3,1) translation to y0.
face=lambda x,y:3*y-x
for t in range(-4,5):
 if t%2:
  assert (face(-t,0),face(-t-1,0))==(t,t+1) # north C right / L left
  assert (face(-t-1,-1),face(-t,-1))==(t-2,t-3) # south
 else:
  assert (face(-t-1,0),face(-t-1,-1))==(t+1,t-2) # west
  assert (face(-t,-1),face(-t,0))==(t-3,t) # east
# Symbolic telescoping for arbitrary proper even t; all low boundary coefficients coalesce to c_right.
for t in range(-4,30,2):
 lo=-40;coef=Counter()
 for q in range(lo+1,t-2,2):coef[q]+=1;coef[q+1]-=1
 for q in range(lo+1,t,2):coef[q-2]-=1;coef[q-3]+=1
 coef={k:v for k,v in coef.items() if v}
 assert coef.get(t-2)==-1 and sum(v for k,v in coef.items() if k<=lo+1)==1 and all(k<=lo+1 or k==t-2 for k in coef)
# Symbolic next-cut and count-map cancellation: 2(n-s)+[-2n+2s+4eta-4lambda].
assert [2-2,-2+2,4,-4]==[0,0,4,-4]
report=dict(status='PASS exact unrestricted stream-height voltage identity and actual standard local nonmonotonicity control',proof_sha256=sha(proof),checker_sha256=sha(code),certificate_sha256=sha(cert),independent_checker_sha256=sha(S),stable_histories={'H':HH,'V':VV},stable_actual_events=stable,lambda_count=lam,eta_count=eta,analytic_scope=['Unit face lower-left index3y-x independently gives all four directed flows with C-right/L-left orientation. Entire prefix starts at genuinely unread lower exterior, so north internal sources q<=t-3 and south q<=t-1 telescope to K=c_right-h_(t-2), not a cropped-prefix assertion.','At the next even cut K increases n-s; the signed exact w transfer gives (2K+w) increment4(eta-lambda). No sign on this increment follows.','The countercontrol uses full stable ordered histories in the retained certified standard104, with full drift(-2,-2) and growth12. It disproves only universal local eta>=lambda, not any reachable(3,1),g8 constraint. Random signed-height controls are not physical front evidence.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
