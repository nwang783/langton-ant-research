#!/usr/bin/env python3
"""Unbounded upper histories above uniform negative-axis bottom multiplicity.
Necessary exact edge clocks plus proper first physical returns. Solver probes only.
"""
from pathlib import Path
from itertools import permutations
import json,sys,time
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj

def make(K,m,depth=3,timeout=30000):
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)'];nodes=[[] for _ in range(2*K)]
 def decl(x):lines.append(f'(declare-fun {x} () Int)');return x
 def add(s):lines.append('(assert '+s+')')
 def even(x):return f'(= (mod {x} 2) 0)'
 def parity(x):return f'(mod {x} 2)'
 def sg(x):return f'(ite {even(x)} 1 (- 1))'
 def summ(xs):return '0' if not xs else xs[0] if len(xs)==1 else '(+ '+' '.join(xs)+')'
 p=[[decl(f'p{i}_{j}') for j in range(m)] for i in range(K)];q=[[decl(f'q{i}_{j}') for j in range(m)] for i in range(K)]
 n=[decl('n'+str(i)) for i in range(2*K)]
 marks=[x for pair in zip(p,q) for x in pair]
 def valid(c,x):return f'(and (<= 0 {x}) (< {x} {n[c]}))'
 def east(c,x):return f'(xor {disj([f"(= {x} {a})" for a in marks[c]])} (not {even(x)}))'
 def ec(c,x):return f'(+ (div {x} 2) '+summ([f'(ite (< {a} {x}) {sg(a)} 0)' for a in marks[c]])+')'
 def wc(c,x):return f'(- {x} {ec(c,x)})'
 def node(c,r,t,guard='true'):nodes[c].append((r,t,guard));add(f'(=> {guard} {valid(c,r)})');add(f'(=> {guard} (= (mod {t} 4) {1 if c%2==0 else 2}))')
 for c,xs in enumerate(marks):
  add(f'(>= {n[c]} {m})')
  for x in xs:add(valid(c,x))
  for a,b in zip(xs,xs[1:]):add(f'(< {a} {b})')
 add('(= (mod P 4) 0)');add('(>= P (+ '+str(2*K*m)+' '+summ(n)+'))')
 # The next active layer requires at least twice the remaining upper vertical ports.
 add('(>= P (* 2 '+summ(n)+'))')
 for i in range(K):
  C=2*i;Di=C+1;prev=2*((i-1)%K)+1
  add(f'(= {ec(C,n[C])} {ec(Di,n[Di])})');add(f'(= {wc(C,n[C])} {wc(prev,n[prev])})')
 cp=[[decl('tc'+str(i)+'_'+str(j)) for j in range(m)] for i in range(K)];dq=[[decl('td'+str(i)+'_'+str(j)) for j in range(m)] for i in range(K)]
 ks={};ls={}
 for i in range(K):
  for j in range(m):
   node(2*i,p[i][j],cp[i][j]);node(2*i+1,q[i][j],dq[i][j])
   t=(i+j%2)%K;wrap=1 if j%2 and i==K-1 else 0
   add(f'(= {cp[t][j]} (+ {dq[i][j]} 3 (* {wrap} P)))')
   k=decl(f'k{i}_{j}');tk=decl(f'tk{i}_{j}');ks[i,j]=k
   l=decl(f'l{i}_{j}');tl=decl(f'tl{i}_{j}');ls[i,j]=l
   for E in (0,1):
    g=even(q[i][j]) if E else '(not '+even(q[i][j])+')';c=2*(i if E else (i+1)%K);node(c,k,tk,g)
    add(f'(=> {g} '+(east(c,k) if E else '(not '+east(c,k)+')')+')')
    cnt=ec if E else wc;add(f'(=> {g} (= {cnt(c,k)} {cnt(2*i+1,q[i][j])}))')
    seam=1 if not E and i==K-1 else 0;add(f'(=> {g} (= {dq[i][j]} (+ {tk} 1 (* (- {seam}) P))))')
    g=even(p[i][j]) if E else '(not '+even(p[i][j])+')';c=2*(i if E else (i-1)%K)+1;node(c,l,tl,g)
    add(f'(=> {g} '+(east(c,l) if E else '(not '+east(c,l)+')')+')')
    add(f'(=> {g} (= {cnt(2*i,p[i][j])} {cnt(c,l)}))')
    seam=1 if not E and i==0 else 0;add(f'(=> {g} (= {tl} (+ {cp[i][j]} 1 (* (- {seam}) P))))')
 add(f'(= {cp[0][0]} 1)')
 for c,ns in enumerate(nodes):
  for a,ta,ga in ns:
   for b,tb,gb in ns:
    add(f'(=> (and {ga} {gb}) (ite (< {a} {b}) (< {ta} {tb}) (ite (= {a} {b}) (= {ta} {tb}) (> {ta} {tb}))))')
 ports=list(ks)
 for L in range(1,min(depth,len(ports))+1):
  for seq in permutations(ports,L):
   for side in ('C','D'):
    guards=[f'(> P {4*L})'];weights=[]
    for z,(i,j) in enumerate(seq):
     t=(i+j%2)%K
     par=q[i][j] if side=='C' else p[t][j]
     weights.append(f'(- {j%2} {parity(par)})')
     if z+1<L:
      ni,nj=seq[z+1]
      if side=='C':guards += [f'(= (mod (+ {ni} {parity(q[ni][nj])}) {K}) {t})',f'(= {p[t][j]} {ks[ni,nj]})']
      else:guards += [f'(= (mod (- {t} {parity(p[t][j])}) {K}) {ni})',f'(= {ls[t,j]} {q[ni][nj]})']
    i,j=seq[0];ni,nj=seq[-1];t=(ni+nj%2)%K
    start=ks[i,j] if side=='C' else q[i][j];end=p[t][nj] if side=='C' else ls[t,nj]
    S=summ(weights);guards.append(f'(= (mod {S} {K}) 0)');g=conj(guards)
    add(f'(=> {g} (ite (< {S} 0) (< {end} {start}) (> {end} {start})))')
    first=conj([f'(distinct {summ(weights[:z])} 0)' for z in range(1,L)])
    add(f'(=> (and {g} (= {S} 0) {first}) (= {end} (+ {start} 1)))')
 return '\n'.join(lines)+'\n'
def run(K,m,depth=3,timeout=30000):
 s=make(K,m,depth,timeout);base=Path(__file__).with_name(f'axis_uniform_boundary_k{K}_m{m}_depth{depth}');base.with_suffix('.smt2').write_text(s)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,s.encode());t=time.time();ans=solve(ctx,sol)
 result=dict(full_drift=[-2*K,0],uniform_bottom=m,depth=depth,status={1:'SAT_RELAXATION',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-t)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
