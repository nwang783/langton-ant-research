#!/usr/bin/env python3
"""Positive-only bounded beam continuation of the frozen X-first reimport factor.
This is not an exhaustive search or an absence certificate.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));C=(-1,0);V=(-1,1);U=(0,1);T=lambda p:3*p[1]-p[0]+11
f=next(f for f in json.load(open(R/'open79_cluster_reimport_discovery.json'))['found']if tuple(f['contact_position'])==(2,1))
p=(2,1);h=2;K={};S=set(map(tuple,f['initial_black']))
word=f['word']
for c in word:
 if p not in K:K[p]=p in S
 assert c==('L'if K[p]else'R');K[p]=not K[p];h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
# All remaining paths retain known physical colors and forbid named lower reads.
# The required V contact sequence is E/L then E/R, as in the submitted theorem.
beam=[(p,h,K,S,word,0)];found=None;nodes=0;peak=0;records=[];width=1600;max_depth=260
for depth in range(len(word),max_depth):
 nxt=[];seen=set();peak=max(peak,len(beam))
 for p,h,K,S,w,stage in beam:
  nodes+=1
  if p==C:
   if stage==4 and h==2 and K[p]:
    found={'word':w+'LLL','initial_black':sorted(S),'initial_position':[2,1],'initial_heading':2,'C_return_time':len(w),'scope':'Positive finite factor only. Outside named reads forbidden in this construction; full lifted chronology not certified.'};break
   continue
  if T(p)<13 and p!=(3,1):continue
  if p==(3,1) and (h!=1 or p in K):continue
  if p==U and(stage!=0 or h!=2):continue
  if p==V:
   if stage not in(1,2,3):continue
   if h!=(3 if stage==1 else 1):continue
   assert K[p]==(stage==2)
  options=[K[p]]if p in K else[False,True]
  for black in options:
   KK=K.copy();SS=S.copy();c='L'if black else'R'
   if p==(3,1) and not black:continue
   if p not in KK and black:SS.add(p)
   KK[p]=not black;hh=(h+(-1 if black else 1))%4;pp=(p[0]+D[hh][0],p[1]+D[hh][1]);ns=stage+(p==V or p==U)
   key=(pp,hh,ns,tuple(sorted(KK.items())))
   if key in seen:continue
   seen.add(key);nxt.append((pp,hh,KK,SS,w+c,ns))
 if found:break
 # Keep diverse physical fields; score by contact stage, distance, and exposed support.
 def score(q):
  pp,hh,kk,ss,w,st=q
  goal=U if st==0 else(C if st==4 else V)
  dist=abs(pp[0]-goal[0])+abs(pp[1]-goal[1])
  return(dist-12*st,len(kk),len(ss),w)
 nxt.sort(key=score);beam=nxt[:width]
 if depth%10==0:records.append([depth,len(nxt),len(beam),max((x[5]for x in beam),default=-1)]);print(records[-1],flush=True)
 if not beam:break
print('END',nodes,'found',None if found is None else(len(found['word']),found['C_return_time'],len(found['initial_black'])),flush=True)
(R/'open79_X_first_joint_completion_discovery.json').write_text(json.dumps({'scope':__doc__,'limits':{'beam_width':width,'max_total_reads':max_depth},'expanded_nodes':nodes,'checkpoints':records,'found':found,'warning':'No absence, shortestness or all-period conclusion follows.'}))
