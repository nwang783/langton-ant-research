#!/usr/bin/env python3
"""Look for an exact finite-prefix counterexample to path balance; no bound is a proof."""
import collections,json,sys
sys.setrecursionlimit(20000)
D=((0,1),(1,0),(0,-1),(-1,0))
def search(m,nodecap=2000000):
 hist={};seed=set();word=[];edge=collections.Counter();adj={};rev=collections.Counter();nodes=0;found=None;counts=collections.Counter();cap=False
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
   hh=(h+c)%4;dx,dy=D[hh];q=p[0]+dx,p[1]+dy;e=p,q;edge[e]+=1;new=edge[e]==2
   if new:
    assert p not in adj
    adj[p]=q;rev[q]+=1
   if new or len(hist[p])==3:
    for root in adj:
     if rev[root]:continue
     vs=[root];v=root
     while v in adj:
      v=adj[v]
      if v in vs:break
      vs.append(v)
     if v in adj or (0,0) in vs or q in vs or any(z in seed for z in vs):continue
     if len(hist.get(vs[0],[]))!=2 or len(hist.get(vs[-1],[]))!=2 or any(len(hist.get(z,[]))!=3 for z in vs[1:-1]):continue
     if hist[vs[0]][0][1]==hist[vs[0]][1][1] or hist[vs[-1]][0][1]!=hist[vs[-1]][1][1]:continue
     kinds=[]
     for z in vs[1:-1]:
      hs=[a[1] for a in hist[z]]
      kinds.append('S' if hs[0]==hs[2] else'A' if hs[0]==hs[1] else'B')
     key=''.join(kinds);counts[key]+=1
     if kinds.count('A')>kinds.count('B'):
      found=dict(seed=sorted(seed),word=''.join(word),path=vs,kinds=kinds,imbalance=kinds.count('A')-kinds.count('B'));break
   if not found:go(q,hh,fuel-fresh)
   if new:del adj[p];rev[q]-=1
   edge[e]-=1;word.pop()
   if fresh:seed.remove(p)
   if old:hist[p]=old
   else:del hist[p]
   if found or cap:return
 go((0,0),0,m)
 return dict(m=m,nodes=nodes,status='WITNESS' if found else 'NODE_CAP_UNKNOWN' if cap else 'EXHAUSTED',found=found,counts=dict(counts))
if __name__=='__main__':
 out=[]
 for m in range(8):
  r=search(m);out.append(r);print(m,r['nodes'],r['status'],r['counts'],flush=True)
  open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
  if r['status']!='EXHAUSTED':break
