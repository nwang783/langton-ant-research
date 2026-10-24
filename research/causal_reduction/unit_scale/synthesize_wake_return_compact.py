"""Prepared104-wake return synthesis in the exact fixed cylinder.
Concrete target drift(-2,-2), same physical sector as its forward producer.
Input bits are the complete mature wake profile, not assumed white.
Only a SAT model with complete literal replay is a construction. Finite-strip
UNSAT or UNKNOWN is not an unbounded no-go. No cap is supplied.
"""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
from synthesize_axis_compact_clock import values
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj
from synthesize_cap_three_cylinder import check_model
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
def base(p):return(p[0]-p[1],p[0]%2)in W
def make(cap,K,H,timeout,pattern='free',real=True,dy=2,fixed_override=None,sector=1,offset=(0,-4)):
 dx=2*K;ps=[(x,(dy*x)//dx+y) for y in range(H) for x in range(dx)];ix={p:i for i,p in enumerate(ps)}
 fixed={(2*i,0):(3,) for i in range(K)};fixed.update({(2*i+1,0):(2,) for i in range(K)})
 if pattern=='odd13':
  assert K==2
  fixed.update({(0,1):(2,0,2,2),(1,1):(3,3,3,1),(2,1):(2,2,2,0),(3,1):(3,1,3,3)})
 elif pattern=='even02':
  assert K==2
  for i,q in enumerate((0,2)):
   fixed[2*i,1]=tuple(0 if j==q+2 else 2 for j in range(6))
   fixed[2*i+1,1]=tuple(((3 if j%2==0 else 1)+ (2 if j==q else 0))%4 for j in range(6))
 elif pattern=='free':fixed={}
 elif pattern!='singleton':raise ValueError(pattern)
 if fixed_override is not None:fixed=fixed_override
 assert max(map(len,fixed.values()),default=0)<=cap
 sort='Real' if real else 'Int';lines=['(set-logic QF_LIRA)' if real else '(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)']
 def add(s):lines.append('(assert '+s+')')
 def port(i,j,h,kind):
  axis=(sector-sum(ps[i])-sum(offset))%2
  incoming=h if kind=='i' else (h-(1 if (j+int(base((ps[i][0]+offset[0],ps[i][1]+offset[1]))))%2==0 else -1))%4
  assert incoming%2==axis
  b=f'b{i}_{j}';return b if incoming==axis+2 else f'(not {b})'
 for i,p in enumerate(ps):
  axis=(sector-sum(p)-sum(offset))%2;lines.append(f'(declare-fun n{i} () Int)');add(f'(and (<= 0 n{i}) (<= n{i} {cap}))')
  for j in range(cap):
   lines += [f'(declare-fun b{i}_{j} () Bool)',f'(declare-fun t{i}_{j} () {sort})'];add(f'(=> (<= n{i} {j}) (not b{i}_{j}))')
   if j:add(f'(=> (> n{i} {j}) (>= t{i}_{j} (+ t{i}_{j-1} 4)))')
  if p in fixed:
   hs=fixed[p];add(f'(= n{i} {len(hs)})')
   for j,h in enumerate(hs):assert h%2==axis;add(f'(= b{i}_{j} '+('true' if h==axis+2 else 'false')+')')
  for kind in ('i','o'):
   for h in range(4):
    if h%2!=(axis if kind=='i' else 1-axis):continue
    lines.append(f'(define-fun {kind}{i}_{h}_0 () Int 0)')
    for j in range(cap):
     lines.append(f'(define-fun {kind}{i}_{h}_{j+1} () Int (+ {kind}{i}_{h}_{j} (ite (and (> n{i} {j}) {port(i,j,h,kind)}) 1 0)))')
 add('(= P (+ '+' '.join(f'n{i}' for i in range(len(ps)))+'))');add('(> P 0)');add('(= (mod P 4) 0)');add(f'(= t{min((ix[p] for p,hs in fixed.items() if hs),default=0)}_0 0)')
 if pattern=='free' and fixed_override is None:add('(> n0 0)')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2==(1-sector+sum(p)+sum(offset))%2:
    x,y=p[0]+ax,p[1]+ay;k=x//dx;v=-k;q=(x%dx,y-k*dy);z=ix.get(q)
    if z is None:add(f'(= o{i}_{h}_{cap} 0)');continue
    add(f'(= o{i}_{h}_{cap} i{z}_{h}_{cap})')
    for j in range(cap):
     for k in range(cap):
      g=conj([f'(> n{i} {j})',f'(> n{z} {k})',port(i,j,h,'o'),port(z,k,h,'i'),f'(= o{i}_{h}_{j} i{z}_{h}_{k})'])
      add(f'(=> {g} (= (+ t{z}_{k} (* {v} P)) (+ t{i}_{j} 1)))')
   else:
    xx=p[0]-ax;q=(xx%dx,p[1]-ay-(xx//dx)*dy)
    if q not in ix:add(f'(= i{i}_{h}_{cap} 0)')
 return '\n'.join(lines)+'\n',ps

def run(cap=10,height=13,sector=1,timeout=60000,fixed_override=None,offset=(0,-4)):
 offset=tuple(offset)
 txt,ps=make(cap,1,height,timeout,sector=sector,offset=offset,fixed_override=fixed_override)
 name=P/f'wake_return_compact_cap{cap}_h{height}_sector{sector}_off{offset[1]}'
 name.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.monotonic();ans=solve(ctx,sol)
 out=dict(scope=__doc__,cap=cap,height=height,offset=offset,sector=sector,status={1:'SAT_PENDING_REPLAY',-1:'UNSAT_FIXED_STRIP_SOLVER_ONLY',0:'UNKNOWN'}[ans],seconds=time.monotonic()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();name.with_suffix('.model').write_text(mt);v=values(mt);vv={'P':int(v['P'])};ss=[]
  for i,p in enumerate(ps):
   n=int(v[f'n{i}']);axis=(sector-sum(p)-sum(offset))%2;hs=[axis+2*int(v[f'b{i}_{j}'])for j in range(n)]
   b=int(base((p[0]+offset[0],p[1]+offset[1])))
   hist=[(1 if(j+b)%2==0 else -1,h)for j,h in enumerate(hs)];ss.append([(''.join(map(str,hs)),hist)]);vv[f's{i}']=0
   for j in range(n):assert v[f't{i}_{j}'].denominator==1;vv[f't{i}_{j}']=int(v[f't{i}_{j}'])
  cert=check_model(vv,ps,ss,(-2,-2));out['certificate_normalized']=cert
  out['physical_head']=[[cert['head'][0][0]+offset[0],cert['head'][0][1]+offset[1]],cert['head'][1]]
  out['status']='SAT_RECONSTRUCTED_BULK_INPUT'
 if ans==0:out['reason']=reason(ctx,sol).decode()
 name.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);return out
if __name__=='__main__':run()
