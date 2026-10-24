"""Current-color first-return exhaustion and full four-history DAG cover."""
from pathlib import Path
from collections import deque
import json,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';stem='direct_mono_lrrlrrrrlrr';start=time.time()
manifest=json.loads((P/'extended_star_packet_manifest.json').read_text());assert all(hashlib.sha256((P/f).read_bytes()).hexdigest()==h for f,h in manifest.items())
assert hashlib.sha256((R/'computability/singleton_first_block_input.json').read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
S={'LRRLRRRRLRR'}
marks={'LLLLRLRRRRLR','RRRLLRLLRRRR'}|{c+p for c in 'LR' for p in S}
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];F={(W+W)[i:i+10] for i in range(104)};assert len(F)==84
D=((0,1),(1,0),(0,-1),(-1,0));board={};nodes=0;maximum=0;returns=set();initial_hits=0
# Current color: absent means an unconstrained initial lamp, not white.
def tree(w,p,h,previous,startmark=None):
 global nodes,maximum,initial_hits
 nodes+=1;maximum=max(maximum,len(w));old=board.get(p)
 for black,c in [(True,'L'),(False,'R')]:
  if old is not None and old!=black:continue
  nw=w+c;bad=len(nw)>=10 and nw[-10:] not in F
  if bad and previous and nw[-11:] not in S:continue
  board[p]=not black;nh=(h+(3 if black else 1))%4;np=(p[0]+D[nh][0],p[1]+D[nh][1])
  if len(nw)>=12 and nw[-12:] in marks:
   if startmark is None:initial_hits+=1
   else:returns.add((startmark,nw[-12:],nw[:-12]))
  else:tree(nw,np,nh,bad,startmark)
  if old is None:board.pop(p,None)
  else:board[p]=old

