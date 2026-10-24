#!/usr/bin/env python3
"""Unbounded upper multiplicity, fixed extreme multiplicity relaxation.
Only symbolic ordinal matching, first returns and a necessary port ballot.
SAT is not a front; UNSAT outputs are solver results, not proof certificates.
"""
import sys,json,time
from pathlib import Path
from itertools import permutations
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj

def make(m,timeout=30000):
 p=[f'p{i}' for i in range(m)];q=[f'q{i}' for i in range(m)];ks=[f'k{i}' for i in range(m)];ls=[f'l{i}' for i in range(m)]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun n () Int)']
 def add(s):lines.append('(assert '+s+')')
 def even(x):return f'(= (mod {x} 2) 0)'
 def sg(x):return f'(ite {even(x)} 1 (- 1))'
 def summ(xs):return '0' if not xs else xs[0] if len(xs)==1 else '(+ '+' '.join(xs)+')'
 def marked(xs,x):return disj([f'(= {x} {r})' for r in xs])
 def east(xs,x):return f'(xor {marked(xs,x)} (not {even(x)}))'
 def ec(xs,x):return f'(+ (div {x} 2) '+summ([f'(ite (< {r} {x}) {sg(r)} 0)' for r in xs])+')'
 def count(xs,x,E):return ec(xs,x) if E else f'(- {x} {ec(xs,x)})'
 def bal(x):return f'(- {summ([f"(ite (<= {r} {x}) {sg(r)} 0)" for r in q])} {summ([f"(ite (<= {r} {x}) {sg(r)} 0)" for r in p])})'
 add(f'(>= n {m})')
 for x in p+q+ks+ls:lines.append(f'(declare-fun {x} () Int)');add(f'(and (<= 0 {x}) (< {x} n))')
 for xs in [p,q]:
  for a,b in zip(xs,xs[1:]):add(f'(< {a} {b})')
 add(f'(= {summ(list(map(sg,p)))} {summ(list(map(sg,q)))})')
 for x in p+q:add(f'(>= {bal(x)} 0)')
 for j,(pj,qj,k,l) in enumerate(zip(p,q,ks,ls)):
  # Every downward target has E iff its local rank is even.
  add(f'(= {east(p,k)} {even(qj)})')
  add(f'(ite {even(qj)} (= {count(p,k,True)} {count(q,qj,True)}) (= {count(p,k,False)} {count(q,qj,False)}))')
  # C_k -> D_qj -> bottom -> C_pj, physical first return iff qj,j same parity.
  if j%2==0:add(f'(ite {even(qj)} (= {pj} (+ {k} 1)) (> {pj} {k}))')
  else:add(f'(ite {even(qj)} (< {pj} {k}) (= {pj} (+ {k} 1)))')
  # C_pj -> D_l, E iff pj even.
  add(f'(= {east(q,l)} {even(pj)})')
  add(f'(ite {even(pj)} (= {count(p,pj,True)} {count(q,l,True)}) (= {count(p,pj,False)} {count(q,l,False)}))')
  if j%2==0:add(f'(ite {even(pj)} (= {l} (+ {qj} 1)) (> {l} {qj}))')
  else:add(f'(ite {even(pj)} (< {l} {qj}) (= {l} (+ {qj} 1)))')
 if m>=2:
  add(even(q[0]));add(f'(= {p[0]} (+ {q[0]} 2))');add(even(q[1]))
 # All upper-row boundary paths after any finite sequence of lower bounces.
 # n>m follows already from p0>=2. Thus every <=4m-step path is proper.
 add('(distinct '+' '.join(ks)+')')
 for starts,ends,par in [(q,ls,p),(ks,p,q)]:
  for length in range(1,m+1):
   for seq in permutations(range(m),length):
    chain=conj([f'(= {ends[a]} {starts[b]})' for a,b in zip(seq,seq[1:])])
    end=ends[seq[-1]];start=starts[seq[0]]
    # A closed component cannot be the full front: n>m gives free upper ports.
    add(f'(=> {chain} '+conj([f'(distinct {end} {starts[j]})' for j in seq])+')')
    weights=[f'(- {j%2} (mod {par[j]} 2))' for j in seq]
    w=summ(weights)
    add(f'(=> {chain} (ite (> {w} 0) (< {end} {start}) (> {end} {start})))')
    first=conj([f'(distinct {summ(weights[:r])} 0)' for r in range(1,length)])
    add(f'(=> (and {chain} (= {w} 0) {first}) (= {end} (+ {start} 1)))')
 return '\n'.join(lines)+'\n' 

def run(m,timeout=30000):
 text=make(m,timeout);base=Path(__file__).with_name(f'axis_extreme_return_symbolic_m{m}');base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());start=time.time();ans=solve(ctx,sol)
 result=dict(m=m,upper_multiplicity='UNBOUNDED',status={1:'SAT_ORDINAL_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-start)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
