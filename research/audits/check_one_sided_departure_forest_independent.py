"""Independent literal orbit and finite exceptional-cycle controls.
Universal termination of b-orbits is the analytic first-time proof.
"""
from pathlib import Path
from itertools import product
from random import Random
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];rng=Random(610274);dirs=(1j,1,-1j,-1)
eight=[]
for word in product('RL',repeat=8):
 q=0j;h=0;points=[q]
 for c in word:h=(h+(1 if c=='R'else-1))%4;q+=dirs[h];points.append(q)
 if q==0 and h==0 and word.count('R')-word.count('L')==4:
  assert len(set(points[:-1]))<8;eight.append(''.join(word))
assert eight
paths=roots=cycles=0;largest=0
for case in range(100):
 seed={complex(x,y)for x in range(-5,6)for y in range(-5,6)if rng.randrange(10)==0}if case else set()
 board=set(seed);q=0j;h=0;first={};edge={};turns=[];N=2800
 for t in range(N):
  isfirst=q not in first
  if isfirst:first[q]=(t,h)
  right=q not in board;turns.append('R'if right else'L');h=(h+(1 if right else-1))%4;target=q+dirs[h]
  if isfirst and q not in seed:edge[q]=target
  board.symmetric_difference_update({q});q=target
 known_roots=set()
 for start,(time,_)in first.items():
  if start in seed or time>N-5:continue
  v=start;chain=[];seen={}
  while v not in seed and v not in seen:
   assert v in first and v in edge
   assert first[v][0]<=time+3
   seen[v]=len(chain);chain.append(v);v=edge[v]
  assert len(chain)<=time+4;largest=max(largest,len(chain));paths+=1
  if v in seed:known_roots.add(('black',v))
  else:
   cyc=chain[seen[v]:];assert len(cyc)==4 and 0j in cyc and turns[:4]==list('RRRR')
   assert {first[z][0]for z in cyc}=={0,1,2,3};known_roots.add(('cycle',0j))
 assert len(known_roots)<=len(seed)+1
 hascycle=('cycle',0j)in known_roots
 assert hascycle==(turns[:4]==list('RRRR'))
 cycles+=hascycle;roots+=len(known_roots)
note=ROOT/'periodic_classification_new/one_sided_first_departure_forest.md'
out=dict(status='PASS independent actual first-departure orbit and exceptional-cycle controls',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),boards=100,literal_updates=100*2800,white_orbits_checked=paths,root_components_seen=roots,initial_RRRR_cycles=cycles,largest_checked_orbit=largest,clockwise_closed_eight_turn_words_checked=len(eight),scope='All-board forest theorem is analytic; controls retain initial-black terminals and the initial-head exception. No bound on incoming tree size or later ant visits.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
