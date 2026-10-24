"""Independent finite controls of the explicit abstract rewrite construction.
The all-time proof is its disjoint block decomposition and generation counts."""
from pathlib import Path
from heapq import heappop,heappush
from math import isqrt
from collections import Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];note=ROOT/'cut_order_obstruction_2026-10-23/mass_sensitive/global_fifo_packing_obstruction.md';runs=[]
for q,limit in[(5,20001),(7,9001),(13,6001)]:
 queue=[(i,complex(i,0),None,i,0)for i in range(q)];serial=q;board={2*complex(i,0):(None,i)for i in range(q)};visited=set();depths=Counter();maxrootdist=0;minimum_age=None
 for tick in range(limit):
  _,z,birth,root,depth=heappop(queue);assert z not in visited;visited.add(z);p=2*z
  assert board.pop(p)==(birth,root)
  if birth is not None:
   age=tick-birth;assert age>=q;minimum_age=age if minimum_age is None else min(age,minimum_age)
  spine=z.imag==0 and z.real>=q-1
  child=[z+1,z+1j]if spine else[z+1j]
  bud=[p,p+1+1j]if spine else[p,p+1,p+1+1j]
  outputs=[2*v for v in child]+bud;assert len(set(outputs))==4
  for v in outputs:
   assert v not in board
   dist=max(abs(v.real-p.real),abs(v.imag-p.imag));assert dist<=2
   if birth is not None:assert 5*dist<=2*(tick-birth)
   rd=max(abs(v.real-2*root),abs(v.imag));assert 5*rd<=10+2*tick
   maxrootdist=max(maxrootdist,rd);board[v]=(tick,root)
  for v in child:heappush(queue,(serial,v,tick,root,depth+1));serial+=1
  depths[depth]+=1
  assert len(queue)>=q and len(board)==q+3*(tick+1)
  assert maxrootdist<=2*isqrt(2*(tick+1))+2
  assert maxrootdist<=(2*(tick+1)+13)//3
  if queue[0][-1]>depth:assert depths[depth]==q+depth
 runs.append({'roots':q,'updates':limit,'current_identities':len(board),'minimum_consumed_produced_age':minimum_age,'maximum_root_distance':int(maxrootdist)})
out={'status':'PASS independent abstract FIFO/identity/packing controls','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runs':runs,'scope':'Not an ant, Tait star, literal DCUV mask, actual C clock or full role-potential model. The all-time construction demonstrates insufficiency only of the listed marginal mass/age/box/monotone-ancestry constraints.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
