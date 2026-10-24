#!/usr/bin/env python3
"""Finite sanity checks only; never a proof of universal capture."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'research/recovered_bundle/ant_global/root/standard.json'
x=json.loads(p.read_text());w=x['word'];assert len(w)==104 and set(w)=={'R','L'}
factors={''.join(w[(i+j)%104]for j in range(10))for i in range(104)}
assert len(factors)==84
# The standard fixture uses headings 0=N,1=E,2=S,3=W.
B={tuple(q)for q in x['seed']};pos=(0,0);h=x['heading'];V=((0,1),(1,0),(0,-1),(-1,0))
for k in range(100):
 begin=pos;start_h=h;word=[]
 for i in range(104):
  black=pos in B;word.append('L'if black else'R')
  if black:B.remove(pos)
  else:B.add(pos)
  h=(h+(-1 if black else 1))%4;pos=(pos[0]+V[h][0],pos[1]+V[h][1])
 assert ''.join(word)==w and h==start_h
 assert [pos[0]-begin[0],pos[1]-begin[1]]==x['drift']
print(json.dumps({'status':'PASS finite smoke checks only','canonical_word_length':104,'cyclic_length_10_factors':84,'fixture_periods_replayed':100,'reads':10400,'fixture_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'universal_conjecture':'UNSOLVED'},indent=2))
