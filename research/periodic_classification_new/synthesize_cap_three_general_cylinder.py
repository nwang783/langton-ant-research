#!/usr/bin/env python3
"""Exact 11-state fixed-drift/fixed-strip synthesis with unbounded read clocks.
Generalizes the signed criterion to axis and oblique full drifts. Bounded
support UNSAT is never claimed as an unrestricted exclusion theorem.
"""
import sys,json,time
from pathlib import Path
from probe_one_a_local_constraints import D,states,conj,disj,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import getints,check_model

def make(w,timeout,dx,dy):
 assert dx>0 and (dx+dy)%2==0
 ps=[(r,(dy*r)//dx+v) for v in range(-w,w+1) for r in range(dx)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 def canonical(q):
  x,y=q;k=x//dx;return (x-k*dx,y-k*dy),k
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)']
 add=lambda x:lines.append('(assert '+x+')')
 mult=[];odd=[]
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} 11))')
  for j in range(3):lines.append(f'(declare-fun t{i}_{j} () Int)')
  add(f'(< t{i}_0 t{i}_1)');add(f'(< t{i}_1 t{i}_2)')
  mult.append('(+ '+' '.join(f'(ite (= s{i} {a}) {len(h)} 0)' for a,(_,h) in enumerate(ss[i]) if h)+')')
  odd.append('(+ '+' '.join(f'(ite (= s{i} {a}) 1 0)' for a,(_,h) in enumerate(ss[i]) if len(h)%2)+')')
 add('(= P (+ '+' '.join(mult)+'))');add('(> P 0)');add('(>= (+ '+' '.join(odd)+') 8)')
 for p,i in ix.items():
  for out_h in range(4):
   if out_h%2!=sum(p)%2:continue
   ax,ay=D[out_h];q,k=canonical((p[0]+ax,p[1]+ay))
   po=[[j for j,(c,h) in enumerate(hist) if (h+c)%4==out_h] for _,hist in ss[i]]
   if q not in ix:
    add(disj([f'(= s{i} {a})' for a,oi in enumerate(po) if not oi]));continue
   z=ix[q];qi=[[j for j,(c,h) in enumerate(hist) if h==out_h] for _,hist in ss[z]];opts=[]
   for a,oi in enumerate(po):
    for b,ij in enumerate(qi):
     if len(oi)!=len(ij):continue
     opts.append(conj([f'(= s{i} {a})',f'(= s{z} {b})']+[f'(= (+ t{z}_{y} (* {k} P)) (+ t{i}_{x} 1))' for x,y in zip(oi,ij)]))
   add(disj(opts))
 for p,i in ix.items():
  for h in range(4):
   if h%2==sum(p)%2:continue
   ax,ay=D[h];q,k=canonical((p[0]-ax,p[1]-ay))
   if q in ix:continue
   add(disj([f'(= s{i} {a})' for a,(_,hist) in enumerate(ss[i]) if not any(hh==h for c,hh in hist)]))
 return '\n'.join(lines)+'\n',ps,ss

def run(dx,dy,w,timeout):
 d=(dx,dy);txt,ps,ss=make(w,timeout,*d);base=Path(__file__).with_name(f'cap3_general_d{dx}_{dy}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(width=w,drift=d,classes=len(ps),timeout_ms=timeout,status={1:'SAT',-1:'UNSAT_FIXED_STRIP',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);result['certificate']=check_model(getints(mt),ps,ss,d)
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 return result
if __name__=='__main__':
 run(*map(int,sys.argv[1:]))
