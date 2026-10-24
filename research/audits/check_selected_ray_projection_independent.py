#!/usr/bin/env python3
"""Independent Cartier affine pullback and bounded parity projection control."""
from pathlib import Path
import sys,json,hashlib
from collections import deque
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'computability/finite_power_exact_validator'))
# The already independently audited exact rational extractor is the sole imported
# mathematical dependency. No author Cartier, carry, relation or projection code.
from ray_parity_extractor import extract_rationals

def xorprod(P,H):
 out=set()
 for a in P:
  for b in H:
   z=tuple(x+y for x,y in zip(a,b))
   if z in out:out.remove(z)
   else:out.add(z)
 return frozenset(out)
def section(P,H,bits):
 return frozenset(tuple(z//2 for z in e) for e in xorprod(P,H) if tuple(z%2 for z in e)==bits)
def finish(P,H,c):
 if min(c)<0:return 0
 while any(c):
  P=section(P,H,tuple(z%2 for z in c));c=tuple(z//2 for z in c)
 return int((0,0,0) in P)
def affine(P,H,coef,constant):
 states=[(P,constant)];ids={states[0]:0};rows=[];output=[]
 for P,c in states:
  output.append(finish(P,H,c));row=[]
  for b in (0,1):
   z=tuple(v+b*a for v,a in zip(c,coef));n=(section(P,H,tuple(v%2 for v in z)),tuple(v//2 for v in z))
   if n not in ids:ids[n]=len(states);states.append(n)
   row.append(ids[n])
  rows.append(row)
 return rows,output

def build():
 shift,rat=extract_rationals(['RLLLLRRRR','LRRRRLLLL']*4);assert shift==(1,1)
 terms=[]
 for s,c in ((0,(1,2,2)),(3,(0,0,1))):
  p,h=rat[s][2:];terms.append(affine(frozenset(p.monoms()),frozenset(h.monoms()),(2,3,3),c))
 states=[(0,0)];ids={states[0]:0};tr=[];out=[]
 for a,b in states:
  out.append(terms[0][1][a]^terms[1][1][b]);row=[]
  for bit in (0,1):
   x=(terms[0][0][a][bit],terms[1][0][b][bit])
   if x not in ids:ids[x]=len(states);states.append(x)
   row.append(ids[x])
  tr.append(row)
 # Hidden k is summed over precisely 0<=k<a. Read LSB-first and track the
 # subtraction a-k-1; initial borrow one and final borrow zero encode this.
 initial=frozenset({(0,1)});masks=[initial];mi={initial:0};proj=[];po=[]
 for mask in masks:
  po.append(sum(out[q] for q,borrow in mask if borrow==0)%2);row=[]
  for abit in (0,1):
   dest=set()
   for q,borrow in mask:
    for kbit in (0,1):
     st=(tr[q][kbit],int(abit-kbit-borrow<0))
     if st in dest:dest.remove(st)
     else:dest.add(st)
   dest=frozenset(dest)
   if dest not in mi:mi[dest]=len(masks);masks.append(dest)
   row.append(mi[dest])
  proj.append(row)
 J=json.loads((ROOT/'computability/finite_power_exact_validator/automatic_selected_ray_control.json').read_text());A=J['forced_relation'];seen={(0,A['start'])};todo=list(seen)
 for u,v in todo:
  assert po[u]==int(v in A['accepting'])
  for b in (0,1):
   pair=proj[u][b],A['transitions'][v][b]
   if pair not in seen:seen.add(pair);todo.append(pair)
 # Canonical accepted inputs 00...001 represent4^j in LSB-first order.
 st=A['start'];seen0=set()
 while st not in seen0:
  seen0.add(st);assert A['transitions'][st][1] in A['accepting']
  st=A['transitions'][A['transitions'][st][0]][0]
 # Completely separate literal read-order controls of the selected leaf.
 images=['RLLLLRRRR','LRRRRLLLL']*4;dirs=(1j,1,-1j,-1);typed=[]
 for state,w in enumerate(images):
  h=state//2;row=[]
  for letter in w:
   row.append(2*h+(letter=='L'));h=(h+(1 if letter=='R' else -1))%4
  typed.append(row)
 literal=[]
 for exponent in range(4):
  depth=2*exponent;word=[0]
  for _ in range(depth):word=[t for state in word for t in typed[state]]
  index=sum(9**j for j in range(depth));position=0j;odd=set();heading=0
  for state in word[:index]:
   assert state//2==heading
   if position in odd:odd.remove(position)
   else:odd.add(position)
   heading=(heading+(1 if state%2==0 else -1))%4;position+=dirs[heading]
  assert position==complex(exponent,exponent) and word[index]==0
  q=A['start']
  for bit in bin(exponent)[2:][::-1] if exponent else []:q=A['transitions'][q][int(bit)]
  assert (position in odd)==(q in A['accepting'])
  literal.append({'a':exponent,'depth':depth,'leaf_index':index,'prior_black_parity':position in odd})
 result={'status':'PASS independent exact all-input automaton equivalence',
 'affine_machine_states':[len(t[0]) for t in terms],'xor_states':len(tr),
 'parity_vector_states':len(proj),'equivalence_pairs':len(seen),'literal_selected_occurrences':literal,
 'infinite_required_black_subfamily':'a=4^j, j>=0; physical cells(a,a)',
 'scope':'Critical selected-occurrence mechanism only. Known excluded unit-nine control, no full occurrence-cover compiler or new class exclusion.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':build()
