#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json
from explore_paid201_top_ownership import embeds
from explore_paid201_top27_ownership import direct_words
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent
for c in[3]:
 O={0,1,2,6,7,6*c+1,32,34};states=[{34:(0,),35:(),36:(),37:()}];rows=[]
 for t in range(33,26,-1):
  out=[];co=Counter();row=[]
  for H in states:
   lev=sorted(H);_,G=graph([H[z]for z in lev],lev);_,paths=returns_to([H[z]for z in lev],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   words,bound,nodes=direct_words(I,J,ih,oh,paths,int(t in O));outcomes=[]
   for h in words:
    hh=H|{t:h};lev=sorted(hh);kind,gg=graph([hh[z]for z in lev],lev)
    if kind=='open':
     if not embeds(t,h):kind='no_complete_fragment_embedding'
     else:out.append(hh)
    co[kind]+=1;outcomes.append({'word':h,'kind':kind})
   row.append({'H':H,'level':t,'ports':[ih,I,oh,J],'bound':bound,'prefix_nodes':nodes,'paths':paths,'words':words,'outcomes':outcomes})
  print('UNIQUE',t,'in',len(states),'counts',dict(co),flush=True);states=out;rows.append({'level':t,'counts':dict(co),'rows':row})
  if not states:break
 (R/'paid201_unique_top_c3_ownership_discovery.json').write_text(json.dumps({'rows':rows,'open':states}))
