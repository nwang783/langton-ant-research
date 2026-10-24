#!/usr/bin/env python3
"""All-cap forced-size outer-patch probe for a hypothesized g8 Ecycle4.
UNSAT is discovery only pending transparent certificate. SAT is open patch only.
"""
from probe_g8_extremal_cycle_boundary import *
from pathlib import Path

def make():
 d=(2,-2);pts=[(r,t-r)for t in range(-1,3)for r in (0,1)];ix={p:i for i,p in enumerate(pts)};caps=[1,1,3,3,9,9,28,28]
 lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(declare-fun P () Int)','(assert (>= P 28))','(assert (= (mod P 4) 0))']
 def add(x):lines.append('(assert '+x+')')
 def active(i,j):return f'(< {j} n{i})'
 def hin(i,j,h):return f'(= h{i}_{j} {h})'
 def hout(i,j,h):return hin(i,j,(h-(1 if j%2==0 else-1))%4)
 def both(a,b):return f'(and {a} {b})'
 def count(i,j,h,out=False):
  f=hout if out else hin;v=[f'(ite {both(active(i,k),f(i,k,h))} 1 0)'for k in range(j)];return'(+ '+' '.join(v)+')'if v else'0'
 for i,p in enumerate(pts):
  lines.append(f'(declare-fun n{i} () Int)');add(f'(and (<= 0 n{i}) (<= n{i} {caps[i]}))')
  if i<4:add(f'(= n{i} {caps[i]})')
  if i>=6:add(f'(= (mod n{i} 2) 0)')
  for j in range(caps[i]):
   lines.append(f'(declare-fun h{i}_{j} () Int)');lines.append(f'(declare-fun t{i}_{j} () Int)')
   ax=sum(p)%2;add(f'(or (= h{i}_{j} {ax}) (= h{i}_{j} {ax+2}))');add(f'(= (mod t{i}_{j} 4) {(2*p[0]-sum(p)%2+1)%4})')
   if j:add(f'(=> {active(i,j)} (>= (- t{i}_{j} t{i}_{j-1}) 4))')
  if i<2:add(f'(= h{i}_0 3)')
  elif i<4:
   for j,h in enumerate((2,2,0)):add(f'(= h{i}_{j} {h})')
 add('(= t0_0 0)')
 # Full ordinal matching for every internal directed edge, upper ports open.
 for i,p in enumerate(pts):
  for h in range(4):
   if h%2==sum(p)%2:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),d)
   if q not in ix:
    if sum(q)<-1:add(f'(= {count(i,caps[i],h,True)} 0)')
    continue
   ii=ix[q];add(f'(= {count(i,caps[i],h,True)} {count(ii,caps[ii],h)})')
   for u in range(caps[i]):
    for v in range(caps[ii]):
     cond=f'(and {active(i,u)} {active(ii,v)} {hout(i,u,h)} {hin(ii,v,h)} (= {count(i,u,h,True)} {count(ii,v,h)}))'
     add(f'(=> {cond} (= (+ t{i}_{u} 1) (+ t{ii}_{v} (* {k} P))))')
 return '\n'.join(lines),pts,caps
if __name__=='__main__':
 text,pts,caps=make();Path(__file__).with_suffix('.smt2').write_text(text);ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();ans=solve(ctx,s);print(ans,time.time()-t,flush=True)
 if ans==1:Path(__file__).with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,s)).decode())
