#!/usr/bin/env python3
"""Exact successor/rank graph on an arbitrary set of COMPLETE named cells.
Absent classes have unrestricted histories; all crossing boundary ports stay open.
A positive-winding closed component is only a rejection if it is proper.
"""
from check_extremal_read_coupling import D,quotient
DRIFT=(2,-2)
def graph(H, pts=None):
 if pts is None:pts=[(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)]
 ix={p:i for i,p in enumerate(pts)}
 nodes=[(i,j)for i,h in enumerate(H)for j in range(len(h))];out={};incoming={}
 for i,p in enumerate(pts):
  for h in range(4):
   src=[j for j,hi in enumerate(H[i])if(hi+(1 if j%2==0 else-1))%4==h]
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT)
   if q not in ix:continue
   ii=ix[q];dst=[j for j,hi in enumerate(H[ii])if hi==h];assert len(src)==len(dst)
   for u,v in zip(src,dst):out[i,u]=((ii,v),k);incoming[ii,v]=((i,u),k)
 chains=[];seen=set()
 for start in nodes:
  if start in incoming:continue
  seq=[];at=start;k=0
  while True:
   assert at not in seen;seen.add(at);seq.append((at,k))
   if at not in out:break
   at,dk=out[at];k+=dk
  chains.append(seq)
 if len(seen)!=len(nodes):
  at=next(v for v in nodes if v not in seen);seq=[];ind={};k=0
  while at not in ind:
   ind[at]=len(seq);seq.append((at,k));at,dk=out[at];k+=dk
  cy=seq[ind[at]:];winding=k-cy[0][1]
  return 'closed_component',{'cycle':cy,'winding':winding,'other_local_events':len(nodes)-len(cy),'open_chains':len(chains)}
 where={}
 for c,seq in enumerate(chains):
  prev={}
  for a,((i,j),k)in enumerate(seq):
   where[i,j]=(c,a,k);p=(pts[i][0]+2*k,pts[i][1]-2*k)
   if p in prev and j!=prev[p][0]+1:return'skipped_rank',{'segment':seq[prev[p][1]:a+1],'point':p,'rank_before':prev[p][0],'rank_after':j}
   prev[p]=(j,a)
 edges=[]
 for i,hs in enumerate(H):
  for j in range(len(hs)-1):
   u,a,ka=where[i,j];v,b,kb=where[i,j+1]
   edges.append((u,v,4+a-b,kb-ka,i,j))
 N=len(nodes);P=10*N+100;n=len(chains);dist=[0]*n;prev=[None]*n;last=None
 for _ in range(n):
  last=None
  for e in edges:
   u,v,C,K,*_=e
   if dist[v]<dist[u]+C+K*P:dist[v]=dist[u]+C+K*P;prev[v]=e;last=v
  if last is None:break
 if last is not None:
  at=last
  for _ in range(n):at=prev[at][0]
  start=at;cy=[]
  while True:
   e=prev[at];cy.append(e);at=e[0]
   if at==start:break
  C=sum(e[2]for e in cy);K=sum(e[3]for e in cy)
  assert K>=0 and C+K*N>0
  return'positive_rank_clock_cycle',{'chains':chains,'inequality_cycle':cy,'constant':C,'period_coefficient':K,'local_event_count':N,'positive_at_minimum_period':C+K*N}
 return'open',{'points':pts,'chains':chains,'event_count':N}

