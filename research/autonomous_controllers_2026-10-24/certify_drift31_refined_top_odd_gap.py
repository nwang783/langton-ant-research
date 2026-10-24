#!/usr/bin/env python3
"""Refined top boundary theorem: some of M-1,M-2,M-3,M-5,M-6 is odd-read.
Complete WHITE full(3,1) front, invariant incoming axis V on even T. Read maxM
is even and a singletonN. No growth, global cap, period, or lower boundary.
"""
import json,hashlib
from pathlib import Path
from collections import Counter
from itertools import combinations
from certify_drift31_read_minimum import words,depart,returns_to
from partial_drift31_graph import graph
ROOT=Path(__file__).resolve().parent


def complete_words(axis,bound,ih,I,oh,J):
 # Fix n and the number r of incoming ih on R ranks. Then l=I-r on L.
 # Outgoing counts depend only on (n,r,l), so individual position subsets
 # enumerate each complete word exactly once, without a visit-count cap.
 for n in range(bound+1):
  ev=tuple(range(0,n,2));od=tuple(range(1,n,2));other=(ih+2)%4
  for r in range(max(0,I-len(od)),min(I,len(ev))+1):
   l=I-r
   count=r*((ih+1)%4==oh)+(len(ev)-r)*((other+1)%4==oh)+l*((ih-1)%4==oh)+(len(od)-l)*((other-1)%4==oh)
   if count!=J:continue
   for rr in combinations(ev,r):
    for ll in combinations(od,l):
     h=[other]*n
     for j in rr+ll:h[j]=ih
     yield tuple(h)

def fmt(H):return{str(t):list(h)for t,h in sorted(H.items())}
def GG(H):
 levels=sorted(H);return graph([H[t]for t in levels],levels)
def main():
 states=[{20:(0,),21:(),22:(),23:()}];records=[];totals={}
 for t in range(19,12,-1):
  out=[];count=Counter()
  for H in states:
   k,G=GG(H);assert k=='open';levels=sorted(H);_,pp=returns_to([H[z]for z in levels],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   bound=2*(I+J)+1;dd=[]
   for h in complete_words(t%2,bound,ih,I,oh,J):
    if t>13 and t!=16 and len(h)%2:continue
    if not all([j for j,hi in enumerate(h)if hi==p['incoming_heading']][p['incoming_ordinal']]==depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]+1 for p in pp):continue
    dd.append(h)
   entry={'level':t,'complete_named_before':fmt(H),'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'derived_bound':bound,'required_parity':0 if t>13 and t!=16 else None,'actual_first_returns':pp,'complete_domain':dd,'outcomes':[]}
   for h in dd:
    HH=H|{t:tuple(h)};kind,w=GG(HH);count[kind]+=1;r={'word':h,'outcome':kind}
    if kind=='open':out.append(HH)
    else:r['witness']=w
    if t==13:
     assert kind=='skipped_rank'
     lev=sorted(HH)
    entry['outcomes'].append(r)
   records.append(entry)
  totals[t]=dict(count);print(t,len(states),dict(count));states=out
 assert not states and totals[13]=={'skipped_rank':62}
 result={'scope':__doc__,'normal':'T=3y-x','normalization':'translate even actual maximum M to20','hypothesis_even_read_levels':[14,15,17,18,19],'lower_exterior':'Every omitted level <=12 remains UNKNOWN; T13 has unrestricted parity.','records':records,'counts':totals,'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in ['DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','partial_drift31_graph.py','certify_drift31_read_minimum.py']},'scope_warning':'T16 andT13 have unrestricted parity. No particular odd-inventory family is excluded here unless its full ownership is separately proved.'}
 (ROOT/'drift31_refined_top_odd_gap_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':main()
