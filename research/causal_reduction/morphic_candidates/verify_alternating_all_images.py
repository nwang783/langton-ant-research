#!/usr/bin/env python3
"""Independently verify the new frozen root-cycle records without source imports."""
from pathlib import Path
from itertools import product
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'audits/check_alternating_nine_all_images.records.json'
records=json.loads(source.read_text())
def geom(w,stop=False):
 z=0j;h=1j;last={};bad=None
 for i,c in enumerate(w):
  if z in last and last[z][1]==c and bad is None:
   bad=(i,last[z][0],int(z.real),int(z.imag),c)
   if stop:return bad
  last[z]=(i,c);h*=(-1j if c=='R' else 1j);z+=h
 return (int(z.real),int(z.imag),int(h.real),int(h.imag)),bad
images={'R':[], 'L':[]};legal={'R':[], 'L':[]}
for chars in product('LR',repeat=9):
 w=''.join(chars);p,b=geom(w)
 for c,target in [('R',(3,0,1,0)),('L',(-3,0,-1,0))]:
  if p==target:
   images[c].append(w)
   if b is None:legal[c].append(w)
expected=set()
for a,b,c,d in product(legal['R'],legal['L'],images['R'],images['L']):
 outer={'R':a,'L':b};s={r:''.join(outer[v] for v in w) for r,w in [('R',c),('L',d)]}
 for root in 'RL':
  f=s[root][0];g=s[f][0]
  if f==root:period=1
  elif g==root:period=2
  else:period=0
  expected.add((a,b,c,d,root,period))
seen=set();new=0;latest=0
for row in records:
 a,b,c,d,root,period,*stored=row
 key=tuple(row[:6]);assert key in expected and key not in seen;seen.add(key)
 new+=1;outer={'R':a,'L':b};s={r:''.join(outer[v] for v in w) for r,w in [('R',c),('L',d)]}
 prefix=''.join(s[v] for v in s[root]);assert period==0 or prefix[0]==root
 got=geom(prefix,True);assert list(got)==stored,(key,got,stored)
 latest=max(latest,got[0])
assert seen==expected
out=dict(record_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),all_cycle_cases_complete=True,all_cycle_cases_replayed=new,latest_conflict=latest,total_inventory=len(expected),scope='Every literal composite-squared image independently regenerated and replayed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
