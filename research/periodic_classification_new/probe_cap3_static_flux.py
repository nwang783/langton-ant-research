#!/usr/bin/env python3
"""Relaxed geometry-only finite-cylinder test. SAT is not an ant front."""
import sys,time,json
from pathlib import Path
from synthesize_cap_three_general_cylinder import *
def runstatic(dx,dy,w,timeout):
 txt,ps,ss=make(w,timeout,dx,dy)
 # Drop each per-edge equality involving a t read clock, retaining state pairs.
 import re
 txt=re.sub(r' \(= \(\+ t\d+_\d \(\* -?\d+ P\)\) \(\+ t\d+_\d 1\)\)','',txt)
 # Actual total seam flux is one because requested full drift is d.
 terms=[]
 for i,(x,y) in enumerate(ps):
  for a,(_,hist) in enumerate(ss[i]):
   voltage=sum((x+D[(h+c)%4][0])//dx for c,h in hist)
   if voltage:terms.append(f'(ite (= s{i} {a}) {voltage} 0)')
 txt+='(assert (= (+ '+' '.join(terms)+') 1))\n'
 base=Path(__file__).with_name(f'cap3_static_d{dx}_{dy}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(drift=[dx,dy],width=w,status={1:'SAT_STATIC_ONLY',-1:'UNSAT_FIXED_STRIP_STATIC',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=getints(mt)
  result['states']={str(p):ss[i][v[f's{i}']][0] for i,p in enumerate(ps) if ss[i][v[f's{i}']][1]}
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':runstatic(*map(int,sys.argv[1:]))
