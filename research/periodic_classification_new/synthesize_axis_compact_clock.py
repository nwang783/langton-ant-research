#!/usr/bin/env python3
"""Compact exact fixed-cylinder white-front clock synthesis.
No exponential local-state enumeration. SAT models must reconstruct and replay.
Finite-strip solver UNSAT/UNKNOWN is not an unrestricted classification theorem.
New producer implementation, not independently audited.
"""
from pathlib import Path
from fractions import Fraction
import re,json,sys,time
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj
from synthesize_cap_three_cylinder import check_model

def values(mt):
 out={}
 for key,expr in re.findall(r'^(\w+) -> ([^\n]+)$',mt,re.M):
  if expr in ('true','false'):out[key]=expr=='true';continue
  toks=re.findall(r'\(|\)|[^\s()]+',expr);it=iter(toks)
  def read(t=None):
   t=next(it) if t is None else t
   if t!='(':return Fraction(t)
   op=next(it);a=read();z=next(it)
   if z==')':assert op=='-';return -a
   b=read(z);assert next(it)==')';return a/b if op=='/' else a-b
  try:out[key]=read()
  except (ValueError,StopIteration,AssertionError):pass
 return out

def make(cap,K,H,timeout,pattern='odd13',real=True,dy=0,fixed_override=None):
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
  axis=1-sum(ps[i])%2
  incoming=h if kind=='i' else (h-(1 if j%2==0 else -1))%4
  assert incoming%2==axis
  b=f'b{i}_{j}';return b if incoming==axis+2 else f'(not {b})'
 for i,p in enumerate(ps):
  axis=1-sum(p)%2;lines.append(f'(declare-fun n{i} () Int)');add(f'(and (<= 0 n{i}) (<= n{i} {cap}))')
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
   if h%2==sum(p)%2:
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

def run(cap,K,H,timeout=60000,pattern='odd13',real=True):
 txt,ps=make(cap,K,H,timeout,pattern,real);base=Path(__file__).with_name(f'axis_compact_k{K}_cap{cap}_H{H}_{pattern}_'+('real' if real else 'int'));base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(full_drift=[-2*K,0],cap=cap,height=H,pattern=pattern,clock_sort='Real' if real else 'Int',status={1:'SAT_PENDING_REPLAY',-1:'UNSAT_FIXED_STRIP_SOLVER_ONLY',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);vv={'P':int(v['P'])};ss=[]
  for i,p in enumerate(ps):
   n=int(v[f'n{i}']);axis=1-sum(p)%2;hs=[axis+2*int(v[f'b{i}_{j}']) for j in range(n)];hist=[(1 if j%2==0 else -1,h) for j,h in enumerate(hs)];ss.append([(''.join(map(str,hs)),hist)]);vv[f's{i}']=0
   for j in range(n):assert v[f't{i}_{j}'].denominator==1;vv[f't{i}_{j}']=int(v[f't{i}_{j}'])
  result['certificate']=check_model(vv,ps,ss,(-2*K,0));result['status']='SAT_RECONSTRUCTED'
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
 args=sys.argv[1:];run(*map(int,args[:4]),*(args[4:5]),bool(int(args[5])) if len(args)>5 else True)
