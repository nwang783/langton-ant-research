"""Independent current-color marker trees, history cover, and staged graph binding."""
import json,hashlib,time
from pathlib import Path
from collections import defaultdict,deque,Counter
ROOT=Path('/workspace/shared/langton');P=ROOT/'word_stabilization';AUD=ROOT/'audits'
manifest=json.loads((P/'staged_two_cell_singletons_manifest.json').read_text())
for f,h in manifest['files'].items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h,f
W=json.loads((ROOT/'computability/singleton_first_block_input.json').read_text())['word']
assert hashlib.sha256(W.encode()).hexdigest()=='9772fa0cced75fab3a1d336c6a1326e0e4be8f4e471a3807e0778fccc94c1f04'
F={(W+W)[i:i+10] for i in range(104)};assert len(F)==84
D=(1j,1,-1j,-1)
def literal(w):
 p=0j;h=0;colors={};vis=[]
 for c in w:
  b=c=='L'
  if p in colors and colors[p]!=b:return None
  colors[p]=not b;vis.append((p,h,c));h=(h+(3 if b else 1))%4;p+=D[h]
 return vis,p,h

def dags(vertices,edges,groups):
 ix={v:i for i,g in enumerate(groups) for v in g};n=len(groups)
 for v in vertices-ix.keys():ix[v]=n;n+=1
 adj=[[] for _ in range(n)];deg=[0]*n
 for u,v in edges:
  a,b=ix[u],ix[v]
  if a==b and a<len(groups):continue
  adj[a].append(b);deg[b]+=1
 Q=deque(i for i,x in enumerate(deg) if not x);seen=0
 while Q:
  a=Q.popleft();seen+=1
  for b in adj[a]:
   deg[b]-=1
   if not deg[b]:Q.append(b)
 assert seen==n
 return n

def cycles(vertices,edges):
 adj={v:[] for v in vertices};rev={v:[] for v in vertices}
 for a,b in edges:adj[a].append(b);rev[b].append(a)
 seen=set();order=[]
 def dfs(v):
  seen.add(v)
  for w in adj[v]:
   if w not in seen:dfs(w)
  order.append(v)
 for v in vertices:
  if v not in seen:dfs(v)
 seen=set();groups=[]
 def back(v,g):
  seen.add(v);g.add(v)
  for w in rev[v]:
   if w not in seen:back(w,g)
 for v in reversed(order):
  if v not in seen:
   g=set();back(v,g)
   if len(g)>1 or (v,v) in edges:groups.append(g)
 return sorted(groups,key=lambda g:(-len(g),min(g)))

def wordsets(q):
 rows=q['macro_words'];out=defaultdict(list)
 for a,k,b in q['quotient_edges']:out[a].append((k,b))
 paths={2:set(),3:set()}
 for a in out:
  for x,b in out[a]:
   for y,c in out[b]:
    if literal(rows[x]['word']+rows[y]['word']+rows[y]['end_marker']):paths[2].add((x,y))
    for z,d in out[c]:
     if literal(rows[x]['word']+rows[y]['word']+rows[z]['word']+rows[z]['end_marker']):paths[3].add((x,y,z))
 return paths

