#!/usr/bin/env python3
"""Geometry-only relaxation, collapsing equal-flow triple histories."""
import sys,time,json
from pathlib import Path
from probe_one_a_local_constraints import D,states,conj,disj,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason

def make(dx,dy,w,timeout):
 assert dx>0 and (dx+dy)%2==0
 ps=[(r,(dy*r)//dx+v) for v in range(-w,w+1) for r in range(dx)];ix={p:i for i,p in enumerate(ps)}
 ss=[]
 for p in ps:
  zs=[];seen=set()
  for name,hist in states(p):
   ins=tuple(sum(h==a for c,h in hist) for a in range(4));outs=tuple(sum((h+c)%4==a for c,h in hist) for a in range(4));f=(ins,outs)
   if f in seen:continue
   seen.add(f);zs.append((name,hist,ins,outs))
  ss.append(zs)
 def can(p):x,y=p;k=x//dx;return(x-k*dx,y-k*dy),k
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)'];add=lambda s:lines.append('(assert '+s+')')
 flux=[];odd=[]
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} {len(ss[i])}))')
  for a,(_,hist,ins,outs) in enumerate(ss[i]):
   voltage=sum((p[0]+D[(h+c)%4][0])//dx for c,h in hist)
   if voltage:flux.append(f'(ite (= s{i} {a}) {voltage} 0)')
   if len(hist)%2:odd.append(f'(ite (= s{i} {a}) 1 0)')
 add('(= (+ '+' '.join(flux)+') 1)');add('(>= (+ '+' '.join(odd)+') 8)')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q,k=can((p[0]+ax,p[1]+ay));z=ix.get(q)
   if z is None:add(disj([f'(= s{i} {a})' for a,(_,hist,ins,outs) in enumerate(ss[i]) if outs[h]==0]));continue
   opts=[]
   for count in range(3):
    opts.append(conj([disj([f'(= s{i} {a})' for a,(_,hist,ins,outs) in enumerate(ss[i]) if outs[h]==count]),disj([f'(= s{z} {a})' for a,(_,hist,ins,outs) in enumerate(ss[z]) if ins[h]==count])]))
   add(disj(opts))
  for h,(ax,ay) in enumerate(D):
   if h%2==sum(p)%2:continue
   q,k=can((p[0]-ax,p[1]-ay))
   if q not in ix:add(disj([f'(= s{i} {a})' for a,(_,hist,ins,outs) in enumerate(ss[i]) if ins[h]==0]))
 return '\n'.join(lines)+'\n',ps,ss

def run(dx,dy,w,to):
 txt,ps,ss=make(dx,dy,w,to);base=Path(__file__).with_name(f'cap3_static_reduced_d{dx}_{dy}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 res=dict(drift=[dx,dy],width=w,status={1:'SAT_STATIC_ONLY',-1:'UNSAT_FIXED_STRIP_STATIC',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:res['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
