#!/usr/bin/env python3
"""Positive finite-factor search for the two supplied cluster reimport ports.
Search limits have no exclusion meaning. Higher fields are prepared explicitly.
"""
from pathlib import Path
from collections import deque
import json
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));X=(2,1);U=(0,1);CL={X,U,(1,1),(1,0)};T=lambda p:3*p[1]-p[0]+11
prefix='RLRRLLR';seed={(1,1),(0,1),(-1,1)};p=X;h=2;known={}
for c in prefix:
 if p not in known:known[p]=p in seed
 assert c==('L'if known[p]else'R');known[p]=not known[p];h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
Q=deque([(p,h,known,seed,prefix)]);found={};nodes=0;maxextra=28;limit=600000
while Q and nodes<limit and len(found)<2:
 p,h,K,S,w=Q.popleft();nodes+=1
 if len(w)-len(prefix)>maxextra:continue
 if p in CL:
  if p in(X,U)and h==2 and p not in found:
   c='L'if K[p]else'R';assert c==('L'if p==X else'R');found[p]={'word':w+c,'initial_position':X,'initial_heading':2,'initial_black':sorted(S),'contact_position':p,'contact_incoming_heading':h,'contact_turn':c,'scope':'Genuine prepared finite factor through first cluster reimport; not a complete first return, full OPEN79 history, or translator.'};print('FOUND',p,'reads',len(w)+1,'seed',len(S),w+c,flush=True)
  continue
 if T(p)<13:continue
 options=[K[p]]if p in K else[False,True]
 for black in options:
  KK=K.copy();SS=S.copy()
  if p not in KK and black:SS.add(p)
  KK[p]=not black;c='L'if black else'R';hh=(h+(-1 if black else 1))%4;pp=(p[0]+D[hh][0],p[1]+D[hh][1]);Q.append((pp,hh,KK,SS,w+c))
print('END',nodes,'queue',len(Q),'found',len(found),flush=True)
(R/'open79_cluster_reimport_discovery.json').write_text(json.dumps({'scope':__doc__,'explored_nodes':nodes,'remaining_queue':len(Q),'positive_search_limits':{'extra_reads':maxextra,'nodes':limit},'found':[v for v in found.values()],'warning':'No absence, shortest-path or all-future claim is inferred from search limits.'}))
