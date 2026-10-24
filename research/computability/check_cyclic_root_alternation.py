#!/usr/bin/env python3
"""Exact finite-carry closure: no equal-turn pair of reads of one cell.
If closure completes, each cell is read at most twice, with opposite turns.
This may certify an infinite-background ant; finite support is a separate test.
"""
from cyclic_root_geometry import model
from selfsimilar_visit_relations import add,sub,mul
from math import isqrt
from pathlib import Path
import json,time,hashlib

def check(u,v,cap=300000):
 rec,controls=model(u,v);k=rec.base;a=rec.scale;norm=sum(z*z for z in a)
 mx=max(x*x+y*y for row in rec.off for cell in row for x,y in cell)
 m=isqrt(mx)+(isqrt(mx)**2<mx);delta=2*m;r=0
 while norm*r*r<(r+delta)**2:r+=1
 # Different initial phases are unnecessary for comparing the same output
 # curve under a FIXED phase swap: equal numeral lengths force equal starts.
 states=[(rec.start,rec.start,c,(0,0),0)for c in range(2)]
 ix={s:i for i,s in enumerate(states)};parents=[None,None];edges=0;outside=0
 for at,st in enumerate(states):
  s,t,c,D,less=st
  if less and D==(0,0)and controls[s][2*c+1]==controls[t][2*c+1]:
   ds=[];z=at
   while parents[z] is not None:
    z,d,e=parents[z];ds.append((d,e))
   ds.reverse();n=q=0
   for d,e in ds:n=k*n+d;q=k*q+e
   return dict(status='SAME_TURN_PAIR',n=n,m=q,phase=c,cell=rec.point(n,c),nodes=len(states),radius=r)
  nc=1-c
  for d in range(k):
   for e in range(k):
    if not less and d>e:continue
    edges+=1;DD=add(mul(a,D),sub(rec.off[s][d][nc],rec.off[t][e][nc]))
    if DD[0]*DD[0]+DD[1]*DD[1]>r*r:outside+=1;continue
    ns=(rec.nxt[s][d],rec.nxt[t][e],nc,DD,int(less or d<e))
    if ns not in ix:
     if len(states)>=cap:return dict(status='NODE_CAP_UNKNOWN',nodes=len(states),radius=r)
     ix[ns]=len(states);states.append(ns);parents.append((at,d,e))
 payload=json.dumps(states,separators=(',',':')).encode()
 return dict(status='EXACT_NO_SAME_TURN_REPEATS',R=u,L=v,scale=a,control_states=len(controls),carry_radius=r,closed_states=len(states),checked_edges=edges,overflow_edges=outside,closure_sha256=hashlib.sha256(payload).hexdigest(),closed_states_data=states)

if __name__=='__main__':
 pairs=[('LRLRLRRLRLRLRLRRL','RLRRLRRLRLRLRLRLR'),('LRLRLRLRLRLRRLRRL','RLRRLRLRLRLRRLRLR')]
 out=[];start=time.monotonic()
 for u,v in pairs:
  ans=check(u,v);out.append(ans);print(json.dumps({k:v for k,v in ans.items()if k!='closed_states_data'}),flush=True)
 result={'cases':out,'seconds':time.monotonic()-start};Path(__file__).with_name('cyclic_root_alternation_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
