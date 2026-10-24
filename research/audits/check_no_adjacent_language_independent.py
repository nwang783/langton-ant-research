#!/usr/bin/env python3
"""Independent no-adjacent-defect coverage: current-color enumeration and DAG contraction.
No source enumeration, SCC, quotient, or macro geometry helpers are imported.
"""
from pathlib import Path
from collections import deque,Counter
import json,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'continuation_2026-10-22/ant_continuation/factor_language';start=time.time()
input_path=R/'computability/singleton_first_block_input.json'
assert hashlib.sha256(input_path.read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
W=json.loads(input_path.read_text())['word']
assert len(W)==104 and set(W)=={'R','L'}
F={int(''.join('1'if c=='R'else'0'for c in (W+W)[i:i+10]),2)for i in range(104)};assert len(F)==84
N=150;side=2*N+1;colors=bytearray([2])*(side*side);origin=N*side+N;step=(side,1,-side,-1)
words=[];levels=[0]*(N+1);digest=hashlib.sha256()
def dfs(depth,p,h,bits,previous_bad):
 levels[depth]+=1
 if depth==N:
  words.append(bits);digest.update((format(bits,'0150b').replace('0','L').replace('1','R')+'\n').encode());return
 old=colors[p]
 for black in (1,0):
  if old!=2 and old!=black:continue
  nb=(bits<<1)+(1-black);bad=depth>=9 and (nb&1023)not in F
  if bad and previous_bad:continue
  colors[p]=1-black;nh=(h+(3 if black else 1))%4
  dfs(depth+1,p+step[nh],nh,nb,bad)
 colors[p]=old
dfs(0,origin,0,0,False)
assert len(words)==304468 and sum(levels)==6866831
source_digest=hashlib.sha256((P/'no_pair_words150.txt').read_bytes()).hexdigest();assert digest.hexdigest()==source_digest
print('complete enumeration',sum(levels),len(words),digest.hexdigest(),round(time.time()-start,2),flush=True)
mask=(1<<149)-1;vertices={w>>1 for w in words}|{w&mask for w in words};assert len(vertices)==270902
H={int(line.split()[0].replace('L','0').replace('R','1'),2)for line in(P/'no_pair_large_scc.txt').read_text().splitlines()};assert len(H)==34712 and H<=vertices
T='RRRLLRLLRRRRLLRRRRLLRLLR'
def cycle_vertices(w):
 long=w*((149+len(w)-1)//len(w)+1)
 return{int(long[i:i+149].replace('L','0').replace('R','1'),2)for i in range(len(w))}
CW=cycle_vertices(W);CT=cycle_vertices(T);assert len(CW)==104 and len(CT)==24
assert CW<=vertices and CT<=vertices and not(H&CW or H&CT or CW&CT)
# Contract three proposed recurrent groups. Acyclicity of this FULL quotient
# proves coverage without trusting the original SCC algorithm or partition.
index={v:0 for v in H};index.update({v:1 for v in CW});index.update({v:2 for v in CT})
for v in vertices-index.keys():index[v]=len(index)-len(H)-len(CW)-len(CT)+3
n=max(index.values())+1;adj=[[]for _ in range(n)];degree=[0]*n;innerH={v:[]for v in H};innerW={v:[]for v in CW};innerT={v:[]for v in CT}
for w in words:
 a,b=w>>1,w&mask;i,j=index[a],index[b]
 if i==j and i<3:
  target=(innerH,innerW,innerT)[i];target[a].append(('R'if w&1 else'L',b))
 else:adj[i].append(j);degree[j]+=1
queue=deque(i for i,d in enumerate(degree)if d==0);processed=0
while queue:
 a=queue.popleft();processed+=1
 for b in adj[a]:
  degree[b]-=1
  if degree[b]==0:queue.append(b)
assert processed==n
assert all(len(v)==1 for v in innerW.values())and all(len(v)==1 for v in innerT.values())
# Check that the claimed cycles have exactly their literal expected successors.
for word,group in ((W,innerW),(T,innerT)):
 long=word*((150+len(word)-1)//len(word)+1)
 for i in range(len(word)):
  a=int(long[i:i+149].replace('L','0').replace('R','1'),2);b=int(long[i+1:i+150].replace('L','0').replace('R','1'),2)
  assert group[a]==[(long[i+149],b)]
assert all(innerH.values()) and sum(map(len,innerH.values()))==36277
M='LLLLRLRRRRLR';mb=int(M.replace('L','0').replace('R','1'),2);ports={v for v in H if v&4095==mb};assert len(ports)==995
# Verify the proposed H group independently in both graph directions.
reverseH={v:[] for v in H}
for a in H:
 for _,b in innerH[a]:reverseH[b].append(a)
for backward in (False,True):
 reached={next(iter(ports))};front=list(reached)
 while front:
  a=front.pop()
  for b in (reverseH[a] if backward else [b for _,b in innerH[a]]):
   if b not in reached:reached.add(b);front.append(b)
 assert reached==H
non=H-ports;deg={v:0 for v in non}
for a in non:
 for _,b in innerH[a]:
  if b in non:deg[b]+=1
queue=deque(a for a,d in deg.items()if d==0);seen=0;non_order=[]
while queue:
 a=queue.popleft();seen+=1;non_order.append(a)
 for _,b in innerH[a]:
  if b in non:
   deg[b]-=1
   if deg[b]==0:queue.append(b)
assert seen==len(non)
non_distance={}
for a in reversed(non_order):non_distance[a]=1+max(non_distance.get(b,0) for _,b in innerH[a])
assert max(non_distance.values())==73
returns=[]
for root in ports:
 stack=[(v,c)for c,v in innerH[root]]
 while stack:
  v,s=stack.pop()
  if v in ports:returns.append(s)
  else:stack.extend((b,s+c)for c,b in innerH[v])
assert len(returns)==2747
unique=set(returns);assert sorted(map(len,unique))==[15,18,28,64,74] and all(w.endswith(M)for w in unique)
canonical=json.loads((P/'five_macro_footprints.json').read_text());before={M+w[:-12]for w in unique};assert before=={d['word']for d in canonical.values()}
# Independent all-epoch first-L obstruction for the24-cycle, from literal traces.
p=0j;o=1;trace=[]
for i,c in enumerate(T):trace.append((p,i,c));o*=(-1j if c=='R'else 1j);p+=1j*o
assert p==2 and o==1
rays=[]
for phase in (7,22):
 q,_,c=trace[phase];assert c=='L'
 incidents=[]
 for a,i,c in trace:
  d=(q-a)/2
  if d.imag==0 and d.real==int(d.real):incidents.append((int(d.real)*24+i,i,c))
 # At q+n*2, this list gives all epoch-relative read times.
 assert min(incidents)==(phase,phase,'L')
 rays.append([int(q.real),int(q.imag),phase])
assert rays[0][1]!=rays[1][1]
out={'status':'Independent no-adjacent-bad-window reduction passed','enumeration_nodes':sum(levels),'words150':len(words),'word_file_sha256':digest.hexdigest(),'vertices':len(vertices),'contracted_DAG_vertices':n,'recurrent_groups':{'H':[len(H),sum(map(len,innerH.values()))],'W104':[len(CW),len(CW)],'T24':[len(CT),len(CT)]},'actual_marker_ports':len(ports),'H_strong_connectivity_verified':True,'longest_nonport_distance_to_a_port':max(non_distance.values()),'return_paths':len(returns),'return_word_counts_by_length':dict(Counter(map(len,returns))),'before_marker_words':sorted(before,key=len),'T24_initial_black_rays':rays,'seconds':time.time()-start,'scope':'Every infinite physically feasible no-adjacent-defect tail eventually follows W104,T24,or a before-marker C/V/U/Q/B concatenation. T24 needs infinite black support; independently proved packet fuel excludes the five-macro case.'}
Path(__file__).with_name('no_adjacent_language_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
