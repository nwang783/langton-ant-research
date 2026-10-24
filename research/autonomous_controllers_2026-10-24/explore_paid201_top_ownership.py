#!/usr/bin/env python3
"""Discovery: exact upper-derived histories and paid201 owned read embeddings.
No result is promoted without frozen explicit witnesses and independent audit.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json
from certify_drift31_refined_top_odd_gap import complete_words
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent
F=json.load(open(R/'open79_paid_chain201_certificate.json'));E=F['events'];by=defaultdict(lambda:defaultdict(list))
for e in E:by[e['normal_level']][tuple(e['position'])].append(e)
assert all(tuple(e['position'])!=(5,2)for e in E) # A complete period P<=200 is impossible.
def embeds(t,h):
 groups=sorted(by[t].values(),key=lambda g:(-g[0]['position'][1],g[0]['time']))
 ans=[]
 def rec(k,after,mp):
  if k==len(groups):ans.append(mp);return
  g=groups[k]
  for j in range(after,len(h)-len(g)+1):
   if all(h[j+a]==e['incoming_heading']and(j+a)%2==(e['turn']=='L')for a,e in enumerate(g)):
    rec(k+1,j+len(g),mp|{e['time']:(t,j+a)for a,e in enumerate(g)})
 rec(0,0,{})
 return ans

def anchored(H,G,anchors):
 levels=sorted(H);where={}
 for c,ch in enumerate(G['chains']):
  for a,((i,j),k)in enumerate(ch):where[levels[i],j]=(c,a,k)
 fixed={};eq=[]
 for time,(t,j)in anchors.items():
  c,a,k=where[t,j];val=(time-a,k-E[time]['position'][1])
  if c in fixed and fixed[c]!=val:
   x,y=fixed[c];aa,bb=val
   if y==bb:return False,{'reason':'zero_period_clock_mismatch','chain':c,'two_affine_starts':[fixed[c],val]}
   pn=aa-x;pd=y-bb
   if pn%pd or pn//pd<=200:return False,{'reason':'fixed_period_not_above201_factor','chain':c,'two_affine_starts':[fixed[c],val],'period_fraction':[pn,pd]}
   eq.append(pn//pd)
  fixed[c]=val
 if len(set(eq))>1:return False,{'reason':'inconsistent_exact_periods','periods':eq}
 return True,{'fixed_chain_starts':fixed,'periods':eq}

results=[]
for c in[3,5]:
 O={0,1,2,6,7,6*c+1,32,34};states=[({34:(0,),35:(),36:(),37:()}, {})];records=[]
 for t in range(33,28,-1):
  out=[];counts=Counter();domains=0
  for H,anchors in states:
   levels=sorted(H);kind,G=graph([H[z]for z in levels],levels);assert kind=='open';_,paths=returns_to([H[z]for z in levels],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   bound=2*(I+J)+1
   for h in complete_words(t%2,bound,ih,I,oh,J):
    if len(h)%2!=(t in O):continue
    domains+=1
    if not all([j for j,hi in enumerate(h)if hi==p['incoming_heading']][p['incoming_ordinal']]==depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]+1 for p in paths):counts['first_return_rank']+=1;continue
    hh=H|{t:h};lev=sorted(hh);kind,gg=graph([hh[z]for z in lev],lev)
    if kind!='open':counts[kind]+=1;continue
    em=embeds(t,h)
    if not em:counts['no_complete_fragment_embedding']+=1;continue
    for mp in em:
     aa=anchors|mp;ok,w=anchored(hh,gg,aa)
     if not ok:counts[w['reason']]+=1;continue
     counts['open']+=1;out.append((hh,aa))
  print('c',c,'level',t,'states_in',len(states),'complete_domains',domains,dict(counts),flush=True);records.append({'level':t,'input_states':len(states),'complete_domains':domains,'counts':dict(counts)})
  states=out
  if not states:break
 results.append({'c':c,'records':records,'open':[{'H':H,'anchors':mp}for H,mp in states]})
(R/'paid201_top_ownership_discovery.json').write_text(json.dumps(results))
