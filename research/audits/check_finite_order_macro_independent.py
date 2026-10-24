from pathlib import Path
from functools import lru_cache
import sys,json,hashlib
B=Path('/workspace/shared/langton');H=B/'computability/flat_exact_validator';sys.path.insert(0,str(H))
import finite_order_macro_adapter as A
D=(1j,1,-1j,-1);M=((-1,0),(0,-1))
cases=[('zero_identity',[(1,'LLLRRRRL')],[[0]],True),('zero_two_cycle',[(1,'LLLRRRRL')]*2,[[1],[0]],True),('zero_branch',[(0,'RRRR')],[[0,0]],False)]
bases=[(s//2,('RLLLLRRRR' if s%2==0 else 'LRRRRLLLL')) for s in range(8)];images=[A.word_states(w,s//2) for s,w in enumerate(['RRRRLRLLL','LRRRLRLLL']*4)];cases.append(('nonzero_multiread_halfturn',bases,images,False));out=[]
for name,bases,images,expected in cases:
 model,cert=A.prepare_macro(bases,images,M,2,max_powered_reads=100000)
 @lru_cache(None)
 def expand(s,r):return (s,) if not r else tuple(v for t in images[s] for v in expand(t,r-1))
 def trace(word,heading):
  z=0j;h=D[heading];reads=[]
  for s in word:
   assert h==D[bases[s][0]]
   for c in bases[s][1]:reads.append((z,c));h*=(-1j if c=='R' else 1j);z+=h
  return reads,z,h
 count=0
 for s in range(len(bases)):
  _,net,final=trace((s,),bases[s][0]);assert tuple(model.images[s])==expand(s,cert['common_power'])
  for r in range(cert['common_power']+1):
   reads,p,h=trace(expand(s,r),bases[s][0]);assert p==(-1)**r*net and h==final;count+=len(reads)
 result=A.solve_macro_finite_order(bases,images,M,2,max_powered_reads=100000);assert result['possible']==expected
 if not expected:
  reads,p,h=trace(expand(0,cert['common_power']),bases[0][0]);needs={};odd=set();conflict=None
  for j,(z,c) in enumerate(reads):
   n=(c=='L')^(z in odd)
   if z in needs and needs[z][0]!=n:conflict=(z,needs[z][1],j);break
   needs[z]=(n,j);odd.symmetric_difference_update({z})
  assert conflict and complex(*result['conflict']['cell'])==conflict[0] and result['conflict']['conflicting_read']==conflict[2]
 else:assert result['candidate_seed']==[(-1,1),(0,0),(0,1)] and not result['given_seed_validation']['accepted_growing_model']
 out.append(dict(name=name,literal_reads=count,power_certificate=cert,result=result))
assert A.solve_macro_finite_order(cases[-1][1],cases[-1][2],M,2,max_powered_reads=20)['possible'] is None
bad=0
for kwargs in [dict(order=True),dict(order=0),dict(order=1),dict(order=2,root=True)]:
 try:A.prepare_macro(cases[0][1],cases[0][2],M,**kwargs)
 except ValueError:bad+=1
 else:raise AssertionError('invalid accepted')
result=dict(status='PASS independent macro expansion, intermediate scaled geometry and conflict replay',controls=out,malformed_rejected=bad,explicit_cap_unknown=True,sha256=hashlib.sha256((H/'finite_order_macro_adapter.py').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
