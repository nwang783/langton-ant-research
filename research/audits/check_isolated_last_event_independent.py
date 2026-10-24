#!/usr/bin/env python3
"""Independent current-color enumeration for the isolated last-defect obstruction."""
from pathlib import Path
from collections import defaultdict,deque
import json,hashlib,time
R=Path(__file__).resolve().parents[1];W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];start=time.time()
assert hashlib.sha256((R/'computability/singleton_first_block_input.json').read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
F={int((W+W)[i:i+10].replace('L','0').replace('R','1'),2)for i in range(104)};assert len(F)==84

def enumerate_words(length,one_event):
 side=2*length+1;colors=bytearray([2])*(side*side);origin=length*side+length;steps=(side,1,-side,-1);leaves=[];nodes=0
 def dfs(depth,p,h,bits):
  nonlocal nodes
  nodes+=1
  if depth==length:leaves.append(bits);return
  old=colors[p]
  for b in (1,0):
   if old!=2 and old!=b:continue
   nb=(bits<<1)+1-b
   if depth>=9:
    bad=(nb&1023)not in F
    if bad != (one_event and depth==10):continue
   colors[p]=1-b;nh=(h+(3 if b else 1))%4
   dfs(depth+1,p+steps[nh],nh,nb)
  colors[p]=old
 dfs(0,origin,0,0);return leaves,nodes
legal,nodes=enumerate_words(150,False);assert len(legal)==6605
mask=(1<<149)-1;vs={w>>1 for w in legal}|{w&mask for w in legal};assert len(vs)==6501
rev=defaultdict(list)
for w in legal:rev[w&mask].append(w>>1)
long=W*3;CW={int(long[i:i+149].replace('L','0').replace('R','1'),2)for i in range(104)};assert CW<=vs
reach=set(CW);q=deque(CW)
while q:
 a=q.popleft()
 for b in rev[a]:
  if b not in reach:reach.add(b);q.append(b)
assert len(reach)==925
isolated,othernodes=enumerate_words(160,True);assert len(isolated)==20
assert all((w&mask)not in reach for w in isolated)
def digest(words,n):return hashlib.sha256(''.join(format(w,'0'+str(n)+'b').replace('0','L').replace('1','R')+'\n'for w in sorted(words)).encode()).hexdigest()
assert digest(legal,150)=='6b76e51621e15d2304f1c0baa28790cc267cabafca3fc03250dea8721b2b4794'
assert digest(isolated,160)=='98a66c8fabfc29ff9e731430be3f6b7a4e56d6779d3eddb8b2da96ec573f0b58'
out={'status':'Independent isolated-last-event finite certificate passed','legal150_words':len(legal),'legal149_vertices':len(vs),'standard_reachable_vertices':len(reach),'isolated160_words':len(isolated),'survivors_reaching_standard':0,'enumeration_nodes':[nodes,othernodes],'legal_word_sha256':digest(legal,150),'isolated_word_sha256':digest(isolated,160),'seconds':time.time()-start,'scope':'No physical turn stream can have an isolated-on-left final J event and later standard104. Combined with the separately reviewed no-adjacent criterion, every finite-support J event has a K event at or after it.'}
Path(__file__).with_name('isolated_last_event_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
