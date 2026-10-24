#!/usr/bin/env python3
"""Unbounded next-row history, supplied singleton-boundary second row.
Second row has length n, one C arrival at r+2 and one D departure at r,
where r is even. Tests necessary top-port matching and <=2-bounce returns.
SAT is only a local ordinal relaxation; solver UNSAT is not a proof artifact.
"""
from pathlib import Path
from itertools import permutations
import sys,json,time
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj

def make(n,r,timeout=10000):
 assert n>=4 and r%2==0 and 0<=r<n-2
 m=n-1;p=[f'p{i}' for i in range(m)];q=[f'q{i}' for i in range(m)];ks=[f'k{i}' for i in range(m)];ls=[f'l{i}' for i in range(m)]
 pi=list(range(m));pi[r],pi[r+1]=pi[r+1],pi[r]
 beta=[j%2 if j<=r+1 else 1-j%2 for j in range(m)]
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
 # No equality of total marked-port counts: arbitrary omitted suffixes.
 for x in p+q:
  balance=f'(- {summ([f"(ite (<= {a} {x}) {sg(a)} 0)" for a in q])} {summ([f"(ite (<= {a} {x}) {sg(a)} 0)" for a in p])})'
  add(f'(=> (and (<= {x} {p[-1]}) (<= {x} {q[-1]})) (>= {balance} 0))')
 for j,(pj,qj,k,l) in enumerate(zip(p,q,ks,ls)):
  add(f'(=> (<= {k} {p[-1]}) (= {east(p,k)} {even(qj)}))')
  add(f'(=> (<= {k} {p[-1]}) (ite {even(qj)} (= {count(p,k,True)} {count(q,qj,True)}) (= {count(p,k,False)} {count(q,qj,False)})))')
  add(f'(=> (<= {l} {q[-1]}) (= {east(q,l)} {even(pj)}))')
  add(f'(=> (<= {l} {q[-1]}) (ite {even(pj)} (= {count(p,pj,True)} {count(q,l,True)}) (= {count(p,pj,False)} {count(q,l,False)})))')
 add('(distinct '+' '.join(ks)+')')
 for starts,ends,par in [(q,[ls[pi[j]] for j in range(m)],[p[pi[j]] for j in range(m)]),(ks,[p[pi[j]] for j in range(m)],q)]:
  for length in range(1,3):
   for seq in permutations(range(m),length):
    chain=conj([f'(= {ends[a]} {starts[b]})' for a,b in zip(seq,seq[1:])]);end=ends[seq[-1]];start=starts[seq[0]]
    add(f'(=> {chain} '+conj([f'(distinct {end} {starts[j]})' for j in seq])+')')
    weights=[f'(- {beta[j]} (mod {par[j]} 2))' for j in seq];w=summ(weights)
    add(f'(=> {chain} (ite (> {w} 0) (< {end} {start}) (> {end} {start})))')
    first=conj([f'(distinct {summ(weights[:k])} 0)' for k in range(1,length)])
    add(f'(=> (and {chain} (= {w} 0) {first}) (= {end} (+ {start} 1)))')
 return '\n'.join(lines)+'\n'

def run(n,r,timeout=10000):
 text=make(n,r,timeout);base=Path(__file__).with_name(f'axis_singleton_prefix_n{n}_r{r}');base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());start=time.time();ans=solve(ctx,sol)
 result=dict(second_row_length_lower_bound=n,core_rank=r,next_row_length='UNBOUNDED',omitted_suffix='ARBITRARY',status={1:'SAT_ORDINAL_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-start)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
