#!/usr/bin/env python3
"""Same signed axis zone abstraction, exact pair-factorized row generation.
Exploratory producer. Completeness of a finished finite graph needs replay.
"""
from collections import defaultdict
import sys
import probe_axis_zone as z
from probe_diagonal_n_window import histories

def rows(p,cap,n):
 assert n==4
 A=histories(0,cap);B=histories(1,cap);ix=defaultdict(list)
 for b in B:ix[b['outs'][1],b['outs'][3]].append(b)
 out=[]
 for a0 in A:
  for a1 in A:
   for b0 in ix[a1['ins'][1],a0['ins'][3]]:
    for b1 in ix[a0['ins'][1],a1['ins'][3]]:
     out.append([a0,b0,a1,b1] if p==0 else [b1,a0,b0,a1])
 return out
z.rows=rows
if __name__=='__main__':
 args=list(map(int,sys.argv[1:]));z.run(args[0],2,*args[1:])
