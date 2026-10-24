#!/usr/bin/env python3
"""Targeted next ownership check with derived bounds and actual return prefix pruning."""
from pathlib import Path
from collections import Counter,defaultdict
import json
from explore_paid201_top_ownership import embeds,anchored
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent

def direct_words(I,J,ih,oh,paths,parity):
 dm={p['outgoing_ordinal']:p['incoming_ordinal']for p in paths};pm={v:k for k,v in dm.items()};assert len(dm)==len(pm)==len(paths)
 assert all(p['outgoing_heading']==oh and p['incoming_heading']==ih for p in paths)
 bound=2*(I+J)+1;out=[];nodes=0
 def dfs(hs,ni,nj,lastdep,pending):
  nonlocal nodes;nodes+=1;k=len(hs)
  if ni==I and nj==J and pending is None and k%2==parity:out.append(hs)
  if k==bound:return
  for h in(ih,(ih+2)%4):
   isp=h==ih;isd=(h+(1 if k%2==0 else-1))%4==oh;ii=ni+isp;jj=nj+isd
   if ii>I or jj>J:continue
   if pending is not None and not(isp and ni==pending):continue
   if isp and ni in pm and lastdep!=pm[ni]:continue
   nxt=dm.get(nj)if isd else None
   if nxt is not None and ii!=nxt:continue
   dfs(hs+(h,),ii,jj,nj if isd else None,nxt)
 dfs((),0,0,None,None);return out,bound,nodes

raw=json.load(open(R/'paid201_top28_ownership_discovery.json'))[0]['open'];groups=defaultdict(list)
for s in raw:
 H={int(t):tuple(h)for t,h in s['H'].items()};a={int(time):tuple(v)for time,v in s['anchors'].items()};groups[tuple(sorted(H.items()))].append(a)
rows=[];openstates=[];counts=Counter()
for key,maps in groups.items():
 H=dict(key);lev=sorted(H);_,G=graph([H[t]for t in lev],lev);_,paths=returns_to([H[t]for t in lev],G,27);I=len(depart(H[28],1));J=H[30].count(0)
 words,bound,nodes=direct_words(I,J,1,0,paths,0);co=Counter()
 for h in words:
  hh=H|{27:h};lev=sorted(hh);kind,gg=graph([hh[t]for t in lev],lev)
  if kind!='open':co[kind]+=1;continue
  em=embeds(27,h)
  if not em:co['no_complete_fragment_embedding']+=1;continue
  for old in maps:
   for mp in em:
    aa=old|mp;ok,w=anchored(hh,gg,aa)
    if not ok:co[w['reason']]+=1;continue
    co['open']+=1;openstates.append({'H':hh,'anchors':aa})
 counts.update(co);print('ports',I,J,'nodes',nodes,'domains',len(words),'maps',len(maps),dict(co),flush=True)
 rows.append({'H':H,'ports':[I,J],'bound':bound,'prefix_nodes':nodes,'complete_return_domains':words,'counts':dict(co)})
(R/'paid201_top27_ownership_discovery.json').write_text(json.dumps({'scope':__doc__,'rows':rows,'counts':dict(counts),'open':openstates}))
print('TOTAL',dict(counts),flush=True)
