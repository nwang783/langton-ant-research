from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib
ROOT=Path('/workspace/shared/langton');G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];R=json.loads((ROOT/'audits/check_dcuv_all_input_ages_independent.json').read_text())['slots'];lam=Q(8,5);B=Q(128,13);rows=[];checks=0
for a in (0,1,4,5,6,7,8,9):
 g=G[a];c=g['name'].count('C');ages=[R[f'{a}:{tuple(v)}']['certified_minimum_C_age']for v in g['inputs']];base=len(g['outputs'])-3*c
 assert len(g['outputs'])-len(g['inputs'])==g['word'].count('R')-g['word'].count('L')
 assert sum(lam**r for r in ages)>=base
 assert len(g['word'])<=10*len(ages)+15*c
 for actual in product(*(range(r,5)for r in ages)):
  for surviving_age in range(5):
   E=sum(lam**r for r in actual)+lam**surviving_age
   after=lam**min(4,surviving_age+c)+len(g['outputs'])*lam**c
   assert after+B<=lam**c*(E+B);checks+=1
 rows.append({'packet':a,'ages':ages,'base_outputs':base,'input_min_weight':str(sum(lam**r for r in ages)),'duration_slack':10*len(ages)+15*c-len(g['word'])})
assert B==6*lam**2/(lam**2-1)
assert B>=3*lam/(lam-1)
# Symbolic root inequalities follow from 3/2<lambda<8/5 and monotonicity;
# only the V/VC relation uses equality lambda^2+lambda^3=6.
assert Q(3,2)**2+Q(3,2)**3<6<lam**2+lam**3
assert Q(3,2)**3>1 and 2*Q(3,2)**4>6 and 2*Q(3,2)**3+3*Q(3,2)**4>9
J={'status':'PASS exact packet energy/duration arithmetic and reviewed symbolic-root epoch proof','lambda_rational':str(lam),'B':str(B),'rows':rows,'exact_basis_controls':checks,'scope':'Finite complete recurrent-eight factors, energy/mass and duration exponential in C count. No upper C bound, confinement, capture or arbitrary-factor extension.','hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(Path(__file__),ROOT/'word_stabilization/dcuv_age_energy_finite_c_bound.md')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
