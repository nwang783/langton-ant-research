#!/usr/bin/env python3
"""Open-patch real clocks with unit separation, equivalent chain chronology.
SAT is only an open-patch history model, not an ant orbit. No installation.
"""
from pathlib import Path
from itertools import combinations
import sys,json,time,re,hashlib
from search_cap4_patch_chains import D,states,validate
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from probe_cylinder_real_clocks import number

def run(r,case,to,maxheight=1):
 root=Path(__file__).parent;src=(root/f'cap4_repeated_r_r{r}_c{case}.smt2').read_text()
 txt=src.replace('(set-logic QF_LIA)','(set-logic QF_LIRA)')
 txt=re.sub(r'\(set-option :timeout \d+\)',f'(set-option :timeout {to})',txt)
 txt=re.sub(r'(\(declare-fun t\d+_\d+ \(\)) Int\)',r'\1 Real)',txt)
 txt=re.sub(r'(\(define-fun [io]\d+_\d+t\d+ \(\)) Int ',r'\1 Real ',txt)
 txt=re.sub(r'^\(assert \(distinct .*\)\)\n','',txt,flags=re.M)
 ts=re.findall(r'\(declare-fun (t\d+_\d+) \(\) Real\)',txt)
 extra=[];add=lambda a:extra.append('(assert '+a+')')
 for a,b in combinations(ts,2):add(f'(or (<= (+ {a} 1) {b}) (<= (+ {b} 1) {a}))')
 ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 def ite(i,vs):
  z=str(vs[-1])
  for j in range(len(vs)-2,-1,-1):z=f'(ite (= s{i} {j}) {vs[j]} {z})'
  return z
 faces=[]
 if maxheight:
  faces=[(x,y) for x in range(-r-1,r+1) for y in range(-r-1,r+1)];fi={f:k for k,f in enumerate(faces)}
  for k,f in enumerate(faces):extra.append(f'(declare-fun z{k} () Real)');add(f'(>= z{k} 0)')
  add(f'(= z{fi[(0,0)]} 0)')
  for x,y in faces:
   for ax,ay in [(1,0),(0,1)]:
    q=x+ax,y+ay
    if q not in fi:continue
    u,v=((x+1,y),(x+1,y+1)) if ax else ((x,y+1),(x+1,y+1))
    if u not in ix:u,v=v,u
    i=ix[u];h=D.index((v[0]-u[0],v[1]-u[1]))
    vs=[sum((ih+(1 if j%2==0 else -1))%4==h or ih==(h+2)%4 for j,ih in enumerate(hs)) for hs in ss[i]]
    C,L=((x,y),q) if (x+y)%2==0 else (q,(x,y))
    add(f'(= (+ z{fi[L]} 1) (+ z{fi[C]} {ite(i,vs)}))')
 txt+='\n'.join(extra)+'\n';out=root/f'cap4_real_patch_r{r}_c{case}_max{maxheight}'
 out.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());start=time.time();ans=solve(ctx,sol)
 result=dict(radius=r,case=case,maxheight=maxheight,timeout_ms=to,status={-1:'UNSAT_LOCAL_REAL_CLOCKS',0:'UNKNOWN',1:'SAT_LOCAL_PENDING_CHECK'}[ans],seconds=time.time()-start,source_sha256=hashlib.sha256(src.encode()).hexdigest())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();out.with_suffix('.model').write_text(mt)
  vals={int(k):int(v) for k,v in re.findall(r'^s(\d+) -> (\d+)$',mt,re.M)};assert len(vals)==len(ps)
  chosen=[vals[i] for i in range(len(ps))];ok,cert=validate(ps,ss,chosen);assert ok,cert
  if maxheight:
   depths={int(k):number(v) for k,v in re.findall(r'^z(\d+) -> (.*)$',mt,re.M)}
   assert len(depths)==len(faces) and all(v.denominator==1 and v>=0 for v in depths.values())
   cert['shifted_height_depths']=[dict(face=f,depth=int(depths[k])) for k,f in enumerate(faces)]
  result.update(status='SAT_LOCAL_CHAIN_ORDER_ONLY',chosen=chosen,certificate=cert)
 out.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('chosen','certificate')}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