replay=json.loads((AUD/'staged_singleton_clause_replay_manifest.json').read_text())
assert replay['status']=='PASS all five independent literal clause checks'
assert replay['checker_sha256']==hashlib.sha256((AUD/'check_literal_spatial_clauses.cpp').read_bytes()).hexdigest()
for record in replay['records']:
 for f,h in record['hashes'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h,f
replay_by_stem={z['stem']:z for z in replay['records']}
reports=[]
for label in ['LRRLRRRRLRL','RRRLRLLRRRR']:
 t0=time.time();lower=label.lower();stem='direct_mono_'+lower
 markers={'LLLLRLRRRRLR','RRRLLRLLRRRR','L'+label,'R'+label};board={};nodes=maximum=hits=0;ret=set()
 def grow(w,p,h,prev,start=None):
  global nodes,maximum,hits
  nodes+=1;maximum=max(maximum,len(w));assert len(w)<200
  old=board.get(p)
  for b,c in [(True,'L'),(False,'R')]:
   if old is not None and old!=b:continue
   nw=w+c;bad=len(nw)>=10 and nw[-10:] not in F
   if prev and bad and nw[-11:]!=label:continue
   board[p]=not b;nh=(h+(3 if b else 1))%4;np=p+D[nh]
   if len(nw)>=12 and nw[-12:] in markers:
    if start:ret.add((start,nw[-12:],nw[:-12]))
    else:hits+=1
   else:grow(nw,np,nh,bad,start)
   if old is None:board.pop(p,None)
   else:board[p]=old
 grow('',0j,0,False);initial=nodes
 for m in sorted(markers):
  board.clear();p=0j;h=0;prev=False;w='';ok=True
  for c in m:
   b=c=='L';w+=c;bad=len(w)>=10 and w[-10:] not in F
   if (p in board and board[p]!=b) or (bad and prev and w[-11:]!=label):ok=False;break
   board[p]=not b;h=(h+(3 if b else 1))%4;p+=D[h];prev=bad
  if ok:grow(m,p,h,prev,m)
 assert ret=={tuple(s.split()) for s in (P/(stem+'.returns.tsv')).read_text().splitlines()}
 mac=sorted(ret,key=lambda z:(len(z[2]),z[2],z[0],z[1]));assert all(w and (w+b).startswith(a) for a,b,w in mac)
 succ={i:[j for j in range(len(mac)) if mac[i][1]==mac[j][0]] for i in range(len(mac))};hist=set()
 def four(ids,body):
  if ids and not literal(body+mac[ids[-1]][1]):return
  if len(ids)==4:hist.add(tuple(ids));return
  for a in (range(len(mac)) if not ids else succ[ids[-1]]):four(ids+[a],body+mac[a][2])
 four([],'');snap='staged_two_cell_snapshots/'+lower
 saved=json.loads((P/(snap+'_history4_words.json')).read_text());assert set(map(tuple,saved['words']))==hist
 assert [(r['start_marker'],r['end_marker'],r['word']) for r in saved['macro_words']]==mac
 V={w[:-1] for w in hist}|{w[1:] for w in hist};edge={(w[:-1],w[1:]) for w in hist}
 q=json.loads((P/(snap+'_history4_scc0_port_quotient.json')).read_text());old=json.loads((P/(stem+'_history4_scc0_port_quotient.json')).read_text())
 assert all(q[k]==v for k,v in old.items() if k!='scope')
 hs=list(map(tuple,q['history_states']));group=set(hs);assert len(hs)==len(group) and group<=V
 contracted=dags(V,edge,[group]);ii={v:i for i,v in enumerate(hs)};local=q['source_return_ids'];li={v:i for i,v in enumerate(local)}
 assert [(r['start_marker'],r['end_marker'],r['word']) for r in q['macro_words']]==[mac[i] for i in local]
 internal={(ii[w[:-1]],li[w[-1]],ii[w[1:]]) for w in hist if w[:-1] in group and w[1:] in group}
 assert internal==set(map(tuple,q['history_edges']));cls=q['history_state_classes']
 assert {(cls[a],b,cls[c]) for a,b,c in internal}==set(map(tuple,q['quotient_edges']))
 assert set(cls)==set(range(q['classes']))
 paths=wordsets(q);contexts=sorted(paths[2]);idx={z:i for i,z in enumerate(contexts)}
 base=stem+'_history4_scc0_context2';ctx=json.loads((P/(base+'_port_quotient.json')).read_text());raw=q['macro_words']
 expected=[dict(word=raw[a]['word'],end_marker=raw[b]['word']+raw[b]['end_marker'],context=[a,b],start_marker=raw[a]['start_marker']) for a,b in contexts]
 assert ctx['macro_words']==expected
 assert set(map(tuple,ctx['quotient_edges']))=={(idx[(a,b)],idx[(a,b)],idx[(b,c)]) for a,b,c in paths[3]}
 stages=[];i=0;current=ctx;currentstem=base;terminal=[]
 while True:
  data=json.loads((AUD/f'check_staged_{lower}_{i}.json').read_text());assert data['status'].startswith('PASS')
  assert data==replay_by_stem[currentstem]['results']
  rr=current['macro_words'];ee=current['quotient_edges']
  expected_literal='\n'.join([str(len(rr))]+[z['word']+' '+z['end_marker'] for z in rr]+[str(len(ee))]+[f'{a} {c}' for a,b,c in ee])+'\n'
  assert (AUD/(currentstem+'_literal.txt')).read_text()==expected_literal
  markfile=P/(currentstem+('_selected_marks.tsv' if i==0 else '_raw_marks.tsv'));marks={int(row.split()[0]) for row in markfile.read_text().splitlines()}
  assert len(marks)==data['raw_marks'];rows=current['macro_words'];E=set(map(tuple,current['quotient_edges']));assert all(a==b for a,b,c in E)
  potential={(a,c) for a,b,c in E};allowed={e for e in potential if literal(rows[e[0]]['word']+rows[e[1]]['word']+rows[e[1]]['end_marker'])}
  g=json.loads((P/(currentstem+'_grammar.json')).read_text());assert set(map(tuple,g['pairs']))<=allowed
  assert data['pairs']==len(allowed)
  # Auditor uses this possibly larger graph for all pruning, never author's SCC list.
  remain=set(range(len(rows)))-marks;newedges={(a,b) for a,b in allowed if a in remain and b in remain};components=cycles(remain,newedges)
  stages.append({'contexts':len(rows),'clauses':data['clauses'],'marks':len(marks),'recurrent_sizes':[len(c) for c in components]})
  nextstem=currentstem+'_residual0';nextfile=P/(nextstem+'_port_quotient.json')
  if nextfile.exists():
   nxt=json.loads(nextfile.read_text());kept=nxt['kept_context_types'];assert set(kept) in components
   for c in components:
    if c!=set(kept):terminal.append((rows,c,allowed))
   ren={v:k for k,v in enumerate(kept)}
   for z,v in zip(nxt['macro_words'],kept):
    assert all(z[k]==rows[v][k] for k in ['word','end_marker','start_marker','context']) and z['old_context_type']==v
   assert set(map(tuple,nxt['quotient_edges']))=={(ren[a],ren[a],ren[b]) for a,b in allowed if a in ren and b in ren}
   current=nxt;currentstem=nextstem;i+=1
  else:
   terminal.extend((rows,c,allowed) for c in components);break
 tailreports=[]
 for rows,c,allowed in terminal:
  internal={(a,b) for a,b in allowed if a in c and b in c};assert all(sum(a==v for a,b in internal)==1 and sum(b==v for a,b in internal)==1 for v in c)
  v=min(c);seq=[]
  while v not in seq:seq.append(v);v=next(b for a,b in internal if a==v)
  assert v==seq[0] and set(seq)==c;word=''.join(rows[a]['word'] for a in seq)
  pose=literal(word);assert pose and pose[2]==0 and pose[1]
  if len(word)==104 and word in W+W:
   tailreports.append({'kind':'standard104','cycle':seq,'phase':(W+W).index(word)});continue
  dx,dy=int(pose[1].real),int(pose[1].imag);classes=defaultdict(list)
  for j,(z,h,c0) in enumerate(pose[0]):
   x,y=int(z.real),int(z.imag)
   if dx:rem=x%abs(dx);key=(dx*y-dy*x,rem);epoch=(x-rem)//dx
   else:rem=y%abs(dy);key=(x,rem);epoch=(y-rem)//dy
   classes[key].append((j-len(word)*epoch,c0))
  firstL=0
  for row in classes.values():
   row.sort();assert all(a[1]!=b[1] for a,b in zip(row,row[1:]));firstL+=row[0][1]=='L'
  assert firstL>0
  tailreports.append({'kind':'infinite_first_L_fuel','word':word,'length':len(word),'drift':[dx,dy],'first_L_classes':firstL})
 reports.append({'label':label,'initial_nodes':initial,'total_nodes':nodes,'max_depth':maximum,'returns':len(mac),'history_words':len(hist),'history_vertices':len(V),'recurrent_histories':len(group),'contracted_DAG_vertices':contracted,'stages':stages,'terminal_cycles':tailreports,'seconds':time.time()-t0})
 print('PASS',label,reports[-1],flush=True)
out={'status':'PASS independent end-to-end staged singleton capture proofs','claims':'Two separate singleton-label statements; their union is NOT proved.','reports':reports,'manifest_sha256':hashlib.sha256((P/'staged_two_cell_singletons_manifest.json').read_bytes()).hexdigest(),'clause_replay_manifest_sha256':hashlib.sha256((AUD/'staged_singleton_clause_replay_manifest.json').read_bytes()).hexdigest(),'cpp_checker_sha256':hashlib.sha256((AUD/'check_literal_spatial_clauses.cpp').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
