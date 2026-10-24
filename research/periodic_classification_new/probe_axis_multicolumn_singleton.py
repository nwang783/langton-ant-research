#!/usr/bin/env python3
"""Necessary all-rank clocks above a negative-axis all-singleton bottom row.
SAT is not a front. It only tests whether the two-class proof generalizes locally.
"""
from pathlib import Path
import sys,json,time
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj

def make(k,spread=1,timeout=20000,phase_bound=2):
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)']
 def decl(x):lines.append(f'(declare-fun {x} () Int)');return x
 def add(s):lines.append('(assert '+s+')')
 def even(x):return f'(= (mod {x} 2) 0)'
 def valid(cell,x):return f'(and (<= 0 {x}) (< {x} n{cell}))'
 def mark(cell):return ('p' if cell%2==0 else 'q')+str(cell//2)
 def east(cell,x):return f'(xor (= {x} {mark(cell)}) (not {even(x)}))'
 def ec(cell,x):return f'(- (div {x} 2) (ite (< {mark(cell)} {x}) 1 0))'
 def wc(cell,x):return f'(- {x} {ec(cell,x)})'
 for cell in range(2*k):decl('n'+str(cell));decl(mark(cell));add(valid(cell,mark(cell)));add('(= (mod '+mark(cell)+' 2) 1)')
 add('(>= P (+ '+str(2*k)+' '+' '.join('n'+str(c) for c in range(2*k))+'))');add('(= (mod P 4) 0)')
 add('(>= P (* 2 (+ '+' '.join('n'+str(c) for c in range(2*k))+')))')
 for i in range(k):
  C=2*i;D=C+1;prev=2*((i-1)%k)+1
  add(f'(= {ec(C,"n"+str(C))} {ec(D,"n"+str(D))})')
  add(f'(= {wc(C,"n"+str(C))} {wc(prev,"n"+str(prev))})')
 nodes=[[] for c in range(2*k)]
 def node(cell,rank,label):
  t=decl('t_'+label);nodes[cell].append((rank,t));return t
 for i in range(k):
  tc=node(2*i,'p'+str(i),'p'+str(i));td=node(2*i+1,'q'+str(i),'q'+str(i));add(f'(= {tc} (+ {td} 3))')
 # Track separate E/W partner possibilities, guarded by exact local heading.
 def edge(cell,rank,label):
  ts=node(cell,rank,label);ret=[];i=cell//2
  for E in (0,1):
   if cell%2==0:dest=2*i+1 if E else 2*((i-1)%k)+1;seam=1 if not E and i==0 else 0
   else:dest=2*i if E else 2*((i+1)%k);seam=1 if not E and i==k-1 else 0
   d=decl('v_'+label+str(E));td=node(dest,d,'v_'+label+str(E));ret.append((dest,d))
   guard=f'(and {valid(cell,rank)} '+(east(cell,rank) if E else '(not '+east(cell,rank)+')')+')'
   add(f'(=> {guard} {valid(dest,d)})');add(f'(=> {guard} '+(east(dest,d) if E else '(not '+east(dest,d)+')')+')')
   count=ec if E else wc
   add(f'(=> {guard} (= {count(cell,rank)} {count(dest,d)}))')
   tc,tx=(ts,td) if cell%2==0 else (td,ts)
   add(f'(=> {guard} (= {tx} (+ {tc} 1 (* (- {seam}) P))))')
   # Inactive partner must be outside its cell so local-order constraints ignore it.
   add(f'(=> (not {guard}) (= {d} (- 1)))')
  return ret
 roots=[]
 for cell in range(2*k):roots.append((cell,mark(cell),'m'+str(cell)));roots += [(d,r,'partner'+str(cell)+'_'+str(j)) for j,(d,r) in enumerate(edge(cell,mark(cell),'base'+str(cell)))]
 for cell,r,label in roots:
  for a in range(-spread,spread+1):
   if a:edge(cell,f'(+ {r} {a})',label+'d'+str(a).replace('-','m'))
 for cell,ns in enumerate(nodes):
  for a,ta in ns:
   for b,tb in ns:add(f'(=> (and {valid(cell,a)} {valid(cell,b)}) (ite (< {a} {b}) (< {ta} {tb}) (ite (= {a} {b}) (= {ta} {tb}) (> {ta} {tb}))))')

 for ca,ns in enumerate(nodes):
  for cb in range(ca,len(nodes)):
   for a,ta in ns:
    for b,tb in nodes[cb]:
     guard=f'(and {valid(ca,a)} {valid(cb,b)} '+(f'(distinct {a} {b})' if ca==cb else 'true')+')'
     for v in range(-phase_bound,phase_bound+1):add(f'(=> {guard} (distinct (- {ta} {tb}) (* {v} P)))')
 return '\n'.join(lines)+'\n'
def run(k,spread=1,timeout=20000):
 text=make(k,spread,timeout);base=Path(__file__).with_name(f'axis_negative_singletons_k{k}_s{spread}_phase2');base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());t=time.time();ans=solve(ctx,sol)
 result=dict(full_drift=[-2*k,0],bottom='ALL_SINGLETON',spread=spread,status={1:'SAT_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-t)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
