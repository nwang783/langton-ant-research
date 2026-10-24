"""Executed supplied-template frame validator for A=I, using exact read sets.
No successful growing model or general template extractor is claimed.
"""
import pathlib,json,time
from presburger_read_set_solver import Context,relation,typed,literal
from check_read_sets import D
HERE=pathlib.Path(__file__).parent

def xor(A,B):return A.subtract(B).union(B.subtract(A)).coalesce()
def pull(A,r='r',x='x',y='y'):
 ctx=A.ctx
 M=ctx.map(f'{{ [R,X,Y] -> [r,x,y] : R={r} and X={x} and Y={y} and r>=0 }}')
 return M.binary('intersect_domain',A).range().coalesce()
def shift(A,p):return pull(A,x=f'x-({p[0]})',y=f'y-({p[1]})')
def periodic_set(ctx,phases):
 parts=[]
 for ph,B in enumerate(phases):
  for x,y in sorted(B):parts.append(f'(r%{len(phases)}={ph} and x={x} and y={y})')
 return ctx.set('{ [r,x,y] : r>=0 and ('+(' or '.join(parts) if parts else '0=1')+') }')
def read_parity(states):
 p=(0,0);Q=set()
 for s in states:
  if p in Q:Q.remove(p)
  else:Q.add(p)
  h=(s//2+(1 if s%2==0 else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return Q,p

def validate(ctx,images,root,I,O,B):
 if not isinstance(images,(list,tuple)) or len(images)!=8:
  raise ValueError('exactly eight image strings are required')
 if any(not isinstance(w,str) or not w or not set(w)<=set('RL') for w in images):
  raise ValueError('every image must be a nonempty R/L string')
 if type(root) is not int or not 0<=root<8:
  raise ValueError('root must be an integer in 0..7')
 phi=typed(images);reachable={root}
 while True:
  new=reachable|{t for s in reachable for t,p in phi[s]}
  if new==reachable:break
  reachable=new
 geometry=True
 for s in reachable:
  reads,p,h,n=literal(images,s,1);out=(s//2+(1 if s%2==0 else -1))%4
  geometry &= h==out and p==D[out]
 assert geometry,'supplied image geometry is not unit identity'
 edges=[(s,t,p) for s in reachable for t,p in phi[s]];R={};formula={}
 for s in reachable:ctx.reset_operations();R[s],formula[s]=relation(ctx,reachable,edges,s)
 delta={s:xor(I[s],O[s]) for s in reachable};fail=[];frame_checks=0;output_checks=0
 origin=ctx.set('{ [r,x,y] : r=0 and x=0 and y=0 }')
 base=ctx.set('{ [r,x,y] : r=0 }')
 for s in reachable:
  if int(not I[s].intersect(origin).is_empty())!=s%2:fail.append(dict(kind='base',state=s))
  if not O[s].intersect(base).is_equal(xor(I[s].intersect(base),origin)):
   fail.append(dict(kind='base_output',state=s))
  current=pull(I[s],r='r+1')
  for j,(t,p) in enumerate(phi[s]):
   childI=shift(I[t],p);childR=shift(R[t],p)
   bad=xor(current,childI).intersect(childR).coalesce();frame_checks+=1
   if not bad.is_empty():fail.append(dict(kind='frame',state=s,child=j,disagreement=str(bad)))
   current=xor(current,shift(delta[t],p))
  output_checks+=1
  if not current.is_equal(pull(O[s],r='r+1')):fail.append(dict(kind='output',state=s))
 rootboard=periodic_set(ctx,[set(B)])
 if not I[root].is_equal(rootboard):fail.append(dict(kind='root initial board is not the supplied fixed B'))
 growing=len(phi[root])>=2 and phi[root][0][0]==root
 return dict(geometry=True,growing_root=growing,frame_checks=frame_checks,output_checks=output_checks,
  all_template_checks_pass=not fail,accepted=growing and not fail,failures=fail,
  exact_read_sets={str(s):str(R[s]) for s in reachable},read_set_formulas={str(s):formula[s] for s in reachable})

def main():
 start=time.monotonic();ctx=Context(max_operations=20000000);records=[];invalid_checks=0
 for images,root in [(['R']*7,0),(['R']*9,0),(['R']*7+[''],0),(['R']*7+['X'],0),(['R']*7+[None],0),(['R']*8,-1),(['R']*8,8),(['R']*8,False)]:
  try:validate(ctx,images,root,{}, {},set())
  except ValueError:invalid_checks+=1
  else:raise AssertionError('malformed input was accepted')
 for root in (0,1):
  images=['R','L']*4;B={(0,0)} if root==1 else set()
  I={root:periodic_set(ctx,[B])};O={root:periodic_set(ctx,[B^{(0,0)}])}
  r=validate(ctx,images,root,I,O,B);assert r['all_template_checks_pass'] and not r['accepted']
  r['name']='identity_R' if root==0 else 'identity_L';records.append(r)
 # An incorrect zero-depth output must not be accepted merely because its
 # forged identity recursion is self-consistent.
 badI={0:periodic_set(ctx,[set()])};badO={0:periodic_set(ctx,[set()])}
 bad=validate(ctx,['R','L']*4,0,badI,badO,set())
 assert any(f['kind']=='base_output' for f in bad['failures'])
 bad['name']='forged_identity_output';records.append(bad)
 # Canonical input/output parity templates of the prescribed R^(5^r) path
 # from the empty seed, specified as exact period-two finite point sets.
 images=['RRRRR','LLLLL']*4;I={};O={}
 for h in range(4):
  s=2*h;z=read_parity([2*j for j in range(h)])[1];inputs=[];outputs=[]
  for residue in range(2):
   n=1 if residue==0 else 5
   q,_=read_parity([2*(j%4) for j in range(h*n)])
   qi={(x-z[0],y-z[1]) for x,y in q}
   qb,_=read_parity([2*((h+j)%4) for j in range(n)])
   inputs.append(qi);outputs.append(qi^qb)
  I[s]=periodic_set(ctx,inputs);O[s]=periodic_set(ctx,outputs)
 r=validate(ctx,images,0,I,O,set());assert r['growing_root'] and not r['accepted']
 assert all(f['kind']=='frame' for f in r['failures']);assert len(r['failures'])>=4
 r['name']='right_five_canonical_period_two';records.append(r)
 out=dict(libisl_version=ctx.version,invalid_input_rejections=invalid_checks,records=records,total_frame_checks=sum(r['frame_checks'] for r in records),
  accepted_growing_models=sum(r['accepted'] for r in records),
  scope='Integrated exact supplied-template validator controls for A=I. No automatic template extractor or nontrivial model.',seconds=time.monotonic()-start)
 (HERE/'presburger_template_validator.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
 print([(r['name'],r['all_template_checks_pass'],len(r['failures'])) for r in records])
if __name__=='__main__':main()
