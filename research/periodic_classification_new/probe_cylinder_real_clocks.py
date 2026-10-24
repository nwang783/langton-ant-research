#!/usr/bin/env python3
"""Exact real-clock variants of a saved discrete-state cylinder formula.
The cycle identity makes all active clocks integral after anchoring. Solver
outcomes are fixed-strip only and are not independent UNSAT certificates.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import sys,json,time,re,hashlib
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import check_model

def number(s):
 s=s.strip()
 if s.startswith('(- ') and s.endswith(')'):return -number(s[3:-1])
 if s.startswith('(/ ') and s.endswith(')'):
  a,b=s[3:-1].split();return number(a)/number(b)
 return Fraction(s)

def run(cap,dx,dy,w,to,variant):
 root=Path(__file__).parent;base=root/f'white_cap{cap}_d{dx}_{dy}_w{w}'
 src=base.with_suffix('.smt2').read_text();txt=re.sub(r'\(set-option :timeout \d+\)',f'(set-option :timeout {to})',src)
 txt=txt.replace('(set-logic QF_LIA)','(set-logic QF_LIRA)' if variant==0 else '(set-logic QF_LRA)')
 txt=re.sub(r'(\(declare-fun t\d+_\d+ \(\)) Int\)',r'\1 Real)',txt)
 txt=re.sub(r'(\(define-fun [io]\d+_\d+t\d+ \(\)) Int ',r'\1 Real ',txt)
 if variant==1:
  txt=txt.replace('() Int','() Real')
  n=2**(cap+1)-1
  for name in re.findall(r'\(declare-fun (s\d+) \(\) Real\)',txt):
   txt+='(assert (or '+' '.join(f'(= {name} {j})' for j in range(n))+'))\n'
 out=root/f'white_real{variant}_cap{cap}_d{dx}_{dy}_w{w}'
 out.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());start=time.time();ans=solve(ctx,sol)
 result=dict(cap=cap,drift=[dx,dy],width=w,variant=variant,timeout_ms=to,status={-1:'UNSAT_FIXED_STRIP_REAL_CLOCKS',0:'UNKNOWN',1:'SAT_PENDING_REPLAY'}[ans],seconds=time.time()-start,source_sha256=hashlib.sha256(src.encode()).hexdigest())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();out.with_suffix('.model').write_text(mt)
  vals={key:number(v) for key,v in re.findall(r'^(P|s\d+|t\d+_\d+) -> (.*)$',mt,re.M)}
  ps=[(r,(dy*r)//dx+v) for v in range(-w,w+1) for r in range(dx)];ss=[]
  for p in ps:
   a=1-sum(p)%2;hh=[()]+[hs for n in range(1,cap+1) for hs in product((a,a+2),repeat=n)]
   ss.append([(''.join(str(h) for h in hs),[(1 if j%2==0 else -1,h) for j,h in enumerate(hs)]) for hs in hh])
  required=['P']+['s'+str(i) for i in range(len(ps))]
  assert all(vals[k].denominator==1 for k in required)
  integers={k:int(vals[k]) for k in required}
  for i in range(len(ps)):
   for j in range(len(ss[i][integers['s'+str(i)]][1])):
    k=f't{i}_{j}';assert vals[k].denominator==1;(integers.__setitem__(k,int(vals[k])))
  result['certificate']=check_model(integers,ps,ss,(dx,dy));result['status']='SAT_RECONSTRUCTED_REAL_CLOCKS'
 out.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
