#!/usr/bin/env python3
"""Finite abstract count-three cycle controls, not embedded front models."""
from itertools import product
from collections import Counter
from pathlib import Path
import json,sys
# Types R1,R2,L1,L2, with zero-based local visit ranks.
I=((0,1,2),(0,2,3),(1,2,3),(0,1,3))
O=((0,2,3),(0,1,2),(0,1,3),(1,2,3))
def feasible(word):
 n=len(word);s={};p={}
 for i,t in enumerate(word):
  nxt=(i+1)%n
  for a,b in zip(O[t],I[word[nxt]]):s[i*4+a]=nxt*4+b;p[nxt*4+b]=i*4+a
 chains=[];which={};pos={}
 for e in range(4*n):
  if e in p:continue
  c=[];v=e
  while v is not None:
   if v in which:return False
   which[v]=len(chains);pos[v]=len(c);c.append(v);v=s.get(v)
  chains.append(c)
 if len(which)!=4*n:return False
 adj=[set() for c in chains];indeg=[0]*len(chains)
 for i in range(n):
  for j in range(3):
   a=i*4+j;b=a+1;ca=which[a];cb=which[b]
   if ca==cb:
    if pos[a]>=pos[b]:return False
   elif cb not in adj[ca]:adj[ca].add(cb);indeg[cb]+=1
 todo=[c for c in range(len(chains)) if not indeg[c]];total=0
 while todo:
  a=todo.pop();total+=1
  for b in adj[a]:
   indeg[b]-=1
   if not indeg[b]:todo.append(b)
 return total==len(chains)
def run(n):
 counts=Counter();first={}
 # Rotate so first type is R1 or R2, covering all mixed words.
 for word in product(range(4),repeat=n):
  if word[0]>=2:continue
  if feasible(word):
   nr=sum(t<2 for t in word);counts[nr]+=1;first.setdefault(nr,word)
 result=dict(length=n,feasible_by_right_count=dict(counts),first_examples={k:list(v) for k,v in first.items()})
 Path(__file__).with_name(f'cap4_high_cycle_n{n}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run(int(sys.argv[1]))
