"""Independent arithmetic, literal read-footprint and canonical-board controls.
Subject modules are black boxes; no ISL membership oracle is used for conversion.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from functools import lru_cache
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[1];H=ROOT/'computability/flat_exact_validator';sys.path.insert(0,str(H))
import general_given_seed as G
import scheme_cover_decider as S
from isl_automatic import convert,Context
start=time.monotonic();ctx=Context(max_operations=30000000);rows=[];total=0
forms=[
 ('signed_floor','{ [r,x,y] : r>=0 and y=floor((3*x-2*r-5)/4) }',lambda r,x,y:r>=0 and y==(3*x-2*r-5)//4),
 ('mod_floor_union','{ [r,x,y] : r>=0 and ((x+2*r)%5=3 and y=floor((x-r)/3)) or (r=2 and x+y=-4) }',lambda r,x,y:(r>=0 and (x+2*r)%5==3 and y==(x-r)//3) or (r==2 and x+y==-4)),
 ('signed_witness','{ [r,x,y] : exists (a,b : x=2*a+3*b and y=a-b and -r<=a<=r) }',lambda r,x,y:(x-2*y)%5==0 and -r<=y+(x-2*y)//5<=r),
 ('large_exact','{ [r,x,y] : 100000000000000000001*x+100000000000000000000*y=r }',lambda r,x,y:100000000000000000001*x+100000000000000000000*y==r),
 ('two_floor','{ [r,x,y] : y=floor((x-r)/3)+floor((2*x+r+1)/5) }',lambda r,x,y:y==(x-r)//3+(2*x+r+1)//5)]
for name,formula,expected in forms:
 obj=ctx.set(formula);n=0
 for signs in product((-1,1),repeat=2):
  A,st=convert(obj,('r','x','y'),(1,*signs))
  for r,x,y in product(range(7),range(9),range(9)):
   assert A.eval(r=r,x=x,y=y)==expected(r,signs[0]*x,signs[1]*y),(name,r,x,y,signs)
   n+=1
 rows.append(dict(name=name,direct_integer_checks=n));total+=n
print('ISL independent',total,flush=True)
malformed=0
for obj,variables,signs in [(ctx.set('[n] -> { [x] : x=n }'),('x',),None),(ctx.set('{ [x,y] }'),('x',),None),(ctx.set('{ [x,y] }'),('x','x'),None),(ctx.set('{ [x] }'),('x',),(True,)),(ctx.set('{ [x] }'),('x',),(0,))]:
 try:convert(obj,variables,signs)
 except ValueError:malformed+=1
 else:raise AssertionError('invalid conversion accepted')
P=G.standard_physical();I=[[s]for s in range(8)]
transient=G.GeneralUnitModel(P+[(0,1)],I+[G.word_states('RLLLLRRRR')],8)
models=[('R_identity',G.identity(0),[],True),('L_identity',G.identity(1),[(0,0)],True),('R5_branch',G.from_strings(['RRRRR','LLLLL']*4),[],False),('transient_R9',transient,[(0,1),(1,0),(1,1)],True),('two_state',G.GeneralUnitModel([(0,1)]*2,[[1],[0]],0),[],True)]
results=[]
for name,m,seed,expect in models:
 V=G.GivenSeedValidator(m,seed);out=V.solve();assert out['possible']==expect
 @lru_cache(None)
 def expand(s,r):return (s,) if not r else tuple(t for u in m.images[s]for t in expand(u,r-1))
 def trace(word,heading):
  h=(1j,1,-1j,-1)[heading];p=0j;reads=[]
  for s in word:
   ih,t=m.physical[s];assert h==(1j,1,-1j,-1)[ih];reads.append((p,t==-1));h*=(-1j if t==1 else 1j);p+=h
  return reads,p,h
 check=0;maxdepth=3
 for s in m.reach:
  pos=complex(*V.positions[s]);pref=V.refs[s]
  # Verify this is a genuine root prefix, rather than an arbitrary reference.
  assert s==m.root or any(tuple(expand(m.root,d)[:len(pref)])==pref and expand(m.root,d)[len(pref)]==s for d in range(len(m.reach)+1))
  tables={}
  for signs in product((-1,1),repeat=2):
   x=({'x':signs[0]},0);y=({'y':signs[1]},0);r=({'r':1},0)
   tables[signs]=(V.I(s,r,x,y,('r','x','y')),V.Q(s,r,x,y,('r','x','y')))
  for depth in range(maxdepth+1):
   word=expand(s,depth);reads,_,_=trace(word,m.physical[s][0]);foot={p for p,t in reads};odd=Counter(p for p,t in reads)
   prefixword=tuple(t for u in pref for t in expand(u,depth));before,_,_=trace(prefixword,m.physical[m.root][0]);toggles=Counter(p for p,t in before)
   for x,y in product(range(-4,5),repeat=2):
    signs=(1 if x>=0 else -1,1 if y>=0 else -1);Iauto,Qauto=tables[signs];val=dict(r=depth,x=abs(x),y=abs(y));z=complex(x,y)
    assert V.read[s][signs].eval(**val)==(z in foot)
    assert Qauto.eval(**val)==bool(odd[z]%2)
    globalp=z+pos;want=((int(globalp.real),int(globalp.imag))in set(map(tuple,seed)))^(toggles[globalp]%2)
    assert Iauto.eval(**val)==want,(name,s,depth,x,y)
    check+=3
 for depth in range(5):
  board={complex(*p)for p in seed};reads,_,_=trace(expand(m.root,depth),m.physical[m.root][0]);legal=True
  for z,black in reads:
   if (z in board)!=black:legal=False;break
   board.symmetric_difference_update({z})
  if expect:assert legal
  if name=='R5_branch'and depth>=1:assert not legal
 results.append(dict(name=name,verdict=out,independent_literal_coordinate_checks=check));print(name,check,flush=True)
# Position coverage must not substitute for chronology.
m=models[2][1]
a=S.solve(m,[S.fixed_path(m,())]);assert a['possible'] is None
b=S.solve(m,[S.fixed_path(m,())]+[S.fixed_path(m,(j,))for j in(1,2,3)]);assert b['position_coverage_exact']and b['possible'] is False
# Invalid schemes cannot manufacture negative requirements.
try:S.validate_scheme(m,(((True,(m.phi[0][1],)),),m.phi[0][1].target))
except ValueError:malformed+=1
else:raise AssertionError('nonclosed star accepted')
res=dict(status='PASS independent integer arithmetic and complete literal template/footprint controls',conversion=rows,malformed_inputs_rejected=malformed,models=results,position_cover_controls=2,seconds=time.monotonic()-start,hashes={p:hashlib.sha256((H/p).read_bytes()).hexdigest()for p in('isl_automatic.py','general_given_seed.py','scheme_cover_decider.py')},scope='Implementation audit of exact given-seed and supplied genuine position-cover realization for additive-I typed unit presentations. No growing positive or global capture theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
