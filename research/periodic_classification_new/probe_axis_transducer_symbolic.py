#!/usr/bin/env python3
"""Arbitrary-length next-row necessary ordinal/first-return constraints.
Literal transducer paths are supplied. SAT is a relaxation, UNSAT solver only.
"""
from pathlib import Path
from itertools import permutations
import sys,json,time
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj
from probe_axis_layer_transducer import second,extend,describe

def make(trans,depth=3,timeout=10000):
 m=len(trans);pi=[k for k,w in trans];beta=[b for j,k,l,b,w in describe(trans)]
 p=[f'p{i}' for i in range(m)];q=[f'q{i}' for i in range(m)];ks=[f'k{i}' for i in range(m)];ls=[f'l{i}' for i in range(m)]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun z () Int)']
 def add(s):lines.append('(assert '+s+')')
 def even(x):return f'(= (mod {x} 2) 0)'
 def sg(x):return f'(ite {even(x)} 1 (- 1))'
 def summ(xs):return '0' if not xs else xs[0] if len(xs)==1 else '(+ '+' '.join(xs)+')'
 def marked(xs,x):return disj([f'(= {x} {a})' for a in xs])
 def east(xs,x):return f'(xor {marked(xs,x)} (not {even(x)}))'
 def ec(xs,x):return f'(+ (div {x} 2) '+summ([f'(ite (< {a} {x}) {sg(a)} 0)' for a in xs])+')'
 def count(xs,x,E):return ec(xs,x) if E else f'(- {x} {ec(xs,x)})'
 add(f'(>= z {m})')
 for x in p+q+ks+ls:lines.append(f'(declare-fun {x} () Int)');add(f'(and (<= 0 {x}) (< {x} z))')
 for xs in [p,q]:
  for a,b in zip(xs,xs[1:]):add(f'(< {a} {b})')
 add(f'(= {summ(list(map(sg,p)))} {summ(list(map(sg,q)))})')
 for x in p+q:
  balance=f'(- {summ([f"(ite (<= {a} {x}) {sg(a)} 0)" for a in q])} {summ([f"(ite (<= {a} {x}) {sg(a)} 0)" for a in p])})'
  add(f'(>= {balance} 0)')
 for j,(pj,qj,k,l) in enumerate(zip(p,q,ks,ls)):
  add(f'(= {east(p,k)} {even(qj)})')
  add(f'(ite {even(qj)} (= {count(p,k,True)} {count(q,qj,True)}) (= {count(p,k,False)} {count(q,qj,False)}))')
  add(f'(= {east(q,l)} {even(pj)})')
  add(f'(ite {even(pj)} (= {count(p,pj,True)} {count(q,l,True)}) (= {count(p,pj,False)} {count(q,l,False)}))')
 add('(distinct '+' '.join(ks)+')')
 for starts,ends,par in [(q,[ls[pi[j]] for j in range(m)],[p[pi[j]] for j in range(m)]),(ks,[p[pi[j]] for j in range(m)],q)]:
  for length in range(1,min(depth,m)+1):
   for seq in permutations(range(m),length):
    chain=conj([f'(= {ends[a]} {starts[b]})' for a,b in zip(seq,seq[1:])]);end=ends[seq[-1]];start=starts[seq[0]]
    proper='true' if length<m else f'(> z {m})'
    chain=f'(and {chain} {proper})'
    add(f'(=> {chain} '+conj([f'(distinct {end} {starts[j]})' for j in seq])+')')
    weights=[f'(- {beta[j]} (mod {par[j]} 2))' for j in seq];w=summ(weights)
    add(f'(=> {chain} (ite (> {w} 0) (< {end} {start}) (> {end} {start})))')
    first=conj([f'(distinct {summ(weights[:k])} 0)' for k in range(1,length)])
    add(f'(=> (and {chain} (= {w} 0) {first}) (= {end} (+ {start} 1)))')
 return '\n'.join(lines)+'\n'

def run(trans,label,depth=3,timeout=10000):
 text=make(trans,depth,timeout);base=Path(__file__).with_name('axis_transducer_'+label);base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());start=time.time();ans=solve(ctx,sol)
 result=dict(label=label,ports=len(trans),depth=depth,next_row_length='UNBOUNDED',status={1:'SAT_ORDINAL_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-start)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 return result
if __name__=='__main__':
 for a in (0,2):
  for L in range(a+4,a+10):
   run(extend(L,[a,a+1,a+2],[a,a+2,a+3],second(4,0)),f'A_a{a}_L{L}')
 for a in (0,2):
  for c in range(a+4,a+10,2):
   for L in range(c+3,c+6):
    run(extend(L,[a,a+1,a+2,c+2],[a,a+2,a+3,c],second(5,0)),f'B_a{a}_c{c}_L{L}')
 for a in (0,2):
  for b in range(a+4,a+10,2):
   for L in range(b+3,b+6):
    run(extend(L,[a+2,b-1,b,b+2],[a,b,b+1,b+2],second(5,2)),f'C_a{a}_b{b}_L{L}')
