#!/usr/bin/env python3
"""Discovery only. Complete-read top profiles to normal depth7; arbitrary parity."""
import json
from pathlib import Path
from collections import Counter
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
from explore_drift31_inventory20 import generated
ROOT=Path(__file__).resolve().parent

def GG(H):
 L=sorted(H);return graph([H[t]for t in L],L)
def main():
 states=[{20:(0,),21:(),22:(),23:()}]
 for t in range(19,12,-1):
  S=Counter();out=[]
  for H in states:
   k,G=GG(H);assert k=='open';L=sorted(H);_,pp=returns_to([H[z]for z in L],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   rel=[(p['outgoing_ordinal'],p['incoming_ordinal'],p['outgoing_heading'],p['incoming_heading'])for p in pp]
   for parity in [0,1]:
    if sum(len(h)%2 for h in H.values())+parity>5:continue
    for h in generated(t%2,2*(I+J)+1,ih,I,oh,J,parity,rel):
     HH=H|{t:h};k,g=GG(HH);S[k]+=1
     if k=='open':out.append(HH)
  print(t,'parents',len(states),'outcomes',dict(S),flush=True);states=out
  profiles=Counter(tuple(len(H[x])%2 for x in range(20,t-1,-1))for H in states)
  print('profiles',len(profiles),dict(profiles),flush=True)
  (ROOT/'drift31_top_parity_profiles_discovery.json').write_text(json.dumps({'depth':20-t,'states':[{str(t):h for t,h in H.items()}for H in states],'profiles':{''.join(map(str,k)):v for k,v in profiles.items()}}))
if __name__=='__main__':main()
