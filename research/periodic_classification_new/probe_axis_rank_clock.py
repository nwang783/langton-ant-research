#!/usr/bin/env python3
"""Exploratory unbounded-rank exact-clock necessary conditions."""
from pathlib import Path
import sys,json,time
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj
from probe_axis_layer_transducer import *

def make(trans,spread=1,timeout=20000):
 m=len(trans);pi=[k for k,w in trans];beta=[b for j,k,l,b,w in describe(trans)];lengths=[len(w) for k,w in trans];B=sum(lengths)-m
 p=[f'p{i}' for i in range(m)];q=[f'q{i}' for i in range(m)]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun z () Int)','(declare-fun P () Int)']
 def add(s):lines.append('(assert '+s+')')
 def decl(x):lines.append(f'(declare-fun {x} () Int)')
 def even(x):return f'(= (mod {x} 2) 0)'
 def sg(x):return f'(ite {even(x)} 1 (- 1))'
 def summ(xs):return '0' if not xs else xs[0] if len(xs)==1 else '(+ '+' '.join(xs)+')'
 def marked(xs,x):return disj([f'(= {x} {a})' for a in xs])
 def east(xs,x):return f'(xor {marked(xs,x)} (not {even(x)}))'
 def ec(xs,x):return f'(+ (div {x} 2) '+summ([f'(ite (< {a} {x}) {sg(a)} 0)' for a in xs])+')'
 def count(xs,x,E):return ec(xs,x) if E else f'(- {x} {ec(xs,x)})'
 def valid(x):return f'(and (<= 0 {x}) (< {x} z))'
 add(f'(>= z {m})');add(f'(>= P (+ {B} (* 2 z)))');add('(= (mod P 4) 0)')
 for x in p+q:decl(x);add(valid(x))
 for xs in [p,q]:
  for a,b in zip(xs,xs[1:]):add(f'(< {a} {b})')
 add(f'(= {summ(list(map(sg,p)))} {summ(list(map(sg,q)))})')
 nodes=[[],[]]
 def node(side,rank,label):
  clock='t_'+label;decl(clock);nodes[side].append((rank,clock));return clock
 cp=[node(0,r,r) for r in p];dq=[node(1,r,r) for r in q]
 for j in range(m):add(f'(= {cp[pi[j]]} (+ {dq[j]} {lengths[j]} (* (- {beta[j]}) P)))')
 # Every designated source event has an exact matched horizontal partner.
 def edge(side,rank,label):
  dest='v_'+label;decl(dest);srcclock=node(side,rank,label);dstclock=node(1-side,dest,'v_'+label)
  add(f'(=> {valid(rank)} {valid(dest)})')
  C,D=(rank,dest) if side==0 else (dest,rank);tc,td=(srcclock,dstclock) if side==0 else (dstclock,srcclock)
  E=east(p,C)
  add(f'(=> {valid(rank)} (= {E} {east(q,D)}))')
  add(f'(=> {valid(rank)} (ite {E} (= {ec(p,C)} {ec(q,D)}) (= {count(p,C,False)} {count(q,D,False)})))')
  add(f'(=> {valid(rank)} (= {td} (+ {tc} 1 (ite {E} 0 P))))')
  return dest
 first=[]
 for side,xs in enumerate([p,q]):
  for i,r in enumerate(xs):first.append((1-side,edge(side,r,f's{side}i{i}')))
 for side,r in list(enumerate([])):pass
 # Include neighborhoods of both marked ranks and their horizontal partners.
 roots=[(0,r,'p'+str(i)) for i,r in enumerate(p)]+[(1,r,'q'+str(i)) for i,r in enumerate(q)]+[(s,r,'v'+str(i)) for i,(s,r) in enumerate(first)]
 for side,r,label in roots:
  for d in range(-spread,spread+1):
   if d:edge(side,f'(+ {r} {d})',label+'d'+str(d).replace('-','m'))
 for side in range(2):
  for a,ta in nodes[side]:
   for b,tb in nodes[side]:
    add(f'(=> (and {valid(a)} {valid(b)}) (ite (< {a} {b}) (< {ta} {tb}) (ite (= {a} {b}) (= {ta} {tb}) (> {ta} {tb}))))')
 return '\n'.join(lines)+'\n'
def run(trans,label,spread=1,timeout=20000):
 text=make(trans,spread,timeout);base=Path(__file__).with_name('axis_rank_clock_'+label);base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());t=time.time();ans=solve(ctx,sol)
 result=dict(label=label,ports=len(trans),spread=spread,status={1:'SAT_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-t)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 return result
if __name__=='__main__':
 for L in range(4,9):run(extend(L,[0,1,2],[0,2,3],second(4,0)),f'A_a0_L{L}')
