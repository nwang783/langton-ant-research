#!/usr/bin/env python3
"""Exact finite local-factor certificate, not a period/width front scan.
All input colors are arbitrary. Five consecutive first returns at one
physical cell, each of length 4 or 8, are impossible.
"""
from itertools import product
from pathlib import Path
import json,hashlib
D=[(0,1),(1,0),(0,-1),(-1,0)]
programs=[]
for h0 in (0,2):
 for L in (4,8):
  for cs in product((1,-1),repeat=L):
   p=(0,0);h=h0;last={};trace=[];valid=True
   for t,c in enumerate(cs):
    if p in last and last[p]==c:valid=False;break
    last[p]=c;trace.append([list(p),h,c]);h=(h+c)%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
    if p==(0,0) and t<L-1:valid=False;break
   if valid and p==(0,0):programs.append(dict(h0=h0,h1=h,length=L,word=''.join('R' if c==1 else'L' for c in cs),trace=trace))
positions=sorted({tuple(p) for a in programs for p,h,c in a['trace']});ix={p:i for i,p in enumerate(positions)}
for a in programs:
 a['guard']=a['black']=a['xor']=0
 for p,h,c in a['trace']:
  bit=1<<ix[tuple(p)]
  if not a['guard']&bit:
   a['guard']|=bit
   if c==-1:a['black']|=bit
  a['xor']^=bit
levels=[[dict(h=0,guard=0,black=0,xor=0,path=[],cost=0)]];failures=[]
for depth in range(1,6):
 nxt=[]
 for parent,s in enumerate(levels[-1]):
  for j,a in enumerate(programs):
   if a['h0']!=s['h']:continue
   need=a['black']^(s['xor']&a['guard']);conflict=(need^s['black'])&s['guard']&a['guard']
   if conflict:
    if depth==5:failures.append(dict(parent=parent,program=j,conflict_cell=(conflict&-conflict).bit_length()-1))
    continue
   nxt.append(dict(h=a['h1'],guard=s['guard']|a['guard'],black=s['black']|(need&~s['guard']),xor=s['xor']^a['xor'],path=s['path']+[j],cost=s['cost']+a['length']))
 levels.append(nxt)
assert [len(a) for a in levels]==[1,12,42,48,16,0]
assert len(failures)==192
assert min(a['cost'] for a in levels[4])==20
result=dict(scope='Arbitrary initial colors, five successive first physical returns to one cell; each gap4 or8. Genuine rotation normalizes incoming N. No front, period or width cutoff.',positions=positions,programs=programs,compatible_prefixes=levels,fifth_step_conflicts=failures,summary=dict(counts=[len(a) for a in levels],minimum_costs=[min((a['cost'] for a in lev),default=None) for lev in levels],status='AUTHOR_EXACT_LOCAL_OBSTRUCTION'))
p=Path(__file__).with_name('four_eight_unit_returns.certificate.json');p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),**result['summary'])))
