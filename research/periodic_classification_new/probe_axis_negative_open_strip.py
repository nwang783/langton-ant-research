#!/usr/bin/env python3
"""Fixed literal lower two rows with full event clocks, open upper boundary."""
import json,time,sys
from pathlib import Path
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
D=[(0,1),(1,0),(0,-1),(-1,0)]
def make(n,p,q,P,timeout=20000):
 k=len(p);a=2*k;H={}
 for i in range(k):
  H[2*i,0]=[3];H[2*i+1,0]=[2]
  H[2*i,1]=[0 if j==p[i] else 2 for j in range(n)]
  H[2*i+1,1]=[(1 if j%2 else 3) if j!=q[i] else (3 if j%2 else 1) for j in range(n)]
 incs={};outs={};events=[]
 label=lambda e:'t'+'_'.join(map(str,e))
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)']
 def add(x):lines.append('(assert '+x+')')
 for (x,y),hs in H.items():
  for j,h in enumerate(hs):
   e=(x,y,j);events.append(e);incs.setdefault((x,y,h),[]).append(e)
   g=(h+(1 if j%2==0 else -1))%4;outs.setdefault((x,y,g),[]).append(e)
   lines.append(f'(declare-fun {label(e)} () Int)')
   if j:add(f'(< {label((x,y,j-1))} {label(e)})')
 add('(= '+label(events[0])+' 0)')
 for (x,y,g),es in outs.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy;v=-(xx//a);xx%=a
  if yy==2:continue
  ts=incs.get((xx,yy,g),[]);assert len(es)==len(ts)
  for s,t in zip(es,ts):add(f'(= {label(t)} (+ {label(s)} {1-v*P}))')
 # Exact global phase distinctness at this supplied period.
 add('(distinct '+' '.join(f'(mod {label(e)} {P})' for e in events)+')')
 return '\n'.join(lines)+'\n',len(events)
def run(n,p,q,P,timeout=20000):
 text,N=make(n,p,q,P,timeout);base=Path(__file__).with_name(f'axis_negative_open_n{n}_P{P}');base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());t=time.time();ans=solve(ctx,sol)
 result=dict(P=P,n=n,p=p,q=q,events=N,status={1:'SAT_OPEN_STRIP',0:'UNKNOWN',-1:'UNSAT_SOLVER_ONLY'}[ans],seconds=time.time()-t)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
 for P in (128,256,512):run(16,[11,3],[15,7],P)
