#!/usr/bin/env python3
"""Exact controls for normalized complete-profile strict-clock corollary.
All-period theorem is analytic; no solver, word search or horizon is used.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
P=Path('/workspace/shared/langton/causal_reduction/unit_scale');O=Path(__file__).parent
NF=json.loads((P/'prepared15324_return_normal_form.json').read_text());W=json.loads((P/'prepared4352_output_return_wave.json').read_text())['word'];D=((0,1),(1,0),(0,-1),(-1,0));I={(t,a)for t,b in NF['bulk_mod26']for a in range(b,78,26)};T=set();p=(13,7);h=0
for c in W:
 j=p[0]-p[1],p[0]%78
 if j in T:T.remove(j)
 else:T.add(j)
 h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
S=I^T;assert len(I)==2892 and len(S)==3300 and(p,h)==((-65,-71),0)
def weight(t,c):return 6*(F(4)**(t-c)+F(4)**(c-t))-2
def phi(profile,n,c,sector=0):
 counts=Counter(t for t,a in profile);sgn=1 if sector==0 else-1
 return sum((sgn*(1 if t%2==0 else-1)*weight(t,c)*k/F(n)for t,k in counts.items()),F(0))
def rat(x):return{'numerator':x.numerator,'denominator':x.denominator}
controls=[]
for c in[0,9,14]:
 delta=phi(S,78,c)-phi(I,78,c);lower=F(2*len(W),78);assert delta>=lower and delta>0
 # Longitudinal lift changes representation but NOT density potential.
 Ilift={(t,a+j*78)for t,a in I for j in range(3)};Slift={(t,a+j*78)for t,a in S for j in range(3)}
 assert phi(Ilift,234,c)==phi(I,78,c)and phi(Slift,234,c)==phi(S,78,c)
 # Opposite sector is required by true time reversal; never exclude that
 # actual positive control by mistakenly keeping the old sector.
 assert phi(I,78,c,1)-phi(S,78,c,1)==delta
 controls.append({'fixed_normal_center':c,'forward_delta':rat(delta),'clock_lower_bound':rat(lower),'same_sector_exact_reset_delta':rat(-delta),'opposite_sector_reverse_delta':rat(delta),'common_period_lift_invariant':True})
# The profile phase bound, here supplied exactly for actual support interval.
a,b=-64,92;c=(a+b)//2;span=sum((weight(t,c)for t in range(a,b+1)),F(0));bound=(span/F(4)).__floor__()
# Independent small rational range check by exhaustive density vertices.
from itertools import product
lo,hi=-2,2;values=[]
for bits in product([0,1],repeat=hi-lo+1):
 vals=sum(((1 if t%2==0 else-1)*weight(t,0)*bits[t-lo]for t in range(lo,hi+1)),F(0));values.append(vals)
assert max(values)-min(values)==sum((weight(t,0)for t in range(lo,hi+1)),F(0))
out={'status':'AUTHOR exact controls PASS for normalized profile-clock theorem','source_input_classes_period78':len(I),'source_output_classes_period78':len(S),'source_period':15324,'source_stride':-78,'sector_bit':0,'clock_parameters':{'a':4,'b':4,'delta':rat(F(1,3)),'M':6,'per_step_gain_at_least':2},'minimum_density_gain_per_full_parallel_phase':4,'controls':controls,'fixed_support_interval':[a,b],'fixed_center':c,'profile_potential_range_bound':rat(span),'maximum_complete_profile_phases':bound,'small_range_extreme_check':True,'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'profile_density_clock.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in['controls','maximum_complete_profile_phases','profile_potential_range_bound']},indent=2));print('Exact15324controls:',json.dumps(controls))
