"""Independent full feasible-set controls for supplied parity / arbitrary seed positions."""
from pathlib import Path
import sys,json,hashlib,time
R=Path(__file__).resolve().parents[1];D=R/'computability/finite_power_exact_validator';sys.path.insert(0,str(D))
source=D/'presburger_bounded_seed.py';source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
import presburger_bounded_seed as candidate
ctx=candidate.Context(max_operations=30_000_000);start=time.monotonic()
def set_phases(phases):
 clauses=[]
 for i,points in enumerate(phases):
  for z in points:clauses.append(f'(r%{len(phases)}={i} and x={int(z.real)} and y={int(z.imag)})')
 return ctx.set('{ [r,x,y] : r>=0 and ('+(' or '.join(clauses)if clauses else'0=1')+') }')
def parity(turn,heading,count):
 z=0j;h=(1j,1,-1j,-1)[heading];q=set()
 for i in range(count):
  if z in q:q.remove(z)
  else:q.add(z)
  h*= -1j if turn=='R'else 1j;z+=h
 return q
malformed=0
other=candidate.Context()
for Q in ({0:ctx.set('[u] -> { [r,x,y] : r>=0 and x=u and y=0 }')},{0:ctx.set('{ [r,x] : r>=0 and x=0 }')},{0:ctx.set('{ [x,r,y] : r>=0 and x=0 and y=0 }')},{0:other.set('{ [r,x,y] : r>=0 and x=0 and y=0 }')},{},None):
 try:candidate.solve(ctx,['R','L']*4,0,Q,0)
 except ValueError:malformed+=1
 else:raise AssertionError('Malformed parity template accepted')
controls=[]
for root in range(8):
 for M in range(3):
  ctx.reset_operations();ans=candidate.solve(ctx,['R','L']*4,root,{root:set_phases([{0j}])},M)
  assert ans['status']=='decided'
  names=[v for i in range(M)for v in(f'a{i}',f'bx{i}',f'by{i}')]
  prefix='['+','.join(names)+'] -> 'if names else''
  active=' and '.join(f'0<=a{i}<=1'for i in range(M))or'1=1'
  occupied=' or '.join(f'(a{i}=1 and bx{i}=0 and by{i}=0)'for i in range(M))or'0=1'
  condition=occupied if root%2 else'not ('+occupied+')'
  expected=ctx.set(prefix+'{ [] : '+active+' and ('+condition+') }').params()
  got=ctx.set(ans['feasible_parameters']);assert got.is_equal(expected),(root,M,str(got),str(expected))
  assert ans['possible']==(not expected.is_empty())
  if ans['possible']:
   assert len(ans['seed'])<=M and ((0,0)in map(tuple,ans['seed']))==bool(root%2)
  controls.append([root,M,'identity',ans['possible']])
for root in range(8):
 turn='L'if root%2 else'R';Q={2*h+root%2:set_phases([parity(turn,h,n)for n in(1,5)])for h in range(4)}
 for M in(0,1):
  ctx.reset_operations();ans=candidate.solve(ctx,['RRRRR','LLLLL']*4,root,Q,M)
  assert ans['status']=='decided'and not ans['possible']and ans['growing'];controls.append([root,M,'five-turn',False])
for mode in('base','recurrence'):
 Q={2*h:set_phases([parity('R',h,n)for n in(1,5)])for h in range(4)}
 Q[0]=set_phases([set()if mode=='base'else{0j}]);ctx.reset_operations()
 ans=candidate.solve(ctx,['RRRRR','LLLLL']*4,0,Q,1);assert ans['status']=='invalid parity certificate'and ans['kind']==mode
assert source_hash==hashlib.sha256(source.read_bytes()).hexdigest(),'Source changed during replay; rerun frozen version'
out={'status':'PASS independent all-coordinate feasible-set and parity controls','identity_parameter_set_equalities':24,'arbitrary_seed_five_turn_exclusions':16,'invalid_parity_certificates':2,'malformed_template_rejections':malformed,'records':controls,'source_sha256':source_hash,'seconds':time.monotonic()-start,'scope':'A=I with supplied exact parameter-free parity sets; no template extraction or accepted growing model.'}
(R/'audits/presburger_bounded_seed_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
