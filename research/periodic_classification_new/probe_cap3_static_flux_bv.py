#!/usr/bin/env python3
"""Bit-vector finite geometry relaxation, no chronological feasibility."""
import sys,time,json
from pathlib import Path
from probe_cap3_static_flux_reduced import make as oldmake
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason

def make(dx,dy,w,to):
 _,ps,ss=oldmake(dx,dy,w,to);ix={p:i for i,p in enumerate(ps)};bits=max(5,(6*len(ps)+1).bit_length()+1)
 def bv(n,b=4):return f'(_ bv{n%(1<<b)} {b})'
 def ites(i,vals,b=2):
  s=bv(vals[-1],b)
  for k in range(len(vals)-2,-1,-1):s=f'(ite (= s{i} {bv(k)}) {bv(vals[k],b)} {s})'
  return s
 def addsum(xs,b):
  if not xs:return bv(0,b)
  s=xs[0]
  for t in xs[1:]:s=f'(bvadd {s} {t})'
  return s
 def can(p):x,y=p;k=x//dx;return(x-k*dx,y-k*dy),k
 lines=['(set-logic QF_BV)',f'(set-option :timeout {to})','(set-option :produce-models true)'];add=lambda s:lines.append('(assert '+s+')');flux=[];odd=[]
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () (_ BitVec 4))');add(f'(bvult s{i} {bv(len(ss[i]))})')
  flux.append(ites(i,[sum((p[0]+D[(h+c)%4][0])//dx for c,h in hist) for name,hist,ins,outs in ss[i]],bits))
  odd.append(ites(i,[len(hist)%2 for name,hist,ins,outs in ss[i]],bits))
  for h in range(4):
   lines.append(f'(define-fun i{i}_{h} () (_ BitVec 2) '+ites(i,[ins[h] for name,hist,ins,outs in ss[i]])+')')
   lines.append(f'(define-fun o{i}_{h} () (_ BitVec 2) '+ites(i,[outs[h] for name,hist,ins,outs in ss[i]])+')')
 add(f'(= {addsum(flux,bits)} {bv(1,bits)})');add(f'(bvuge {addsum(odd,bits)} {bv(8,bits)})')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2==sum(p)%2:
    q,k=can((p[0]+ax,p[1]+ay));z=ix.get(q)
    add(f'(= o{i}_{h} '+(bv(0,2) if z is None else f'i{z}_{h}')+')')
   else:
    q,k=can((p[0]-ax,p[1]-ay))
    if q not in ix:add(f'(= i{i}_{h} {bv(0,2)})')
 return '\n'.join(lines)+'\n',ps,ss

def run(dx,dy,w,to):
 txt,ps,ss=make(dx,dy,w,to);base=Path(__file__).with_name(f'cap3_static_bv_d{dx}_{dy}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 res=dict(drift=[dx,dy],width=w,status={1:'SAT_STATIC_ONLY',-1:'UNSAT_FIXED_STRIP_STATIC',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:res['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
