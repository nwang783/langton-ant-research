"""Independent current-color enumeration, full cyclic cover, old-H inclusion, ports."""
from pathlib import Path
from collections import deque,Counter
import json,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';OLD=R/'continuation_2026-10-22/ant_continuation/factor_language';start=time.time();stem='mono_rrrlrrrrlrr_'
assert hashlib.sha256((OLD/'no_pair_words150.txt').read_bytes()).hexdigest()=='28c950002dd8c7bcaddee65da9fcb2291f7166196aea80f4fab6b3db7374ba27'
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];assert hashlib.sha256((R/'computability/singleton_first_block_input.json').read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
bits=lambda w:int(w.replace('L','0').replace('R','1'),2)
F={bits((W+W)[i:i+10]) for i in range(104)};assert len(F)==84
pattern=bits('RRRLRRRRLRR');side=301;colors=bytearray([2])*(side*side);origin=150*side+150;step=(side,1,-side,-1);words=[];levels=[0]*151;digest=hashlib.sha256()
def dfs(t,p,h,b,prev):
 levels[t]+=1
 if t==150:words.append(b);digest.update((format(b,'0150b').replace('0','L').replace('1','R')+'\n').encode());return
 old=colors[p]
 for black in (1,0):
  if old!=2 and old!=black:continue
  nb=(b<<1)+(1-black);bad=t>=9 and (nb&1023) not in F
  if bad and prev and (nb&2047)!=pattern:continue
  colors[p]=1-black;nh=(h+(3 if black else 1))%4;dfs(t+1,p+step[nh],nh,nb,bad)
 colors[p]=old
dfs(0,origin,0,0,False)
assert len(words)==364858 and digest.hexdigest()==hashlib.sha256((P/(stem+'words150.txt')).read_bytes()).hexdigest();print('enumeration',sum(levels),len(words),time.time()-start,flush=True)
mask=(1<<149)-1;V={w>>1 for w in words}|{w&mask for w in words};assert len(V)==326637
Be={bits(s) for s in (P/(stem+'bad_component.txt')).read_text().splitlines()};B={w>>1 for w in Be}|{w&mask for w in Be};assert len(B)==42002 and len(Be)==43912
T='RRRLLRLLRRRRLLRRRRLLRLLR'
def cyc(w,n):return {bits((w*((n+len(w)-1)//len(w)+1))[i:i+n]) for i in range(len(w))}
WC,TC=cyc(W,149),cyc(T,149);assert len(WC)==104 and len(TC)==24 and not B&WC and not B&TC and not WC&TC and B|WC|TC<=V
index={v:0 for v in B};index.update({v:1 for v in WC});index.update({v:2 for v in TC});nextid=3
for v in V-index.keys():index[v]=nextid;nextid+=1
adj=[[] for _ in range(nextid)];degree=[0]*nextid;innerB={v:[] for v in B};internals=[set(),set(),set()]
for w in words:
 a,b=w>>1,w&mask;i,j=index[a],index[b]
 if i==j and i<3:
  internals[i].add(w)
  if i==0:innerB[a].append(('R' if w&1 else 'L',b))
 else:adj[i].append(j);degree[j]+=1
q=deque(i for i,n in enumerate(degree) if n==0);seen=0
while q:
 a=q.popleft();seen+=1
 for b in adj[a]:
  degree[b]-=1
  if not degree[b]:q.append(b)
assert seen==nextid and internals==[Be,cyc(W,150),cyc(T,150)]
oldH={bits(s.split()[0]) for s in (OLD/'no_pair_large_scc.txt').read_text().splitlines()};assert len(oldH)==34712 and oldH<=B
oldHe={bits(s) for s in (OLD/'no_pair_words150.txt').read_text().splitlines() if bits(s)>>1 in oldH and bits(s)&mask in oldH};assert len(oldHe)==36277 and oldHe<=Be
markers={bits(s):s for s in ['LLLLRLRRRRLR','RRRRLRRRRLRR']};ports={v for v in B if v&4095 in markers};assert len(ports)==1402
non=B-ports;deg={v:0 for v in non}
for a in non:
 for c,b in innerB[a]:
  if b in non:deg[b]+=1
q=deque(a for a,n in deg.items() if not n);order=[]
while q:
 a=q.popleft();order.append(a)
 for c,b in innerB[a]:
  if b in non:
   deg[b]-=1
   if not deg[b]:q.append(b)
assert len(order)==len(non);height={}
for a in reversed(order):height[a]=1+max(height.get(b,0) for c,b in innerB[a])
assert max(height.values())==73
Q=json.loads((P/(stem+'port_quotient.json')).read_text());label={(z['start_marker'],z['word'],z['end_marker']):i for i,z in enumerate(Q['macro_words'])};assert len(label)==7
returns=[]
for a in sorted(ports):
 stack=[(b,c) for c,b in innerB[a]]
 while stack:
  b,s=stack.pop()
  if b in ports:
   am,bm=markers[a&4095],markers[b&4095];joined=am+s;assert joined.endswith(bm);k=label[am,joined[:-12],bm];returns.append((a,k,b))
  else:stack.extend((v,s+c) for c,v in innerB[b])
assert len(returns)==3657
actual=json.loads((P/(stem+'actual_ports.json')).read_text());hist=list(map(bits,actual['port_histories']));assert len(hist)==1402 and set(hist)==ports
assert Counter(returns)==Counter((hist[a],k,hist[b]) for a,k,b in actual['edges'])
classes=actual['classes'];assert len(classes)==1402 and set(classes)==set(range(52));cmap=dict(zip(hist,classes));allowed=set(map(tuple,Q['quotient_edges']));assert len(allowed)==113 and {(cmap[a],k,cmap[b]) for a,k,b in returns}==allowed
oldports={v for v in oldH if v&4095 in markers};assert all(markers[v&4095]=='LLLLRLRRRRLR' for v in oldports)
standalone=json.loads((R/'audits/check_seven_monochromatic_context_independent.json').read_text());assert standalone['status']=='independent seven-word context certificate verified' and standalone['certificate_sha256']==hashlib.sha256((P/(stem+'context2_kernel.tsv')).read_bytes()).hexdigest() and standalone['quotient_sha256']==hashlib.sha256((P/(stem+'port_quotient.json')).read_bytes()).hexdigest()
out={'status':'complete independent seven-word monochromatic coverage verified, including old H embedding','nodes':sum(levels),'words150':len(words),'histories149':len(V),'contracted_DAG_vertices':nextid,'component_vertices':len(B),'component_edges':len(Be),'old_H_vertices':len(oldH),'old_H_edges':len(oldHe),'old_H_marker_ports':len(oldports),'ports':len(ports),'nonport_height':max(height.values()),'returns':len(returns),'literal_macros':7,'quotient_states':52,'quotient_edges':113,'source_word_sha256':digest.hexdigest(),'seconds':time.time()-start,'theorem':'For finite seeds, eventual adjacent forbidden-ten pairs all labeled RRRLRRRRLRR imply standard capture. Actual old-H factors inherit the linear contextual fuel bound; arbitrary raw-five factors do not. Universal K finiteness remains open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
