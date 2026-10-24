#!/usr/bin/env python3
"""Finite exact witness finder. A failure to find a cycle is not a theorem."""
import sys,json,collections
sys.setrecursionlimit(10000)
D=((0,1),(1,0),(0,-1),(-1,0))
def search(fuelcap,nodecap=2000000):
 reads={};seed=set();word=[];edges=collections.Counter();adj={};nodes=0;out=[];stop=False
 def go(p,h,fuel):
  nonlocal nodes,stop
  nodes+=1
  if nodes>=nodecap:stop=True;return
  old=reads.get(p)
  if old and old[0]>=3:return
  opts=(-old[1],) if old else ((1,-1) if fuel else (1,))
  for c in opts:
   reads[p]=(old[0]+1,c) if old else(1,c)
   freshblack=old is None and c==-1
   if freshblack:seed.add(p)
   word.append('R' if c==1 else'L');hh=(h+c)%4;dx,dy=D[hh];q=p[0]+dx,p[1]+dy
   e=p,q;edges[e]+=1;new=edges[e]==2
   if new:
    assert p not in adj
    adj[p]=q;v=q;cyc=[p]
    while v in adj and v!=p and len(cyc)<=len(adj):cyc.append(v);v=adj[v]
    if v==p:
     item=dict(fuelcap=fuelcap,nodes=nodes,word=''.join(word),seed=sorted(seed),cycle=cyc,white_cycle=not any(v in seed for v in cyc))
     out.append(item)
     if item['white_cycle']:stop=True
   if not stop:go(q,hh,fuel-freshblack)
   if new:del adj[p]
   edges[e]-=1
   word.pop()
   if freshblack:seed.remove(p)
   if old:reads[p]=old
   else:del reads[p]
   if stop:return
 go((0,0),0,fuelcap)
 return dict(fuelcap=fuelcap,nodes=nodes,status='STOPPED' if stop else'EXHAUSTED',cycles=out)
if __name__=='__main__':
 out=[]
 for m in range(7):
  r=search(m);out.append(r);print(m,r['nodes'],r['status'],len(r['cycles']),flush=True)
  open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
  if r['status']=='STOPPED':break
