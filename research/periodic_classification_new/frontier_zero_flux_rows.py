#!/usr/bin/env python3
"""Exact internally matched histories with necessary zero transverse cut flux.
The full event loop has zero net crossing of each transverse row cut. This
filters static inventories only; it imposes no period, width or growth cap.
"""
from collections import defaultdict
from probe_diagonal_n_window import histories

def rows(p,cap,g):
 hs=[histories(g.parity(p,c),cap) for c in range(g.a)];past=[[] for _ in hs]
 for ac,bc,d,k,delta in g.arcs[p]:
  if delta:continue
  assert ac!=bc
  if ac<bc:past[bc].append((ac,False,d))
  else:past[ac].append((bc,True,d))
 flux=[]
 for j,cs in enumerate(hs):
  ups=[d for c,cc,d,k,dr in g.arcs[p] if c==j and dr==1]
  fromabove=[d for c,cc,d,k,dr in g.arcs[1-p] if cc==j and dr==-1]
  flux.append({tuple(c['h']):sum(c['outs'][d] for d in ups)-sum(c['ins'][d] for d in fromabove) for c in cs})
 mins=[0]*(len(hs)+1);maxs=mins[:]
 for j in range(len(hs)-1,-1,-1):mins[j]=mins[j+1]+min(flux[j].values());maxs[j]=maxs[j+1]+max(flux[j].values())
 buckets=[]
 for j,cs in enumerate(hs):
  ix=defaultdict(list)
  for c in cs:
   key=tuple(c['outs'][d] if source else c['ins'][d] for _,source,d in past[j]);ix[key].append(c)
  buckets.append(ix)
 out=[];chosen=[]
 def gen(j,f):
  if f+mins[j]>0 or f+maxs[j]<0:return
  if j==len(hs):assert f==0;out.append(chosen[:]);return
  key=tuple(chosen[a]['ins'][d] if source else chosen[a]['outs'][d] for a,source,d in past[j])
  for c in buckets[j].get(key,()):chosen.append(c);gen(j+1,f+flux[j][tuple(c['h'])]);chosen.pop()
 gen(0,0);return out
