#!/usr/bin/env python3
"""Independent exact singleton first-block proof using a trie/failure automaton.
This detects finite104-letter blocks, never claims permanent capture.
"""
from pathlib import Path
from collections import deque
import json,csv,hashlib,time
R=Path(__file__).resolve().parents[1];source=R/'computability/singleton_first_block_input.json';I=json.loads(source.read_text());W=I['word'];assert len(W)==104 and set(W)=={'R','L'}
# Bind the literal standard word to the independently audited source definition.
import sys
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W as canonical
assert W==canonical
nxt=[{}];fail=[0];done=[False]
for j in range(104):
 s=0
 for c in W[j:]+W[:j]:
  if c not in nxt[s]:nxt[s][c]=len(nxt);nxt.append({});fail.append(0);done.append(False)
  s=nxt[s][c]
 done[s]=True
queue=deque()
for c in 'RL':
 if c in nxt[0]:queue.append(nxt[0][c])
 else:nxt[0][c]=0
while queue:
 s=queue.popleft()
 for c in 'RL':
  if c in nxt[s]:
   t=nxt[s][c];fail[t]=nxt[fail[s]][c];done[t]|=done[fail[t]];queue.append(t)
  else:nxt[s][c]=nxt[fail[s]][c]
TR=[(d['R'],d['L']) for d in nxt];D=((0,1),(1,0),(0,-1),(-1,0))
def simulate(seed,save_reads=False):
 B=set(seed);x=y=h=s=radius=0;reads=set()
 for t in range(1,200001):
  p=(x,y)
  if save_reads:reads.add(p)
  black=p in B
  if black:B.remove(p)
  else:B.add(p)
  s=TR[s][black];h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy;radius=max(radius,abs(x),abs(y))
  if done[s]:return t,len(B),radius,reads
 raise AssertionError(('No finite block',seed))
start=time.time();blank=simulate([],True);sites=sorted(blank[3]);assert blank[0]==10081==I['blank_first_block_end'];assert sites==list(map(tuple,I['candidate_sites'])) and len(sites)==1398
old={ (int(r['seed_x']),int(r['seed_y'])):(int(r['first_end']),int(r['black_at_first_end']),int(r['max_radius'])) for r in csv.DictReader((R/'computability/singleton_first_block.csv').open())};assert set(old)==set(sites)
rows=[];total=0
for i,p in enumerate(sites):
 t,m,r,_=simulate([p]);assert(t,m,r)==old[p],(p,(t,m,r),old[p]);total+=t;rows.append([*p,t,m,r])
 if i%200==199:print('passed',i+1,flush=True)
maximum=max(r[2]for r in rows);worst=[r[:2]for r in rows if r[2]==maximum];assert maximum==106362 and worst==[[7,7]] and total==14740545
out={'status':'Independent finite exhaustive singleton first-cyclic104-block certificate passed','blank_first_block_end':blank[0],'candidate_count':len(sites),'total_literal_moves':total,'maximum_first_block_end':maximum,'worst_sites':worst,'automaton_states':len(nxt),'scope':'All single black sites anywhere via first-difference coupling; first observed block only, NOT permanent highway onset','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'rows':rows,'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='rows'})
