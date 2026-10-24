import sys,json,collections,pathlib
p=pathlib.Path(sys.argv[1]);d=json.load(open(p));N=d['states'];G=[[]for _ in range(N)];R=[[]for _ in range(N)]
for e in d['graph_edges']:G[e[0]].append(e[1]);R[e[1]].append(e[0])
seen=bytearray(N);order=[]
for root in range(N):
 if seen[root]:continue
 stack=[(root,False)]
 while stack:
  v,done=stack.pop()
  if done:order.append(v);continue
  if seen[v]:continue
  seen[v]=1;stack.append((v,True));stack.extend((w,False)for w in G[v]if not seen[w])
comp=[-1]*N;ss=[]
for root in reversed(order):
 if comp[root]>=0:continue
 c=len(ss);stack=[root];S=[];comp[root]=c
 while stack:
  v=stack.pop();S.append(v)
  for w in R[v]:
   if comp[w]<0:comp[w]=c;stack.append(w)
 ss.append(S)
cyc=[S for S in ss if len(S)>1];selfs=[e for e in d['graph_edges']if e[0]==e[1]]
print('scc',len(cyc),sorted(map(len,cyc),reverse=True)[:20],'self',len(selfs))
internal=[e for e in d['graph_edges']if comp[e[0]]==comp[e[1]]];print('internal edges',len(internal),'deltas',collections.Counter(e[4] for e in internal))
json.dump(dict(scc_sizes=sorted(map(len,cyc),reverse=True),self_edges=selfs,cyclic_components=cyc,internal_edges=internal),open(str(p).replace('.json','_cycles.json'),'w'))
