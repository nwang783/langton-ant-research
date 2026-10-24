from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import hashlib,json
ROOT=Path('/workspace/shared/langton');P=ROOT/'causal_reduction/unit_scale';D=ROOT/'new_constructive_2026-10-23';SELF=Path(__file__).resolve();word=json.loads((P/'prepared4352_output_return_wave.json').read_text())['word'];base={tuple(q)for q in json.loads((P/'prepared15324_return_normal_form.json').read_text())['bulk_mod26']};I={(t,a+26*k)for t,a in base for k in range(3)}
p=13+7j;h=0;dirs=(1j,1,-1j,-1);balance=Counter()
for c in word:
 balance[int(p.real-p.imag),int(p.real)%78]+=1 if c=='R'else-1
 h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
assert(p,h)==(-65-71j,0);assert all(n in(-1,0,1)for n in balance.values())
O=set(I)
for q,n in balance.items():
 assert int(q in I)+n in(0,1)
 if n:O.symmetric_difference_update({q})
assert len(I)==2892 and len(O)==3300
# Exact polynomial coefficients in w=4^(c-t) of the rotated local clock.
# Field coefficient sigma*(-1)^t=(-1)^h, J uses heading h+1 after CW rotation.
A=(F(1,3),F(1,3),F(-4,3),F(-4,3));local=[]
for hh,c in product(range(4),'RL'):
 turn=1 if c=='R'else-1;nh=(hh+turn)%4;step=dirs[nh];dt=int(step.real-step.imag);sgn=(-1)**hh*turn
 cw=6*sgn+6*A[(nh+1)%4]*F(4)**(-dt)-6*A[(hh+1)%4]
 ci=6*sgn+6*A[(nh+3)%4]*F(4)**dt-6*A[(hh+3)%4]
 const=-2*sgn;assert(cw,ci,const)in[(0,0,2),(2,22,-2),(22,2,-2)]
 local.append(dict(h=hh,turn=c,w_coeff=int(cw),inverse_w_coeff=int(ci),constant=const))
def f(t,c):return 6*(F(4)**(t-c)+F(4)**(c-t))-2
def phi(S,n,c,sigma=1):return sum((sigma*(-1 if t%2 else 1)*f(t,c)*F(count,n)for t,count in Counter(t for t,a in S).items()),F(0))
rat=lambda q:[q.numerator,q.denominator];checks=[]
for center in(0,9,14):
 delta=phi(O,78,center)-phi(I,78,center);assert delta>=F(2*len(word),78)
 # Sum literal local weights independently. Head telescopes since normal/head return.
 direct=sum(((-1 if t%2 else 1)*f(t,center)*n for(t,a),n in balance.items()),F(0));assert direct==78*delta and direct>=2*len(word)
 for mult in(2,3,5):
  il={(t,a+78*k)for t,a in I for k in range(mult)};ol={(t,a+78*k)for t,a in O for k in range(mult)}
  assert phi(il,78*mult,center)==phi(I,78,center)and phi(ol,78*mult,center)==phi(O,78,center)
 assert phi(I,78,center,-1)-phi(O,78,center,-1)==delta
 checks.append(dict(center=center,delta=rat(delta),lower=rat(F(2*len(word),78))))
values=[sum(((-1 if t%2 else 1)*f(t,0)*bit for t,bit in zip(range(-2,3),bits)),F(0))for bits in product((0,1),repeat=5)]
assert max(values)-min(values)==sum((f(t,0)for t in range(-2,3)),F(0))
ref=json.loads((D/'profile_density_clock.json').read_text())
for x,y in zip(checks,ref['controls']):assert x['center']==y['fixed_normal_center']and x['delta']==[y['forward_delta']['numerator'],y['forward_delta']['denominator']]
note=D/'profile_density_clock.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='723bd11f026a4fdbb0327fbc6e6e0586955e578619527fefea89e4aeb286d676'
out=dict(status='PASS independent normalized complete-profile scalar-clock theorem',note_sha256=sha,exact_eight_local_coefficients=local,complete_input_classes=len(I),complete_output_classes=len(O),controls=checks,proof='For any common longitudinal multiple L, k=L/|s| repeats contribute at least2kP. Heading and normal return cancel all J terms. Complete alternating orbit histories give net O-I, including unchanged passive orbits. The weighted sum is L times density potential change, yielding deltaPhi>=2P/|s|>=4.',scope='Fixed physical oblique axis, sector, normal anchor, complete mature periodic profiles and legitimate translating-interface contracts. Finite caps/transients do not change bulk. No profile cycle or same-sector exact bulk reset; fixed normal support gives finite number of complete phases. Not a finite-board rank, finite endpoint transient bound, global capture or existence statement.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(local)
