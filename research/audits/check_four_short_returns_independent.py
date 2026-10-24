"""Every four-step physical return is one unit-face loop, first turn free.
Exhaustive internal-color consistency of four consecutive returns, any board.
"""
from pathlib import Path
from itertools import product
import json
rows=[];short=[]
for n in(3,4):
 for initial in('R','L'):
  for orientations in product('RL',repeat=n):
   origin_turns=[initial if j%2==0 else('L'if initial=='R'else'R')for j in range(n)]
   word=''.join(a+b*3 for a,b in zip(origin_turns,orientations));p=0j;h=1j;last={};conflict=None;visits=[]
   for t,c in enumerate(word):
    if p in last and last[p][1]==c and conflict is None:conflict=[last[p][0],t,[int(p.real),int(p.imag)],c]
    last[p]=(t,c);visits.append((int(p.real),int(p.imag)));h*=(-1j if c=='R'else 1j);p+=h
    if t%4==3:assert p==0j
   row={'initial_turn':initial,'loop_orientations':orientations,'word':word,'first_conflict':conflict}
   (rows if n==4 else short).append(row)
assert len(rows)==32 and all(r['first_conflict']is not None for r in rows)
assert any(r['first_conflict']is None for r in short)
out={'status':'PASS all32 four-return cases have an internal color conflict; three returns can be legal','four_return_cases':rows,'three_return_legal_controls':[r for r in short if r['first_conflict']is None],'scope':'Any literal ordinary ant coloring; four successive physical returns each of exact length4 are impossible. Does not exclude separated or longer returns.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('legal three-return words',[r['word']for r in short if r['first_conflict']is None])
