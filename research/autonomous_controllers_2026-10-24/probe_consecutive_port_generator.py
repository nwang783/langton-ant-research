#!/usr/bin/env python3
"""Derived local complete histories with physical first-return obligations."""
from functools import lru_cache

def generate(I,J,isC,rels,allowed_parity=None):
 plus,minus,dep=(1,3,2)if isC else(0,2,3)
 dm={a:b for a,b,L in rels};pm={b:a for a,b,L in rels}
 assert len(dm)==len(rels)and len(pm)==len(rels)
 bound=2*(I+J)+1 if isC else 2*(I+J)
 out=[]
 def dfs(k,ni,nj,lastdep,pending,hs):
  if ni==I and nj==J and pending is None and (allowed_parity is None or k%2==allowed_parity):out.append(hs)
  if k==bound:return
  for h in(plus,minus):
   isp=h==plus;isd=(h+(1 if k%2==0 else-1))%4==dep
   ii=ni+isp;jj=nj+isd
   if ii>I or jj>J:continue
   if pending is not None and not(isp and ni==pending):continue
   if isp and ni in pm and lastdep!=pm[ni]:continue
   newpending=dm.get(nj)if isd else None
   if newpending is not None and ii!=newpending:continue
   dfs(k+1,ii,jj,nj if isd else None,newpending,hs+(h,))
 dfs(0,0,0,None,None,())
 return out
if __name__=='__main__':
 import probe_boundary_extension as p
 for I in range(6):
  for J in range(6):
   for c in(0,1):
    a=set(generate(I,J,c,[]));b=set(p.words(I,J,c,[])[0]);assert a==b,(I,J,c,len(a),len(b))
 print('all 72 zero-relation cases passed')
