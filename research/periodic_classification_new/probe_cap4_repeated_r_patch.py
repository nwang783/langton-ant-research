#!/usr/bin/env python3
"""Exact necessary local chronology for cap-four white histories.
Center is a repeated-first/third-R-heading cell. SAT is only a local patch,
not a global orbit. UNSAT at any radius excludes precisely the forced case.
"""
from itertools import product
from pathlib import Path
import json,sys,time
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason

def states(p):
 a=1-sum(p)%2
 return [()]+[hs for n in range(1,5) for hs in product((a,a+2),repeat=n)]
def run(r,case,to,distinct=1):
 ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {to})','(set-option :produce-models true)'];add=lambda s:lines.append('(assert '+s+')')
 def ite(i,vals):
  s=str(vals[-1])
  for k in range(len(vals)-2,-1,-1):
   if str(vals[k])!=s:s=f'(ite (= s{i} {k}) {vals[k]} {s})'
  return s
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} 31))')
  for j in range(4):lines.append(f'(declare-fun t{i}_{j} () Int)')
  add('(and '+' '.join(f'(< t{i}_{j} t{i}_{j+1})' for j in range(3))+')')
  for kind in ('i','o'):
   for h in range(4):
    if h%2 != (1-sum(p)%2 if kind=='i' else sum(p)%2):continue
    indices=[[j for j,x in enumerate(hs) if (x if kind=='i' else (x+(1 if j%2==0 else -1))%4)==h] for hs in ss[i]]
    lines.append(f'(define-fun {kind}{i}_{h}c () Int {ite(i,[len(z) for z in indices])})')
    for j in range(4):
     lines.append(f'(define-fun {kind}{i}_{h}t{j} () Int {ite(i,[f"t{i}_{z[j]}" if len(z)>j else "0" for z in indices])})')
 if distinct:add('(distinct '+' '.join(f't{i}_{j}' for i in range(len(ps)) for j in range(4))+')')
 for p,i in ix.items():
  for h,(dx,dy) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q=p[0]+dx,p[1]+dy
   if q not in ix:continue
   k=ix[q];add(f'(= o{i}_{h}c i{k}_{h}c)')
   for j in range(4):add(f'(=> (> o{i}_{h}c {j}) (= i{k}_{h}t{j} (+ o{i}_{h}t{j} 1)))')
 center=ix[(0,0)];cases=[(3,1,3),(3,3,3),(3,1,3,1),(3,1,3,3),(3,3,3,1),(3,3,3,3)]
 hs=cases[case];add(f'(= s{center} {ss[center].index(hs)})');add(f'(= t{center}_0 0)')
 txt='\n'.join(lines)+'\n';base=Path(__file__).with_name(f'cap4_repeated_r_r{r}_c{case}'+('' if distinct else '_nodistinct'));base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(distinct=bool(distinct),radius=r,cells=len(ps),center_history=list(hs),timeout_ms=to,status={1:'SAT_LOCAL_ONLY',-1:'UNSAT_LOCAL',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
