from pathlib import Path
p=Path('/workspace/shared/langton/word_stabilization/bdd_macro_colored_ports_trap.py');s=p.read_text();a=s.index('F=dict(initial);queue=');s=s[:a]+'''# Backward closure of the SAME finite overapproximation used by the forward
# checker. The forward source cubes are now the accepting last-R states.
SOURCE=initial
RC={c:[] for c in contexts}
for (c,k),to in CT.items():RC[to].append((c,k))
REV={}
for head in heads:
 for k in ALPHA:
  pre=[]
  if head[0]=='OUT':
   for oldh in range(4):
    if zero[oldh,k][1][2]==head[1]:pre.append((('OUT',oldh),1,0))
   for ph in inside:
    to,g,odd,touch=T[ph,k]
    if to==head and not touch:pre.append((ph,g,odd))
  else:
   a,b,h=head
   for oldh in range(4):
    _,(da,db,eh)=zero[oldh,k]
    if eh!=h:continue
    ph=(a-da,b-db,oldh)
    if ph in HS:
     to,g,odd,touch=T[ph,k];assert to==head
     if not touch:pre.append((ph,g,odd))
    else:
     assert head in BOUND[oldh,k]
     pre.append((('OUT',oldh),1,0))
  REV[head,k]=pre
F={}
target_guard=T[(0,0,0),TARGET][1]
for c in contexts:
 if (c,TARGET) in CT:
  root=bb.intersect(target_guard,color_guard((0,0,0),c))
  if root:F[((0,0,0),c)]=root
queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1
 if bb.intersect(F[key],SOURCE.get(key,0)):
  print('ABSTRACT WITNESS BACKWARD',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);break
 if len(bb.nodes)>100000 and iters%100==0:
  before=len(bb.nodes);roots=list(F.values())+list(SOURCE.values())+list(G.values())+[x[1] for x in T.values()]
  mp=bb.collect(roots)
  F={h:mp[v] for h,v in F.items()};SOURCE={h:mp[v] for h,v in SOURCE.items()};G={h:mp[v] for h,v in G.items()}
  T={hk:(to,mp[g],odd,t) for hk,(to,g,odd,t) in T.items()}
  REV={hk:[(ph,mp[g],odd) for ph,g,odd in prev] for hk,prev in REV.items()}
  print('GC',iters,before,'->',len(bb.nodes),'elapsed',round(time.time()-t0,1),flush=True)
  if len(bb.nodes)>LIMIT:print('LIVE NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 for pc,k in RC[ctx]:
  for ph,guard,odd in REV[head,k]:
   root=bb.intersect(bb.flip(F[key],odd),guard)
   root=bb.intersect(root,color_guard(ph,pc))
   if not root:continue
   pkey=(ph,pc);old=F.get(pkey,0);new=bb.union(old,root)
   if new!=old:
    F[pkey]=new
    if pkey not in queued:queued.add(pkey);queue.append(pkey)
else:print('EXCLUDED BACKWARD',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
''';p.with_name('bdd_macro_backward_ports.py').write_text(s)
