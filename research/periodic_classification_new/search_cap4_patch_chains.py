#!/usr/bin/env python3
"""Lazy exact local-history feasibility via chronological chain blocks.
SAT means an open patch of complete white cap-four histories, not an ant
orbit. Learned clauses exclude literal forced successor/order cycles.
Every clause records its bad event witness and fixed cell states.
"""
from itertools import product
from pathlib import Path
from collections import deque
import json,sys,time,re
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
CASES=[(3,1,3),(3,3,3),(3,1,3,1),(3,1,3,3),(3,3,3,1),(3,3,3,3)]
def states(p):
 a=1-sum(p)%2
 return [()]+[hs for n in range(1,5) for hs in product((a,a+2),repeat=n)]
def validate(ps,ss,chosen):
 ix={p:i for i,p in enumerate(ps)};hs=[ss[i][v] for i,v in enumerate(chosen)]
 ev=[(i,j) for i,h in enumerate(hs) for j in range(len(h))];succ={};pred={}
 for p,i in ix.items():
  for h,(dx,dy) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q=p[0]+dx,p[1]+dy
   if q not in ix:continue
   k=ix[q]
   out=[j for j,x in enumerate(hs[i]) if (x+(1 if j%2==0 else -1))%4==h]
   ins=[j for j,x in enumerate(hs[k]) if x==h]
   assert len(out)==len(ins)
   for a,b in zip(out,ins):succ[i,a]=(k,b);pred[k,b]=(i,a)
 chains=[];which={};pos={}
 for e in ev:
  if e in pred:continue
  chain=[];v=e
  while v is not None:
   assert v not in which;which[v]=len(chains);pos[v]=len(chain);chain.append(v);v=succ.get(v)
  chains.append(chain)
 if len(which)<len(ev):
  v=next(e for e in ev if e not in which);cycle=[v];u=succ[v]
  while u!=v:cycle.append(u);u=succ[u]
  return False,dict(kind='successor_cycle',events=cycle,cells=sorted({i for i,j in cycle}))
 adj=[{} for _ in chains]
 for i,h in enumerate(hs):
  for j in range(len(h)-1):
   a=(i,j);b=(i,j+1);ca=which[a];cb=which[b]
   if ca==cb:
    if pos[a]>=pos[b]:
     segment=chains[ca][pos[b]:pos[a]+1]
     return False,dict(kind='reversed_same_chain',events=segment,cells=sorted({x for x,y in segment}|{i}),order=[a,b])
   else:adj[ca][cb]=(a,b)
 color=[0]*len(chains);parents={}
 def dfs(a):
  color[a]=1
  for b,order in adj[a].items():
   if color[b]==0:
    parents[b]=a;v=dfs(b)
    if v is not None:return v
   elif color[b]==1:
    cyc=[a];v=a
    while v!=b:v=parents[v];cyc.append(v)
    cyc.reverse();return cyc
  color[a]=2
  return None
 for a in range(len(chains)):
  if color[a]==0:
   cyc=dfs(a)
   if cyc is not None:
    cells=sorted({i for c in cyc for i,j in chains[c]})
    return False,dict(kind='chain_order_cycle',chains=[chains[c] for c in cyc],orders=[adj[cyc[k]][cyc[(k+1)%len(cyc)]] for k in range(len(cyc))],cells=cells)
 indeg=[0]*len(chains)
 for edges in adj:
  for b in edges:indeg[b]+=1
 q=deque(a for a in range(len(chains)) if not indeg[a]);order=[]
 while q:
  a=q.popleft();order.append(a)
  for b in adj[a]:
   indeg[b]-=1
   if not indeg[b]:q.append(b)
 assert len(order)==len(chains)
 times={};t=0
 for c in order:
  for e in chains[c]:times[e]=t;t+=1
  t+=10
 assert all(times[i,j]<times[i,j+1] for i,h in enumerate(hs) for j in range(len(h)-1))
 assert all(times[b]==times[a]+1 for a,b in succ.items())
 return True,dict(chains=[chains[c] for c in order],cells=[dict(position=ps[i],headings=list(h),times=[times[i,j] for j in range(len(h))]) for i,h in enumerate(hs) if h])
