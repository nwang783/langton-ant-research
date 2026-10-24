from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);D=S.parents[1]/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'DRIFT31_COMPLETE_ADDITIVE_COCYCLE_CLASSIFICATION.md';assert sha(F)=='3f8a2a32350be902d822dc1c9a0469bad9fe2cd0be009a530e33db2c165134ee'
C=D/'drift31_complete_additive_cocycles_certificate.json';assert sha(C)=='f56008b01ee46c1969705dd97c2d6957110292a6ee8e5d59085ec198c7b47467';J=json.loads(C.read_text());vec=(1j,1,-1j,-1);group=defaultdict(list);seen=set();trans=0;failed=Counter()
# Reconstruct independently from explicit coefficient forms, not producer recurrence.
for x0,x1,x2,y0,rho in product(range(4),repeat=5):
 x=[x0,x1,x2];ys=[y0,y0+2*(x1+x0+rho),y0+2*(x2+x0)];ys+= [q+2*rho for q in ys]
 A=lambda t:(x[(t//2)%3]if t%2==0 else ys[(t//2)%6])%4
 W0=[y0+x0+2*x2+2*rho,y0-x2-rho,y0-x1,y0+x0+2*x1+rho,y0+2*x0+2*x1-x2+2*rho,y0+2*x0-x1+2*x2-rho]
 W=lambda t:(W0[t%6]+(t//6)*2*rho)%4
 psi=lambda t,h:(A(t)+(2*W(t)if h!=t%2 else 0))%4
 for t in range(12):
  assert W(t)==((A(t-1)-A(t))if t%2==0 else(A(t)-A(t+3)-rho))%4
  for h in(t%2,t%2+2):
   for sg in(-1,1):
    hn=(h+sg)%4;v=vec[hn];tn=t+int(3*v.imag-v.real)
    assert (psi(tn,hn)-psi(t,h)-W(t)*sg+rho*int(v.imag))%4==0;trans+=1
 # Both eliminated infinite recurrences, tested without reducing their indices by producer tables.
 for j in range(-9,10):
  assert(A(2*(j+2))-A(2*(j-1))-2*A(2*j+1)+2*A(2*(j-2)+1))%4==0
  assert(3*A(2*j+1)-2*A(2*(j+2))-2*rho-2*A(2*j)+A(2*(j-1)+1))%4==0
 row=next(r for r in J['models']if r['x']==x and r['y0']==y0 and r['rho']==rho)
 weights=[W(t)for t in range(12)];pot=[[t,h,psi(t,h)]for t in range(12)for h in(t%2,t%2+2)]
 assert weights==row['weights_T_mod12']and pot==row['potential24'];seen.add(tuple(x+[y0,rho]));group[rho,tuple(weights)].append(pot)
 for cp,ap in product(range(2),repeat=2):
  # Choose genuine ordered distinct full inventories for every parity combination.
  c=2+cp;a=c+((ap-c)%2);O=[0,1,2,6,7,6*c+1,6*a+2,6*a+4];assert len(set(O))==8 and 2<=c<=a
  residual=(sum(W(t)for t in O)-rho)%4;assert residual==2*rho*(c+1)%4;failed[cp,ap]+=bool(residual)
assert len(seen)==1024 and len(group)==256 and trans==49152
for members in group.values():
 assert len(members)==4
 for q in members:
  dif={(v-w)%4 for(_,_,v),(_,_,w)in zip(q,members[0])};assert len(dif)==1
assert dict(failed)=={(0,0):512,(0,1):512,(1,0):0,(1,1):0}
# Formal coefficient cancellation in variables(x0,x1,x2,y0,rho), using unit basis evaluations.
coeff=[]
for t in range(12):
 vals=[]
 for k in range(5):
  z=[int(j==k)for j in range(5)];a,b,c,y,r=z;base=[y+a+2*c+2*r,y-c-r,y-b,y+a+2*b+r,y+2*a+2*b-c+2*r,y+2*a-b+2*c-r];vals.append((base[t%6]+2*r*(t//6))%4)
 coeff.append(vals)
for c,a in product(range(2),repeat=2):
 O=[0,1,2,6,7,6*c+1,6*a+2,6*a+4];r=[(sum(coeff[t%12][k]for t in O)-int(k==4))%4 for k in range(5)];assert r==[0,0,0,0,2*(c+1)%4]
out=dict(status='PASS complete universal additive Z4 position/signed-turn cocycle ansatz on full(3,1) quotient',proof=sha(F),producer=sha(D/'certify_drift31_complete_additive_cocycles.py'),certificate=sha(C),potential_models=1024,weight_winding_pairs=256,checked_transitions=trans,constant_gauge_multiplicity=4,full_inventory_residual_coefficients='[0,0,0,0,2*(c+1)] in x0,x1,x2,y0,rho',analytic_review=[
'Full(3,1) is primitive and equalT means exact integer multiple of(3,1), so arbitrary invariant position functions really are functions of T. The specified sector is preserved by every allowed move.',
'Four move equations give B-A=2w and even/odd neighbor equations with rho vertical signs. Eliminating B gives both displayed infinite-index equations. Substituting one into the other modulo4 yields dy_j=2(x_j+x_(j-1)+rho), without dividing by2.',
'Every dy_j is even, hence2(y_j-y_(j-2))=0. Thus x_(j+2)=x_(j-1) on all integers. Summing3increments gives y_(j+3)-y_j=2rho. This forces Tperiod12; no finite spatial period was assumed. Four free initial potentials plusrho determine all integerindices in both directions.',
'Independent closed coefficient forms recover all1024 potentials and49152 moves, agreeing with complete certificate. Each(w,rho) has exactly4 constant-gauge potentials. Sufficiency holds at every integerT by forcedperiodicity.',
'CompleteWHITE full-class signed turn sums are1 for odd and0 for even histories. On the full owned middle-short eight-class set, all four potential parameters and all a terms cancel, leaving2rho(c+1). Thus c odd passes EVERY stated cocycle; no wider invariant or controller classification is asserted.',
'BLACK-first odd classes require negative weights. The count-only296-read aside is not a proof premise or a physical transfer realization. Chronology,rank,board/nonlinear and additional multiplicity terms remain outside this exhausted ansatz.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
