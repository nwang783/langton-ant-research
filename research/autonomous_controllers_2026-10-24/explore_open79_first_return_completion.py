#!/usr/bin/env python3
"""Bounded positive-only continuation of the two frozen reimport controls.
No exclusion follows from finite search limits. Higher fields are explicit.
"""
from pathlib import Path
from collections import deque
import json
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));T=lambda p:3*p[1]-p[0]+11
C=(-1,0);X=(2,1);BD=(3,1);U=(0,1);B=(0,0)
raw=json.load(open(R/'open79_cluster_reimport_discovery.json'));results=[]
for f in raw['found']:
 p=tuple(f['initial_position']);h=f['initial_heading'];K={};S=set(map(tuple,f['initial_black']));xr=0;br=0
 for c in f['word']:
  if p not in K:K[p]=p in S
  assert c==('L'if K[p]else'R');K[p]=not K[p]
  xr+=p==X;br+=p==BD;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 Q=deque([(p,h,K,S,f['word'],xr,br)]);nodes=0;found=None;max_extra=44;limit=400000
 while Q and nodes<limit:
  p,h,K,S,w,xr,br=Q.popleft();nodes+=1
  if len(w)-len(f['word'])>max_extra:continue
  if p==C:
   if h==2 and K[p]:
    ww=w;kk=K.copy();pp=p;hh=h;tail=[]
    for _ in range(3):
     if pp not in kk:break
     c='L'if kk[pp]else'R';tail.append((pp,hh,c));ww+=c;kk[pp]=not kk[pp];hh=(hh+(1 if c=='R'else-1))%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
    assert tail[:2]==[(C,2,'L'),(B,1,'L')]
    found={'word':ww,'initial_position':f['initial_position'],'initial_heading':f['initial_heading'],'initial_black':sorted(S),'first_reimport_branch':f['contact_position'],'C_return_time':len(w),'C_return_incoming':'S','post_return_tail':tail,'scope':'Genuine prepared finite factor through the next C return and two following reads. Named physical cells outside C/X/B+d are avoided before the C return. No whole OPEN79 completion, period clocks or translator.'};print('FOUND',f['contact_position'],len(ww),'return',len(w),'seed',len(S),'nodes',nodes,ww,flush=True);break
   continue
  # Every other physical named-level read is forbidden in this under-approximation.
  required=None
  if T(p)<=12:
   if p==X and xr==1:required=(2,'L')
   elif p==BD and br==0:required=(1,'L')
   else:continue
   if h!=required[0]:continue
  options=[K[p]]if p in K else[False,True]
  for black in options:
   c='L'if black else'R'
   if required is not None and c!=required[1]:continue
   KK=K.copy();SS=S.copy()
   if p not in KK and black:SS.add(p)
   KK[p]=not black;hh=(h+(-1 if black else 1))%4;pp=(p[0]+D[hh][0],p[1]+D[hh][1]);Q.append((pp,hh,KK,SS,w+c,xr+(p==X),br+(p==BD)))
 print('END',f['contact_position'],nodes,len(Q),bool(found),flush=True)
 results.append({'branch':f['contact_position'],'positive_search_limits':{'max_extra':max_extra,'nodes':limit},'explored_nodes':nodes,'remaining_queue':len(Q),'found':found})
(R/'open79_first_return_completion_discovery.json').write_text(json.dumps({'scope':__doc__,'results':results,'warning':'Positive-only bounded search; no absence or completeness claim.'}))
