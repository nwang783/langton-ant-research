#!/usr/bin/env python3
"""Exact factorized generation of all internally matched row histories.
No chronology, growth, symmetry, count or color-state pruning is added.
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
 buckets=[]
 for j,cs in enumerate(hs):
  ix=defaultdict(list)
  for c in cs:
   key=tuple(c['outs'][d] if source else c['ins'][d] for _,source,d in past[j]);ix[key].append(c)
  buckets.append(ix)
 out=[];chosen=[]
 def gen(j):
  if j==len(hs):out.append(chosen[:]);return
  key=tuple(chosen[a]['ins'][d] if source else chosen[a]['outs'][d] for a,source,d in past[j])
  for c in buckets[j].get(key,()):chosen.append(c);gen(j+1);chosen.pop()
 gen(0);return out
