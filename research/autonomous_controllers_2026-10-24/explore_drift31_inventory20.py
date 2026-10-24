#!/usr/bin/env python3
"""Discovery only, one exact O20 inventory; all local bounds derived."""
from itertools import combinations
from collections import Counter
import json
from pathlib import Path
from partial_drift31_graph import graph
from certify_drift31_read_minimum import depart,returns_to
ROOT=Path(__file__).resolve().parent
ODD={0,1,2,5,6,8,13,20}
def generated(axis,bound,ih,I,oh,J,parity,relations=()):
 for n in range(parity,bound+1,2):
  ev=list(range(0,n,2));od=list(range(1,n,2));other=(ih+2)%4
  for r in range(max(0,I-len(od)),min(I,len(ev))+1):
   l=I-r
   base=[other]*n
   # outgoing count depends only on parities, not individual placements.
   htest=[ih]*r+[other]*(len(ev)-r)
   kout=sum((h+1)%4==oh for h in htest)+l*((ih-1)%4==oh)+(len(od)-l)*((other-1)%4==oh)
   if kout!=J:continue
   for rr in combinations(ev,r):
    for ll in combinations(od,l):
     h=base.copy()
     for j in rr+ll:h[j]=ih
     if any(nextrel(h,a,b,oo,ii)==False for a,b,oo,ii in relations):continue
     yield tuple(h)
def nextrel(h,a,b,oo,ii):
 A=depart(h,oo);B=[j for j,hh in enumerate(h)if hh==ii]
 return a<len(A)and b<len(B)and B[b]==A[a]+1

def Gof(H):
 levels=sorted(H);return graph([H[t]for t in levels],levels)
def paths(H,t):
 kind,G=Gof(H)
 if kind!='open':return kind,G,None
 levels=sorted(H);r,p=returns_to([H[z]for z in levels],G,t)
 rel=[(x['outgoing_ordinal'],x['incoming_ordinal'],x['outgoing_heading'],x['incoming_heading'])for x in p]
 return kind,G,(rel,p)
def step(states,t,side):
 stats=Counter();res=[];maxbound=0;raw=0
 for H in states:
  kind,G,rp=paths(H,t);assert kind=='open'
  if side=='bottom':
   if t%2==0:ih,I,oh,J=0,len(depart(H[t-3],0)),1,H[t-1].count(1)
   else:ih,I,oh,J=3,len(depart(H[t-1],3)),2,H[t-3].count(2)
  else:
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
  bound=2*(I+J)+1;maxbound=max(maxbound,bound)
  for h in generated(t%2,bound,ih,I,oh,J,int(t in ODD),rp[0]):
   raw+=1;HH=H|{t:h};k,g=Gof(HH);stats[k]+=1
   if k=='open':res.append(HH)
 print('STEP',t,side,'parents',len(states),'raw',raw,'bound',maxbound,'outcomes',dict(stats),flush=True)
 return res

def main():
 bot={t:tuple('NESW'.index(c)for c in s)for t,s in enumerate(['S','W','S','EEWE','SSNS','EEW','NNN','EEEW'])}|{t:()for t in [-3,-2,-1]}
 top={20:(0,),21:(),22:(),23:()}
 B=[bot];T=[top]
 for t in [8,9,10]:B=step(B,t,'bottom')
 for t in [19,18,17,16]:T=step(T,t,'top')
 print('BOTTOM',[[''.join('NESW'[x]for x in H[t])for t in [8,9,10]]for H in B])
 print('TOP',[[''.join('NESW'[x]for x in H[t])for t in [16,17,18,19]]for H in T])
 json.dump({'odd':sorted(ODD),'bottom':[{str(t):h for t,h in H.items()}for H in B],'top':[{str(t):h for t,h in H.items()}for H in T]},open(ROOT/'drift31_inventory20_discovery.json','w'))
if __name__=='__main__':main()
