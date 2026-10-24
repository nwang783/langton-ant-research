"""Separate complex-coordinate literal genealogy extraction; finite controls
supplement the inherited all-n adjacent-circuit overlap proof."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
H=(ROOT/'word_stabilization/standard_word.txt').read_text().strip();F={(H*2)[i:i+10]for i in range(104)}
SIX={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
offset={1j:-1j,1:-1-1j,-1j:-1,-1:0j}
labels=set();counts=0
for n in list(range(2,35))+[50,77,100]:
 w=''.join('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L' for j in range(n,0,-1))
 reads=[];p=0j;h=1j;last={};seed=set()
 for t,c in enumerate(w):
  reads.append((p,h,c))
  if p in last:assert last[p]!=c
  elif c=='L':seed.add(p)
  last[p]=c;h*=(-1j if c=='R'else 1j);p+=h
 assert len(seed)==11*n+2
 owner={q:('root',q)for q in seed};birth={q:None for q in seed};node=0
 parents={0:None};children=defaultdict(list);starts={0:0};nodeat={};outs=defaultdict(list);marks=defaultdict(list);ages={}
 for t,(p,h,c)in enumerate(reads):
  nodeat[t]=node
  if t>=10:
   label=w[t-10:t+1]
   if label[:10]not in F and label[1:]not in F and label not in SIX:marks[node].append(label)
  if c=='R':
   assert p not in owner;owner[p]=node;birth[p]=t;outs[node].append(p)
  else:
   parent=owner.pop(p);bt=birth.pop(p)
   if bt is not None:ages[p]=t-bt
   node+=1;parents[node]=parent;children[parent].append(node);starts[node]=t+1
 root=('root',complex(-2*n-3,2*n-1));P=[];Q=[]
 for k in range(n):
  j=n-k;t=k*(16*n+6)-8*k*(k-1);tau=t+8*j+7;u=nodeat[tau]
  assert starts[u]==tau;P.append(u);v=complex(-2*n-3+k,2*n-2-k)
  p,h,c=reads[tau];assert p==v+1+1j and h==1 and p+offset[h]==v
  assert outs[u]==([v+1+1j,v+1]if j>=2 else[v+1+1j])
  assert len(marks[u])==(3 if j>=2 else 2);labels.update(marks[u])
  if k==0:assert parents[u]==root
  else:
   q=nodeat[tau-1];Q.append(q);assert starts[q]==tau-1 and parents[q]==parents[u]==P[-2]
   assert outs[q]==[] and len(marks[q])==1;labels.update(marks[q])
   p,h,c=reads[tau-1];assert p+offset[h]==v-1+1j
  if j>=2:
   assert ages[v+1+1j]==ages[v+1]==16*j-4
 active=set();todo=list(children[root])
 while todo:
  u=todo.pop();assert u not in active;active.add(u);todo.extend(children[u])
 assert active==set(P+Q) and sum(len(marks[u])for u in active)==4*n-2
 assert sum(max(0,len(children[u])-1)for u in active)==n-1
 assert sum(bool(children[u])for u in active)==n-1
 counts+=len(w)
assert labels=={'RLLRRLLRLLR','LLRRLLRLLRR','LRRLLRLLRRL','LLRRLLRLLRL','RRLLRRLLRLL','LRLLRRLLRLL'}
# All-n affine ages reduce symbolically to these exact coefficients.
# tau(k+1)-tau(k) = 16(n-k)-2; both births/consumptions differ by two.
for n,k in[(2,0),(100,50)]:
 tau=lambda i:i*(16*n+6)-8*i*(i-1)+8*(n-i)+7
 assert tau(k+1)-tau(k)-2==16*(n-k)-4
out={'status':'PASS independent literal token ownership and marked comb extraction','parameters':36,'literal_reads':counts,'fixed_residual_labels':sorted(labels),'scope':'All-n geometry follows from signed adjacent-circuit overlap and explicit affine timing. One-root component only; complete seed mass11n+2 grows. No fixed-mass or infinite-seed counterexample.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
