"""Unknown bounded-mass seed solver at A=I with supplied, VERIFIED parity sets.
No guessed spatial radius. This does not extract parity templates in general.
"""
import pathlib,sys,json,time,ctypes as C
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from presburger_read_set_solver import Context,relation,typed,literal
from presburger_template_validator import xor,pull,shift,periodic_set,read_parity
from isl_exact import sample_parameters, Object, _bind, _P
_set_dim=_bind('isl_set_dim',[_P,C.c_int],C.c_int)
_dim_name=_bind('isl_set_get_dim_name',[_P,C.c_int,C.c_uint],C.c_char_p)

def references(phi,root):
 reach={root}
 while True:
  new=reach|{t for s in reach for t,p in phi[s]}
  if new==reach:break
  reach=new
 word=[root]
 while not reach<=set(word):word=[t for s in word for t,p in phi[s]]
 return {s:word[:word.index(s)] for s in reach}

def solve(ctx,images,root,Q,M):
 if not isinstance(images,(list,tuple)) or len(images)!=8 or any(not isinstance(w,str) or not w or not set(w)<=set('RL') for w in images):
  raise ValueError('eight nonempty R/L images are required')
 if type(root) is not int or not 0<=root<8 or type(M) is not int or M<0:
  raise ValueError('invalid root or mass bound')
 phi=typed(images)
 if len(phi[root])>1 and phi[root][0][0]!=root:raise ValueError('take a first-letter fixed power first')
 if phi[root][0][0]!=root:raise ValueError('root must be first-letter fixed')
 refs=references(phi,root);states=sorted(refs)
 for s in states:
  q=Q.get(s) if isinstance(Q,dict) else None
  if not isinstance(q,Object) or q.kind!='set' or q.ctx is not ctx:
   raise ValueError('every reachable parity template must be a set in the supplied context')
  if _set_dim(q.ptr,1)!=0 or _set_dim(q.ptr,3)!=3:
   raise ValueError('parity templates must have no parameters and exactly three set coordinates')
  if tuple(_dim_name(q.ptr,3,i) for i in range(3))!=(b'r',b'x',b'y'):
   raise ValueError('parity coordinate order must be [r,x,y]')
 for s in states:
  _,p,h,_=literal(images,s,1);sign=1 if s%2==0 else -1;out=(s//2+sign)%4
  from check_read_sets import D
  if h!=out or p!=D[out]:raise ValueError('wrong A=I image geometry')
 # A supplied parity certificate is exact iff base and full recurrence hold.
 empty=periodic_set(ctx,[set()]);origin=ctx.set('{ [r,x,y] : r=0 and x=0 and y=0 }')
 base=ctx.set('{ [r,x,y] : r=0 }')
 for s in states:
  if not Q[s].intersect(base).is_equal(origin):return dict(status='invalid parity certificate',state=s,kind='base')
  rhs=empty
  for t,p in phi[s]:rhs=xor(rhs,shift(Q[t],p))
  if not rhs.is_equal(pull(Q[s],r='r+1')):return dict(status='invalid parity certificate',state=s,kind='recurrence')
 names=[v for i in range(M) for v in (f'a{i}',f'bx{i}',f'by{i}')]
 prefix=('['+','.join(names)+'] -> ') if names else ''
 active=' and '.join(f'0<=a{i}<=1' for i in range(M)) or '1=1'
 universe=ctx.set(prefix+'{ [] : '+active+' }').params()
 membership=' or '.join(f'(a{i}=1 and x=bx{i} and y=by{i})' for i in range(M)) or '0=1'
 B=ctx.set(prefix+'{ [r,x,y] : r>=0 and '+active+' and ('+membership+') }')
 z={s:read_parity(refs[s])[1] for s in states};I={}
 for s in states:
  qprefix=empty;p=(0,0)
  for t in refs[s]:
   qprefix=xor(qprefix,shift(Q[t],p))
   h=(t//2+(1 if t%2==0 else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  I[s]=shift(xor(B,qprefix),(-z[s][0],-z[s][1]))
 edges=[(s,t,p) for s in states for t,p in phi[s]]
 R={}
 for s in states:ctx.reset_operations();R[s],_=relation(ctx,states,edges,s)
 bad=ctx.set(prefix+'{ [] : 0=1 }').params();frame_checks=0
 for s in states:
  ctx.reset_operations()
  black=I[s].intersect(origin).params().intersect(universe)
  wrong=black if s%2==0 else universe.subtract(black)
  bad=bad.union(wrong)
 # First the exact zero-depth slice, then all depths. A contradiction already
 # covering every parameter value is a complete NO, not a capped search.
 for initial_slice in (True,False):
  for s in states:
   ctx.reset_operations();current=pull(I[s],r='r+1')
   for t,p in phi[s]:
    ctx.reset_operations();guard=shift(R[t],p)
    if initial_slice:guard=guard.intersect(base)
    discrepancy=xor(current.intersect(guard),shift(I[t],p).intersect(guard))
    bad=bad.union(discrepancy.params().intersect(universe));frame_checks+=1
    if universe.subtract(bad).is_empty():
     return dict(status='decided',mass_bound=M,possible=False,growing=len(phi[root])>1,accepted_growing_model=False,
      feasible_parameters=str(universe.subtract(bad)),parameter_names=names,
      witness_assignment=None,seed=None,frame_checks=frame_checks,
      rejected_by_zero_depth_slice=initial_slice)
    current=xor(current,shift(Q[t],p))
 feasible=universe.subtract(bad).coalesce();possible=not feasible.is_empty()
 seed=None;assignment=None
 if possible:
  assignment=sample_parameters(feasible,len(names)) if names else ()
  seed=sorted({(assignment[3*i+1],assignment[3*i+2]) for i in range(M) if assignment[3*i]})
 return dict(status='decided',mass_bound=M,possible=possible,growing=len(phi[root])>1,accepted_growing_model=possible and len(phi[root])>1,
  feasible_parameters=str(feasible),parameter_names=names,witness_assignment=assignment,seed=seed,
  frame_checks=frame_checks)

def main():
 start=time.monotonic();ctx=Context(max_operations=30000000);records=[];invalid_template_checks=0
 otherctx=Context()
 for bad_template in [ctx.set('[p] -> { [r,x,y] : r>=0 and x=p and y=0 }'),ctx.set('{ [r,x] : r>=0 and x=0 }'),ctx.set('{ [x,r,y] : r>=0 and x=0 and y=0 }'),otherctx.set('{ [r,x,y] : r>=0 and x=0 and y=0 }')]:
  try:solve(ctx,['R','L']*4,0,{0:bad_template},0)
  except ValueError:invalid_template_checks+=1
  else:raise AssertionError('malformed parity relation accepted')
 for root in (0,1):
  Q={root:periodic_set(ctx,[{(0,0)}])}
  for M in (0,1,2):
   r=solve(ctx,['R','L']*4,root,Q,M)
   assert r['possible']==(root==0 or M>=1)
   if r['possible']:assert ((0,0) in r['seed'])==(root==1)
   r['name']='identity_R' if root==0 else 'identity_L';records.append(r);print(r['name'],M,r['possible'],flush=True)
 images=['RRRRR','LLLLL']*4;Q={}
 for h in range(4):
  Q[2*h]=periodic_set(ctx,[read_parity([2*((h+j)%4) for j in range(n)])[0] for n in (1,5)])
 for M in (0,1,2):
  r=solve(ctx,images,0,Q,M);assert r['status']=='decided' and not r['possible']
  r['name']='right_five';records.append(r);print(r['name'],M,r['possible'],flush=True)
 badQ=dict(Q);badQ[0]=periodic_set(ctx,[set()]);bad=solve(ctx,images,0,badQ,1)
 assert bad['status']=='invalid parity certificate';bad['name']='forged_parity_base';records.append(bad)
 badQ=dict(Q);badQ[0]=periodic_set(ctx,[{(0,0)}]);bad=solve(ctx,images,0,badQ,1)
 assert bad['status']=='invalid parity certificate' and bad['kind']=='recurrence'
 bad['name']='forged_parity_recurrence';records.append(bad)
 out=dict(libisl_version=ctx.version,invalid_template_rejections=invalid_template_checks,records=records,decided_cases=sum(r['status']=='decided' for r in records),
  accepted_growing_models=sum(r.get('possible',False) and r.get('growing',False) for r in records),
  scope='All-coordinate bounded-seed solver with exact supplied parity certificates at A=I; general extraction remains absent.',seconds=time.monotonic()-start)
 (HERE/'presburger_bounded_seed.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
 print([(r['name'],r.get('mass_bound'),r.get('possible'),r.get('seed')) for r in records])
if __name__=='__main__':main()
