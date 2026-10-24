#!/usr/bin/env python3
"""Uniform top boundary theorem: some of M-1,...,M-6 must be odd-read.
Complete WHITE full(3,1) front, invariant incoming axis V on even T. Read maxM
is even and a singletonN. No growth, global cap, period, or lower boundary.
"""
import json,hashlib
from pathlib import Path
from collections import Counter
from certify_drift31_read_minimum import words,depart,returns_to
from partial_drift31_graph import graph
ROOT=Path(__file__).resolve().parent

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
   for h in words(t%2,bound,ih,I,oh,J):
    if t>13 and len(h)%2:continue
    if not all([j for j,hi in enumerate(h)if hi==p['incoming_heading']][p['incoming_ordinal']]==depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]+1 for p in pp):continue
    dd.append(h)
   entry={'level':t,'complete_named_before':fmt(H),'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'derived_bound':bound,'required_parity':0 if t>13 else None,'actual_first_returns':pp,'complete_domain':dd,'outcomes':[]}
   for h in dd:
    HH=H|{t:tuple(h)};kind,w=GG(HH);count[kind]+=1;r={'word':h,'outcome':kind}
    if kind=='open':out.append(HH)
    else:r['witness']=w
    if t==13:
     assert kind=='skipped_rank'and(w['rank_before'],w['rank_after'])==(0,2)and len(w['segment'])==9
     lev=sorted(HH);assert lev[w['segment'][0][0][0]]==14
    entry['outcomes'].append(r)
   records.append(entry)
  totals[t]=dict(count);print(t,len(states),dict(count));states=out
 assert not states and totals[13]=={'skipped_rank':10}
 result={'scope':__doc__,'normal':'T=3y-x','normalization':'translate even actual maximum M to20','hypothesis_even_read_levels':[14,15,16,17,18,19],'lower_exterior':'Every omitted level <=12 remains UNKNOWN; T13 has unrestricted parity.','records':records,'counts':totals,'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in ['DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','partial_drift31_graph.py','certify_drift31_read_minimum.py']},'family_corollary':'For the signed live two-quad g8 family O={0,1,2,5,6,6a+1,6b+2,6c+2},1<=b<a<=c,a>=2,c>=3, a<c puts the next largest odd at least7 below max. Hence a=c is necessary. No claim of completion or exclusion when a=c.'}
 (ROOT/'drift31_top_odd_gap_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':main()
