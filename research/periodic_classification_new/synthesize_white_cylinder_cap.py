#!/usr/bin/env python3
"""Fixed-strip exact white-front synthesis with configurable complete visit cap.
Every heading history is included, not the special cap-three 11-state subset.
The signed positive-voltage one-cycle argument applies unchanged. A finite
UNSAT/UNKNOWN result is not an unrestricted theorem. New implementation,
pending independent audit; every SAT model is reconstructed and replayed.
"""
from itertools import product
from pathlib import Path
import json,sys,time,re
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import check_model

def getints(text):
 out={}
 for key,value in re.findall(r'^(P|s\d+|t\d+_\d+) -> (-?\d+|\(- \d+\))$',text,re.M):
  out[key]=-int(value[3:-1]) if value.startswith('(- ') else int(value)
 return out

def run(cap,dx,dy,w,to):
 assert cap>=1 and dx>0 and (dx+dy)%2==0
 ps=[(r,(dy*r)//dx+v) for v in range(-w,w+1) for r in range(dx)];ix={p:i for i,p in enumerate(ps)}
 ss=[]
 for p in ps:
  a=1-sum(p)%2
  hh=[()]+[hs for n in range(1,cap+1) for hs in product((a,a+2),repeat=n)]
  ss.append([(''.join(str(h) for h in hs),[(1 if j%2==0 else -1,h) for j,h in enumerate(hs)]) for hs in hh])
 def canonical(q):
  k=q[0]//dx;return(q[0]-k*dx,q[1]-k*dy),k
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {to})','(set-option :produce-models true)','(declare-fun P () Int)'];add=lambda s:lines.append('(assert '+s+')')
 def ite(i,vals):
  s=str(vals[-1])
  for k in range(len(vals)-2,-1,-1):
   if str(vals[k])!=s:s=f'(ite (= s{i} {k}) {vals[k]} {s})'
  return s
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} {len(ss[i])}))')
  for j in range(cap):lines.append(f'(declare-fun t{i}_{j} () Int)')
  for j in range(cap-1):add(f'(< t{i}_{j} t{i}_{j+1})')
  lines.append(f'(define-fun m{i} () Int {ite(i,[len(h) for name,h in ss[i]])})')
  for kind in ('i','o'):
   for h in range(4):
    if h%2 != (1-sum(p)%2 if kind=='i' else sum(p)%2):continue
    inds=[[j for j,(c,x) in enumerate(hist) if (x if kind=='i' else (x+c)%4)==h] for name,hist in ss[i]]
    lines.append(f'(define-fun {kind}{i}_{h}c () Int {ite(i,[len(z) for z in inds])})')
    for j in range(cap):lines.append(f'(define-fun {kind}{i}_{h}t{j} () Int {ite(i,[f"t{i}_{z[j]}" if len(z)>j else "0" for z in inds])})')
 add('(= P (+ '+' '.join(f'm{i}' for i in range(len(ps)))+'))');add('(> P 0)')
 # Fix the free common temporal origin at the first active representative.
 for i in range(len(ps)):
  pre='(and '+' '.join([f'(> s{i} 0)']+[f'(= s{j} 0)' for j in range(i)])+')'
  add(f'(=> {pre} (= t{i}_0 0))')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2==sum(p)%2:
    q,k=canonical((p[0]+ax,p[1]+ay));z=ix.get(q)
    if z is None:add(f'(= o{i}_{h}c 0)');continue
    add(f'(= o{i}_{h}c i{z}_{h}c)')
    for j in range(cap):add(f'(=> (> o{i}_{h}c {j}) (= (+ i{z}_{h}t{j} (* {k} P)) (+ o{i}_{h}t{j} 1)))')
   else:
    q,k=canonical((p[0]-ax,p[1]-ay))
    if q not in ix:add(f'(= i{i}_{h}c 0)')
 txt='\n'.join(lines)+'\n';base=Path(__file__).with_name(f'white_cap{cap}_d{dx}_{dy}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(cap=cap,drift=[dx,dy],width=w,classes=len(ps),local_states=len(ss[0]),timeout_ms=to,status={1:'SAT_EXACT_MODEL_PENDING_REPLAY',-1:'UNSAT_FIXED_STRIP',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);result['certificate']=check_model(getints(mt),ps,ss,(dx,dy));result['status']='SAT_RECONSTRUCTED'
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
