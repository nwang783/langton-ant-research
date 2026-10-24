#!/usr/bin/env python3
"""Discovery only: exact prefix-ranked enumeration, derived bound, even T12."""
import json,time
from pathlib import Path
from collections import Counter
import explore_drift31_inventory20 as m
R=Path(__file__).resolve().parent

def domain(I,J,ih,oh,paths):
 dm={p['outgoing_ordinal']:p['incoming_ordinal']for p in paths};pm={v:k for k,v in dm.items()};assert len(dm)==len(pm)==len(paths)
 assert all(p['outgoing_heading']==oh and p['incoming_heading']==ih for p in paths)
 bound=2*(I+J)+1;out=[]
 def dfs(hs,ni,nj,lastdep,pending):
  k=len(hs)
  if ni==I and nj==J and pending is None and k%2==0:out.append(hs)
  if k==bound:return
  for h in(ih,(ih+2)%4):
   isp=h==ih;isd=(h+(1 if k%2==0 else-1))%4==oh;ii=ni+isp;jj=nj+isd
   if ii>I or jj>J:continue
   if pending is not None and not(isp and ni==pending):continue
   if isp and ni in pm and lastdep!=pm[ni]:continue
   nxt=dm.get(nj)if isd else None
   if nxt is not None and ii!=nxt:continue
   dfs(hs+(h,),ii,jj,nj if isd else None,nxt)
 dfs((),0,0,None,None);return out

def main():
 q=json.load(open(R/'drift31_middle_short_even_gap_discovery.json'));B=[{int(t):tuple(h)for t,h in H.items()}for H in q['T11_states']];C=Counter();out=[];details=[]
 for i,H in enumerate(B):
  k,G,rp=m.paths(H,12);I=len(m.depart(H[9],0));J=H[11].count(1);dd=domain(I,J,0,1,rp[1]);cc=Counter()
  for w in dd:
   kind,g=m.Gof(H|{12:w});C[kind]+=1;cc[kind]+=1
   if kind=='open':out.append(H|{12:w})
  details.append({'parent_index':i,'domain_count':len(dd),'outcomes':dict(cc)})
  if i%10==0:print(i,'totals',dict(C),'domain',len(dd),flush=True)
  (R/'drift31_middle_short_T12_discovery.json').write_text(json.dumps({'scope':__doc__,'processed_parents':i+1,'outcomes':dict(C),'details':details,'states':[{str(t):h for t,h in H.items()}for H in out]}))
 print('DONE',dict(C),'open',len(out))
if __name__=='__main__':main()
