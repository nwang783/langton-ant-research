"""Exact all-depth chronology of U^r c V^r, no horizon or guessed colors.
Uses the existing ownership-safe libisl bridge; resource errors are errors.
"""
import pathlib,sys,json,time
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from presburger_read_set_solver import Context
from isl_exact import Object,_FUN,sample_parameters
D=((0,1),(1,0),(0,-1),(-1,0))

def trace(word,h):
 x=y=0;rows=[]
 for c in word:
  rows.append((x,y,h,c));h=(h+(1 if c=='R' else -1))%4
  dx,dy=D[h];x+=dx;y+=dy
 return rows,(x,y),h

def validate(U,c,V,h):
 if not isinstance(U,str) or not isinstance(V,str) or not set(U+V)<=set('RL') or c not in ('R','L'):
  raise ValueError('U,V must be R/L words and parent must be R or L')
 if type(h) is not int or not 0<=h<4:raise ValueError('heading must be0..3')
 u,q,hu=trace(U,h);middle,v,hm=trace(c,h);vv,qv,hv=trace(V,hm)
 if hu!=h or hv!=hm or qv!=tuple(-a for a in q):raise ValueError('not a valid unit-pose hairpin geometry')
 return u,q,middle,v,vv

def certify(ctx,U,c,V,h=0):
 ctx.reset_operations();u,q,mid,v,vv=validate(U,c,V,h)
 if q==(0,0):raise ValueError('this moving-hairpin adapter requires nonzero drift')
 a,b=len(U),len(V);families=[]
 for j,(x,y,_,turn) in enumerate(u):families.append(((x,y),'U',j,turn))
 families.append(((0,0),'C',0,c))
 for j,(x,y,_,turn) in enumerate(vv):families.append(((v[0]+x,v[1]+y),'V',j,turn))
 groups=[]
 def shift(p,rep):
  at=0 if q[0] else 1;d=p[at]-rep[at]
  if d%q[at]:return None
  k=d//q[at]
  return k if all(p[j]-rep[j]==k*q[j] for j in range(2)) else None
 for p,phase,j,turn in families:
  for rep,rows in groups:
   k=shift(p,rep)
   if k is not None:break
  else:rep=p;rows=[];groups.append((rep,rows));k=0
  if phase=='U':domain=f'r>=0 and 0<=z-{k}<r';tm=f'{a}*z+{j-a*k}'
  elif phase=='V':domain=f'r>=0 and 1<=z-{k}<=r';tm=f'{a+b}*r+{-b}*z+{1+j+b*k}'
  else:domain=f'r>=0 and z=r+{k}';tm=f'{a}*r'
  rows.append((ctx.set('[r]->{[z]:'+domain+'}'),tm,turn))
 bad_depths=ctx.set('[r]->{[]:0=1}').params();black=ctx.set('[r]->{[x,y]:0=1}')
 final=ctx.set('[r]->{[x,y]:0=1}');support=ctx.set('[r]->{[x,y]:0=1}')
 for group,(rep,rows) in enumerate(groups):
  for f,(df,tf,cf) in enumerate(rows):
   mapping=ctx.map(f'[r]->{{[z]->[x,y]:x={rep[0]}+{q[0]}*z and y={rep[1]}+{q[1]}*z}}')
   def image(domain):
    return Object(ctx,'map',_FUN['map','intersect_domain'](mapping._copy(),domain._copy())).range()
   support=support.union(image(df))
   if cf=='R':
    last=df
    for dh,th,ch in rows:
     last=last.subtract(dh.intersect(ctx.set(f'[r]->{{[z]:({th})>({tf})}}')))
    final=final.union(image(last))
   if cf=='L':
    first=df
    for dh,th,ch in rows:
     first=first.subtract(dh.intersect(ctx.set(f'[r]->{{[z]:({th})<({tf})}}')))
    mapping=ctx.map(f'[r]->{{[z]->[x,y]:x={rep[0]}+{q[0]}*z and y={rep[1]}+{q[1]}*z}}')
    mapped=Object(ctx,'map',_FUN['map','intersect_domain'](mapping._copy(),first._copy()))
    black=black.union(mapped.range())
   for g,(dg,tg,cg) in enumerate(rows):
    if f==g or cf!=cg:continue
    ctx.reset_operations()
    candidate=df.intersect(dg).intersect(ctx.set(f'[r]->{{[z]:({tf})<({tg})}}'))
    if candidate.is_empty():continue
    for dh,th,ch in rows:
     middle=dh.intersect(ctx.set(f'[r]->{{[z]:({tf})<({th})<({tg})}}'))
     candidate=candidate.subtract(middle)
    bad_depths=bad_depths.union(candidate.params())
  # A group's literal visits are exhausted by its finitely many rows.
 bad_depths=bad_depths.coalesce();black=black.coalesce()
 return dict(all_depths_internally_legal=bad_depths.is_empty(),bad_depths=str(bad_depths),
  counterexample_depth=sample_parameters(bad_depths,1),required_initial_black=str(black),
  position_cosets=len(groups),maximum_reads_per_cell=max(len(rows) for _,rows in groups),
  final_minimal_black=str(final.coalesce()),read_support=str(support.coalesce()),
  bad_relation=bad_depths,black_relation=black,final_relation=final.coalesce(),support_relation=support.coalesce())

