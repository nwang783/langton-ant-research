from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(D/'DRIFT31_EVEN_GAP_TRANSFER_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(D/f.strip())==h
J=json.loads((D/'drift31_even_gap_transfer_certificate.json').read_text());A=((1,-2,2),(2,0,1),(1,1,-1));mul=lambda a,b:tuple(tuple(sum(a[i][k]*b[k][j]for k in range(3))for j in range(3))for i in range(3));mv=lambda v:tuple(sum(a*b for a,b in zip(row,v))for row in A)
assert mul(mul(A,A),A)==((-3,0,0),(0,-3,0),(0,0,-3))
# Enumerate R/L rank allocations, not the author's m/r/l search.
controls=0
for I,J0 in product(range(12),repeat=2):
 actual_even=set();actual_odd=set()
 for nr in range(I+1):
  nl=I-nr
  for sr in range(I+J0+1):
   sl=nr+sr-nl
   if sl<0:continue
   m=nr+sr
   if nr+sl==J0:actual_even.add((m,nl))
   if sr+nl==J0:actual_odd.add((m,nl))
 even={(J0-I+2*h,h)for h in range(max(0,(2*I-J0+2)//3,I-J0),I+1)}
 odd={(I+J0-2*l,l)for l in range(min(I,J0,(I+J0)//3)+1)}
 assert actual_even==even and actual_odd==odd;controls+=1
 # Formulae give four nonnegative rank bin counts and exact incoming/outgoing totals.
 for m,h in even:assert min(I-h,h,J0-2*I+3*h,J0-I+h)>=0 and m<=I+J0
 for m,l in odd:assert min(I-l,l,J0-l,I+J0-3*l)>=0 and m<=I+J0
count=0
for w,n,s in product(range(9),repeat=3):
 u=w+n-s
 if u<0:continue
 for l in range(min(w,s,(w+s)//3)+1):
  e=2*s+w-4*l;nn=s+2*w-4*l
  for h in range(max(0,(2*n-e+2)//3,n-e),n+1):
   ww=e-2*n+4*h;ss=2*e-3*n+4*h;v=(ww,nn,u);expected=mv((w,n,s));assert v==(expected[0]+4*(h-l),expected[1]-4*l,expected[2])and ww+nn-u==ss and min(*v,ss)>=0;count+=1
assert controls==J['local_count_formula_control_pairs']and count==J['two_cell_transfer_controls']
cycles=[];seen=set()
for v in product(range(4),repeat=3):
 if v in seen:continue
 cycle=[];a=v
 while a not in seen:cycle.append(a);seen.add(a);a=tuple(x%4 for x in mv(a))
 assert a==v;cycles.append(cycle)
assert cycles==[[tuple(v)for v in cyc]for cyc in J['all64_residue_states_as_cycles']]
assert Counter(map(len,cycles))=={1:4,3:20}
V={'N':1j,'E':1,'S':-1j,'W':-1};inv={v:k for k,v in V.items()};out=lambda w:[inv[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)];fullD=3+1j
phase=lambda p:int(p.real)%2 if int(p.imag)%2==0 else 3-int(p.real)%2
family=[]
for z in J['literal_family_controls']:
 k=z['k'];hs=['NNSS'*k,'EEWW'*k,'NNSS'*k];T=[[128*b+t for b in range(k)for t in ts]for ts in([60,64,96,100],[1,33,65,97],[0,4,8,32])];P=128*k+2;assert z['clocks_at_representatives']==T and z['period_parameter']==P
 nodes=[(i,r)for i,w in enumerate(hs)for r in range(len(w))];succ={}
 for i,w in enumerate(hs):
  assert all(T[i][r+1]-T[i][r]>=4 and(T[i][r+1]-T[i][r])%4==0 for r in range(len(w)-1))
  for lift in range(-9,10):assert all((t+lift*P)%4==phase(-i+lift*fullD)for t in T[i])
  for h in V:
   p=-i+V[h];j=int(3*p.imag-p.real);vol=int(p.imag)
   if j not in(0,1,2):continue
   sr=[r for r,hh in enumerate(out(w))if hh==h];rr=[r for r,hh in enumerate(hs[j])if hh==h];assert len(sr)==len(rr)
   for r,t in zip(sr,rr):succ[i,r]=(j,t,vol);assert T[j][t]+vol*P==T[i][r]+1
  assert Counter(w)==Counter({h:2*k for h in('NS'if i%2==0 else'EW')})and Counter(out(w))==Counter({h:2*k for h in('EW'if i%2==0 else'NS')})
 assert len(succ)==4*k and all((j,t)not in succ for j,t,vol in succ.values())and len(set(sum(T,[])))==12*k
 assert min(sum(T,[]))==0 and max(sum(T,[]))==128*k-28<P
 assert len(nodes)-len(succ)==8*k and P-len(nodes)==116*k+2;family.append(dict(k=k,P=P,internal_edges=len(succ),chains=len(nodes)-len(succ)))
outj=dict(status='PASS exact even-gap integer transfer/residue projection and unbounded OPEN clock family only',proof_sha256=sha(D/'DRIFT31_EVEN_GAP_TRANSFER_SEMANTICS.md'),bindings_sha256=sha(D/'DRIFT31_EVEN_GAP_TRANSFER_SHA256SUMS'),matrix_cube=[[-3,0,0],[0,-3,0],[0,0,-3]],local_count_controls=controls,transfer_controls=count,residue_cycle_counts=dict(Counter(map(len,cycles))),literal_controls=family,analytic_review=[
'Even vertical N/R=I-h,N/L=h,S/R=J-2I+3h,S/L=J-I+h and odd horizontal W/R=I-l,W/L=l,E/R=J-l,E/L=I+J-3l derive all admissible integer intervals by nonnegativity. Every bin allocation has an alternating-position word, but chronology is not implied. Empty allzero cell is allowed at count level.',
'At the even-level cut, parity-sector orientation leaves precisely W_t,N_(t-1) crossing forward and S_(t+1),S_(t+3) backward. Complete finite read support and balanced actual traffic give w+n-s-u=0. Processing odd then even gives displayed integer map and A^3=-3I, hence three-step residue period, not integer-state finiteness.',
'Formulae valid for every k>=1: named clocks occupy twelve disjoint residues per128block and lie in0..P-1; P mod4=2 equals the phase shift of full drift(3,1). Four exact internal ordinal edges perblock have zero voltage and +1clock; every remaining port is UNKNOWN. The graph has8k open chains and no internal cycle.',
'The open family is not a finite physical factor, complete WHITE front, controller, g8 prefix-reachable state or counterexample to attraction. Zero odd output on a partial band is not a zero-output whole front.',
'The list of exact boundary metadata is understood as sufficient data for faithful explicit ordinal transfer, not a proved lower bound on all possible representations. No impossibility of every finite quotient is inferred from the unbounded displayed family.'
]);S.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status']);print(sha(S.with_suffix('.json')))