def run(r,case,to,maxiter,maxheight=0):
 ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 decls=[f'(declare-fun s{i} () (_ BitVec 5))' for i in range(len(ps))]
 lines=['(set-logic QF_BV)',f'(set-option :timeout {to})','(set-option :produce-models true)']+decls
 add=lambda x:lines.append('(assert '+x+')')
 bv=lambda x,n=5:f'(_ bv{x} {n})'
 def ite(i,vals,b=3):
  s=bv(vals[-1],b)
  for k in range(len(vals)-2,-1,-1):s=f'(ite (= s{i} {bv(k)}) {bv(vals[k],b)} {s})'
  return s
 for i in range(len(ps)):add(f'(bvult s{i} {bv(31)})')
 for p,i in ix.items():
  for h,(dx,dy) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q=p[0]+dx,p[1]+dy
   if q not in ix:continue
   k=ix[q]
   out=[sum((x+(1 if j%2==0 else -1))%4==h for j,x in enumerate(hs)) for hs in ss[i]]
   ins=[sum(x==h for x in hs) for hs in ss[k]]
   add(f'(= {ite(i,out)} {ite(k,ins)})')
 c=ix[(0,0)];add(f'(= s{c} {bv(ss[c].index(CASES[case]))})')
 faces=[]
 if maxheight:
  faces=[(x,y) for x in range(-r-1,r+1) for y in range(-r-1,r+1)];fi={f:k for k,f in enumerate(faces)};bound=8*r+8;hb=(bound+5).bit_length()
  for k,f in enumerate(faces):
   lines.append(f'(declare-fun z{k} () (_ BitVec {hb}))');add(f'(bvule z{k} {bv(bound,hb)})')
  add(f'(= z{fi[(0,0)]} {bv(0,hb)})')
  for x,y in faces:
   for ax,ay in [(1,0),(0,1)]:
    q=x+ax,y+ay
    if q not in fi:continue
    u,v=((x+1,y),(x+1,y+1)) if ax else ((x,y+1),(x+1,y+1))
    if u not in ix:u,v=v,u
    i=ix[u];h=D.index((v[0]-u[0],v[1]-u[1]))
    vals=[sum((ih+(1 if j%2==0 else -1))%4==h or ih==(h+2)%4 for j,ih in enumerate(hs)) for hs in ss[i]]
    C,L=((x,y),q) if (x+y)%2==0 else (q,(x,y))
    add(f'(= (bvadd z{fi[L]} {bv(1,hb)}) (bvadd z{fi[C]} {ite(i,vals,hb)}))')
 base=Path(__file__).with_name(f'cap4_chains_r{r}_c{case}'+('_globalmax' if maxheight else ''))
 previous=json.loads(base.with_suffix('.json').read_text()) if base.with_suffix('.json').exists() else {}
 if previous.get('status') in ('SAT_LOCAL_CHAIN_ORDER_ONLY','UNSAT_LOCAL_LEARNED_CYCLES'):
  print(json.dumps(dict(previous_result_preserved=True,**{k:v for k,v in previous.items() if k not in ('chosen','certificate')})),flush=True);return
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,('\n'.join(lines)+'\n').encode());start=time.time();clauses=[];status=None
 if base.with_suffix('.clauses.json').exists():
  clauses=json.loads(base.with_suffix('.clauses.json').read_text())
  for proof in clauses:
   clause='(or '+' '.join(f'(not (= s{i} {bv(v)}))' for i,v in proof['states'])+')'
   parse(ctx,sol,('(assert '+clause+')\n').encode())
 prior_seconds=previous.get('seconds',0)
 def checkpoint(status,iteration,extra=None):
  result=dict(radius=r,case=case,center_history=CASES[case],status=status,iterations=iteration+1,clauses=len(clauses),seconds=prior_seconds+time.time()-start)
  if extra:result.update(extra)
  for suffix,data in [('.json',result),('.clauses.json',clauses)]:
   dst=base.with_suffix(suffix);temp=Path(str(dst)+'.tmp');temp.write_text(json.dumps(data,indent=2 if suffix=='.json' else None)+'\n');temp.replace(dst)
  return result
 for iteration in range(len(clauses),maxiter):
  ans=solve(ctx,sol)
  if ans==-1:status='UNSAT_LOCAL_LEARNED_CYCLES';break
  if ans==0:status='UNKNOWN';break
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();vs={int(a):int(b,2) for a,b in re.findall(r'^s(\d+) -> #b([01]+)$',mt,re.M)}
  assert len(vs)==len(ps),(len(vs),mt)
  chosen=[vs[i] for i in range(len(ps))];ok,witness=validate(ps,ss,chosen)
  if ok:
   if maxheight:
    depths={int(a):int(b,2) for a,b in re.findall(r'^z(\d+) -> #b([01]+)$',mt,re.M)};assert len(depths)==len(faces)
    witness['shifted_height_depths']=[dict(face=f,depth=depths[k]) for k,f in enumerate(faces)]
   status='SAT_LOCAL_CHAIN_ORDER_ONLY';break
  cells=witness['cells'];clause='(or '+' '.join(f'(not (= s{i} {bv(chosen[i])}))' for i in cells)+')'
  proof=dict(states=[[i,chosen[i]] for i in cells],witness=witness);clauses.append(proof)
  parse(ctx,sol,('(assert '+clause+')\n').encode())
  if iteration%1000==0:
   result=checkpoint('UNKNOWN_RUNNING',iteration);print(json.dumps(result),flush=True)
 else:status='UNKNOWN_ITERATION_LIMIT'
 result=checkpoint(status,iteration,dict(chosen=chosen,certificate=witness) if status=='SAT_LOCAL_CHAIN_ORDER_ONLY' else None)
 print(json.dumps({k:v for k,v in result.items() if k not in ('chosen','certificate')}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
