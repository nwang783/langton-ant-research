#!/usr/bin/env python3
"""Safe cap-four CELL-flow cycle filter from signed KT.
Track count-three connectivity and seam parity in the ACTUAL full cylinder.
A closed simple quotient cycle has winding0 or+/-1; even parity is exactly
a forbidden finite physical cycle. Odd essential cycles are retained.
"""
def transition(state,old,new,p,geometry):
 rows=(old,new)
 def active(row):return {c for c,a in enumerate(row) if 3 in a['ins'] or 3 in a['outs']}
 A=active(old);B=active(new);stored={c for comp in state for c,w in comp};assert stored==A,(stored,A)
 nodes={(0,c) for c in A}|{(1,c) for c in B};parent={v:v for v in nodes};pot={v:0 for v in nodes}
 def find(v):
  if parent[v]!=v:
   root,w=find(parent[v]);pot[v]=(pot[v]+w)%2;parent[v]=root
  return parent[v],pot[v]
 def join(a,b,k,check):
  ra,wa=find(a);rb,wb=find(b)
  if ra==rb:return not(check and (wa+k-wb)%2==0)
  parent[rb]=ra;pot[rb]=(wa+k-wb)%2;return True
 for comp in state:
  c0,w0=comp[0];assert w0==0
  for c,w in comp[1:]:assert join((0,c0),(0,c),w,False)
 for ar,ac,br,bc,d,k in geometry.splice_arcs(p):
  u=rows[ar][ac]['outs'][d];v=rows[br][bc]['ins'][d]
  assert u==v
  if u==3:
   if not join((ar,ac),(br,bc),k,True):return None
 groups={}
 for c in sorted(B):
  root,w=find((1,c));groups.setdefault(root,[]).append((c,w))
 comps=[]
 for cs in groups.values():
  base=cs[0][1];comps.append(tuple((c,(w-base)%2) for c,w in cs))
 return tuple(sorted(comps))
