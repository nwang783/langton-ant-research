"""Exact finite macro-history overapproximation of first-marker-return paths.
All paths are current-read feasible with actual final marker. No long-path
feasibility is inferred. Every genuine infinite marked trace yields a path.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,sys,time

prefix=sys.argv[1];k=int(sys.argv[2]);start=time.time()
M=[{'start_marker':a,'end_marker':b,'word':w}for a,b,w in (l.split()for l in Path(prefix+'.returns.tsv').read_text().splitlines())]
M.sort(key=lambda x:(len(x['word']),x['word'],x['start_marker'],x['end_marker']))
D=(1j,1,-1j,-1)
def feasible(ids):
 p=0j;h=0;last={}
 for c in ''.join(M[a]['word']for a in ids)+M[ids[-1]]['end_marker']:
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return True
succ={a:[b for b in range(len(M))if M[a]['end_marker']==M[b]['start_marker']]for a in range(len(M))}
words=[(a,)for a in range(len(M))if feasible((a,))]
for n in range(2,k+1):
 words=[w+(b,)for w in words for b in succ[w[-1]]if feasible(w+(b,))]
 print('depth',n,'words',len(words),'seconds',round(time.time()-start,3),flush=True)
 if len(words)>3000000:raise RuntimeError('history-size cap; incomplete')
V=sorted({w[:-1]for w in words}|{w[1:]for w in words});vi={w:i for i,w in enumerate(V)};E={(vi[w[:-1]],vi[w[1:]])for w in words};A=[[]for _ in V];B=[[]for _ in V]
for u,v in E:A[u].append(v);B[v].append(u)
seen=set();order=[]
for r in range(len(V)):
 if r in seen:continue
 stack=[(r,False)]
 while stack:
  u,done=stack.pop()
  if done:order.append(u);continue
  if u in seen:continue
  seen.add(u);stack.append((u,True));stack.extend((v,False)for v in A[u]if v not in seen)
seen=set();comps=[]
for r in reversed(order):
 if r in seen:continue
 stack=[r];cs=set();seen.add(r)
 while stack:
  u=stack.pop();cs.add(u)
  for v in B[u]:
   if v not in seen:seen.add(v);stack.append(v)
 if len(cs)>1 or(r,r)in E:comps.append({V[u]for u in cs})
comps.sort(key=lambda s:(len(s),sorted(s)))
print('vertices',len(V),'edges',len(E),'cyclic components',len(comps),flush=True)
allout=[]
for i,s in enumerate(comps):
 ids={w:j for j,w in enumerate(sorted(s))};edges=sorted({(ids[w[:-1]],w[-1],ids[w[1:]])for w in words if w[:-1]in s and w[1:]in s});types=sorted({a for u,a,v in edges});tm={a:j for j,a in enumerate(types)}
 A=defaultdict(list)
 for u,a,v in edges:A[u].append((tm[a],v))
 cl=[0]*len(ids)
 while True:
  sig=[tuple(sorted(set((a,cl[v])for a,v in A[u])))for u in range(len(ids))];si={a:j for j,a in enumerate(sorted(set(sig)))};nc=[si[a]for a in sig]
  if len(set(cl))==len(si):cl=nc;break
  cl=nc
 qe=sorted({(cl[u],tm[a],cl[v])for u,a,v in edges});out={'macro_words':[M[a]for a in types],'quotient_edges':qe,'classes':len(si),'source_return_ids':types,'history_depth':k,'history_states':[list(w)for w in sorted(s)],'history_state_classes':cl,'history_edges':[(u,tm[a],v)for u,a,v in edges],'scope':'finite physical macro-history overapproximation; no claimed149-history equivalence'}
 name=f'{prefix}_history{k}_scc{i}';Path(name+'_port_quotient.json').write_text(json.dumps(out,indent=2));allout.append({'prefix':name,'states':len(s),'edges':len(edges),'types':len(types),'classes':len(si),'quotient_edges':len(qe),'words':[M[a]['word']for a in types]})
 print('SCC',i,'states',len(s),'edges',len(edges),'types',len(types),'classes',len(si),'qedges',len(qe),'lengths',Counter(len(M[a]['word'])for a in types),flush=True)
Path(f'{prefix}_history{k}_words.json').write_text(json.dumps({'macro_words':M,'history_depth':k,'words':words},separators=(',',':')))
Path(f'{prefix}_history{k}_summary.json').write_text(json.dumps({'vertices':len(V),'edges':len(E),'components':allout},indent=2))
