#!/usr/bin/env python3
"""Discovery of count-only whole-strip candidates; never a controller claim."""
from probe_g8_extremal_cycle_boundary import *
from check_extremal_read_coupling import quotient,D
from collections import Counter
from pathlib import Path

def make_flow(cap=200):
 d=(2,-2);pts=[(r,t-r)for t in range(-1,12)for r in (0,1)];ix={p:i for i,p in enumerate(pts)}
 O={(0,-1),(1,-2),(0,0),(1,-1),(0,1),(1,2),(0,5),(1,10)}
 axis=lambda p:sum(p)%2
 var=lambda i,c,h:f'v{i}_{c}_{h}'
 vv=[[(c,h)for c in (1,-1)for h in (axis(p),axis(p)+2)]for p in pts]
 # Q even has vertical arrivals, C odd horizontal arrivals.
 vv=[[(c,h)for c in (1,-1)for h in ((0,2)if sum(p)%2==0 else(1,3))]for p in pts]
 def v(i,c,h):return f'v{i}_{"R"if c==1 else"L"}_{h}'
 def sm(xs):return '(+ '+' '.join(xs)+')'if xs else'0'
 lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(declare-fun P () Int)',f'(assert (and (>= P 28) (<= P {cap})))','(assert (= (mod P 4) 0))']
 for i,p in enumerate(pts):
  for c,h in vv[i]:lines.extend([f'(declare-fun {v(i,c,h)} () Int)',f'(assert (>= {v(i,c,h)} 0))'])
  lines.append(f'(assert (= (- {sm([v(i,c,h)for c,h in vv[i]if c==1])} {sm([v(i,c,h)for c,h in vv[i]if c==-1])}) {int(p in O)}))')
 for i,p in enumerate(pts):
  for ho in range(4):
   vals=[v(i,c,h)for c,h in vv[i]if(h+c)%4==ho]
   if not vals:continue
   q,k=quotient((p[0]+D[ho][0],p[1]+D[ho][1]),d)
   dest=sm([v(ix[q],c,hi)for c,hi in vv[ix[q]]if hi==ho])if q in ix else'0'
   lines.append(f'(assert (= {sm(vals)} {dest}))')
 # Also zero incoming on exterior faces.
 for i,p in enumerate(pts):
  for hi in (0,1,2,3):
   vals=[v(i,c,h)for c,h in vv[i]if h==hi]
   if not vals:continue
   q,k=quotient((p[0]-D[hi][0],p[1]-D[hi][1]),d)
   if q not in ix:lines.append(f'(assert (= {sm(vals)} 0))')
 lines.append(f'(assert (= P {sm([v(i,c,h)for i in range(len(pts))for c,h in vv[i]])}))')
 for ax in (0,1):
  terms=[f'(* {D[(h+c)%4][ax]} {v(i,c,h)})'for i in range(len(pts))for c,h in vv[i]if D[(h+c)%4][ax]]
  lines.append(f'(assert (= {sm(terms)} {d[ax]}))')
 for ph in range(4):
  terms=[v(i,c,h)for i,p in enumerate(pts)if(2*p[0]-sum(p)%2)%4==ph for c,h in vv[i]]
  lines.append(f'(assert (= (* 4 {sm(terms)}) P))')
 pinned={(0,-1):(3,),(1,-2):(3,),(0,0):(2,2,0),(1,-1):(2,2,0),(0,1):(1,1,3,3,3),(1,0):(1,1,3,3)}
 for p,hs in pinned.items():
  cnt=Counter((1 if j%2==0 else-1,h)for j,h in enumerate(hs));i=ix[p]
  for c,h in vv[i]:lines.append(f'(assert (= {v(i,c,h)} {cnt[c,h]}))')
 return '\n'.join(lines),pts,O,vv
if __name__=='__main__':
 text,pts,O,vv=make_flow();ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();ans=solve(ctx,s);print(ans,time.time()-t)
 if ans==1:
  model=modelstr(ctx,getmodel(ctx,s)).decode();print(model);Path(__file__).with_suffix('.model').write_text(model)
