"""Check exact finite-range rational certificates, using semisimple sets.
This is the positive certificate checker, not a practical complete enumerator.
"""
import pathlib,sys,json,itertools,time
import sympy as S
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'))
from isl_exact import Context

def monomial(variables,v):return S.prod(x**a for x,a in zip(variables,v))
def check(F,variables,allowed,components):
 """component=(integer label, nonnegative base tuple, period tuples)."""
 d=len(variables);ctx=Context(max_operations=10000000);names=[f'x{i}' for i in range(d)]
 base_universe=ctx.set('{ ['+','.join(names)+'] : '+' and '.join(f'{n}>=0' for n in names)+' }')
 union=ctx.set('{ ['+','.join(names)+'] : 0=1 }');GF=S.Integer(0);parsed=[]
 for label,base,periods in components:
  if label not in allowed:return dict(valid=False,reason='label outside specified range')
  if len(base)!=d or any(type(a) is not int or a<0 for a in base):return dict(valid=False,reason='invalid base')
  if any(len(v)!=d or any(type(a) is not int or a<0 for a in v) or not any(v) for v in periods):
   return dict(valid=False,reason='invalid period')
  if periods and S.Matrix(periods).rank()!=len(periods):return dict(valid=False,reason='dependent periods')
  counters=[f'n{j}' for j in range(len(periods))]
  equations=[]
  for i in range(d):
   rhs=str(base[i])+''.join(f'+{v[i]}*n{j}' for j,v in enumerate(periods) if v[i])
   equations.append(f'x{i}={rhs}')
  if counters:
   formula='exists ('+','.join(counters)+' : '+' and '.join([f'{n}>=0' for n in counters]+equations)+')'
  else:formula=' and '.join(equations)
  R=ctx.set('{ ['+','.join(names)+'] : '+formula+' }')
  if not union.intersect(R).is_empty():return dict(valid=False,reason='overlapping components')
  union=union.union(R);GF+=label*monomial(variables,base)/S.prod(1-monomial(variables,v) for v in periods)
  parsed.append(str(R))
 if 0 not in allowed and not base_universe.subtract(union).is_empty():return dict(valid=False,reason='unlisted zero coefficients')
 if S.cancel(F-GF)!=0:return dict(valid=False,reason='rational functions differ')
 # Exact support-fiber test treats first coordinate as depth/time.
 bounded=True;why=[]
 for ci,(label,base,periods) in enumerate(components):
  if label==0:continue
  nz=list(periods)
  if any(v[0]==0 for v in nz):bounded=False;why.append([ci,'nonzero zero-time period']);continue
  if nz:
   u=nz[0]
   if any(any(v[i]*u[0]!=u[i]*v[0] for i in range(1,d)) for v in nz):
    bounded=False;why.append([ci,'distinct period velocities'])
 return dict(valid=True,semilinear_sets=parsed,uniform_support_fibers=bounded,
  fiber_bound=sum(label!=0 for label,base,periods in components) if bounded else None,
  unbounded_witnesses=why)

def main():
 start=time.monotonic();z,x,y=S.symbols('z x y');v=(z,x,y);allowed={-1,0,1};records=[]
 cases=[('glider',1/(1-z*x),[(1,(0,0,0),[(1,1,0)])],True,True),
 ('expanding_fiber',1/((1-z*x)*(1-z*y)),[(1,(0,0,0),[(1,1,0),(1,0,1)])],True,False),
 ('zero_time_fiber',1/(1-x),[(1,(0,0,0),[(0,1,0)])],True,False),
 ('signed_two_tracks',1/(1-z*x)-y/(1-z*y),[(1,(0,0,0),[(1,1,0)]),(-1,(0,0,1),[(1,0,1)])],True,True),
 ('duplicate_track',2/(1-z*x),[(1,(0,0,0),[(1,1,0)]),(1,(0,0,0),[(1,1,0)])],False,None),
 ('dependent_periods',1/(1-z*x)**2,[(1,(0,0,0),[(1,1,0),(1,1,0)])],False,None),
 ('wrong_rational_identity',1/(1-z-z*x),[(1,(0,0,0),[(1,1,0)])],False,None)]
 for name,F,c,want,bound in cases:
  r=check(F,v,allowed,c);assert r['valid']==want,(name,r)
  if want:assert r['uniform_support_fibers']==bound,(name,r)
  r['name']=name;records.append(r)
 r=check(S.Integer(1),v,{1},[(1,(0,0,0),[])])
 assert not r['valid'] and r['reason']=='unlisted zero coefficients';r['name']='missing_coverage';records.append(r)
 out=dict(records=records,positive_certificates=sum(r['valid'] for r in records),
  negative_controls=sum(not r['valid'] for r in records),
  scope='Exact supplied semisimple rational-certificate checker; no complete enumerator or ant model.',seconds=time.monotonic()-start)
 (HERE/'simple_linear_range_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
