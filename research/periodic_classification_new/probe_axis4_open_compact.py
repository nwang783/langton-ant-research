#!/usr/bin/env python3
"""Necessary exact compact lower-two-row clocks, unbounded upper exterior.
SAT is an open strip, not a complete white front. No exclusion beyond supplied
literal cap and bottom profile may be inferred.
"""
from pathlib import Path
import sys,re,time,json
from synthesize_axis_compact_clock import make,values
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason

def run(cap,bottom,qparity='any',timeout=30000):
 fixed={(x,0):tuple((3 if j%2==0 else 1) if x%2==0 else 2 for j in range(m)) for x,m in enumerate(bottom)}
 txt,ps=make(cap,2,2,timeout,'free',True,fixed_override=fixed)
 # Leave ONLY upper boundary unbound: C has incoming S, D outgoing N.
 for x in range(4):
  i=ps.index((x,1));kind,h=('i',2) if x%2==0 else ('o',0)
  txt=txt.replace(f'(assert (= {kind}{i}_{h}_{cap} 0))\n','')
 old='(assert (= P (+ '+' '.join(f'n{i}' for i in range(8))+')))'
 txt=txt.replace(old,'(assert (>= P (+ '+' '.join(f'n{i}' for i in range(8))+')))')
 txt+='(assert (>= P (* 2 (+ n4 n5 n6 n7))))\n'
 if qparity!='any':
  # x=3,y=1 has incoming E on even-rank S exits, W on odd-rank S exits.
  parity=int(qparity)
  for j in range(cap):
   if j%2!=parity:
    b=f'b7_{j}';s=b if j%2 else f'(not {b})'
    txt+=f'(assert (=> (> n7 {j}) (not {s})))\n'
 base=Path(__file__).with_name('axis4_open_cap'+str(cap)+'_bottom'+''.join(map(str,bottom))+'_q'+qparity)
 base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());t=time.time();ans=solve(ctx,sol)
 out=dict(cap=cap,bottom=bottom,qparity=qparity,status={1:'SAT_OPEN_STRIP',0:'UNKNOWN',-1:'UNSAT_LOCAL_SOLVER_ONLY'}[ans],seconds=time.time()-t)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);out['P']=int(v['P']);hs={}
  for i,p in enumerate(ps):
   n=int(v['n'+str(i)]);axis=1-sum(p)%2;hs[str(p)]=[axis+2*int(v[f'b{i}_{j}']) for j in range(n)]
  out['histories']=hs
 if ans==0:out['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':run(int(sys.argv[1]),list(map(int,sys.argv[2])),*(sys.argv[3:4]),int(sys.argv[4]) if len(sys.argv)>4 else 30000)
