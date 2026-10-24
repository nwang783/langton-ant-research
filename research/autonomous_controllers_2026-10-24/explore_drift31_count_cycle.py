#!/usr/bin/env python3
"""Positive count-level cycle discovery only. Bounds are search limits, not proof exclusions."""
import json
from check_drift31_even_gap_transfer import h_opts,v_opts
start=(5,4,5,2);cap=24
layers=[{start:None}]
for step in range(6):
 out={}
 for state in layers[-1]:
  w,n,s,K=state;u=w+n-s
  for l in h_opts(w,s):
   e=2*s+w-4*l;nn=s+2*w-4*l
   for h in v_opts(n,e):
    ww=e-2*n+4*h;ss=2*e-3*n+4*h;z=(ww,nn,u,K+n-s)
    if max(ww,nn,u,ss)>cap or min(ww,nn,u,ss)<0:continue
    if abs(z[3])>cap:continue
    out.setdefault(z,(state,l,h,2*(w+s-2*l),2*(e-n+2*h)))
 layers.append(out);print(step+1,len(out),'goal',start in out,flush=True)
 if step==5 and start in out:
  path=[];at=start
  for j in range(6,0,-1):
   prev,l,h,nH,nV=layers[j][at];path.append({'before':prev,'lambda':l,'eta':h,'new_H_reads':nH,'new_V_reads':nV,'after':at});at=prev
  path.reverse();json.dump({'scope':__doc__,'search_cap':cap,'start':start,'cycle':path,'total_new_reads':sum(z['new_H_reads']+z['new_V_reads']for z in path),'warning':'Counts only: no ordinal words, clock state, finite factor or front claimed.'},open('drift31_count_cycle_discovery.json','w'),indent=2);print(json.dumps(path));break
