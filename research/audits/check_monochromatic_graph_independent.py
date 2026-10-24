"""Independent current-color enumeration, full DAG cover, and exact ports."""
from pathlib import Path
from collections import deque,Counter
import json,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';OLD=R/'continuation_2026-10-22/ant_continuation/factor_language';start=time.time()
assert hashlib.sha256((R/'computability/singleton_first_block_input.json').read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
assert hashlib.sha256((OLD/'no_pair_words150.txt').read_bytes()).hexdigest()=='28c950002dd8c7bcaddee65da9fcb2291f7166196aea80f4fab6b3db7374ba27'
assert hashlib.sha256((P/'single_k_rrrllrllrlr_port_quotient.json').read_bytes()).hexdigest()=='c993b17a633f00220b28ab6875aa9eb09b49180438671103480bd84509c90755'
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];assert len(W)==104
bits=lambda w:int(w.replace('L','0').replace('R','1'),2)
F={bits((W+W)[i:i+10]) for i in range(104)};assert len(F)==84
pattern=bits('RRRLLRLLRLR');N=150;side=301;colors=bytearray([2])*(side*side);origin=N*side+N;step=(side,1,-side,-1);words=[];levels=[0]*151;digest=hashlib.sha256()
def dfs(t,p,h,b,prev):
 levels[t]+=1
 if t==150:
  words.append(b);digest.update((format(b,'0150b').replace('0','L').replace('1','R')+'\n').encode());return
 old=colors[p]
 for black in (1,0):
  if old!=2 and old!=black:continue
  nb=(b<<1)+(1-black);bad=t>=9 and (nb&1023) not in F
  if bad and prev and (nb&2047)!=pattern:continue
  colors[p]=1-black;nh=(h+(3 if black else 1))%4;dfs(t+1,p+step[nh],nh,nb,bad)
 colors[p]=old
dfs(0,origin,0,0,False)
assert len(words)==863913 and sum(levels)==17560058
source=P/'single_k_rrrllrllrlr_words150.txt';assert digest.hexdigest()==hashlib.sha256(source.read_bytes()).hexdigest()
print('complete enumeration',sum(levels),len(words),digest.hexdigest(),time.time()-start,flush=True)
mask=(1<<149)-1;V={w>>1 for w in words}|{w&mask for w in words};assert len(V)==766480
H={bits(s.split()[0]) for s in (OLD/'no_pair_large_scc.txt').read_text().splitlines()}
Bedge={bits(s) for s in (P/'single_k_rrrllrllrlr_bad_component.txt').read_text().splitlines()};B={w>>1 for w in Bedge}|{w&mask for w in Bedge}
assert len(H)==34712 and len(B)==23759 and not H&B and H|B<=V
index={v:0 for v in H};index.update({v:1 for v in B});nextid=2
for v in V-index.keys():index[v]=nextid;nextid+=1
adj=[[] for _ in range(nextid)];degree=[0]*nextid;innerH={v:[] for v in H};innerB={v:[] for v in B};Hwords=set()
for w in words:
 a,b=w>>1,w&mask;i,j=index[a],index[b]
 if i==j and i<2:
  (innerH if i==0 else innerB)[a].append(('R' if w&1 else 'L',b))
  if i==0:Hwords.add(w)
 else:adj[i].append(j);degree[j]+=1
q=deque(i for i,n in enumerate(degree) if n==0);seen=0
while q:
 a=q.popleft();seen+=1
 for b in adj[a]:
  degree[b]-=1
  if not degree[b]:q.append(b)
assert seen==nextid
oldH=set()
for line in (OLD/'no_pair_words150.txt').read_text().splitlines():
 b=bits(line)
 if b>>1 in H and b&mask in H:oldH.add(b)
assert Hwords==oldH and len(Hwords)==36277 and sum(map(len,innerB.values()))==24691
assert {((a<<1)+(c=='R')) for a in innerB for c,b in innerB[a]}==Bedge
M='LLLLRLRRRRLR';Nmark='RRRLLRLLRRRR';Pmark='RRRRLLRLLRLR';badmark='L'+'RRRLLRLLRLR';markers={bits(w):w for w in (M,Nmark,Pmark,badmark)}
ports={v for v in B if v&4095 in markers};assert len(ports)==1082 and all(markers[v&4095]!=badmark for v in ports)
non=B-ports;degree={v:0 for v in non}
for a in non:
 for c,b in innerB[a]:
  if b in non:degree[b]+=1
q=deque(a for a,n in degree.items() if not n);order=[]
while q:
 a=q.popleft();order.append(a)
 for c,b in innerB[a]:
  if b in non:
   degree[b]-=1
   if not degree[b]:q.append(b)
assert len(order)==len(non)
height={}
for a in reversed(order):height[a]=1+max(height.get(b,0) for c,b in innerB[a])
assert max(height.values())==44
# Every infinite B path therefore has infinitely many ports; no finite cutoff.
Q=json.loads((P/'single_k_rrrllrllrlr_port_quotient.json').read_text());mac=Q['macro_words'];label={(z['start_marker'],z['word'],z['end_marker']):i for i,z in enumerate(mac)}
assert len(label)==11
returns=[]
for a in sorted(ports):
 stack=[(b,c) for c,b in innerB[a]]
 while stack:
  b,s=stack.pop()
  if b in ports:
   am=markers[a&4095];bm=markers[b&4095];joined=am+s;assert joined.endswith(bm)
   raw=joined[:-12];k=label[am,raw,bm];returns.append((a,k,b))
  else:stack.extend((v,s+c) for c,v in innerB[b])
assert len(returns)==2510
actual=json.loads((P/'single_k_rrrllrllrlr_actual_ports.json').read_text());history=list(map(bits,actual['port_histories']));assert len(history)==1082 and set(history)==ports
claimed=[(history[a],k,history[b]) for a,k,b in actual['edges']];assert Counter(returns)==Counter(claimed)
classes=actual['classes'];assert len(classes)==1082 and set(classes)==set(range(6));cmap=dict(zip(history,classes));allowed=set(map(tuple,Q['quotient_edges']));assert len(allowed)==12
assert {(cmap[a],k,cmap[b]) for a,k,b in returns}==allowed
# Rebind the standalone certificate's literal graph and charged-fuel proof.
standalone=json.loads((R/'audits/check_monochromatic_context_independent.json').read_text());assert standalone['status']=='independent context certificate verified'
assert standalone['certificate_sha256']==hashlib.sha256((P/'single_k_rrrllrllrlr_context2_kernel.tsv').read_bytes()).hexdigest()
out={'status':'complete independent monochromatic-defect coverage verified','nodes':sum(levels),'words150':len(words),'histories149':len(V),'contracted_DAG_vertices':nextid,'old_H_vertices':len(H),'old_H_edges':len(Hwords),'new_component_vertices':len(B),'new_component_edges':sum(map(len,innerB.values())),'ports':len(ports),'nonport_height':max(height.values()),'returns':len(returns),'literal_macros':len(label),'quotient_states':6,'quotient_edges':12,'source_word_sha256':digest.hexdigest(),'seconds':time.time()-start,'theorem':'For finite initial black sets, if eventually every adjacent forbidden-ten pair has the specific eleven-word RRRLLRLLRLR, then the orbit captures standard104. The universal finiteness claim is still open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
