#!/usr/bin/env python3
"""Open-boundary necessary tests. SAT is not an orbit."""
import sys,time,json
from pathlib import Path
import probe_one_a_local_constraints as z
PAT={
 'a_sink_aa_circle':[((0,1),'A0'),((1,1),'S3'),((0,0),'A1'),((-1,1),'B1'),((-1,0),'B0'),((1,2),'D0'),((0,2),'B3')],
 'b_sink_bb_circle':[((0,1),'A0'),((1,1),'S3'),((0,0),'A1'),((-1,1),'B1'),((-1,0),'B0'),((-1,2),'S2'),((-2,2),'D3'),((-2,1),'A0')]
}
def run(name,r,timeout):
 txt,ps,ss=z.make(r,timeout);ix={p:i for i,p in enumerate(ps)}
 for p,n in [((0,0),'S3'),((0,1),'A0'),((-1,1),'D3')]:
  i=ix[p];k=[a for a,h in ss[i]].index(n);txt=txt.replace(f'(assert (= s{i} {k}))\n','')
 for p,n in PAT[name]:
  i=ix[p];k=[a for a,h in ss[i]].index(n);txt+=f'(assert (= s{i} {k}))\n'
 base=Path(__file__).with_name(f'{name}_r{r}');base.with_suffix('.smt2').write_text(txt)
 ctx=z.mkcontext(z.mkconfig());sol=z.mksolver(ctx);z.inc(ctx,sol);z.parse(ctx,sol,txt.encode());st=time.time();ans=z.solve(ctx,sol)
 res=dict(pattern=name,radius=r,result={1:'SAT_LOCAL_ONLY',-1:'UNSAT_LOCAL',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:base.with_suffix('.model').write_text(z.modelstr(ctx,z.getmodel(ctx,sol)).decode())
 if ans==0:res['reason']=z.reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
if __name__=='__main__':run(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
