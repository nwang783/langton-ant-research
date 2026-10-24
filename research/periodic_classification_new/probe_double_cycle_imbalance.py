#!/usr/bin/env python3
"""Finite falsification probe, never a general exclusion certificate."""
import collections,json,sys
sys.setrecursionlimit(20000)
D=((0,1),(1,0),(0,-1),(-1,0))
def search(m,nodecap=2000000):
 hist={};seed=set();word=[];edge=collections.Counter();adj={};cycles=[];nodes=0;found=None;counts=collections.Counter();cap=False
 def go(p,h,fuel):
  nonlocal nodes,found,cap
  nodes+=1
  if nodes>=nodecap:cap=True;return
  old=hist.get(p,[])
  if len(old)>=3:return
  opts=(-old[-1][0],) if old else ((1,-1) if fuel else(1,))
  for c in opts:
   hist[p]=old+[(c,h)];fresh=c==-1 and not old
   if fresh:seed.add(p)
   word.append('R' if c==1 else'L')
   for cyc in cycles:
    if (0,0) in cyc or any(v in seed or len(hist.get(v,[]))!=3 for v in cyc):continue
    kinds=[]
    for v in cyc:
     hs=[x[1] for x in hist[v]]
     kinds.append('S' if hs[0]==hs[2] else 'A' if hs[0]==hs[1] else 'B')
    key=(len(cyc),kinds.count('A')-kinds.count('B'),kinds.count('S'))
    counts[key]+=1
    if kinds.count('A')>kinds.count('B') or kinds.count('S')>0:
     found=dict(seed=sorted(seed),word=''.join(word),cycle=cyc,kinds=kinds,criterion='positive A-B or any same-type vertex');break
   hh=(h+c)%4;dx,dy=D[hh];q=p[0]+dx,p[1]+dy;e=p,q;edge[e]+=1;new=edge[e]==2;newcyc=False
   if new:
    assert p not in adj
    adj[p]=q;v=q;cyc=[p]
    while v in adj and v!=p and len(cyc)<=len(adj):cyc.append(v);v=adj[v]
    if v==p:cycles.append(cyc);newcyc=True
   if not found:go(q,hh,fuel-fresh)
   if newcyc:cycles.pop()
   if new:del adj[p]
   edge[e]-=1;word.pop()
   if fresh:seed.remove(p)
   if old:hist[p]=old
   else:del hist[p]
   if found or cap:return
 go((0,0),0,m)
 return dict(m=m,nodes=nodes,status='WITNESS' if found else 'NODE_CAP_UNKNOWN' if cap else 'EXHAUSTED',found=found,counts={str(k):v for k,v in counts.items()})
if __name__=='__main__':
 out=[]
 for m in range(8):
  r=search(m);out.append(r);print(m,r['nodes'],r['status'],r['counts'],flush=True)
  open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
  if r['status']!='EXHAUSTED':break