tree('',(0,0),0,False);initial_nodes=nodes;initial_max=maximum;assert initial_nodes==18453 and initial_max==90
for marker in sorted(marks):
 board.clear();p=(0,0);h=0;prev=False;legal=True;w=''
 for c in marker:
  black=c=='L';old=board.get(p);w+=c;bad=len(w)>=10 and w[-10:] not in F
  if (old is not None and old!=black) or (bad and prev and w[-11:] not in S):legal=False;break
  board[p]=not black;h=(h+(3 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);prev=bad
 if legal:tree(marker,p,h,prev,marker)
assert nodes==19006 and maximum==91 and len(returns)==23
assert returns=={tuple(s.split()) for s in (P/(stem+'.returns.tsv')).read_text().splitlines()}
for a,b,w in returns:assert w and (w+b).startswith(a)
mac=sorted(returns,key=lambda z:(len(z[2]),z[2],z[0],z[1]));succ={i:[j for j in range(23) if mac[i][1]==mac[j][0]] for i in range(23)}
def feasible(w):
 p=(0,0);h=0;colors={}
 for c in w:
  black=c=='L'
  if p in colors and colors[p]!=black:return False
  colors[p]=not black;h=(h+(3 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return True

hist=set();tested=0
# Every appended raw+endpoint marker starts its required start marker.
# Therefore each interim raw+marker is a literal prefix of every extension.
# Rejecting an infeasible interim prefix is exact, not a heuristic.
def six(ids,body):
 global tested
 tested+=1
 if ids and not feasible(body+mac[ids[-1]][1]):return
 if len(ids)==6:hist.add(tuple(ids));return
 for a in (range(len(mac)) if not ids else succ[ids[-1]]):six(ids+[a],body+mac[a][2])
six([],'');assert len(hist)==13042
claimed=json.loads((P/(stem+'_history6_words.json')).read_text());assert set(map(tuple,claimed['words']))==hist
assert [(z['start_marker'],z['end_marker'],z['word']) for z in claimed['macro_words']]==mac
V={w[:-1] for w in hist}|{w[1:] for w in hist};assert len(V)==4019
groups=[];labels=[];counts=[];large=None
for i in range(3):
 j=json.loads((P/(stem+f'_history6_scc{i}_port_quotient.json')).read_text());hs=list(map(tuple,j['history_states']));g=set(hs);assert len(g)==len(hs) and g<=V and all(not g&x for x in groups);groups.append(g)
 es={w for w in hist if w[:-1] in g and w[1:] in g};counts.append(len(es));local=j['source_return_ids'];assert [(z['start_marker'],z['end_marker'],z['word']) for z in j['macro_words']]==[mac[a] for a in local]
 hi={s:k for k,s in enumerate(hs)};li={a:k for k,a in enumerate(local)}
 he={(hi[w[:-1]],li[w[-1]],hi[w[1:]]) for w in es};assert he==set(map(tuple,j['history_edges']))
 cl=j['history_state_classes'];qe={(cl[a],b,cl[c]) for a,b,c in he};assert qe==set(map(tuple,j['quotient_edges'])) and set(cl)==set(range(j['classes']))
 allk=set()
 for a in {w[-1] for w in es}:
  word=mac[a][2]+mac[a][1]
  for n in range(11,len(word)+1):
   f=word[n-11:n]
   if f[:10] not in F and f[1:] not in F:allk.add(f)
 if i<2:assert not allk
 else:assert allk==S;large=j
 labels.append(sorted(allk))
assert list(map(len,groups))==[2,3,945] and counts[2]==2987
idx={v:i for i,g in enumerate(groups) for v in g};n=3
for v in V-idx.keys():idx[v]=n;n+=1
adj=[[] for _ in range(n)];deg=[0]*n
for w in hist:
 a,b=idx[w[:-1]],idx[w[1:]]
 if a==b and a<3:continue
 adj[a].append(b);deg[b]+=1
q=deque(i for i,z in enumerate(deg) if not z);seen=0
while q:
 a=q.popleft();seen+=1
 for b in adj[a]:
  deg[b]-=1
  if not deg[b]:q.append(b)
assert seen==n
# Derive every return to M in the overapproximating 78-state quotient.
raw=large['macro_words'];edges=set(map(tuple,large['quotient_edges']));assert large['classes']==78
begin={v:{raw[a]['start_marker'] for u,a,w in edges if u==v} for v in range(78)}
assert all(len(x)==1 for x in begin.values());begin={v:next(iter(x)) for v,x in begin.items()}
assert all(raw[a]['end_marker']==begin[w] for u,a,w in edges)
M='LLLLRLRRRRLR';Pm='RLRRLRRRRLRR';Fword='RLRRLRRRRLRRRR';ports={v for v in begin if begin[v]==M};assert len(ports)==65
outgoing={v:[(a,w) for u,a,w in edges if u==v] for v in range(78)}
assert all(begin[v]==Pm and all(raw[a]['word']==Fword and w in ports for a,w in outgoing[v]) for v in set(begin)-ports)
returns2=set()
for v in ports:
 for a,w in outgoing[v]:
  if w in ports:returns2.add((v,raw[a]['word'],w))
  else:
   assert raw[a]['word'] in {'LLLLRLRRR','LLLLRLRRRRLRLLLLRRR'}
   for b,z in outgoing[w]:returns2.add((v,raw[a]['word']+raw[b]['word'],z))
pkt=json.loads((P/(stem+'_packets_port_quotient.json')).read_text());assert set(pkt['source_port_states'])==ports
ren=dict(zip(pkt['source_port_states'],pkt['source_state_classes']));assert set(ren.values())==set(range(65))
pwords=[z['word'] for z in pkt['macro_words']];assert len(pwords)==len(set(pwords))==7
assert all(z['start_marker']==z['end_marker']==M for z in pkt['macro_words'])
projected={(ren[v],pwords.index(w),ren[z]) for v,w,z in returns2};assert projected==set(map(tuple,pkt['quotient_edges'])) and len(projected)==224
cert=json.loads((R/'audits/check_extended_star_context_independent.json').read_text());assert cert['status']=='independent extended-star seven-packet context certificate verified'
out={'status':'independent complete extended-star singleton capture proof verified','label':'LRRLRRRRLRR','initial_nodes':initial_nodes,'total_nodes':nodes,'max_unmarked_depth':maximum,'raw_returns':len(mac),'prefix_tree_nodes_for_six_histories':tested,'feasible_six_histories':len(hist),'history_vertices':len(V),'component_sizes':list(map(len,groups)),'component_edges':counts,'component_K_labels':labels,'full_contracted_DAG_vertices':n,'large_quotient_states':78,'M_ports':65,'contracted_packet_edges':224,'packet_count':7,'kernel_forbidden_pairs':cert['forbidden_types'],'seconds':time.time()-start,'manifest_sha256':hashlib.sha256((P/'extended_star_packet_manifest.json').read_bytes()).hexdigest(),'scope':'Eventual sole K label LRRLRRRRLRR implies standard capture. No arbitrary mixtures or universal residual-event finiteness follow from this singleton theorem.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
