"""Current-color first-return exhaustion and full four-history DAG cover."""
from pathlib import Path
from collections import deque
import json,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';stem='direct_five_signed_labels';start=time.time()
manifest=json.loads((P/'five_label_union_manifest.json').read_text());assert all(hashlib.sha256((P/f).read_bytes()).hexdigest()==h for f,h in manifest.items())
assert hashlib.sha256((R/'computability/singleton_first_block_input.json').read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
S={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR'}
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

tree('',(0,0),0,False);initial_nodes=nodes;initial_max=maximum;assert initial_nodes==19290 and initial_max==90
for marker in sorted(marks):
 board.clear();p=(0,0);h=0;prev=False;legal=True;w=''
 for c in marker:
  black=c=='L';old=board.get(p);w+=c;bad=len(w)>=10 and w[-10:] not in F
  if (old is not None and old!=black) or (bad and prev and w[-11:] not in S):legal=False;break
  board[p]=not black;h=(h+(3 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);prev=bad
 if legal:tree(marker,p,h,prev,marker)
assert nodes==20679 and maximum==91 and len(returns)==69
assert returns=={tuple(s.split()) for s in (P/(stem+'.returns.tsv')).read_text().splitlines()}
for a,b,w in returns:assert w and (w+b).startswith(a)
mac=sorted(returns,key=lambda z:(len(z[2]),z[2],z[0],z[1]));succ={i:[j for j in range(69) if mac[i][1]==mac[j][0]] for i in range(69)}
def feasible(w):
 p=(0,0);h=0;colors={}
 for c in w:
  black=c=='L'
  if p in colors and colors[p]!=black:return False
  colors[p]=not black;h=(h+(3 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return True
hist=set();tested=0
def four(ids):
 global tested
 if len(ids)==4:
  tested+=1;w=''.join(mac[a][2] for a in ids)+mac[ids[-1]][1]
  if feasible(w):hist.add(tuple(ids))
 else:
  for a in (range(69) if not ids else succ[ids[-1]]):four(ids+[a])
four([]);assert len(hist)==3493
claimed=json.loads((P/(stem+'_history4_words.json')).read_text());assert set(map(tuple,claimed['words']))==hist
assert [(z['start_marker'],z['end_marker'],z['word']) for z in claimed['macro_words']]==mac
V={w[:-1] for w in hist}|{w[1:] for w in hist};assert len(V)==887
groups=[];labelsets=[];edgecounts=[]
for i,expected in enumerate(['RRRLLRLLRLR','RRRLRRRRLRR']):
 q=json.loads((P/(stem+f'_history4_scc{i}_port_quotient.json')).read_text());g=set(map(tuple,q['history_states']));assert g<=V;groups.append(g)
 edges={w for w in hist if w[:-1] in g and w[1:] in g};edgecounts.append(len(edges));labels={w[-1] for w in edges};allk=set()
 for a in labels:
  word=mac[a][2]+mac[a][1]
  for j in range(11,len(word)+1):
   factor=word[j-11:j]
   if factor[:10] not in F and factor[1:] not in F:allk.add(factor)
 assert allk=={expected};labelsets.append(sorted(allk))
assert list(map(len,groups))==[43,65] and edgecounts==[85,210] and not groups[0]&groups[1]
idx={v:i for i,g in enumerate(groups) for v in g};n=2
for v in V-idx.keys():idx[v]=n;n+=1
adj=[[] for _ in range(n)];deg=[0]*n
for w in hist:
 a,b=idx[w[:-1]],idx[w[1:]]
 if a==b and a<2:continue
 adj[a].append(b);deg[b]+=1
q=deque(i for i,z in enumerate(deg) if z==0);visited=0
while q:
 a=q.popleft();visited+=1
 for b in adj[a]:
  deg[b]-=1
  if not deg[b]:q.append(b)
assert visited==n==781
# These are global previously reviewed theorems, not raw-grammar inclusions.
assert json.loads((R/'audits/check_monochromatic_graph_independent.json').read_text())['status']=='complete independent monochromatic-defect coverage verified'
assert json.loads((R/'audits/check_seven_monochromatic_graph_independent.json').read_text())['status']=='complete independent seven-word monochromatic coverage verified, including old H embedding'
out={'status':'independent five-label union capture bridge verified','allowed_K_labels':sorted(S),'initial_nodes':initial_nodes,'initial_max_unmarked_depth':initial_max,'total_nodes':nodes,'max_unmarked_depth':maximum,'raw_returns':len(mac),'marker_compatible_four_paths_tested_without_prefix_pruning':tested,'physically_feasible_four_histories':len(hist),'history_vertices':len(V),'component_sizes':list(map(len,groups)),'component_internal_edges':edgecounts,'component_K_label_sets':labelsets,'full_contracted_DAG_vertices':n,'seconds':time.time()-start,'theorem':'For every finite ant seed, capture iff only finitely many K events have labels outside this five-element set. This does not prove universal finiteness of the residual events.','manifest_sha256':hashlib.sha256((P/'five_label_union_manifest.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
