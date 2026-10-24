#!/usr/bin/env python3
"""Base-k two-root inflation adapter without replacing k by k squared."""
from phase_permuted_recurrence import PhaseRecurrence
from selfsimilar_visit_relations import D,add,rot
from automatic_radix import Rel,reverse_msb
from math import isqrt
import json,time

def model(u,v):
 assert len(u)==len(v)>1 and u[0]=='L' and v[0]=='R'
 assert set(u+v)<=set('RL');words=[u,v];k=len(u);pp=[];hh=[];ends=[]
 for w in words:
  p=(0,0);h=0;ps=[];hs=[]
  for c in w:
   ps.append(p);hs.append(h);h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h])
  pp.append(ps);hh.append(hs);ends.append((p,h))
 a=ends[0][0];assert ends[0][1]==1 and ends[1]==((-a[0],-a[1]),3)
 states=[(0,0,0,1)];ix={states[0]:0};nxt=[];off=[];perm=[]
 for hR,cR,hL,cL in states:
  row=[];ofs=[]
  for j in range(k):
   new=((hL+hh[cL][j])%4,int(words[cL][j]=='L'),(hR+hh[cR][j])%4,int(words[cR][j]=='L'))
   if new not in ix:ix[new]=len(states);states.append(new)
   row.append(ix[new]);ofs.append([rot(pp[cL][j],hL),rot(pp[cR][j],hR)])
  nxt.append(row);off.append(ofs);perm.append([[1,0]for _ in range(k)])
 rec=PhaseRecurrence(k,a,nxt,perm,off);rec.validate()
 return rec,states

def controls():
 out=[]
 for u,v in [('LRLRLRRLRLRLRLRRL','RLRRLRRLRLRLRLRLR'),('LRLRLRLRLRLRRLRRL','RLRRLRLRLRLRRLRLR')]:
  rec,states=model(u,v);checked=0
  for phase,root in enumerate('RL'):
   w=root
   while len(w)<600:w=''.join(u if c=='R'else v for c in w);w=''.join(u if c=='R'else v for c in w)
   p=(0,0);h=0
   for n,c in enumerate(w[:600]):
    assert rec.point(n,phase)==p
    assert states[rec.state(n)][2*phase:2*phase+2]==(h,int(c=='L'))
    h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h]);checked+=1
  out.append(dict(R=u,L=v,scale=rec.scale,controls=len(states),literal_pose_checks=checked))
 return out

if __name__=='__main__':
 from pathlib import Path
 out={'status':'PASS finite root-cycle geometry controls','cases':controls()};Path(__file__).with_name('cyclic_root_geometry_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
