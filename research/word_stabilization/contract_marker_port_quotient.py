from pathlib import Path
from collections import defaultdict,deque
import json,sys
base,out,marker=sys.argv[1:4];q=json.load(open(base+'_port_quotient.json'));M=q['macro_words'];A=defaultdict(list)
for u,a,v in q['quotient_edges']:A[u].append((a,v))
markers={u:{M[a]['start_marker']for a,v in z}for u,z in A.items()};assert all(len(s)==1 for s in markers.values())
ports={u for u,s in markers.items()if marker in s};other=set(A)-ports;deg={u:0 for u in other}
for u in other:
 for a,v in A[u]:
  if v in other:deg[v]+=1
queue=deque(u for u in other if not deg[u]);seen=[]
while queue:
 u=queue.popleft();seen.append(u)
 for a,v in A[u]:
  if v in other:
   deg[v]-=1
   if deg[v]==0:queue.append(v)
assert len(seen)==len(other),'non-port cycle needs separate treatment'
E=[];raw=set()
for u in ports:
 stack=[(v,(a,))for a,v in A[u]]
 while stack:
  v,path=stack.pop()
  if v in ports:
   word=''.join(M[a]['word']for a in path);raw.add(word);E.append((u,word,v))
  else:
   for a,z in A[v]:stack.append((z,path+(a,)))
words=sorted(raw,key=lambda s:(len(s),s));wi={s:i for i,s in enumerate(words)};pi={u:i for i,u in enumerate(sorted(ports))};adj=[[]for _ in ports]
for u,w,v in E:adj[pi[u]].append((wi[w],pi[v]))
cl=[0]*len(ports)
while True:
 sig=[tuple(sorted(set((a,cl[v])for a,v in z)))for z in adj];si={s:i for i,s in enumerate(sorted(set(sig)))};nc=[si[s]for s in sig]
 if len(set(cl))==len(si):cl=nc;break
 cl=nc
edges=sorted({(cl[pi[u]],wi[w],cl[pi[v]])for u,w,v in E});res={'source':base,'marker':marker,'source_port_states':sorted(ports),'source_state_classes':cl,'macro_words':[{'word':w,'start_marker':marker,'end_marker':marker}for w in words],'quotient_edges':edges,'classes':len(si),'scope':'first returns to selected marker in supplied finite presentation'}
Path(out+'_port_quotient.json').write_text(json.dumps(res,indent=2));print('port states',len(ports),'nonports',len(other),'packets',len(words),'classes',len(si),'edges',len(edges));print([(i,len(w),w)for i,w in enumerate(words)])
