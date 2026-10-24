#!/usr/bin/env python3
"""Cap-three finite-prefix synthesis. Arbitrary initial colors outside fixed
white central one-A motif. One open boundary entry and exit; exact local
integer clocks force one event path. SAT will be literally replayed.
"""
import sys,time,json,itertools
from pathlib import Path
from probe_one_a_local_constraints import D,conj,disj,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import getints

def states(p):
 axis=1 if sum(p)%2==0 else 0
 out=[('0',[])]
 for n in (1,2,3):
  for c in (1,-1):
   for hs in itertools.product((axis,(axis+2)%4),repeat=n):
    hist=[(c*(-1)**j,h) for j,h in enumerate(hs)]
    out.append((''.join('R' if z[0]==1 else'L' for z in hist)+':'+''.join(map(str,hs)),hist))
 return out

def make(r,to):
 ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+2)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {to})','(set-option :produce-models true)'];add=lambda x:lines.append('(assert '+x+')')
 ent=[];ex=[]
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} {len(ss[i])}))')
  for j in range(3):lines.append(f'(declare-fun t{i}_{j} () Int)')
  add(f'(< t{i}_0 t{i}_1)');add(f'(< t{i}_1 t{i}_2)')
  for a,(_,hist) in enumerate(ss[i]):
   if not hist:continue
   add(f'(=> (= s{i} {a}) '+conj([f'(and (<= 0 t{i}_{j}) (< t{i}_{j} {3*len(ps)}))' for j in range(len(hist))])+')')
 for p,name in [((0,0),'RL:31'),((0,1),'RLR:002'),((-1,1),'RL:33')]:
  i=ix[p];a=[n for n,h in ss[i]].index(name);add(f'(= s{i} {a})')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q=(p[0]+ax,p[1]+ay);po=[[j for j,(c,hh) in enumerate(hist) if (hh+c)%4==h] for _,hist in ss[i]]
   if q not in ix:
    add(disj([f'(= s{i} {a})' for a,oi in enumerate(po) if len(oi)<=1]));ex += [f'(ite (= s{i} {a}) 1 0)' for a,oi in enumerate(po) if len(oi)==1];continue
   z=ix[q];qi=[[j for j,(c,hh) in enumerate(hist) if hh==h] for _,hist in ss[z]];opts=[]
   for a,oi in enumerate(po):
    for b,ij in enumerate(qi):
     if len(oi)!=len(ij):continue
     opts.append(conj([f'(= s{i} {a})',f'(= s{z} {b})']+[f'(= t{z}_{y} (+ t{i}_{x} 1))' for x,y in zip(oi,ij)]))
   add(disj(opts))
  for h,(ax,ay) in enumerate(D):
   if h%2==sum(p)%2:continue
   q=(p[0]-ax,p[1]-ay)
   if q in ix:continue
   qi=[[j for j,(c,hh) in enumerate(hist) if hh==h] for _,hist in ss[i]]
   add(disj([f'(= s{i} {a})' for a,ii in enumerate(qi) if len(ii)<=1]));ent += [f'(ite (= s{i} {a}) 1 0)' for a,ii in enumerate(qi) if len(ii)==1]
   for a,ii in enumerate(qi):
    if len(ii)==1:add(f'(=> (= s{i} {a}) (= t{i}_{ii[0]} 0))')
 add('(= (+ '+' '.join(ent)+') 1)');add('(= (+ '+' '.join(ex)+') 1)')
 return '\n'.join(lines)+'\n',ps,ss

def verify(v,ps,ss):
 events={};seed=[];hist={}
 for i,p in enumerate(ps):
  name,hs=ss[i][v['s'+str(i)]]
  if not hs:continue
  if hs[0][0]==-1:seed.append(p)
  ts=[v[f't{i}_{j}'] for j in range(len(hs))];assert all(a<b for a,b in zip(ts,ts[1:]));hist[p]=list(zip(ts,hs))
  for t,(c,h) in zip(ts,hs):assert t not in events;events[t]=(p,c,h)
 P=len(events);assert set(events)==set(range(P));board=set(seed);reads={}
 for t in range(P):
  p,c,h=events[t];assert c==(-1 if p in board else 1)
  board.symmetric_difference_update([p]);reads[p]=reads.get(p,0)+1;assert reads[p]<=3
  hh=(h+c)%4;q=(p[0]+D[hh][0],p[1]+D[hh][1])
  if t+1<P:assert events[t+1][0]==q and events[t+1][2]==hh
 return dict(seed=sorted(seed),head=events[0][0],heading=events[0][2],word=''.join('R' if events[t][1]==1 else'L' for t in range(P)),steps=P,central={str(p):hist[p] for p in [(0,0),(0,1),(-1,1),(-1,0)]})
def run(r,to):
 txt,ps,ss=make(r,to);base=Path(__file__).with_name(f'one_a_finite_r{r}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 res=dict(radius=r,cells=len(ps),timeout_ms=to,status={1:'SAT_FINITE_PREFIX',-1:'UNSAT_FIXED_BOX',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);res['certificate']=verify(getints(mt),ps,ss)
 if ans==0:res['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
