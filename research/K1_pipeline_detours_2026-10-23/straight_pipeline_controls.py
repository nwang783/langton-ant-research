"""Literal pipeline controls only; no period/drift front search."""
from collections import defaultdict,Counter,deque
from pathlib import Path
import json
R=Path(__file__).resolve().parent
D=(1j,1,-1j,-1)
def inv(z):return[int(z.real),int(z.imag)]
def literal(word,copies):
 a=copies;d=complex(-a,a);P=len(word)*copies;q=0j;h=1j;hist=defaultdict(list);flow=Counter()
 def canon(z):
  k=int(-z.real)//a;return z-k*d,k
 for t,c in enumerate(word*copies):
  z,k=canon(q);out=h*(-1j if c=='R'else 1j);hist[z].append((t-k*P,h,c));flow[z,out]+=1;q+=out;h=out
 assert q==d and h==1j
 hist={z:sorted(es)for z,es in hist.items()}
 hs=[]
 for z,es in sorted(hist.items(),key=lambda kv:(kv[0].real,kv[0].imag)):
  good=all(es[j][2]!=es[j-1][2]for j in range(1,len(es)))
  hs.append(dict(cell=inv(z),transverse=int(z.real+z.imag),turns=''.join(c for t,h,c in es),incoming=[inv(h)for t,h,c in es],times=[t for t,h,c in es],alternating=good,input_color='white'if es[0][2]=='R'else'black'))
 return dict(word=word,copies=copies,full_period=P,full_drift=inv(d),histories=hs,all_alternating=all(x['alternating']for x in hs))
short=[literal('RRRRLR',a)for a in(1,2,3)]
prepared=[literal('RRRLLLLRLR',a)for a in(1,2,3)]
assert all(not x['all_alternating']for x in short)
assert all(x['all_alternating']for x in prepared)
for x in prepared:
 assert {y['transverse']for y in x['histories']if y['input_color']=='black'}=={-2}
 assert Counter((y['transverse'],y['turns'])for y in x['histories'])==Counter({(-2,'L'):x['copies'],(-1,'RLRL'):x['copies'],(0,'RLRL'):x['copies'],(1,'R'):x['copies']})
# Direct finite-board positive controls. Two head helpers plus n lower-rail blacks.
positives=[]
for n in(1,2,3,10,100):
 seed={0-1j,1-2j}|{complex(-i,i-2)for i in range(n)};black=set(seed);q=0j;h=1j;seen=defaultdict(list)
 for t,c in enumerate('RRRLLLLRLR'*n):
  got='L'if q in black else'R';assert got==c
  seen[q].append((t,h,got));black.symmetric_difference_update({q});h*=(-1j if got=='R'else 1j);q+=h
 assert q==complex(-n,n)and h==1j and len(black)==len(seed)
 # Continuing the next prefix is forced until missing lower fuel demands R instead of L.
 mismatch=None
 for j,c in enumerate('RRRLLLLRLR'):
  got='L'if q in black else'R'
  if got!=c:mismatch=dict(next_stage_offset=j,position=inv(q),expected=c,actual=got);break
  black.symmetric_difference_update({q});h*=(-1j if got=='R'else 1j);q+=h
 assert mismatch['next_stage_offset']==4 and mismatch['position']==[-n,n-2]
 positives.append(dict(stages=n,initial_black_count=len(seed),initial_black=[inv(z)for z in sorted(seed,key=lambda z:(z.real,z.imag))],matched_steps=10*n,first_mismatch=mismatch))
res=dict(status='PASS literal exact controls; NOT a white translating front',scope='Uniform straight-diagonal K1 contact prototype only. Word6 fails on every coloring; word10 is a prepared translator consuming one black lower-rail cell per stage. Full drifts retained for all copies.',six_step_controls=short,ten_step_controls=prepared,finite_fuel_controls=positives)
(R/'straight_pipeline_controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(dict(status=res['status'],six_step_invalid=[x['full_period']for x in short],ten_step_valid=[x['full_period']for x in prepared],finite_prefixes=[x['matched_steps']for x in positives])))