def literal(U,c,V,h,r):
 word=U*r+c+V*r;rows,_,_=trace(word,h);last={};black=set();bad=False
 for t,(x,y,_,turn) in enumerate(rows):
  p=x,y
  if p in last:
   if last[p]==turn:bad=True
  elif turn=='L':black.add(p)
  last[p]=turn
 return bad,black

def tiled(ctx,points,q):
 clauses=[f'exists(i:0<=i<r and x={x}+{q[0]}*i and y={y}+{q[1]}*i)' for x,y in points]
 return ctx.set('[r]->{[x,y]:r>=0 and ('+' or '.join(clauses)+')}').coalesce()

def main():
 start=time.monotonic();ctx=Context(max_operations=40000000)
 path=HERE.parents[1]/'causal_reduction/unit_scale/probe_decorated_transport_cycles.json'
 records=json.loads(path.read_text())['records'];output=[];checks=0;tile_control=None
 for rec in records:
  result=certify(ctx,rec['U'],rec['parent'],rec['V'])
  for r in range(25):
   bad,black=literal(rec['U'],rec['parent'],rec['V'],0,r)
   at=ctx.set(f'[r] -> {{ [] : r={r} }}').params()
   assert result['bad_relation'].intersect_params(at).is_empty()==(not bad)
   expected=ctx.set('[r] -> { [x,y] : 0=1 }')
   for x,y in black:expected=expected.union(ctx.set(f'[r] -> {{ [x,y] : r={r} and x={x} and y={y} }}'))
   assert result['black_relation'].intersect_params(at).is_equal(expected)
   checks+=1
  if rec['source']=='R21' and rec['recursive_read']==14:
   I=[(-2,0),(-2,1),(-1,1),(-1,2),(0,0),(0,2)]
   O=[(-2,1),(-2,2),(-1,0),(0,3),(1,1),(1,2)];q=(-1,3)
   cap=ctx.set('[r]->{[x,y]:r>=0 and x=-r and y=3r}')
   J=sorted({(x,y) for x,y,h,c in trace(rec['word'],0)[0]}-{q})
   assert result['black_relation'].is_equal(tiled(ctx,I,q))
   assert result['final_relation'].is_equal(tiled(ctx,O,q).union(cap))
   assert result['support_relation'].is_equal(tiled(ctx,J,q).union(cap))
   tile_control=dict(drift=q,input_tile=I,output_tile=O,read_tile=J,
    all_depth_input_equality=True,all_depth_output_equality=True,all_depth_read_support_equality=True)
  output.append(dict(source=rec['source'],recursive_read=rec['recursive_read'],drift=rec['drift'],
   **{k:v for k,v in result.items() if not k.endswith('_relation')}))
 out=dict(scope='Exact all-r internal chronology and first-read black requirements for nine supplied hairpin families, not a common finite seed or prolongable growing model.',
  records=output,positive_tile_control=tile_control,literal_depth_controls=checks,seconds=time.monotonic()-start,isl_version=ctx.version)
 HERE.joinpath('hairpin_presburger.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
